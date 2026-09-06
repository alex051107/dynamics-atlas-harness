"""Bounded calibration-only IRF response hypotheses and executable Q09 follow-up.

Conditional Poisson calibration realizations keep sample counts fixed. They are
sensitivity experiments, not a joint sampling confidence interval or clean-IRF
estimator. Nonnegative grouped MLEs can retain positive finite-sample tail bias.
"""
from __future__ import annotations
import copy
import numpy as np
from scipy.signal import fftconvolve
from . import q09_forward_adequacy_v1 as q

OPERATOR_ID='q09_calibration_sensitivity_v1'
CONFIG={'version':'q09-calibration-sensitivity/v1','hypotheses':['compact_3_7ns','adaptive_full_axis'],
        'edge_bins':256,'support_ns':[3.,7.],'group_target_photons':256,'group_max_bins':128,
        'replicate_seeds':[91001,91002,91003,91004],'branch_seeds':[[20.,60.,.5],[40.,80.,.8]],
        'fixed_branch_f0':.8,'scatter_fraction':0.,'calibration_model':'independent Poisson(response + constant background)',
        'grouping':'original IRF only; fixed at 3ns/7ns boundaries; max(mean-background,0)',
        'sample_counts':'unchanged DA and D0; each calibration role sampled once per realization',
        'claim_ceiling':'conditional finite sensitivity; no joint confidence interval, global optimum or protein-state verdict'}


def groups(data,role):
    y=data.irf[role];cuts=sorted(set([0,len(y),int(np.searchsorted(data.t,3)),int(np.searchsorted(data.t,7))]));out=[]
    for left,right in zip(cuts,cuts[1:]):
        start=left;count=0.
        for i in range(left,right):
            count+=y[i]
            if count>=CONFIG['group_target_photons'] or i-start+1>=CONFIG['group_max_bins'] or i==right-1:
                out.append((start,i+1));start=i+1;count=0.
    return out


