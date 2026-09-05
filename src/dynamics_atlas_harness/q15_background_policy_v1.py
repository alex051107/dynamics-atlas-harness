"""A finite method-discrepancy check, not a protein-state decision rule."""
import hashlib
import json

import numpy as np

from . import q15_apbs_comparison_v1 as main_method

RULE_ID = 'Q15R01_BACKGROUND_HANDLING_SENSITIVITY_V1'
OPERATOR_ID = 'q15_background_handling_sensitivity_v1'
ALTERNATIVES = ('LITERAL_ALEX_SUITE_49DFEF', 'CHANNELWISE_NONNEGATIVE')


def corrected_alternative(counts, duration_s, alternative, policy=main_method.POLICY):
    """Keep the historical assignment order, including its channel indices."""
    if alternative not in ALTERNATIVES:
        raise ValueError('UNKNOWN_BACKGROUND_ALTERNATIVE')
    baseline = main_method.correct(counts, duration_s, policy)
    dd, da, aa = baseline['corrected_counts_DD_DA_AA'].T.copy()
    if alternative == ALTERNATIVES[0]:
        da[da < 0] = 0
        dd[da < 0] = 0  # Literal source: already-cleared DA mask.
        da[aa < 0] = 0  # Literal source modifies DA, leaving AA unchanged.
    else:
        dd = np.maximum(dd, 0)
        da = np.maximum(da, 0)
        aa = np.maximum(aa, 0)
    f = da - policy['alpha'] * dd - policy['delta'] * aa
    donor = policy['gamma'] * dd + f
    total = donor + aa / policy['beta']
    with np.errstate(divide='ignore', invalid='ignore'):
        e, s = f / donor, donor / total
    lo, hi = policy['stoichiometry_open_interval']
    selected = (baseline['eligible'] & (donor > 0) & (total > 0)
                & np.isfinite(e) & np.isfinite(s) & (s > lo) & (s < hi))
    return {'E': e, 'S': s, 'selected': selected,
            'corrected_counts_DD_DA_AA': np.column_stack((dd, da, aa))}


def direction_signature(comparison):
    lo, hi = comparison['all_cross_repetition_difference_range']
    delta = comparison['holo_minus_apo_E']
    if not all(np.isfinite(v) for v in [lo, hi, delta]) or lo > hi:
        raise ValueError('INVALID_DIRECTION_VALUES')
    return {'mean_direction': 'INCREASE' if delta > 0 else 'DECREASE' if delta < 0 else 'ZERO',
            'all_cross_repetition_direction': 'INCREASE' if lo > 0 else 'DECREASE' if hi < 0 else 'NOT_UNIFORM'}


def evaluate(main_report, source_facts, evidence=None):
    binding = {'rule_id': RULE_ID, 'input_id': main_report['input_id'],
               'source_facts': source_facts}
    instance = hashlib.sha256(json.dumps(binding, sort_keys=True).encode()).hexdigest()
    negative = sum(f['eligible_negative_corrected_count_events'] for f in main_report['files'])
    triggered = negative > 0 and source_facts.get('clipping_discrepancy_verified') is True
    result = {'rule_id': RULE_ID, 'rule_instance_id': instance,
              'input_id': main_report['input_id'], 'development_adapter': True,
              'trigger': {'eligible_negative_count_events': negative,
                          'clipping_discrepancy_verified': source_facts.get('clipping_discrepancy_verified')},
              'status': 'UNRESOLVED' if triggered else 'NOT_APPLICABLE',
              'operator_obligations': [OPERATOR_ID] if triggered else [],
              'method_disposition': 'AWAITING_FINITE_METHOD_COMPARISON' if triggered else 'NO_TRIGGER',
              'scientific_question_status': 'INCOMPLETE',
              'claim_ceiling': 'Finite background-handling alternatives only; no absolute distance, dye safety, protein closure or full Q15 answer'}
    if evidence is None:
        return result
    if not triggered:
        raise ValueError('EVIDENCE_WITHOUT_TRIGGER')
    if (evidence.get('input_id') != result['input_id']
            or evidence.get('rule_instance_id') != instance
            or set(evidence.get('alternatives', {})) != set(ALTERNATIVES)):
        raise ValueError('EVIDENCE_BINDING_OR_ALTERNATIVES')
    changes = []
    reference = main_report['condition_comparisons']
    for name, alternative in evidence['alternatives'].items():
        actual = alternative['condition_comparisons']
        if set(actual) != set(reference):
            raise ValueError('EVIDENCE_PAIR_COVERAGE')
        for pair, baseline in reference.items():
            if direction_signature(actual[pair]) != direction_signature(baseline):
                changes.append({'alternative': name, 'pair': pair,
                                'before': direction_signature(baseline),
                                'after': direction_signature(actual[pair])})
    result.update(operator_obligations=[], direction_changes=changes,
                  method_disposition='DIRECTION_DEPENDS_ON_BACKGROUND_HANDLING' if changes else 'DIRECTION_STABLE_FOR_TWO_CHECKED_ALTERNATIVES')
    # A completed sensitivity test does not settle the unknown author executable.
    result['status'] = 'UNRESOLVED'
    return result


def dispatch(main_report, source_facts, operator, enabled=True):
    before = evaluate(main_report, source_facts)
    if not enabled or not before['operator_obligations']:
        return {'before': before, 'after': before, 'operator_calls': 0, 'evidence_result': None}
    evidence = operator(before)
    after = evaluate(main_report, source_facts, evidence)
    return {'before': before, 'after': after, 'operator_calls': 1, 'evidence_result': evidence}
