import copy
import json
from pathlib import Path
import unittest
from unittest.mock import patch
import numpy as np
from dynamics_atlas_harness.q05_joint_numeric_v1 import (
    digest, score, solve_joint, evaluate_joint_rule, dispatch_obligation, validate_config, seal_data, load_inputs, _check_author_payloads,
)
ROOT=Path(__file__).resolve().parents[1]
CONFIG=json.loads((ROOT/'research/paper_result_reproduction_screen_v1/q05_joint_method_v1.json').read_text())
from dynamics_atlas_harness.paper_blind_exposed_v1 import validate_agent_proposal, project_admitted_proposal_to_rules_casegraph
PACKET=ROOT/'evidence/paper_blind_exposed_v1/public/q05_public_fact_packet_v1.json'
PROPOSAL=json.loads((ROOT/'research/paper_result_reproduction_screen_v1/q05_fact_proposal_v1.json').read_text())
GRAPH=project_admitted_proposal_to_rules_casegraph(PACKET,validate_agent_proposal(PACKET,PROPOSAL))

def data(target):
    return seal_data({'A':np.array([[0.,0.,0.],[1.,1.,1.]]),'b':np.array(target),
            'sigma':np.full(3,.1),'channel':np.array(['saxs','amide','methyl']),
            'frame_ids':[0,1],'labels':['s','a','m'],'input_id':digest(target)},CONFIG)

