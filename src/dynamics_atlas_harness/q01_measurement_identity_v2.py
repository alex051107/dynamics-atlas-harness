"""Bind Q01 numerical inputs by role, trajectory, atom mapping and time axis.

This is an execution identity. Creating it today does not establish historical
immutability; old unbound data require a separately recorded readmission.
"""
import hashlib
import numpy as np
from . import q01_path_comparison_v1 as q


def array_record(value):
    array = np.asarray(value, dtype='<f8', order='C')
    if not np.all(np.isfinite(array)):
        raise ValueError('NONFINITE_BOUND_MEASUREMENT')
    return {'shape': list(array.shape), 'dtype': '<f8',
            'sha256': hashlib.sha256(array.tobytes(order='C')).hexdigest()}


def reference_identity(reference, contacts):
    roles = {s+'_'+role: array_record(reference[s+'_'+role])
             for s in q.STATES for role in ('core', 'lid', 'distances_A')}
    return q.identity({'arrays_in_angstrom': roles, 'contact_columns': contacts,
                       'core_atom_keys': [[i, a] for i in q.CORE for a in q.ATOM_NAMES],
                       'lid_atom_keys': [[i, a] for i in q.LID for a in q.ATOM_NAMES]})


def measurement_manifest(records, contacts, reference, mappings, facts):
    by_name = {entry['name']: entry for entry in mappings}
    if set(by_name) != set(records) or len(by_name) != len(mappings):
        raise ValueError('TRAJECTORY_IDENTITY_MISMATCH')
    rows = []
    for name in sorted(records):
        record, entry = records[name], by_name[name]
        if record['seed'] != entry['seed'] or record['seed'] not in q.STATES:
            raise ValueError('SEED_IDENTITY_MISMATCH')
        if not np.array_equal(record['time_ns'], np.arange(20, 1021)):
            raise ValueError('NONCANONICAL_BOUND_TIME_AXIS')
        if np.shape(record['distances_A']) != (1001, len(contacts)):
            raise ValueError('CONTACT_COLUMN_AXIS_MISMATCH')
        arrays = {'time_ns': record['time_ns'], 'contact_distances_A': record['distances_A']}
        for state in q.STATES:
            value = record['geometry_A'][state]
            if np.shape(value) != (1001,):
                raise ValueError('GEOMETRY_TIME_AXIS_MISMATCH')
            arrays[state+'_reference_lid_rmsd_A'] = value
        rows.append({'trajectory': name, 'seed': record['seed'],
                     'source_and_atom_mapping_id': q.identity(entry),
                     'arrays': {role: array_record(value) for role, value in arrays.items()}})
    body = {'schema': 'q01-measurement-manifest/v2', 'facts_id': q.identity(facts),
            'input_id': facts['input_id'], 'method_id': facts['method_id'],
            'contact_columns': contacts, 'reference_id': reference_identity(reference, contacts),
            'trajectories': rows}
    return dict(body, manifest_id=q.identity(body))


def verify_manifest(expected, records, contacts, reference, mappings, facts):
    actual = measurement_manifest(records, contacts, reference, mappings, facts)
    if actual != expected:
        raise ValueError('CONTINUOUS_MEASUREMENT_OR_REFERENCE_IDENTITY_MISMATCH')
    return actual


def verify_policy(policy, reference, contacts, expected_reference_id):
    from . import q01_relative_paths_v1 as r
    if reference_identity(reference, contacts) != expected_reference_id:
        raise ValueError('REFERENCE_ARRAY_IDENTITY_MISMATCH')
    rebuilt = r.reference_policy({s: reference[s+'_distances_A'] for s in q.STATES}, contacts)
    for key in ('policy', 'normalization', 'reference_preference'):
        if policy.get(key) != rebuilt[key]:
            raise ValueError('REFERENCE_POLICY_NOT_SOURCE_DERIVED:'+key)
