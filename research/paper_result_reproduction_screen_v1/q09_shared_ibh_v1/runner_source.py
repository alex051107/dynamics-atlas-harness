"""Two actual DA records and one shared D0; local K2, not global state inference."""
from pathlib import Path
import json
import csv
import time
import numpy as np
from scipy.optimize import minimize
from q09_shared_ibh_v1 import SharedIBH

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'outputs/q09_shared_ibh_v1'
if (OUT/'joint_runs.json').exists():raise RuntimeError('PRESERVE_EXISTING_RUN')
admission=json.loads((OUT/'input_forward_check.json').read_text())
assert admission['status']=='CONDITIONAL_SHARED_IBH_INPUT_AND_FORWARD_PASS'
data=SharedIBH()
seeds=[[35.,65.,.5,.1],[50.,85.,.8,.2],[30.,100.,.2,.05],[65.,40.,.5,.1]]
config={'scope':'TWO_VARIANTS_SHARED_DONOR_CONDITIONAL_LOCAL_K2','variants':['19-119','19-132'],
        'dt_ns':.0141,'Gaussian_sigma_A':6.,'radiative_rate_per_ns':.224,'kappa_squared':2/3,'reduced_radius_A':56.4,
        'parameter_order':['donor_tau1','donor_tau2','donor_amplitude1','D0_background','D0_shift']+[v+'_'+p for v in ['19-119','19-132'] for p in ['R1','R2','FRET_fraction1','DA_f0','background','shift']],
        'initial_local_seeds':seeds,'second_DA_initialization':'swapdistancecomponent order and complementpopulation,physicallyidenticallocalstart',
        'numerical_method':'reusePQv3unitcoordinates symmetricJac;physicalprojectedgradient1e-6+optimizer.success;1500iter120s',
        'donor_initializer':'prior19-119 localdoublelifetimefit;not authorfit;initializeronly becausebin integrationnowexplicit',
        'likelihood':'OneD0record+bothdistinctDA;conditionalindependentPoisson after fixedIRF/Lin;latentdonorparametersshared',
        'instrument_assumptions':'17binHanning reflectLin;maskLin>.1medianpositive;IRFmedianlast256validsubtractclip;scatter0;nonperiodiccausal;separatefittedshift/background perrecord',
        'reference_applicability':'UNKNOWN donor mutant equivalence;shareone response asconditional depositedreferenceanalysis',
        'scientific_claim_ceiling':'No globalpopulation,thirdstate,authorreproduction orRulesgain',
        'author_final_fit_values_used':False}
(OUT/'method_config.json').write_text(json.dumps(config,indent=2)+'\n')


def optimize(initial,bounds,objective,label):
    start=time.monotonic()
    def bounded(p):
        if time.monotonic()-start>120:raise TimeoutError('120S_PRESPECIFIED_STOP')
        return objective(p)
    try:
        lower=np.array([b[0] for b in bounds]);span=np.array([b[1]-b[0] for b in bounds])
        def scaled(z):return bounded(lower+span*z)
        def symmetric_gradient(z):
            gradient=[]
            for i in range(len(z)):
                h=1e-5*max(abs(z[i]),.001)
                plus=np.array(z);minus=np.array(z)
                plus[i]=min(1.,z[i]+h);minus[i]=max(0.,z[i]-h)
                gradient.append((scaled(plus)-scaled(minus))/(plus[i]-minus[i]))
            return np.array(gradient)
        fit=minimize(scaled,(np.asarray(initial)-lower)/span,jac=symmetric_gradient,method='L-BFGS-B',bounds=[(0.,1.)]*len(initial),
                     options={'maxiter':1500,'maxfun':20000,'ftol':1e-15,'gtol':1e-11})
        physical=lower+span*fit.x
        grad=np.array(fit.jac)/span
        for i,(lo,hi) in enumerate(bounds):
            if (physical[i]<=lo+1e-7 and grad[i]>0) or (physical[i]>=hi-1e-7 and grad[i]<0):grad[i]=0
        pg=float(np.max(abs(grad)))
        fit.x=physical
        return {'label':label,'initial':initial,'parameters':fit.x.tolist(),'scaled_objective':float(fit.fun),
                'optimizer_success':bool(fit.success),'message':str(fit.message),'projected_gradient_inf':pg,
                'numerical_status':'PASS' if fit.success and np.isfinite(pg) and pg<1e-6 else 'UNRESOLVED',
                'bound_hits':[i for i,(lo,hi) in enumerate(bounds) if min(abs(fit.x[i]-lo),abs(fit.x[i]-hi))<1e-5],
                'iterations':int(fit.nit),'evaluations':int(fit.nfev),'elapsed_seconds':time.monotonic()-start}
    except TimeoutError as error:
        return {'label':label,'initial':initial,'numerical_status':'TIME_BUDGET_STOP','message':str(error),'elapsed_seconds':time.monotonic()-start}

