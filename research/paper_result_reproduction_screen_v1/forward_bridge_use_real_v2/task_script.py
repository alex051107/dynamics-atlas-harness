"""Admit existing sources, then run common F05R02 phase on real bridge uses."""
import json,pathlib,copy
from unittest.mock import patch
from dynamics_atlas_harness import forward_bridge_use_v1 as f
from dynamics_atlas_harness import q15_cross_modal_evidence_v1 as q15
from dynamics_atlas_harness import q16_shape_flexibility_v1 as q16
ROOT=pathlib.Path(__file__).resolve().parents[1];OUT=ROOT/'outputs/forward_bridge_use_real_v2'
if OUT.exists():raise FileExistsError(OUT)
def read(s):return json.loads((ROOT/'outputs'/s).read_text())
context={'inputs':{},'admissions':{}}
graph=copy.deepcopy(read('q15_rules_probe_v1/projected_casegraph.json'));graph['case']['case_id']='development-bridge-use-comparison';graph['forward_bridge_uses']=[]
bundle=read('q15_rules_probe_v1/rules_bundle_snapshot.json')
# Source objects have already been admitted; do not rewrite the old graph lineage.
original=dict(main=read('q15_apbs_comparison_v1/report.json'),summary=read('q15_pro19_verification_v1/report.json'),deer=read('q15_deer_source_audit_v1/report.json'),forward=read('q15_probe_forward_source_facts_v1.json'))
q15.verify_admitted_sources(original)
# Source verification and matched numeric summary guard happen before new admission.
q15.synthesize_manual_evidence(*(original[k]for k in ['main','summary','deer','forward']))
def add(use_id,scope,method,data,receipts,basis,assumptions):
 ref='input-'+use_id;value=dict(scope=scope,method_id=method,data=data)
 context['inputs'][ref]=value
 context['admissions'][ref]=dict(input_digest=f.digest(value),source_receipts=receipts,method_basis=basis,conditional_assumptions=assumptions,authority_binding=dict(source_id=scope['source_id'],source_version='source-receipts:'+','.join(receipts),measurement_version='derived-input:'+use_id,relationship_to_graph='LATER_ADMITTED_SOURCE_FOR_CURRENT_USE',relevant_contradictions=[]),role='NEW_DERIVED_INPUT_ADMISSION_FROM_PRIOR_SOURCES_NOT_SCIENTIFIC_APPROVAL')
 graph['forward_bridge_uses'].append(dict(contract=f.CONTRACT,use_id=use_id,scope=scope,method_id=method,input_ref=ref,requested_use='MODEL_OBSERVATION_COMPARISON'))
for pair in ['55_175','175_228']:
 pred=original['forward']['pairs'][pair]['FRET_sim'];diag=original['summary']['diagnostics'][pair]
 add('reference-'+pair,dict(source_id='Q15_APBS_'+pair,model_id='author-open-closed-reference',observable='FRET_E',probe='AF555_AF647_'+pair,condition='apo:1mM_sialic_acid',unit='dimensionless_efficiency',aggregation='equal_repetition_mean_E_vs_efficiency_weighted_reference_R',target_support='apo:holo'),
 'efficiency_weighted_reference_direction_v1',dict(reference_definition='EFFICIENCY_WEIGHTED_DISTANCE',observed_change=original['main']['condition_comparisons'][pair]['holo_minus_apo_E'],reference_apo=pred['apo'],reference_holo=pred['holo'],direction_checks=[diag['equal_repetition_median_effect'],*diag['leave_one_per_condition_effects']]),
 ['q15_admitted_source_receipt_v2.json','q15_probe_forward_source_facts_v1.json'],original['forward']['locator']+'; stable-probe reference hypothesis; no mean-distance conversion',['stable-probe reference hypothesis','efficiency-weighted reference output, not mean distance'])
