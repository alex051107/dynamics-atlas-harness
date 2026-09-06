import copy
import unittest
from dynamics_atlas_harness import q09_method_evidence_v1 as m


class MethodEvidenceTests(unittest.TestCase):
    def test_candidate_checks_objective_gradient_and_false_success(self):
        objective = lambda p: (p[0]-.3)**2
        row = {'parameters': [.3], 'objective': 0., 'projected_gradient_inf': 0.,
               'numerical_status': 'PASS', 'optimizer_success': True}
        self.assertEqual(m.check_candidate(row, [(0., 1.)], objective)['numerical_status'], 'PASS')
        for key, value in [('parameters', [2.]), ('objective', .1), ('projected_gradient_inf', .2), ('optimizer_success', False)]:
            changed = dict(row, **{key: value})
            with self.assertRaises(ValueError): m.check_candidate(changed, [(0., 1.)], objective)

    def test_lower_unfinished_point_is_not_hidden_by_a_stationary_candidate(self):
        rows = [{'objective': 2., 'numerical_status': 'PASS', 'candidate_id': 'stationary'},
                {'objective': 1., 'numerical_status': 'NUMERICAL_STOP_WITH_FEASIBLE_POINT', 'candidate_id': 'lower'}]
        result = m.group_disposition('D0_01', ['19-119', '19-132'], rows)
        self.assertEqual(result['status'], 'LOWER_FEASIBLE_CANDIDATE_REQUIRES_CONTINUATION')
        self.assertEqual(result['best_candidate_id'], 'lower')
        rows[0]['numerical_status'] = 'NUMERICAL_STOP_WITH_FEASIBLE_POINT'
        self.assertEqual(m.group_disposition('D0_24', ['70-119', '70-132'], rows)['stationary_candidates'], 0)

    def fixture(self):
        base = {'rule_instance_id': m.a.RULE_ID+'::CASE::q09_t4l_state_number_20260905',
                'request_id': 'base_request', 'comparison': {'scientific': 'UNRESOLVED'},
                'reason_codes': ['SOLVER_COMPARISON_INCOMPLETE', 'DONOR_AND_INSTRUMENT_ADEQUACY_NOT_ESTABLISHED'],
                'status': 'UNRESOLVED', 'complete_question_answer': False}
        report = {'policy': copy.deepcopy(m.POLICY), 'input_id': 'source', 'provenance': m.PROVENANCE,
                  'optimizer_calls': 0, 'new_rules_extra_calculations': 0, 'complete_question_answer': False,
                  'group_dispositions': [{'reference': 'D0_01', 'next_action': 'continue'}],
                  'response_transfer': {'status': 'COMMON_RESPONSE_TRANSFER_REQUIRES_CALIBRATION'}}
        evidence = {'input_id': 'source', 'base_result_id': m.a.q.digest(base),
                    'rule_instance_id': base['rule_instance_id'], 'report_id': m.a.q.digest(report)}
        return base, report, evidence

    def test_manual_evidence_changes_method_actions_without_extra_credit_or_science_upgrade(self):
        base, report, evidence = self.fixture(); original = copy.deepcopy(base)
        after = m.consume(base, 'source', evidence, lambda _: report)
        self.assertEqual(base, original)
        self.assertEqual(after['comparison'], base['comparison'])
        self.assertEqual(after['rule_instance_id'], base['rule_instance_id'])
        self.assertEqual(after['method_obligations'][0]['next_action'], 'continue')
        self.assertFalse(after['complete_question_answer'])
        self.assertNotIn('DONOR_AND_INSTRUMENT_ADEQUACY_NOT_ESTABLISHED', after['reason_codes'])
        called = []
        off = m.consume(base, 'source', evidence, lambda _: called.append(1), enabled=False)
        self.assertEqual(called, [])
        self.assertEqual(off['reason_codes'], base['reason_codes'])

    def test_changed_or_unverified_evidence_keeps_method_obligation(self):
        base, report, evidence = self.fixture()
        for key, value in [('input_id', 'other'), ('base_result_id', 'other'), ('report_id', 'other')]:
            out = m.consume(base, 'source', dict(evidence, **{key: value}), lambda _: report)
            self.assertEqual(out['method_evidence_application'], 'REJECTED')
            self.assertEqual(len(out['method_obligations']), 1)
        self.assertEqual(m.consume(base, 'source', evidence)['method_evidence_application'], 'REJECTED')
        for key, value in [('provenance', 'RULE_TRIGGERED'), ('new_rules_extra_calculations', 36), ('complete_question_answer', True)]:
            changed = dict(report, **{key: value}); ev = dict(evidence, report_id=m.a.q.digest(changed))
            self.assertEqual(m.consume(base, 'source', ev, lambda _: changed)['method_evidence_application'], 'REJECTED')

    def test_window_and_method_mutation_rejected_before_source_consumption(self):
        response = {'method': dict(m.RESPONSE_METHOD, window='widened')}
        with self.assertRaisesRegex(ValueError, 'MANUAL_IRF_METHOD_CHANGED'):
            m.verify_diagnostics(None, response, {}, {'method': m.SOURCE_ORDER_METHOD}, {}, {})


if __name__ == '__main__': unittest.main()
