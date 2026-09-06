"""Predeclared actual single-pair K2 fit. No protein-state-number inference."""
from pathlib import Path
import json
import csv
import time
import numpy as np
from scipy.optimize import minimize
from q09_pq_joint_v1 import PQPair
from q09_forward_v1 import poisson_deviance

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'outputs/q09_pq_joint_v1'
data=PQPair()
config={'variant':'22-127','scope':'SINGLE_PAIR_DEVELOPMENT_PROBE','dt_ns':.008,'distance_sigma_A':6.,
        'radiative_rate_per_ns':.224,'kappa_squared':2/3,'reduced_radius_A':56.4,
        'donor_components':[1,2],'FRET_components':2,'DA_internal_donor_only_fraction':'f0 free[0,1] distinct from FRETpopulations',
        'conditional_choices':'allnativebins;IRFmedianlast256subtractclip;noLinPQ;scatter0;causalIRF;fittedshift+/-5bins',
        'likelihood':'profiled count-scale Poisson deviance;D0once+DAonce;latent donor parameters shared',
        'time_bins':'exact exponential integration before discrete histogram IRF convolution',
        'R_bounds_A':[10.,120.],'tau_bounds_ns':[.05,10.],'background_bounds':[1e-12,.05],
        'optimizer':'L-BFGS-B max500iterations/120s perstart;predeclared4D0+4jointcalls',
        'joint_parameter_order':['tau1','tau2','donor_amplitude1','R1','R2','FRET_fraction1','DA_f0','D0_background','D0_shift','DA_background','DA_shift'],
        'joint_initial_distance_population_f0':[[35.,65.,.5,.1],[50.,85.,.8,.2],[30.,100.,.2,.05],[65.,40.,.5,.1]],
        'scientific_verdict':'NOT_EVALUATED_NO_K3_OR_GLOBAL_COMPARISON','author_postfit_targets_used':False}
(OUT/'method_config.json').write_text(json.dumps(config,indent=2)+'\n')


def optimize(initial,bounds,objective,label):
    start=time.monotonic()
    def bounded(p):
        if time.monotonic()-start>120:raise TimeoutError('120S_PRESPECIFIED_STOP')
        return objective(p)
    try:
        fit=minimize(bounded,initial,method='L-BFGS-B',bounds=bounds,
                     options={'maxiter':500,'maxfun':20000,'ftol':1e-13,'gtol':1e-8})
        grad=np.array(fit.jac)
        for i,(lo,hi) in enumerate(bounds):
            if (fit.x[i]<=lo+1e-7 and grad[i]>0) or (fit.x[i]>=hi-1e-7 and grad[i]<0):grad[i]=0
        pg=float(np.max(abs(grad)))
        return {'label':label,'initial':initial,'parameters':fit.x.tolist(),'scaled_objective':float(fit.fun),
                'optimizer_success':bool(fit.success),'message':str(fit.message),'projected_gradient_inf':pg,
                'numerical_status':'PASS' if fit.success and np.isfinite(pg) and pg<1e-6 else 'UNRESOLVED',
                'bound_hits':[i for i,(lo,hi) in enumerate(bounds) if min(abs(fit.x[i]-lo),abs(fit.x[i]-hi))<1e-5],
                'iterations':int(fit.nit),'evaluations':int(fit.nfev),'elapsed_seconds':time.monotonic()-start}
    except TimeoutError as error:
        return {'label':label,'initial':initial,'numerical_status':'TIME_BUDGET_STOP','message':str(error),'elapsed_seconds':time.monotonic()-start}


def donor_counts(p,n):
    if n==1:
        tau,bg,shift=p;curve=data.intrinsic_donor([tau],[1.])
    else:
        t1,t2,a,bg,shift=p;curve=data.intrinsic_donor([t1,t2],[a,1-a])
    return data.counts('D0',curve,bg,shift)


