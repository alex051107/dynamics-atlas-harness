"""Render leak-checked Q15 P/PD snapshots for a direct-versus-Rules comparison.

The input manifest is the authority for what both paths may see.  This script
copies only its allowed numerical, source-role, and limitation fields into two
new packets; it never passes precomputed relation labels or answer prose to the
direct path.
"""
import argparse
import json
from pathlib import Path


FORBIDDEN_KEYS = {
    'fluorescence_relation', 'relation', 'allowed_conclusion', 'local_support',
    'histogram_answer', 'probe_answer', 'probe_readout_condition_dependence',
    'replacement_donor_reduces_observed_concern', 'question_answer_candidate',
    'scientific_synthesis', 'interpretation', 'closure', 'answer', 'direction',
}


def read(path):
    return json.loads(path.read_text())


def require_keys(value, keys, *, source):
    missing = set(keys) - set(value)
    if missing:
        raise ValueError(f'MISSING_REQUIRED_FIELDS:{source}:{sorted(missing)}')


def assert_no_forbidden_keys(value, *, path='root'):
    if isinstance(value, dict):
        overlap = FORBIDDEN_KEYS & set(value)
        if overlap:
            raise ValueError(f'ANSWER_BEARING_FIELD_LEAK:{path}:{sorted(overlap)}')
        for key, child in value.items():
            assert_no_forbidden_keys(child, path=f'{path}.{key}')
    elif isinstance(value, list):
        for index, child in enumerate(value):
            assert_no_forbidden_keys(child, path=f'{path}[{index}]')


def source(task_root, relative_path):
    path = task_root / 'outputs' / relative_path
    if not path.is_file():
        raise ValueError(f'MISSING_ADMITTED_SOURCE:{relative_path}')
    return read(path)


