"""Absolute structural paths and decomposed evidence for the original Q01 claim.

The original relative labels remain intact. MD references are development data,
and contact disagreement is an interpretive limit rather than a new classifier.
"""
import numpy as np
from . import q01_path_comparison_v1 as q
from . import q01_relative_paths_v1 as relative

OPERATOR_ID = 'q01_absolute_paths_and_development_MD_reference_v1'
POLICY = {'version': 'q01-absolute-paths/v1', 'baseline_samples': 20, 'terminal_samples': 20,
          'event_comparison_samples': 20, 'persistence_samples': [20, 5, 50],
          'MD_reference_samples_ns': list(range(20, 1021, 100)),
          'MD_reference_source': 'open-seeded trajectories, leave whole query trajectory out',
          'MD_reference_quantiles': [.05, .25, .5, .75, .95],
          'MD_quantile_role': 'descriptive geometry scale, not a calibrated state boundary',
          'group_unit': 'trajectory', 'bootstrap_replicates': 2000, 'bootstrap_seed': 4215,
          'bootstrap_scope': 'conditional resampling of the twenty source seed runs per group; not biological replication or force-field uncertainty',
          'new_state_classifier': False, 'author_trajectory_labels_used': False}


def quantiles(values):
    a = np.asarray(values, float)
    return dict(zip(('q05', 'q25', 'median', 'q75', 'q95'), map(float, np.quantile(a, [.05, .25, .5, .75, .95]))))


def window_change(values, before, after):
    a, b = np.asarray(values)[before], np.asarray(values)[after]
    if len(a) == 0 or len(b) == 0:
        return {'before_samples': len(a), 'after_samples': len(b), 'delta': None}
    return {'before_samples': len(a), 'after_samples': len(b),
            'before_median': float(np.median(a)), 'after_median': float(np.median(b)),
            'delta': float(np.median(b)-np.median(a))}


