"""Conditional raw DEER feasibility witnesses; not original inverse reproduction.

Six records, finite two-Gaussian family, free background and modulation depth.
Unknown global optimum and unaccepted proxy noise preclude confidence/exclusion claims.
"""
import json, time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from q16_forward_method_audit_v1 import kernel

TASK=Path(__file__).resolve().parents[1]
R=np.linspace(2,10,201)
WIDTH=np.full(201,.04); WIDTH[[0,-1]]=.02
LOW=np.array([.5,0,.001,2,.08,5.5,.08,0.])
HIGH=np.array([1.5,1,1,5.5,2,10,2,1.])
STARTS=[np.array([1,.05,.3,3.5,.5,7,.5,.3]),np.array([1,.05,.3,4.5,1,8.5,1,.7])]

def gaussian(mu,sigma):
    exponent=-.5*((R-mu)/sigma)**2
    mass=np.exp(exponent-exponent.max())*WIDTH
    mass/=mass.sum()
    a=(R-mu)/sigma**2; b=(R-mu)**2/sigma**3
    return mass,mass*(a-mass@a),mass*(b-mass@b)

def forward(x,t,K):
    A,k,lam,rs,ss,rl,sl,p=x
    Ps,ds,ws=gaussian(rs,ss);Pl,dl,wl=gaussian(rl,sl)
    Fs,Fl=K@Ps,K@Pl
    mixture=(1-p)*Fs+p*Fl
    decay=np.exp(-k*t);pref=A*decay
    factor=1-lam+lam*mixture
    prediction=pref*factor
    jac=np.column_stack([decay*factor,-t*prediction,pref*(mixture-1),
        pref*lam*(1-p)*(K@ds),pref*lam*(1-p)*(K@ws),
        pref*lam*p*(K@dl),pref*lam*p*(K@wl),pref*lam*(Fl-Fs)])
    return prediction,jac