cal=json.loads((ROOT/'outputs/q09_donor_calibration_v2/summary.json').read_text())
accepted=[x for x in cal['runs'] if x['components']==2 and x['numerical_status']=='PASS']
donor_initial=min(accepted,key=lambda x:x['poisson_deviance'])['parameters']
bounds=[(.05,10.),(.05,10.),(0.,1.),(1e-12,.05),(-5.,5.)]+2*[(10.,120.),(10.,120.),(0.,1.),(0.,1.),(1e-12,.05),(-5.,5.)]
runs=[]
for r1,r2,x,f0 in seeds:
    initial=donor_initial+[r1,r2,x,f0,.001,0.]+[r2,r1,1-x,f0,.001,0.]
    result=optimize(initial,bounds,lambda p:data.deviance(p)/data.total,'SHARED_REFERENCE_LOCAL_K2')
    if 'parameters' in result:
        result['channel_deviance']=data.channel_deviance(result['parameters'])
        result['total_deviance']=sum(result['channel_deviance'].values())
    runs.append(result)
    (OUT/'joint_runs.json').write_text(json.dumps(runs,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['numerical_status','total_deviance','projected_gradient_inf','elapsed_seconds','bound_hits'] if k in result}),flush=True)
evaluated=[x for x in runs if 'total_deviance' in x]
accepted=[x for x in evaluated if x['numerical_status']=='PASS']
best=min(accepted or evaluated,key=lambda x:x['total_deviance']) if evaluated else None
summary={'status':'CONDITIONAL_SHARED_REFERENCE_JOINT_NUMERIC_PASS' if accepted else 'NUMERICAL_STOP',
         'runs':runs,'best_joint':best,'accepted_starts':len(accepted),'optimizer_calls':len(runs),
         'D0_likelihood_contributions':1,'distinct_DA_likelihood_contributions':2,
         'fit_photons':int(data.total),'scientific_state_number_verdict':'NOT_EVALUATED','Rules_controlled':False,'full_question_answers_added':0}
if best:
    predictions=data.joint_counts(best['parameters']);blocks={}
    with (OUT/'per_bin.csv').open('w') as f:
        w=csv.writer(f);w.writerow(['record','bin0','time_ns','observed','expected','Lin','included'])
        for key,d in data.records.items():
            for i in range(len(data.t)):w.writerow([key,i,data.t[i],int(d['y'][i]),predictions[key][i],d['Lin'][i],bool(d['mask'][i])])
            blocks[key]=[{'first_bin':int(ix[0]),'last_bin':int(ix[-1]),'observed':float(d['y'][ix].sum()),'expected':float(predictions[key][ix].sum())} for ix in np.array_split(np.flatnonzero(d['mask']),15)]
    (OUT/'residual_blocks.json').write_text(json.dumps(blocks,indent=2)+'\n')
(OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
(OUT/'runner_source.py').write_text(Path(__file__).read_text())
print('SUMMARY',json.dumps(summary),flush=True)