def build_snapshots(task_root):
    apbs = source(task_root, 'q15_apbs_comparison_v1/report.json')
    diagnostics = source(task_root, 'q15_pro19_verification_v1/report.json')
    cross = source(task_root, 'q15_pro20_admission_replay_v2/cross_modal_evidence.json')
    fret = source(task_root, 'q15_58_134_forward_bridge_v3/report.json')
    dye = source(task_root, 'q15_dye_response_v1/report.json')

    comparisons = apbs['condition_comparisons']
    require_keys(comparisons, {'55_175', '175_228'}, source='apbs comparisons')
    primary_apbs = {
        pair: {key: comparisons[pair][key] for key in [
            'holo_minus_apo_E', 'all_cross_repetition_difference_range',
            'uncertainty',
        ]}
        for pair in ['55_175', '175_228']
    }
    primary_diagnostics = {
        pair: {key: diagnostics['diagnostics'][pair][key] for key in [
            'equal_repetition_mean_effect', 'equal_repetition_median_effect',
            'leave_one_per_condition_effects', 'leave_one_per_condition_range',
            'fixed_selected_E_clipping_effect_bound',
        ]}
        for pair in ['55_175', '175_228']
    }

    raw_cross_rows = {row['pair']: row for row in cross['rows']}
    require_keys(raw_cross_rows, {'55_175', '175_228'}, source='cross-modal rows')
    primary_cross = [
        {key: raw_cross_rows[pair][key] for key in [
            'pair', 'observed_E_effect',
            'DEER_central_mean_change_source_axis_units',
            'author_forward_distance_changes_A',
        ]}
        for pair in ['55_175', '175_228']
    ]
    primary_fret = {
        'observed_change': fret['on']['numerical']['observed_change'],
        'reference_distance_change': fret['on']['numerical']['reference_distance_change'],
        'direction_checks': fret['on']['numerical']['direction_checks'],
        'conditional_assumptions': fret['on']['conditional_assumptions'],
        'claim_ceiling': fret['claim_ceiling'],
    }
    primary = {
        'snapshot_id': 'P_primary_comparisons',
        'evidence_ids': [
            'apbs_55_175_and_175_228', 'author_deer_and_forward_inputs',
            'fret_58_134',
        ],
        'question': 'What bounded HiSiaP structural interpretation, if any, is supported after substrate addition, and what limits follow from differing readouts?',
        'common_processing_contract': (
            'Use only the displayed observations, reference semantics, source-role facts, '
            'and limits. Analyze each labelled measurement pair separately; do not infer a pooled vote over sites.'
        ),
        'manual_provenance': {
            'apbs_and_cross_modal_values': 'PREVIOUS_MANUAL_NUMERICAL_CALCULATION_OR_SOURCE_INTAKE; not Rules credit',
            'fret_58_134': 'RULES_CONTROLLED_LOCAL_NUMERICAL_USE only for its saved F05R02 use; underlying APBS calculation remains manual',
        },
        'apbs_observations': primary_apbs,
        'apbs_direction_diagnostics': primary_diagnostics,
        'deer_and_author_forward_inputs': {
            'rows': primary_cross,
            'hypothesis': cross['hypothesis'],
            'limits': cross['limits'],
        },
        'fret_58_134': primary_fret,
        'claim_limits': [
            'No mean-efficiency to absolute-distance conversion.',
            'No common population inference across cryogenic DEER and fluorescence.',
            'No saturation, activity, unique mechanism, or full quantitative reproduction claim.',
        ],
    }
    comparison_keys = {'175_AF555', '58_AF555', '175_TMR'}
    require_keys(dye['results'], comparison_keys, source='dye comparisons')
    probe_followup = {
        name: dye['results'][name]['comparison'] for name in sorted(comparison_keys)
    }
    geometry = source(task_root, 'q15_tmr_histogram_intake_v1/source_geometry.local.json')
    concordance = source(task_root, 'q15_dye_response_v1/source_concordance_check.json')
    raw_histogram_geometry = {key: geometry[key] for key in [
        'role', 'source_pdf', 'physical_page', 'figure', 'variant', 'dye_pair',
        'frames', 'bins',
    ]}
    raw_trace_observations = {
        name: {condition: dye['results'][name][condition] for condition in ['apo', 'holo']}
        for name in sorted(comparison_keys)
    }
    pd = {
        **primary,
        'snapshot_id': 'PD_primary_plus_probe_dye',
        'evidence_ids': [
            *primary['evidence_ids'], 'probe_dye_time_windows',
            'published_histogram_geometry', 'source_concordance',
        ],
        'probe_dye_time_windows': {
            'comparison_values': probe_followup,
            'per_condition_windows': raw_trace_observations,
            'roles': dye['roles'],
            'uncertainty': dye['uncertainty'],
            'limits': dye['limits'],
        },
        'published_histogram_geometry': raw_histogram_geometry,
        'source_concordance': concordance,
    }
    assert_no_forbidden_keys(primary)
    assert_no_forbidden_keys(pd)
    return primary, pd


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--task-root', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    task_root = args.task_root.resolve()
    output = args.output.resolve()
    if output.exists():
        raise ValueError('OUTPUT_ALREADY_EXISTS')
    primary, primary_plus_probe = build_snapshots(task_root)
    output.mkdir(parents=True)
    for filename, packet in [
        ('P_primary_comparisons.json', primary),
        ('PD_primary_plus_probe_dye.json', primary_plus_probe),
    ]:
        (output / filename).write_text(json.dumps(packet, indent=2, allow_nan=False) + '\n')
    receipt = {
        'version': 'q15-same-evidence-packet/v2',
        'status': 'PACKETS_RENDERED_NO_ANSWER_GENERATED',
        'snapshots': ['P_primary_comparisons', 'PD_primary_plus_probe_dye'],
        'forbidden_key_check': 'PASS',
        'admission_anchors': [
            'research/paper_result_reproduction_screen_v1/q15_admitted_source_receipt_v2.json',
            'outputs/q15_question_answer_v3/admission.json',
            'outputs/q15_58_134_frozen_reuse_v3/producer_admission.json',
        ],
        'answer_generation': 'NOT_RUN',
        'numerical_reruns': 0,
        'rules_reruns': 0,
    }
    (output / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
