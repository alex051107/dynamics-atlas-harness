"""Fixed parameter diagnosis; no optimizer, no promoted fitted candidate."""
from pathlib import Path
import json,time,datetime
import numpy as np
from dynamics_atlas_harness import q09_global_comparison_v1 as a
from dynamics_atlas_harness.q09_cached_group_v2 import CachedGroup
T=Path(__file__).resolve().parents[1];O=T/'outputs/q09_fixed_stop_diagnosis_v1'
POLICY={'version':'q09-fixed-stop-diagnosis/v1','gradient_step_multipliers':[.1,1.,10.],
        'normalized_coordinate_probe_steps':[1e-6,1e-5,1e-4,1e-3],
        'IRF_shift':'padded_linear_v2','acceptance_gradient_unchanged':1e-6,
        'optimizer_calls':0,'candidate_promotion':False,'maximum_seconds':120}

def save(n,v):(O/n).write_text(json.dumps(v,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
def gradient(p,bounds,objective,multiplier):
    lo,hi=np.asarray(bounds).T;span=hi-lo;z=(p-lo)/span;grad=[]
    for j in range(len(z)):
        h=multiplier*1e-5*max(abs(z[j]),.001);u=z.copy();v=z.copy();u[j]=min(1,z[j]+h);v[j]=max(0,z[j]-h)
        grad.append((objective(lo+span*u)-objective(lo+span*v))/(span[j]*(u[j]-v[j])))
    grad=np.asarray(grad)
    for j,(lower,upper) in enumerate(bounds):
        if (p[j]<=lower+1e-7 and grad[j]>0)or(p[j]>=upper-1e-7 and grad[j]<0):grad[j]=0
    return grad

def main():
    O.mkdir(exist_ok=False);started=time.monotonic();save('policy.json',POLICY)
    data=a.GlobalData(T/'inputs/q09_author')
    source=json.loads((T/'outputs/q09_targeted_continuation_v1/verified_report.json').read_text())
    out={'policy':POLICY,'source_input_id':data.input_id,'source_report_id':a.q.digest(source),'points':[]}
    for row in source['runs']:
        original=next(g for g in data.groups if g.ref==row['reference']);g=CachedGroup(original.ref,original.owners,original.records,3)
        p=np.asarray(row['fit']['parameters']);bounds=g.bounds('local2');lo,hi=np.asarray(bounds).T;span=hi-lo
        fun=lambda p:g.deviance(p,'local2')/g.total
        actual=fun(p);np.testing.assert_allclose(actual,row['fit']['objective'],rtol=1e-8,atol=1e-11)
        gradients={str(s):gradient(p,bounds,fun,s)for s in POLICY['gradient_step_multipliers']}
        gp=gradients['1.0'];j=int(np.argmax(abs(gp)));direction=-np.sign(gp[j]);probes=[]
        for step in POLICY['normalized_coordinate_probe_steps']:
            target=p.copy();target[j]=np.clip(p[j]+direction*step*span[j],lo[j],hi[j]);v=fun(target)
            probes.append({'normalized_step':step,'parameter_index':j,'parameter_before':float(p[j]),'parameter_probe':float(target[j]),'objective_delta':float(v-actual),'deviance_delta':float((v-actual)*g.total)})
        shifts=[6]+[g.donor_size+6*i+5 for i in range(len(g.owners))]
        names=['tau1_ns','tau2_ns','tau3_ns','donor_stick1','donor_stick2','D0_background','D0_shift']
        for v in g.owners:names += [v+suffix for suffix in ('_R1_A','_R2_A','_population','_f0','_background','_shift')]
        out['points'].append({'reference':g.ref,'parent_candidate_id':row['parent_candidate_id'],'original_status':row['fit']['numerical_status'],
            'objective':actual,'original_termination':row['fit']['message'],'parameter_names':names,
            'gradient_by_step':{k:v.tolist()for k,v in gradients.items()},
            'maximum_projected_gradient_by_step':{k:float(np.max(abs(v)))for k,v in gradients.items()},
            'dominant_parameter':names[j],'dominant_parameter_index':j,'probes':probes,
            'IRF_shifts':[{'index':i,'name':names[i],'value':float(p[i]),'distance_to_integer':float(abs(p[i]-round(p[i])))}for i in shifts],
            'all_bound_distances_normalized':np.minimum((p-lo)/span,(hi-p)/span).tolist()})
        save('result.json',out)
        if time.monotonic()-started>120:raise TimeoutError('FIXED_POINT_AUDIT_BUDGET')
    out.update(completed_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-started)
    save('result.json',out)
    print(json.dumps([{'reference':r['reference'],'status':r['original_status'],'gradients':r['maximum_projected_gradient_by_step'],'dominant':r['dominant_parameter'],'best_probe_deviance_delta':min(x['deviance_delta']for x in r['probes'])}for r in out['points']],indent=2))
if __name__=='__main__':main()
