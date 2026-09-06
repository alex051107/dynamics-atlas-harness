"""Exposed Q01 development obligation and finite-time path comparison.

This deliberately narrow adapter is separate from the unchanged Draft baseline.
Reference envelopes are construction diagnostics, not statistical confidence sets.
No equilibrium, rate, activity or held-out accuracy claim is produced.
"""
import hashlib
import itertools
import json

import numpy as np

RULE_ID = 'Q01_R01_STATE_METHOD_CONSISTENCY_V1'
OPERATOR_ID = 'q01_full40_same_coordinates_dual_threshold_v1'
METHODS = ('deposited_uniform', 'SI_per_contact')
STATES = ('open', 'closed')
CORE = list(range(40, 98)) + list(range(137, 221))
LID = list(range(98, 137))
ATOM_NAMES = ('N', 'CA', 'C', 'O')
CONFIG = {
    'version': 'q01-path-comparison/v1',
    'core_residues': CORE, 'lid_residues': LID, 'backbone_atoms': ATOM_NAMES,
    'time_ns': [20, 1020, 1], 'methods': METHODS,
    'primary_persistence_frames': 20, 'sensitivity_frames': [5, 50],
    'geometry_envelope': 'max leave-one-model-out nearest own-reference lid RMSD',
    'contact_envelope': 'max own-reference mean violation, separately per state/method',
    'calibration_role': 'CONSTRUCTION_ONLY_NOT_CONFIDENCE_BOUND',
    'support_rule': 'unique intersection of geometry and contact reference support',
    'distance_numerical_tolerance_A': .011,
    'claim_ceiling': 'Conditional finite-time paths for source seeds; no kinetics/equilibrium/activity',
}