def response(data,role,observed,hypothesis):
    a=np.asarray(observed,float)
    if a.shape!=data.t.shape or np.any(a<0) or not np.all(np.isfinite(a)):raise ValueError('INVALID_CALIBRATION_REALIZATION')
    n=min(CONFIG['edge_bins'],len(a)//2)
    if n==0:raise ValueError('NO_CALIBRATION_EDGES')
    background=float(np.r_[a[:n],a[-n:]].mean());h=np.zeros_like(a)
    for left,right in groups(data,role):
        if hypothesis=='compact_3_7ns' and not (3<=data.t[left]<7):continue
        h[left:right]=max(float(a[left:right].mean())-background,0.)
    if h.sum()<=0:raise ValueError('EMPTY_CALIBRATED_RESPONSE')
    mean=h+background
    return h,{'background':background,'response_total':float(h.sum()),'outside_3_7_response':float(h[(data.t<3)|(data.t>=7)].sum()),
              'calibration_deviance':q.poisson_deviance(a,mean),'groups':len(groups(data,role)),
              'realization_id':q.digest(a.tolist()),'response_id':q.digest(h.tolist())}


def calibrated_data(data,hypothesis,seed=None):
    if hypothesis not in CONFIG['hypotheses']:raise ValueError('UNDECLARED_CALIBRATION_HYPOTHESIS')
    out=copy.copy(data);out.irf={};stats={};rng=np.random.default_rng(seed) if seed is not None else None
    for role in ('D0','DA'):
        original=data.irf[role];h,st=response(data,role,original,hypothesis)
        sample=original if rng is None else rng.poisson(h+st['background'])
        out.irf[role],stats[role]=response(data,role,sample,hypothesis)
    return out,stats


def objective(data,p):
    return sum(q.poisson_deviance(data.y[k],v) for k,v in q.j3_counts(data,p).items())/sum(v.sum() for v in data.y.values())


def geometry(data,p):
    """Finite-window photon shares and local weighted shape geometry, not resolution."""
    amps=q.amplitudes(*p[3:5]);donor=data.intrinsic_donor(p[:3],amps)
    latent=[p[8]*donor]
    for R,pop in zip(p[5:7],[p[7],1-p[7]]):
        _,quenched=data.intrinsic_pair(p[:3],amps,[R],[1.],0.)
        latent.append((1-p[8])*pop*quenched)
    integrals=np.array([f.sum()*data.dt for f in latent]);shares=integrals/integrals.sum()
    axis=np.arange(len(data.t));irf=np.interp(axis-p[12],axis,data.irf['DA'],left=0,right=0);irf/=irf.sum()
    convolved=[np.maximum(fftconvolve(f,irf)[:len(irf)],0) for f in latent]
    detected=np.array([f.sum() for f in convolved]);detected/=detected.sum()
    fast=1+int(np.argmin(p[5:7]));conv=convolved[fast]/convolved[fast].sum()
    contrast=conv-irf
    base=q.j3_counts(data,p)['DA'];prob=base/base.sum();weight=1/np.sqrt(np.maximum(prob,1e-15))
    columns=[]
    for i,step in [(12,1e-3),(11,1e-7),(8,1e-5)]:
        a=np.array(p);b=np.array(p);a[i]+=step;b[i]-=step
        lo,hi=q.J3_BOUNDS[i];a[i]=min(hi,a[i]);b[i]=max(lo,b[i])
        pa=q.j3_counts(data,a)['DA'];pb=q.j3_counts(data,b)['DA']
        columns.append((pa/pa.sum()-pb/pb.sum())/(a[i]-b[i]))
    A=np.stack(columns,axis=1)*weight[:,None];c=contrast*weight
    # Normalize columns for a stable nuisance-span projection; coefficients are
    # geometric and are not a fitted/independently constrained scatter fraction.
    norms=np.linalg.norm(A,axis=0);A=A/np.where(norms>0,norms,1.)
    coef,_,rank,_=np.linalg.lstsq(A,c,rcond=1e-10);res=c-A@coef
    return {'latent_finite_window_fluorescence_shares':shares.tolist(),'convolved_finite_window_fluorescence_shares':detected.tolist(),'fast_component_index':fast,
            'distance_means_A':list(p[5:7]),'fast_scatter_cosine':float(conv@irf/np.linalg.norm(conv)/np.linalg.norm(irf)),
            'fast_scatter_total_variation':float(abs(contrast).sum()/2),
            'weighted_contrast_norm':float(np.linalg.norm(c)),
            'weighted_contrast_remaining_fraction':float(np.linalg.norm(res)/np.linalg.norm(c)),
            'nuisance_projection_rank':int(rank),'shift_ps':float(p[12]*data.dt*1000),
            'sample_photons_DA':float(data.y['DA'].sum()),'fast_component_photons_before_background':float(detected[fast]*(1-p[11])*data.y['DA'].sum())}


def request_id(base_evidence):return q.digest({'base_evidence':base_evidence,'config':CONFIG})


def gaps(data,base_evidence):
    p=base_evidence['joint_runs'][base_evidence['selected_joint_index']]['parameters']
    edge=any(v['mean']>0 and v['median']==0 for a in q.irf_audit(data).values() for v in a['regions'].values())
    rate=.224*(2/3)*(56.4/min(p[5:7]))**6
    return {'IRF_edge_signal_unrepresented_by_median':bool(edge),'fast_transfer_time_ns':float(1/rate),
            'fast_transfer_relative_to_two_bins':bool(1/rate<2*data.dt)}


def apply_followup(result,data,base_evidence,calibration_evidence=None):
    gap=gaps(data,base_evidence);result['numeric_gap_assessment']=gap
    result['local_forward_status']='CALIBRATION_SENSITIVITY_REQUIRED'
    profile_complete=all(x['status']=='VERIFIED' for x in result['profile_checks'])
    result['profile_branch_status']='VERIFIED_LOCAL_STATIONARY_POINTS' if profile_complete else 'INCOMPLETE'
    if not gap['IRF_edge_signal_unrepresented_by_median'] and not gap['fast_transfer_relative_to_two_bins']:
        result.update(local_forward_status='NO_DECLARED_CALIBRATION_GAP',next_required_evidence='Global shared/local state comparison and structure evidence');return result
    rid=request_id(base_evidence)
    pending={'rule_instance_id':result['rule_instance_id'],'operator_id':OPERATOR_ID,'request_id':rid,'input_id':data.input_id,
             'purpose':'CALIBRATION_ONLY_IRF_AND_FAST_COMPONENT_SENSITIVITY'}
    result['calibration_request_id']=rid
    if calibration_evidence is None:
        result['obligations']=[pending];return result
    try:verified=verify_evidence(data,base_evidence,calibration_evidence)
    except (ValueError,KeyError,TypeError,IndexError,OverflowError) as err:
        result['reason_codes'].append('CALIBRATION_EVIDENCE_REJECTED');result['calibration_rejection_reason']=str(err);result['obligations']=[pending];return result
    result['calibration_assessment']=verified
    result['reason_codes']=[v for v in result['reason_codes'] if v!='IRF_UNCERTAINTY_NOT_PROPAGATED']+['BOUND_CALIBRATION_SENSITIVITY_RECOMPUTED']
    complete=verified['all_calibration_fits_verified']
    result['local_forward_status']='CONDITIONAL_SENSITIVITY_ASSESSED_WITH_LIMITS' if complete else 'PARTIAL_SENSITIVITY_WITH_NUMERICAL_STOPS'
    result['next_required_evidence']='Conditional global shared/local comparison and structure evidence; retain calibration assumptions and incomplete profile branches'
    return result


def run(data,base_evidence,checkpoint=None):
    q.verify_data(data);p=base_evidence['joint_runs'][base_evidence['selected_joint_index']]['parameters']
    e={'schema':CONFIG['version'],'operator_id':OPERATOR_ID,'request_id':request_id(base_evidence),'input_id':data.input_id,
       'config':CONFIG,'numpy_version':np.__version__,'calibration_runs':[],'branch_runs':[],
       'base_geometry':geometry(data,p),'base_parameters':p}
    def record():
        if checkpoint:checkpoint(e)
    for hypothesis in CONFIG['hypotheses']:
        mean_p=p
        for seed in [None]+CONFIG['replicate_seeds']:
            d,stats=calibrated_data(data,hypothesis,seed)
            r=q.optimize(list(mean_p),q.J3_BOUNDS,lambda x:objective(d,x),'CALIBRATION_JOINT')
            item={'hypothesis':hypothesis,'seed':seed,'calibration':stats,'fit':r}
            if 'parameters' in r:item['geometry']=geometry(d,r['parameters']);item['summary']=q.summarize(d,q.j3_counts(d,r['parameters']))
            e['calibration_runs'].append(item);record()
            if seed is None and r['numerical_status']=='PASS':mean_p=r['parameters']
    for seed in CONFIG['branch_seeds']:
        initial=list(p);initial[5:8]=seed;initial[8]=CONFIG['fixed_branch_f0']
        def expand(x):return list(x[:8])+[CONFIG['fixed_branch_f0']]+list(x[8:])
        r=q.optimize(initial[:8]+initial[9:],q.J3_BOUNDS[:8]+q.J3_BOUNDS[9:],lambda x:objective(data,expand(x)),'FIXED_F0_BRANCH')
        if 'parameters' in r:r['full_parameters']=expand(r['parameters'])
        e['branch_runs'].append(r);record()
    return e


def verify_evidence(data,base,e):
    q.verify_data(data)
    if e['schema']!=CONFIG['version'] or e['operator_id']!=OPERATOR_ID or e['config']!=CONFIG or e['request_id']!=request_id(base) or e['input_id']!=data.input_id:raise ValueError('CALIBRATION_BINDING_MISMATCH')
    if e['numpy_version']!=np.__version__:raise ValueError('REPLAY_CALIBRATION_RNG_VERSION_MISMATCH')
    p=base['joint_runs'][base['selected_joint_index']]['parameters']
    if e['base_parameters']!=p:raise ValueError('CALIBRATION_BASE_FIT_MISMATCH')
    q._compare(e['base_geometry'],geometry(data,p))
    if len(e['calibration_runs'])!=10 or len(e['branch_runs'])!=2:raise ValueError('INCOMPLETE_CALIBRATION_BUDGET')
    checks=[];accepted=[];i=0
    for hypothesis in CONFIG['hypotheses']:
        mean_p=p
        for seed in [None]+CONFIG['replicate_seeds']:
            item=e['calibration_runs'][i];i+=1
            if item['hypothesis']!=hypothesis or item['seed']!=seed:raise ValueError('UNDECLARED_CALIBRATION_RUN')
            d,stats=calibrated_data(data,hypothesis,seed)
            if item['calibration']!=stats:raise ValueError('CALIBRATION_REALIZATION_NOT_REPRODUCED')
            fit=item['fit']
            if fit['initial']!=mean_p:raise ValueError('UNDECLARED_CALIBRATION_START')
            check=q.verify_fit(fit,q.J3_BOUNDS,lambda x:objective(d,x))
            if 'parameters' in fit:
                q._compare(item['geometry'],geometry(d,fit['parameters']));q._compare(item['summary'],q.summarize(d,q.j3_counts(d,fit['parameters'])))
            checks.append({'hypothesis':hypothesis,'seed':seed,**check})
            if check['status']=='VERIFIED':
                accepted.append({'hypothesis':hypothesis,'seed':seed,'parameters':fit['parameters'],'deviance':sum(v['deviance'] for v in item['summary'].values())})
                if seed is None:mean_p=fit['parameters']
    branch_checks=[]
    for seed,fit in zip(CONFIG['branch_seeds'],e['branch_runs']):
        initial=list(p);initial[5:8]=seed
        if fit['initial']!=initial[:8]+initial[9:]:raise ValueError('UNDECLARED_F0_BRANCH_START')
        def expand(x):return list(x[:8])+[CONFIG['fixed_branch_f0']]+list(x[8:])
        if 'parameters' in fit and fit['full_parameters']!=expand(fit['parameters']):raise ValueError('FIXED_F0_BRANCH_BINDING_MISMATCH')
        branch_checks.append(q.verify_fit(fit,q.J3_BOUNDS[:8]+q.J3_BOUNDS[9:],lambda x:objective(data,expand(x))))
    return {'all_calibration_fits_verified':all(x['status']=='VERIFIED' for x in checks),'calibration_fit_checks':checks,'branch_checks':branch_checks,
            'accepted_conditional_fits':accepted,'interpretation':'Finite calibration sensitivity with sample counts fixed; profile points are existence witnesses, not global exclusion or joint confidence intervals'}


def dispatch(result,data,graph,base_evidence,checkpoint=None):
    if not result['obligations']:return None
    expected=q.evaluate_forward_rule(graph,data,base_evidence)
    if result!=expected:raise ValueError('INVALID_CALIBRATION_OBLIGATION')
    if not result['obligations']:return None
    if len(result['obligations'])!=1 or result['obligations'][0]['operator_id']!=OPERATOR_ID:raise ValueError('WRONG_CALIBRATION_OPERATOR')
    return run(data,base_evidence,checkpoint)
