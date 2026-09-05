"""Frozen specialist diagnostics, with no automatic-routing credit."""
import json, pathlib, subprocess, inspect, copy
from unittest.mock import patch
from dynamics_atlas_harness import q14_correlation_sensitivity_v1 as a
from dynamics_atlas_harness import q15_cross_modal_evidence_v1 as b
from dynamics_atlas_harness import q16_shape_flexibility_v1 as c
ROOT=pathlib.Path(__file__).resolve().parents[1]
OUT=ROOT/'outputs/frozen_capability_diagnostic_v1'
if OUT.exists(): raise FileExistsError(OUT)
head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
assert head=='6b5856e3381314f698429f725a5a194ff94a932a'
def read(n): return json.loads((ROOT/'outputs'/n).read_text())
results={'frozen_head':head,'scope':'Exposed development diagnostic. Specialist selection supplied by harness; not end-to-end routing or accuracy.','production_edits':0,'new_fits':0,'new_operator_calls':0}
s=read('q14_source_admission_v1/measurement_summary.json');m=read('q14_summary_ratio_main_v1/report.json');r=read('q14_correlation_admission_v1.json');e=read('q14_correlation_sensitivity_v1/evidence.json')
with patch.object(a,'operator',side_effect=AssertionError('NO_OPERATOR')):
 x=a.evaluate(s,m,r,evidence=e)
results['Q14']={'specialist_result':x,'automatic_selection':'NOT_TESTED_BY_SPECIALIST_CALL','required_inputs':['source','manual main report','prior admission receipt'],'finding':'Existing numeric component consumes evidence; selected path and covariance-status prerequisite supplied externally. Partial answer only.'}
original=dict(main=read('q15_apbs_comparison_v1/report.json'),summary=read('q15_pro19_verification_v1/report.json'),deer=read('q15_deer_source_audit_v1/report.json'),forward=read('q15_probe_forward_source_facts_v1.json'))
r=read('q15_dye_admission_v2.json');dyes={k:read(v['path']) for k,v in r['sources'].items()}
e=b.synthesize_manual_evidence(*(original[k] for k in ['main','summary','deer','forward']))
x=b.evaluate(original['main'],e,admitted_sources=original,dye_sources=dyes,dye_receipt=r,dye_evidence=read('q15_question_answer_v3/evidence.json'))
results['Q15']={'specialist_result':x,'automatic_selection':'NOT_TESTED_BY_SPECIALIST_CALL','finding':'Saved admitted sources reach bounded scientific synthesis through selected specialist. Alternative complete-answer coverage unmeasured.'}
p=read('q16_shape_flexibility_v1/input.local.json');base=read('q16_conditional_feasibility_v1/report.json');r=read('q16_shape_flexibility_v1/admission_receipt.json');e=read('q16_shape_flexibility_v1/evidence.json');tail=read('q16_saved_tail_audit_v1/report.json')
aug=copy.deepcopy(e);aug['tail_audit']=tail
with patch.object(c,'operator',side_effect=AssertionError('NO_OPERATOR')),patch.object(c,'nnls',side_effect=AssertionError('NO_NNLS')):
 x=c.evaluate(p,base,r,evidence=aug)
old=read('q16_saved_tail_audit_v1/saved_evidence_reassessment.json')
results['Q16']={'specialist_result':x,'unchanged_vs_saved_without_tail':x==old,'tail_summary':tail['summary'],'supported_signature':str(inspect.signature(c.evaluate)),'finding':'Additional tail_audit field ignored. Unsupported-evidence-extension diagnostic, not a formally supported tail contract. Source confirms no native tail-consumption path.','automatic_selection':'NOT_TESTED_BY_SPECIALIST_CALL'}
assert results['Q16']['unchanged_vs_saved_without_tail']
OUT.mkdir();(OUT/'report.json').write_text(json.dumps(results,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
print(json.dumps({'head':head,'Q14_full':results['Q14']['specialist_result']['full_question_answer'],'Q15_synthesis':results['Q15']['specialist_result']['question_answer_candidate']['scientific_synthesis']['status'],'Q16_tail_extension_ignored':results['Q16']['unchanged_vs_saved_without_tail'],'new_fits':0,'new_operators':0},ensure_ascii=False))
