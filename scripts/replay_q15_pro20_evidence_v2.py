"""Re-admit saved Q15 numerical evidence without rerunning APBS or DEER."""
import argparse
import copy
import datetime
import json
from pathlib import Path
from dynamics_atlas_harness import q15_cross_modal_evidence_v1 as cross
from dynamics_atlas_harness import q15_background_policy_v1 as background


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--task-root',type=Path,required=True);parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    def read(name):return json.loads((args.task_root/'outputs'/name).read_text())
    sources=dict(main=read('q15_apbs_comparison_v1/report.json'),summary=read('q15_pro19_verification_v1/report.json'),deer=read('q15_deer_source_audit_v1/report.json'),forward=read('q15_probe_forward_source_facts_v1.json'))
    admitted=cross.verify_admitted_sources(sources)
    old_background=read('q15_background_policy_v1/evidence_result.json')
    if cross.canonical_digest(old_background)!=admitted['sources']['background']['canonical_sha256']:
        raise ValueError('BACKGROUND_REPORT_NOT_PREVIOUSLY_ADMITTED')
    # Explicit metadata-only readmission of already executed method. Original remains immutable.
    new_background=copy.deepcopy(old_background);new_background['policy']=sources['main']['policy']
    bg=background.evaluate(sources['main'],read('q15_background_policy_v1/source_facts.json'),new_background)
    old_after=read('q15_background_policy_v1/after.json')
    assert bg['rule_instance_id']==old_after['rule_instance_id'] and bg['method_disposition']==old_after['method_disposition']
    evidence=cross.synthesize_manual_evidence(*(sources[k] for k in ['main','summary','deer','forward']))
    after=cross.evaluate(sources['main'],evidence,admitted_sources=sources)
    previous=read('q15_cross_modal_evidence_v1/after.json')
    assert after['partial_claims']==previous['partial_claims']
    off=cross.evaluate(sources['main'],evidence,False)
    args.output.mkdir(parents=True,exist_ok=False)
    values={'source_admission.json':admitted,'background_evidence_readmitted.json':new_background,'background_after.json':bg,'cross_modal_evidence.json':evidence,'cross_modal_after.json':after,'cross_modal_off.json':off,'receipt.json':dict(timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat(),source_reports_verified=5,new_APBS_runs=0,new_DEER_inversions=0,new_optimizer_calls=0,new_rules_extra=0,numerical_relations_unchanged=True,background_readmission='Only policy metadata added after fixed prior source receipt verified',cross_modal_evidence_applications=after['evidence_applications'],off_applications=off['evidence_applications'],full_question_answer=False)}
    for name,value in values.items():(args.output/name).write_text(json.dumps(value,indent=2,allow_nan=False)+'\n')
    print(json.dumps(values['receipt.json'],indent=2))
if __name__=='__main__':main()
