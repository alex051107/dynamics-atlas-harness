"""One developmental obligation: test finite shape flexibility after a poor fit.

This is a finite, conditional witness search, never a state/population classifier.
"""
import hashlib
import json
import time
import numpy as np
from scipy import constants, special
from scipy.optimize import nnls

RULE_ID='Q16R02_FINITE_DISTRIBUTION_ADEQUACY_V1'
OPERATOR_ID='q16_finite_shape_flexibility_v1'
R=np.linspace(2,10,81)
K_GRID=[0.,.002,.005,.01,.02,.04,.08,.16,.32,.64,1.]
P_GRID=[None,0.,.25,.5,.75,1.]
LONG=R>=5.5
D=constants.mu_0/(4*np.pi)*(constants.physical_constants['Bohr magneton'][0]*abs(constants.physical_constants['electron g factor'][0]))**2/constants.hbar*1e21

def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,allow_nan=False).encode()).hexdigest()

def kernel(t):
    phase=D*np.abs(t)[:,None]/R[None,:]**3
    xi=np.sqrt(6*phase/np.pi);s,c=special.fresnel(xi)
    out=np.ones_like(phase)
    np.divide(c*np.cos(phase)+s*np.sin(phase),xi,out=out,where=xi!=0)
    return out

def basis_transform(p):
    """Map nonnegative coupling amplitudes to grid masses with fixed long fraction."""
    if p is None:return np.eye(len(R))
    short=np.where(~LONG)[0];long=np.where(LONG)[0]
    if p==0:return np.eye(len(R))[:,short]
    if p==1:return np.eye(len(R))[:,long]
    transform=np.zeros((len(R),len(short)*len(long)))
    for column,(i,j) in enumerate((i,j)for i in short for j in long):
        transform[i,column]=1-p;transform[j,column]=p
    return transform

def arrays(record):
    raw=np.asarray(record['raw_time_real_imaginary'],float)
    if raw.ndim!=2 or raw.shape[1]!=3 or len(raw)<10 or not np.isfinite(raw).all() or not np.all(np.diff(raw[:,0])>0):
        raise ValueError('INVALID_RAW_RECORD')
    t,y,imag=raw.T;differences=np.diff(imag)
    noise=float(np.median(np.abs(differences-np.median(differences)))/(.6744897501960817*np.sqrt(2)))
    if noise<=0:raise ValueError('NO_POSITIVE_NOISE_PROXY')
    return t,y,noise,kernel(t)

def audit_candidate(candidate,t,y,noise,K):
    if candidate['k'] not in K_GRID or candidate['p'] not in P_GRID:
        raise ValueError('UNDECLARED_PROFILE_POINT')
    weights=np.zeros(len(R));indices=set()
    for index,value in candidate['grid_weights']:
        if type(index) is not int or not 0<=index<len(R) or index in indices or not np.isfinite(value) or value<0:
            raise ValueError('INVALID_GRID_WEIGHTS')
        weights[index]=value;indices.add(index)
    a0=candidate['unmodulated_amplitude']
    if not np.isfinite(a0) or a0<0:raise ValueError('INVALID_UNMODULATED_AMPLITUDE')
    mass=float(weights.sum());amplitude=a0+mass
    fraction=float(weights[LONG].sum()/mass) if mass else None
    if candidate['p'] is not None and fraction is not None and abs(fraction-candidate['p'])>1e-8:
        raise ValueError('FIXED_FRACTION_CONSTRAINT')
    prediction=np.exp(-candidate['k']*t)*(a0+K@weights)
    residual=prediction-y;rms=float(np.sqrt(np.mean(residual**2)))
    lag=float(np.corrcoef(residual[:-1],residual[1:])[0,1]) if np.std(residual)>0 else 0.
    lam=mass/amplitude if amplitude else 0
    witness=bool(.5<=amplitude<=1.5 and .001<=lam<=1 and rms<=2*noise and abs(lag)<=.2)
    return dict(raw_rms=rms,noise_proxy=noise,residual_lag1=lag,amplitude=amplitude,
        modulation=lam,long_grid_fraction=fraction,conditional_witness=witness)