donor=[]
for n,initials,bounds in [
    (1,[[4.,.001,0.]],[(.05,10.),(1e-12,.05),(-5.,5.)]),
    (2,[[.5,4.,.1,.001,0.],[1.,3.,.5,.001,0.],[2.,5.,.5,.001,0.]],[(.05,10.),(.05,10.),(0.,1.),(1e-12,.05),(-5.,5.)])]:
    for initial in initials:
        result=optimize(initial,bounds,lambda p:poisson_deviance(data.y['D0'],donor_counts(p,n))/data.y['D0'].sum(),f'D0_{n}')
        if 'parameters' in result:result['deviance']=poisson_deviance(data.y['D0'],donor_counts(result['parameters'],n))
        donor.append(result)
(OUT/'donor_calibration.json').write_text(json.dumps(donor,indent=2)+'\n')
print('D0 calibration:',json.dumps([{k:r[k] for k in ('label','numerical_status','deviance','parameters') if k in r} for r in donor]),flush=True)
accepted=[r for r in donor if r['label']=='D0_2' and r['numerical_status']=='PASS']
if not accepted:
    (OUT/'summary.json').write_text(json.dumps({'status':'DONOR_NUMERICAL_STOP','donor_runs':donor,'joint_fits':0},indent=2)+'\n')
    raise SystemExit('D0 model unresolved;dependent jointfit not started')
best_donor=min(accepted,key=lambda r:r['deviance'])
t1,t2,a,bg0,s0=best_donor['parameters']
bounds=[(.05,10.),(.05,10.),(0.,1.),(10.,120.),(10.,120.),(0.,1.),(0.,1.),(1e-12,.05),(-5.,5.),(1e-12,.05),(-5.,5.)]
joint=[];total=sum(v.sum() for v in data.y.values())
for r1,r2,x,f0 in config['joint_initial_distance_population_f0']:
    initial=[t1,t2,a,r1,r2,x,f0,bg0,s0,.001,0.]
    result=optimize(initial,bounds,lambda p:data.deviance(p)/total,'JOINT_K2')
    if 'parameters' in result:
        predictions=data.joint_counts(result['parameters'])
        result['channel_deviance']={k:poisson_deviance(data.y[k],v) for k,v in predictions.items()}
        result['total_deviance']=sum(result['channel_deviance'].values())
    joint.append(result)
    (OUT/'joint_runs.json').write_text(json.dumps(joint,indent=2)+'\n')
    print('Joint start:',json.dumps({k:result[k] for k in ['numerical_status','total_deviance','projected_gradient_inf','elapsed_seconds','bound_hits'] if k in result}),flush=True)
evaluated=[r for r in joint if 'total_deviance' in r]
best=min(evaluated,key=lambda r:r['total_deviance']) if evaluated else None
if best:
    predictions=data.joint_counts(best['parameters'])
    with (OUT/'per_bin.csv').open('w') as f:
        w=csv.writer(f);w.writerow(['time_ns','D0_observed','D0_expected','DA_observed','DA_expected'])
        for i,time_value in enumerate(data.t):w.writerow([time_value,int(data.y['D0'][i]),predictions['D0'][i],int(data.y['DA'][i]),predictions['DA'][i]])
summary={'status':'ACTUAL_PQ_JOINT_K2_DIAGNOSTIC_COMPLETE','donor_runs':donor,'joint_runs':joint,'best_joint':best,
         'donor_observation_contributions':1,'DA_observation_contributions':1,'new_optimizer_calls':len(donor)+len(joint),
         'scientific_question_verdict':'NOT_EVALUATED_SINGLE_PAIR_K2_ONLY','Rules_run':False,'full_answers_added':0}
(OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
(OUT/'runner_source.py').write_text(Path(__file__).read_text())
(OUT/'instrument_source.py').write_text((ROOT/'scripts/q09_forward_v1.py').read_text())
print('SUMMARY',json.dumps({'status':summary['status'],'best_joint':best}),flush=True)
