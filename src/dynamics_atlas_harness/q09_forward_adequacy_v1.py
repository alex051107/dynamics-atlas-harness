"""One Q09 diagnostic obligation, actual numerical evidence and bounded reassessment."""
from __future__ import annotations
import hashlib
import json
import time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from .q09_fluorescence_v1 import PQPair, poisson_deviance
from .rules_prototype_v1 import rule_instance_id

REPO=Path(__file__).resolve().parents[2]
RULE_ID='Q09R01_CASE_FORWARD_ADEQUACY_V1'
OPERATOR_ID='q09_donor_instrument_diagnostic_v1'
CONFIG={'version':'Q09_DONOR_INSTRUMENT_DIAGNOSTIC_V1','variant':'22-127','donor_components':[2,3],'FRET_components':2,
 'candidate_donor_initials':[[.2,1.,4.,.2,.4],[.5,2.,5.,.4,.5],[.1,3.,7.,.1,.7],[1.,4.,8.,.6,.3]],
 'joint_fret_initials':[[35.,65.,.5,.1],[50.,85.,.8,.2],[30.,100.,.2,.05],[65.,40.,.5,.1]],
 'profile_f0':[.4,.6,.8],'maxiter':1500,'max_seconds':120,'physical_gradient_tolerance':1e-6,
 'source_model_form':'PublishedSI21_Table2a_three_donor_terms;author_fit_values_excluded',
 'instrument':'native8ps;separateIRF;tail256median;scatter0;all6100bins;noLin;nonperiodic',
 'IRF_audit_regions':'first256_and_last256_descriptive_no_pure_background_assertion',
 'claim_ceiling':'ConditionalmodeldependenceandIRFdiagnostic;noabsoluteadequacyorstate-numberdecision'}
D3_BOUNDS=[(.05,10.)]*3+[(0.,1.)]*2+[(1e-12,.05),(-5.,5.)]
J3_BOUNDS=[(.05,10.)]*3+[(0.,1.)]*2+[(10.,120.)]*2+[(0.,1.)]*2+[(1e-12,.05),(-5.,5.),(1e-12,.05),(-5.,5.)]


def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()


def _input_identity(data):
    h=hashlib.sha256()
    # Semantic identity includes role names, not dictionary insertion order.
    arrays=[('time',data.t)]
    for field in ('y','irf'):
        mapping=getattr(data,field)
        if set(mapping)!={'D0','DA'}:raise ValueError('EXACT_DA_D0_ROLES_REQUIRED')
        arrays.extend((field+':'+role,mapping[role]) for role in ('D0','DA'))
    arrays.extend(zip(('lin','mask','r','qweights','rates','transfer_exp'),(data.lin,data.mask,data.r,data.qweights,data.rates,data.transfer_exp)))
    for name,a in arrays:
        h.update(name.encode());h.update(str(a.shape).encode());h.update(a.dtype.str.encode());h.update(a.tobytes())
    h.update(json.dumps({'dt':data.dt,'baseline':data.baseline,'source_identity':data.source_identity},sort_keys=True,allow_nan=False).encode())
    return h.hexdigest()


def load_inputs(root):
    root=Path(root);raw=(root/'eTCSPC_wildtype.zip').read_bytes()
    if hashlib.md5(raw).hexdigest()!='177132ce5bb9fefde871bafe8c92cbfd':raise ValueError('AUTHOR_ARCHIVE_IDENTITY_MISMATCH')
    data=PQPair(root)
    summary=json.loads((REPO/'research/paper_result_reproduction_screen_v1/q09_pq_joint_v3/summary.json').read_text())
    data.baseline=summary['best_joint']['parameters']
    data.source_identity={'archive_md5':'177132ce5bb9fefde871bafe8c92cbfd','variant':'22-127','baseline_head':'3dc3d77fab096ab4d05613839e323af931d9d27a','baseline_file':'q09_pq_joint_v3/summary.json'}
    data.input_id=_input_identity(data)
    for a in [data.t,*data.y.values(),*data.irf.values(),data.lin,data.mask,data.r,data.qweights,data.rates,data.transfer_exp]:a.flags.writeable=False
    return data


