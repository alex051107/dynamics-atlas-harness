"""Prepare reference-only criteria, then dispatch the source-bound full40 operator."""
import argparse
import csv
import datetime
import gzip
import hashlib
import importlib.util
import json
import subprocess
from pathlib import Path

import numpy as np
from dynamics_atlas_harness import q01_path_comparison_v1 as q
from dynamics_atlas_harness import q01_measurement_identity_v2 as binding


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024*1024), b''):
            h.update(block)
    return h.hexdigest()


def read_gro(path):
    lines = path.read_text().splitlines(); n = int(lines[1]); atoms = {}
    for index, line in enumerate(lines[2:2+n], 1):
        key = (int(line[:5]), line[10:15].strip())
        if key in atoms:
            raise ValueError('DUPLICATE_GRO_ATOM')
        atoms[key] = (index, line[5:10].strip())
    if len(atoms) != n:
        raise ValueError('GRO_ATOM_COUNT')
    return atoms


def mapping(atoms, contacts):
    keys = [(res, name) for res in sorted(q.CORE+q.LID) for name in q.ATOM_NAMES]
    hydrogen_names = {'HB*': ['HB1', 'HB2', 'HB3'], 'HD1*': ['HD1', 'HD2', 'HD3'],
                      'HD2*': ['HD21', 'HD22', 'HD23'], 'HE*': ['HE1', 'HE2', 'HE3'], 'HG2*': ['HG21', 'HG22', 'HG23']}
    contact_keys = []
    for c in contacts:
        pair = []
        for endpoint in ('i', 'j'):
            expected = c['resname_'+endpoint]
            kk = [(c['residue_'+endpoint], h) for h in hydrogen_names[c['pseudoatom_'+endpoint]]]
            if any(atoms[k][1] != expected for k in kk):
                raise ValueError('CONTACT_RESIDUE_IDENTITY')
            pair.append(kk); keys.extend(k for k in kk if k not in keys)
        contact_keys.append(pair)
    index = {k: i for i, k in enumerate(keys)}
    return {'atom_keys': keys, 'atom_indices': [atoms[k][0] for k in keys],
            'core': [index[(r, a)] for r in q.CORE for a in q.ATOM_NAMES],
            'lid': [index[(r, a)] for r in q.LID for a in q.ATOM_NAMES],
            'contacts': [[[index[k] for k in side] for side in pair] for pair in contact_keys]}


def paths(workspace):
    root = workspace/'autoresearch/tasks'
    return root/'dynamics_atlas_hsp90_acquisition_20260725', root/'dynamics_atlas_hsp90_feasibility_20260725'


