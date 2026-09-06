import copy
import unittest
from unittest.mock import patch
from dynamics_atlas_harness import forward_bridge_use_v1 as f


def fixture(change=.1):
    scope=dict(source_id='s',model_id='reference',observable='efficiency',probe='dye-a',condition='apo:holo',unit='1',aggregation='mean-efficiency',target_support='paired-conditions')
    use=dict(contract=f.CONTRACT,use_id='u',scope=scope,method_id='efficiency_weighted_reference_direction_v1',input_ref='i',requested_use='MODEL_OBSERVATION_COMPARISON')
    value=dict(scope=scope,method_id=use['method_id'],data=dict(reference_definition='EFFICIENCY_WEIGHTED_DISTANCE',observed_change=change,reference_apo=6.,reference_holo=5.,direction_checks=[change,change*.9]))
    context=dict(inputs={'i':value},admissions={'i':dict(input_digest=f.digest(value),source_receipts=['test-only admitted source'],method_basis='synthetic stable-probe hypothesis',conditional_assumptions=['stable-probe reference hypothesis'],authority_binding=dict(source_id='s',source_version='test-source-v1',measurement_version='test-measurement-v1',relationship_to_graph='LATER_ADMITTED_SOURCE_FOR_CURRENT_USE',relevant_contradictions=[]))})
    graph=dict(evidence_items=[dict(source_id='s')],forward_bridge_uses=[use])
    return graph,context


def admit_evidence(graph,context):
    u=graph['forward_bridge_uses'][0];v=context['inputs']['i']
    context['evidence']={'u':dict(use_digest=f.digest(u),input_digest=f.digest(v),numerical=f.numerical_check(u['method_id'],v['data']))}