def verify_data(data):
    if _input_identity(data)!=data.input_id:raise ValueError('ADMITTED_INPUT_CHANGED')


def amplitudes(u,v):return [u,(1-u)*v,(1-u)*(1-v)]


def d3_counts(data,p):
    t1,t2,t3,u,v,bg,shift=p
    intrinsic=data.intrinsic_donor([t1,t2,t3],amplitudes(u,v))
    return {'D0':data.counts('D0',intrinsic,bg,shift)}


def j3_counts(data,p):
    t1,t2,t3,u,v,r1,r2,x,f0,bg0,s0,bga,sa=p
    d0,da=data.intrinsic_pair([t1,t2,t3],amplitudes(u,v),[r1,r2],[x,1-x],f0)
    return {'D0':data.counts('D0',d0,bg0,s0),'DA':data.counts('DA',da,bga,sa)}


def summarize(data,predictions):
    result={}
    for role,mu in predictions.items():
        y=data.y[role];blocks=[]
        for ix in np.array_split(np.arange(len(y)),20):
            Y=float(y[ix].sum());M=float(mu[ix].sum())
            blocks.append({'first_bin':int(ix[0]),'last_bin':int(ix[-1]),'observed':Y,'expected':M,'scaled_residual':float((Y-M)/np.sqrt(M))})
        result[role]={'deviance':poisson_deviance(y,mu),'expected_total':float(mu.sum()),'observed_total':float(y.sum()),'blocks':blocks}
    return result


def irf_audit(data):
    # This PQ reference has observedtail median0; admitted irf is therefore raw.
    result={}
    for role,a in data.irf.items():
        if data.irf_baseline[role]!=0:raise ValueError('THIS_DIAGNOSTIC_REQUIRES_RETAINED_RAW_PQ_IRF')
        result[role]={'total':float(a.sum()),'regions':{}}
        for name,sl in [('first256',slice(0,256)),('last256',slice(-256,None))]:
            v=a[sl];result[role]['regions'][name]={'sum':float(v.sum()),'mean':float(v.mean()),'median':float(np.median(v)),'zero_fraction':float(np.mean(v==0))}
    return result


def gradient_at(p,bounds,objective):
    lo=np.array([b[0] for b in bounds]);span=np.array([b[1]-b[0] for b in bounds]);z=(np.asarray(p)-lo)/span;gz=[]
    for i in range(len(z)):
        h=1e-5*max(abs(z[i]),.001);plus=z.copy();minus=z.copy();plus[i]=min(1,z[i]+h);minus[i]=max(0,z[i]-h)
        gz.append((objective(lo+span*plus)-objective(lo+span*minus))/(plus[i]-minus[i]))
    gp=np.array(gz)/span
    for i,(low,high) in enumerate(bounds):
        if (p[i]<=low+1e-7 and gp[i]>0) or (p[i]>=high-1e-7 and gp[i]<0):gp[i]=0
    return gp


