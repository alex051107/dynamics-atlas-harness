import copy,math,unittest
import numpy as np
from unittest.mock import patch
from dynamics_atlas_harness import q14_correlation_sensitivity_v1 as q

class CorrelationTests(unittest.TestCase):
 def test_sharp_bounds_have_psd_witnesses(self):
  # Synthetic fixed marginals: construct planar Gram vectors giving zero sum.
  g=[.04,-.03,-.05,.048];a,b,c,d=map(abs,g);t=.06
  x=(t*t+a*a-b*b)/(2*t);y=math.sqrt(a*a-x*x)
  z=(t*t+c*c-d*d)/(2*t);v=math.sqrt(c*c-z*z)
  vectors=np.array([[x,y],[t-x,-y],[-z,v],[-t+z,-v]])
  unit=vectors/np.array(g)[:,None];corr=unit@unit.T
  self.assertLess(abs(np.array(g)@corr@np.array(g)),1e-15)
  self.assertTrue(np.allclose(np.diag(corr),1));self.assertGreater(np.linalg.eigvalsh(corr).min(),-1e-12)
  high=np.outer(np.sign(g),np.sign(g));bounds=q.sd_bounds(g,[1]*4)
  self.assertAlmostEqual(np.array(g)@high@np.array(g),bounds['delta_variance_bounds'][1])
  self.assertEqual(bounds['delta_sd_bounds'][0],0)
  self.assertEqual(q.sd_bounds([3,1],[1,1])['delta_sd_bounds'],[2,4])
  with self.assertRaises(ValueError):q.sd_bounds([1],[-1])

 def test_actual_style_rule_off_source_binding_and_mutation(self):
  source=dict(role='AUTHOR_SUMMARIZED_INTENSITY_BASED_MEASUREMENTS',samples={k:dict(R_apparent_A=x,R_sd_A=s)for k,x,s in [('1-lo',83.4,2.5),('1-mid',60.3,1.3),('2-lo',85.4,3.4),('2-mid',63.7,2.3)]})
  vals,sd,g,delta=q.source_values(source)
  main=dict(main_inputs=dict(means_A=vals,published_sd_A=sd),difference_jacobian=g,cross_pair_difference=delta,covariance_status='UNAVAILABLE_NOT_ASSUMED_ZERO_FOR_CONCLUSION')
  receipt=dict(source_digest=q.digest(source),main_digest=q.digest(main))
  on=q.run(source,main,receipt);self.assertEqual(on['operator_calls'],1)
  with patch.object(q,'operator',side_effect=AssertionError):off=q.run(source,main,receipt,False)
  self.assertEqual(off['operator_calls'],0);self.assertEqual(on['before']['rule_instance_id'],on['after']['rule_instance_id'])
  self.assertFalse(on['after']['full_question_answer'])
  bad=copy.deepcopy(on['evidence']);bad['delta_sd_bounds']=[0,0]
  with self.assertRaisesRegex(ValueError,'BOUND_SOURCE'):q.evaluate(source,main,receipt,bad)
  source['samples']['1-lo']['R_sd_A']=5
  with self.assertRaisesRegex(ValueError,'PREVIOUSLY_ADMITTED'):q.run(source,main,receipt)
if __name__=='__main__':unittest.main()
