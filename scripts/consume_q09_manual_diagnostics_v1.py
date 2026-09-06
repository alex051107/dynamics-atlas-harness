"""Replay fixed historical candidates once, then consume verified method evidence."""
import argparse
import datetime
import json
import time
from pathlib import Path
from dynamics_atlas_harness import q09_global_comparison_v1 as a
from dynamics_atlas_harness import q09_method_evidence_v1 as method


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--task-root', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args(); t = args.task_root.resolve(); out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=False)
    def read(relative): return json.loads((t/relative).read_text())
    def save(name, value): (out/name).write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False)+'\n')
    started = time.monotonic(); data = a.GlobalData(t/'inputs/q09_author')
    previous = read('outputs/q09_global_comparison_v1/replayed_with_structure/rule_after.json')
    graph = json.loads((a.ROOT/'q09_global_comparison_v1/case_graph.json').read_text())
    if previous['request_id'] != a.request(data, graph):
        raise ValueError('BASE_COMPARISON_REQUEST_CHANGED')
    save('base_verified_result_snapshot.json', previous)
    save('rules_before.json', method.consume(previous, data.input_id))
    save('rules_off.json', method.consume(previous, data.input_id, enabled=False))
    response = read('outputs/q09_60_119_response_diagnostic_v1/evidence.json')
    response_input = read('outputs/q09_60_119_response_diagnostic_v1/input_receipt.json')
    orders = read('outputs/q09_donor_order_groups_v2/evidence.json')
    source = json.loads((a.ROOT/'q09_deposited_structure_intake_v1/donor_order_source_audit.json').read_text())
    old = read('outputs/q09_global_comparison_v1/evidence.json')
    report = method.verify_diagnostics(data, response, response_input, orders, source, old)
    save('verified_method_report.json', report)
    evidence = {'input_id': data.input_id, 'base_result_id': a.q.digest(previous),
                'rule_instance_id': previous['rule_instance_id'], 'report_id': a.q.digest(report),
                'provenance': method.PROVENANCE, 'report_path': 'verified_method_report.json'}
    after = method.consume(previous, data.input_id, evidence, lambda _: report)
    save('evidence_result.json', evidence); save('rules_after.json', after)
    receipt = {'completed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'status': after['method_evidence_application'], 'candidate_verifications': 36,
        'optimizer_calls': 0, 'new_rules_extra_calculations': 0, 'manual_provenance_preserved': True,
        'same_instance': previous['rule_instance_id'] == after['rule_instance_id'],
        'original_global_comparison_preserved': previous['comparison'] == after['comparison'],
        'original_structure_evidence_preserved': previous['structure_comparison'] == after['structure_comparison'],
        'historical_base_status': 'Previously verified result snapshot; matching current source request checked, old global fits not reverified in this method-only application.',
        'elapsed_seconds': time.monotonic()-started,
        'dispositions': {row['reference']: row['status'] for row in report['group_dispositions']},
        'response_transfer': report['response_transfer']['status'],
        'complete_question_answer': False}
    save('receipt.json', receipt); print(json.dumps(receipt, indent=2))


if __name__ == '__main__': main()
