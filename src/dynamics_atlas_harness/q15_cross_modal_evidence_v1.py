"""Consume manual source evidence for a conditional, matched-pair comparison."""
import hashlib
import json
import math
from pathlib import Path

RULE_ID = 'Q15R02_MATCHED_PROBE_DIRECTION_V1'
PAIRS = {'55_175', '175_228'}
SOURCE_RECEIPT = Path(__file__).resolve().parents[2] / 'research/paper_result_reproduction_screen_v1/q15_admitted_source_receipt_v2.json'


def canonical_digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, allow_nan=False).encode()).hexdigest()


def verify_admitted_sources(sources, receipt=None):
    """Compare against a prior accepted version, not a digest of new input alone."""
    receipt = json.loads(SOURCE_RECEIPT.read_text()) if receipt is None else receipt
    if receipt.get('forward_distance_semantics') != 'FRET_EFFICIENCY_AVERAGED_MODEL_DISTANCE':
        raise ValueError('FORWARD_DISTANCE_SEMANTICS_NOT_ADMITTED')
    if set(sources) != {'main', 'summary', 'deer', 'forward'}:
        raise ValueError('ADMITTED_SOURCE_COVERAGE')
    for name, value in sources.items():
        if canonical_digest(value) != receipt['sources'][name]['canonical_sha256']:
            raise ValueError('SOURCE_NOT_PREVIOUSLY_ADMITTED:' + name)
    return receipt



def sign(value):
    if not math.isfinite(value):
        raise ValueError('NONFINITE_DIRECTION')
    return 1 if value > 0 else -1 if value < 0 else 0


def synthesize_manual_evidence(main, summary, deer, forward):
    """New relational synthesis; inputs remain previously computed/manual evidence."""
    if summary['input_id'] != main['input_id']:
        raise ValueError('FLUORESCENCE_INPUT_MISMATCH')
    if (set(main['condition_comparisons']) != PAIRS or set(forward['pairs']) != PAIRS
            or forward['system'] != 'HiSiaP'
            or forward['doi'] != '10.1038/s41467-022-31945-6'
            or forward['source_role'] != 'AUTHOR_COMPUTED_FORWARD_NOT_LOCAL_SIMULATION'):
        raise ValueError('MATCHED_SYSTEM_PAIR_SOURCE_REQUIRED')
    if deer['source_role'] != 'AUTHOR_PROCESSED_DEER_DISTRIBUTION_NOT_RAW_TRACE_REINVERSION':
        raise ValueError('DEER_SOURCE_ROLE')
    rows=[]
    for pair in sorted(PAIRS):
        curves={}
        for c in deer['curves']:
            if c['pair'].replace('/','_') != pair:continue
            if c['condition'] in curves:raise ValueError('DUPLICATE_DEER_CONDITION')
            curves[c['condition']]=c
        if set(curves) != {'apo','holo'}:raise ValueError('MATCHED_DEER_CONDITIONS_REQUIRED')
        deer_change=curves['holo']['mean_source_axis_units']-curves['apo']['mean_source_axis_units']
        prediction=forward['pairs'][pair]
        changes={k:prediction[k]['holo']-prediction[k]['apo'] for k in ['FRET_sim','PELDOR_sim']}
        effect=main['condition_comparisons'][pair]['holo_minus_apo_E']
        diagnostic=summary['diagnostics'][pair]
        if not math.isclose(diagnostic['equal_repetition_mean_effect'],effect,abs_tol=1e-12,rel_tol=0):
            raise ValueError('MANUAL_DIAGNOSTIC_DIFFERS_FROM_MAIN')
        sensitivity=[diagnostic['equal_repetition_median_effect'],*diagnostic['leave_one_per_condition_effects']]
        descriptive_direction_retained=sign(effect)!=0 and all(sign(x)==sign(effect) for x in sensitivity)
        expected_E_sign=-sign(changes['FRET_sim'])
        relation=('DESCRIPTIVE_DIRECTION_UNRESOLVED' if not descriptive_direction_retained
                  else 'DIRECTIONAL_AGREEMENT_WITH_REFERENCE_READOUT' if sign(effect)==expected_E_sign
                  else 'DIRECTIONAL_TENSION_WITH_REFERENCE_READOUT')
        rows.append({'pair':pair,'observed_E_effect':effect,
                     'descriptive_direction_retained_in_manual_checks':descriptive_direction_retained,
                     'DEER_central_mean_change_source_axis_units':deer_change,
                     'author_forward_distance_changes_A':changes,
                     'DEER_direction_matches_own_spin_prediction':sign(deer_change)==sign(changes['PELDOR_sim']) and sign(deer_change)!=0,
                     'fluorescence_relation':relation})
    digest=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True).encode()).hexdigest()
    return {'input_id':main['input_id'],'source_bindings':{'manual_summary':digest(summary),'manual_DEER':digest(deer),'author_forward':digest(forward)},
            'rows':rows,'provenance':'MANUAL_RELATIONAL_SYNTHESIS_OF_EXISTING_NUMERICAL_EVIDENCE',
            'new_numerical_operator_calls':0,
            'hypothesis':'Condition maps to its published structural reference prediction, with stable probe/readout; no changing ensemble or dye parameters assumed.',
            'limits':['No mean-E to absolute-distance conversion','Not a local FPS or spin-label simulation',
                      'DEER uses author-processed curves and common positive source-axis scale; original nm/Angstrom conflict retained',
                      'Cryogenic DEER and fluorescence are not pooled into a common population',
                      'Directional tension is not formal ensemble-model rejection or proof of a unique dye mechanism']}


