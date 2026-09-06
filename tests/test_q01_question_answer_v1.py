import copy
import json
from pathlib import Path
import unittest
from dynamics_atlas_harness import q01_absolute_paths_v1 as a


class QuestionAnswerTests(unittest.TestCase):
    def setUp(self):
        self.report = json.loads((Path(__file__).resolve().parents[1]/'research/paper_result_reproduction_screen_v1/q01_absolute_paths_v1/numerical_report.json').read_text())

    def test_actual_answer_and_reverse_group_evidence_do_not_produce_same_direction(self):
        original = a.question_answer(self.report)
        self.assertEqual(original['group_movement_direction'], 'CLOSED_GREATER')
        self.assertEqual(original['evidence_disposition'], 'SUPPORT_WITHIN_CEILING')
        changed = copy.deepcopy(self.report)
        for row in changed['rows']:
            row['absolute_metrics']['lid_displacement_from_20ns_A']['first20_to_last20']['after_median'] = 2. if row['seed_group'] == 'closed' else 10.
        changed['uncertainty']['observed_A'] = -8.
        changed['uncertainty']['conditional_bootstrap_percentile_95_A'] = [-9., -7.]
        answer = a.question_answer(changed)
        self.assertEqual(answer['group_movement_direction'], 'OPEN_GREATER')
        self.assertEqual(answer['evidence_disposition'], 'CANNOT_SUPPORT_REQUESTED_CLAIM')
        self.assertIn('open-seeded paths have greater', answer['answer'])
        self.assertEqual(answer['source_science_review_status'], 'PENDING_DOMAIN_REVIEW')

    def test_relative_events_farther_from_both_references_are_not_absolute_approach(self):
        for row in self.report['rows']:
            if row['seed_group'] == 'closed':
                for state in ('open', 'closed'):
                    row['absolute_metrics'][state+'_reference_lid_rmsd_A']['first20_to_last20']['delta'] = 2.
        answer = a.question_answer(self.report)
        self.assertEqual(answer['evidence_disposition'], 'CANNOT_SUPPORT_REQUESTED_CLAIM')
        for values in answer['directional_paths_by_method'].values():
            self.assertEqual(len(values['sustained_open_preference_trajectories']), 9)
            self.assertEqual(values['absolute_approach_open_and_leave_closed_trajectories'], [])

    def test_contact_disagreement_keeps_magnitude_and_no_event_is_not_support(self):
        answer = a.question_answer(self.report)
        es17 = next(r for r in answer['all_trajectory_answers'] if 'ES17' in r['trajectory'])
        counts = [v['events'][0]['internal_disagreement_samples'] for v in es17['methods'].values()]
        self.assertEqual(sorted(counts), [41, 42])
        self.assertTrue(es17['absolute_approach_open_and_leave_closed'])
        self.assertTrue(all(v['all_channels_agree_in_observed_primary_events'] is False for v in es17['methods'].values()))
        no_event = next(r for r in answer['all_trajectory_answers'] if r['seed_group'] == 'open')
        self.assertTrue(all(v['all_channels_agree_in_observed_primary_events'] is None for v in no_event['methods'].values()))
        self.assertFalse(answer['accuracy_gain_claimed'])
        self.assertTrue(answer['human_final_authority'])


if __name__ == '__main__': unittest.main()
