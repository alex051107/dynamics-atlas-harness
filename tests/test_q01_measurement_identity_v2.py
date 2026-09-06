import copy
import unittest
import numpy as np
from dynamics_atlas_harness import q01_path_comparison_v1 as q
from dynamics_atlas_harness import q01_relative_paths_v1 as r
from dynamics_atlas_harness import q01_measurement_identity_v2 as b


class MeasurementIdentity(unittest.TestCase):
    def setUp(self):
        self.contacts = [{'state': 'open', 'dviol_angstrom': 10.},
                         {'state': 'closed', 'dviol_angstrom': 8.5}]
        self.refs = {s+'_'+role: np.zeros((2, 2, 3)) for s in q.STATES for role in ('core', 'lid')}
        self.refs.update(open_distances_A=np.array([[9., 20.]]*2),
                         closed_distances_A=np.array([[20., 8.]]*2))
        self.policy = r.reference_policy({s: self.refs[s+'_distances_A'] for s in q.STATES}, self.contacts)
        distances = np.tile([9., 20.], (1001, 1)); distances[:100] = [20., 8.]
        self.records = {'a': {'seed': 'closed', 'time_ns': np.arange(20, 1021),
                             'distances_A': distances,
                             'geometry_A': {'open': np.full(1001, 9.), 'closed': np.full(1001, 8.)}}}
        self.mappings = [{'name': 'a', 'seed': 'closed', 'mapping': {'columns': 'synthetic'}}]
        self.facts = {'input_id': 'source', 'method_id': 'method'}
        self.manifest = b.measurement_manifest(self.records, self.contacts, self.refs, self.mappings, self.facts)

    def test_changed_continuous_values_keep_parent_report_but_are_rejected(self):
        calibration = {'geometry_A': {'open': 2., 'closed': 2.},
                       'contact_A': {m: {'open': 0., 'closed': 0.} for m in q.METHODS}}
        parent, _ = q.summarize(self.records, self.contacts, calibration)
        old, _ = r.compare(self.records, self.contacts, self.policy)
        self.records['a']['geometry_A']['closed'][100:] = 10.
        changed, _ = q.summarize(self.records, self.contacts, calibration)
        new, _ = r.compare(self.records, self.contacts, self.policy)
        self.assertEqual(parent, changed)
        self.assertNotEqual(old['rows'][0]['paths']['20']['category'], new['rows'][0]['paths']['20']['category'])
        with self.assertRaisesRegex(ValueError, 'CONTINUOUS_MEASUREMENT'):
            b.verify_manifest(self.manifest, self.records, self.contacts, self.refs, self.mappings, self.facts)

    def test_roles_mapping_seed_time_and_reference_are_bound(self):
        b.verify_manifest(self.manifest, self.records, self.contacts, self.refs, self.mappings, self.facts)
        for mutation in ('role', 'mapping', 'time', 'seed', 'reference'):
            rec, maps, refs = copy.deepcopy(self.records), copy.deepcopy(self.mappings), copy.deepcopy(self.refs)
            if mutation == 'role': rec['a']['distances_A'] = rec['a']['distances_A'][:, ::-1]
            if mutation == 'mapping': maps[0]['mapping']['columns'] = 'other'
            if mutation == 'time': rec['a']['time_ns'][100] += 1
            if mutation == 'seed': rec['a']['seed'] = 'open'
            if mutation == 'reference': refs['open_core'][0, 0, 0] += .1
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                b.verify_manifest(self.manifest, rec, self.contacts, refs, maps, self.facts)

    def test_arbitrary_normalization_and_unsupported_policy_rejected(self):
        identity = self.manifest['reference_id']
        b.verify_policy(self.policy, self.refs, self.contacts, identity)
        altered = copy.deepcopy(self.policy)
        altered['normalization'][q.METHODS[0]]['mid'][0] += 1
        with self.assertRaisesRegex(ValueError, 'NOT_SOURCE_DERIVED'):
            b.verify_policy(altered, self.refs, self.contacts, identity)
        altered = copy.deepcopy(self.policy); altered['policy']['primary_persistence_frames'] = 37
        with self.assertRaisesRegex(ValueError, 'UNSUPPORTED_RELATIVE_POLICY'):
            r.compare(self.records, self.contacts, altered)
        self.assertEqual(r.POLICY['primary_persistence_frames'], 20)

    def test_partial_coverage_lists_unhandled_paths(self):
        envelope = {'paths': [{'trajectory': 'covered', 'persistence_results': {'20': {'initial_support': 'open'}}},
                              {'trajectory': 'missing', 'persistence_results': {'20': {'initial_support': 'outside'}}}]}
        base = {'facts_id': q.identity(self.facts), 'rule_id': q.RULE_ID, 'instance_id': 'same',
                'status': 'COMPARISON_EXECUTED', 'numeric_result': envelope}
        result = r.evaluate(base, self.facts, envelope, self.policy)
        self.assertEqual(result['unhandled_initial_support_trajectories'], ['missing'])
        self.assertEqual(result['operator_requests'], [])

    def test_relative_reversal_does_not_prove_absolute_approach(self):
        labels, _, _ = r.preference({'open': [3., 5.], 'closed': [1., 6.]},
                                   {'open': [20., 0.], 'closed': [0., 100.]},
                                   {'mid': [10., 50.], 'delta': [20., -100.]})
        self.assertEqual(labels.tolist(), ['closed', 'open'])
        self.assertGreater(5., 3.)


if __name__ == '__main__':
    unittest.main()
