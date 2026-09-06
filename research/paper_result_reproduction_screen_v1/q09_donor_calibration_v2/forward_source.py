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


def expected_counts(intrinsic, irf, lin, mask, total, shift_bins=0.0, background_fraction=0.0, scatter_fraction=0.0):
    """Causal convolution, scatter + constant then all times Lin; profile scale.

    IRF shift uses linear interpolation with zero fill. Component fractions are
    defined before Lin over the specified window. No periodic wrap is used.
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
    shifted = np.interp(axis - shift_bins, axis, h, left=0, right=0)
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
