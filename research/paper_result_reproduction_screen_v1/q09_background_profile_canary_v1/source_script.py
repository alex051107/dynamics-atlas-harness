"""Exact pre-Lin background reparameterization; manual numerical canary."""
from pathlib import Path
import json,time,datetime
import numpy as np
from scipy.signal import fftconvolve
from scipy.optimize import brentq
from dynamics_atlas_harness import q09_global_comparison_v1 as a
from dynamics_atlas_harness.q09_cached_group_v2 import CachedGroup
T=Path(__file__).resolve().parents[1];O=T/'outputs/q09_background_profile_canary_v1'
POLICY={'version':'q09-background-profile-canary/v1','source_method':'padded_linear_v2;mix beforeLin and finalmasknormalization',
        'background_bounds':[1e-12,.05],'count_parity_backgrounds':[0.,.001,.05],
        'count_relative_tolerance':1e-12,'gradient_atol':2e-8,'gradient_rtol':.001,
        'root_xtol':1e-15,'root_rtol':1e-14,'root_maxiter':100,
        'maximum_scalar_roots':9,'full_fit_optimizer_calls':0,'Rules_controlled':False,
        'official_API':'https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.brentq.html'}

def save(n,v):(O/n).write_text(json.dumps(v,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
def templates(record,intrinsic,shift):
    h=record['irf'];linear=record['Lin'];mask=record['mask'];pad=int(np.ceil(abs(shift)))+1
    shifted=np.interp(np.arange(len(h))-shift,np.arange(-pad,len(h)+pad),np.pad(h,(pad,pad)),left=0,right=0)
    shifted/=shifted.sum();fluorescence=np.maximum(fftconvolve(intrinsic,shifted,mode='full')[:len(h)],0)
    signal=fluorescence/fluorescence[mask].sum()*linear;background=linear/mask.sum()
    U=float(signal[mask].sum());V=float(background[mask].sum())
    return signal/U,background/V,U,V

def main():
    O.mkdir(exist_ok=False);save('policy.json',POLICY);started=time.monotonic()
    data=a.GlobalData(T/'inputs/q09_author');source=json.loads((T/'outputs/q09_targeted_continuation_v1/verified_report.json').read_text())
    result={'policy':POLICY,'input_id':data.input_id,'source_report_id':a.q.digest(source),'points':[],'scalar_root_calls':0}
    prepared=[]
    # Complete every method parity check before any root solve.
    for row in source['runs']:
        original=next(g for g in data.groups if g.ref==row['reference']);g=CachedGroup(original.ref,original.owners,original.records,3)
        p=np.array(row['fit']['parameters']);tau=p[:3];amp=a.q.amplitudes(*p[3:5]);roles=[]
        for role,record in g.records.items():
            if role==g.ref:
                index=5;shift=p[6];intrinsic=record['kernel'].intrinsic_donor(tau,amp)
            else:
                start=7+6*g.owners.index(role);part=p[start:start+6];index=start+4;shift=part[5]
                _,intrinsic=record['kernel'].intrinsic_pair(tau,amp,part[:2],[part[2],1-part[2]],part[3])
            S,B,U,V=templates(record,intrinsic,shift);mask=record['mask'];total=float(record['y'][mask].sum())
            to_w=lambda b: b*V/((1-b)*U+b*V)
            def prediction(b,S=S,B=B,U=U,V=V,total=total):
                z=b*V/((1-b)*U+b*V);return total*((1-z)*S+z*B)
            parity=[]
            for b in POLICY['count_parity_backgrounds']:
                pp=p.copy();pp[index]=b;expected=g.predict(pp,'local2')[role];actual=prediction(b)
                delta=float(np.max(abs(actual-expected))/np.max(expected));parity.append(delta)
                if delta>1e-12:raise ValueError('PROFILE_COUNTS_NOT_SOURCE_EQUIVALENT')
            def derivative_w(z,S=S,B=B,total=total,record=record,mask=mask):
                mu=total*((1-z)*S[mask]+z*B[mask]);return float(2*total*np.sum((B[mask]-S[mask])*(1-record['y'][mask]/mu)))
            b=p[index];analytic=derivative_w(to_w(b))*U*V/((1-b)*U+b*V)**2/g.total
            h=1e-7*max(abs(b),.001)
            finite=(a.poisson_deviance(record['y'][mask],prediction(b+h)[mask])-a.poisson_deviance(record['y'][mask],prediction(b-h)[mask]))/(2*h*g.total)
            if not np.isclose(analytic,finite,atol=2e-8,rtol=.001):raise ValueError('PROFILE_ANALYTIC_GRADIENT_MISMATCH')
            roles.append({'role':role,'index':index,'S':S,'B':B,'U':U,'V':V,'total':total,'mask':mask,'record':record,
                          'derivative':derivative_w,'count_parity':parity,'analytic':analytic,'finite':finite})
        prepared.append((row,g,p,roles))
    save('method_parity.json',{'status':'PASS','roles':[{k:r[k]for k in ['role','index','count_parity','analytic','finite']}for _,_,_,rs in prepared for r in rs],'scalar_roots_started':False})
    for row,g,p,roles in prepared:
        changed=p.copy();updates=[]
        for r in roles:
            U,V=r['U'],r['V'];lo,hi=POLICY['background_bounds'];low=lo*V/((1-lo)*U+lo*V);high=hi*V/((1-hi)*U+hi*V)
            derivative=r['derivative'];dl,dh=derivative(low),derivative(high)
            if dl>=0:z=low;root_status='LOWER_BOUND_MINIMUM';iterations=0
            elif dh<=0:z=high;root_status='UPPER_BOUND_MINIMUM';iterations=0
            else:
                z,receipt=brentq(derivative,low,high,xtol=1e-15,rtol=1e-14,maxiter=100,full_output=True)
                assert receipt.converged;result['scalar_root_calls']+=1;iterations=int(receipt.iterations);root_status='ROOT_CONVERGED'
            b=z*U/(V*(1-z)+z*U);changed[r['index']]=b
            updates.append({'role':r['role'],'parameter_index':r['index'],'original_preLin_background':float(p[r['index']]),
                            'new_preLin_background':float(b),'observed_mixture_weight':float(z),'preLin_signal_normalizer':U,'preLin_uniform_normalizer':V,
                            'root_status':root_status,'iterations':iterations,'objective_derivative_w':derivative(z)})
        fun=lambda p:g.deviance(p,'local2')/g.total
        before=fun(p);after=fun(changed);pg=a.q.gradient_at(changed,g.bounds('local2'),fun)
        assert after<=before+1e-13
        result['points'].append({'reference':g.ref,'parent_candidate_id':row['parent_candidate_id'],'old_status':row['fit']['numerical_status'],
            'parameters_before':p.tolist(),'parameters_after_background_only':changed.tolist(),'role_updates':updates,
            'objective_before':before,'objective_after':after,'deviance_delta':(after-before)*g.total,
            'full_projected_gradient':pg.tolist(),'projected_gradient_inf':float(np.max(abs(pg))),
            'passes_original_gradient_criterion':bool(np.max(abs(pg))<=1e-6),
            'whole_fit_or_scientific_PASS_claimed':False,'manual_method_canary_not_Rules_extra':True})
        save('result.json',result)
        if time.monotonic()-started>120:raise TimeoutError('PROFILE_CANARY_BUDGET')
    result.update(completed_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-started)
    save('result.json',result);print(json.dumps([{k:r[k]for k in ['reference','old_status','deviance_delta','projected_gradient_inf','passes_original_gradient_criterion']}for r in result['points']],indent=2))
if __name__=='__main__':main()
