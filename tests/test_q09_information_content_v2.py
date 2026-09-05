import copy
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import numpy as np
from dynamics_atlas_harness import q09_global_comparison_v1 as a
from dynamics_atlas_harness.q09_fluorescence_v1 import expected_counts
import test_q09_global_comparison_v1 as fixture


class InformationTests(unittest.TestCase):
    def test_f0_one_makes_arbitrary_distances_exactly_unobserved(self):
        group=fixture.GlobalTests().group();p=group.from_local(group.initial(),'shared2')
        k=group.donor_size;p[k:k+3]=[120.,120.,1.]
        old=group.predict(p,'shared2',[.4,.6]);p[k:k+2]=[35.,65.]
        new=group.predict(p,'shared2',[.4,.6])
        for role in old:np.testing.assert_array_equal(old[role],new[role])
        info=a.component_information([35.,65.],[.4,.6],1.)
        self.assertTrue(all(x['distance_status']=='ZERO_OBSERVATIONAL_CONTRIBUTION' for x in info))

    def test_zero_weight_and_coincidence_are_distinct(self):
        info=a.component_information([35.,35.,65.],[.4,.6,0.],.2)
        self.assertTrue(info[0]['population_degeneracy'])
        self.assertGreater(info[0]['fret_prefactor'],0)
        self.assertEqual(info[2]['reason'],'ZERO_COMPONENT_WEIGHT')
        self.assertFalse(info[2]['population_degeneracy'])
        self.assertIn('IDENTIFIABILITY_UNESTABLISHED',info[0]['distance_status'])

    def test_archive_identity_rejected_before_metadata_or_matching_bytes(self):
        with tempfile.TemporaryDirectory() as td:
            (Path(td)/'eTCSPC_wildtype.zip').write_bytes(b'not the specified author archive')
            with self.assertRaisesRegex(ValueError,'AUTHOR_ARCHIVE_IDENTITY_MISMATCH'):
                a.GlobalData(td,Path(td)/'no-manifest')

    def test_bad_structure_preserves_valid_decay_and_obligation(self):
        graph={'case':{'case_id':'q09_t4l_state_number_20260905','requested_claim_level':'STATE_NUMBER_AND_STRUCTURE_CONSISTENCY'}}
        data=SimpleNamespace(input_id='synthetic',audit={'variants':['synthetic']},verify=lambda:None)
        report={'numerical_status':'NUMERICAL_COMPARISON_INCOMPLETE'}
        correct={'models':{'shared2':{'zero_contribution_components':2}}}
        with patch.object(a.q,'_validate_graph'),patch.object(a,'verify',return_value=report),patch.object(a,'structure_comparison',return_value=correct):
            missing=a.evaluate(graph,data,{'id':'synthetic'})
            valid=a.evaluate(graph,data,{'id':'synthetic'},structure_evidence=correct)
            invalid=a.evaluate(graph,data,{'id':'synthetic'},structure_evidence={'models':{}})
        self.assertEqual(invalid['comparison'],report)
        self.assertEqual(invalid['obligations'],missing['obligations'])
        self.assertIn('STRUCTURE_EVIDENCE_REJECTED',invalid['reason_codes'])
        self.assertIn('ZERO_CONTRIBUTION_DISTANCE_PARAMETERS_ARE_NOT_OBSERVATIONAL_EVIDENCE',valid['reason_codes'])

    def test_padded_shift_is_continuous_at_both_nonzero_endpoints(self):
        t=np.arange(64);f=np.exp(-t/12);h=np.exp(-((t-3)/4)**2)+.2
        lin=np.ones(64);mask=np.ones(64,bool)
        def model(s,policy):return expected_counts(f,h,lin,mask,100000,shift_bins=s,background_fraction=.01,shift_policy=policy)
        for center in [-5.,-1.,0.,1.,5.]:
            base=model(center,'padded_linear_v2')
            for eps in [-1e-10,1e-10]:
                self.assertLess(np.max(abs(model(center+eps,'padded_linear_v2')-base)),1e-5)
        self.assertGreater(np.max(abs(model(1e-12,'legacy_endpoint_v1')-model(0,'legacy_endpoint_v1'))),1)
        np.testing.assert_array_equal(model(0,'legacy_endpoint_v1'),model(0,'padded_linear_v2'))


if __name__=='__main__':unittest.main()
