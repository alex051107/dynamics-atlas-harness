import unittest
import copy
import numpy as np
from dynamics_atlas_harness import q15_apbs_comparison_v1 as q


class APBSTests(unittest.TestCase):
    def test_exact_background_and_correction_recover_forward_counts(self):
        # Construct exact integer raw counts for E=.25,S=.5 with calibrated DD=120,DA=92,AA=140.
        policy=copy.deepcopy(q.POLICY);policy.update(background_kHz_DD_DA_AA=[1,2,3],alpha=.1,delta=0.,gamma=2.,beta=.4375)
        out=q.correct([[130,112,170]],[.01],policy)
        np.testing.assert_allclose(out['E'],[.25]);np.testing.assert_allclose(out['S'],[.5]);self.assertTrue(out['selected'][0])
        changed=q.correct([[130,112,170]],[.001],policy)
        self.assertNotAlmostEqual(changed['E'][0],.25)

    def test_no_silent_clipping_and_invalid_raw_input_rejected(self):
        out=q.correct([[200,0,160]],[.001])
        self.assertLess(out['E'][0],0)
        self.assertLess(out['corrected_counts_DD_DA_AA'][0,1],0)
        with self.assertRaises(ValueError):q.correct([[1,-1,1]],[.001])
        with self.assertRaises(ValueError):q.correct([[1,1,1]],[0])

    def test_repetition_direction_changes_without_state_claim(self):
        rows=[{'pair':'pair','condition':c,'repetition':str(i),'E':{'mean':x+i*.01}}for c,x in [('apo',.2),('holo',.6)]for i in range(3)]
        report=q.group_difference(rows)['pair'];self.assertEqual(report['observed_direction'],'INCREASE');self.assertFalse(report['protein_closure_inferred'])
        for r in rows:r['condition']='holo'if r['condition']=='apo'else'apo'
        self.assertEqual(q.group_difference(rows)['pair']['observed_direction'],'DECREASE')
        with self.assertRaises(ValueError):q.group_difference(rows[:-1])

if __name__=='__main__':unittest.main()