def prepare(workspace, out):
    out.mkdir(parents=True, exist_ok=False)
    acquisition, feasibility = paths(workspace)
    config = json.loads((acquisition/'config/noe_contacts_v0.json').read_text())
    contacts = [dict(c, state=s) for s in q.STATES for c in config[s+'_contacts'] if c['md_used']]
    if len(contacts) != 24:
        raise ValueError('SOURCE_CONTACT_COUNT')
    save(out/'contacts.json', contacts)
    source = acquisition/'scripts/structural_contact_calibration.py'
    spec = importlib.util.spec_from_file_location('q01_source_calibration', source)
    parser = importlib.util.module_from_spec(spec); spec.loader.exec_module(parser)
    refs = {}; inputs = [acquisition/'config/noe_contacts_v0.json', source]
    arrays = {}
    for state, pdb in [('open', '8B7I'), ('closed', '8B7J')]:
        path = feasibility/'inputs'/f'{pdb}.cif.gz'; inputs.append(path)
        models = parser.read_atom_models(path)
        if len(models) != 20:
            raise ValueError('REFERENCE_MODEL_COUNT')
        cores, lids, distances = [], [], []
        for model in models.values():
            residue_map = {}
            for (res, name), atoms in model.items():
                if res in residue_map:
                    raise ValueError('REFERENCE_RESIDUE_AMBIGUOUS')
                residue_map[res] = atoms
            cores.append([residue_map[r][a] for r in q.CORE for a in q.ATOM_NAMES])
            lids.append([residue_map[r][a] for r in q.LID for a in q.ATOM_NAMES])
            distances.append([parser.evaluate_contact(model, c)[0] for c in contacts])
        refs[state] = {'core': np.array(cores), 'lid': np.array(lids), 'distances_A': np.array(distances)}
        arrays.update({state+'_'+k: v for k, v in refs[state].items()})
    calibration = q.calibrate(refs, contacts)
    save(out/'reference_calibration.json', calibration)
    np.savez_compressed(out/'reference_coordinates.npz', **arrays)
    method = {'config': q.CONFIG, 'contacts': contacts, 'calibration': calibration,
              'reference_id': binding.reference_identity(arrays, contacts), 'prespecified_before_full40': now(), 'author_route_labels_used': False,
              'method_origin': 'Conditional reference-envelope operationalization; not original TTClust assignments',
              'source_method_review': 'source_method_review.md'}
    save(out/'frozen_method.json', method)
    runs = []
    for path in sorted((acquisition/'data/trajectories').glob('*.xtc')):
        name = path.stem; family = name.split('_')[0]
        if family not in ('R46A', 'R60A'):
            continue
        gro = acquisition/'data/contract/MD'/family/name/'processed.gro'
        atoms = read_gro(gro); m = mapping(atoms, contacts)
        # Directory is source seed lineage; simulation coordinates have WT ARG46/60.
        if atoms[(46, 'CA')][1] != 'ARG' or atoms[(60, 'CA')][1] != 'ARG':
            raise ValueError('SIMULATION_SEQUENCE_IDENTITY')
        runs.append({'name': name, 'seed': 'closed' if family == 'R46A' else 'open',
                     'xtc': str(path.relative_to(workspace)), 'gro': str(gro.relative_to(workspace)),
                     'atom_count': len(atoms), 'mapping': m})
        inputs += [path, gro]
    if len(runs) != 40 or sum(r['seed'] == 'open' for r in runs) != 20:
        raise ValueError('FULL40_SOURCE_ROSTER')
    inventory = [{'path': str(p.relative_to(workspace)), 'bytes': p.stat().st_size, 'sha256': digest(p)} for p in inputs]
    save(out/'input_inventory.json', inventory)
    save(out/'trajectory_mapping.json', runs)
    facts = {'question_id': 'Q01', 'claim': 'FINITE_TIME_SEEDED_PATH_COMPARISON',
             'input_id': q.identity(inventory), 'method_id': q.identity(method),
             'original_facts_locator': 'q01_original_facts_v1.json',
             'source_class': 'EXPOSED_DEVELOPMENT_RAW_MD_NMR_CONSTRUCTION',
             'threshold_definitions': [
                 {'source_locator': 'MD/Tools/VIOLATION/NOE_specific_GS_ES_2022-01-07_distances.itp; no-ref call',
                  'bounds_A': [10. if c['state'] == 'open' else 8.5 for c in contacts]},
                 {'source_locator': 'Henot2022 SupplementaryTable2 pp4-5 dviol;explicitMDsubset19+5',
                  'bounds_A': [c['dviol_angstrom'] for c in contacts]}],
             'source_exclusions': {'O04': 'SI2c,f', 'O10': 'SI2c,f', 'O15': 'SI2d,f', 'O23': 'SI2e,f', 'O24': 'SI2e,f'},
             'original_full_execution_config': 'UNKNOWN'}
    save(out/'facts.json', facts)
    print(json.dumps({'prepared_at': now(), 'calibration': calibration, 'trajectories': len(runs), 'method_id': facts['method_id']}, indent=2))