def main():
    out=TASK/'outputs/q16_conditional_feasibility_v1';out.mkdir(exist_ok=False)
    tc=np.linspace(0,6.88,31);kc=kernel(tc,R);x=STARTS[0].copy()
    pred,jac=forward(x,tc,kc)
    numerical=np.empty_like(jac)
    for i in range(8):
        step=1e-6;xp=x.copy();xm=x.copy();xp[i]+=step;xm[i]-=step
        numerical[:,i]=(forward(xp,tc,kc)[0]-forward(xm,tc,kc)[0])/(2*step)
    err=float(np.max(np.abs(jac-numerical)))
    assert err<1e-7,err
    source=json.loads((TASK/'outputs/q16_observation_independence_v2/source_curves.local.json').read_text())
    records=[]
    for pair in ['29','36']:
        for mode,condition,cut in [('long_full','eg50_1mM',6.88),('long_raw_cropped','eg50_1mM',4.896),('actual_noEG_raw','eg0_1mM',4.896)]:
            key=f'SI Figure10:{pair}_{condition}'
            raw=np.asarray(source[key]['raw'],float)
            raw=raw[(raw[:,0]>=0)&(raw[:,0]<=cut+1e-9)]
            records.append((pair+'_'+mode,key,raw))
    begun=time.monotonic();calls=[];summaries=[];curves={};interrupted=None
    def fit(name,t,y,K,noise,start,fixed_p):
        initial=start if fixed_p is None else start[:-1]
        bounds=(LOW,HIGH) if fixed_p is None else (LOW[:-1],HIGH[:-1])
        cache={}
        def calculate(z):
            if time.monotonic()-begun>120:raise TimeoutError('BATCH_WALL_BUDGET')
            if 'x' not in cache or not np.array_equal(z,cache['x']):
                full=z if fixed_p is None else np.r_[z,fixed_p]
                prediction,j=forward(full,t,K)
                cache.update(x=z.copy(),f=(prediction-y)/noise,j=j/noise if fixed_p is None else j[:,:-1]/noise)
            return cache
        result=least_squares(lambda z:calculate(z)['f'],initial,jac=lambda z:calculate(z)['j'],
            bounds=bounds,max_nfev=500,ftol=1e-10,xtol=1e-10,gtol=1e-8,x_scale='jac')
        full=result.x if fixed_p is None else np.r_[result.x,fixed_p]
        prediction,_=forward(full,t,K);residual=prediction-y
        rms=float(np.sqrt(np.mean(residual**2)));lag=float(np.corrcoef(residual[:-1],residual[1:])[0,1])
        witness=bool(np.isfinite(prediction).all() and rms<=2*noise and abs(lag)<=.2)
        call=dict(record=name,call_index=len(calls),fixed_p=fixed_p,x=full.tolist(),
            weighted_sse=float(np.sum((residual/noise)**2)),raw_rms=rms,noise_proxy=noise,
            residual_lag1=lag,criterion_witness=witness,solver_success=bool(result.success),
            solver_status=int(result.status),nfev=int(result.nfev),optimality=float(result.optimality),
            numerical_stationarity=bool(result.optimality<1e-3),
            active_bounds=[i for i in range(8) if min(abs(full[i]-LOW[i]),abs(full[i]-HIGH[i]))<1e-4])
        calls.append(call)
        with (out/'calls.jsonl').open('a')as f:f.write(json.dumps(call,allow_nan=False)+'\n')
        return call,prediction,residual
    try:
        for name,key,raw in records:
            t,y=raw[:,0],raw[:,1];d=np.diff(raw[:,3])
            noise=float(np.median(np.abs(d-np.median(d)))/(.6744897501960817*np.sqrt(2)))
            assert noise>0
            K=kernel(t,R)
            base=[fit(name,t,y,K,noise,start,None) for start in STARTS]
            best=min(base,key=lambda item:item[0]['weighted_sse'])
            profile=[]
            for p in [0.,.25,.5,.75,1.]:
                results=[fit(name,t,y,K,noise,start,p)for start in [np.array(best[0]['x']),STARTS[1]]]
                chosen=min(results,key=lambda item:item[0]['weighted_sse'])
                profile.append(dict(p=p,any_witness=any(v[0]['criterion_witness']for v in results),
                    best_sse_call=chosen[0]['call_index'],all_stationary=all(v[0]['numerical_stationarity']for v in results)))
            selected=[v for v in calls if v['record']==name]
            summaries.append(dict(record=name,source_block=key,n=len(t),end_us=float(t[-1]),noise_proxy=noise,
                best_free=best[0],profile=profile,any_witness=any(v['criterion_witness']for v in selected),
                allowed_tested_p=[v['p']for v in profile if v['any_witness']],
                exclusion='NO_EXCLUSION_FROM_FAILED_LOCAL_SEARCH'))
            curves[name]=dict(time=t.tolist(),observed=y.tolist(),best_free_prediction=best[1].tolist(),residual=best[2].tolist())
            print(name,'allowedtestedp',summaries[-1]['allowed_tested_p'],'freeRMS/noise',best[0]['raw_rms']/noise,'lag',best[0]['residual_lag1'],flush=True)
    except TimeoutError as exc:interrupted=str(exc)
    report=dict(status='CONDITIONAL_FINITE_FAMILY_WITNESSES' if any(x['any_witness']for x in summaries) else 'NO_ADEQUATE_WITNESS_METHOD_STOP',
        completed_records=len(summaries),planned_records=6,optimizer_calls=len(calls),wall_seconds=time.monotonic()-begun,
        interrupted=interrupted,analytic_derivative_max_abs_error=err,records=summaries,
        rules_extra_credit=0,first_manual_conditional_main=True,original_inverse_reproduced=False,
        model='A exp(-kt)[1-lambda+lambda((1-p)Gshort+pGlong)]',
        parameter_names=['A','k_per_us','lambda','short_center_nm','short_width_nm','long_center_nm','long_width_nm','p'],
        bounds=[LOW.tolist(),HIGH.tolist()],distance_grid_nm=[2,10,201],
        source_roles_used=['raw time','raw real','raw imaginary noise proxy'],
        source_roles_excluded=['authorfit','authorP(r)','depositedbackground'],
        criterion='rawRMS<=2*window-local imaginarydiffMADscale andabsresiduallag1<=.2; conditional screen,notCI',
        limits=['Local search and finite Gaussian family; failed search never excludes p.',
                'p is long-centered Gaussian contribution; overlapping tails mean not exact mass above5.5nm.',
                '5.5nm is declared analysis partition, not an open/closed structural boundary.',
                'Fixed published timeorigin; no new phase calibration. Noiseproxy not an accepted likelihood.',
                'Monotone exponential background may be inadequate; deposited29EG50background increases.',
                'No original inverse reproduction, protein population or final scientific answer.'])
    (out/'report.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    (out/'curves.local.json').write_text(json.dumps(curves,allow_nan=False)+'\n')
    print('END',report['status'],'calls',len(calls),'seconds',report['wall_seconds'],flush=True)

if __name__=='__main__':main()
