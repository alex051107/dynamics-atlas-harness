"""Inventory unmodified author decays and literal metadata references; no fitting.

Only the observed flat two-column formats are parsed. Metadata is inspected as
source text, not treated as a valid executable YAML configuration.
"""
from pathlib import Path
import csv
import json
import math
import re
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'inputs/q09_author/unpacked/eTCSPC'
OUT = ROOT / 'outputs/q09_decay_admission_v1'


def curve(path):
    lines = path.read_text().splitlines()
    ibh = lines[0].startswith('Item name:') and 'Chan\tData' in lines
    if ibh:
        start = lines.index('Chan\tData') + 1
        rows = lines[start:]
    else:
        rows = lines
    values = []
    for line in rows:
        if not line.strip():
            continue
        fields = line.split()
        if len(fields) != 2:
            raise ValueError(f'UNRECOGNIZED_ROW {path}: {line}')
        x, y = map(float, fields)
        if not math.isfinite(x) or not math.isfinite(y) or y < 0 or y != int(y):
            raise ValueError(f'INVALID_COUNT {path}')
        values.append((x, int(y)))
    if len(values) < 2:
        raise ValueError(f'EMPTY_CURVE {path}')
    steps = [b[0] - a[0] for a, b in zip(values, values[1:])]
    step = steps[0]
    if step <= 0 or not all(math.isclose(s, step, rel_tol=1e-7, abs_tol=1e-10) for s in steps):
        raise ValueError(f'NONUNIFORM_AXIS {path}')
    if ibh and not all(x == i + 1 for i, (x, _) in enumerate(values)):
        raise ValueError(f'NONSTANDARD_CHANNEL_INDEX {path}')
    return {'file': str(path.relative_to(SOURCE)),
            'format': 'IBH_CHANNEL_COUNTS' if ibh else 'NUMERIC_TIME_COUNTS',
            'bins': len(values), 'first_axis_value': values[0][0],
            'last_axis_value': values[-1][0], 'axis_step_as_stored': step,
            'axis_unit': 'channel' if ibh else 'ns_supported_by_setup_8ps',
            'counts_sum': sum(y for _, y in values),
            'maximum_count': max(y for _, y in values),
            'zero_bins': sum(y == 0 for _, y in values),
            'normalized_or_corrected': False}


def main():
    OUT.mkdir(exist_ok=True)
    if any(OUT.iterdir()):
        raise ValueError('REFUSE_TO_OVERWRITE_EXISTING_OUTPUT')
    curves = [curve(f) for f in sorted(SOURCE.rglob('*')) if f.suffix in ('.txt', '.dat')]
    variants = []
    for folder in sorted(SOURCE.iterdir()):
        metadata = list(folder.glob('*.yml'))
        if len(metadata) != 1:
            raise ValueError(f'METADATA_COUNT {folder}')
        text = metadata[0].read_text()
        measurement_section = text.split('Measurement datasets:', 1)[1].split('Setup parts:', 1)[0]
        references = []
        for line_no, line in enumerate(text.splitlines(), 1):
            match = re.match(r'\s+Filename:\s+(\S+)', line)
            if match:
                target = match[1]
                references.append({'literal': target, 'line': line_no,
                                   'exists_exactly': (folder / target).is_file()})
        ids = re.findall(r'^    (\S.*):\s*$', measurement_section, re.M)
        sample_id = re.search(r'^    Measurement ID: (.+)$', text.split('Measurement datasets:', 1)[0], re.M).group(1)
        variants.append({'variant_folder': folder.name,
                         'metadata_filename': metadata[0].name,
                         'metadata_name_matches_folder': metadata[0].stem == folder.name,
                         'sample_measurement_id': sample_id,
                         'sample_id_matches_exact_dataset_key': sample_id in ids,
                         'dataset_keys': ids,
                         'literal_references': references,
                         'setup_ids': re.findall(r'^        Setup ID: (.+)$', measurement_section, re.M),
                         'declared_resolution_ps': re.findall(r'Resolution \[ps\]: (\S+)', text),
                         'input_scope': 'FILE_FORMAT_AND_LITERAL_LINK_CHECK_ONLY'})
    summary = {'status': 'RAW_CURVES_PARSED_METHOD_AND_MAPPING_NOT_YET_ADMITTED',
               'variant_folders': len(variants), 'numeric_files': len(curves),
               'format_counts': dict(Counter(c['format'] for c in curves)),
               'bin_counts': dict(Counter(c['bins'] for c in curves)),
               'all_counts_finite_nonnegative_integers': True,
               'missing_literal_references': [dict(variant=v['variant_folder'], **r)
                   for v in variants for r in v['literal_references'] if not r['exists_exactly']],
               'metadata_filename_mismatches': [v['variant_folder'] for v in variants if not v['metadata_name_matches_folder']],
               'sample_dataset_key_mismatches': [v['variant_folder'] for v in variants if not v['sample_id_matches_exact_dataset_key']],
               'mixed_instrument_variants': [v['variant_folder'] for v in variants if len(set(v['setup_ids'])) > 1],
               'optimizer_runs': 0, 'rules_runs': 0, 'full_scientific_answers': 0,
               'not_admitted': ['Supplementary equations20,24-27 and Table5 model constraints',
                                'exact per-dataset IRF/linearization/time-axis mapping',
                                'fit window, nuisance parameters, distance-width constraints',
                                'predeclared model comparison and uncertainty evaluation']}
    with (OUT / 'curves.csv').open('w') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(curves[0]))
        writer.writeheader()
        writer.writerows(curves)
    for name, data in [('variants.json', variants), ('summary.json', summary)]:
        (OUT / name).write_text(json.dumps(data, indent=2) + '\n')
    (OUT / 'source_snapshot.py').write_text(Path(__file__).read_text())
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
