import copy
import math
import unittest
from dynamics_atlas_harness.q16_common_window_v1 import POLICY,run,evaluate,stats

def fixture():
 pairs={}
 for p,conditions in [('29',['eg50_1mM','eg50_10mM','eg0_1mM','eg25_1mM','gly25_1mM']),('36',['eg50_1mM','eg50_10mM','eg0_1mM'])]:
  pairs[p]={}
  for j,c in enumerate(conditions):
   n=40 if c=='eg0_1mM' else 60
   ys=[1+.15*math.cos(i*.2+(0 if j<2 else .7)) for i in range(n)]
   pairs[p][c]=dict(role='AUTHOR_DEPOSITED_OBSERVED_DEER_TRACES',raw=[[i*.032,y,.9,0] for i,y in enumerate(ys)],processed=[[i*.032,y] for i,y in enumerate(ys)])
 return dict(doi='10.1038/s41467-022-31945-6',policy=POLICY,pairs=pairs)

class TestQ16(unittest.TestCase):
 def test_actual_routing_and_common_window(self):
  p=fixture();a=run(p);b=run(p,False,operator=lambda _:self.fail('off called'))
  self.assertEqual((a['operator_calls'],b['operator_calls']),(1,0));self.assertEqual(a['evidence']['results']['29']['n'],40)
  self.assertEqual(a['before']['rule_instance_id'],a['after']['rule_instance_id']);self.assertFalse(a['after']['full_question_answer'])
  self.assertEqual(a['after']['obligation'],'COMMON_WINDOW_COMPARISON_COMPLETED')
 def test_offset_scale_invariance_and_binding(self):
  self.assertLess(stats([1,2,4],[9,11,15])['shape_distance'],1e-12)
  p=fixture();e=run(p)['evidence'];e['results']['29']['n']=41
  with self.assertRaisesRegex(ValueError,'NUMERIC'):evaluate(p,e)
  e['input_id']='wrong'
  with self.assertRaisesRegex(ValueError,'BINDING'):evaluate(p,e)
 def test_missing_grid_and_role_rejected(self):
  p=fixture();del p['pairs']['29']['eg0_1mM']['processed'][3]
  with self.assertRaisesRegex(ValueError,'MISSING_COMMON'):run(p)
  p=fixture();p['pairs']['29']['eg0_1mM']['role']='AUTHOR_FITTED_CLOSED_POPULATION'
  with self.assertRaisesRegex(ValueError,'SOURCE_ROLE'):run(p)

 def test_numeric_counterfact_changes_partial_claim(self):
  p=fixture();first=run(p)['after'];self.assertEqual(first['partial_claim'],'OBSERVED_PREPARATION_SHAPE_CONTRAST_EXCEEDS_TESTED_DOSE_CONTRAST')
  c=p['pairs']['29'];c['eg0_1mM'],c['eg50_10mM']=c['eg50_10mM'],c['eg0_1mM']
  second=run(p)['after'];self.assertEqual(second['partial_claim'],'NO_CONSISTENT_ORDERING_ACROSS_PAIRS_AND_PROCESSING');self.assertFalse(second['full_question_answer'])
