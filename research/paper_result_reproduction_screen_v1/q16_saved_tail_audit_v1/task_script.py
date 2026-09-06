"""No-fit audit of saved finite-grid witnesses and same-record heldout tails."""
import json,argparse
from pathlib import Path
import numpy as np
from unittest.mock import patch
from dynamics_atlas_harness import q16_shape_flexibility_v1 as q

def main():
 p=argparse.ArgumentParser();p.add_argument('--task-root',type=Path,required=True);a=p.parse_args();root=a.task_root/'outputs';out=root/'q16_saved_tail_audit_v1'
 if out.exists():raise FileExistsError(out)
 read=lambda n:json.loads((root/n).read_text())
 payload=read('q16_shape_flexibility_v1/input.local.json');baseline=read('q16_conditional_feasibility_v1/report.json');receipt=read('q16_shape_flexibility_v1/admission_receipt.json');e=read('q16_shape_flexibility_v1/evidence.json')
 # Re-entry consumes evidence; failure stubs make accidental fits a visible error.
 with patch.object(q,'operator',side_effect=AssertionError('NO_NEW_OPERATOR')),patch.object(q,'nnls',side_effect=AssertionError('NO_NEW_NNLS')):
  after=q.evaluate(payload,baseline,receipt,evidence=e)
  boundary=[];tail=[]
  for c in e['candidates']:
   if 'error' in c:continue
   rec=payload['records'][c['record']];metrics=q.audit_candidate(c,*q.arrays(rec));w=np.zeros(len(q.R))
   for i,v in c['grid_weights']:w[i]=v
   mass=w.sum();long=w[q.LONG].sum()
   row=dict(record=c['record'],p=c['p'],k=c['k'],**metrics,total_mass_at_10nm=float(w[-1]/mass) if mass else None,long_mass_at_10nm=float(w[-1]/long) if long else None,total_mass_ge8nm=float(w[q.R>=8].sum()/mass) if mass else None)
   if metrics['conditional_witness']:boundary.append(row)
   if 'cropped' not in c['record']:continue
   full_name=c['record'].replace('raw_cropped','full');full=payload['records'][full_name]
   assert rec['source_key']==full['source_key']
   raw=np.array(rec['raw_time_real_imaginary']);rawfull=np.array(full['raw_time_real_imaginary']);assert np.array_equal(rawfull[:len(raw)],raw)
   held=rawfull[len(raw):];assert len(held) and np.all(held[:,0]>raw[-1,0])
   pred=np.exp(-c['k']*held[:,0])*(c['unmodulated_amplitude']+q.kernel(held[:,0])@w);res=pred-held[:,1]
   rms=float(np.sqrt(np.mean(res**2)));lag=float(np.corrcoef(res[:-1],res[1:])[0,1])
   tail.append(dict(**row,full_record=full_name,source_key=rec['source_key'],heldout_n=len(held),heldout_start=float(held[0,0]),heldout_end=float(held[-1,0]),heldout_rms=rms,heldout_mean_residual=float(res.mean()),heldout_lag1=lag,heldout_rms_over_training_noise=rms/metrics['noise_proxy'],passes_same_descriptive_screen=bool(rms<=2*metrics['noise_proxy'] and abs(lag)<=.2),prediction=pred.tolist()))
  # Independent sparse sum of production weights: checks predictive assembly, not physics.
  c=next(c for c in e['candidates'] if 'error' not in c);t=np.array([0.,4.928,6.88]);K=q.kernel(t)
  direct=np.array([np.exp(-c['k']*x)*(c['unmodulated_amplitude']+sum(v*K[j,i] for i,v in c['grid_weights'])) for j,x in enumerate(t)])
  w=np.zeros(len(q.R))
  for i,v in c['grid_weights']:w[i]=v
  err=float(np.max(np.abs(direct-np.exp(-c['k']*t)*(c['unmodulated_amplitude']+K@w))));assert err<1e-12
 summary={}
 for name in sorted({x['record'] for x in tail}):
  rows=[x for x in tail if x['record']==name and x['conditional_witness']]
  summary[name]=dict(training_witnesses=len(rows),tail_pass_same_screen=sum(x['passes_same_descriptive_screen'] for x in rows),rms_range=[min(x['heldout_rms'] for x in rows),max(x['heldout_rms'] for x in rows)],by_p={str(p):dict(n=sum(x['p']==p for x in rows),tail_pass=sum(x['p']==p and x['passes_same_descriptive_screen'] for x in rows)) for p in sorted({x['p'] for x in rows},key=lambda x:-1 if x is None else x)})
 result=dict(status='SAVED_WITNESS_BOUNDARY_AND_SAME_RECORD_TAIL',witnesses=boundary,tail_candidates=tail,summary=summary,new_fits=0,new_operators=0,independent_sum_error=err,limits=['Tail belongs to same EG record, never actual noEG.','Frozen descriptive RMS/lag1 screen is not validated independent-noise inference or a confidence region.','Mass at upper grid boundary is a conditional tail/background decomposition, not resolved open-state population.','No grid expansion or parameter refit; failed witnesses do not exclude whole model families.'])
 out.mkdir();(out/'report.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');(out/'saved_evidence_reassessment.json').write_text(json.dumps(after,indent=2)+'\n');print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
