import unittest
import numpy as np
from dynamics_atlas_harness import q01_path_comparison_v1 as q


class Q01Paths(unittest.TestCase):
    def facts(self):
        return {'question_id': 'Q01', 'claim': 'FINITE_TIME_SEEDED_PATH_COMPARISON',
                'method_id': 'synthetic-method', 'input_id': 'synthetic-input',
                'threshold_definitions': [{'source_locator': 'source1', 'bounds_A': [8.5]},
                                          {'source_locator': 'source2', 'bounds_A': [10.08]}]}

    def test_rule_controls_dispatch_and_evidence_changes_same_instance(self):
        facts = self.facts(); calls = []
        self.assertEqual(q.dispatch(q.evaluate(facts, enabled=False), calls.append), [])
        before = q.evaluate(facts)
        def operator(request):
            calls.append(request); return dict(request)
        evidence = q.dispatch(before, operator)[0]
        self.assertEqual(len(calls), 1)
        report = {'trajectory_count': 40, 'group_counts': {'open': 20, 'closed': 20},
                  'trajectory_changes': [{'primary_route_changed': True, 'primary_initial_support_changed': False}]}
        after = q.evaluate(facts, evidence, verify_evidence=lambda e: report)
        self.assertEqual(before['instance_id'], after['instance_id'])
        self.assertEqual(after['scientific_status'], 'METHOD_DEPENDENT_PATH_JUDGMENTS')
        self.assertFalse(after['accuracy_gain_claimed'])
        self.assertEqual(after['operator_requests'], [])
        report['trajectory_changes'][0]['primary_route_changed'] = False
        self.assertEqual(q.evaluate(facts, evidence, verify_evidence=lambda e: report)['scientific_status'],
                         'PATH_JUDGMENTS_UNCHANGED_UNDER_TWO_METHODS')
        report['paths'] = [{'persistence_results': {'20': {'initial_support': 'outside'}}}]
        self.assertEqual(q.evaluate(facts, evidence, verify_evidence=lambda e: report)['scientific_status'],
                         'INITIAL_REFERENCE_SUPPORT_UNESTABLISHED_FOR_ALL_TRAJECTORIES')
        evidence['input_id'] = 'different-source'
        self.assertEqual(len(q.evaluate(facts, evidence, verify_evidence=lambda e: report)['operator_requests']), 1)
        facts['threshold_definitions'][1]['bounds_A'] = [8.5]
        self.assertEqual(q.evaluate(facts)['operator_requests'], [])

    def test_core_alignment_preserves_lid_motion_and_rotation(self):
        core = np.array([[0, 0, 0], [1, 0, 0], [0, 2, 0], [0, 0, 3]], float)
        lid = np.array([[4, 5, 6], [3, 7, 8]], float)
        rot = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
        np.testing.assert_allclose(q.nearest_lid_rmsd((core@rot+10)[None], (lid@rot+10)[None], core[None], lid[None]), 0, atol=1e-12)
        np.testing.assert_allclose(q.nearest_lid_rmsd(core[None], (lid+np.array([2, 0, 0]))[None], core[None], lid[None]), 2, atol=1e-12)

    def test_periodic_distance_oblique_box(self):
        box = np.array([[[3., 0, 0], [1., 3., 0], [.5, .5, 4.]]])
        v = np.array([[[.2, .3, .4]]])
        delta = v + box[:, 1:2] - 2*box[:, 2:3]
        np.testing.assert_allclose(q.minimum_image(delta, box), np.linalg.norm(v, axis=2), atol=1e-12)

    def test_persistence_uses_full_path_and_never_one_frame(self):
        path = ['closed']*30+['open']+['closed']*30
        self.assertEqual(q.path_summary(path, 'closed', 20)['route'], 'NO_PERSISTENT_DEPARTURE_FROM_INITIAL_REFERENCE_SUPPORT')
        path = ['closed']*30+['open']*20+['closed']*120
        result = q.path_summary(path, 'closed', 20)
        self.assertEqual(result['route'], 'DEPARTED_INITIAL_AND_SUSTAINED_OTHER_REFERENCE')
        self.assertEqual(result['first_other_support_frame'], 30)
        self.assertEqual(result['sampled_span_ns'], 19)
        self.assertEqual(q.path_summary(['outside']+path, 'closed', 20)['route'], 'INITIAL_OUTSIDE_OR_AMBIGUOUS_REFERENCE_SUPPORT')

    def test_state_requires_both_supports_not_lower_unscaled_score(self):
        calibration = {'geometry_A': {'open': 2, 'closed': 2},
                       'contact_A': {'deposited_uniform': {'open': .1, 'closed': 1}}}
        labels = q.classify({'open': [1, 1, 4], 'closed': [4, 1, 4]},
                            {'open': [.05, .05, 0], 'closed': [0, 0, 0]}, calibration, q.METHODS[0])
        self.assertEqual(labels.tolist(), ['open', 'ambiguous', 'outside'])


if __name__ == '__main__':
    unittest.main()