def describe(records, contacts, relative_policy, displacement, md_distance):
    if relative_policy['policy'] != relative.POLICY:
        raise ValueError('RELATIVE_POLICY_MISMATCH')
    relative_report, relative_frames = relative.compare(records, contacts, relative_policy)
    rows = []; full = {}
    open_loo = np.concatenate([md_distance[n] for n, rec in records.items() if rec['seed'] == 'open'])
    md_scale = quantiles(open_loo)
    for name, record in records.items():
        seed = record['seed']; other = 'closed' if seed == 'open' else 'open'
        common = {'open_reference_lid_rmsd_A': record['geometry_A']['open'],
                  'closed_reference_lid_rmsd_A': record['geometry_A']['closed'],
                  'lid_displacement_from_20ns_A': displacement[name],
                  'nearest_open_MD_lid_rmsd_A': md_distance[name]}
        metric = {key: {'initial': float(v[0]), 'final': float(v[-1]),
                       'initial_to_final_delta': float(v[-1]-v[0]),
                       'distribution': quantiles(v),
                       'first20_to_last20': window_change(v, slice(0, 20), slice(-20, None))}
                  for key, v in common.items()}
        method_rows = {}
        for method in q.METHODS:
            score = q.scores(record['distances_A'], contacts, method)
            norm = relative_policy['normalization'][method]
            z = -(np.column_stack([score[s] for s in q.STATES])-norm['mid'])/norm['delta']
            split = (z[:, 0]*z[:, 1] < -1e-20)
            labels = relative_frames[(name, method)]['labels']
            arrays = dict(common, open_contact_A=score['open'], closed_contact_A=score['closed'],
                          open_contact_normalized_direction=z[:, 0], closed_contact_normalized_direction=z[:, 1])
            events = {}
            for n in POLICY['persistence_samples']:
                intervals = [(a, b) for a, b in q.runs(labels == other) if b-a >= n]
                entries = []
                for a, b in intervals:
                    pre, event = slice(max(0, a-20), a), slice(a, min(a+20, b))
                    later_seed = [(u, v) for u, v in q.runs(labels[b:] == seed) if v-u >= n]
                    entries.append({'start_ns': 20+a, 'end_ns': 20+b-1, 'sample_count': b-a,
                        'sampled_span_ns': b-a-1,
                        'event_contact_internal_disagreement_frames': int(np.sum(split[a:b])),
                        'first_subsequent_seed_preference_ns': 20+b+later_seed[0][0] if later_seed else None,
                        'pre20_to_first20_event': {key: window_change(v, pre, event) for key, v in arrays.items()},
                        'event_range': {key: [float(np.min(v[a:b])), float(np.max(v[a:b]))] for key, v in arrays.items()}})
                events[str(n)] = entries
            primary = events['20']
            method_rows[method] = {'unchanged_relative_path': relative.path(labels, seed, 20),
                'last_relative_preference': str(labels[-1]),
                'contact_changes_first20_to_last20': {s: window_change(score[s], slice(0, 20), slice(-20, None)) for s in q.STATES},
                'contact_internal_disagreement_frames': int(np.sum(split)),
                'opposite_preference_frames_with_internal_contact_disagreement': int(np.sum(split & (labels == other))),
                'events_by_persistence': events,
                'interpretation': ('RELATIVE_EVENT_WITH_INTERNAL_CONTACT_DISAGREEMENT; do not claim all structural channels support one state'
                    if any(e['event_contact_internal_disagreement_frames'] for e in primary)
                    else 'NO_INTERNAL_CONTACT_DISAGREEMENT_IN_PRIMARY_EVENTS; not independent structural validation'),
                'open_specific_contact_direction_positive_frames': int(np.sum(z[:, 0] > 1e-10)),
                'closed_specific_contact_direction_negative_frames': int(np.sum(z[:, 1] < -1e-10))}
            full[(name, method)] = dict(arrays, internal_contact_disagreement=split,
                                       relative_preference=labels)
        rows.append({'trajectory': name, 'seed_group': seed, 'absolute_metrics': metric,
                     'methods': method_rows,
                     'fraction_within_open_LOO_geometry_q95': float(np.mean(md_distance[name] <= md_scale['q95'])),
                     'MD_reference_scale_is_state_boundary': False})
    grouped = {}
    for seed in q.STATES:
        group = [row for row in rows if row['seed_group'] == seed]
        grouped[seed] = {'trajectory_count': len(group), 'trajectory_level': {
            metric: quantiles([row['absolute_metrics'][metric]['first20_to_last20']['after_median'] for row in group])
            for metric in common},
            'first20_to_last20_delta': {metric: quantiles([row['absolute_metrics'][metric]['first20_to_last20']['delta'] for row in group]) for metric in common},
            'trajectories_with_both_reference_distances_increasing_first20_to_last20': [row['trajectory'] for row in group
                if all(row['absolute_metrics'][s+'_reference_lid_rmsd_A']['first20_to_last20']['delta'] > 0 for s in q.STATES)]}
    rng = np.random.default_rng(POLICY['bootstrap_seed'])
    samples = {seed: np.array([row['absolute_metrics']['lid_displacement_from_20ns_A']['first20_to_last20']['after_median']
                              for row in rows if row['seed_group'] == seed]) for seed in q.STATES}
    medians = {seed: np.median(rng.choice(v, (POLICY['bootstrap_replicates'], len(v)), replace=True), axis=1)
               for seed, v in samples.items()}
    uncertainty = {'metric': 'closed minus open median terminal lid displacement from analysis start',
        'observed_A': float(np.median(samples['closed'])-np.median(samples['open'])),
        'conditional_bootstrap_percentile_95_A': np.quantile(medians['closed']-medians['open'], [.025, .975]).tolist(),
        'scope': POLICY['bootstrap_scope'], 'zero_observed_events_implies_zero_population_probability': False}
    return {'trajectory_count': len(rows), 'rows': rows, 'grouped': grouped,
            'open_MD_leave_whole_trajectory_out_geometry_A': md_scale,
            'uncertainty': uncertainty, 'relative_summary_unchanged': relative_report['grouped'],
            'new_state_membership_claimed': False, 'equilibrium_or_rate_claimed': False,
            'full_question_scientific_review_required': True}, full


