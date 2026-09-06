"""Execute one Rules-controlled source-code sensitivity on original APBS inputs."""
import argparse
import collections
import csv
import datetime
import hashlib
import json
from pathlib import Path
import time

import numpy as np

from dynamics_atlas_harness import q15_apbs_comparison_v1 as q
from dynamics_atlas_harness import q15_background_policy_v1 as rule


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--task-root', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    task, out = args.task_root.resolve(), args.output.resolve()
    out.mkdir(parents=True, exist_ok=False)
    def save(name, value):
        (out / name).write_text(json.dumps(value, indent=2, allow_nan=False) + '\n')
    baseline = json.loads((task / 'outputs/q15_apbs_comparison_v1/report.json').read_text())
    if baseline['policy'] != q.POLICY:
        raise ValueError('FROZEN_MAIN_POLICY_CHANGED')
    source = (task / 'inputs/q15_author/alex_suite_source/models.py').read_text()
    assignments = ['DA_bkg_corr[DA_bkg_corr < 0] = 0',
                   'DD_bkg_corr[DA_bkg_corr < 0] = 0',
                   'DA_bkg_corr[AA_bkg_corr < 0] = 0']
    positions = [source.index(line) for line in assignments]
    if positions != sorted(positions):
        raise ValueError('SOURCE_ASSIGNMENT_ORDER_CHANGED')
    facts = {'clipping_discrepancy_verified': True,
             'source_commit': '49dfef079129696e84c4983ecc330d7b5d60e71b',
             'source_locator': 'alex/models.py lines607-609',
             'literal_assignments': assignments,
             'exact_Peter2022_executable': 'UNKNOWN',
             'alternatives': list(rule.ALTERNATIVES),
             'other_calibration_and_selection': 'Frozen main policy; selection recomputed for each alternative; no E clipping'}
    save('source_facts.json', facts)
    save('before.json', rule.evaluate(baseline, facts))
    def forbidden(_):
        raise AssertionError('DISABLED_RULE_CALLED_OPERATOR')
    save('off.json', rule.dispatch(baseline, facts, forbidden, enabled=False))
    started = time.monotonic()

    def operator(instance):
        h = hashlib.sha256()
        h.update(json.dumps(q.POLICY, sort_keys=True).encode())
        groups = {a: collections.defaultdict(list) for a in rule.ALTERNATIVES}
        per_file = []
        for source_name in ['q15_apbs_intake_v1', 'q15_normal_control_intake_v1']:
            intake = json.loads((task / 'outputs' / source_name / 'member_intake_receipt.json').read_text())
            for item in intake['results']:
                name = item['member']['name']
                if not name.endswith('_apbs_alex.csv'):
                    continue
                if item['status'] != 'LOCAL_HEADER_CENTRAL_CRC_LENGTH_MATCH':
                    raise ValueError('UNADMITTED_SOURCE')
                b = (task / 'outputs' / source_name / 'source_members' / name).read_bytes()
                q.validate_member_bytes(b, item['member'])
                h.update(name.encode() + b'\0' + len(b).to_bytes(8, 'big') + b)
                lines = b.decode().splitlines()
                data_start = lines.index('DATA')
                rows = list(csv.DictReader(lines[data_start+1:]))
                counts = np.array([[float(row[k]) for k in ['F_Dexc_Dem','F_Dexc_Aem','F_Aexc_Aem']] for row in rows])
                duration = np.array([float(row['Tau']) for row in rows])
                if not np.array_equal(counts.sum(axis=1), [float(row['Len']) for row in rows]):
                    raise ValueError('RAW_LENGTH_IDENTITY')
                parts = name.split('/')
                pair = parts[1].split('_1mM')[0].split('_apo')[0]
                condition = 'holo' if '_1mM_SA' in parts[1] else 'apo'
                key = (pair, condition, parts[2])
                reference = q.correct(counts, duration)['selected']
                entry = {'member': name, 'raw_events': len(rows), 'alternatives': {}}
                for alternative in rule.ALTERNATIVES:
                    result = rule.corrected_alternative(counts, duration, alternative)
                    mask = result['selected']
                    groups[alternative][key].append((result['E'][mask], result['S'][mask]))
                    entry['alternatives'][alternative] = {
                        'selected': int(mask.sum()),
                        'entered_selection': int(np.sum(mask & ~reference)),
                        'left_selection': int(np.sum(reference & ~mask)),
                        'E': q.summarize(result['E'][mask])}
                per_file.append(entry)
        if h.hexdigest() != baseline['input_id']:
            raise ValueError('ORIGINAL_MAIN_INPUT_IDENTITY_MISMATCH')
        if len(per_file) != 140:
            raise ValueError('SOURCE_FILE_COVERAGE')
        evidence = {'input_id': baseline['input_id'], 'rule_instance_id': instance['rule_instance_id'],
                    'operator_id': rule.OPERATOR_ID, 'policy': q.POLICY, 'alternatives': {},
                    'source_files': len(per_file), 'raw_events': sum(f['raw_events'] for f in per_file),
                    'files': per_file, 'optimizer_calls': 0, 'scientific_question_answer': False}
        for alternative, values in groups.items():
            repetitions = []
            for (pair, condition, repetition), parts in sorted(values.items()):
                repetitions.append({'pair': pair, 'condition': condition, 'repetition': repetition,
                                    'files': len(parts), 'E': q.summarize(np.concatenate([p[0] for p in parts])),
                                    'S': q.summarize(np.concatenate([p[1] for p in parts]))})
            evidence['alternatives'][alternative] = {
                'repetitions': repetitions, 'condition_comparisons': q.group_difference(repetitions),
                'selected_events': sum(r['E']['n'] for r in repetitions)}
        return evidence

    actual = rule.dispatch(baseline, facts, operator)
    save('evidence_result.json', actual['evidence_result'])
    save('after.json', actual['after'])
    save('receipt.json', {'completed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                         'elapsed_seconds': time.monotonic()-started,
                         'on_calls': actual['operator_calls'], 'off_calls': 0,
                         'rule_instance_id': actual['after']['rule_instance_id'],
                         'source_input_id': baseline['input_id'], 'source_input_identity_matches': True,
                         'new_rules_extra': 1, 'optimizer_calls': 0,
                         'same_rule_instance_reassessed': actual['before']['rule_instance_id'] == actual['after']['rule_instance_id'],
                         'claim_ceiling': actual['after']['claim_ceiling']})
    print(json.dumps({'after': actual['after'], 'comparisons': {a: v['condition_comparisons'] for a,v in actual['evidence_result']['alternatives'].items()}}, indent=2))


if __name__ == '__main__':
    main()
