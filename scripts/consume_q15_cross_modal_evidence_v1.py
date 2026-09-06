"""Materialize conditional matched-probe claims without repeating science work."""
import argparse
import datetime
import json
from pathlib import Path
from dynamics_atlas_harness import q15_cross_modal_evidence_v1 as q


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--task-root',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--source-receipt',type=Path,default=q.SOURCE_RECEIPT,help='Explicit prior admission; default is the reviewed production source receipt')
    args=parser.parse_args();task=args.task_root.resolve();out=args.output.resolve()
    out.mkdir(parents=True,exist_ok=False)
    def read(name):return json.loads((task/'outputs'/name).read_text())
    def save(name,value):(out/name).write_text(json.dumps(value,indent=2,allow_nan=False)+'\n')
    main_report=read('q15_apbs_comparison_v1/report.json')
    summary=read('q15_pro19_verification_v1/report.json')
    deer=read('q15_deer_source_audit_v1/report.json')
    forward=read('q15_probe_forward_source_facts_v1.json')
    sources=dict(main=main_report,summary=summary,deer=deer,forward=forward)
    source_receipt=q.verify_admitted_sources(sources,json.loads(args.source_receipt.read_text()))
    save('admitted_source_receipt.json',source_receipt)
    save('source_forward_predictions.json',forward)
    save('before.json',q.evaluate(main_report))
    evidence=q.synthesize_manual_evidence(main_report,summary,deer,forward)
    save('manual_relational_evidence.json',evidence)
    off=q.evaluate(main_report,evidence,enabled=False);after=q.evaluate(main_report,evidence,admitted_sources=sources,source_receipt=source_receipt)
    save('off.json',off);save('after.json',after)
    save('receipt.json',{'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),
                         'input_id':main_report['input_id'],'rule_instance_id':after['rule_instance_id'],
                         'evidence_applications_on':after['evidence_applications'],
                         'evidence_applications_off':off['evidence_applications'],
                         'new_numerical_operator_calls':0,'optimizer_calls':0,'full_question_answer':False,
                         'manual_evidence_not_reclassified_as_rules_extra':True})
    print(json.dumps(after,indent=2))


if __name__=='__main__':main()