def optimize(initial,bounds,objective,label):
    start=time.monotonic();lo=np.array([b[0] for b in bounds]);span=np.array([b[1]-b[0] for b in bounds])
    def fun(z):
        if time.monotonic()-start>CONFIG['max_seconds']:raise TimeoutError('120S_PRESPECIFIED_STOP')
        return objective(lo+span*z)
    def jac(z):
        values=[]
        for i in range(len(z)):
            h=1e-5*max(abs(z[i]),.001);a=z.copy();b=z.copy();a[i]=min(1,z[i]+h);b[i]=max(0,z[i]-h)
            values.append((fun(a)-fun(b))/(a[i]-b[i]))
        return np.array(values)
    try:
        fit=minimize(fun,(np.asarray(initial)-lo)/span,jac=jac,method='L-BFGS-B',bounds=[(0.,1.)]*len(initial),options={'maxiter':CONFIG['maxiter'],'maxfun':20000,'ftol':1e-15,'gtol':1e-11})
        p=lo+span*fit.x;g=np.asarray(fit.jac)/span
        for i,(low,high) in enumerate(bounds):
            if (p[i]<=low+1e-7 and g[i]>0) or (p[i]>=high-1e-7 and g[i]<0):g[i]=0
        pg=float(max(abs(g)))
        return {'label':label,'initial':initial,'parameters':p.tolist(),'objective':float(fit.fun),'optimizer_success':bool(fit.success),'message':str(fit.message),'iterations':int(fit.nit),'evaluations':int(fit.nfev),'projected_gradient_inf':pg,'numerical_status':'PASS' if fit.success and pg<=CONFIG['physical_gradient_tolerance'] else 'UNRESOLVED','elapsed_seconds':time.monotonic()-start,'bound_hits':[i for i,(l,h) in enumerate(bounds) if min(abs(p[i]-l),abs(p[i]-h))<1e-5]}
    except TimeoutError as e:return {'label':label,'initial':initial,'numerical_status':'TIME_BUDGET_STOP','message':str(e),'elapsed_seconds':time.monotonic()-start}


def _validate_graph(graph):
    packet=json.loads((REPO/'evidence/paper_blind_exposed_v1/public/q09_public_fact_packet_v1.json').read_text());a=packet['platform_authority_envelope']['rules_projection_authority']
    if graph['case']['scientific_claim']!=a['case']['scientific_claim']:raise ValueError('Q09_CLAIM_MISMATCH')
    if {v['source_id']:v['evidence_role'] for v in graph.get('evidence_items',[])}!=a['source_evidence_roles'] or len(graph.get('evidence_items',[]))!=3:raise ValueError('Q09_SOURCE_SET_MISMATCH')
    keys=['comparison_id','left_source_id','right_source_id','relation_type']
    if sorted(tuple(x.get(k) for k in keys) for x in graph.get('comparisons',[]))!=sorted(tuple(x.get(k) for k in keys) for x in a['comparisons']):raise ValueError('Q09_COMPARISON_MISMATCH')


