"""Execute the evidence-derived calibration obligation and reassess same instance."""
from pathlib import Path
import argparse,json
from dynamics_atlas_harness import q09_forward_adequacy_v1 as q
from dynamics_atlas_harness import q09_calibration_sensitivity_v1 as c

def main():
    p=argparse.ArgumentParser();p.add_argument('--input-root',type=Path,required=True);p.add_argument('--base-evidence-dir',type=Path,required=True);p.add_argument('--output-dir',type=Path,required=True);a=p.parse_args();a.output_dir.mkdir(parents=True,exist_ok=False)
    def save(name,obj):(a.output_dir/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False,allow_nan=False)+'\n')
    data=q.load_inputs(a.input_root);base=json.loads((a.base_evidence_dir/'evidence.json').read_text());graph=json.loads((a.base_evidence_dir/'case_graph.json').read_text())
    before=q.evaluate_forward_rule(graph,data,base);off=q.evaluate_forward_rule(graph,data,base,enabled=False);save('rule_before.json',before);save('rule_off.json',off)
    assert c.dispatch(off,data,graph,base) is None
    count=[-1]
    def checkpoint(e):
        save('evidence.json',e);records=[r['fit'] for r in e['calibration_runs']]+e['branch_runs']
        if len(records)!=count[0]:
            count[0]=len(records);print(json.dumps({'completed':count[0],'last':{k:records[-1][k] for k in ['label','numerical_status','objective','projected_gradient_inf'] if k in records[-1]} if records else None}),flush=True)
    e=c.dispatch(before,data,graph,base,checkpoint);save('evidence.json',e)
    after=q.evaluate_forward_rule(graph,data,base,calibration_evidence=e);save('rule_after.json',after)
    save('receipt.json',{'optimizer_calls':len(e['calibration_runs'])+len(e['branch_runs']),'extra_operator_calls':1,'off_operator_calls':0,'same_instance':before['rule_instance_id']==after['rule_instance_id'],'full_question_answer':False,'local_forward_status':after['local_forward_status'],'source_input_id':data.input_id,'base_evidence_request_id':c.request_id(base)})
    for n in ['q09_forward_adequacy_v1.py','q09_calibration_sensitivity_v1.py']:(a.output_dir/n).write_text((q.REPO/'src/dynamics_atlas_harness'/n).read_text())
    print(json.dumps(after,indent=2),flush=True)
if __name__=='__main__':main()
