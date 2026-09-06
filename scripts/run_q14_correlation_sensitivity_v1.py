import argparse,json
from pathlib import Path
from dynamics_atlas_harness import q14_correlation_sensitivity_v1 as q

def main():
 p=argparse.ArgumentParser()
 for name in ['source','main','admission','output']:p.add_argument('--'+name,type=Path,required=True)
 a=p.parse_args()
 if a.output.exists():raise FileExistsError(a.output)
 source=json.loads(a.source.read_text());main=json.loads(a.main.read_text());receipt=json.loads(a.admission.read_text())
 on=q.run(source,main,receipt);off=q.run(source,main,receipt,False)
 a.output.mkdir()
 for name,value in [('before',on['before']),('after',on['after']),('evidence',on['evidence']),('off',off)]:
  (a.output/(name+'.json')).write_text(json.dumps(value,indent=2,allow_nan=False)+'\n')
 r=dict(on_operator_calls=on['operator_calls'],off_operator_calls=off['operator_calls'],same_instance=on['before']['rule_instance_id']==on['after']['rule_instance_id'],full_question_answer=False)
 (a.output/'receipt.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(dict(**r,actual_sd_bounds=on['evidence']['delta_sd_bounds']),indent=2))
if __name__=='__main__':main()