def extract(workspace, out, run, contacts):
    directory = out/'trajectories'/run['name']; directory.mkdir(parents=True, exist_ok=False)
    m = run['mapping']; ndx = directory/'selection.ndx'
    ndx.write_text('[ Q01_backbone_and_methyl_H ]\n'+' '.join(map(str, m['atom_indices']))+'\n')
    cmd = ['/opt/homebrew/bin/gmx', 'traj', '-f', str(workspace/run['xtc']), '-s', str(workspace/run['gro']),
           '-n', str(ndx), '-b', '20000', '-e', '1020000', '-nocom', '-nopbc', '-nonojump', '-fp',
           '-ox', str(directory/'coordinates_nm.xvg'), '-ob', str(directory/'box_nm.xvg'), '-xvg', 'none']
    save(directory/'command.json', {'command': cmd, 'stdin': '0\n', 'cwd': str(directory),
                                  'coordinate_policy': 'source fitBB coordinates unchanged; no COM/make-whole/nojump'})
    process = subprocess.run(cmd, input='0\n', text=True, capture_output=True, cwd=directory, timeout=60)
    (directory/'stdout.txt').write_text(process.stdout); (directory/'stderr.txt').write_text(process.stderr)
    if process.returncode:
        raise ValueError('GROMACS_EXTRACTION_REJECTED:'+run['name'])
    coords = np.loadtxt(directory/'coordinates_nm.xvg'); b = np.loadtxt(directory/'box_nm.xvg')
    if coords.shape != (1001, 1+3*len(m['atom_indices'])) or b.shape != (1001, 7):
        raise ValueError('EXTRACTED_SOURCE_AXIS_OR_BOX_SHAPE')
    if not np.array_equal(coords[:, 0], np.arange(20000, 1020001, 1000)) or not np.array_equal(coords[:, 0], b[:, 0]):
        raise ValueError('EXTRACTED_TIME_AXIS')
    xyz = coords[:, 1:].reshape(1001, -1, 3); box = np.zeros((1001, 3, 3))
    # gmx_traj.cpp v2025.1 writes XX/XX,YY/YY,ZZ/ZZ,YY/XX,ZZ/XX,ZZ/YY.
    box[:, 0, 0], box[:, 1, 1], box[:, 2, 2] = b[:, 1], b[:, 2], b[:, 3]
    box[:, 1, 0], box[:, 2, 0], box[:, 2, 1] = b[:, 4], b[:, 5], b[:, 6]
    delta = np.stack([xyz[:, pair[0]].mean(axis=1)-xyz[:, pair[1]].mean(axis=1) for pair in m['contacts']], axis=1)
    distances = q.minimum_image(delta, box)*10.
    if not np.all(np.isfinite(xyz)):
        raise ValueError('NONFINITE_COORDINATES')
    # Contiguity is checked without modifying deposited molecules.
    for side in (side for pair in m['contacts'] for side in pair):
        if np.max(np.linalg.norm(xyz[:, side]-xyz[:, side].mean(axis=1, keepdims=True), axis=2)) > .3:
            raise ValueError('SPLIT_METHYL_GROUP')
    save(directory/'mapping.json', m)
    np.savez_compressed(directory/'coordinates.npz', xyz_nm=xyz, box_nm=box, time_ns=coords[:, 0]/1000)
    # Independent archived pseudo-COM series check for every source trajectory.
    acquisition, _ = paths(workspace); family, short = run['name'].split('_')[:2]
    errors = {}
    uniform = q.scores(distances, contacts, q.METHODS[0])
    for state, folder in [('open', 'GS'), ('closed', 'ES')]:
        stored_path = acquisition/'data/contract/MD/ANALYSE'/family/'VIOLATION'/folder/short/'avg_up_violations_time.dat'
        stored = np.loadtxt(stored_path)
        if stored.shape[0] != 1001 or not np.array_equal(stored[:, 0], np.arange(1, 1002)):
            raise ValueError('ARCHIVED_SCORE_TIME_AXIS')
        errors[state] = float(np.max(abs(uniform[state]-stored[:, 2])))
    if any(v > .011 for v in errors.values()):
        save(directory/'parity_failure.json', errors)
        raise ValueError('SOURCE_PARITY_METHOD_GAP:'+run['name'])
    save(directory/'admission.json', {'source_score_parity_max_A': errors, 'status': 'PASS', 'frames': 1001,
                                    'atoms': len(m['atom_indices']), 'coordinate_atom_count': run['atom_count']})
    return xyz, distances, coords[:, 0]/1000, errors


