from pathlib import Path
import json
import numpy as np
from scipy.integrate import quad
from scipy.special import ndtr
from q09_forward_v1 import donor_decay, transfer_survival, expected_counts, linearization_reference, poisson_deviance

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'outputs/q09_forward_v1'
OUT.mkdir(exist_ok=False)
t = np.array([0., 0.01, 1., 10., 50.])
np.testing.assert_allclose(transfer_survival(t, [1e6], [1.], sigma_A=0), 1., atol=1e-12)
np.testing.assert_allclose(transfer_survival(t, [50.], [1.], sigma_A=0), np.exp(-t * .224 * (2/3) * (56.4/50.)**6), rtol=1e-12)
np.testing.assert_allclose(transfer_survival([0.], [20., 50.], [.3, .7]), 1., atol=1e-11)
worst = 0.
for mean in [20., 45., 70.]:
    actual = transfer_survival(t, [mean], [1.])
    ref = np.array([quad(lambda r: np.exp(-.5*((r-mean)/6)**2) / (6*np.sqrt(2*np.pi)*ndtr(mean/6)) * np.exp(-time*.224*(2/3)*(56.4/r)**6), 0, mean+60, epsabs=1e-12)[0] for time in t])
    worst = max(worst, float(np.max(abs(actual-ref))))
    np.testing.assert_allclose(actual, ref, atol=2e-9, rtol=2e-9)
x = np.arange(80)*.1
f = donor_decay(x, [1., 4.], [.3, .7])
h = np.zeros(80);h[3:6] = [.2, .5, .3]
lin = np.linspace(.7, 1.3, 80);mask = np.ones(80, dtype=bool)
y = expected_counts(f,h,lin,mask,12345.,background_fraction=.03,scatter_fraction=.02)
direct = np.convolve(f,h)[:80]; direct = .95*direct/direct.sum()+.02*h+.03/80
direct *= lin; direct *= 12345/direct.sum()
np.testing.assert_allclose(y,direct,rtol=1e-12,atol=1e-10)
assert abs(y.sum()-12345)<1e-8
np.testing.assert_allclose(linearization_reference(np.ones(80)*100),1.,atol=1e-12)
assert poisson_deviance(np.array([0.,5.]),np.array([0.,5.]))==0
assert np.isinf(poisson_deviance([1.],[0.]))
result={'status':'CONDITIONAL_KERNEL_CHECK_PASS','checks':['zero_FRET','delta_distance','zero_time_normalization','Gaussian_quadrature_vs_independent_quad','FFT_vs_direct_and_full_Lin_placement','photon_normalization','flat_reference','Poisson_zero_cases'], 'worst_quadrature_absolute_error':worst,'scientific_fits':0,'rules_runs':0,'method_status':'Conditional Eq34-only survival; original author executed method unknown'}
(OUT/'validation.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'forward_source.py').write_text((ROOT/'scripts/q09_forward_v1.py').read_text())
(OUT/'check_source.py').write_text(Path(__file__).read_text())
print(json.dumps(result,indent=2))
