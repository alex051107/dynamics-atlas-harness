"""Prospective Rules-controlled continuation of verified unresolved candidates."""
from copy import deepcopy
from . import q09_global_comparison_v1 as a
from . import q09_method_evidence_v1 as m

OPERATOR_ID = 'q09_targeted_source_order_continuation_v1'
POLICY = {'version': OPERATOR_ID, 'IRF_shift': 'padded_linear_v2', 'donor_components': 3,
          'FRET_components': 2, 'sigma_A': 6., 'distance_bounds_A': [10., 120.],
          'seconds_per_fit': 60, 'maxiter': 1500, 'max_fits': 3,
          'stationarity_limit': 1e-6, 'window_and_normalization': 'unchanged_source_native',
          'unique_D0_likelihood': True, 'optimizer': 'existing_scaled_L-BFGS-B'}
NEEDS_CONTINUATION = {'LOWER_FEASIBLE_CANDIDATE_REQUIRES_CONTINUATION',
                      'NO_STATIONARY_CANDIDATE_REQUIRES_CONTINUATION'}


def current_groups(previous):
    """Fold verified descendants without overwriting the historical manual report."""
    report = previous['method_evidence']
    groups = deepcopy(report['source_order_groups'])
    for row in report['group_dispositions']:
        gr = groups[row['reference']]
        if row != m.group_disposition(row['reference'], gr['owners'], gr['candidates']):
            raise ValueError('METHOD_DISPOSITION_NOT_DERIVED_FROM_CANDIDATES')
    history = previous.get('targeted_numerical_history')
    if history is None:
        history = [previous['targeted_numerical_evidence']] if 'targeted_numerical_evidence' in previous else []
    for result in history:
        for run in result['runs']:
            candidates = groups[run['reference']]['candidates']
            parents = [c for c in candidates if c['candidate_id'] == run['parent_candidate_id']]
            if len(parents) != 1:
                raise ValueError('CONTINUATION_PARENT_NOT_CURRENT')
            child = deepcopy(run['checked'])
            if any(c['candidate_id'] == child['candidate_id'] for c in candidates):
                raise ValueError('CONTINUATION_CHILD_ID_REUSED')
            # A worse stationary point must not erase a lower feasible STOP.
            if child['objective'] <= parents[0]['objective']:
                candidates.remove(parents[0])
            candidates.append(child)
    return groups


def request(previous):
    if previous.get('method_evidence_application') != 'VERIFIED_MANUAL_DIAGNOSTICS_CONSUMED':
        raise ValueError('VERIFIED_MANUAL_METHOD_RESULT_REQUIRED')
    report = previous['method_evidence']
    if report['policy'] != m.POLICY or report['provenance'] != m.PROVENANCE:
        raise ValueError('MANUAL_METHOD_CHANGED')
    selected = []
    for ref, gr in current_groups(previous).items():
        row = m.group_disposition(ref, gr['owners'], gr['candidates'])
        if row['status'] in NEEDS_CONTINUATION:
            for candidate in gr['candidates']:
                if candidate['numerical_status'] != 'PASS':
                    selected.append({'reference': ref, 'owners': row['owners'],
                        'parent_candidate_id': candidate['candidate_id'], 'initial': candidate['parameters']})
    if len(selected) > POLICY['max_fits']:
        raise ValueError('TARGETED_BUDGET_EXCEEDED')
    result = {'operator_id': OPERATOR_ID, 'policy': deepcopy(POLICY),
        'input_id': report['input_id'], 'rule_instance_id': previous['rule_instance_id'],
        'base_result_id': a.q.digest(previous), 'selected': selected}
    result['request_id'] = a.q.digest(result)
    return result


def evaluate(previous, evidence=None, verify=None, enabled=True):
    out = deepcopy(previous)
    out['targeted_operator_obligations'] = []
    if not enabled:
        out['targeted_continuation'] = 'DISABLED'; return out
    req = request(previous)
    if not req['selected']:
        out['targeted_continuation'] = 'NO_VERIFIED_NUMERICAL_STOP_SELECTED'; return out
    out['targeted_operator_obligations'] = [req]
    if evidence is None:
        out['targeted_continuation'] = 'CONTINUATION_REQUIRED_BY_NUMERICAL_EVIDENCE'; return out
    try:
        if any(evidence[key] != req[key] for key in ('request_id', 'input_id', 'rule_instance_id', 'base_result_id')) or verify is None:
            raise ValueError('CONTINUATION_EVIDENCE_CONTEXT_CHANGED')
        report = verify(evidence)
        if report['request_id'] != req['request_id'] or a.q.digest(report) != evidence['report_id'] or report['optimizer_calls'] != len(req['selected']):
            raise ValueError('CONTINUATION_REPORT_CHANGED')
        if [r['parent_candidate_id'] for r in report['runs']] != [r['parent_candidate_id'] for r in req['selected']]:
            raise ValueError('CONTINUATION_CANDIDATE_OWNERSHIP_CHANGED')
    except (KeyError, ValueError, TypeError) as error:
        out['targeted_continuation'] = 'EVIDENCE_REJECTED'; out['targeted_rejection'] = str(error); return out
    out['targeted_operator_obligations'] = []
    out['targeted_continuation'] = 'TARGETED_NUMERICAL_CONTINUATION_ASSESSED'
    history = deepcopy(previous.get('targeted_numerical_history',
        [previous['targeted_numerical_evidence']] if 'targeted_numerical_evidence' in previous else []))
    history.append(deepcopy(report))
    out['targeted_numerical_history'] = history
    out['targeted_numerical_evidence'] = deepcopy(report)
    groups = current_groups(out)
    replacements = {ref: m.group_disposition(ref, gr['owners'], gr['candidates'])
                    for ref, gr in groups.items()}
    out['method_obligations'] = [dict(replacements[row['reference']], kind='DONOR_GROUP_NEXT_ACTION')
        if row.get('reference') in replacements and row['kind'] == 'DONOR_GROUP_NEXT_ACTION' else row
        for row in previous['method_obligations']]
    out['complete_question_answer'] = False
    return out


def dispatch(before, previous, operator):
    obligations = before['targeted_operator_obligations']
    if not obligations:
        return []
    if before != evaluate(previous):
        raise ValueError('TARGETED_DISPATCH_NOT_CURRENT_RULE_OUTPUT')
    return [operator(obligation) for obligation in obligations]
