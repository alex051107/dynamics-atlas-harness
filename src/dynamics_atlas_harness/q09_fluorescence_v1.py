"""Conditional Q09 forward math; not registered or an author-code reproduction."""
import numpy as np
from scipy.signal import fftconvolve
from scipy.special import ndtr
from numpy.polynomial.legendre import leggauss


def donor_decay(time_ns, lifetimes_ns, amplitudes):
    t = np.asarray(time_ns, float)
    tau = np.asarray(lifetimes_ns, float)
    a = np.asarray(amplitudes, float)
    if t.ndim != 1 or np.any(t < 0) or tau.ndim != 1 or tau.shape != a.shape:
        raise ValueError('INVALID_TIME_OR_DONOR_SHAPE')
    if not all(np.all(np.isfinite(v)) for v in (t, tau, a)) or np.any(tau <= 0) or np.any(a < 0) or not np.isclose(a.sum(), 1):
        raise ValueError('INVALID_DONOR_PARAMETERS')
    return np.exp(-t[:, None] / tau) @ a


def transfer_survival(time_ns, distances_A, populations, sigma_A=6.0, quadrature=96):
    """Eq34-only transfer; positive truncated normal, tails cut at mu+10sigma.

    The positive-domain normalizer is analytic. Omitted upper tail is below
    standard double-precision relevance. This corrects the printed Eq36 extra
    constant explicitly and remains conditional pending independent review.
    """
    t = np.asarray(time_ns, float)
    means = np.asarray(distances_A, float)
    weights = np.asarray(populations, float)
    if t.ndim != 1 or means.ndim != 1 or means.shape != weights.shape:
        raise ValueError('INVALID_TRANSFER_SHAPE')
    if not all(np.all(np.isfinite(v)) for v in (t, means, weights)) or np.any(t < 0) or np.any(means <= 0) or np.any(weights < 0) or not np.isclose(weights.sum(), 1) or sigma_A < 0:
        raise ValueError('INVALID_TRANSFER_PARAMETERS')
    coefficient = 0.224 * (2 / 3) * 56.4 ** 6
    if sigma_A == 0:
        return np.exp(-t[:, None] * coefficient / means[None, :] ** 6) @ weights
    if not np.isfinite(sigma_A) or quadrature < 16:
        raise ValueError('INVALID_QUADRATURE')
    nodes, factors = leggauss(quadrature)
    answer = np.zeros_like(t)
    for mean, weight in zip(means, weights):
        upper = mean + 10 * sigma_A
        r = (nodes + 1) * upper / 2
        p = np.exp(-0.5 * ((r - mean) / sigma_A) ** 2) / (sigma_A * np.sqrt(2 * np.pi) * ndtr(mean / sigma_A))
        integral_weights = p * factors * upper / 2
        answer += weight * (np.exp(-t[:, None] * coefficient / r[None, :] ** 6) @ integral_weights)
    return answer


def linearization_reference(raw_counts):
    a = np.asarray(raw_counts, float)
    if a.ndim != 1 or len(a) < 17 or not np.all(np.isfinite(a)) or np.any(a < 0) or a.mean() <= 0:
        raise ValueError('INVALID_LINEARIZATION')
    window = np.hanning(17)
    window /= window.sum()
    return np.convolve(np.pad(a, (8, 8), mode='reflect'), window, mode='valid') / a.mean()


def expected_counts(intrinsic, irf, lin, mask, total, shift_bins=0.0, background_fraction=0.0, scatter_fraction=0.0, *, shift_policy='legacy_endpoint_v1'):
    """Causal convolution, scatter + constant then all times Lin; profile scale.

    The default preserves the historical v1 endpoint-truncation model for
    reproducible old evidence. It is discontinuous when an endpoint is nonzero.
    New method comparisons must explicitly use padded_linear_v2 and bind that
    policy in their configuration; old fit evidence cannot be silently upgraded.
    Component fractions are defined before Lin. No periodic wrap is used.
    """
    f, h, linear = [np.asarray(x, float) for x in (intrinsic, irf, lin)]
    mask = np.asarray(mask, bool)
    if f.ndim != 1 or f.shape != h.shape or f.shape != linear.shape or f.shape != mask.shape or not mask.any():
        raise ValueError('ARRAY_OR_MASK_MISMATCH')
    if not all(np.all(np.isfinite(x)) and np.all(x >= 0) for x in (f, h, linear)) or h.sum() <= 0 or not np.isfinite(total) or total <= 0:
        raise ValueError('INVALID_COUNTS_INPUT')
    if not np.isfinite(shift_bins) or background_fraction < 0 or scatter_fraction < 0 or background_fraction + scatter_fraction >= 1:
        raise ValueError('INVALID_NUISANCE')
    axis = np.arange(len(h))
    if shift_policy == 'legacy_endpoint_v1':
        shifted = np.interp(axis - shift_bins, axis, h, left=0, right=0)
    elif shift_policy == 'padded_linear_v2':
        pad = int(np.ceil(abs(shift_bins))) + 1
        shifted = np.interp(axis - shift_bins, np.arange(-pad, len(h)+pad), np.pad(h, (pad,pad)), left=0, right=0)
    else:
        raise ValueError('UNKNOWN_IRF_SHIFT_POLICY')
    if shifted.sum() <= 0:
        raise ValueError('EMPTY_SHIFTED_IRF')
    shifted /= shifted.sum()
    fluorescence = np.maximum(fftconvolve(f, shifted, mode='full')[:len(f)], 0)
    if fluorescence[mask].sum() <= 0 or shifted[mask].sum() <= 0:
        raise ValueError('EMPTY_MODEL_IN_WINDOW')
    shape = (1 - background_fraction - scatter_fraction) * fluorescence / fluorescence[mask].sum()
    shape += scatter_fraction * shifted / shifted[mask].sum()
    shape += background_fraction / mask.sum()
    shape *= linear
    if shape[mask].sum() <= 0:
        raise ValueError('EMPTY_CORRECTED_MODEL')
    return total * shape / shape[mask].sum()


