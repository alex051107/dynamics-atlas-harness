import unittest
from types import SimpleNamespace
import numpy as np
from dynamics_atlas_harness import q09_global_comparison_v1 as a
from test_q09_state_comparison_v1 import data

class GlobalTests(unittest.TestCase):
    def group(self,ref='ref',name='v'):
        d=data();rs={ref:d.records['D0_shared'],name:d.records['19-119_DA']}
        for r in rs.values():r['kernel']=d
        return a.Group(ref,[name],rs,2)
    def test_native_kernel_matches_existing_bin_integrals(self):
        from dynamics_atlas_harness.q09_fluorescence_v1 import PQPair
        for dt,n in [(.008,80),(.0141,80)]:
            native=a.Native(n,dt);d0,da=native.intrinsic_pair([1,4],[.3,.7],[35,65],[.2,.8],.1)
            self.assertTrue(np.all(da>=0));self.assertTrue(np.all(da<=d0+1e-12))
            same=PQPair.intrinsic_pair(native,[1,4],[.3,.7],[35,65],[.2,.8],.1)
            np.testing.assert_array_equal(da,same[1])
    def test_joint_gradient_matches_full_objective_and_group_scaling(self):
        groups=[self.group('r1','v1'),self.group('r2','v2')];d=SimpleNamespace(groups=groups,total=sum(g.total for g in groups))
        j=a.Joint(d,'shared2');p=sum((g.from_local(g.initial(),'shared2') for g in groups),[])+[.4];z=(p-j.lo)/j.span
        grad=j.jac_scaled(z)
        for k in [0,3,7,len(z)-1]:
            h=1e-5*max(abs(z[k]),.001);plus=z.copy();minus=z.copy();plus[k]+=h;minus[k]-=h
            brute=(j.objective(j.lo+j.span*plus)-j.objective(j.lo+j.span*minus))/(2*h)
            self.assertAlmostEqual(grad[k],brute,places=7)
        ck=j.stationary(p);self.assertEqual(set(ck['group_scaled_physical_gradient']),{'r1','r2'})
        self.assertGreaterEqual(max(ck['group_scaled_physical_gradient'].values()),ck['global_scaled_physical_gradient'])
    def test_total_is_derived_and_reference_once(self):
        g=self.group();total=g.total;g.records['v']['y']*=2
        self.assertGreater(g.total,total);self.assertEqual(len(g.records),2)
    def test_partial_optimizer_retains_feasible_point_and_stop(self):
        from unittest.mock import patch
        g=self.group();initial=g.initial()
        with patch.dict(a.CONFIG,local_seconds=-1):r=a.optimize_local(g,initial)
        self.assertEqual(r['numerical_status'],'NUMERICAL_STOP_WITH_FEASIBLE_POINT')
        self.assertEqual(r['parameters'],initial);self.assertTrue(np.isfinite(r['objective']))
        self.assertFalse(r['optimizer_success'])

    def test_global_sharedK2_zero_weight_K3_prediction_embedding(self):
        g=self.group();p=g.from_local(g.initial(),'shared2');k=g.donor_size
        p3=p[:k]+p[k:k+2]+[50.]+p[k+2:]
        for key,v in g.predict(p,'shared2',[.35,.65]).items():np.testing.assert_allclose(v,g.predict(p3,'shared3',[.35,.65,0])[key],rtol=1e-12,atol=1e-9)

if __name__=='__main__':unittest.main()