def operator(payload,wall_seconds=120):
    begun=time.monotonic();candidates=[];attempts=0;stopped=False
    transforms={p:basis_transform(p)for p in P_GRID}
    for name,record in payload['records'].items():
        t,y,noise,K=arrays(record)
        for p in P_GRID:
            T=transforms[p]
            basis=np.column_stack([np.ones(len(t)),K@T])
            for k in K_GRID:
                if time.monotonic()-begun>wall_seconds:stopped=True;break
                attempts+=1;matrix=np.exp(-k*t[:,None])*basis
                try:
                    coefficients,_=nnls(matrix,y,maxiter=1000)
                    w=T@coefficients[1:]
                    candidates.append(dict(record=name,p=p,k=k,unmodulated_amplitude=float(coefficients[0]),
                        grid_weights=[[int(i),float(w[i])]for i in np.where(w>0)[0]]))
                except RuntimeError as exc:
                    candidates.append(dict(record=name,p=p,k=k,error='NNLS_ITERATION_STOP',detail=str(exc)))
            if stopped:break
        if stopped:break
    return dict(operator_id=OPERATOR_ID,input_id=digest(payload),candidates=candidates,
        solver_attempts=attempts,planned_attempts=len(payload['records'])*len(K_GRID)*len(P_GRID),
        wall_budget_stop=stopped,wall_seconds=time.monotonic()-begun)

def evaluate(payload,baseline,receipt,evidence=None,enabled=True):
    identity=digest(payload)
    if identity!=receipt['input_digest'] or digest(baseline)!=receipt['baseline_digest']:
        raise ValueError('SOURCE_OR_BASELINE_NOT_PREVIOUSLY_ADMITTED')
    names=set(payload['records'])
    if names!={r['record']for r in baseline['records']}:
        raise ValueError('BASELINE_RECORD_COVERAGE')
    trigger=sorted(r['record']for r in baseline['records']if not r['any_witness'])
    result=dict(rule_id=RULE_ID,rule_instance_id=RULE_ID+'::'+identity,input_id=identity,
        triggered_records=trigger,development_adapter=True,status='UNRESOLVED',
        remaining_obligations=['FINITE_SHAPE_FAMILY_ADEQUACY_CHECK'] if trigger else [],
        evidence_applications=0,full_question_answer=False,protein_population=False)
    if not enabled or not trigger or evidence is None:return result
    if evidence.get('operator_id')!=OPERATOR_ID or evidence.get('input_id')!=identity:
        raise ValueError('EVIDENCE_PRODUCER_INPUT_MISMATCH')
    if len(evidence['candidates'])!=evidence['solver_attempts']:
        raise ValueError('ATTEMPT_COVERAGE')
    seen=set();audited={name:[]for name in names};numeric={name:arrays(payload['records'][name])for name in names}
    for candidate in evidence['candidates']:
        name=candidate['record'];key=(name,candidate['p'],candidate['k'])
        if name not in names or key in seen:raise ValueError('DUPLICATE_OR_FOREIGN_PROFILE_POINT')
        seen.add(key)
        if 'error' in candidate:
            if candidate['error']!='NNLS_ITERATION_STOP':raise ValueError('UNKNOWN_SOLVER_STOP')
            continue
        metrics=audit_candidate(candidate,*numeric[name])
        audited[name].append(dict(p=candidate['p'],k=candidate['k'],**metrics))
    expected={(name,p,k)for name in names for p in P_GRID for k in K_GRID}
    if not seen<=expected or (not evidence['wall_budget_stop'] and seen!=expected):
        raise ValueError('INCOMPLETE_PROFILE_GRID')
    results={}
    for name,points in audited.items():
        good=[point for point in points if point['conditional_witness']]
        results[name]=dict(any_witness=bool(good),allowed_tested_p=sorted({c['p']for c in good if c['p']is not None}),
            witness_points=good,best_rms_point=min(points,key=lambda c:c['raw_rms'])if points else None,
            failed_search_is_exclusion=False)
    changed=[name for name in trigger if results[name]['any_witness']]
    result.update(evidence_applications=1,results=results,
        model_adequacy_changed_records=changed,
        partial_claim='LIMITED_GAUSSIAN_FAILURE_NOT_STABLE_TO_FINITE_SHAPE_FLEXIBILITY' if changed else 'METHOD_ADEQUACY_STILL_UNRESOLVED',
        remaining_obligations=['NOISE_BACKGROUND_TIMEORIGIN_AND_MODEL_APPLICABILITY','STRUCTURAL_ASSIGNMENT_AND_PROBE_REFERENCE'],
        numerical_grid_completed=seen==expected,
        claim_ceiling=['Conditional finite-grid witnesses only; no confidence interval or exclusion.',
                      'p is grid mass at r>=5.5nm, not prior Gaussian-component p or protein population.',
                      'No author inverse or source-fitted distribution used as scientific target.'])
    if seen!=expected:result['remaining_obligations'].insert(0,'INCOMPLETE_NUMERICAL_GRID')
    return result

def run(payload,baseline,receipt,enabled=True):
    before=evaluate(payload,baseline,receipt,enabled=enabled)
    if not enabled or not before['triggered_records']:
        return dict(before=before,after=before,operator_calls=0,evidence=None)
    evidence=operator(payload)
    after=evaluate(payload,baseline,receipt,evidence)
    return dict(before=before,after=after,operator_calls=1,evidence=evidence)
