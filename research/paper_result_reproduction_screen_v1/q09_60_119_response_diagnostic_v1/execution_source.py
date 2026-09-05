"""Bounded real-reference diagnostic; new IRF policy, no scientific state verdict."""
import datetime,functools,json,time
from pathlib import Path
from unittest.mock import patch
import numpy as np
from scipy.optimize import minimize
from dynamics_atlas_harness import q09_global_comparison_v1 as a

W=Path(__file__).resolve().parents[4];T=Path(__file__).resolve().parents[1]
O=T/'outputs/q09_60_119_response_diagnostic_v1'
METHOD={'version':'60-119-response-diagnostic/v1','IRF_shift':'padded_linear_v2','window':'unchangedIBH17HanningLin>0.1medianpositive','dt_ns':.0141,'donor_components':2,'FRET_components':2,'sigma_A':6.,'scatter':0.,'max_fits':10,'seconds_per_fit':60,'maxiter':1500,'gradient_limit':1e-6,'shared_reference_applicability':'UNKNOWN','role':'MANUAL_METHOD_DIAGNOSTIC_NOT_RULES_GAIN','fit_regions_ns':[0,5,10,20,40,60]}
SINGLE_BOUNDS=[(.05,10.),(.05,10.),(0.,1.),(1e-12,.05),(-5.,5.)]
NULL_BOUNDS=SINGLE_BOUNDS+[(1e-12,.05),(-5.,5.)]

def save(n,v):(O/n).write_text(json.dumps(v,indent=2,ensure_ascii=False,allow_nan=False)+'\n')
def optimize(bounds,initial,fun):
    lo=np.array([b[0] for b in bounds]);span=np.array([b[1]-b[0] for b in bounds]);start=time.monotonic();best={'parameters':list(initial),'objective':float(fun(initial))};calls=0
    def wrapped(z):
        nonlocal calls
        if time.monotonic()-start>60:raise TimeoutError('DECLARED_60S_BUDGET')
        calls+=1;p=lo+span*z;val=float(fun(p))
        if val<best['objective']:best.update(parameters=p.tolist(),objective=val)
        return val
    def jac(z):
        grad=[]
        for i in range(len(z)):
            h=1e-5*max(abs(z[i]),.001);u=z.copy();v=z.copy();u[i]=min(1,z[i]+h);v[i]=max(0,z[i]-h);grad.append((wrapped(u)-wrapped(v))/(u[i]-v[i]))
        return np.array(grad)
    success=False;nit=None
    try:
        result=minimize(wrapped,(np.array(initial)-lo)/span,jac=jac,bounds=[(0,1)]*len(lo),method='L-BFGS-B',options={'maxiter':1500,'ftol':1e-15,'gtol':1e-11,'maxfun':20000});success=bool(result.success);message=str(result.message);nit=int(result.nit)
    except TimeoutError as err:message=str(err)
    pg=float(max(abs(a.q.gradient_at(best['parameters'],bounds,fun))))
    return dict(best,initial=list(initial),optimizer_success=success,iterations=nit,message=message,evaluations=calls,projected_gradient_inf=pg,numerical_status='PASS' if success and pg<=1e-6 else 'NUMERICAL_STOP_WITH_FEASIBLE_POINT',elapsed_seconds=time.monotonic()-start)

