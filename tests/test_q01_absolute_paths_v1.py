import unittest
import json
from pathlib import Path
import numpy as np
from dynamics_atlas_harness import q01_path_comparison_v1 as q
from dynamics_atlas_harness import q01_relative_paths_v1 as r
from dynamics_atlas_harness import q01_absolute_paths_v1 as a


class AbsolutePaths(unittest.TestCase):
    def test_full_paths_keep_absolute_counterexample_and_internal_disagreement(self):
        contacts = [{'state': 'open', 'dviol_angstrom': 10.}, {'state': 'closed', 'dviol_angstrom': 8.5}]
        policy = r.reference_policy({'open': np.array([[9., 20.]]*2), 'closed': np.array([[20., 8.]]*2)}, contacts)
        records = {}
        for name, seed in [('o', 'open'), ('c', 'closed')]:
            distance = np.tile([9., 9.], (1001, 1))
            op, cl = np.full(1001, 5.), np.full(1001, 6.)
            if seed == 'closed':
                distance[:100] = [20., 8.]; op[:100] = 3.; cl[:100] = 1.
            records[name] = {'seed': seed, 'time_ns': np.arange(20, 1021), 'distances_A': distance,
                             'geometry_A': {'open': op, 'closed': cl}}
        displacement = {name: np.linspace(0, 6, 1001) for name in records}
        md = {name: np.ones(1001) for name in records}
        report, full = a.describe(records, contacts, policy, displacement, md)
        row = next(x for x in report['rows'] if x['seed_group'] == 'closed')
        self.assertEqual(row['methods'][q.METHODS[0]]['unchanged_relative_path']['category'],
                         'SUSTAINED_OPPOSITE_REFERENCE_PREFERENCE')
        event = row['methods'][q.METHODS[0]]['events_by_persistence']['20'][0]
        self.assertEqual(event['pre20_to_first20_event']['open_reference_lid_rmsd_A']['delta'], 2.)
        self.assertEqual(event['pre20_to_first20_event']['closed_reference_lid_rmsd_A']['delta'], 5.)
        self.assertEqual(event['event_contact_internal_disagreement_frames'], 901)
        self.assertIn('INTERNAL_CONTACT_DISAGREEMENT', row['methods'][q.METHODS[0]]['interpretation'])
        self.assertFalse(report['new_state_membership_claimed'])
        self.assertEqual(len(full[('c', q.METHODS[0])]['relative_preference']), 1001)

    def test_rules_retain_instance_and_evidence_changes_interpretation_without_refit(self):
        previous = {'status': 'RELATIVE_COMPARISON_EXECUTED', 'instance_id': 'same',
                    'facts_id': 'facts', 'rule_id': q.RULE_ID}
        method = {'measurement_manifest_id': 'bound', 'policy': a.POLICY}
        calls = []
        a.dispatch(a.evaluate(previous, method, enabled=False), calls.append)
        self.assertEqual(calls, [])
        before = a.evaluate(previous, method)
        evidence = a.dispatch(before, lambda request: dict(request))[0]
        report = json.loads((Path(__file__).resolve().parents[1]/'research/paper_result_reproduction_screen_v1/q01_absolute_paths_v1/numerical_report.json').read_text())
        after = a.evaluate(previous, method, evidence, lambda _: report)
        self.assertEqual(after['instance_id'], previous['instance_id'])
        self.assertEqual(after['operator_requests'], [])
        self.assertTrue(any('ES17' in name for name in after['trajectory_interpretation_limits']))
        evidence['measurement_manifest_id'] = 'other'
        self.assertEqual(len(a.evaluate(previous, method, evidence, lambda _: report)['operator_requests']), 1)


if __name__ == '__main__':
    unittest.main()