def run(workspace, out):
    facts = json.loads((out/'facts.json').read_text()); method = json.loads((out/'frozen_method.json').read_text())
    inventory = json.loads((out/'input_inventory.json').read_text()); contacts = json.loads((out/'contacts.json').read_text())
    runs = json.loads((out/'trajectory_mapping.json').read_text()); calibration = method['calibration']
    if q.identity(method) != facts['method_id'] or q.identity(inventory) != facts['input_id'] or contacts != method['contacts']:
        raise ValueError('FROZEN_INPUT_OR_METHOD_MUTATED')
    for row in inventory:
        if digest(workspace/row['path']) != row['sha256']:
            raise ValueError('SOURCE_FILE_CHANGED:'+row['path'])
    ref = np.load(out/'reference_coordinates.npz', allow_pickle=False)
    if binding.reference_identity(ref, contacts) != method.get('reference_id'):
        raise ValueError('REFERENCE_CHANGED_SINCE_PREPARATION')
    before = q.evaluate(facts); off = q.evaluate(facts, enabled=False)
    save(out/'rules_before.json', before); save(out/'rules_off.json', off)
    calls = []; records = {}; parities = {}
    def operator(request):
        calls.append(request); save(out/'operator_dispatch.json', {'started_at': now(), 'request': request})
        for entry in runs:
            xyz, distances, time, errors = extract(workspace, out, entry, contacts)
            m = entry['mapping']
            geometry = {s: q.nearest_lid_rmsd(xyz[:, m['core']]*10, xyz[:, m['lid']]*10, ref[s+'_core'], ref[s+'_lid']) for s in q.STATES}
            record = {'seed': entry['seed'], 'time_ns': time, 'distances_A': distances, 'geometry_A': geometry}
            records[entry['name']] = record; parities[entry['name']] = errors
            np.savez_compressed(out/'trajectories'/entry['name']/'measurements.npz', time_ns=time, distances_A=distances, open_rmsd_A=geometry['open'], closed_rmsd_A=geometry['closed'])
            print('admitted', entry['name'], errors, flush=True)
        measurement = binding.measurement_manifest(records, contacts, ref, runs, facts)
        save(out/'measurement_manifest.json', measurement)
        report, labels = q.summarize(records, contacts, calibration)
        save(out/'numerical_report.json', report)
        with (out/'full_paths.tsv').open('w', newline='') as f:
            writer = csv.writer(f, delimiter='\t')
            writer.writerow(['trajectory', 'seed', 'time_ns', 'open_lid_rmsd_A', 'closed_lid_rmsd_A', 'uniform_open_A', 'uniform_closed_A', 'SI_open_A', 'SI_closed_A', 'uniform_support', 'SI_support'])
            for name, r in records.items():
                s1, s2 = [q.scores(r['distances_A'], contacts, m) for m in q.METHODS]
                for i, time in enumerate(r['time_ns']):
                    writer.writerow([name, r['seed'], time, r['geometry_A']['open'][i], r['geometry_A']['closed'][i], s1['open'][i], s1['closed'][i], s2['open'][i], s2['closed'][i], labels[name][q.METHODS[0]][i], labels[name][q.METHODS[1]][i]])
        result = dict(request, report_path='numerical_report.json', evidence_type='ACTUAL_COORDINATE_PATH_COMPARISON',
                      completed_at=now(), report_id=q.identity(report), measurement_manifest_id=measurement['manifest_id'])
        save(out/'evidence_result.json', result); return result
    q.dispatch(off, operator)
    if calls:
        raise ValueError('OFF_DISPATCHED')
    evidence = q.dispatch(before, operator)[0]
    def verify(value):
        # Recompute numerical classification from the actual distances/RMSD, not a declared status.
        report, _ = q.summarize(records, contacts, calibration)
        if q.identity(report) != value['report_id']:
            raise ValueError('NUMERICAL_REPORT_MISMATCH')
        return report
    after = q.evaluate(facts, evidence, verify_evidence=verify)
    save(out/'rules_after.json', after)
    receipt = {'completed_at': now(), 'status': after['status'], 'instance_id': after['instance_id'],
               'on_operator_calls': len(calls), 'off_operator_calls': 0, 'new_gmx_calls': 40,
               'new_optimizations': 0, 'trajectories_admitted': len(records),
               'max_uniform_source_parity_A': max(v for r in parities.values() for v in r.values()),
               'scientific_status': after['scientific_status'], 'accuracy_gain_claimed': False,
               'full_question_answer': False, 'original_rules_baseline_changed': False,
               'manual_canary_reclassified_as_extra': False, 'method_id': facts['method_id'], 'input_id': facts['input_id']}
    save(out/'receipt.json', receipt); print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--phase', choices=['prepare', 'run'], required=True)
    args = parser.parse_args()
    globals()[args.phase](args.workspace.resolve(), args.output.resolve())
