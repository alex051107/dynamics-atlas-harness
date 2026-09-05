"""Consume verified manual method diagnostics without retroactive operator credit."""
from copy import deepcopy
import numpy as np
from . import q09_global_comparison_v1 as a
from .q09_cached_group_v2 import CachedGroup

PROVENANCE = 'MANUAL_DIAGNOSTICS_VERIFIED_WITHOUT_REFITTING'
POLICY = {'version': 'q09-method-evidence/v1', 'IRF_shift': 'padded_linear_v2',
          'objective_atol': 1e-11, 'objective_rtol': 1e-8,
          'gradient_replay_atol': 1e-8, 'gradient_replay_rtol': .001,
          'stationarity_limit': 1e-6, 'protein_state_number': 'UNRESOLVED'}
RESPONSE_METHOD = {'version': '60-119-response-diagnostic/v1', 'IRF_shift': 'padded_linear_v2', 'window': 'unchangedIBH17HanningLin>0.1medianpositive', 'dt_ns': 0.0141, 'donor_components': 2, 'FRET_components': 2, 'sigma_A': 6.0, 'scatter': 0.0, 'max_fits': 10, 'seconds_per_fit': 60, 'maxiter': 1500, 'gradient_limit': 1e-06, 'shared_reference_applicability': 'UNKNOWN', 'role': 'MANUAL_METHOD_DIAGNOSTIC_NOT_RULES_GAIN', 'fit_regions_ns': [0, 5, 10, 20, 40, 60]}
SOURCE_ORDER_METHOD = {'version': 'q09-source-donor-groups/v2', 'IRF_shift': 'padded_linear_v2', 'source_orders': 'SI21Table2a componentpresence only', 'models': ['donor2_FRET2_fixed_reference', 'donor3_FRET2_conditional'], 'unique_D0_likelihood': True, 'seconds_per_fit': 30, 'fits_per_changed_group': 2, 'max_fits': 26, 'maxiter': 1500, 'gradient_tolerance': 1e-06, 'new_donor_seed': [0.2, 1.5, 4.0, 0.2, 0.5], 'author_fitted_values_used': False, 'protein_state_number': 'NOT_INFERRED'}
SINGLE_BOUNDS = [(.05, 10.)]*2+[(0., 1.), (1e-12, .05), (-5., 5.)]


def check_candidate(run, bounds, objective):
    p = np.asarray(run['parameters'], dtype=float)
    low, high = np.asarray(bounds).T
    if p.shape != low.shape or not np.isfinite(p).all() or np.any(p < low) or np.any(p > high):
        raise ValueError('METHOD_CANDIDATE_BOUNDS')
    actual = float(objective(p))
    if not np.isfinite(actual) or not np.isclose(actual, run['objective'], atol=POLICY['objective_atol'], rtol=POLICY['objective_rtol']):
        raise ValueError('METHOD_OBJECTIVE_REPLAY_MISMATCH')
    gradient = float(np.max(np.abs(a.q.gradient_at(p, bounds, objective))))
    if not np.isclose(gradient, run['projected_gradient_inf'], atol=POLICY['gradient_replay_atol'], rtol=POLICY['gradient_replay_rtol']):
        raise ValueError('METHOD_GRADIENT_REPLAY_MISMATCH')
    status = run['numerical_status']
    if status not in ('PASS', 'NUMERICAL_STOP_WITH_FEASIBLE_POINT'):
        raise ValueError('METHOD_UNKNOWN_NUMERICAL_STATUS')
    if status == 'PASS' and (run.get('optimizer_success') is not True or gradient > POLICY['stationarity_limit']):
        raise ValueError('METHOD_FALSE_STATIONARITY_PASS')
    return {'objective': actual, 'projected_gradient_inf': gradient,
            'objective_difference': actual-run['objective'], 'numerical_status': status,
            'parameters': p.tolist(), 'candidate_id': a.q.digest(run)}


