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


def positive_fixture(d=None):
    # SYNTHETIC_EXPECTED_CURVE: exact generated means, not experimental counts
    # or a claim that an optimizer ran. No paper targets or fitted values.
    if d is None:
        d=synthetic();d.irf['D0'][0]=.1;d.irf['DA'][-1]=.1
    p=[.2,1.,4.,.2,.4,35.,65.,.5,.4,.001,.2,.001,.3]
    d.y=q.j3_counts(d,p);d.input_id=q._input_identity(d)
    total=sum(x.sum() for x in d.y.values());dp=p[:5]+p[9:11]
    def record(par,bounds,fun,initial):
        return {'initial':initial,'parameters':par,'objective':fun(par),'optimizer_success':True,'numerical_status':'PASS',
                'projected_gradient_inf':float(max(abs(q.gradient_at(par,bounds,fun)))),'fixture_origin':'SYNTHETIC_EXPECTED_CURVE_KNOWN_PARAMETERS'}
    df=lambda x:q.poisson_deviance(d.y['D0'],q.d3_counts(d,x)['D0'])/d.y['D0'].sum()
    jf=lambda x:sum(q.poisson_deviance(d.y[k],v) for k,v in q.j3_counts(d,x).items())/total
    e={'schema':'q09-forward-evidence/v1','operator_id':q.OPERATOR_ID,'request_id':q.evaluate_forward_rule(graph(),d)['request_id'],
       'input_id':d.input_id,'config':copy.deepcopy(q.CONFIG),'baseline_parameters':d.baseline,'baseline':q.summarize(d,d.joint_counts(d.baseline)),
       'IRF_audit':q.irf_audit(d),'donor_runs':[record(dp,q.D3_BOUNDS,df,seed+[.001,0.]) for seed in q.CONFIG['candidate_donor_initials']],
       'joint_runs':[record(p,q.J3_BOUNDS,jf,dp[:5]+seed+dp[5:]+[.001,0.]) for seed in q.CONFIG['joint_fret_initials']],
       'selected_donor_index':0,'selected_joint_index':0,'candidate':q.summarize(d,q.j3_counts(d,p)),'profile_runs':[]}
    reduced=p[:8]+p[9:]
    for f0 in q.CONFIG['profile_f0']:
        r={'fixed_f0':f0,'initial':reduced,'numerical_status':'TIME_BUDGET_STOP'}
        if f0==p[8]:
            r.update(record(reduced,q.J3_BOUNDS[:8]+q.J3_BOUNDS[9:],lambda x:jf(list(x[:8])+[f0]+list(x[8:])),reduced))
            r['full_parameters']=p
        e['profile_runs'].append(r)
    return d,e


class Q09AdequacyTests(unittest.TestCase):
    def test_expected_curve_positive_evidence_without_optimizer(self):
        d,e=positive_fixture()
        with patch.object(q,'optimize',side_effect=AssertionError('No verification optimizer')):
            r=q.evaluate_forward_rule(graph(),d,e)
        self.assertIn('BOUND_NUMERIC_DIAGNOSTIC_RECOMPUTED',r['reason_codes'])
        self.assertEqual([x['status'] for x in r['profile_checks']],['VERIFIED','NUMERICAL_STOP','NUMERICAL_STOP'])
        self.assertEqual(len(r['obligations']),1);self.assertEqual(r['profile_branch_status'],'INCOMPLETE')

    def test_profile_missing_and_malformed_are_local_not_joint_success(self):
        d,e=positive_fixture();e['profile_runs']=[]
        r=q.evaluate_forward_rule(graph(),d,e)
        self.assertEqual([x['status'] for x in r['profile_checks']],['NOT_RUN']*3)
        for mutation in ['missing_full','wrong_length','negative_objective','false_convergence','wrong_fixed','wrong_initial']:
            d,e=positive_fixture();x=e['profile_runs'][0]
            if mutation=='missing_full':del x['full_parameters']
            if mutation=='wrong_length':x['parameters']=[-1.]
            if mutation=='negative_objective':x['objective']=-10.
            if mutation=='false_convergence':x['projected_gradient_inf']=.9
            if mutation=='wrong_fixed':x['fixed_f0']=.8
            if mutation=='wrong_initial':x['initial']=[0.]*12
            r=q.evaluate_forward_rule(graph(),d,e)
            self.assertIn('BOUND_NUMERIC_DIAGNOSTIC_RECOMPUTED',r['reason_codes'],mutation)
            self.assertEqual(r['profile_checks'][0]['status'],'REJECTED',mutation)

    def test_joint_initial_is_verified(self):
        d,e=positive_fixture();e['joint_runs'][0]['initial']=[0.]*13
        self.assertEqual(q.evaluate_forward_rule(graph(),d,e)['reason_codes'],['DIAGNOSTIC_EVIDENCE_REJECTED'])

    def test_replay_requires_affirmative_verification(self):
        spec=importlib.util.spec_from_file_location('q09_replay',REPO/'scripts/replay_q09_numeric_evidence_v1.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
        with self.assertRaises(ValueError):m.require_verified_replay({'status':'NOT_APPLICABLE','reason_codes':[]})
        m.require_verified_replay({'reason_codes':['BOUND_NUMERIC_DIAGNOSTIC_RECOMPUTED']})

    def test_role_identity_and_dictionary_order(self):
        for field in ('y','irf'):
            d=synthetic();old=getattr(d,field)
            setattr(d,field,{'DA':old['DA'],'D0':old['D0']});q.verify_data(d)
            d=synthetic();old=getattr(d,field)
            if field=='irf':old['DA'][4]=1;d.input_id=q._input_identity(d)
            setattr(d,field,{'DA':old['D0'],'D0':old['DA']})
            with self.assertRaises(ValueError):q.verify_data(d)
            for keys in ({'DA'}, {'D0','DA','unexpected'}):
                d=synthetic();setattr(d,field,{k:d.y['D0'] for k in keys})
                with self.assertRaises(ValueError):q.verify_data(d)

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
