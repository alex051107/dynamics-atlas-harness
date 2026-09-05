import copy
import unittest
from dynamics_atlas_harness import q15_cross_modal_evidence_v1 as q


def inputs():
    main={'input_id':'x','condition_comparisons':{p:{'holo_minus_apo_E':.1 if p=='55_175' else -.1} for p in q.PAIRS}}
    summary={'input_id':'x','diagnostics':{p:{'equal_repetition_mean_effect':r['holo_minus_apo_E'],
              'equal_repetition_median_effect':r['holo_minus_apo_E'],'leave_one_per_condition_effects':[r['holo_minus_apo_E']]*9} for p,r in main['condition_comparisons'].items()}}
    deer={'source_role':'AUTHOR_PROCESSED_DEER_DISTRIBUTION_NOT_RAW_TRACE_REINVERSION',
          'curves':[{'pair':p.replace('_','/'),'condition':s,'mean_source_axis_units':v} for p in q.PAIRS for s,v in [('apo',50),('holo',40)]]}
    forward={'pairs':{p:{k:{'apo':50,'holo':40} for k in ['FRET_sim','PELDOR_sim']} for p in q.PAIRS},
             'system':'HiSiaP','doi':'10.1038/s41467-022-31945-6','source_role':'AUTHOR_COMPUTED_FORWARD_NOT_LOCAL_SIMULATION'}
    return main,summary,deer,forward


class CrossModalTests(unittest.TestCase):
    def test_evidence_off_and_missing_dye_branch(self):
        args=inputs();e=q.synthesize_manual_evidence(*args)
        self.assertEqual(q.evaluate(args[0],e,False)['evidence_applications'],0)
        after=q.evaluate(args[0],e)
        self.assertEqual(after['new_numerical_operator_calls'],0)
        self.assertFalse(after['full_question_answer'])
        self.assertIn('TMR_CY5_DOUBLE_LABEL_DATA_AND_CALIBRATION',after['remaining_obligations'])
        self.assertEqual({r['pair']:r['fluorescence_relation'] for r in after['partial_claims']},
                         {'55_175':'DIRECTIONAL_AGREEMENT_WITH_REFERENCE_READOUT','175_228':'DIRECTIONAL_TENSION_WITH_REFERENCE_READOUT'})

    def test_direction_counterfacts_change_scientific_relations(self):
        args=inputs();args[2]['curves'][1]['mean_source_axis_units']=60
        e=q.synthesize_manual_evidence(*args)
        self.assertEqual(sum(r['DEER_direction_matches_own_spin_prediction'] for r in e['rows']),1)
        args[1]['diagnostics']['175_228']['leave_one_per_condition_effects'][0]=.01
        e=q.synthesize_manual_evidence(*args)
        row=next(r for r in e['rows'] if r['pair']=='175_228')
        self.assertEqual(row['fluorescence_relation'],'DESCRIPTIVE_DIRECTION_UNRESOLVED')

    def test_unmatched_input_or_probe_cannot_close_rule(self):
        args=inputs();args[1]['input_id']='other'
        with self.assertRaisesRegex(ValueError,'INPUT_MISMATCH'):q.synthesize_manual_evidence(*args)
        args=inputs();e=q.synthesize_manual_evidence(*args);e['rows'][0]['pair']='another'
        with self.assertRaisesRegex(ValueError,'PAIR_BINDING'):q.evaluate(args[0],e)
        args=inputs();args[3]['source_role']='AUTHOR_FITTED_EXPERIMENTAL_TARGET'
        with self.assertRaisesRegex(ValueError,'SOURCE_REQUIRED'):q.synthesize_manual_evidence(*args)


if __name__=='__main__':unittest.main()
