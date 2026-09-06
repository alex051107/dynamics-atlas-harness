"""Run one Q16 finite-shape obligation against explicitly admitted prior inputs."""
import argparse
import json
from pathlib import Path
from dynamics_atlas_harness.q16_shape_flexibility_v1 import run

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--input',type=Path,required=True)
    parser.add_argument('--baseline',type=Path,required=True)
    parser.add_argument('--admission',type=Path,required=True)
    parser.add_argument('--output-dir',type=Path,required=True)
    args=parser.parse_args()
    if args.output_dir.exists():
        raise FileExistsError('Preserve existing scientific results; choose a new output directory')
    payload=json.loads(args.input.read_text())
    baseline=json.loads(args.baseline.read_text())
    prior=json.loads(args.admission.read_text())
    off=run(payload,baseline,prior,False)
    on=run(payload,baseline,prior)
    args.output_dir.mkdir(parents=True,exist_ok=False)
    for name,value in [('before',on['before']),('after',on['after']),('evidence',on['evidence']),('rules_off',off)]:
        (args.output_dir/(name+'.json')).write_text(json.dumps(value,indent=2,allow_nan=False)+'\n')
    receipt=dict(on_operator_calls=on['operator_calls'],off_operator_calls=off['operator_calls'],
        input_id=on['before']['input_id'],same_instance=on['before']['rule_instance_id']==on['after']['rule_instance_id'],
        full_question_answer=False)
    (args.output_dir/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))

if __name__=='__main__':main()
