"""No-optimization replay of original-source-bound calibration sensitivity."""
from pathlib import Path
import argparse,json
from dynamics_atlas_harness import q09_forward_adequacy_v1 as q
from dynamics_atlas_harness import q09_calibration_sensitivity_v1 as c

def main():
    p=argparse.ArgumentParser();p.add_argument('--input-root',type=Path,required=True);p.add_argument('--base-evidence-dir',type=Path,required=True);p.add_argument('--evidence',type=Path,required=True);p.add_argument('--output-dir',type=Path,required=True);a=p.parse_args();a.output_dir.mkdir(parents=True,exist_ok=False)
    d=q.load_inputs(a.input_root);base=json.loads((a.base_evidence_dir/'evidence.json').read_text());g=json.loads((a.base_evidence_dir/'case_graph.json').read_text());e=json.loads(a.evidence.read_text())
    result=q.evaluate_forward_rule(g,d,base,calibration_evidence=e)
    if 'BOUND_CALIBRATION_SENSITIVITY_RECOMPUTED' not in result['reason_codes']:raise ValueError('CALIBRATION_REPLAY_REQUIRES_AFFIRMATIVE_VERIFICATION')
    (a.output_dir/'reassessment.json').write_text(json.dumps(result,indent=2)+'\n')
    (a.output_dir/'receipt.json').write_text(json.dumps({'status':'CALIBRATION_EVIDENCE_RECOMPUTED','optimizer_calls':0,'input_id':d.input_id,'local_forward_status':result['local_forward_status'],'complete_question_answer':False},indent=2)+'\n')
    print(result['local_forward_status'])
if __name__=='__main__':main()