def group_disposition(reference, owners, checked):
    best = min(checked, key=lambda x: x['objective'])
    passed = [r for r in checked if r['numerical_status'] == 'PASS']
    if best['numerical_status'] != 'PASS':
        status = 'LOWER_FEASIBLE_CANDIDATE_REQUIRES_CONTINUATION' if passed else 'NO_STATIONARY_CANDIDATE_REQUIRES_CONTINUATION'
        action = 'Continue the recorded feasible point under the declared padded donor-order model; retain every stop and candidate.'
    else:
        status = 'CONDITIONAL_NUMERICAL_CANDIDATE_AVAILABLE'
        action = 'Use the verified source-order candidate for conditional method comparison; assess absolute fit and transfer before structural/population inference.'
    return {'reference': reference, 'owners': owners, 'status': status,
            'candidate_count': len(checked), 'stationary_candidates': len(passed),
            'best_candidate_id': best['candidate_id'], 'best_objective': best['objective'],
            'next_action': action, 'donor_order': 3, 'FRET_components': 2,
            'absolute_adequacy': 'NOT_ESTABLISHED', 'author_joint_configuration': 'UNKNOWN',
            'structure_or_population_claim_permitted': False}


def verify_diagnostics(data, response, response_input, orders, source_orders, old_global):
    """One fixed-parameter pass over 10+26 historical candidates, zero optimizers."""
    if response['method'] != RESPONSE_METHOD or orders['method'] != SOURCE_ORDER_METHOD:
        raise ValueError('MANUAL_IRF_METHOD_CHANGED')
    if response['method']['donor_components'] != 2 or response['method']['FRET_components'] != 2 or response['method']['sigma_A'] != 6. or response['method']['scatter'] != 0.:
        raise ValueError('RESPONSE_MODEL_CHANGED')
    if orders['method']['models'] != ['donor2_FRET2_fixed_reference', 'donor3_FRET2_conditional'] or orders['method']['unique_D0_likelihood'] is not True:
        raise ValueError('SOURCE_ORDER_MODEL_CHANGED')
    if response_input['source_input_id'] != data.input_id or response['input_id'] != a.q.digest(response_input) or response_input['method'] != response['method']:
        raise ValueError('RESPONSE_INPUT_BINDING')
    if orders['source_input_id'] != data.input_id or orders['source_orders'] != source_orders or orders['request_id'] != a.q.digest({'source': data.input_id, 'method': orders['method'], 'source_orders': source_orders}):
        raise ValueError('SOURCE_ORDER_INPUT_BINDING')
    selected = {row['reference']: row for row in source_orders['groups'] if row['mismatch_variants']}
    if set(orders['groups']) != set(selected) or orders['fits'] != 26 or response['new_fits'] != 10:
        raise ValueError('INCOMPLETE_DECLARED_MANUAL_BATCH')
    checked_groups = {}; dispositions = []
    for ref, row in orders['groups'].items():
        original = next(g for g in data.groups if g.ref == ref)
        if row['reference'] != ref or row['owners'] != original.owners or row['source'] != selected[ref] or original.donors != 2:
            raise ValueError('MANUAL_GROUP_ROLE_CHANGED')
        gr = CachedGroup(ref, original.owners, original.records, 3)
        gr2 = CachedGroup(ref, original.owners, original.records, 2)
        p = row['old_donor2_parameters']
        if p != old_global['local_runs'][ref]['parameters'] or len(row['runs']) != 2:
            raise ValueError('HISTORICAL_REFERENCE_PARAMETERS_CHANGED')
        embedded = [p[0], p[1], (p[0]+p[1])/2, p[2], 1., p[3], p[4]]+p[5:]
        seeds = [embedded, [.2, 1.5, 4., .2, .5]+p[3:5]+p[5:]]
        pred2 = gr2.predict(p, 'local2'); pred3 = gr.predict(embedded, 'local2')
        parity = {role: float(np.max(abs(pred2[role]-pred3[role]))/np.max(pred2[role])) for role in pred2}
        if max(parity.values()) > 1e-12:
            raise ValueError('SOURCE_ORDER_EMBEDDING_CHANGED')
        actual = gr2.deviance(p, 'local2')
        if not np.isclose(actual, row['old_donor2_padded_deviance'], atol=1e-6, rtol=1e-8):
            raise ValueError('OLD_PADDED_METHOD_MISMATCH')
        checks = []
        for run, seed in zip(row['runs'], seeds):
            if run['initial'] != seed:
                raise ValueError('SOURCE_ORDER_START_CHANGED')
            checks.append(check_candidate(run, gr.bounds('local2'), lambda x: gr.deviance(x, 'local2')/gr.total))
        checked_groups[ref] = {'owners': gr.owners, 'candidates': checks,
                               'embedding_max_relative_delta': parity, 'old_donor2_deviance': actual,
                               'best_donor3_deviance': min(r['objective'] for r in checks)*gr.total}
        dispositions.append(group_disposition(ref, gr.owners, checks))
    original = next(g for g in data.groups if g.owners == ['60-119'])
    gr = CachedGroup(original.ref, original.owners, original.records, 2)
    if response_input['reference'] != gr.ref or response_input['roles'] != list(gr.records) or set(response['single_runs']) != set(gr.records):
        raise ValueError('RESPONSE_ROLES_CHANGED')
    def single(role, p):
        r = gr.records[role]
        counts = gr.observed(role, p[:2], [p[2], 1-p[2]], [], [], 1., p[3], p[4])
        return a.poisson_deviance(r['y'][r['mask']], counts[r['mask']])
    singles = {}
    for role, runs in response['single_runs'].items():
        if len(runs) != 2:
            raise ValueError('RESPONSE_SINGLE_STARTS_MISSING')
        total = float(gr.records[role]['y'][gr.records[role]['mask']].sum())
        singles[role] = [check_candidate(r, SINGLE_BOUNDS, lambda p: single(role, p)/total) for r in runs]
    if len(response['shared_null_runs']) != 2 or len(response['FRET2_runs']) != 4:
        raise ValueError('RESPONSE_SHARED_STARTS_MISSING')
    nulls = [check_candidate(r, SINGLE_BOUNDS+SINGLE_BOUNDS[-2:],
             lambda p: (single(gr.ref, p[:5])+single('60-119', list(p[:3])+list(p[5:7])))/gr.total)
             for r in response['shared_null_runs']]
    frets = [check_candidate(r, gr.bounds('local2'), lambda p: gr.deviance(p, 'local2')/gr.total) for r in response['FRET2_runs']]
    best_single = {role: min(rows, key=lambda r: r['objective']) for role, rows in singles.items()}
    latent_means = {}
    for role, record in best_single.items():
        p = record['parameters']; tau = np.array(p[:2]); amp = np.array([p[2], 1-p[2]])
        latent_means[role] = float(np.sum(amp*tau*tau)/np.sum(amp*tau))
    response_report = {'reference': gr.ref, 'owners': gr.owners, 'single_candidates': singles,
        'shared_null_candidates': nulls, 'FRET2_candidates': frets,
        'separate_deviance': sum(r['objective']*float(gr.records[role]['y'][gr.records[role]['mask']].sum()) for role, r in best_single.items()),
        'shared_null_deviance': min(r['objective'] for r in nulls)*gr.total,
        'FRET2_deviance': min(r['objective'] for r in frets)*gr.total,
        'conditional_latent_means_ns': latent_means,
        'latent_mean_difference_DA_minus_D0_ns': latent_means['60-119']-latent_means[gr.ref]}
    response_report['status'] = ('COMMON_RESPONSE_TRANSFER_REQUIRES_CALIBRATION'
        if response_report['latent_mean_difference_DA_minus_D0_ns'] > 0 else 'COMMON_RESPONSE_ADEQUACY_STILL_UNESTABLISHED')
    response_report['next_action'] = 'Check independent response/IRF applicability before further similar FRET starts; independent effective DA decay is not an established donor model.'
    assessed = {v for row in dispositions for v in row['owners']} | {'60-119'}
    return {'policy': deepcopy(POLICY), 'provenance': PROVENANCE, 'input_id': data.input_id,
        'historical_diagnostic_id': a.q.digest({'response': response, 'response_input': response_input, 'orders': orders}),
        'candidate_count': 36, 'optimizer_calls': 0, 'new_rules_extra_calculations': 0,
        'source_order_groups': checked_groups, 'group_dispositions': dispositions,
        'response_transfer': response_report,
        'unassessed_variants': sorted(set(data.audit['variants'])-assessed),
        'unassessed_reason': 'No manual diagnostic in this evidence batch; preserve existing obligations.',
        'complete_question_answer': False, 'absolute_adequacy_established': False}


