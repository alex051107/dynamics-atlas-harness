"""Materialize an answer from the already verified full40 evidence, no new science run."""
import argparse
import datetime
import json
from pathlib import Path
from dynamics_atlas_harness import q01_absolute_paths_v1 as a
from dynamics_atlas_harness import q01_path_comparison_v1 as q


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--absolute-output', type=Path, required=True)
    parser.add_argument('--review-directory', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args(); parent = args.absolute_output.resolve(); out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=False)
    def read(root, name): return json.loads((root/name).read_text())
    def save(name, value): (out/name).write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False)+'\n')
    previous = read(parent, 'rules_after.json'); report = read(parent, 'numerical_report.json')
    method = read(parent, 'frozen_method.json'); evidence = read(parent, 'evidence_result.json')
    relative = read(parent, 'verified_relative_instance.json'); receipt = read(parent, 'receipt.json')
    if previous['numerical_evidence'] != report or q.identity(report) != evidence['report_id'] or receipt['measurement_manifest_id'] != evidence['measurement_manifest_id']:
        raise ValueError('PREVIOUSLY_VERIFIED_ABSOLUTE_EVIDENCE_CHANGED')
    # This is a reducer over a prior verified snapshot; no geometry replay is claimed.
    after = a.evaluate(relative, method, evidence, lambda _: report)
    if after['status'] != 'ABSOLUTE_PATHS_AND_CONTACT_DECOMPOSITION_EVALUATED':
        raise ValueError('ANSWER_EVIDENCE_REJECTED')
    review = read(args.review_directory, 'capture_receipt.json')
    if review['complete'] is not True or review['reviewer'] != 'ChatGPT 6 Pro' or review['reviewed_head'] != '1fbb417113b01952678eec9d0f02a240524cc95e':
        raise ValueError('REVIEW_SCOPE_OR_IDENTITY_MISMATCH')
    answer = after['question_level_answer']
    record = {'question_id': 'Q01', 'original_question_preserved': True,
        'development_answer_status': 'COMPLETE_FINITE_TIME_ANSWER_WITH_NAMED_EXTERNAL_AI_SCIENCE_REVIEW',
        'answer_id': q.identity(answer), 'report_id': q.identity(report),
        'rule_instance_id': after['instance_id'], 'measurement_manifest_id': evidence['measurement_manifest_id'],
        'method_id': evidence['method_id'], 'named_review': review,
        'review_scope': 'Pro16 accepted the bounded scientific content at its reviewed head; this new evidence-dependent reducer is a subsequent code change, tested locally and pending next review.',
        'source_science_review_status': 'PENDING_DOMAIN_REVIEW', 'human_final_authority': True,
        'human_final_approval_recorded': False, 'development_question_content_completed': True,
        'heldout_accuracy': 'NOT_MEASURED', 'incremental_Rules_accuracy': 'NOT_ESTABLISHED',
        'completed_at': datetime.datetime.now(datetime.timezone.utc).isoformat()}
    save('question_answer.json', answer); save('rules_after_with_question_answer.json', after)
    save('named_review_and_development_completion.json', record)
    save('receipt.json', {'status': 'EVIDENCE_DEPENDENT_QUESTION_ANSWER_MATERIALIZED',
        'instance_id': after['instance_id'], 'same_instance': after['instance_id'] == previous['instance_id'],
        'new_operator_calls': 0, 'new_trajectory_calculations': 0, 'new_fits': 0,
        'prior_verified_snapshot_checked': True, 'geometric_recomputation_claimed': False,
        'human_final_approval_recorded': False})
    print(json.dumps({'status': record['development_answer_status'], 'evidence_disposition': answer['evidence_disposition'], 'human_approval': False}, indent=2))


if __name__ == '__main__': main()
