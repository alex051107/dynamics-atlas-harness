"""Explicit Q09 file mapping and analytic method checks, no fitted parameters."""
from pathlib import Path
from collections import defaultdict
import json
import math
import re

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'inputs/q09_author/unpacked/eTCSPC'
OUT = ROOT / 'outputs/q09_method_admission_v1'


def main():
    mappings = []
    same_bytes = {role: defaultdict(list) for role in ('DA', 'D0', 'IRF_DA', 'IRF_D0')}
    for folder in sorted(DATA.iterdir()):
        meta = next(folder.glob('*.yml'))
        text = meta.read_text()
        sample_name = re.search(r'^    Name: (.+)$', text, re.M).group(1)
        records = []
        for role in ('DA', 'D0'):
            candidates = list(folder.glob(f'{folder.name}_{role}.*'))
            assert len(candidates) == 1
            decay = candidates[0]
            is_ibh = decay.suffix == '.txt'
            irf_name = f'IRF_{role}{decay.suffix}'
            exception = None
            if folder.name == '19-86' and role == 'D0':
                irf_name = 'IRF_Do.txt'
                exception = 'Explicit candidate alias: metadataIRF_D0.txt versus sole IBH IRF_Do.txt; original unchanged'
            elif folder.name == '19-86' and role == 'DA':
                exception = 'Explicit candidate alias: metadataIRF_DA.txt versus sole PQ IRF_DA.dat; original unchanged'
            irf = folder / irf_name
            lin = folder / f'Linearization_{role}.txt' if is_ibh else None
            assert irf.is_file() and (lin is None or lin.is_file())
            records.append({'role': role, 'decay': str(decay.relative_to(DATA)),
                            'irf': str(irf.relative_to(DATA)),
                            'linearization': str(lin.relative_to(DATA)) if lin else None,
                            'instrument': 'IBH' if is_ibh else 'PQ',
                            'bin_width_ns': 0.0141 if is_ibh else 0.008,
                            'time_origin_convention': 'first stored bin zero; fitted IRF shift remains unspecified',
                            'original_irf_reference_exception': exception,
                            'mapping_status': 'EXPLICIT_CONDITIONAL_MAPPING' if exception else 'EXACT_FILE_ROLE_MAPPING',
                            'authority': 'per-variant metadata + filename + observed file format; SI57 timing'})
            for label, path in [(role, decay), ('IRF_' + role, irf)]:
                same_bytes[label][path.read_bytes()].append(str(path.relative_to(DATA)))
        mappings.append({'variant': folder.name, 'sample_name': sample_name,
                         'metadata': str(meta.relative_to(DATA)), 'datasets': records,
                         'original_metadata_preserved': True,
                         'sample_identity_rule': 'Sample.Name + dataset description + actual decay filenames; conflicting top-level Measurement ID not silently trusted'})
    repeated = {role: [files for files in groups.values() if len(files) > 1]
                for role, groups in same_bytes.items()}
    # Eq33 already includes intrinsic donor decay. In Eq34 kRET tends to zero
    # at infinite distance; printed Eq36 nevertheless retains kappa2*kF.
    kappa2, kf, t = 2 / 3, 0.224, 10.0
    printed_survival = math.exp(-t * kappa2 * kf)
    physical_zero_fret_survival = 1.0
    assert printed_survival < 0.23 and physical_zero_fret_survival == 1
    # Eq37 exp(-2*(r-mu)^2/w^2) corresponds to sigma=w/2, not sigma=w.
    limiting = {'kind': 'ANALYTIC_LIMIT_NOT_Q09_FIT', 'source': 'OriginalSI58 Eq33,34,36;SI59 Eq37',
                'time_ns': t, 'kappa_squared': kappa2, 'radiative_rate_per_ns': kf,
                'zero_fret_limit_expected_survival': physical_zero_fret_survival,
                'printed_eq36_zero_fret_survival': printed_survival,
                'printed_eq36_extra_rate_per_ns': kappa2 * kf,
                'eq37_width_A': 12.0, 'eq37_gaussian_sigma_A': 6.0,
                'verdict': 'PRINTED_FORMULA_CONSISTENCY_GAP; author executed code unknown',
                'candidate_correction': 'Use exp(-t*kRET) for FRET-only survival fromEq34; requires independent scientific review before scientific fitting',
                'scientific_fits': 0}
    summary = {'variant_count': len(mappings), 'decay_role_records': sum(len(m['datasets']) for m in mappings),
               'unique_byte_payload_counts': {role: len(groups) for role, groups in same_bytes.items()},
               'repeated_reference_policy': 'Byte-identical records provide no independent acquisition identity evidence; retain originals and resolve joint likelihood multiplicity from source provenance',
               'formula_status': limiting['verdict'], 'fits': 0, 'rules_runs': 0}
    for name, value in [('dataset_mapping.json', mappings), ('byte_identical_groups.json', repeated),
                        ('limiting_case.json', limiting), ('summary.json', summary)]:
        (OUT / name).write_text(json.dumps(value, indent=2) + '\n')
    (OUT / 'mapping_source.py').write_text(Path(__file__).read_text())
    print(json.dumps({'summary': summary, 'limiting': limiting}, indent=2))


if __name__ == '__main__':
    main()
