"""Run the original admitted Q05 facts plus one explicitly new joint numeric rule."""
import argparse
import datetime
import json
from pathlib import Path
import subprocess
import sys

from dynamics_atlas_harness.paper_blind_exposed_v1 import validate_agent_proposal, project_admitted_proposal_to_rules_casegraph
from dynamics_atlas_harness.real_case_vertical_slice_v1 import load_rules_v1_bundle
from dynamics_atlas_harness.rules_prototype_v1 import evaluate_active_rules
from dynamics_atlas_harness.q05_joint_numeric_v1 import load_inputs, evaluate_joint_rule, dispatch_obligation

ROOT=Path(__file__).resolve().parents[1]

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--input-root',type=Path,required=True)
    parser.add_argument('--output-dir',type=Path,required=True);args=parser.parse_args()
    args.output_dir.mkdir(parents=True,exist_ok=False)
    def save(name,obj):
        (args.output_dir/name).write_text(json.dumps(obj,indent=2,allow_nan=False)+'\n')
    receipt={'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),
             'source_head':subprocess.check_output(['git','-C',str(ROOT),'rev-parse','HEAD'],text=True).strip(),
             'source_uncommitted':bool(subprocess.check_output(['git','-C',str(ROOT),'status','--porcelain'],text=True).strip()),
             'rules_run_kind':'ORIGINAL_DECLARATION_SLICE_PLUS_EXPLICIT_NEW_Q05_CASE_RULE',
             'main_calculation_operator_calls':0,'extra_calculation_operator_calls':0,
             'rules_off_control_kind':'ROUTING_CAPABILITY_ONLY_NOT_ACCURACY_ABLATION',
             'full_scientific_answers':0,'original_question_count':20}
    try:
        packet=ROOT/'evidence/paper_blind_exposed_v1/public/q05_public_fact_packet_v1.json'
        proposal=json.loads((ROOT/'research/paper_result_reproduction_screen_v1/q05_fact_proposal_v1.json').read_text())
        graph=project_admitted_proposal_to_rules_casegraph(packet,validate_agent_proposal(packet,proposal))
        config=json.loads((ROOT/'research/paper_result_reproduction_screen_v1/q05_joint_method_v1.json').read_text())
        save('casegraph.json',graph);save('method_config.json',config)
        save('joint_rule.json',json.loads((ROOT/'registries/rules_v1/q05_joint_numeric_rule_v1.json').read_text()))
        save('declaration_rule_results.json',evaluate_active_rules(case_graph=graph,**load_rules_v1_bundle(ROOT/'registries/rules_v1')))
        data=load_inputs(args.input_root,config)
        save('input_identity.json',data['input_identity'])
        before=evaluate_joint_rule(graph,data);save('rule_before.json',before)
        off=evaluate_joint_rule(graph,data,enabled=False);save('rule_off.json',off)
        assert dispatch_obligation(off,data,config,graph) is None
        evidence=dispatch_obligation(before,data,config,graph)
        if evidence is None:raise ValueError('NO_ACTUAL_OBLIGATION_DISPATCHED')
        receipt['main_calculation_operator_calls']=1
        save('numeric_evidence.json',evidence)
        after=evaluate_joint_rule(graph,data,evidence);save('rule_after.json',after)
        assert before['rule_instance_id']==after['rule_instance_id']
        receipt.update(status='NUMERIC_EVIDENCE_AND_SAME_INSTANCE_REASSESSMENT_SAVED',
                       numerical_conditions_satisfied=evidence['optimization']['numerical_conditions_satisfied'],
                       relative_fit_change=after.get('relative_fit_change'),
                       scientific_compatibility=after['scientific_compatibility'])
    except Exception as exc:
        receipt.update(status='INPUT_OR_NUMERICAL_EXECUTION_FAILURE',error=f'{type(exc).__name__}: {exc}')
        raise
    finally:
        save('receipt.json',receipt)
        (args.output_dir/'operator_source.py').write_text((ROOT/'src/dynamics_atlas_harness/q05_joint_numeric_v1.py').read_text())
        (args.output_dir/'runner_source.py').write_text(Path(__file__).read_text())
        print(json.dumps(receipt,indent=2))

if __name__=='__main__':main()
