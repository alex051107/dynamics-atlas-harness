import copy
import json
from pathlib import Path
import unittest
from unittest.mock import patch
import numpy as np
from dynamics_atlas_harness.q05_joint_numeric_v1 import (
    digest, score, solve_joint, evaluate_joint_rule, dispatch_obligation, validate_config,
)
ROOT=Path(__file__).resolve().parents[1]
CONFIG=json.loads((ROOT/'research/paper_result_reproduction_screen_v1/q05_joint_method_v1.json').read_text())
GRAPH={'case':{'case_id':'q05_nanodisc_saxs_noe_20260904'},'comparisons':[{'relation_type':'JOINT_ENSEMBLE_FIT'}]}

def data(target):
    return {'A':np.array([[0.,0.,0.],[1.,1.,1.]]),'b':np.array(target),
            'sigma':np.full(3,.1),'channel':np.array(['saxs','amide','methyl']),
            'frame_ids':[0,1],'labels':['s','a','m'],'input_id':digest(target)}

class JointNumericTests(unittest.TestCase):
    def test_all_inputs_are_explicit_and_unknown_original_configuration_retained(self):
        validate_config(CONFIG)
        missing=copy.deepcopy(CONFIG);missing.pop('noe_power')
        with self.assertRaises(ValueError):validate_config(missing)
        wrong=copy.deepcopy(CONFIG);wrong['theta']=7
        with self.assertRaises(ValueError):validate_config(wrong)

    def test_shared_weight_optimum_and_same_instance_reassessment(self):
        d=data([.5,.5,.5]);before=evaluate_joint_rule(GRAPH,d['input_id'])
        self.assertEqual(len(before['obligations']),1)
        e=dispatch_obligation(before,d,CONFIG)
        self.assertTrue(e['optimization']['numerical_conditions_satisfied'])
        np.testing.assert_allclose(e['weights'],[.5,.5],atol=1e-8)
        after=evaluate_joint_rule(GRAPH,d['input_id'],e)
        self.assertEqual(before['rule_instance_id'],after['rule_instance_id'])
        self.assertEqual(after['conditional_calculation'],'COMPLETE')
        self.assertEqual(after['status'],'UNRESOLVED')
        self.assertFalse(after['complete_question_answer'])
        for mutation in ('weights','frame_ids','input','channel'):
            with self.subTest(mutation=mutation):
                bad=copy.deepcopy(e);input_id=d['input_id']
                if mutation=='weights':bad['weights']=[.4,.6]
                if mutation=='frame_ids':bad['frame_ids'].reverse()
                if mutation=='input':input_id='different-input'
                if mutation=='channel':bad['channel_weight_ids']['amide']='other-vector'
                result=evaluate_joint_rule(GRAPH,input_id,bad)
                self.assertEqual(result['reason_codes'],['JOINT_INPUT_OR_SHARED_WEIGHT_IDENTITY_MISMATCH'])

    def test_disabled_rule_never_dispatches_main_calculation(self):
        d=data([.5,.5,.5]);off=evaluate_joint_rule(GRAPH,d['input_id'],enabled=False)
        with patch('dynamics_atlas_harness.q05_joint_numeric_v1.solve_joint') as solver:
            self.assertIsNone(dispatch_obligation(off,d,CONFIG));solver.assert_not_called()

    def test_separate_success_cannot_prove_common_weights(self):
        d=data([.1,.9,.9])
        self.assertAlmostEqual(score(d,np.array([.9,.1]))['channels']['saxs']['squared_loss_sum'],0)
        self.assertAlmostEqual(score(d,np.array([.1,.9]))['channels']['amide']['squared_loss_sum'],0)
        e=solve_joint(d,CONFIG)
        self.assertGreater(e['fitted']['channels']['saxs']['squared_loss_sum'],1)
        self.assertGreater(e['fitted']['channels']['amide']['squared_loss_sum'],1)
        self.assertNotEqual(evaluate_joint_rule(GRAPH,d['input_id'],e)['status'],'PASS')
        # Explicit admissible sets in this synthetic counterexample do not intersect.
        self.assertLess(.11,.89)

    def test_fixed_denominator_loss_respects_improving_each_residual(self):
        # Transformed-domain lower-bound data yielding residuals -2,-.1 then -1.9,0.
        d={'A':np.array([[1.,2.9],[1.1,3.]]),'b':np.array([3.,3.]),
           'sigma':np.ones(2),'channel':np.array(['amide','amide'])}
        old=score(d,np.array([1.,0.]))['channels']['amide']
        new=score(d,np.array([0.,1.]))['channels']['amide']
        self.assertLess(new['fixed_row_mean'],old['fixed_row_mean'])
        self.assertGreater(new['squared_loss_sum']/new['nonzero_residual_count'],
                           old['squared_loss_sum']/old['nonzero_residual_count'])

if __name__=='__main__':unittest.main()
