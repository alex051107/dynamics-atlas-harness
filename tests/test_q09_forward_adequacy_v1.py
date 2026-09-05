import copy
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch
import numpy as np
from scipy.integrate import quad
from dynamics_atlas_harness import q09_forward_adequacy_v1 as q
from dynamics_atlas_harness.q09_fluorescence_v1 import PQPair, bin_factor, transfer_survival, expected_counts, poisson_deviance
from dynamics_atlas_harness.paper_blind_exposed_v1 import validate_agent_proposal, project_admitted_proposal_to_rules_casegraph

REPO=Path(__file__).resolve().parents[1]
PACKET=REPO/'evidence/paper_blind_exposed_v1/public/q09_public_fact_packet_v1.json'
PROPOSAL=REPO/'research/paper_result_reproduction_screen_v1/q09_fact_proposal_v1.json'


def graph():return project_admitted_proposal_to_rules_casegraph(PACKET,validate_agent_proposal(PACKET,json.loads(PROPOSAL.read_text())))


def synthetic():
    d=PQPair.__new__(PQPair);d.dt=.008;d.t=np.arange(32)*d.dt;d.y={'D0':np.ones(32)*20,'DA':np.ones(32)*10};h=np.zeros(32);h[3]=100
    d.irf={'D0':h.copy(),'DA':h.copy()};d.irf_baseline={'D0':0.,'DA':0.};d.lin=np.ones(32);d.mask=np.ones(32,bool)
    nodes,weights=np.polynomial.legendre.leggauss(32);d.r=(nodes+1)*90;d.qweights=weights*90;d.rates=.224*(2/3)*(56.4/d.r)**6;d.transfer_exp=np.exp(-d.t[:,None]*d.rates)
    d.baseline=[1.,4.,.2,35.,65.,.5,.1,.001,0.,.001,0.];d.source_identity={'synthetic':True};d.input_id=q._input_identity(d);return d


