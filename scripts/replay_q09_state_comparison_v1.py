from pathlib import Path
import argparse,json
from dynamics_atlas_harness import q09_state_comparison_v1 as q

def main():
    p=argparse.ArgumentParser();p.add_argument('--input-root',type=Path,required=True);p.add_argument('--evidence-dir',type=Path,required=True);p.add_argument('--output-dir',type=Path,required=True);a=p.parse_args();a.output_dir.mkdir(exist_ok=False)
    d=q.load_inputs(a.input_root);g=json.loads((a.evidence_dir/'case_graph.json').read_text());e=json.loads((a.evidence_dir/'evidence.json').read_text());r=q.evaluate(g,d,e)
    if 'BOUND_SHARED_LOCAL_COMPARISON_RECOMPUTED' not in r['reason_codes']:raise ValueError(r)
    (a.output_dir/'rule_after.json').write_text(json.dumps(r,indent=2)+'\n');(a.output_dir/'receipt.json').write_text(json.dumps({'status':'COMPARISON_NUMERIC_EVIDENCE_REPLAYED','optimizer_calls':0,'original_optimizer_calls':13,'off_calls':0,'same_instance':r['rule_instance_id']==json.loads((a.evidence_dir/'rule_before.json').read_text())['rule_instance_id'],'full_question_answer':False},indent=2)+'\n')
    print(json.dumps({k:v for k,v in r['comparison'].items() if k!='profile_checks'},indent=2))
if __name__=='__main__':main()
