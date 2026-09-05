"""Run the Q16 developmental obligation on locally admitted observed curves."""
import argparse
import json
from pathlib import Path
from dynamics_atlas_harness.q16_common_window_v1 import POLICY,run

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--source-curves',type=Path,required=True);ap.add_argument('--output-dir',type=Path,required=True);args=ap.parse_args()
 source=json.loads(args.source_curves.read_text());pairs={}
 for pair,conditions in [('29',['eg50_1mM','eg50_10mM','eg0_1mM','eg25_1mM','gly25_1mM']),('36',['eg50_1mM','eg50_10mM','eg0_1mM'])]:
  pairs[pair]={}
  for condition in conditions:
   sheet='SI Figure9' if condition=='eg50_10mM' else 'SI Figure10'
   key=sheet+':'+pair+'_'+condition;record=source[key]
   pairs[pair][condition]=dict(source_block=key,role='AUTHOR_DEPOSITED_OBSERVED_DEER_TRACES',raw=record['raw'],processed=[r[:2] for r in record['processed']])
 payload=dict(doi='10.1038/s41467-022-31945-6',policy=POLICY,pairs=pairs)
 # No author fit column, inverse distribution or state assignment enters payload.
 on=run(payload);off=run(payload,False)
 args.output_dir.mkdir(exist_ok=False,parents=True)
 for name,obj in [('input.local.json',payload),('rules_before.json',on['before']),('rules_off.json',off),('evidence.json',on['evidence']),('rules_after.json',on['after']),('receipt.json',dict(on_operator_calls=on['operator_calls'],off_operator_calls=off['operator_calls'],deterministic_evidence_verification_passes=1,iterative_fits=0,full_question_answer=False,input_id=on['before']['input_id'],source_curves=str(args.source_curves)))]:
  (args.output_dir/name).write_text(json.dumps(obj,indent=2)+'\n')
 print(json.dumps({p:{'window':r['window_us'],'n':r['n'],'ordering':r['ordering']} for p,r in on['evidence']['results'].items()},indent=2))
if __name__=='__main__':main()