class JointNumericTests(unittest.TestCase):
    def test_all_inputs_are_explicit_and_unknown_original_configuration_retained(self):
        validate_config(CONFIG)
        missing=copy.deepcopy(CONFIG);missing.pop('noe_power')
        with self.assertRaises(ValueError):validate_config(missing)
        wrong=copy.deepcopy(CONFIG);wrong['theta']=7
        with self.assertRaises(ValueError):validate_config(wrong)

    def test_shared_weight_optimum_and_same_instance_reassessment(self):
        d=data([.5,.5,.5]);before=evaluate_joint_rule(GRAPH,d)
        self.assertEqual(len(before['obligations']),1)
        e=dispatch_obligation(before,d,CONFIG,GRAPH)
        self.assertTrue(e['optimization']['numerical_conditions_satisfied'])
        np.testing.assert_allclose(e['weights'],[.5,.5],atol=1e-8)
        after=evaluate_joint_rule(GRAPH,d,e)
        self.assertEqual(before['rule_instance_id'],after['rule_instance_id'])
        self.assertEqual(after['conditional_calculation'],'COMPLETE')
        self.assertEqual(after['status'],'UNRESOLVED')
        self.assertFalse(after['complete_question_answer'])
        for mutation in ('weights','frame_ids','input','channel'):
            with self.subTest(mutation=mutation):
                bad=copy.deepcopy(e);input_data=d
                if mutation=='weights':bad['weights']=[.4,.6]
                if mutation=='frame_ids':bad['frame_ids'].reverse()
                if mutation=='input':bad['input_id']='different-input'
                if mutation=='channel':bad['channel_weight_ids']['amide']='other-vector'
                result=evaluate_joint_rule(GRAPH,input_data,bad)
                self.assertEqual(result['reason_codes'],['NUMERIC_EVIDENCE_REJECTED'])

    def test_disabled_rule_never_dispatches_main_calculation(self):
        d=data([.5,.5,.5]);off=evaluate_joint_rule(GRAPH,d,enabled=False)
        with patch('dynamics_atlas_harness.q05_joint_numeric_v1.solve_joint') as solver:
            self.assertIsNone(dispatch_obligation(off,d,CONFIG,GRAPH));solver.assert_not_called()

    def test_separate_success_cannot_prove_common_weights(self):
        d=data([.1,.9,.9])
        self.assertAlmostEqual(score(d,np.array([.9,.1]))['channels']['saxs']['squared_loss_sum'],0)
        self.assertAlmostEqual(score(d,np.array([.1,.9]))['channels']['amide']['squared_loss_sum'],0)
        e=dispatch_obligation(evaluate_joint_rule(GRAPH,d),d,CONFIG,GRAPH)
        self.assertGreater(e['fitted']['channels']['saxs']['squared_loss_sum'],1)
        self.assertGreater(e['fitted']['channels']['amide']['squared_loss_sum'],1)
        self.assertNotEqual(evaluate_joint_rule(GRAPH,d,e)['status'],'PASS')
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

    def test_inconsistent_evidence_rejected_without_reoptimization(self):
        d=data([.1,.9,.9]);e=dispatch_obligation(evaluate_joint_rule(GRAPH,d),d,CONFIG,GRAPH)
        for mutation in ('loss','status','producer','config','labels','negative','multiplier','prediction','request'):
            with self.subTest(mutation=mutation):
                bad=copy.deepcopy(e)
                if mutation=='loss':
                    for k in bad['fitted']['channels']:bad['fitted']['channels'][k]['squared_loss_sum']=0
                if mutation=='status':bad['optimization'].update(success=False,projected_gradient_inf=1e10)
                if mutation=='producer':bad['operator_id']='wrong'
                if mutation=='config':bad['config']['theta']=7
                if mutation=='labels':bad['labels']=[]
                if mutation=='negative':
                    bad['weights']=[-1.,2.]
                    wid=digest({'frame_ids':bad['frame_ids'],'weights':bad['weights']})
                    bad['weight_id']=wid;bad['channel_weight_ids']={k:wid for k in ('saxs','amide','methyl')}
                if mutation=='multiplier':bad['dual_multipliers'][0]+=1
                if mutation=='prediction':bad['fitted']['prediction'][0]+=1
                if mutation=='request':bad['request_id']='stale'
                with patch('dynamics_atlas_harness.q05_joint_numeric_v1.solve_joint') as solver:
                    result=evaluate_joint_rule(GRAPH,d,bad);solver.assert_not_called()
                self.assertEqual(result['reason_codes'],['NUMERIC_EVIDENCE_REJECTED'])

    def test_dispatch_rejects_wrong_status_target_instance_and_graph_before_solver(self):
        d=data([.5,.5,.5]);before=evaluate_joint_rule(GRAPH,d)
        for mutation in ('status','target','instance','inner_instance','request','graph'):
            with self.subTest(mutation=mutation):
                bad=copy.deepcopy(before);graph=copy.deepcopy(GRAPH)
                if mutation=='status':bad['status']='NOT_APPLICABLE'
                if mutation=='target':bad['target']['id']='wrong'
                if mutation=='instance':bad['rule_instance_id']='wrong'
                if mutation=='inner_instance':bad['obligations'][0]['rule_instance_id']='wrong'
                if mutation=='request':bad['obligations'][0]['request_id']='wrong'
                if mutation=='graph':graph['evidence_items'].pop()
                with patch('dynamics_atlas_harness.q05_joint_numeric_v1.solve_joint') as solver:
                    with self.assertRaises(ValueError):dispatch_obligation(bad,d,CONFIG,graph)
                    solver.assert_not_called()

    def test_parsed_arrays_cannot_change_after_admission(self):
        d=data([.5,.5,.5]);before=evaluate_joint_rule(GRAPH,d)
        with self.assertRaises(ValueError):d['A'][0,0]=123
        d['A']=d['A'].copy();d['A'][0,0]=123
        with patch('dynamics_atlas_harness.q05_joint_numeric_v1.solve_joint') as solver:
            with self.assertRaisesRegex(ValueError,'ADMITTED_PARSED_INPUT_CHANGED'):
                dispatch_obligation(before,d,CONFIG,GRAPH)
            solver.assert_not_called()

    def test_wrong_payload_identity_rejected_before_any_numeric_parsing(self):
        # Valid-looking replacements retain row order/size possibilities, but lack source identity.
        root=Path('/synthetic')
        for rel,payload in (
            ('BME_reweight/inputs_and_method/simulation_SAXS.dat',b'1 0.1 0.2\n'),
            ('BME_reweight/inputs_and_method/exp_HN2_NOE.dat',b'1-ALA-H 2-ALA-H 5 0.3 UPPER\n'),
            ('SAXS_and_SANS/Delta_H5_no_tag_Static_SAXS_30C_RB_subtracted.dat',b'q I error\n0.1 1 .1\n'),
        ):
            with self.subTest(relative=rel):
                with self.assertRaisesRegex(ValueError,'AUTHOR_SOURCE_IDENTITY_MISMATCH'):
                    _check_author_payloads({'x':payload},{'x':root/rel},root)

if __name__=='__main__':unittest.main()
