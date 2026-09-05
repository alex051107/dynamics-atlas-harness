"""Opt-in F05R02 numerical use checks; never a whole-question sufficiency test.

The platform supplies prior input admissions separately from the proposed CaseGraph.
Use scopes identify the *requested* observation, not the training observation.
"""
import hashlib
import json
import math

RULE_ID = 'F05R02_MODEL_OBSERVATION_USE_V1'
CONTRACT = 'forward-bridge-use/v1'
METHODS = {'efficiency_weighted_reference_direction_v1', 'fixed_deer_prediction_screen_v1'}
REQUESTS = {'OBSERVATION_DESCRIPTION', 'MODEL_OBSERVATION_COMPARISON', 'STRUCTURAL_POPULATION'}
SCOPE_FIELDS = {'source_id', 'model_id', 'observable', 'probe', 'condition', 'unit', 'aggregation', 'target_support'}


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, allow_nan=False).encode()).hexdigest()


def numerical_check(method, data):
    if method == 'efficiency_weighted_reference_direction_v1':
        # Reference distances must be efficiency-weighted forward outputs under
        # the separately admitted stable-probe hypothesis, not mean distances.
        if data['reference_definition'] != 'EFFICIENCY_WEIGHTED_DISTANCE':
            raise ValueError('REFERENCE_IS_NOT_EFFICIENCY_WEIGHTED')
        values = [data['observed_change'], data['reference_apo'], data['reference_holo'], *data['direction_checks']]
        if not all(math.isfinite(v) for v in values) or min(data['reference_apo'], data['reference_holo']) <= 0:
            raise ValueError('INVALID_REFERENCE_NUMBERS')
        if not data['direction_checks']:
            raise ValueError('DIRECTION_CHECKS_MISSING')
        sign = lambda v: (v > 0) - (v < 0)
        observed = sign(data['observed_change'])
        expected = -sign(data['reference_holo'] - data['reference_apo'])
        stable = observed != 0 and all(sign(v) == observed for v in data['direction_checks'])
        return {'observed_change': data['observed_change'],
                'reference_distance_change': data['reference_holo']-data['reference_apo'],
                'direction_checks': data['direction_checks'],
                'relation': 'UNRESOLVED_DIRECTION' if not stable or expected == 0 else 'COMPATIBLE' if observed == expected else 'TENSION',
                'limitation': 'Conditional reference-readout direction only; not a calibrated absolute distance or mechanism.'}
    if method == 'fixed_deer_prediction_screen_v1':
        import numpy as np
        from . import q16_shape_flexibility_v1 as deer
        training, target, candidate = data['training_record'], data['target_record'], data['candidate']
        if training['source_key'] != target['source_key']:
            raise ValueError('DIFFERENT_RECORD_FOR_PREDICTION')
        train = np.asarray(training['raw_time_real_imaginary'], float)
        full = np.asarray(target['raw_time_real_imaginary'], float)
        t, y, noise, K = deer.arrays(training)
        deer.arrays(target)  # Shape, finite and ordering checks; target noise not used.
        if len(full) <= len(train) or not np.array_equal(full[:len(train)], train):
            raise ValueError('TRAINING_NOT_EXACT_PREFIX')
        metrics = deer.audit_candidate(candidate, t, y, noise, K)
        tail = full[len(train):]
        if len(tail) < 3:
            raise ValueError('PREDICTION_WINDOW_TOO_SHORT')
        w = np.zeros(len(deer.R))
        for index, value in candidate['grid_weights']:
            w[index] = value
        prediction = np.exp(-candidate['k']*tail[:, 0])*(candidate['unmodulated_amplitude'] + deer.kernel(tail[:, 0]) @ w)
        residual = prediction-tail[:, 1]
        rms = float(np.sqrt(np.mean(residual**2)))
        lag = float(np.corrcoef(residual[:-1], residual[1:])[0, 1]) if np.std(residual) > 0 else 0.
        if not math.isfinite(lag):
            raise ValueError('UNDEFINED_RESIDUAL_CORRELATION')
        return {'training_metrics': metrics, 'prediction': prediction.tolist(),
                'target_support': [float(tail[0, 0]), float(tail[-1, 0]), len(tail)],
                'rms': rms, 'lag1': lag, 'training_noise': noise,
                'relation': 'COMPATIBLE' if rms <= 2*noise and abs(lag) <= .2 else 'TENSION',
                'limitation': 'Fixed-candidate descriptive screen, not a confidence test, family exclusion or population estimate.'}
    raise ValueError('METHOD_NOT_SUPPORTED')


def _input(use, context):
    ref = use['input_ref']
    value = context.get('inputs', {}).get(ref)
    receipt = context.get('admissions', {}).get(ref)
    if value is None or receipt is None:
        return None
    if receipt.get('input_digest') != digest(value) or not receipt.get('source_receipts'):
        raise ValueError('INPUT_NOT_PREVIOUSLY_ADMITTED')
    if value['scope'] != use['scope'] or value['method_id'] != use['method_id']:
        return None
    if not receipt.get('method_basis'):
        return None
    return value