def evaluate_forward_rule(graph,data=None,evidence=None,*,enabled=True,calibration_evidence=None):
    case=graph['case'];instance=rule_instance_id(RULE_ID,'CASE',case['case_id'])
    result={'rule_instance_id':instance,'runtime_subrule_id':RULE_ID,'target':{'kind':'CASE','id':case['case_id']},'status':'UNRESOLVED','obligations':[],'reason_codes':[],'complete_question_answer':False,'state_number_verdict':'UNRESOLVED'}
    rule=json.loads((REPO/'registries/rules_v1/q09_forward_adequacy_rule_v1.json').read_text())
    if rule['rule_id']!=RULE_ID or rule['operator_id']!=OPERATOR_ID or rule['scientific_pass_enabled']:raise ValueError('UNSUPPORTED_RULE_VERSION')
    if not enabled or case['case_id']!=rule['case_id'] or case['requested_claim_level']!=rule['trigger_claim_level']:
        result.update(status='NOT_APPLICABLE',reason_codes=['RULE_DISABLED' if not enabled else 'NO_STATE_NUMBER_REQUEST']);return result
    _validate_graph(graph)
    if data is None:result['reason_codes']=['TYPED_DA_D0_IRF_AND_CURRENT_MODEL_REQUIRED'];return result
    verify_data(data);request=digest({'instance':instance,'graph':graph,'input_id':data.input_id,'config':CONFIG})
    result['request_id']=request
    if evidence is None:
        result['reason_codes']=['FORWARD_MODEL_ADEQUACY_NUMERIC_EVIDENCE_REQUIRED']
        result['obligations']=[{'rule_instance_id':instance,'operator_id':OPERATOR_ID,'request_id':request,'input_id':data.input_id,'purpose':'DONOR_ORDER_AND_INSTRUMENT_DIAGNOSTIC_KEEP_FRET_K2'}];return result
    try:verified=verify_evidence(data,evidence,request)
    except (ValueError,KeyError,TypeError,OverflowError) as error:
        result['reason_codes']=['DIAGNOSTIC_EVIDENCE_REJECTED'];result['rejection_reason']=str(error);return result
    if verified['status']=='NUMERICAL_STOP':
        result.update(reason_codes=['BOUND_NUMERIC_DIAGNOSTIC_RECOMPUTED','DIAGNOSTIC_NUMERICAL_STOP'],diagnostic_status='NUMERICAL_STOP',next_required_evidence='Resolve recorded numerical stop before interpreting donor or state number');return result
    result.update(reason_codes=['BOUND_NUMERIC_DIAGNOSTIC_RECOMPUTED','IRF_UNCERTAINTY_NOT_PROPAGATED','PROTEIN_STATE_NUMBER_NOT_IDENTIFIED'],diagnostic_status=verified['status'],profile_checks=verified['profile_checks'],model_changes=verified['model_changes'],next_required_evidence='Calibration-constrained IRF sensitivity and identifiability;not automatic FRET K3',claim_ceiling='Conditional model dependence only;no scientific state-number support')
    from .q09_calibration_sensitivity_v1 import apply_followup
    return apply_followup(result,data,evidence,calibration_evidence)


def run_diagnostic(data,request_id,checkpoint=None):
    verify_data(data)
    evidence={'schema':'q09-forward-evidence/v1','operator_id':OPERATOR_ID,'request_id':request_id,'input_id':data.input_id,'config':CONFIG,'baseline_parameters':data.baseline,'baseline':summarize(data,data.joint_counts(data.baseline)),'IRF_audit':irf_audit(data),'donor_runs':[],'joint_runs':[],'profile_runs':[],'selected_donor_index':None,'selected_joint_index':None,'candidate':None}
    def record():
        if checkpoint:checkpoint(evidence)
    total=sum(v.sum() for v in data.y.values());dtotal=data.y['D0'].sum()
    def loss_d(p):return poisson_deviance(data.y['D0'],d3_counts(data,p)['D0'])/dtotal
    def loss_j(p):return sum(poisson_deviance(data.y[k],v) for k,v in j3_counts(data,p).items())/total
    record()
    for seed in CONFIG['candidate_donor_initials']:
        r=optimize(seed+[.001,0.],D3_BOUNDS,loss_d,'DONOR3');evidence['donor_runs'].append(r);record()
    accepted=[(i,x) for i,x in enumerate(evidence['donor_runs']) if x['numerical_status']=='PASS']
    if not accepted:return evidence
    i,best=min(accepted,key=lambda x:x[1]['objective']);evidence['selected_donor_index']=i;donor=best['parameters']
    for seed in CONFIG['joint_fret_initials']:
        initial=donor[:5]+seed+[donor[5],donor[6],.001,0.]
        r=optimize(initial,J3_BOUNDS,loss_j,'JOINT_DONOR3_FRET2');evidence['joint_runs'].append(r);record()
    accepted=[(i,x) for i,x in enumerate(evidence['joint_runs']) if x['numerical_status']=='PASS']
    if not accepted:return evidence
    i,best=min(accepted,key=lambda x:x[1]['objective']);evidence['selected_joint_index']=i;parameters=best['parameters'];evidence['candidate']=summarize(data,j3_counts(data,parameters));record()
    reduced_bounds=J3_BOUNDS[:8]+J3_BOUNDS[9:]
    for f0 in CONFIG['profile_f0']:
        def expand(p):return list(p[:8])+[f0]+list(p[8:])
        r=optimize(parameters[:8]+parameters[9:],reduced_bounds,lambda p:loss_j(expand(p)),'FIXED_F0_PROFILE')
        r['fixed_f0']=f0
        if 'parameters' in r:r['full_parameters']=expand(r['parameters'])
        evidence['profile_runs'].append(r);record()
    return evidence


