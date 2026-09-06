"""Reconstruct historical measurements from saved extraction, never reread XTC.

Outputs establish current parity with saved GROMACS text and primary reference
coordinates. They make no retrospective promise about unbound historical files.
"""
import argparse
import datetime
import importlib.util
import json
from pathlib import Path
import numpy as np
from dynamics_atlas_harness import q01_path_comparison_v1 as q
from dynamics_atlas_harness import q01_measurement_identity_v2 as binding
import run_q01_path_comparison_v1 as runner


def run(workspace, parent, out):
    out.mkdir(parents=True, exist_ok=False)
    facts = json.loads((parent/'facts.json').read_text())
    method = json.loads((parent/'frozen_method.json').read_text())
    contacts = json.loads((parent/'contacts.json').read_text())
    mappings = json.loads((parent/'trajectory_mapping.json').read_text())
    if q.identity(method) != facts['method_id'] or method['contacts'] != contacts:
        raise ValueError('PARENT_FROZEN_METHOD_CHANGED')
    acquisition, feasibility = runner.paths(workspace)
    contact_config = json.loads((acquisition/'config/noe_contacts_v0.json').read_text())
    source_contacts = [dict(c, state=s) for s in q.STATES for c in contact_config[s+'_contacts'] if c['md_used']]
    if contacts != source_contacts:
        raise ValueError('PRIMARY_CONTACT_CONFIG_CHANGED')
    spec = importlib.util.spec_from_file_location('source_reference_parser', acquisition/'scripts/structural_contact_calibration.py')
    parser = importlib.util.module_from_spec(spec); spec.loader.exec_module(parser)
    reference = {}; refs = {}
    old_reference = np.load(parent/'reference_coordinates.npz', allow_pickle=False)
    for state, pdb in [('open', '8B7I'), ('closed', '8B7J')]:
        models = parser.read_atom_models(feasibility/'inputs'/f'{pdb}.cif.gz')
        cores, lids, distances = [], [], []
        for model in models.values():
            residues = {res: atoms for (res, _), atoms in model.items()}
            cores.append([residues[res][atom] for res in q.CORE for atom in q.ATOM_NAMES])
            lids.append([residues[res][atom] for res in q.LID for atom in q.ATOM_NAMES])
            distances.append([parser.evaluate_contact(model, c)[0] for c in contacts])
        refs[state] = {'core': np.array(cores), 'lid': np.array(lids), 'distances_A': np.array(distances)}
        for role, value in refs[state].items():
            np.testing.assert_allclose(value, old_reference[state+'_'+role], rtol=0, atol=1e-10)
            reference[state+'_'+role] = value
    calibration = q.calibrate(refs, contacts)
    if calibration != json.loads((parent/'reference_calibration.json').read_text()):
        raise ValueError('REFERENCE_CALIBRATION_CHANGED')
    records = {}; checks = []
    for entry in mappings:
        directory = parent/'trajectories'/entry['name']; m = entry['mapping']
        rebuilt_map = runner.mapping(runner.read_gro(workspace/entry['gro']), contacts)
        if json.loads(json.dumps(rebuilt_map)) != m:
            raise ValueError('ATOM_MAPPING_CHANGED:'+entry['name'])
        xyz_text = np.loadtxt(directory/'coordinates_nm.xvg')
        box_text = np.loadtxt(directory/'box_nm.xvg')
        coordinate = np.load(directory/'coordinates.npz', allow_pickle=False)
        xyz, box, time = coordinate['xyz_nm'], coordinate['box_nm'], coordinate['time_ns']
        np.testing.assert_array_equal(xyz_text[:, 1:].reshape(xyz.shape), xyz)
        np.testing.assert_array_equal(xyz_text[:, 0]/1000, time)
        np.testing.assert_array_equal(box_text[:, 0]/1000, time)
        rebuilt_box = np.zeros_like(box)
        rebuilt_box[:, 0, 0], rebuilt_box[:, 1, 1], rebuilt_box[:, 2, 2] = box_text[:, 1], box_text[:, 2], box_text[:, 3]
        rebuilt_box[:, 1, 0], rebuilt_box[:, 2, 0], rebuilt_box[:, 2, 1] = box_text[:, 4], box_text[:, 5], box_text[:, 6]
        np.testing.assert_array_equal(rebuilt_box, box)
        delta = np.stack([xyz[:, pair[0]].mean(axis=1)-xyz[:, pair[1]].mean(axis=1) for pair in m['contacts']], axis=1)
        distances = q.minimum_image(delta, box)*10.
        geometry = {s: q.nearest_lid_rmsd(xyz[:, m['core']]*10, xyz[:, m['lid']]*10,
                    reference[s+'_core'], reference[s+'_lid']) for s in q.STATES}
        old = np.load(directory/'measurements.npz', allow_pickle=False)
        errors = {'contact_A': float(np.max(abs(distances-old['distances_A'])))}
        np.testing.assert_array_equal(time, old['time_ns'])
        np.testing.assert_allclose(distances, old['distances_A'], rtol=0, atol=1e-10)
        for state in q.STATES:
            errors[state+'_rmsd_A'] = float(np.max(abs(geometry[state]-old[state+'_rmsd_A'])))
            np.testing.assert_allclose(geometry[state], old[state+'_rmsd_A'], rtol=0, atol=1e-10)
        records[entry['name']] = {'seed': entry['seed'], 'time_ns': time, 'distances_A': distances, 'geometry_A': geometry}
        checks.append({'trajectory': entry['name'], 'status': 'CURRENT_SAVED_EXTRACTION_PARITY', 'maximum_errors': errors})
        print('readmitted', entry['name'], errors, flush=True)
    report, _ = q.summarize(records, contacts, calibration)
    if report != json.loads((parent/'numerical_report.json').read_text()):
        raise ValueError('HISTORICAL_ENVELOPE_REPLAY_DIFFERENCE')
    manifest = binding.measurement_manifest(records, contacts, reference, mappings, facts)
    runner.save(out/'measurement_manifest.json', manifest)
    runner.save(out/'receipt.json', {'completed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'status': 'COORDINATE_DERIVED_READMISSION_PASS', 'trajectories': checks,
        'tolerance_A': 1e-10, 'reference_primary_CIF_replayed': True,
        'new_GROMACS_calls': 0, 'optimizations': 0,
        'historical_immutability_established': False,
        'claim': 'Current derived arrays match saved extraction text/boxes and source NMR references; historical unbound originals preserved.',
        'measurement_manifest_id': manifest['manifest_id']})


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', type=Path, required=True)
    parser.add_argument('--parent', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    run(args.workspace.resolve(), args.parent.resolve(), args.output.resolve())
