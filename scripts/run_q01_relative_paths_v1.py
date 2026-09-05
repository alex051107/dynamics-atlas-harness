"""Zero-extraction continuation of the actual Q01 same-instance obligation."""
import argparse
import csv
import datetime
import json
from pathlib import Path
import numpy as np
from dynamics_atlas_harness import q01_path_comparison_v1 as q
from dynamics_atlas_harness import q01_relative_paths_v1 as r


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')


def prepare(parent, out):
    out.mkdir(parents=True, exist_ok=False)
    contacts = json.loads((parent/'contacts.json').read_text())
    ref = np.load(parent/'reference_coordinates.npz', allow_pickle=False)
    policy = r.reference_policy({s: ref[s+'_distances_A'] for s in q.STATES}, contacts)
    policy['frozen_before_grouped_preference_outcomes'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    policy['method_revision_context'] = 'Original40 envelope failure observed; exposed development revision, not heldout'
    save(out/'frozen_policy.json', policy)
    print(json.dumps(policy, indent=2))


def run(parent, out):
    facts = json.loads((parent/'facts.json').read_text())
    contacts = json.loads((parent/'contacts.json').read_text())
    calibration = json.loads((parent/'reference_calibration.json').read_text())
    policy = json.loads((out/'frozen_policy.json').read_text())
    mappings = json.loads((parent/'trajectory_mapping.json').read_text())
    records = {}
    for entry in mappings:
        v = np.load(parent/'trajectories'/entry['name']/'measurements.npz', allow_pickle=False)
        records[entry['name']] = {'seed': entry['seed'], 'time_ns': v['time_ns'], 'distances_A': v['distances_A'],
            'geometry_A': {'open': v['open_rmsd_A'], 'closed': v['closed_rmsd_A']}}
    envelope, _ = q.summarize(records, contacts, calibration)
    if envelope != json.loads((parent/'numerical_report.json').read_text()):
        raise ValueError('PARENT_NUMERICAL_REPLAY_MISMATCH')
    old_evidence = json.loads((parent/'evidence_result.json').read_text())
    if q.identity(envelope) != old_evidence['report_id']:
        raise ValueError('PARENT_EVIDENCE_ID')
    base = q.evaluate(facts, old_evidence, verify_evidence=lambda e: envelope)
    before = r.evaluate(base, facts, envelope, policy)
    off = r.evaluate(base, facts, envelope, policy, enabled=False)
    save(out/'parent_rule_verified.json', base); save(out/'rules_before.json', before); save(out/'rules_off.json', off)
    calls = []
    def operator(request):
        calls.append(request)
        save(out/'operator_dispatch.json', request)
        report, frames = r.compare(records, contacts, policy)
        save(out/'numerical_report.json', report)
        with (out/'full_preference_paths.tsv').open('w', newline='') as f:
            writer = csv.writer(f, delimiter='\t')
            writer.writerow(['trajectory', 'seed', 'time_ns', 'geometry_margin_A', 'uniform_contact_margin', 'SI_contact_margin', 'uniform_preference', 'SI_preference'])
            for name, record in records.items():
                f1, f2 = [frames[(name, method)] for method in q.METHODS]
                for i, time in enumerate(record['time_ns']):
                    writer.writerow([name, record['seed'], time, f1['geometry_margin_A'][i], f1['contact_margin'][i], f2['contact_margin'][i], f1['labels'][i], f2['labels'][i]])
        return dict(request, report_id=q.identity(report), report_path='numerical_report.json',
                    evidence_type='ACTUAL_SAME_COORDINATE_RELATIVE_REFERENCE_PATHS')
    r.dispatch(off, operator)
    if calls:
        raise ValueError('OFF_DISPATCHED')
    evidence = r.dispatch(before, operator)[0]
    def verify(value):
        report, _ = r.compare(records, contacts, policy)
        if q.identity(report) != value['report_id']:
            raise ValueError('FOLLOWUP_NUMERICAL_REPORT_MISMATCH')
        return report
    after = r.evaluate(base, facts, envelope, policy, evidence, verify)
    save(out/'evidence_result.json', evidence); save(out/'rules_after.json', after)
    receipt = {'completed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'status': after['status'],
        'scientific_status': after['scientific_status'], 'instance_id': after['instance_id'],
        'same_instance_as_parent': after['instance_id'] == base['instance_id'], 'on_operator_calls': len(calls), 'off_operator_calls': 0,
        'new_gmx_calls': 0, 'new_optimizations': 0, 'trajectory_count': len(records),
        'changed_primary_trajectories': after['changed_primary_trajectories'],
        'state_membership_claimed': False, 'accuracy_gain_claimed': False, 'full_question_answer': False,
        'development_method_revision': True, 'original_envelope_results_preserved': True}
    save(out/'receipt.json', receipt)
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--parent', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--phase', choices=['prepare', 'run'], required=True)
    args = parser.parse_args()
    globals()[args.phase](args.parent.resolve(), args.output.resolve())
