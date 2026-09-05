import unittest
import numpy as np
from dynamics_atlas_harness import q01_relative_paths_v1 as r
from dynamics_atlas_harness import q01_path_comparison_v1 as q


class RelativePaths(unittest.TestCase):
    def test_preference_is_scale_aware_and_keeps_conflict(self):
        normalization = {'mid': [10, 50], 'delta': [20, -100]}
        labels, _, values = r.preference({'open': [1, 5, 1], 'closed': [5, 1, 5]},
            {'open': [0, 20, 20], 'closed': [100, 0, 0]}, normalization)
        self.assertEqual(labels.tolist(), ['open', 'closed', 'conflict'])
        np.testing.assert_allclose(values, [.5, -.5, -.5])
        labels2, _, _ = r.preference({'open': [1, 5, 1], 'closed': [5, 1, 5]},
            {'open': [0, 200, 200], 'closed': [100, 0, 0]}, {'mid': [100, 50], 'delta': [200, -100]})
        self.assertEqual(labels.tolist(), labels2.tolist())

    def test_same_instance_requires_actual_all_initial_gap_and_numeric_evidence(self):
        facts = {'input_id': 'input', 'method_id': 'parent'}
        envelope = {'paths': [{'persistence_results': {'20': {'initial_support': 'outside'}}}]}
        base = {'facts_id': q.identity(facts), 'rule_id': q.RULE_ID, 'instance_id': 'same',
                'status': 'COMPARISON_EXECUTED', 'numeric_result': envelope}
        policy = {'policy': 'synthetic'}
        before = r.evaluate(base, facts, envelope, policy)
        calls = []
        r.dispatch(r.evaluate(base, facts, envelope, policy, enabled=False), calls.append)
        self.assertEqual(calls, [])
        evidence = r.dispatch(before, lambda request: dict(request))[0]
        report = {'trajectory_count': 40, 'method_changes': [{'category_changes': {'20': True}}]}
        after = r.evaluate(base, facts, envelope, policy, evidence, lambda e: report)
        self.assertEqual(after['instance_id'], 'same')
        self.assertEqual(after['scientific_status'], 'RELATIVE_DIRECTION_METHOD_DEPENDENT')
        self.assertFalse(after['state_membership_claimed'])
        evidence['input_id'] = 'wrong'
        self.assertEqual(len(r.evaluate(base, facts, envelope, policy, evidence, lambda e: report)['operator_requests']), 1)
        envelope['paths'][0]['persistence_results']['20']['initial_support'] = 'open'
        self.assertEqual(r.evaluate(base, facts, envelope, policy)['status'], 'FOLLOWUP_NOT_TRIGGERED')


if __name__ == '__main__':
    unittest.main()
