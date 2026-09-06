"""First manual summary-data main; not raw lab reproduction or covariance estimation."""
import json,math
from pathlib import Path
T=Path(__file__).resolve().parents[1];D=T/'outputs/q14_source_admission_v1';out=T/'outputs/q14_summary_ratio_main_v1'
if out.exists():raise FileExistsError(out)
s=json.loads((D/'measurement_summary.json').read_text());ref=json.loads((D/'reference_model.json').read_text())
rows=[];jac=[];sd=[];means=[]
for pair in ['1','2']:
 a,b=[s['samples'][pair+'-'+x]for x in ['lo','mid']];x,y=a['R_apparent_A'],b['R_apparent_A'];g=[1/y,-x/y**2];ratio=x/y
 rows.append(dict(pair=pair,ratio=ratio,zero_covariance_delta_sd=math.hypot(g[0]*a['R_sd_A'],g[1]*b['R_sd_A'])))
 means.extend([x,y]);sd.extend([a['R_sd_A'],b['R_sd_A']]);jac.extend([v*(1 if pair=='1' else -1) for v in g])
f=lambda x:x[0]/x[1]-x[2]/x[3]
errors=[]
for i in range(4):
 xp=means.copy();xm=means.copy();xp[i]+=1e-4;xm[i]-=1e-4;errors.append(abs((f(xp)-f(xm))/2e-4-jac[i]))
assert max(errors)<1e-10
model=[]
for pair in ['1','2']:
 a,b=[ref['samples'][pair+'-'+x]for x in ['lo','mid']]
 model.append(dict(pair=pair,ratio=a['R_model_A']/b['R_model_A'],parameter_box_ratio=[(a['R_model_A']-a['spread_A'])/(b['R_model_A']+b['spread_A']),(a['R_model_A']+a['spread_A'])/(b['R_model_A']-b['spread_A'])],role='AUTHOR_REFERENCE_PARAMETER_SENSITIVITY_NOT_CI'))
report=dict(status='CONDITIONAL_SUMMARY_RATIOS_COVARIANCE_UNRESOLVED',ratios=rows,cross_pair_difference=f(means),main_inputs=dict(means_A=means,published_sd_A=sd),difference_jacobian=jac,zero_covariance_difference_sd=math.sqrt(sum((g*s)**2 for g,s in zip(jac,sd))),covariance_status='UNAVAILABLE_NOT_ASSUMED_ZERO_FOR_CONCLUSION',zero_covariance_role='EXPLICIT_BASELINE_ONLY',shared_R0='Cancels exactly only when identical within pair; sample-specific factor remains unknown',reference=model,jacobian_max_error=max(errors),full_question_answer=False,new_numerical_operators=0,limits=['Published dispersion not SEM/CI; no certified independent lab sample size.','Mean of apparent lab distances not distance transformed from pooled E.','Unknown calibration covariance and dye model variation prevent full quantitative comparison.'])
out.mkdir();(out/'report.json').write_text(json.dumps(report,indent=2)+'\n');(out/'measurement_input.json').write_text(json.dumps(s,indent=2)+'\n');print(json.dumps(report,indent=2))