def poisson_deviance(observed, expected):
    y, mu = np.asarray(observed, float), np.asarray(expected, float)
    if y.shape != mu.shape or np.any(y < 0) or np.any(mu < 0) or not np.all(np.isfinite(y)) or not np.all(np.isfinite(mu)):
        raise ValueError('INVALID_POISSON_VALUES')
    if np.any((y > 0) & (mu == 0)):
        return float('inf')
    positive = y > 0
    terms = mu - y
    terms[positive] += y[positive] * np.log(y[positive] / mu[positive])
    return float(2 * terms.sum())


from pathlib import Path
import zipfile

def bin_factor(rate, dt):
    x = np.asarray(rate)*dt
    return -np.expm1(-x)/x

class PQPair:
    def __init__(self, root, quadrature=256):
        BASE = Path(root)
        self.name='22-127'
        directory=BASE/'unpacked/eTCSPC'/self.name
        filenames=[self.name+'.yml',self.name+'_D0.dat',self.name+'_DA.dat','IRF_D0.dat','IRF_DA.dat']
        with zipfile.ZipFile(BASE/'eTCSPC_wildtype.zip') as archive:
            for name in filenames:
                if (directory/name).read_bytes()!=archive.read('eTCSPC/'+self.name+'/'+name):
                    raise ValueError('EXTRACTED_BYTES_DIFFER_FROM_FROZEN_ZIP')
        metadata=(directory/(self.name+'.yml')).read_text()
        if metadata.count('Setup ID: PQ TCSPC')!=4 or 'Resolution [ps]: 8' not in metadata:
            raise ValueError('UNEXPECTED_INSTRUMENT_METADATA')
        self.y={};self.irf={};self.irf_baseline={}
        self.dt=.008
        for role in ('D0','DA'):
            curve=np.loadtxt(directory/(self.name+'_'+role+'.dat'))
            response=np.loadtxt(directory/('IRF_'+role+'.dat'))
            if curve.shape!=response.shape or curve.shape[1]!=2 or not np.array_equal(curve[:,0],response[:,0]):
                raise ValueError('IRF_AND_COUNT_AXIS_MISMATCH')
            if not np.allclose(np.diff(curve[:,0]),self.dt,rtol=0,atol=1e-10) or curve[0,0]!=0:
                raise ValueError('PHYSICAL_TIME_AXIS_MISMATCH')
            if not np.all(np.isfinite(curve)) or not np.all(np.isfinite(response)) or np.any(curve[:,1]<0) or np.any(response[:,1]<0):
                raise ValueError('INVALID_RAW_COUNTS')
            if not np.all(curve[:,1]==np.floor(curve[:,1])) or not np.all(response[:,1]==np.floor(response[:,1])):
                raise ValueError('NONINTEGER_RAW_COUNTS')
            self.t=curve[:,0];self.y[role]=curve[:,1]
            self.irf_baseline[role]=float(np.median(response[-256:,1]))
            self.irf[role]=np.maximum(response[:,1]-self.irf_baseline[role],0)
        self.lin=np.ones_like(self.t);self.mask=np.ones_like(self.t,dtype=bool)
        nodes,factors=leggauss(quadrature)
        self.r=(nodes+1)*90.;self.qweights=factors*90.
        self.rates=.224*(2/3)*(56.4/self.r)**6
        self.transfer_exp=np.exp(-self.t[:,None]*self.rates)

    def intrinsic_donor(self,taus,amplitudes):
        alpha=1/np.asarray(taus)
        return (np.exp(-self.t[:,None]*alpha)*bin_factor(alpha,self.dt))@np.asarray(amplitudes)

    def intrinsic_pair(self,taus,amplitudes,means,populations,f0):
        density=np.zeros_like(self.r)
        for mean,population in zip(means,populations):
            density+=population*np.exp(-.5*((self.r-mean)/6.)**2)/(6*np.sqrt(2*np.pi)*ndtr(mean/6))
        density*=self.qweights
        quenched=np.zeros_like(self.t)
        for tau,amplitude in zip(taus,amplitudes):
            alpha=1/tau
            # Exact integral of each total-rate exponential over native time bin.
            quenched+=amplitude*np.exp(-self.t*alpha)*(self.transfer_exp@(density*bin_factor(alpha+self.rates,self.dt)))
        donor=self.intrinsic_donor(taus,amplitudes)
        return donor, f0*donor+(1-f0)*quenched

    def counts(self,role,intrinsic,bg,shift):
        return expected_counts(intrinsic,self.irf[role],self.lin,self.mask,float(self.y[role].sum()),shift_bins=shift,background_fraction=bg)

    def joint_counts(self,p):
        tau1,tau2,a,r1,r2,x,f0,bg0,shift0,bga,shifta=p
        d0,da=self.intrinsic_pair([tau1,tau2],[a,1-a],[r1,r2],[x,1-x],f0)
        return {'D0':self.counts('D0',d0,bg0,shift0),'DA':self.counts('DA',da,bga,shifta)}

    def deviance(self,p):
        values=self.joint_counts(p)
        return sum(poisson_deviance(self.y[role],values[role]) for role in ('D0','DA'))
