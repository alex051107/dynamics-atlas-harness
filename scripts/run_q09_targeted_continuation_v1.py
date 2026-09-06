"""Bounded continuation of current Rules-selected historical stop points."""
import argparse
import datetime
import json
import time
from pathlib import Path
from dynamics_atlas_harness import q09_global_comparison_v1 as a
from dynamics_atlas_harness import q09_method_evidence_v1 as m
from dynamics_atlas_harness import q09_targeted_continuation_v1 as c
from dynamics_atlas_harness.q09_cached_group_v2 import CachedGroup


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--task-root', type=Path, required=True); p.add_argument('--output', type=Path, required=True)
    p.add_argument('--previous-result', type=Path, help='Latest verified rules_after.json; defaults to the original manual admission for first use.')
    args = p.parse_args(); task = args.task_root.resolve(); out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=False)
    def save(n, value): (out/n).write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False)+'\n')
    parent = task/'outputs/q09_method_evidence_v1'
    previous_path = args.previous_result.resolve() if args.previous_result else parent/'rules_after.json'
    previous = json.loads(previous_path.read_text())
    parent_evidence = json.loads((parent/'evidence_result.json').read_text())
    if a.q.digest(previous['method_evidence']) != parent_evidence['report_id']:
        raise ValueError('PREVIOUSLY_VERIFIED_METHOD_ARTIFACT_CHANGED')
    latest_evidence = None
    if c.history_reports(previous):
        latest_evidence = json.loads((previous_path.parent/'evidence_result.json').read_text())
        c.verify_saved_history(previous, latest_evidence)
    data = a.GlobalData(task/'inputs/q09_author')
    if previous['method_evidence']['input_id'] != data.input_id:
        raise ValueError('CURRENT_SOURCE_INPUT_CHANGED')
    if a.CONFIG['local_seconds'] != 60 or a.CONFIG['maxiter'] != 1500:
        raise ValueError('OPTIMIZER_BUDGET_CHANGED')
    before = c.evaluate(previous); off = c.evaluate(previous, enabled=False)
    save('rules_before.json', before); save('rules_off.json', off)
    save('frozen_request.json', c.request(previous)); calls = []; started = time.monotonic()
    report = None
    def operator(req):
        nonlocal report
        calls.append(req)
        report = {'request_id': req['request_id'], 'policy': req['policy'], 'runs': [], 'optimizer_calls': 0}
        for item in req['selected']:
            original = next(g for g in data.groups if g.ref == item['reference'])
            if original.owners != item['owners']:
                raise ValueError('CONTINUATION_OWNER_CHANGED')
            group = CachedGroup(original.ref, original.owners, original.records, 3)
            run = a.optimize_local(group, item['initial'])
            report['runs'].append(dict(item, fit=run)); report['optimizer_calls'] += 1
            save('raw_new_fits.json', report)
            print(item['reference'], run['numerical_status'], run['objective']*group.total, flush=True)
        return {'request_id': req['request_id'], 'input_id': req['input_id'],
                'rule_instance_id': req['rule_instance_id'], 'base_result_id': req['base_result_id']}
    c.dispatch(off, previous, operator)
    if calls: raise ValueError('DISABLED_RULE_DISPATCHED')
    dispatched = c.dispatch(before, previous, operator)
    if not dispatched:
        save('rules_after.json', before)
        if latest_evidence is not None:
            save('evidence_result.json', latest_evidence)  # unchanged prior evidence, zero new calculation
        save('receipt.json', {'status': before['targeted_continuation'], 'optimizer_calls': 0,
                             'on_operator_calls': 0, 'off_operator_calls': 0})
        return
    evidence = dispatched[0]
    # Verify each new objective/gradient once. No historical candidates are refitted.
    for item in report['runs']:
        original = next(g for g in data.groups if g.ref == item['reference'])
        group = CachedGroup(original.ref, original.owners, original.records, 3)
        if item['fit']['initial'] != item['initial']:
            raise ValueError('CONTINUATION_INITIAL_CHANGED')
        item['checked'] = m.check_candidate(item['fit'], group.bounds('local2'), lambda p: group.deviance(p, 'local2')/group.total)
        item['checked']['deviance'] = item['checked']['objective']*group.total
    evidence['report_id'] = a.q.digest(report)
    after = c.evaluate(previous, evidence, lambda _: report)
    evidence = c.evidence_anchor(after, evidence)
    save('verified_report.json', report); save('evidence_result.json', evidence); save('rules_after.json', after)
    receipt = {'completed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'status': after['targeted_continuation'], 'on_operator_calls': len(calls), 'off_operator_calls': 0,
        'optimizer_calls': report['optimizer_calls'], 'historical_fits_repeated': 0,
        'historical_manual_work_reclassified': False, 'same_instance': previous['rule_instance_id'] == after['rule_instance_id'],
        'selected_from_recorded_stop_parameters': True, 'elapsed_seconds': time.monotonic()-started,
        'complete_question_answer': False,
        'updated_dispositions': {r['reference']: r['status'] for r in after['method_obligations'] if r['kind'] == 'DONOR_GROUP_NEXT_ACTION'}}
    save('receipt.json', receipt); print(json.dumps(receipt, indent=2))


if __name__ == '__main__': main()