class Q09AdequacyTests(unittest.TestCase):
    def test_wrong_case_and_forbidden_operator_proposals_rejected(self):
        proposal=json.loads(PROPOSAL.read_text());proposal['case_id']='other'
        with self.assertRaises(ValueError):validate_agent_proposal(PACKET,proposal)
        proposal=json.loads(PROPOSAL.read_text());proposal['operator_id']='force_run'
        with self.assertRaises(ValueError):validate_agent_proposal(PACKET,proposal)

    def test_q09_original_facts_are_preserved_by_entry(self):
        spec=importlib.util.spec_from_file_location('q09_probe',REPO/'scripts/run_q09_rules_probe_v1.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
        packet=json.loads(PACKET.read_text());facts=[x for x in packet['source_materials'][0]['permitted_facts'] if x.startswith('Original answer-free fact packet: ')][0]
        original=json.loads(facts.split(': ',1)[1]);original['method_facts']['original_fitting_configuration']='invented'
        with self.assertRaises(ValueError):mod.admit_q09(original,json.loads(PROPOSAL.read_text()))

    def test_actual_request_triggers_but_description_does_not(self):
        g=graph();d=synthetic();r=q.evaluate_forward_rule(g,d);self.assertEqual(len(r['obligations']),1)
        g['case']['requested_claim_level']='DESCRIBE_CURVE';self.assertEqual(q.evaluate_forward_rule(g,d)['status'],'NOT_APPLICABLE')

    def test_disabled_rule_never_dispatches_calculation(self):
        g=graph();d=synthetic();r=q.evaluate_forward_rule(g,d,enabled=False)
        with patch.object(q,'run_diagnostic') as run:self.assertIsNone(q.dispatch_obligation(r,d,g));run.assert_not_called()

    def test_changed_source_and_request_rejected(self):
        g=graph();d=synthetic();r=q.evaluate_forward_rule(g,d)
        changed=copy.deepcopy(g);changed['comparisons'][0]['condition_relation']='DIFFERENT'
        with self.assertRaises(ValueError):q.dispatch_obligation(r,d,changed)
        d.y['DA']=d.y['DA']+1
        with self.assertRaises(ValueError):q.dispatch_obligation(r,d,g)

    def test_optimizer_success_boolean_cannot_close_science(self):
        d=synthetic();r=q.evaluate_forward_rule(graph(),d,{'optimizer_success':True,'model_valid':True})
        self.assertEqual(r['status'],'UNRESOLVED');self.assertEqual(r['reason_codes'],['DIAGNOSTIC_EVIDENCE_REJECTED']);self.assertFalse(r['complete_question_answer'])

    def stopped_evidence(self,data):
        request=q.evaluate_forward_rule(graph(),data)['request_id']
        return {'schema':'q09-forward-evidence/v1','operator_id':q.OPERATOR_ID,'request_id':request,'input_id':data.input_id,'config':copy.deepcopy(q.CONFIG),'baseline_parameters':data.baseline,'baseline':q.summarize(data,data.joint_counts(data.baseline)),'IRF_audit':q.irf_audit(data),'donor_runs':[{'initial':seed+[.001,0.],'numerical_status':'TIME_BUDGET_STOP'} for seed in q.CONFIG['candidate_donor_initials']],'joint_runs':[],'profile_runs':[],'selected_donor_index':None,'selected_joint_index':None,'candidate':None}

    def test_preserved_numerical_stop_does_not_become_completed_diagnostic(self):
        data=synthetic();e=self.stopped_evidence(data);r=q.evaluate_forward_rule(graph(),data,e)
        self.assertEqual(r['diagnostic_status'],'NUMERICAL_STOP');self.assertIn('DIAGNOSTIC_NUMERICAL_STOP',r['reason_codes'])

    def test_evidence_numbers_and_request_are_recomputed_not_trusted(self):
        data=synthetic();e=self.stopped_evidence(data);e['baseline']['D0']['deviance']+=100
        self.assertEqual(q.evaluate_forward_rule(graph(),data,e)['reason_codes'],['DIAGNOSTIC_EVIDENCE_REJECTED'])
        e=self.stopped_evidence(data);e['request_id']='different_request'
        self.assertEqual(q.evaluate_forward_rule(graph(),data,e)['reason_codes'],['DIAGNOSTIC_EVIDENCE_REJECTED'])

    def test_new_donor_parameterization_preserves_normalization(self):
        for u,v in [(0.,0.),(1.,1.),(.2,.4)]:self.assertAlmostEqual(sum(q.amplitudes(u,v)),1.)
        d=synthetic();p=[.2,1.,4.,.2,.4,35.,65.,.5,1.,.001,0.,.001,0.];pred=q.j3_counts(d,p)
        np.testing.assert_allclose(pred['D0']/pred['D0'].sum(),pred['DA']/pred['DA'].sum(),rtol=1e-12)

    def test_bin_integral_and_transfer_rate_independent(self):
        for rate in [.1,1.,10.]:self.assertAlmostEqual(float(bin_factor(rate,.008)),quad(lambda t:np.exp(-rate*t),0,.008)[0]/.008,places=12)
        t=np.array([0.,1.,10.]);np.testing.assert_allclose(transfer_survival(t,[56.4],[1.],sigma_A=0),np.exp(-t*.224*2/3),rtol=1e-12)

    def test_instrument_order_and_poisson_zero(self):
        f=np.array([1.,.5,.25,.125]);irf=np.array([1.,0.,0.,0.]);lin=np.array([1.,2.,3.,4.]);mask=np.ones(4,bool)
        actual=expected_counts(f,irf,lin,mask,100.,background_fraction=.2)
        expected=(.8*f/f.sum()+.2/4)*lin;expected*=100/expected.sum();np.testing.assert_allclose(actual,expected)
        self.assertEqual(poisson_deviance(np.array([0.,1.]),np.array([0.,1.])),0.)

if __name__=='__main__':unittest.main()
