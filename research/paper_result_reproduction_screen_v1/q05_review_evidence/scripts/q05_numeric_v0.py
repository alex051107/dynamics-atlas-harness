"""Q05 downstream numeric reconstruction, not a Rules-registered Operator.

Established Gaussian BME dual: Bottaro et al. 2020, author BME.py fit()/maxent
at KULL-Centre/BME@314d3b5bb8cd400c1a9eee984acdb903a03c3da4.
Uses NumPy/SciPy only because the full author loader requires absent sklearn.
Paper-specific NOE r^-3 averaging: Bengtsen et al. 2020, PDF p17.
Author final weights/statistics are NEVER read by this runner.
"""
from pathlib import Path
import datetime,json,sys,time,signal
import numpy as np
import scipy
from scipy.optimize import minimize
from scipy.special import logsumexp
ROOT=Path(__file__).resolve().parents[1];INP=ROOT/'inputs/q05_author';OUT=ROOT/'outputs/q05_numeric_v0';OUT.mkdir(parents=True,exist_ok=True)
start=time.monotonic();THETA=6.0
config={'theta':THETA,'theta_basis':'Reconstruction assumption fixed from author grid near paper18percent effective fraction; not confirmed original fit config. No tuning to our results.','saxs_selection':'no-tag static30C; exact90 q labels from author stats grid, excluding first experimental q=0.00253895','saxs_scaling':'as deposited, no fitted scale/offset','noe_averaging':'power3','noe_bound':'UPPER distance -> LOWER r^-3 intensity','noe_sigma':'deposited0.3 Angstrom; first-order propagated for objective','prior':'uniform across deposited rows','statistical_unit':'simulation and experiment replicate; frames correlated; no inferential CIs in this subcalculation','author_fit_targets_or_weights_used':False,'author_q_label_metadata_used':True,'claim_ceiling':'author-processed numeric subcalculation; no coordinate reanalysis, full reproduction or Rules trigger/route success'}
(OUT/'config.json').write_text(json.dumps(config,indent=2)+'\n')
p=INP/'BME_reweight/inputs_and_method'
sim={k:np.loadtxt(p/n) for k,n in {'saxs':'simulation_SAXS.dat','amide':'simulation_HN2_NOE.dat','methyl':'simulation_methyl_NOE.dat'}.items()}
ids=sim['saxs'][:,0];n=len(ids)
for k,a in sim.items():
 assert np.array_equal(a[:,0],ids),(k,'frame IDs differ')
 assert np.all(np.isfinite(a)) and np.all(a[:,1:]>0),k
assert len(np.unique(ids))==n and np.all(np.diff(ids)>0)
obs=np.loadtxt(INP/'SAXS_and_SANS/Delta_H5_no_tag_Static_SAXS_30C_RB_subtracted.dat',skiprows=1)
q_labels=np.loadtxt(p/'SAXS_q_labels_from_author_stats.dat')
indices=[]
for q in q_labels:
 found=np.flatnonzero(np.isclose(obs[:,0],q,rtol=0,atol=1e-10))
 assert len(found)==1,('q label not uniquely matched',q,found)
 indices.append(int(found[0]))
assert len(set(indices))==len(indices)
obs=obs[indices]
assert obs.shape[0]==sim['saxs'].shape[1]-1,('SAXS q count',obs.shape,sim['saxs'].shape)
assert np.all(obs[:,2]>0) and np.all(np.diff(obs[:,0])>0)
def noe(name):
 rows=[x.split() for x in (p/('exp_HN2_NOE.dat' if name=='amide' else 'exp_methyl_NOE.dat')).read_text().splitlines() if x.strip() and not x.startswith('#')]
 assert all(len(x)==5 and x[4]=='UPPER' for x in rows)
 lab=[x[0]+'--'+x[1] for x in rows]; upper=np.array([float(x[2]) for x in rows]);sigma=np.array([float(x[3]) for x in rows])
 assert len(rows)==sim[name].shape[1]-1 and np.all(upper>0) and np.all(sigma>0)
 return lab,upper,sigma
noes={k:noe(k) for k in ['amide','methyl']};w0=np.ones(n)/n
A=[sim['saxs'][:,1:]];b=[obs[:,1]];sig=[obs[:,2]];bounds=[(None,None)]*len(obs);labels=['SAXS_q='+str(q) for q in obs[:,0]]
for k in ['amide','methyl']:
 lab,u,e=noes[k];y=u**-3;sd=3*y*e/u
 A.append(sim[k][:,1:]**-3);b.append(y);sig.append(sd);bounds.extend([(None,0.0)]*len(u));labels.extend(k+':'+x for x in lab)