def identity(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def nearest_lid_rmsd(core, lid, ref_core, ref_lid, exclude_self=False):
    """Row-vector Kabsch on core only; never independently realign the lid."""
    core, lid = np.asarray(core, float), np.asarray(lid, float)
    centroid = core.mean(axis=1, keepdims=True)
    centered = core - centroid
    distances = []
    for j, (rc, rl) in enumerate(zip(ref_core, ref_lid)):
        rmean = rc.mean(axis=0)
        cov = np.einsum('nai,aj->nij', centered, rc-rmean)
        u, _, vt = np.linalg.svd(cov)
        signs = np.ones((len(core), 3)); signs[:, -1] = np.linalg.det(u @ vt)
        rotation = (u * signs[:, None, :]) @ vt
        fitted = (lid-centroid) @ rotation + rmean
        d = np.sqrt(np.mean(np.sum((fitted-rl)**2, axis=2), axis=1))
        if exclude_self:
            if len(core) != len(ref_core):
                raise ValueError('LEAVE_ONE_OUT_AXIS_MISMATCH')
            d[j] = np.inf
        distances.append(d)
    return np.min(np.stack(distances, axis=1), axis=1)


def minimum_image(delta, box):
    """Nearest periodic displacement for reduced GROMACS boxes, in source nm."""
    delta, box = np.asarray(delta, float), np.asarray(box, float)
    if box.shape != (len(delta), 3, 3) or np.any(np.linalg.det(box) <= 0):
        raise ValueError('INVALID_PERIODIC_BOX')
    fractional = np.einsum('nci,nij->ncj', delta, np.linalg.inv(box))
    base = np.rint(fractional)
    best = np.full(delta.shape[:2], np.inf)
    for offset in itertools.product((-1, 0, 1), repeat=3):
        vector = np.einsum('nci,nij->ncj', fractional-base-np.array(offset), box)
        best = np.minimum(best, np.sum(vector**2, axis=2))
    return np.sqrt(best)


def scores(distances_A, contacts, method):
    if method not in METHODS:
        raise ValueError('UNKNOWN_THRESHOLD_METHOD')
    result = {}
    for state in STATES:
        ids = [i for i, c in enumerate(contacts) if c['state'] == state]
        bounds = [contacts[i]['dviol_angstrom'] if method == METHODS[1]
                  else (10. if state == 'open' else 8.5) for i in ids]
        result[state] = np.maximum(0., distances_A[:, ids]-bounds).mean(axis=1)
    return result


def calibrate(reference, contacts):
    """Only NMR reference coordinates enter; trajectory outcomes are unavailable."""
    calibration = {'geometry_A': {}, 'contact_A': {}, 'reference_discrimination': {}}
    for state in STATES:
        own = reference[state]
        loo = nearest_lid_rmsd(own['core'], own['lid'], own['core'], own['lid'], True)
        calibration['geometry_A'][state] = float(np.max(loo))
    for method in METHODS:
        calibration['contact_A'][method] = {
            state: float(np.max(scores(reference[state]['distances_A'], contacts, method)[state]))
            for state in STATES}
        discrimination = {}
        for origin in STATES:
            own = reference[origin]
            geometry = {state: nearest_lid_rmsd(own['core'], own['lid'], reference[state]['core'],
                        reference[state]['lid'], state == origin) for state in STATES}
            labels = classify(geometry, scores(own['distances_A'], contacts, method), calibration, method)
            discrimination[origin] = {label: int(np.sum(labels == label)) for label in ('open', 'closed', 'ambiguous', 'outside')}
        calibration['reference_discrimination'][method] = discrimination
    return calibration


def classify(geometry, contact_scores, calibration, method):
    support = [(np.asarray(geometry[s]) <= calibration['geometry_A'][s]+1e-10) &
               (np.asarray(contact_scores[s]) <= calibration['contact_A'][method][s]+1e-10)
               for s in STATES]
    a, b = support
    return np.where(a & ~b, 'open', np.where(b & ~a, 'closed', np.where(a & b, 'ambiguous', 'outside')))


def runs(mask):
    padded = np.r_[False, np.asarray(mask, bool), False].astype(int)
    return list(zip(np.flatnonzero(np.diff(padded) == 1).tolist(), np.flatnonzero(np.diff(padded) == -1).tolist()))


def path_summary(labels, seed, persistence):
    labels = np.asarray(labels)
    initial = str(labels[0]); other = 'closed' if initial == 'open' else 'open'
    departures = [(a, b) for a, b in runs(labels != initial) if b-a >= persistence]
    arrival = [(a, b) for a, b in runs(labels == other) if b-a >= persistence and a > 0]
    if initial not in STATES:
        route = 'INITIAL_OUTSIDE_OR_AMBIGUOUS_REFERENCE_SUPPORT'
    elif arrival:
        route = 'DEPARTED_INITIAL_AND_SUSTAINED_OTHER_REFERENCE'
    elif departures:
        route = 'DEPARTED_INITIAL_REFERENCE_WITHOUT_SUSTAINED_OTHER_SUPPORT'
    else:
        route = 'NO_PERSISTENT_DEPARTURE_FROM_INITIAL_REFERENCE_SUPPORT'
    return {'seed_group': seed, 'initial_support': initial, 'initial_matches_seed': initial == seed,
            'route': route, 'persistence_frames': persistence, 'sampled_span_ns': persistence-1,
            'first_departure_frame': departures[0][0] if departures else None,
            'first_other_support_frame': arrival[0][0] if arrival and initial in STATES else None,
            'frame_counts': {s: int(np.sum(labels == s)) for s in (*STATES, 'ambiguous', 'outside')},
            'longest_seed_support_frames': max([b-a for a, b in runs(labels == seed)] or [0]),
            'longest_other_support_frames': max([b-a for a, b in runs(labels == ('closed' if seed == 'open' else 'open'))] or [0])}


def summarize(trajectories, contacts, calibration):
    paths = {}; frame_labels = {}; trajectory_changes = []
    for name, record in trajectories.items():
        if record['geometry_A'].keys() != set(STATES):
            raise ValueError('MISSING_GEOMETRY_REFERENCE')
        time = np.asarray(record['time_ns'])
        if not np.array_equal(time, np.arange(20, 1021)):
            raise ValueError('NONCANONICAL_TIME_AXIS')
        if not np.all(np.isfinite(record['distances_A'])):
            raise ValueError('NONFINITE_DISTANCE')
        labels_by_method = {}
        for method in METHODS:
            labels = classify(record['geometry_A'], scores(record['distances_A'], contacts, method), calibration, method)
            labels_by_method[method] = labels
            paths[(name, method)] = {str(p): path_summary(labels, record['seed'], p) for p in (20, 5, 50)}
        frame_labels[name] = labels_by_method
        left, right = (paths[(name, method)] for method in METHODS)
        trajectory_changes.append({'trajectory': name, 'seed_group': record['seed'],
            'frame_label_changes': int(np.sum(labels_by_method[METHODS[0]] != labels_by_method[METHODS[1]])),
            'primary_route_changed': left['20']['route'] != right['20']['route'],
            'primary_initial_support_changed': left['20']['initial_support'] != right['20']['initial_support'],
            'sensitivity_route_changes': {str(p): left[str(p)]['route'] != right[str(p)]['route'] for p in (5, 50)}})
    grouped = {}
    for method in METHODS:
        grouped[method] = {}
        for seed in STATES:
            entries = [paths[(name, method)] for name, r in trajectories.items() if r['seed'] == seed]
            grouped[method][seed] = {str(p): {route: sum(x[str(p)]['route'] == route for x in entries)
                for route in sorted({x[str(p)]['route'] for x in entries})} for p in (20, 5, 50)}
    result = {'trajectory_count': len(trajectories), 'group_counts': {s: sum(r['seed'] == s for r in trajectories.values()) for s in STATES},
              'trajectory_changes': trajectory_changes, 'grouped_paths': grouped,
              'paths': [{'trajectory': name, 'method': method, 'persistence_results': values} for (name, method), values in paths.items()],
              'full_question_answer': False, 'claim_ceiling': CONFIG['claim_ceiling']}
    return result, frame_labels


def evaluate(facts, evidence=None, enabled=True, verify_evidence=None):
    """A new source-bound CASE rule, not a replacement baseline or paper gold."""
    if facts.get('question_id') != 'Q01' or facts.get('claim') != 'FINITE_TIME_SEEDED_PATH_COMPARISON':
        raise ValueError('Q01_SCOPE_REQUIRED')
    token = identity(facts)
    instance = {'rule_id': RULE_ID, 'instance_id': RULE_ID+':'+token[:20], 'facts_id': token,
                'operator_requests': [], 'scientific_status': 'UNRESOLVED', 'status': 'DISABLED' if not enabled else 'PENDING',
                'scope': 'EXPOSED_DEVELOPMENT_CASE_RULE'}
    if not enabled:
        return instance
    definitions = facts.get('threshold_definitions', [])
    if len(definitions) != 2 or any(not d.get('source_locator') or not d.get('bounds_A') for d in definitions):
        instance['status'] = 'SOURCE_DEFINITION_GAP'; return instance
    if definitions[0]['bounds_A'] == definitions[1]['bounds_A']:
        instance['status'] = 'NO_THRESHOLD_DIFFERENCE'; return instance
    instance['reason'] = 'Same source trajectories have two admissible state-score definitions; test path conclusion sensitivity.'
    request = {'operator_id': OPERATOR_ID, 'instance_id': instance['instance_id'], 'facts_id': token,
               'method_id': facts['method_id'], 'input_id': facts['input_id']}
    if evidence is not None:
        try:
            if any(evidence.get(k) != v for k, v in request.items()):
                raise ValueError('EVIDENCE_BINDING_MISMATCH')
            if verify_evidence is None:
                raise ValueError('NUMERICAL_REPLAY_REQUIRED')
            report = verify_evidence(evidence)
            if report['trajectory_count'] != 40 or report['group_counts'] != {'open': 20, 'closed': 20}:
                raise ValueError('FULL40_REQUIRED')
            changed = sum(x['primary_route_changed'] or x['primary_initial_support_changed'] for x in report['trajectory_changes'])
            instance.update(status='COMPARISON_EXECUTED', numeric_result=report,
                scientific_status='METHOD_DEPENDENT_PATH_JUDGMENTS' if changed else 'PATH_JUDGMENTS_UNCHANGED_UNDER_TWO_METHODS',
                changed_primary_trajectories=changed, accuracy_gain_claimed=False)
            if report.get('paths') and all(p['persistence_results']['20']['initial_support'] not in STATES for p in report['paths']):
                instance['scientific_status'] = 'INITIAL_REFERENCE_SUPPORT_UNESTABLISHED_FOR_ALL_TRAJECTORIES'
                instance['limitation'] = 'The comparison completed but this construction-envelope classification supplies no initial-state departure answer.'
            return instance
        except (ValueError, KeyError, TypeError) as exc:
            instance['evidence_error'] = str(exc)
    instance['operator_requests'] = [request]
    return instance


def dispatch(instance, operator):
    results = []
    for request in instance['operator_requests']:
        if request['operator_id'] != OPERATOR_ID or request['instance_id'] != instance['instance_id']:
            raise ValueError('UNKNOWN_OR_UNBOUND_OPERATOR')
        results.append(operator(request))
    return results
