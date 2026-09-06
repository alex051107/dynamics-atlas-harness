import copy
import unittest
from unittest.mock import patch
import numpy as np
from dynamics_atlas_harness import q16_shape_flexibility_v1 as m

class ShapeFlexibilityTests(unittest.TestCase):
    def test_positive_basis_exact_fixed_fraction(self):
        for p in [0.,.25,.5,.75,1.]:
            T=m.basis_transform(p)
            coefficients=np.arange(1,T.shape[1]+1,dtype=float)
            mass=T@coefficients
            self.assertTrue(np.all(mass>=0))
            self.assertAlmostEqual(mass[m.LONG].sum()/mass.sum(),p,places=12)
            np.testing.assert_allclose(T.sum(axis=0),1,atol=1e-14)

    def test_numeric_residuals_control_witness_not_label(self):
        t=np.linspace(0,4,80);K=m.kernel(t)
        candidate=dict(k=0.,p=0.,unmodulated_amplitude=.7,grid_weights=[[15,.3]],conditional_witness=True)
        y=.7+.3*K[:,15]
        self.assertTrue(m.audit_candidate(candidate,t,y,.003,K)['conditional_witness'])
        changed=y+.02*np.sin(np.linspace(0,3,80))
        self.assertFalse(m.audit_candidate(candidate,t,changed,.003,K)['conditional_witness'])
        bad=copy.deepcopy(candidate);bad['p']=1.
        with self.assertRaises(ValueError):m.audit_candidate(bad,t,y,.003,K)

    def test_off_no_operator_and_prior_source_change_rejected(self):
        payload={'records':{'x':{}}};baseline={'records':[{'record':'x','any_witness':False}]}
        receipt={'input_digest':m.digest(payload),'baseline_digest':m.digest(baseline)}
        with patch.object(m,'operator',side_effect=AssertionError('off dispatched')):
            self.assertEqual(m.run(payload,baseline,receipt,False)['operator_calls'],0)
        changed=copy.deepcopy(baseline);changed['records'][0]['any_witness']=True
        with self.assertRaises(ValueError):m.evaluate(payload,changed,receipt)

if __name__=='__main__':unittest.main()