A=np.hstack(A);b=np.concatenate(b);sig=np.concatenate(sig)
# Same affine feature standardization as BME_tools.standardize; preserves dual objective.
center=w0@A;scale=(np.sqrt(np.average((A-center)**2,axis=0,weights=w0))+sig)/2
assert np.all(scale>0);X=(A-center)/scale;y=(b-center)/scale;s=sig/scale
logw0=np.log(w0)
def fun(lam):
 v=logw0-X@lam;z=logsumexp(v);w=np.exp(v-z)
 obj=(z+lam@y+0.5*THETA*np.sum((s*lam)**2))/THETA
 grad=(y-X.T@w+THETA*s*s*lam)/THETA
 return obj,grad
# One meaningful derivative check for the local formula port.
rng=np.random.default_rng(5);direction=rng.normal(size=len(b));direction/=np.linalg.norm(direction);eps=1e-6
zero=np.zeros(len(b));fd=(fun(zero+eps*direction)[0]-fun(zero-eps*direction)[0])/(2*eps);analytic=fun(zero)[1]@direction
assert abs(fd-analytic)<1e-5*max(1,abs(analytic)),(fd,analytic)
def metrics(w,power=3):
 out={};calc=w@sim['saxs'][:,1:];out['saxs_chi2_mean']=float(np.mean(((calc-obs[:,1])/obs[:,2])**2))
 for k in ['amide','methyl']:
  _,u,e=noes[k];r=(w@(sim[k][:,1:]**(-power)))**(-1/power);delta=np.maximum(r-u,0);z=delta/e;nv=int(np.sum(delta>0))
  out[k]={'constraints':len(u),'exceed_upper_count':nv,'chi2_all_constraints':float(np.mean(z*z)),'chi2_exceeded_only':float(np.sum(z*z)/nv) if nv else None,'max_excess_A':float(delta.max())}
 out['effective_fraction_entropy']=float(np.exp(-np.sum(w[w>0]*np.log(w[w>0]/w0[w>0]))))
 out['weight_ess_not_independent_samples']=float(1/np.sum(w*w));out['max_weight']=float(w.max())
 return out
result={'status':'INPUT_ADMITTED_BASELINE_DONE','timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'input':{'frames':n,'frame_id_range':[float(ids[0]),float(ids[-1])],'saxs_points':len(obs),'q_range':[float(obs[0,0]),float(obs[-1,0])],'amide_constraints':len(noes['amide'][1]),'methyl_constraints':len(noes['methyl'][1]),'frame_identity':'same ordered IDs in all3 matrices; coordinate mapping not yet verified','source_commit':'85979b1b4123b6b5391b617d16551969eda9f56e'},'baseline_power3':metrics(w0),'baseline_default_power6_sensitivity':metrics(w0,6),'gradient_check':{'finite_difference':float(fd),'analytic':float(analytic),'passed':True},'config':config}
(OUT/'result.json').write_text(json.dumps(result,indent=2)+'\n');print('Input/baseline:',json.dumps(result['input']),json.dumps(result['baseline_power3']),flush=True)
def timeout(*args):raise TimeoutError('120-second optimizer budget')
signal.signal(signal.SIGALRM,timeout);signal.alarm(120)
try:
 opt=minimize(fun,zero,method='L-BFGS-B',jac=True,bounds=bounds,options={'maxiter':2000,'ftol':1e-12,'gtol':1e-7,'maxls':40})
 signal.alarm(0)
 w=np.exp(logw0-X@opt.x-logsumexp(logw0-X@opt.x));assert np.all(np.isfinite(w)) and np.all(w>=0) and abs(w.sum()-1)<1e-10
 assert float(opt.fun)<=float(fun(zero)[0])+1e-8
 result['optimizer']={'success':bool(opt.success),'message':str(opt.message),'iterations':int(opt.nit),'objective_at_uniform':float(fun(zero)[0]),'objective_final':float(opt.fun),'weight_sum':float(w.sum())};result['reweighted_power3']=metrics(w);result['status']='NUMERIC_SUBCALCULATION_COMPLETE' if opt.success else 'OPTIMIZER_NOT_CONVERGED'
 np.savetxt(OUT/'frame_weights.tsv',np.column_stack([ids,w0,w]),delimiter='\t',header='frame_id\tuniform_weight\treconstructed_weight',comments='')
 np.savetxt(OUT/'saxs_predictions.tsv',np.column_stack([obs, w0@sim['saxs'][:,1:], w@sim['saxs'][:,1:]]),delimiter='\t',header='q\tobserved\terror\tuniform_prediction\treweighted_prediction',comments='')
except TimeoutError as e:
 result['status']='OPTIMIZER_TIME_BUDGET_REACHED';result['error']=str(e)
result['elapsed_seconds']=time.monotonic()-start;result['runtime']={'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__}
(OUT/'result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