def evaluate_uses(case_graph, context=None):
    uses = case_graph.get('forward_bridge_uses', [])
    if not isinstance(uses, list):
        raise ValueError('BRIDGE_USES_MUST_BE_LIST')
    context = context or {}
    sources = {x['source_id'] for x in case_graph.get('evidence_items', [])}
    results, seen = [], set()
    for use in uses:
        if use.get('contract') != CONTRACT or use.get('requested_use') not in REQUESTS:
            raise ValueError('UNSUPPORTED_BRIDGE_USE_CONTRACT')
        scope = use['scope']
        if set(scope) != SCOPE_FIELDS or any(v is None or v == '' for v in scope.values()):
            raise ValueError('INCOMPLETE_SCIENTIFIC_SCOPE')
        if scope['source_id'] not in sources or use['use_id'] in seen:
            raise ValueError('FOREIGN_SOURCE_OR_DUPLICATE_USE')
        seen.add(use['use_id'])
        identity = digest(use)
        result = dict(runtime_subrule_id=RULE_ID, rule_instance_id=RULE_ID+'::'+identity,
                      use_id=use['use_id'], target_kind='SOURCE_USE', status='UNRESOLVED',
                      requested_use=use['requested_use'], scope=scope, input_ref=use['input_ref'],
                      method_id=use['method_id'], route='SOURCE_LOOKUP', check_completed=False,
                      local_support=None, full_question_answer=False,
                      remaining_obligations=['MODEL_OBSERVATION_USE_EVIDENCE'])
        results.append(result)
        if use['requested_use'] == 'OBSERVATION_DESCRIPTION':
            result.update(status='NOT_APPLICABLE', route='DIRECT_EVALUATION',
                          reason='OBSERVATION_DESCRIPTION_DOES_NOT_REQUIRE_STRUCTURAL_FORWARD_CHECK', remaining_obligations=[])
            continue
        value = _input(use, context)
        if value is None or use['method_id'] not in METHODS:
            result['reason'] = 'SOURCE_SCOPE_METHOD_OR_CALIBRATION_UNAVAILABLE'
            continue
        evidence = context.get('evidence', {}).get(use['use_id'])
        if evidence is None or evidence.get('use_digest') != identity or evidence.get('input_digest') != digest(value):
            result.update(route='REGISTERED_OPERATOR', reason='REQUESTED_USE_NUMERICAL_CHECK_MISSING')
            continue
        expected = numerical_check(use['method_id'], value['data'])
        if evidence.get('numerical') != expected:
            raise ValueError('NUMERICAL_EVIDENCE_NOT_REPRODUCIBLE')
        if 'target_support' in expected and expected['target_support'] != scope['target_support']:
            raise ValueError('TARGET_WINDOW_DIFFERS_FROM_REQUEST')
        relation = expected['relation']
        result.update(route='DIRECT_EVALUATION', check_completed=True, numerical=expected,
                      status='PASS' if relation == 'COMPATIBLE' else 'FAIL' if relation == 'TENSION' else 'UNRESOLVED',
                      local_support=True if relation == 'COMPATIBLE' else False if relation == 'TENSION' else None,
                      reason='REQUESTED_USE_'+relation,
                      remaining_obligations=[] if relation != 'UNRESOLVED_DIRECTION' else ['DIRECTION_RESOLUTION'],
                      allowed_conclusion='Conditional model-observation comparison: '+relation+'. '+expected['limitation'])
        if use['requested_use'] == 'STRUCTURAL_POPULATION':
            result['remaining_obligations'].append('STRUCTURAL_ASSIGNMENT_AND_IDENTIFIABILITY')
        result['claim_ceiling'] = 'This specific model-observation use only; no whole-question or population approval.'
    return results


def run_checks(*, case_graph, runtime_subrules, bindings, contracts, context, enabled=True):
    """Rules select numerical work; reenter the same common evaluator afterward."""
    from copy import deepcopy
    from .rules_prototype_v1 import evaluate_active_rules
    ctx = deepcopy(context)
    def evaluate():
        return evaluate_active_rules(case_graph=case_graph, runtime_subrules=runtime_subrules,
                                     bindings=bindings, contracts=contracts, forward_bridge_context=ctx)
    before = evaluate()
    calls = []
    if enabled:
        by_id = {u['use_id']: u for u in case_graph.get('forward_bridge_uses', [])}
        for result in before:
            if result.get('runtime_subrule_id') != RULE_ID or result.get('route') != 'REGISTERED_OPERATOR':
                continue
            use = by_id[result['use_id']]
            value = _input(use, ctx)
            numeric = numerical_check(use['method_id'], value['data'])
            ctx.setdefault('evidence', {})[use['use_id']] = dict(use_digest=digest(use), input_digest=digest(value), numerical=numeric)
            calls.append(dict(use_id=use['use_id'], method_id=use['method_id'], execution_role='DEVELOPMENT_REPLAY_OF_EXISTING_SCIENTIFIC_COMPONENT'))
    return dict(before=before, after=evaluate() if calls else before, evidence=ctx.get('evidence', {}),
                operator_calls=calls, original_manual_results_reclassified=False)
