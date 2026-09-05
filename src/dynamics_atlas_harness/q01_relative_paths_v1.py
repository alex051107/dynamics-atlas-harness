"""Evidence-triggered relative-reference comparison after envelope noncoverage.

Relative preference is explicitly different from membership in an NMR envelope.
This is an exposed method revision, never a retrospective held-out success.
"""
import numpy as np
from . import q01_path_comparison_v1 as q

OPERATOR_ID = 'q01_relative_reference_paths_v1'
POLICY = {'version': 'q01-relative-reference/v1', 'primary_persistence_frames': 20,
          'sensitivity_frames': [5, 50], 'geometry_margin': 'closed_RMSD_minus_open_RMSD_A',
          'contact_margin': 'negative_mean((score-mid_reference_score)/(closed_reference_mean-open_reference_mean))',
          'joint_preference': 'geometry and both-channel contact projection agree in sign; else conflict',
          'state_membership_claimed': False, 'time_axis_ns': [20, 1020, 1],
          'author_trajectory_labels_used': False,
          'claim_ceiling': 'Relative-reference finite-time direction in deposited seeds, not state entry, rates, equilibrium or activity'}


def reference_policy(reference_distances, contacts):
    output = {'policy': POLICY, 'normalization': {}, 'reference_preference': {}}
    for method in q.METHODS:
        matrix = {state: np.column_stack([q.scores(reference_distances[state], contacts, method)[s] for s in q.STATES]) for state in q.STATES}
        means = {state: matrix[state].mean(axis=0) for state in q.STATES}
        delta = means['closed']-means['open']; mid = (means['closed']+means['open'])/2
        if np.any(abs(delta) < 1e-8):
            raise ValueError('REFERENCE_SCORE_NOT_DISCRIMINATING')
        output['normalization'][method] = {'mid': mid.tolist(), 'delta': delta.tolist(),
                                           'open_mean': means['open'].tolist(), 'closed_mean': means['closed'].tolist()}
        output['reference_preference'][method] = {s: (-np.mean((matrix[s]-mid)/delta, axis=1)).tolist() for s in q.STATES}
    return output


def preference(geometry, scores, normalization):
    g = np.asarray(geometry['closed'])-np.asarray(geometry['open'])
    x = np.column_stack([scores[s] for s in q.STATES])
    c = -np.mean((x-np.array(normalization['mid']))/np.array(normalization['delta']), axis=1)
    if not np.all(np.isfinite(g)) or not np.all(np.isfinite(c)):
        raise ValueError('NONFINITE_PREFERENCE')
    labels = np.where((g > 1e-10) & (c > 1e-10), 'open',
                      np.where((g < -1e-10) & (c < -1e-10), 'closed', 'conflict'))
    return labels, g, c


def path(labels, seed, n):
    other = 'closed' if seed == 'open' else 'open'
    initial = str(labels[0])
    events = [(a, b) for a, b in q.runs(labels == other) if b-a >= n]
    departures = [(a, b) for a, b in q.runs(labels != seed) if b-a >= n]
    if initial != seed:
        category = 'INITIAL_PREFERENCE_NOT_SEED_ALIGNED'
    elif events:
        category = 'SUSTAINED_OPPOSITE_REFERENCE_PREFERENCE'
    elif departures:
        category = 'SUSTAINED_LOSS_OF_SEED_PREFERENCE_WITHOUT_OPPOSITE_AGREEMENT'
    else:
        category = 'NO_SUSTAINED_LOSS_OF_SEED_PREFERENCE'
    return {'category': category, 'initial_preference': initial, 'persistence_frames': n,
            'sampled_span_ns': n-1,
            'first_opposite_interval_ns': [20+events[0][0], 20+events[0][1]-1] if events else None,
            'opposite_intervals': len(events),
            'counts': {s: int(np.sum(labels == s)) for s in (*q.STATES, 'conflict')},
            'longest_seed_frames': max([b-a for a, b in q.runs(labels == seed)] or [0]),
            'longest_opposite_frames': max([b-a for a, b in q.runs(labels == other)] or [0]),
            'state_transition_claimed': False}


