"""Single actual D0 diagnostic under fixed choices; not Q09 state-number fit."""
from pathlib import Path
import csv
import json
import time
import numpy as np
from scipy.optimize import minimize
from q09_forward_v1 import donor_decay, linearization_reference, expected_counts, poisson_deviance

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT/'inputs/q09_author/unpacked/eTCSPC/19-119'
OUT = ROOT/'outputs/q09_donor_calibration_v1'
OUT.mkdir(exist_ok=False)


def read_counts(name):
    text = (DATA/name).read_text().split('Chan\tData\n',1)[1]
    return np.array([int(row.split()[1]) for row in text.splitlines() if row.strip()],dtype=float)


observed = read_counts('19-119_D0.txt')
raw_irf = read_counts('IRF_D0.txt')
raw_lin = read_counts('Linearization_D0.txt')
lin = linearization_reference(raw_lin)
positive = lin[lin>0]
mask = lin > .1*np.median(positive)
valid_indices = np.flatnonzero(mask)
irf_background = float(np.median(raw_irf[valid_indices[-256:]]))
irf = np.maximum(raw_irf-irf_background,0)
t = np.arange(len(observed))*.0141
total = float(observed[mask].sum())
config = {'variant':'19-119','role':'D0_ONLY','dt_ns':.0141,'components':[1,2],
          'lifetimes_bounds_ns':[.05,10.], 'shift_bounds_bins':[-5.,5.],
          'background_fraction_bounds':[0.,.05],'scatter_fraction':0.,
          'linearization':'17binHanning reflectpadding divided by raw all-bin mean',
          'fit_mask':'Lin greater than0.1*median positiveLin;data count independent',
          'irf_background':'median of last256 electronic-valid bins,subtract and clip0',
          'irf_background_value':irf_background,'irf_shift':'linear interpolation zero fill',
          'convolution':'causal nonperiodic; repetition effects not evaluated',
          'objective':'Poisson deviance / observed masked photon count; total scale profiled',
          'max_seconds_per_optimization':120,'model_status':'CONDITIONAL_DIAGNOSTIC_NOT_ORIGINAL_AUTHOR_METHOD',
          'no_FRET_or_paper_fit_targets':True}
(OUT/'method_config.json').write_text(json.dumps(config,indent=2)+'\n')


def model(params, components):
    if components==1:
        tau,bg,shift=params
        intrinsic=donor_decay(t,[tau],[1.])
    else:
        tau1,tau2,fraction,bg,shift=params
        intrinsic=donor_decay(t,[tau1,tau2],[fraction,1-fraction])
    return expected_counts(intrinsic,irf,lin,mask,total,shift_bins=shift,background_fraction=bg)


runs=[]
for components,initials,bounds in [
    (1,[[4.,.001,0.]],[(.05,10.),(0.,.05),(-5.,5.)]),
    (2,[[.5,4.,.1,.001,0.],[1.,3.,.5,.001,0.],[2.,5.,.5,.001,0.]],[(.05,10.),(.05,10.),(0.,1.),(0.,.05),(-5.,5.)])]:
    for initial in initials:
        start=time.monotonic()
        def loss(params):
            if time.monotonic()-start>120:
                raise TimeoutError('PRESPECIFIED_120S_OPTIMIZER_LIMIT')
            return poisson_deviance(observed[mask],model(params,components)[mask])/total
        try:
            fitted=minimize(loss,initial,method='L-BFGS-B',bounds=bounds,
                            options={'maxiter':2000,'maxfun':20000,'ftol':1e-13,'gtol':1e-8})
            predicted=model(fitted.x,components)
            gradient=np.array(fitted.jac)
            for i,(low,high) in enumerate(bounds):
                if (fitted.x[i]<=low+1e-7 and gradient[i]>0) or (fitted.x[i]>=high-1e-7 and gradient[i]<0):gradient[i]=0
            projected=float(np.max(abs(gradient)))
            runs.append({'components':components,'initial':initial,'success':bool(fitted.success),
                         'message':str(fitted.message),'parameters':fitted.x.tolist(),
                         'iterations':int(fitted.nit),'evaluations':int(fitted.nfev),
                         'poisson_deviance':poisson_deviance(observed[mask],predicted[mask]),
                         'projected_scaled_gradient_inf':projected,
                         'numerical_status':'PASS' if fitted.success and projected<1e-6 else 'UNRESOLVED',
                         'bound_hits':[i for i,(lo,hi) in enumerate(bounds) if min(abs(fitted.x[i]-lo),abs(fitted.x[i]-hi))<1e-5],
                         'elapsed_seconds':time.monotonic()-start})
        except TimeoutError as error:
            runs.append({'components':components,'initial':initial,'success':False,'message':str(error),'numerical_status':'TIME_BUDGET_STOP','elapsed_seconds':time.monotonic()-start})
best={}
for components in (1,2):
    candidates=[r for r in runs if r['components']==components and 'poisson_deviance' in r]
    if candidates:best[str(components)]=min(candidates,key=lambda r:r['poisson_deviance'])
predictions={k:model(v['parameters'],int(k)) for k,v in best.items()}
with (OUT/'per_bin.csv').open('w') as f:
    writer=csv.writer(f);writer.writerow(['bin_zero_based','time_ns','observed','IRF_raw','Lin','included']+[f'expected_{k}component' for k in predictions])
    for i in range(len(observed)):
        writer.writerow([i,t[i],int(observed[i]),int(raw_irf[i]),lin[i],bool(mask[i])]+[a[i] for a in predictions.values()])
blocks=[]
for indices in np.array_split(valid_indices,12):
    blocks.append({'first_bin':int(indices[0]),'last_bin':int(indices[-1]),'observed_sum':float(observed[indices].sum()),
                   'models':{k:{'expected_sum':float(a[indices].sum()),'deviance':poisson_deviance(observed[indices],a[indices])} for k,a in predictions.items()}})
summary={'status':'REAL_DONOR_ONLY_DIAGNOSTIC_COMPLETE','fit_bins':int(mask.sum()),'masked_photons':total,
         'excluded_photons':float(observed[~mask].sum()),'fits_attempted':len(runs),'runs':runs,'best_by_components':best,
         'deviance_per_fit_bin_descriptive_only':{k:v['poisson_deviance']/mask.sum() for k,v in best.items()},
         'residual_blocks':blocks,'scientific_state_number_verdict':'NOT_EVALUATED','Rules_run':False,
         'full_question_answers_added':0,'limits':['Single reference diagnostic;free nuisance assumptions not originalmethod','No regular likelihood-ratio scientific test','No FRET or globalpopulation fit','Reference replication multiplicity not used here']}
(OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
(OUT/'runner_source.py').write_text(Path(__file__).read_text())
(OUT/'forward_source.py').write_text((ROOT/'scripts/q09_forward_v1.py').read_text())
print(json.dumps({k:summary[k] for k in ('status','fit_bins','masked_photons','excluded_photons','best_by_components','deviance_per_fit_bin_descriptive_only')},indent=2))
