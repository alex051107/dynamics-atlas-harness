"""Recompute saved Q09 predictions and evidence without any optimization history."""
from pathlib import Path
import argparse,csv,json
from dynamics_atlas_harness import q09_forward_adequacy_v1 as q


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--input-root',type=Path,required=True);p.add_argument('--evidence-dir',type=Path,required=True);p.add_argument('--output-dir',type=Path,required=True);args=p.parse_args()
    args.output_dir.mkdir(parents=True,exist_ok=False)
    data=q.load_inputs(args.input_root);e=json.loads((args.evidence_dir/'evidence.json').read_text());g=json.loads((args.evidence_dir/'case_graph.json').read_text())
    result=q.evaluate_forward_rule(g,data,e)
    if 'DIAGNOSTIC_EVIDENCE_REJECTED' in result['reason_codes']:raise ValueError(result['rejection_reason'])
    predictions={'prior_'+k:v for k,v in data.joint_counts(data.baseline).items()}
    if e['selected_joint_index'] is not None:predictions.update({'candidate_'+k:v for k,v in q.j3_counts(data,e['joint_runs'][e['selected_joint_index']]['parameters']).items()})
    with (args.output_dir/'predictions.csv').open('w') as f:
        w=csv.writer(f);w.writerow(['bin0','time_ns','D0_observed','DA_observed']+list(predictions))
        for i,t in enumerate(data.t):w.writerow([i,t,int(data.y['D0'][i]),int(data.y['DA'][i])]+[v[i] for v in predictions.values()])
    (args.output_dir/'reassessment.json').write_text(json.dumps(result,indent=2)+'\n')
    (args.output_dir/'receipt.json').write_text(json.dumps({'status':'SAVED_NUMERIC_EVIDENCE_RECOMPUTED','input_id':data.input_id,'optimizer_calls':0,'historical_failed_runners_executed':0,'same_rule_instance':result['rule_instance_id']},indent=2)+'\n')
    print(json.dumps({'status':'SAVED_NUMERIC_EVIDENCE_RECOMPUTED','optimizer_calls':0,'rule_status':result['status']}))
if __name__=='__main__':main()