def _compare(actual,expected):
    if isinstance(expected,dict):
        if not isinstance(actual,dict) or set(actual)!=set(expected):raise ValueError('EVIDENCE_FIELDS_MISMATCH')
        for k,v in expected.items():_compare(actual[k],v)
    elif isinstance(expected,list):
        if len(actual)!=len(expected):raise ValueError('EVIDENCE_ARRAY_LENGTH_MISMATCH')
        for a,b in zip(actual,expected):_compare(a,b)
    else:
        if not np.isfinite(actual) or not np.isclose(actual,expected,rtol=1e-8,atol=1e-8):raise ValueError('EVIDENCE_NUMBERS_MISMATCH')


def verify_fit(record,bounds,objective):
    """Recompute every consumable numeric fit; a status/gradient claim cannot admit it."""
    status=record.get('numerical_status')
    if 'parameters' not in record:
        if status!='TIME_BUDGET_STOP':raise ValueError('MISSING_FIT_PARAMETERS')
        return {'status':'NUMERICAL_STOP','reason':'TIME_BUDGET_STOP'}
    p=np.asarray(record['parameters'],dtype=float)
    if p.shape!=(len(bounds),) or not np.all(np.isfinite(p)) or any(v<lo or v>hi for v,(lo,hi) in zip(p,bounds)):raise ValueError('OUT_OF_BOUNDS_EVIDENCE_PARAMETERS')
    value=float(objective(p));_compare(record['objective'],value)
    pg=float(max(abs(gradient_at(p,bounds,objective))))
    _compare(record['projected_gradient_inf'],pg)
    if status not in ('PASS','UNRESOLVED'):raise ValueError('INVALID_NUMERICAL_STATUS')
    passed=record.get('optimizer_success') is True and np.isfinite(pg) and pg<=CONFIG['physical_gradient_tolerance']
    if (status=='PASS')!=passed:raise ValueError('FIT_STATUS_NOT_NUMERICALLY_VERIFIED')
    return {'status':'VERIFIED' if passed else 'NUMERICAL_STOP','objective':value,'projected_gradient_inf':pg}