def main():
    O.mkdir(exist_ok=False);d=a.GlobalData(T/'inputs/q09_author');gr=next(g for g in d.groups if g.owners==['60-119']);assert gr.donors==2
    save('method.json',METHOD);old=json.loads((a.ROOT/'q09_global_comparison_v1/evidence.json').read_text())['local_runs'][gr.ref]
    bound={'source_input_id':d.input_id,'method':METHOD,'reference':gr.ref,'roles':list(gr.records),'old_result_review_side':old,'source_mapping':[x for x in d.mapping if x['variant']=='60-119']};save('input_receipt.json',bound)
    expected=functools.partial(a.expected_counts,shift_policy=METHOD['IRF_shift'])
    def single_counts(role,p):
        r=gr.records[role];f=r['kernel'].intrinsic_donor(p[:2],[p[2],1-p[2]])
        return expected(f,r['irf'],r['Lin'],r['mask'],float(r['y'][r['mask']].sum()),shift_bins=p[4],background_fraction=p[3])
    def single_loss(role,p):
        r=gr.records[role];mask=r['mask'];return a.poisson_deviance(r['y'][mask],single_counts(role,p)[mask])/float(r['y'][mask].sum())
    e={'method':METHOD,'input_id':a.q.digest(bound),'single_runs':{},'shared_null_runs':[],'FRET2_runs':[],'new_fits':0}
    for role in gr.records:
        e['single_runs'][role]=[]
        for seed in [[1.,4.,.3,.001,0.],[.3,3.,.6,.001,0.]]:
            r=optimize(SINGLE_BOUNDS,seed,lambda p:single_loss(role,p));e['single_runs'][role].append(r);e['new_fits']+=1;save('evidence.json',e);print(role,r['numerical_status'],r['objective'],flush=True)
    accepted={role:[r for r in runs if r['numerical_status']=='PASS'] for role,runs in e['single_runs'].items()}
    if any(not v for v in accepted.values()):
        save('receipt.json',{'status':'SEPARATE_RESPONSE_NUMERIC_STOP','fits':e['new_fits'],'dependent_fits_run':0});return 0
    best={role:min(rs,key=lambda r:r['objective']) for role,rs in accepted.items()};p0=best[gr.ref]['parameters'];pa=best['60-119']['parameters']
    def null_counts(p):return {gr.ref:single_counts(gr.ref,p[:5]),'60-119':single_counts('60-119',list(p[:3])+list(p[5:7]))}
    def loss(pred):return sum(a.poisson_deviance(r['y'][r['mask']],pred[role][r['mask']]) for role,r in gr.records.items())/gr.total
    for seed in [p0+pa[-2:],old['parameters'][:5]+old['parameters'][-2:]]:
        fit=optimize(NULL_BOUNDS,seed,lambda p:loss(null_counts(p)));e['shared_null_runs'].append(fit);e['new_fits']+=1;save('evidence.json',e);print('sharednull',fit['numerical_status'],fit['objective'],flush=True)
    with patch.object(a,'expected_counts',expected):
        for distances in [[20.,40.],[35.,65.],[60.,90.],[15.,100.]]:
            seed=p0+distances+[.5,.2]+pa[-2:]
            fit=a.optimize_local(gr,seed);e['FRET2_runs'].append(fit);e['new_fits']+=1;save('evidence.json',e);print('FRET2',fit['numerical_status'],fit['objective'],flush=True)
        bestF=min(e['FRET2_runs'],key=lambda r:r['objective']);fret_predictions=gr.predict(bestF['parameters'],'local2')
    bestN=min(e['shared_null_runs'],key=lambda r:r['objective'])
    models={'separate_effective_response':{role:single_counts(role,x['parameters']) for role,x in best.items()},'shared_donor_only_null':null_counts(bestN['parameters']),'shared_donor_FRET2':fret_predictions}
    region=[]
    for model,pred in models.items():
        for role,r in gr.records.items():
            for lo,hi in zip(METHOD['fit_regions_ns'][:-1],METHOD['fit_regions_ns'][1:]):
                mask=r['mask']&(r['kernel'].t>=lo)&(r['kernel'].t<hi)
                region.append({'model':model,'role':role,'region_ns':[lo,hi],'included_bins':int(mask.sum()),'observed_counts':int(r['y'][mask].sum()),'predicted_counts':float(pred[role][mask].sum()),'deviance':float(a.poisson_deviance(r['y'][mask],pred[role][mask]))})
    save('fixed_region_residuals.json',region)
    summary={'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'BOUNDED_RESPONSE_DIAGNOSTIC_COMPLETED','fits':e['new_fits'],'method':METHOD,'separate_total_deviance':sum(best[role]['objective']*float(r['y'][r['mask']].sum()) for role,r in gr.records.items()),'shared_null_best_D':bestN['objective']*gr.total,'FRET2_best_D':bestF['objective']*gr.total,'FRET2_best_parameters':bestF['parameters'],'FRET2_best_status':bestF['numerical_status'],'separate_effective_parameters':{role:x['parameters'] for role,x in best.items()},'old_joint_D_at_legacy_parameters':old['objective']*gr.total,'all_run_statuses':{**{role:[x['numerical_status'] for x in rs] for role,rs in e['single_runs'].items()},'shared_null':[x['numerical_status'] for x in e['shared_null_runs']],'FRET2':[x['numerical_status'] for x in e['FRET2_runs']]},'rules_controlled':False,'full_question_answer':False,'scientific_ceiling':'Effective independent decay fits diagnose latent-response transfer and localminima; no proof sample error/noFRET/state-number.'}
    save('receipt.json',summary);print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
