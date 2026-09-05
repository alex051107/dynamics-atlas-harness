import functools
import unittest
from unittest.mock import patch
import numpy as np
from dynamics_atlas_harness import q09_global_comparison_v1 as a
from dynamics_atlas_harness.q09_cached_group_v2 import CachedGroup
import test_q09_global_comparison_v1 as fixture


class CachedGroupTests(unittest.TestCase):
    def test_same_latent_mixture_and_native_count_predictions(self):
        original=fixture.GlobalTests().group();cached=CachedGroup(original.ref,original.owners,original.records,2)
        padded=functools.partial(a.expected_counts,shift_policy='padded_linear_v2')
        for kind in ['local2','shared2','shared3']:
            p=original.initial() if kind=='local2' else original.from_local(original.initial(),kind)
            pop=[.2,.5,.3] if kind=='shared3' else [.3,.7]
            for i in range(len(p)):
                point=p.copy();lo,hi=original.bounds(kind)[i];point[i]=max(lo,min(hi,point[i]+.001*(hi-lo)))
                with patch.object(a,'expected_counts',padded):expected=original.predict(point,kind,pop)
                actual=cached.predict(point,kind,pop)
                for role in expected:np.testing.assert_allclose(actual[role],expected[role],rtol=2e-13,atol=1e-9)

    def test_zero_contributions_and_cache_eviction_preserve_values(self):
        original=fixture.GlobalTests().group();cached=CachedGroup(original.ref,original.owners,original.records,2,cache_entries=4)
        p=original.from_local(original.initial(),'shared3');p[original.donor_size+3]=1.
        first=cached.predict(p,'shared3',[.3,.7,0.]);p[original.donor_size:original.donor_size+3]=[10.,120.,75.]
        second=cached.predict(p,'shared3',[.1,.2,.7])
        for role in first:np.testing.assert_array_equal(first[role],second[role])
        self.assertLessEqual(len(cached.cache),4)
        first[cached.owners[0]][:]=0
        self.assertGreater(cached.predict(p,'shared3',[.1,.2,.7])[cached.owners[0]].sum(),0)

    def test_shared_gradient_matches_uncached_same_policy(self):
        from types import SimpleNamespace
        g=fixture.GlobalTests().group();c=CachedGroup(g.ref,g.owners,g.records,2)
        uncached=a.Joint(SimpleNamespace(groups=[g],total=g.total),'shared3')
        cached=a.Joint(SimpleNamespace(groups=[c],total=c.total),'shared3')
        p=g.from_local(g.initial(),'shared3')+[.2,.625]
        # Away from interpolation knots, compare the same physical objective.
        p[g.donor_size-1]=.23;p[-3]=.17
        padded=functools.partial(a.expected_counts,shift_policy='padded_linear_v2')
        with patch.object(a,'expected_counts',padded):old=uncached.jac_scaled((p-uncached.lo)/uncached.span)
        new=cached.jac_scaled((p-cached.lo)/cached.span)
        np.testing.assert_allclose(new,old,rtol=2e-5,atol=2e-7)


if __name__=='__main__':unittest.main()