def consume(previous, input_id, evidence=None, verify=None, enabled=True):
    """Same-instance method update; prior numeric and structure evidence is retained."""
    result = deepcopy(previous)
    if not enabled:
        result['method_evidence_application'] = 'DISABLED'; return result
    if not previous['rule_instance_id'].startswith(a.RULE_ID+'::CASE::') or 'comparison' not in previous or 'request_id' not in previous:
        raise ValueError('VERIFIED_Q09_COMPARISON_REQUIRED')
    obligation = {'kind': 'METHOD_EVIDENCE_ADMISSION', 'rule_instance_id': previous['rule_instance_id'],
                  'input_id': input_id, 'base_result_id': a.q.digest(previous),
                  'purpose': 'Verify and consume existing donor-order and response diagnostics; no refitting.'}
    result['method_obligations'] = [obligation]
    if evidence is None:
        result['method_evidence_application'] = 'EXISTING_DIAGNOSTIC_VERIFICATION_REQUIRED'; return result
    try:
        if evidence['input_id'] != input_id or evidence['base_result_id'] != obligation['base_result_id'] or evidence['rule_instance_id'] != previous['rule_instance_id']:
            raise ValueError('METHOD_EVIDENCE_CONTEXT_CHANGED')
        if verify is None:
            raise ValueError('NUMERICAL_METHOD_VERIFIER_REQUIRED')
        report = verify(evidence)
        if report['input_id'] != input_id or report['policy'] != POLICY or report['provenance'] != PROVENANCE or a.q.digest(report) != evidence['report_id']:
            raise ValueError('METHOD_REPORT_BINDING_OR_PROVENANCE_CHANGED')
        if report['optimizer_calls'] != 0 or report['new_rules_extra_calculations'] != 0 or report['complete_question_answer']:
            raise ValueError('RETROACTIVE_GAIN_OR_SCIENCE_UPGRADE')
    except (ValueError, KeyError, TypeError) as error:
        result['method_evidence_application'] = 'REJECTED'; result['method_evidence_rejection'] = str(error); return result
    result['method_evidence_application'] = 'VERIFIED_MANUAL_DIAGNOSTICS_CONSUMED'
    result['method_evidence'] = report
    result['method_obligations'] = [dict(row, kind='DONOR_GROUP_NEXT_ACTION') for row in report['group_dispositions']]
    result['method_obligations'].append({'kind': 'RESPONSE_TRANSFER_CALIBRATION', **report['response_transfer']})
    result['reason_codes'] = [code for code in previous['reason_codes'] if code != 'DONOR_AND_INSTRUMENT_ADEQUACY_NOT_ESTABLISHED']
    result['reason_codes'] += ['DONOR_AND_INSTRUMENT_ADEQUACY_PARTITIONED_BY_VERIFIED_DIAGNOSTICS',
                              'ABSOLUTE_ADEQUACY_AND_AUTHOR_CONFIGURATION_UNESTABLISHED']
    result['complete_question_answer'] = False
    return result
