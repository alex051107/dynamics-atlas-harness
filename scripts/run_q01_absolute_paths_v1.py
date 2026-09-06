"""Frozen full40 absolute-path comparison, with zero new trajectory extraction."""
import argparse
import csv
import datetime
import json
from pathlib import Path
import time
import numpy as np
from dynamics_atlas_harness import q01_path_comparison_v1 as q
from dynamics_atlas_harness import q01_relative_paths_v1 as relative
from dynamics_atlas_harness import q01_measurement_identity_v2 as binding
from dynamics_atlas_harness import q01_absolute_paths_v1 as absolute
from run_q01_relative_paths_v1 import load_bound_records


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')


def coordinate_binding(coordinate):
    return {key: binding.array_record(coordinate[key]) for key in ('xyz_nm', 'box_nm', 'time_ns')}


def prepare(parent, admission, relative_output, out):
    records, reference, manifest = load_bound_records(parent, admission)
    mappings = json.loads((parent/'trajectory_mapping.json').read_text())
    coordinate_ids = {}
    for entry in mappings:
        coordinate = np.load(parent/'trajectories'/entry['name']/'coordinates.npz', allow_pickle=False)
        coordinate_ids[entry['name']] = coordinate_binding(coordinate)
    method = {'policy': absolute.POLICY, 'measurement_manifest_id': manifest['manifest_id'],
              'reference_id': manifest['reference_id'], 'coordinate_bindings': coordinate_ids,
              'relative_policy': json.loads((relative_output/'frozen_policy.json').read_text()),
              'saved_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'development_status': 'Relative outcomes exposed; absolute full-path and MD-reference policy frozen before new computation',
              'coordinate_readmission': json.loads((admission/'receipt.json').read_text()),
              'historical_immutability_claimed': False}
    out.mkdir(parents=True, exist_ok=False)
    save(out/'frozen_method.json', method)
    print(json.dumps({'status': 'ABSOLUTE_POLICY_FROZEN', 'trajectories': len(records),
                      'measurement_manifest_id': manifest['manifest_id'], 'method_id': q.identity(method)}))