def compare(records, contacts, policy):
    result = {'rows': [], 'grouped': {}, 'method_changes': [], 'full_question_answer': False,
              'claim_ceiling': POLICY['claim_ceiling']}; frames = {}
    for name, r in records.items():
        if not np.array_equal(r['time_ns'], np.arange(20, 1021)):
            raise ValueError('NONCANONICAL_TIME_AXIS')
        local = {}
        for method in q.METHODS:
            labels, gm, cm = preference(r['geometry_A'], q.scores(r['distances_A'], contacts, method), policy['normalization'][method])
            local[method] = {str(n): path(labels, r['seed'], n) for n in (20, 5, 50)}
            frames[(name, method)] = {'labels': labels, 'geometry_margin_A': gm, 'contact_margin': cm}
            result['rows'].append({'trajectory': name, 'seed_group': r['seed'], 'method': method,
                                   'paths': local[method], 'geometry_margin_initial_A': float(gm[0]),
                                   'geometry_margin_final_A': float(gm[-1]),
                                   'geometry_margin_range_A': [float(gm.min()), float(gm.max())]})
        result['method_changes'].append({'trajectory': name, 'seed_group': r['seed'],
            'frame_preference_changes': int(np.sum(frames[(name, q.METHODS[0])]['labels'] != frames[(name, q.METHODS[1])]['labels'])),
            'category_changes': {str(n): local[q.METHODS[0]][str(n)]['category'] != local[q.METHODS[1]][str(n)]['category'] for n in (20, 5, 50)}})
    for method in q.METHODS:
        result['grouped'][method] = {}
        for seed in q.STATES:
            rows = [r for r in result['rows'] if r['method'] == method and r['seed_group'] == seed]
            result['grouped'][method][seed] = {str(n): {category: sum(r['paths'][str(n)]['category'] == category for r in rows)
                for category in sorted({r['paths'][str(n)]['category'] for r in rows})} for n in (20, 5, 50)}
    result['trajectory_count'] = len(records)
    return result, frames


def evaluate(base_instance, facts, envelope_evidence, policy, evidence=None, verify=None, enabled=True):
    if base_instance['facts_id'] != q.identity(facts) or base_instance['rule_id'] != q.RULE_ID:
        raise ValueError('BASE_INSTANCE_BINDING')
    if base_instance['status'] != 'COMPARISON_EXECUTED' or base_instance['numeric_result'] != envelope_evidence:
        raise ValueError('VALIDATED_ENVELOPE_EVIDENCE_REQUIRED')
    result = {k: base_instance[k] for k in ('instance_id', 'facts_id', 'rule_id')}
    result.update(status='DISABLED' if not enabled else 'PENDING', operator_requests=[],
                  state_membership_claimed=False, accuracy_gain_claimed=False)
    if not enabled:
        return result
    paths = envelope_evidence.get('paths', [])
    if not paths or any(p['persistence_results']['20']['initial_support'] in q.STATES for p in paths):
        result['status'] = 'FOLLOWUP_NOT_TRIGGERED'; return result
    request = {'operator_id': OPERATOR_ID, 'instance_id': result['instance_id'], 'facts_id': result['facts_id'],
               'input_id': facts['input_id'], 'parent_method_id': facts['method_id'], 'method_id': q.identity(policy)}
    result['reason'] = 'Validated construction envelopes classify no initial trajectory frame; relative directional claim requires a different estimand.'
    if evidence is not None:
        try:
            if any(evidence.get(k) != v for k, v in request.items()) or verify is None:
                raise ValueError('RELATIVE_EVIDENCE_BINDING_OR_REPLAY')
            report = verify(evidence)
            if report['trajectory_count'] != 40:
                raise ValueError('FULL40_REQUIRED')
            changed = sum(r['category_changes']['20'] for r in report['method_changes'])
            result.update(status='RELATIVE_COMPARISON_EXECUTED', numeric_result=report,
                          scientific_status='RELATIVE_DIRECTION_METHOD_DEPENDENT' if changed else 'RELATIVE_DIRECTION_STABLE_ACROSS_TWO_METHODS',
                          changed_primary_trajectories=changed,
                          original_envelope_gap='PRESERVED_NOT_SOLVED_BY_RELATIVE_PREFERENCE')
            return result
        except (ValueError, KeyError, TypeError) as exc:
            result['evidence_error'] = str(exc)
    result['operator_requests'] = [request]
    return result


def dispatch(instance, operator):
    outputs = []
    for request in instance['operator_requests']:
        if request['operator_id'] != OPERATOR_ID or request['instance_id'] != instance['instance_id']:
            raise ValueError('UNKNOWN_OR_UNBOUND_FOLLOWUP')
        outputs.append(operator(request))
    return outputs
