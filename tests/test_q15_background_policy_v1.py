import copy
import unittest

import numpy as np

from dynamics_atlas_harness import q15_background_policy_v1 as r


class BackgroundPolicyTests(unittest.TestCase):
    def test_literal_source_keeps_sequential_cross_channel_behavior(self):
        # 1 ms exposure gives [DD,DA,AA]=[-1,4,4], [4,-1,4], [4,4,-1].
        policy = {'background_kHz_DD_DA_AA': [2,2,2], 'alpha':0, 'delta':0,
                  'gamma':1, 'beta':1, 'minimum_raw_photons':0,
                  'stoichiometry_open_interval':[.25,.75]}
        counts = [[1,6,6],[6,1,6],[6,6,1]]
        literal = r.corrected_alternative(counts, [.001]*3, r.ALTERNATIVES[0], policy)
        intended = r.corrected_alternative(counts, [.001]*3, r.ALTERNATIVES[1], policy)
        np.testing.assert_array_equal(literal['corrected_counts_DD_DA_AA'], [[-1,4,4],[4,0,4],[4,0,-1]])
        np.testing.assert_array_equal(intended['corrected_counts_DD_DA_AA'], [[0,4,4],[4,0,4],[4,4,0]])
        self.assertGreater(literal['E'][0], 1)  # No later E clipping.

    def test_real_trigger_and_rule_off(self):
        main = {'input_id':'source', 'files':[{'eligible_negative_corrected_count_events':1}],
                'condition_comparisons': {'pair': {'holo_minus_apo_E':.1,'all_cross_repetition_difference_range':[.02,.2]}}}
        facts = {'clipping_discrepancy_verified':True}
        self.assertEqual(r.evaluate(main,facts)['operator_obligations'],[r.OPERATOR_ID])
        def forbidden(_):
            self.fail('Disabled or non-triggered operator invoked')
        self.assertEqual(r.dispatch(main,facts,forbidden,False)['operator_calls'],0)
        self.assertEqual(r.dispatch(main,{},forbidden)['operator_calls'],0)

    def test_evidence_changes_method_judgment_but_not_full_science(self):
        comparison = {'holo_minus_apo_E':.1,'all_cross_repetition_difference_range':[.02,.2]}
        main = {'input_id':'source','files':[{'eligible_negative_corrected_count_events':1}],
                'condition_comparisons':{'pair':comparison}}
        facts={'clipping_discrepancy_verified':True}
        before=r.evaluate(main,facts)
        evidence={'input_id':'source','rule_instance_id':before['rule_instance_id'],
                  'alternatives':{a:{'condition_comparisons':{'pair':copy.deepcopy(comparison)}} for a in r.ALTERNATIVES}}
        stable=r.dispatch(main,facts,lambda _:evidence)
        self.assertEqual(stable['operator_calls'],1)
        self.assertEqual(stable['after']['method_disposition'],'DIRECTION_STABLE_FOR_TWO_CHECKED_ALTERNATIVES')
        evidence['alternatives'][r.ALTERNATIVES[1]]['condition_comparisons']['pair']['all_cross_repetition_difference_range']=[-.01,.2]
        changed=r.evaluate(main,facts,evidence)
        self.assertEqual(changed['method_disposition'],'DIRECTION_DEPENDS_ON_BACKGROUND_HANDLING')
        self.assertEqual(changed['scientific_question_status'],'INCOMPLETE')
        self.assertEqual(changed['rule_instance_id'],before['rule_instance_id'])
        evidence['input_id']='other source'
        with self.assertRaisesRegex(ValueError,'BINDING'):
            r.evaluate(main,facts,evidence)


if __name__ == '__main__':
    unittest.main()