def evaluate(relative_instance, method, evidence=None, verify=None, enabled=True):
    if relative_instance['status'] != 'RELATIVE_COMPARISON_EXECUTED':
        raise ValueError('VALIDATED_RELATIVE_RESULT_REQUIRED')
    result = {k: relative_instance[k] for k in ('instance_id', 'facts_id', 'rule_id')}
    result.update(status='PENDING_ABSOLUTE_PATHS' if enabled else 'DISABLED', operator_requests=[])
    if not enabled:
        return result
    request = dict(operator_id=OPERATOR_ID, instance_id=result['instance_id'],
                   measurement_manifest_id=method['measurement_manifest_id'], method_id=q.identity(method))
    if evidence is not None:
        try:
            if any(evidence.get(k) != v for k, v in request.items()) or verify is None:
                raise ValueError('ABSOLUTE_EVIDENCE_BINDING')
            report = verify(evidence)
            if report['trajectory_count'] != 40:
                raise ValueError('ALL40_REQUIRED')
            limits = {row['trajectory']: {m: row['methods'][m]['interpretation'] for m in q.METHODS}
                      for row in report['rows']}
            answer = question_answer(report)
            result.update(status='ABSOLUTE_PATHS_AND_CONTACT_DECOMPOSITION_EVALUATED',
                          numerical_evidence=report, trajectory_interpretation_limits=limits,
                          scientific_claim=answer['answer'],
                          question_level_answer=answer,
                          original_relative_labels_preserved=True, accuracy_gain_claimed=False)
            return result
        except (ValueError, KeyError, TypeError) as exc:
            result['evidence_error'] = str(exc)
    result['reason'] = 'Original question needs departure and structural approach; relative preference alone and its averaged contact projection cannot establish them.'
    result['operator_requests'] = [request]
    return result


def dispatch(instance, operator):
    results = []
    for request in instance['operator_requests']:
        if request['operator_id'] != OPERATOR_ID or request['instance_id'] != instance['instance_id']:
            raise ValueError('UNBOUND_ABSOLUTE_PATH_OPERATOR')
        results.append(operator(request))
    return results

