import copy
import unittest
from unittest.mock import patch
import numpy as np
from test_q09_forward_adequacy_v1 import positive_fixture,graph
from dynamics_atlas_harness import q09_forward_adequacy_v1 as q
from dynamics_atlas_harness import q09_calibration_sensitivity_v1 as c

class CalibrationTests(unittest.TestCase):
    def data(self):
        d,e=positive_fixture();d.t=np.arange(256)*.05;d.dt=.05
        d.irf={k:np.full(256,.3) for k in ('D0','DA')}
        for h in d.irf.values():h[96:99]=[100.,200.,100.]
        return d

    def test_calibration_uses_original_only_and_seed_is_replayable(self):
        d=self.data();a,sa=c.calibrated_data(d,'adaptive_full_axis',91001)
        d.y={k:y*3 for k,y in d.y.items()};b,sb=c.calibrated_data(d,'adaptive_full_axis',91001)
        self.assertEqual(sa,sb)
        for k in a.irf:np.testing.assert_array_equal(a.irf[k],b.irf[k])
        self.assertTrue(all(hi-lo<=128 for lo,hi in c.groups(d,'DA')))
        compact,st=c.calibrated_data(d,'compact_3_7ns')
        self.assertEqual(float(compact.irf['DA'][(d.t<3)|(d.t>=7)].sum()),0.)

    def test_verified_gap_dispatches_and_off_does_not(self):
        d,e=positive_fixture();g=graph();r=q.evaluate_forward_rule(g,d,e)
        self.assertEqual(r['obligations'][0]['operator_id'],c.OPERATOR_ID)
        with patch.object(c,'run',return_value={'executed':True}) as run:
            self.assertEqual(c.dispatch(r,d,g,e),{'executed':True});run.assert_called_once()
        with patch.object(c,'run') as run:
            self.assertIsNone(c.dispatch(q.evaluate_forward_rule(g,d,e,enabled=False),d,g,e));run.assert_not_called()
        bad=copy.deepcopy(r);bad['obligations'][0]['input_id']='different'
        with self.assertRaises(ValueError):c.dispatch(bad,d,g,e)

    def test_unverified_calibration_cannot_close_or_remove_obligation(self):
        d,e=positive_fixture();r=q.evaluate_forward_rule(graph(),d,e,calibration_evidence={'success':True})
        self.assertIn('CALIBRATION_EVIDENCE_REJECTED',r['reason_codes']);self.assertEqual(len(r['obligations']),1)
        self.assertFalse(r['complete_question_answer'])

    def complete_fixture(self):
        from test_q09_forward_adequacy_v1 import synthetic
        d=synthetic();d.dt=.008;d.t=np.arange(1024)*d.dt;d.y={'D0':np.ones(1024)*20,'DA':np.ones(1024)*10}
        d.irf={k:np.zeros(1024) for k in ('D0','DA')}
        for h in d.irf.values():h[375]=100000.
        d.lin=np.ones(1024);d.mask=np.ones(1024,bool);d.transfer_exp=np.exp(-d.t[:,None]*d.rates)
        d,e=positive_fixture(d);p=e['joint_runs'][0]['parameters']
        # A single calibration impulse remains exactly the same normalized
        # response for both representations and all nonzero Poisson replicates.
        # Known-mean fixture only; this does not impersonate executed fits.
        def fit(initial,bounds,objective,label):
            if label=='FIXED_F0_BRANCH':return {'initial':initial,'numerical_status':'TIME_BUDGET_STOP'}
            return {'initial':initial,'parameters':p,'objective':objective(p),'optimizer_success':True,'numerical_status':'PASS',
                    'projected_gradient_inf':float(max(abs(q.gradient_at(p,bounds,objective)))),'fixture_origin':'EXPECTED_MEAN_NO_OPTIMIZATION'}
        with patch.object(q,'optimize',side_effect=fit):cal=c.run(d,e)
        return d,e,cal

    def test_complete_calibration_positive_and_numeric_mutations(self):
        d,e,cal=self.complete_fixture()
        with patch.object(q,'optimize',side_effect=AssertionError('Verification must not optimize')):
            self.assertTrue(c.verify_evidence(d,e,cal)['all_calibration_fits_verified'])
        for kind in ['realization','parameter','gradient','summary','seed','initial','base']:
            bad=copy.deepcopy(cal);x=bad['calibration_runs'][0]
            if kind=='realization':x['calibration']['DA']['response_id']='wrong'
            if kind=='parameter':x['fit']['parameters'][5]=-1
            if kind=='gradient':x['fit']['projected_gradient_inf']=.9
            if kind=='summary':x['summary']['DA']['deviance']+=10
            if kind=='seed':x['seed']=99
            if kind=='initial':x['fit']['initial'][0]=9.
            if kind=='base':bad['base_parameters'][0]=9.
            with self.assertRaises(ValueError,msg=kind):c.verify_evidence(d,e,bad)

    def test_geometry_shares_and_similarity(self):
        d,e=positive_fixture();p=e['joint_runs'][0]['parameters'];g=c.geometry(d,p)
        self.assertAlmostEqual(sum(g['latent_finite_window_fluorescence_shares']),1.)
        self.assertGreaterEqual(g['fast_scatter_cosine'],0.);self.assertLessEqual(g['fast_scatter_cosine'],1.+1e-12)
        self.assertLessEqual(g['weighted_contrast_remaining_fraction'],1.+1e-12)

if __name__=='__main__':unittest.main()
