"""Execute one Q09 donor/instrument obligation and re-evaluate its same instance."""
from pathlib import Path
import argparse
import csv
import json
import datetime
import subprocess
import sys
from dynamics_atlas_harness import q09_forward_adequacy_v1 as q
from dynamics_atlas_harness.paper_blind_exposed_v1 import validate_agent_proposal,project_admitted_proposal_to_rules_casegraph
from dynamics_atlas_harness.real_case_vertical_slice_v1 import load_rules_v1_bundle
from dynamics_atlas_harness.rules_prototype_v1 import evaluate_active_rules


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--input-root',type=Path,required=True);p.add_argument('--output-dir',type=Path,required=True);args=p.parse_args();args.output_dir.mkdir(parents=True,exist_ok=False)
    def save(name,obj):(args.output_dir/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
    packet=q.REPO/'evidence/paper_blind_exposed_v1/public/q09_public_fact_packet_v1.json';proposal=json.loads((q.REPO/'research/paper_result_reproduction_screen_v1/q09_fact_proposal_v1.json').read_text())
    graph=project_admitted_proposal_to_rules_casegraph(packet,validate_agent_proposal(packet,proposal));save('case_graph.json',graph)
    baseline=evaluate_active_rules(case_graph=graph,**load_rules_v1_bundle(q.REPO/'registries/rules_v1'));save('declaration_rule_results.json',baseline)
    data=q.load_inputs(args.input_root);save('input_receipt.json',{'input_id':data.input_id,'source_identity':data.source_identity,'config':q.CONFIG,'baseline_parameters':data.baseline,'source_binding':'ZIPpublishedMD5+5memberexactbytes+parsedarraysfingerprint','scope':'22-127 methoddiagnostic insideQ09;notall33'})
    off=q.evaluate_forward_rule(graph,data,enabled=False);save('rule_off.json',off);assert q.dispatch_obligation(off,data,graph) is None
    before=q.evaluate_forward_rule(graph,data);save('rule_before.json',before)
    last_count=[-1]
    def checkpoint(e):
        save('evidence.json',e);records=e['donor_runs']+e['joint_runs']+e['profile_runs']
        if len(records)!=last_count[0]:
            last_count[0]=len(records)
            print(json.dumps({'completed_optimizer_calls':len(records),'latest':{k:records[-1][k] for k in ['label','numerical_status','objective','projected_gradient_inf','bound_hits'] if k in records[-1]} if records else None}),flush=True)
    evidence=q.dispatch_obligation(before,data,graph,checkpoint);save('evidence.json',evidence)
    after=q.evaluate_forward_rule(graph,data,evidence);save('rule_after.json',after)
    assert after['rule_instance_id']==before['rule_instance_id']
    predictions={'prior_D0':data.joint_counts(data.baseline)['D0'],'prior_DA':data.joint_counts(data.baseline)['DA']}
    if evidence['selected_donor_index'] is not None:predictions['candidate_D0_only']=q.d3_counts(data,evidence['donor_runs'][evidence['selected_donor_index']]['parameters'])['D0']
    if evidence['selected_joint_index'] is not None:
        for role,v in q.j3_counts(data,evidence['joint_runs'][evidence['selected_joint_index']]['parameters']).items():predictions['candidate_joint_'+role]=v
    with (args.output_dir/'per_bin.csv').open('w') as f:
        w=csv.writer(f);w.writerow(['bin0','time_ns','D0_observed','DA_observed']+list(predictions))
        for i,t in enumerate(data.t):w.writerow([i,t,int(data.y['D0'][i]),int(data.y['DA'][i])]+[v[i] for v in predictions.values()])
    for name in ['q09_fluorescence_v1.py','q09_forward_adequacy_v1.py']:(args.output_dir/name).write_text((q.REPO/'src/dynamics_atlas_harness'/name).read_text())
    (args.output_dir/'runner_source.py').write_text(Path(__file__).read_text())
    receipt={'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':[sys.executable,str(Path(__file__).resolve()),*sys.argv[1:]],'source_head':subprocess.check_output(['git','-C',str(q.REPO),'rev-parse','HEAD'],text=True).strip(),'new_rule_uncommitted':True,'rule_id':q.RULE_ID,'operator_id':q.OPERATOR_ID,'declaration_instances':len(baseline),'extra_operator_calls':1,'optimizer_calls':len(evidence['donor_runs'])+len(evidence['joint_runs'])+len(evidence['profile_runs']),'off_operator_calls':0,'same_rule_instance_reassessed':True,'status_after':after['status'],'reason_codes_after':after['reason_codes'],'complete_question_answer':False,'claim':'Actualrule-controlledextra methoddiagnostic;no comparativeaccuracygain againstcompletecorrectmanualworkflow'}
    save('receipt.json',receipt);print(json.dumps(receipt,indent=2),flush=True)
if __name__=='__main__':main()