payload=read('q16_shape_flexibility_v1/input.local.json');base=read('q16_conditional_feasibility_v1/report.json');receipt=read('q16_shape_flexibility_v1/admission_receipt.json');e=read('q16_shape_flexibility_v1/evidence.json')
assert q16.digest(payload)==receipt['input_digest'] and q16.digest(base)==receipt['baseline_digest']
# Choose first previously reported training witness per record, without selecting tail success.
saved=read('q16_saved_tail_audit_v1/report.json');selected=[]
for name in sorted({x['record']for x in saved['tail_candidates']}):
 row=next(x for x in saved['tail_candidates']if x['record']==name and x['conditional_witness'])
 candidate=next(x for x in e['candidates']if x['record']==name and x['p']==row['p']and x['k']==row['k'])
 source='source-'+name;graph['evidence_items'].append(dict(source_id=source,case_evidence_scope='CLAIM_EVIDENCE',evidence_role='DIAGNOSTIC',data_lineage_status='AGENT_PROPOSED_UNVERIFIED'))
 full=payload['records'][row['full_record']];training=payload['records'][name]
 scope=dict(source_id=source,model_id='saved-candidate-'+name+'-'+str(candidate['p'])+'-'+str(candidate['k']),observable='DEER_raw_real',probe='spin_'+name,condition='same_EG_record',unit='microsecond_normalized_signal',aggregation='time_trace_not_independent_repeats',target_support=[row['heldout_start'],row['heldout_end'],row['heldout_n']])
 add('prediction-'+name,scope,'fixed_deer_prediction_screen_v1',dict(training_record=training,target_record=full,candidate=candidate),['q16_shape_flexibility_v1/admission_receipt.json','q16_saved_tail_audit_v1/report.json'],'Frozen 2..10nm finite kernel; fixed saved parameters; RMS<=2 training-noise and abs(lag1)<=.2 descriptive only',['fixed saved candidate','training-noise RMS and lag screen only'])
 selected.append(dict(use_id='prediction-'+name,record=name,p=row['p'],k=row['k'],expected_rms=row['heldout_rms'],expected_lag1=row['heldout_lag1']))
# Seal derived inputs before any new computation; original source admissions remain distinct.
OUT.mkdir();(OUT/'admission.json').write_text(json.dumps(context,indent=2)+'\n');(OUT/'casegraph.json').write_text(json.dumps(graph,indent=2)+'\n')
kwargs=dict(case_graph=graph,runtime_subrules=bundle['runtime_subrules'],bindings=bundle['bindings'],contracts=bundle['contracts'])
with patch.object(q16,'nnls',side_effect=AssertionError('NO_OPTIMIZATION')),patch.object(q16,'operator',side_effect=AssertionError('NO_REFIT')):
 off=f.run_checks(**kwargs,context=context,enabled=False)
 on=f.run_checks(**kwargs,context=context)
 ctx=copy.deepcopy(context);ctx['evidence']=on['evidence'];reentry=f.run_checks(**kwargs,context=ctx)
for row in selected:
 actual=next(x for x in on['after']if x.get('use_id')==row['use_id'])['numerical']
 assert abs(actual['rms']-row['expected_rms'])<1e-12 and abs(actual['lag1']-row['expected_lag1'])<1e-12
summary=[{k:x.get(k)for k in ['use_id','status','local_support','check_completed','remaining_obligations']}for x in on['after']if x.get('runtime_subrule_id')==f.RULE_ID]
assert len(on['operator_calls'])==4 and not off['operator_calls'] and not reentry['operator_calls']
for name,value in [('on',on),('off',off),('reentry',reentry)]: (OUT/(name+'.json')).write_text(json.dumps(value,indent=2)+'\n')
report=dict(summary=summary,on_calls=4,off_calls=0,reentry_calls=0,new_fits=0,original_manual_calculations_reclassified=False,selected_tail_candidates=selected,full_question_count_change=0,scope='Development replay on previously exposed same-paper cases; not blind generalization or science accuracy.')
(OUT/'report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False))
