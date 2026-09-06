"""One real source group, identical method: forward/gradient parity and timing."""
import functools,json,time
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import numpy as np
from dynamics_atlas_harness import q09_global_comparison_v1 as a
from dynamics_atlas_harness.q09_cached_group_v2 import CachedGroup
T=Path(__file__).resolve().parents[1];O=T/'outputs/q09_cached_group_v2'
def save(n,v):(O/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n')
def main():
 O.mkdir(exist_ok=False);d=a.GlobalData(T/'inputs/q09_author');base=next(g for g in d.groups if g.ref=='D0_01');g=a.Group(base.ref,base.owners,base.records,3);c=CachedGroup(base.ref,base.owners,base.records,3)
 e=json.loads((T/'outputs/q09_donor_order_groups_v2/evidence.json').read_text());runs=e['groups']['D0_01']['runs'];chosen=min((r for r in runs if r['numerical_status']=='PASS'),key=lambda r:r['objective']);p=chosen['parameters']
 padded=functools.partial(a.expected_counts,shift_policy='padded_linear_v2');delta=[]
 for kind in ['local2','shared2','shared3']:
  point=p if kind=='local2' else g.from_local(p,kind);pop=[.2,.5,.3] if kind=='shared3' else [.35,.65]
  for i in range(len(point)):
   pp=point.copy();lo,hi=g.bounds(kind)[i];pp[i]=max(lo,min(hi,pp[i]+1e-5*(hi-lo)))
   with patch.object(a,'expected_counts',padded):original=g.predict(pp,kind,pop)
   cached=c.predict(pp,kind,pop)
   for role in original:
    rel=float(np.max(abs(cached[role]-original[role]))/np.max(original[role]));assert rel<2e-12
    delta.append({'model':kind,'parameter_index':i,'role':role,'max_relative_count_delta':rel})
 j=a.Joint(SimpleNamespace(groups=[g],total=g.total),'shared3');jc=a.Joint(SimpleNamespace(groups=[c],total=c.total),'shared3');pg=g.from_local(p,'shared3')+[.2,.625];z=(pg-j.lo)/j.span
 timings={};grads={};c.cache.clear()
 for mode,model in [('uncached',j),('cached',jc)]:
  for temperature in ['cold','warm']:
   model.cache.clear();start=time.perf_counter()
   if mode=='uncached':
    with patch.object(a,'expected_counts',padded):gradient=model.jac_scaled(z)
   else:gradient=model.jac_scaled(z)
   timings[mode+'_'+temperature]=time.perf_counter()-start;grads[mode+'_'+temperature]=gradient
 difference=float(np.max(abs(grads['uncached_cold']-grads['cached_cold'])));assert difference<2e-7
 with patch.object(a,'expected_counts',padded):obj=j.objective(pg)
 objc=jc.objective(pg);assert abs(obj-objc)<1e-11
 save('prediction_checks.json',delta);save('gradient_checks.json',{k:v.tolist() for k,v in grads.items()})
 receipt={'status':'PASS_SAME_METHOD_FORWARD_OBJECTIVE_GRADIENT','reference':base.ref,'owners':base.owners,'donor_components':3,'source_input_id':d.input_id,'IRF_policy':'padded_linear_v2','model_for_gradient':'shared3','max_relative_count_delta':max(x['max_relative_count_delta'] for x in delta),'max_scaled_gradient_delta':difference,'objective_delta':objc-obj,'timings_seconds':timings,'cold_speed_ratio':timings['uncached_cold']/timings['cached_cold'],'warm_speed_ratio':timings['uncached_warm']/timings['cached_warm'],'cache_entries':len(c.cache),'cache_hits':c.hits,'cache_misses':c.misses,'optimizer_calls':0,'global_convergence_claimed':False,'timing_scope':'Onegradient pertemperature andimplementation;localmicrobenchmarknotall33speedguarantee'};save('receipt.json',receipt);print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()
