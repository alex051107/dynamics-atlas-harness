"""Bounded per-group reuse of native latent components under padded IRF v2.

Caches are local to a frozen, source-verified group. Parameters enter keys in
physical coordinates. Components are combined before observational normalization.
This is a numerical implementation, not a new scientific adequacy criterion.
"""
from collections import OrderedDict
import numpy as np
from scipy.special import ndtr
from .q09_global_comparison_v1 import Group
from .q09_fluorescence_v1 import bin_factor, expected_counts
from .q09_forward_adequacy_v1 import amplitudes


class CachedGroup(Group):
    shift_policy='padded_linear_v2'

    def __init__(self,ref,owners,records,donors,cache_entries=128):
        super().__init__(ref,owners,records,donors)
        self.cache_entries=cache_entries;self.cache=OrderedDict()
        self.hits=0;self.misses=0

    def memo(self,key,calculate):
        if key in self.cache:
            self.hits+=1;value=self.cache.pop(key);self.cache[key]=value;return value
        self.misses+=1;value=calculate();self.cache[key]=value
        if len(self.cache)>self.cache_entries:self.cache.popitem(last=False)
        return value

    def donor_component(self,kernel,tau):
        return self.memo(('donor',id(kernel),float(tau)),lambda:np.exp(-kernel.t/tau)*bin_factor(1/tau,kernel.dt))

    def quenched_component(self,kernel,tau,mu):
        def calculate():
            density=np.exp(-.5*((kernel.r-mu)/6.)**2)/(6*np.sqrt(2*np.pi)*ndtr(mu/6))*kernel.qweights
            return np.exp(-kernel.t/tau)*(kernel.transfer_exp@(density*bin_factor(1/tau+kernel.rates,kernel.dt)))
        return self.memo(('quenched',id(kernel),float(tau),float(mu)),calculate)

    def observed(self,role,tau,amp,means,pop,f0,bg,shift):
        key=('observed',role,tuple(tau),tuple(amp),tuple(means),tuple(pop),float(f0),float(bg),float(shift))
        def calculate():
            record=self.records[role];kernel=record['kernel']
            donor=sum((weight*self.donor_component(kernel,lifetime) for lifetime,weight in zip(tau,amp) if weight),np.zeros_like(kernel.t))
            if len(means)==0 or f0==1:
                intrinsic=donor
            else:
                quenched=sum((weight*population*self.quenched_component(kernel,lifetime,mu)
                              for lifetime,weight in zip(tau,amp) for mu,population in zip(means,pop)
                              if weight and population),np.zeros_like(kernel.t))
                intrinsic=f0*donor+(1-f0)*quenched
            return expected_counts(intrinsic,record['irf'],record['Lin'],record['mask'],
                float(record['y'][record['mask']].sum()),shift_bins=shift,background_fraction=bg,
                shift_policy=self.shift_policy)
        # A caller receives a copy; cached numerical values cannot be overwritten.
        return self.memo(key,calculate).copy()

    def predict(self,p,kind,pop=None):
        n=self.donors;tau=p[:n];amp=[p[n],1-p[n]] if n==2 else amplitudes(*p[n:n+2])
        offset=self.donor_size;bg,shift=p[offset-2:offset]
        out={self.ref:self.observed(self.ref,tau,amp,[],[],1.,bg,shift)}
        step=6 if kind in ('local2','shared3') else 5
        for i,variant in enumerate(self.owners):
            row=p[offset+step*i:offset+step*(i+1)];nr=3 if kind=='shared3' else 2
            weights=[row[nr],1-row[nr]] if kind=='local2' else pop
            f0,bg,shift=row[-3:]
            out[variant]=self.observed(variant,tau,amp,row[:nr],weights,f0,bg,shift)
        return out
