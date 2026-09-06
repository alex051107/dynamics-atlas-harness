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

    def fixture(self):
        repetitions=[{'pair':'pair','condition':c,'repetition':str(i),'E':{'n':10,'mean':v+i*.005}} for c,v in [('apo',.2),('holo',.3)] for i in range(3)]
        comparison=r.main_method.group_difference(repetitions)
        main={'input_id':'source','policy':r.main_method.POLICY,'files':[{'eligible_negative_corrected_count_events':1}],'repetitions':repetitions,'condition_comparisons':comparison}
        facts={'clipping_discrepancy_verified':True};before=r.evaluate(main,facts)
        evidence={'operator_id':r.OPERATOR_ID,'policy':r.main_method.POLICY,'input_id':'source','rule_instance_id':before['rule_instance_id'],'alternatives':{a:{'repetitions':copy.deepcopy(repetitions),'condition_comparisons':copy.deepcopy(comparison),'selected_events':60} for a in r.ALTERNATIVES}}
        return main,facts,evidence

    def test_evidence_changes_method_judgment_but_not_full_science(self):
        main,facts,evidence=self.fixture();stable=r.dispatch(main,facts,lambda _:evidence)
        self.assertEqual(stable['operator_calls'],1)
        self.assertEqual(stable['after']['method_disposition'],'DIRECTION_STABLE_FOR_TWO_CHECKED_ALTERNATIVES')
        alt=evidence['alternatives'][r.ALTERNATIVES[1]]
        for rep in alt['repetitions']:
            if rep['condition']=='holo':rep['E']['mean']-=.2
        alt['condition_comparisons']=r.main_method.group_difference(alt['repetitions'])
        changed=r.evaluate(main,facts,evidence)
        self.assertEqual(changed['method_disposition'],'DIRECTION_DEPENDS_ON_BACKGROUND_HANDLING')
        self.assertEqual(changed['operator_obligations'],[])
        self.assertEqual(changed['scientific_question_status'],'INCOMPLETE')
        self.assertEqual(changed['rule_instance_id'],stable['before']['rule_instance_id'])
        evidence['input_id']='other source'
        with self.assertRaisesRegex(ValueError,'BINDING'):r.evaluate(main,facts,evidence)

    def test_inconsistent_repetitions_producer_method_and_missing_rejected(self):
        main,facts,original=self.fixture()
        for mutation in ['repetition','producer','method','missing','selected','duplicate']:
            e=copy.deepcopy(original);alt=e['alternatives'][r.ALTERNATIVES[0]]
            if mutation=='repetition':alt['repetitions'][-1]['E']['mean']+=.5
            if mutation=='producer':e['operator_id']='wrong'
            if mutation=='method':e['policy']['gamma']=7
            if mutation=='missing':alt.pop('repetitions')
            if mutation=='selected':alt['selected_events']+=1
            if mutation=='duplicate':alt['repetitions'][-1]=alt['repetitions'][-2]
            with self.subTest(mutation=mutation),self.assertRaises(ValueError):r.evaluate(main,facts,e)
        self.assertEqual(r.evaluate(main,facts)['operator_obligations'],[r.OPERATOR_ID])


if __name__ == '__main__':
    unittest.main()