class BridgeUseTest(unittest.TestCase):
    def test_compatible_and_conflict_are_completed_not_missing(self):
        for effect,support in [(.1,True),(-.1,False)]:
            g,c=fixture(effect);admit_evidence(g,c);r=f.evaluate_uses(g,c)[0]
            self.assertTrue(r['check_completed']);self.assertEqual(r['local_support'],support)
            self.assertEqual(r['route'],'DIRECT_EVALUATION');self.assertFalse(r['full_question_answer'])

    def test_description_needs_no_model_and_population_not_licensed(self):
        g,c=fixture();g['forward_bridge_uses'][0]['requested_use']='OBSERVATION_DESCRIPTION'
        self.assertEqual(f.evaluate_uses(g,{})[0]['status'],'NOT_APPLICABLE')
        g['forward_bridge_uses'][0]['requested_use']='STRUCTURAL_POPULATION';admit_evidence(g,c)
        r=f.evaluate_uses(g,c)[0];self.assertTrue(r['local_support'])
        self.assertIn('STRUCTURAL_ASSIGNMENT_AND_IDENTIFIABILITY',r['remaining_obligations'])

    def test_missing_vs_wrong_scope_vs_forged_numbers(self):
        g,c=fixture();self.assertEqual(f.evaluate_uses(g,c)[0]['route'],'REGISTERED_OPERATOR')
        g['forward_bridge_uses'][0]['scope']=dict(g['forward_bridge_uses'][0]['scope'],probe='different-dye')
        self.assertEqual(f.evaluate_uses(g,c)[0]['route'],'SOURCE_LOOKUP')
        g,c=fixture();admit_evidence(g,c);c['evidence']['u']['numerical']['observed_change']=99
        with self.assertRaisesRegex(ValueError,'NUMERICAL_EVIDENCE'):f.evaluate_uses(g,c)

    def test_mean_distance_and_unadmitted_source_rejected(self):
        g,c=fixture();c['inputs']['i']['data']['reference_definition']='MEAN_DISTANCE'
        with self.assertRaisesRegex(ValueError,'PREVIOUSLY_ADMITTED'):f.evaluate_uses(g,c)
        with self.assertRaisesRegex(ValueError,'EFFICIENCY_WEIGHTED'):f.numerical_check(g['forward_bridge_uses'][0]['method_id'],c['inputs']['i']['data'])

    def test_identity_rebinding_preserves_scientific_relation(self):
        g,c=fixture();admit_evidence(g,c);expected=f.evaluate_uses(g,c)[0]['local_support']
        g['evidence_items'][0]['source_id']='renamed-source';u=g['forward_bridge_uses'][0];u['use_id']='renamed-use';u['scope']['source_id']='renamed-source'
        c['admissions']['i']['authority_binding']['source_id']='renamed-source'
        c['admissions']['i']['input_digest']=f.digest(c['inputs']['i'])
        c['evidence']={u['use_id']:dict(use_digest=f.digest(u),input_digest=f.digest(c['inputs']['i']),numerical=f.numerical_check(u['method_id'],c['inputs']['i']['data']))}
        self.assertEqual(f.evaluate_uses(g,c)[0]['local_support'],expected)

    def test_deer_prefix_and_target_window_are_distinct(self):
        import numpy as np
        from dynamics_atlas_harness import q16_shape_flexibility_v1 as d
        t=np.arange(20)*.032;candidate=dict(k=0.,p=0.,unmodulated_amplitude=.7,grid_weights=[[0,.3]])
        y=.7+d.kernel(t)[:,0]*.3
        raw=np.column_stack([t,y,np.sin(np.arange(20))*.001]).tolist()
        value=dict(training_record=dict(source_key='record',raw_time_real_imaginary=raw[:12]),target_record=dict(source_key='record',raw_time_real_imaginary=raw),candidate=candidate)
        r=f.numerical_check('fixed_deer_prediction_screen_v1',value)
        self.assertLess(r['rms'],1e-14);self.assertEqual(r['target_support'],[float(t[12]),float(t[-1]),8])
        value['target_record']['source_key']='other'
        with self.assertRaisesRegex(ValueError,'DIFFERENT_RECORD'):f.numerical_check('fixed_deer_prediction_screen_v1',value)

    def test_unknown_scientific_identity_or_basis_is_a_specific_gap(self):
        for field,bad in [('model_id','UNKNOWN'),('probe',{}),('condition',[]),('unit','')]:
            g,c=fixture();g['forward_bridge_uses'][0]['scope'][field]=bad;c['inputs']['i']['scope']=g['forward_bridge_uses'][0]['scope']
            c['admissions']['i']['input_digest']=f.digest(c['inputs']['i']);admit_evidence(g,c)
            r=f.evaluate_uses(g,c)[0]
            self.assertEqual(r['route'],'SOURCE_LOOKUP');self.assertIn('SCIENTIFIC_SCOPE_',r['reason']);self.assertFalse(r['check_completed'])
        g,c=fixture();c['admissions']['i']['method_basis']='UNKNOWN';admit_evidence(g,c)
        r=f.evaluate_uses(g,c)[0]
        self.assertEqual(r['reason'],'METHOD_BASIS_OR_CONDITIONAL_ASSUMPTION_UNAVAILABLE');self.assertFalse(r['check_completed'])

    def test_conditional_assumption_is_preserved_and_authority_conflicts_are_local(self):
        g,c=fixture();admit_evidence(g,c)
        self.assertEqual(f.evaluate_uses(g,c)[0]['conditional_assumptions'],['stable-probe reference hypothesis'])
        g['evidence_items'][0]['data_lineage_status']='CONTRADICTED'
        r=f.evaluate_uses(g,c)[0];self.assertEqual(r['reason'],'SOURCE_MEASUREMENT_AUTHORITY_CONFLICT')
        c['admissions']['i']['authority_binding']['relationship_to_graph']='SUPERSEDES_NONAUTHORITATIVE_PROPOSAL'
        self.assertTrue(f.evaluate_uses(g,c)[0]['check_completed'])

    def test_deer_target_with_zero_imaginary_trailing_values_needs_no_target_noise(self):
        import numpy as np
        from dynamics_atlas_harness import q16_shape_flexibility_v1 as d
        t=np.arange(20)*.032;candidate=dict(k=0.,p=0.,unmodulated_amplitude=.7,grid_weights=[[0,.3]])
        y=.7+d.kernel(t)[:,0]*.3
        raw=np.column_stack([t,y,np.r_[np.sin(np.arange(12))*.001,np.zeros(8)]]).tolist()
        value=dict(training_record=dict(source_key='record',raw_time_real_imaginary=raw[:12]),target_record=dict(source_key='record',raw_time_real_imaginary=raw),candidate=candidate)
        r=f.numerical_check('fixed_deer_prediction_screen_v1',value)
        self.assertLess(r['rms'],1e-14);self.assertGreater(r['training_noise'],0)