def verify_evidence(data,e,request_id):
    verify_data(data)
    keys={'schema','operator_id','request_id','input_id','config','baseline_parameters','baseline','IRF_audit','donor_runs','joint_runs','profile_runs','selected_donor_index','selected_joint_index','candidate'}
    if set(e)!=keys or e['schema']!='q09-forward-evidence/v1' or e['operator_id']!=OPERATOR_ID or e['request_id']!=request_id or e['input_id']!=data.input_id or e['config']!=CONFIG or e['baseline_parameters']!=data.baseline:raise ValueError('EVIDENCE_REQUEST_OR_METHOD_MISMATCH')
    if len(e['donor_runs'])!=4 or len(e['joint_runs']) not in (0,4) or len(e['profile_runs'])>3:raise ValueError('INCOMPLETE_DECLARED_DIAGNOSTIC_RUNS')
    for i,r in enumerate(e['donor_runs']):
        if r['initial']!=CONFIG['candidate_donor_initials'][i]+[.001,0.]:raise ValueError('UNDECLARED_DONOR_START')
    if e['selected_joint_index'] is not None and e['selected_donor_index'] is None:raise ValueError('JOINT_WITHOUT_DONOR_DIAGNOSTIC')
    if e['selected_joint_index'] is None and e['profile_runs']:raise ValueError('PROFILE_WITHOUT_JOINT')
    _compare(e['baseline'],summarize(data,data.joint_counts(data.baseline)));_compare(e['IRF_audit'],irf_audit(data))
    total=sum(v.sum() for v in data.y.values());dtotal=data.y['D0'].sum()
    selected={}
    for name,bounds,counts,N,indexfield in [('donor_runs',D3_BOUNDS,d3_counts,dtotal,'selected_donor_index'),('joint_runs',J3_BOUNDS,j3_counts,total,'selected_joint_index')]:
        objective=lambda q:sum(poisson_deviance(data.y[k],v) for k,v in counts(data,q).items())/N
        validated=[]
        for i,r in enumerate(e[name]):
            if name=='joint_runs':
                if 'donor_runs' not in selected:raise ValueError('JOINT_WITHOUT_VERIFIED_DONOR')
                donor=selected['donor_runs']['parameters']
                initial=donor[:5]+CONFIG['joint_fret_initials'][i]+[donor[5],donor[6],.001,0.]
                if r['initial']!=initial:raise ValueError('UNDECLARED_JOINT_START')
            check=verify_fit(r,bounds,objective)
            if check['status']=='VERIFIED':validated.append((i,check['objective']))
        index=e[indexfield]
        if index is not None:
            if type(index) is not int or index not in [x[0] for x in validated]:raise ValueError('SELECTED_FIT_NOT_NUMERICALLY_VERIFIED')
            chosen=next(v for i,v in validated if i==index)
            if chosen>min(v for i,v in validated)+1e-12:raise ValueError('SELECTED_FIT_NOT_LOWEST_VERIFIED_OBJECTIVE')
            selected[name]=e[name][index]
        elif validated:raise ValueError('VERIFIED_FIT_NOT_SELECTED')
    if 'joint_runs' not in selected:
        if e['candidate'] is not None:raise ValueError('CANDIDATE_WITHOUT_ACCEPTED_JOINT')
        return {'status':'NUMERICAL_STOP','model_changes':{},'profile_checks':[]}
    best=selected['joint_runs']['parameters']
    _compare(e['candidate'],summarize(data,j3_counts(data,best)))
    profile_checks=[]
    for index,f0 in enumerate(CONFIG['profile_f0']):
        check={'fixed_f0':f0,'status':'NOT_RUN'}
        if index<len(e['profile_runs']):
            r=e['profile_runs'][index]
            try:
                if r.get('fixed_f0')!=f0 or r.get('initial')!=best[:8]+best[9:]:raise ValueError('PROFILE_BINDING_MISMATCH')
                if 'parameters' in r:
                    p=r['parameters'];full=r['full_parameters']
                    if full!=p[:8]+[f0]+p[8:]:raise ValueError('PROFILE_FULL_PARAMETERS_MISMATCH')
                objective=lambda p:sum(poisson_deviance(data.y[k],v) for k,v in j3_counts(data,list(p[:8])+[f0]+list(p[8:])).items())/total
                check.update(verify_fit(r,J3_BOUNDS[:8]+J3_BOUNDS[9:],objective))
            except (ValueError,KeyError,TypeError,IndexError,OverflowError) as error:
                check.update(status='REJECTED',reason=str(error))
        profile_checks.append(check)
    changes={role:{'prior_deviance':e['baseline'][role]['deviance'],'candidate_deviance':e['candidate'][role]['deviance'],'change':e['candidate'][role]['deviance']-e['baseline'][role]['deviance']} for role in ('D0','DA')}
    return {'status':'CALCULATED_WITH_UNRESOLVED_CALIBRATION_AND_IDENTIFIABILITY','model_changes':changes,'profile_checks':profile_checks}


def dispatch_obligation(result,data,graph,checkpoint=None):
    if not result['obligations']:return None
    expected=evaluate_forward_rule(graph,data)
    if result!=expected:raise ValueError('INVALID_DIAGNOSTIC_OBLIGATION')
    return run_diagnostic(data,result['request_id'],checkpoint)