def evaluate(main, evidence=None, enabled=True, *, admitted_sources=None, source_receipt=None):
    instance=RULE_ID+'::'+main['input_id']
    result={'rule_id':RULE_ID,'rule_instance_id':instance,'input_id':main['input_id'],
            'development_adapter':True,
            'status':'UNRESOLVED','partial_claims':[],
            'remaining_obligations':['MATCHED_DEER_AND_FORWARD_EVIDENCE','TMR_CY5_DOUBLE_LABEL_DATA_AND_CALIBRATION'],
            'full_question_answer':False,'new_numerical_operator_calls':0,'evidence_applications':0}
    if not enabled or evidence is None:return result
    if evidence.get('input_id')!=main['input_id'] or {r.get('pair') for r in evidence.get('rows',[])}!=PAIRS or len(evidence.get('rows',[]))!=2:
        raise ValueError('EVIDENCE_INPUT_PAIR_BINDING')
    if admitted_sources is None:
        raise ValueError('PREVIOUSLY_ADMITTED_SOURCES_REQUIRED')
    if admitted_sources.get('main') != main:
        raise ValueError('MAIN_SOURCE_MISMATCH')
    verify_admitted_sources(admitted_sources, source_receipt)
    expected=synthesize_manual_evidence(*(admitted_sources[k] for k in ['main','summary','deer','forward']))
    if evidence != expected:
        raise ValueError('EVIDENCE_DIFFERS_FROM_ADMITTED_NUMERICAL_SYNTHESIS')
    # Both relation and ceiling are evaluator-owned, rebuilt from admitted values.
    evidence=expected
    result.update(partial_claims=evidence['rows'],evidence_applications=1,
                  remaining_obligations=['TMR_CY5_DOUBLE_LABEL_DATA_AND_CALIBRATION','PROBE_AND_SAMPLE_CONDITION_EXPLANATIONS'],
                  source_bindings=evidence['source_bindings'],claim_ceiling=evidence['limits'],
                  comparison_hypothesis=evidence['hypothesis'],
                  partial_answer_status='MATCHED_DIRECTIONAL_EVIDENCE_AVAILABLE',
                  source_request_route='REQUEST_NEW_DATA_IF_PUBLIC_SOURCE_SEARCH_EXHAUSTED')
    return result