def question_answer(report):
    """Reduce verified paths to an evidence-dependent finite-time answer.

    This adds no numerical method. Human source-science authority remains pending.
    """
    rows = report['rows']
    if len(rows) != 40 or len({r['trajectory'] for r in rows}) != 40:
        raise ValueError('QUESTION_ANSWER_REQUIRES_ALL40')
    groups = {s: [r for r in rows if r['seed_group'] == s] for s in q.STATES}
    if any(len(group) != 20 for group in groups.values()):
        raise ValueError('QUESTION_ANSWER_GROUP_OWNERSHIP')
    metric = 'lid_displacement_from_20ns_A'
    medians = {s: float(np.median([r['absolute_metrics'][metric]['first20_to_last20']['after_median'] for r in group]))
               for s, group in groups.items()}
    difference = medians['closed']-medians['open']
    if not np.isfinite(list(medians.values())).all() or not np.isclose(difference, report['uncertainty']['observed_A'], atol=1e-10, rtol=1e-10):
        raise ValueError('QUESTION_GROUP_SUMMARY_INCONSISTENT')
    movement = ('CLOSED_GREATER' if difference > 0 else 'OPEN_GREATER' if difference < 0 else 'EQUAL')
    trajectories = []; by_method = {}
    for row in rows:
        delta = {s: row['absolute_metrics'][s+'_reference_lid_rmsd_A']['first20_to_last20']['delta'] for s in q.STATES}
        if not np.isfinite(list(delta.values())).all():
            raise ValueError('QUESTION_ABSOLUTE_DIRECTION_MISSING')
        approach = delta['open'] < 0 and delta['closed'] > 0
        methods = {}
        for name in q.METHODS:
            events = row['methods'][name]['events_by_persistence']['20']
            event_rows = [{'start_ns': e['start_ns'], 'end_ns': e['end_ns'], 'sample_count': e['sample_count'],
                           'internal_disagreement_samples': e['event_contact_internal_disagreement_frames'],
                           'internal_disagreement_fraction': e['event_contact_internal_disagreement_frames']/e['sample_count'],
                           'contact_direction_ranges': {k: v for k, v in e['event_range'].items() if k.endswith('normalized_direction')}} for e in events]
            methods[name] = {'sustained_opposite_preference_event_count': len(events),
                'contact_event_interpretation': ('NOT_APPLICABLE_NO_PRIMARY_EVENT' if not events else
                    'INTERNAL_DISAGREEMENT_RECORDED_WITH_DURATION_AND_AMPLITUDE' if any(e['internal_disagreement_samples'] for e in event_rows)
                    else 'NO_INTERNAL_DISAGREEMENT_OBSERVED_IN_PRIMARY_EVENTS'),
                'all_channels_agree_in_observed_primary_events': None if not events else not any(e['internal_disagreement_samples'] for e in event_rows),
                'events': event_rows, 'complete_physical_open_state_established': False}
        trajectories.append({'trajectory': row['trajectory'], 'seed_group': row['seed_group'],
            'first20_to_last20_NMR_distance_delta_A': delta,
            'absolute_approach_open_and_leave_closed': bool(approach),
            'both_reference_distances_increase': bool(all(v > 0 for v in delta.values())), 'methods': methods})
    for name in q.METHODS:
        selected = [r for r in trajectories if r['seed_group'] == 'closed' and r['methods'][name]['sustained_opposite_preference_event_count']]
        by_method[name] = {'sustained_open_preference_trajectories': [r['trajectory'] for r in selected],
            'absolute_approach_open_and_leave_closed_trajectories': [r['trajectory'] for r in selected if r['absolute_approach_open_and_leave_closed']]}
    supported = movement == 'CLOSED_GREATER' and all(v['absolute_approach_open_and_leave_closed_trajectories'] for v in by_method.values())
    counts = '; '.join(f"{name}: {len(v['sustained_open_preference_trajectories'])} sustained relative-open paths, {len(v['absolute_approach_open_and_leave_closed_trajectories'])} also approach open and leave closed" for name, v in by_method.items())
    direction = {'CLOSED_GREATER': 'closed-seeded paths have greater typical lid displacement',
                 'OPEN_GREATER': 'open-seeded paths have greater typical lid displacement', 'EQUAL': 'the two seed groups have equal median lid displacement'}[movement]
    claim = (f"Within these source simulations and20–1020ns, {direction} (closed {medians['closed']:.2f}Å; open {medians['open']:.2f}Å). {counts}. "+
        ('This supports the bounded finite-time asymmetry and open-direction rearrangement, compatible with the closed-state metastability interpretation.' if supported else
         'These results do not support the requested combination of greater closed-seed motion and sustained absolute open-direction rearrangement.')+
        ' Contact disagreements retain their event duration and amplitude; neither relative preference nor MD proximity establishes a complete physical state, equilibrium population, rate or activity.')
    return {'question_id': 'Q01', 'evidence_report_id': q.identity(report),
        'evidence_disposition': 'SUPPORT_WITHIN_CEILING' if supported else 'CANNOT_SUPPORT_REQUESTED_CLAIM',
        'group_movement_direction': movement, 'terminal_lid_displacement_medians_A': medians,
        'closed_minus_open_median_A': difference, 'conditional_uncertainty': report['uncertainty'],
        'directional_paths_by_method': by_method, 'all_trajectory_answers': trajectories,
        'answer': claim, 'scientific_interpretation_scope': 'Finite-time source-simulation structural motion; exposed development answer.',
        'terminal_disposition': 'ABSTAIN_OR_HUMAN_REVIEW', 'source_science_review_status': 'PENDING_DOMAIN_REVIEW',
        'human_final_authority': True, 'unsupported_claims': ['all candidates complete one open-state transition',
            'equilibrium population', 'transition rate', 'activity', 'mutant causal effect', 'held-out accuracy'],
        'new_operator_calls': 0, 'new_trajectory_calculations': 0, 'accuracy_gain_claimed': False}
