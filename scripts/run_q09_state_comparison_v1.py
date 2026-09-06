from pathlib import Path
import argparse,json
from dynamics_atlas_harness import q09_state_comparison_v1 as q

def main():
    p=argparse.ArgumentParser();p.add_argument('--input-root',type=Path,required=True);p.add_argument('--graph',type=Path,required=True);p.add_argument('--output-dir',type=Path,required=True);a=p.parse_args();a.output_dir.mkdir(exist_ok=False)
    def save(n,v):(a.output_dir/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n')
    d=q.load_inputs(a.input_root);g=json.loads(a.graph.read_text());save('source_admission.json',d.audit);save('case_graph.json',g)
    before=q.evaluate(g,d);off=q.evaluate(g,d,enabled=False);save('rule_before.json',before);save('rule_off.json',off);assert q.dispatch(off,d,g) is None
    def checkpoint(e):
        save('evidence.json',e);print(json.dumps({'profiles':len(e['profile_runs']),'refinement':e['shared2_refinement'],'K3':len(e['K3_runs'])},ensure_ascii=False),flush=True)
    e=q.dispatch(before,d,g,checkpoint);save('evidence.json',e);after=q.evaluate(g,d,e);save('rule_after.json',after);print(json.dumps(after,indent=2),flush=True)
    save('receipt.json',{'operator_calls':1,'off_calls':0,'optimizer_calls':len(e['profile_runs'])+int(e['shared2_refinement'] is not None)+len(e['K3_runs']),'same_instance':before['rule_instance_id']==after['rule_instance_id'],'complete_question_answer':False,'source_input_id':d.input_id})
if __name__=='__main__':main()
