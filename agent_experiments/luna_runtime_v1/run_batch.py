"""Run only the order in a frozen, explicit task. No C arm in this campaign."""
import argparse
import json
import subprocess
import sys
from pathlib import Path
from datetime import datetime, timezone
from agent_run import campaign_usage


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--freeze', type=Path, required=True)
    p.add_argument('--task-root', type=Path, required=True)
    p.add_argument('--budget-usd', type=float, required=True)
    args = p.parse_args()
    root = args.task_root.resolve()
    freeze = json.loads(args.freeze.read_text())
    if any(arm not in ('A', 'B') for arm in freeze['run_order']):
        raise RuntimeError('Only A/B permitted; C is outside this adopted campaign')
    if args.budget_usd != freeze['budget_usd']:
        raise RuntimeError('Budget differs from frozen configuration')
    result_path = root / 'outputs/results.json'
    if result_path.exists():
        old = json.loads(result_path.read_text())
        if old.get('attempts') or old.get('actual_attempts'):
            raise RuntimeError('This frozen batch already has attempts; no automatic rerun')
    results = {'freeze': args.freeze.name, 'case': freeze['case'], 'attempts': [], 'unplanned_B': None if freeze['selector_branch']=='OK' else 'NOT_RUN_RULES_PATH_UNAVAILABLE'}
    for i, arm in enumerate(freeze['run_order'], 1):
        spent, cap = campaign_usage(root)
        if spent >= cap:
            results['stop'] = 'GLOBAL_COST_LIMIT'
            break
        before = set((root / 'runs').iterdir())
        command = [sys.executable, str(Path(__file__).with_name('agent_run.py')), freeze['case'], arm, '--task-root', str(root), '--image', freeze['image'], '--budget-usd', str(args.budget_usd)]
        proc = subprocess.run(command, text=True, capture_output=True)
        created = sorted(set((root / 'runs').iterdir()) - before)
        record = {'slot': i, 'arm': arm, 'completed_at': datetime.now(timezone.utc).isoformat(), 'returncode': proc.returncode, 'stdout': proc.stdout, 'stderr': proc.stderr}
        if len(created)==1 and (created[0]/'receipt.json').exists():
            record.update(run=created[0].name, receipt=json.loads((created[0]/'receipt.json').read_text()))
        else:
            record['status'] = 'INCOMPLETE_NO_RUN_RECEIPT'
        results['attempts'].append(record)
        result_path.write_text(json.dumps(results, ensure_ascii=False, indent=2)+'\n')
        if (root/'outputs/UNKNOWN_CHARGE.json').exists() or proc.returncode or record.get('receipt',{}).get('status') == 'EXECUTION_ERROR' or record.get('status') == 'INCOMPLETE_NO_RUN_RECEIPT':
            results['stop'] = 'UNKNOWN_CHARGE' if (root/'outputs/UNKNOWN_CHARGE.json').exists() else 'EXECUTION_FAILURE'
            break
        ledger = root/'outputs/paid_usage.jsonl'
        local_spent = sum(json.loads(line)['cost'] for line in ledger.read_text().splitlines()) if ledger.exists() else 0
        if local_spent >= args.budget_usd:
            results['stop'] = 'ROUND_COST_LIMIT'
            break
    results['unstarted_slots'] = [{'slot': i+1, 'arm': arm, 'status': 'NOT_STARTED_AFTER_STOP'} for i, arm in enumerate(freeze['run_order']) if i >= len(results['attempts'])]
    result_path.write_text(json.dumps(results, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'attempts':len(results['attempts']),'stop':results.get('stop')}))


if __name__ == '__main__':
    main()