def run(parent, admission, relative_output, out):
    started = time.monotonic()
    records, reference, manifest = load_bound_records(parent, admission)
    mappings = json.loads((parent/'trajectory_mapping.json').read_text())
    method = json.loads((out/'frozen_method.json').read_text())
    contacts = json.loads((parent/'contacts.json').read_text())
    facts = json.loads((parent/'facts.json').read_text())
    calibration = json.loads((parent/'reference_calibration.json').read_text())
    if method['policy'] != absolute.POLICY or method['measurement_manifest_id'] != manifest['manifest_id']:
        raise ValueError('FROZEN_ABSOLUTE_METHOD_OR_INPUT_CHANGED')
    policy = method['relative_policy']
    binding.verify_policy(policy, reference, contacts, manifest['reference_id'])
    if policy['measurement_manifest_id'] != manifest['manifest_id']:
        raise ValueError('RELATIVE_INPUT_CHANGED')
    envelope, _ = q.summarize(records, contacts, calibration)
    parent_evidence = json.loads((parent/'evidence_result.json').read_text())
    if q.identity(envelope) != parent_evidence['report_id']:
        raise ValueError('PARENT_REPLAY_CHANGED')
    base = q.evaluate(facts, parent_evidence, verify_evidence=lambda _: envelope)
    relative_report, _ = relative.compare(records, contacts, policy)
    relative_evidence = json.loads((relative_output/'evidence_result.json').read_text())
    if q.identity(relative_report) != relative_evidence['report_id']:
        raise ValueError('RELATIVE_NUMERICAL_REPLAY_CHANGED')
    previous = relative.evaluate(base, facts, envelope, policy, relative_evidence, lambda _: relative_report)
    before = absolute.evaluate(previous, method); off = absolute.evaluate(previous, method, enabled=False)
    save(out/'verified_relative_instance.json', previous)
    save(out/'rules_before.json', before); save(out/'rules_off.json', off)
    calls = []; displacement = {}; md_distance = {}; anchors = {}
    def load_coordinates(entry):
        values = dict(np.load(parent/'trajectories'/entry['name']/'coordinates.npz', allow_pickle=False))
        if coordinate_binding(values) != method['coordinate_bindings'][entry['name']]:
            raise ValueError('CONTINUOUS_COORDINATES_CHANGED:'+entry['name'])
        m = entry['mapping']
        np.testing.assert_array_equal(values['time_ns'], records[entry['name']]['time_ns'])
        return values['xyz_nm'][:, m['core']]*10, values['xyz_nm'][:, m['lid']]*10
    def operator(request):
        calls.append(request); save(out/'operator_dispatch.json', request)
        indices = np.array(absolute.POLICY['MD_reference_samples_ns'])-20
        for entry in mappings:
            if entry['seed'] == 'open':
                core, lid = load_coordinates(entry)
                anchors[entry['name']] = (core[indices], lid[indices])
        anchor_manifest = {'time_ns': absolute.POLICY['MD_reference_samples_ns'],
            'trajectories': list(anchors), 'whole_query_trajectory_excluded_for_open_LOO': True,
            'selected_from_closed_trajectories': False, 'reference_frames': sum(len(v[0]) for v in anchors.values())}
        save(out/'MD_reference_anchors.json', anchor_manifest)
        for entry in mappings:
            if time.monotonic()-started > 1200:
                raise TimeoutError('BOUNDED_ABSOLUTE_PATH_BUDGET_EXCEEDED')
            core, lid = load_coordinates(entry); name = entry['name']
            displacement[name] = q.nearest_lid_rmsd(core, lid, core[:1], lid[:1])
            use = [value for key, value in anchors.items() if key != name]
            ref_core, ref_lid = (np.concatenate([v[i] for v in use]) for i in (0, 1))
            md_distance[name] = q.nearest_lid_rmsd(core, lid, ref_core, ref_lid)
            np.savez_compressed(out/(name+'.npz'), time_ns=records[name]['time_ns'],
                displacement_from_20ns_A=displacement[name], nearest_open_MD_lid_rmsd_A=md_distance[name])
            print('absolute_path', name, 'MD_anchors', len(ref_core), 'elapsed_seconds', round(time.monotonic()-started, 1), flush=True)
        report, full = absolute.describe(records, contacts, policy, displacement, md_distance)
        save(out/'numerical_report.json', report)
        with (out/'full_absolute_paths.tsv').open('w', newline='') as stream:
            writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
            keys = ['open_reference_lid_rmsd_A', 'closed_reference_lid_rmsd_A', 'lid_displacement_from_20ns_A',
                    'nearest_open_MD_lid_rmsd_A', 'open_contact_A', 'closed_contact_A',
                    'open_contact_normalized_direction', 'closed_contact_normalized_direction',
                    'internal_contact_disagreement', 'relative_preference']
            writer.writerow(['trajectory', 'seed', 'method', 'time_ns', *keys])
            for name, rec in records.items():
                for m in q.METHODS:
                    arrays = full[(name, m)]
                    for i, t in enumerate(rec['time_ns']):
                        writer.writerow([name, rec['seed'], m, t, *[arrays[key][i] for key in keys]])
        return dict(request, report_id=q.identity(report), report_path='numerical_report.json',
                    evidence_type='ACTUAL_ABSOLUTE_PATH_AND_CONTACT_COMPONENT_EVIDENCE')
    absolute.dispatch(off, operator)
    if calls:
        raise ValueError('OFF_DISPATCHED')
    evidence = absolute.dispatch(before, operator)[0]
    def verify(value):
        report, _ = absolute.describe(records, contacts, policy, displacement, md_distance)
        if q.identity(report) != value['report_id']:
            raise ValueError('ABSOLUTE_NUMERICAL_EVIDENCE_CHANGED')
        return report
    after = absolute.evaluate(previous, method, evidence, verify)
    save(out/'evidence_result.json', evidence); save(out/'rules_after.json', after)
    save(out/'receipt.json', {'status': after['status'], 'completed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'instance_id': after['instance_id'], 'same_instance_as_relative': after['instance_id'] == previous['instance_id'],
        'on_operator_calls': len(calls), 'off_operator_calls': 0, 'new_GROMACS_calls': 0, 'new_optimizations': 0,
        'elapsed_seconds': time.monotonic()-started, 'trajectory_count': len(records),
        'measurement_manifest_id': manifest['manifest_id'], 'historical_work_reclassified_as_extra': False,
        'source_raw_coordinates_published': False, 'original_labels_preserved': True})
    print(json.dumps({'status': after['status'], 'elapsed_seconds': time.monotonic()-started}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('parent', 'admission', 'relative-output', 'output'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--phase', choices=['prepare', 'run'], required=True)
    args = parser.parse_args()
    globals()[args.phase](args.parent.resolve(), args.admission.resolve(), args.relative_output.resolve(), args.output.resolve())
