import copy
import unittest
from dynamics_atlas_harness import q09_targeted_continuation_v1 as c
from dynamics_atlas_harness import q09_method_evidence_v1 as m


class ContinuationTests(unittest.TestCase):
    def previous(self):
        groups = {'one': {'owners': ['A'], 'candidates': [
                  {'objective': 2., 'candidate_id': 'passed', 'numerical_status': 'PASS', 'parameters': [2.]},
                  {'objective': 1., 'candidate_id': 'stopped', 'numerical_status': 'NUMERICAL_STOP_WITH_FEASIBLE_POINT', 'parameters': [1.]}]},
                  'two': {'owners': ['B'], 'candidates': [
                  {'objective': .5, 'candidate_id': 'ok', 'numerical_status': 'PASS', 'parameters': [.5]}]}}
        ds = [m.group_disposition(ref, row['owners'], row['candidates']) for ref, row in groups.items()]
        report = {'policy': copy.deepcopy(m.POLICY), 'provenance': m.PROVENANCE, 'input_id': 'input',
                  'group_dispositions': ds, 'source_order_groups': groups}
        return {'rule_instance_id': 'same', 'method_evidence_application': 'VERIFIED_MANUAL_DIAGNOSTICS_CONSUMED',
                'method_evidence': report, 'method_obligations': [dict(row, kind='DONOR_GROUP_NEXT_ACTION') for row in ds],
                'complete_question_answer': False, 'comparison': {'old': 'preserved'}}

    def test_only_unfinished_lower_candidates_dispatch_and_off_has_zero_calls(self):
        previous = self.previous(); before = c.evaluate(previous)
        req = before['targeted_operator_obligations'][0]
        self.assertEqual([r['parent_candidate_id'] for r in req['selected']], ['stopped'])
        calls = []
        self.assertEqual(c.dispatch(c.evaluate(previous, enabled=False), previous, calls.append), [])
        self.assertEqual(calls, [])
        c.dispatch(before, previous, calls.append)
        self.assertEqual(len(calls), 1)
        changed = copy.deepcopy(before); changed['targeted_operator_obligations'][0]['selected'][0]['initial'] = [3.]
        with self.assertRaises(ValueError): c.dispatch(changed, previous, calls.append)

    def test_changed_disposition_cannot_select_other_candidates(self):
        previous = self.previous(); previous['method_evidence']['group_dispositions'][1]['status'] = 'NO_STATIONARY_CANDIDATE_REQUIRES_CONTINUATION'
        with self.assertRaises(ValueError): c.request(previous)

    def test_better_new_stationary_result_changes_only_its_method_action(self):
        previous = self.previous(); req = c.request(previous)
        report = {'request_id': req['request_id'], 'optimizer_calls': 1,
                  'runs': [{'reference': 'one', 'parent_candidate_id': 'stopped',
                            'checked': {'objective': .9, 'numerical_status': 'PASS', 'candidate_id': 'new'}}]}
        evidence = {k: req[k] for k in ('request_id', 'input_id', 'rule_instance_id', 'base_result_id')}
        evidence['report_id'] = c.a.q.digest(report)
        after = c.evaluate(previous, evidence, lambda _: report)
        self.assertEqual(after['method_obligations'][0]['status'], 'CONDITIONAL_NUMERICAL_CANDIDATE_AVAILABLE')
        self.assertEqual(after['comparison'], previous['comparison'])
        self.assertFalse(after['complete_question_answer'])
        report['runs'][0]['checked'].update(objective=1.1, numerical_status='PASS')
        evidence['report_id'] = c.a.q.digest(report)
        after = c.evaluate(previous, evidence, lambda _: report)
        self.assertEqual(after['method_obligations'][0]['status'], 'LOWER_FEASIBLE_CANDIDATE_REQUIRES_CONTINUATION')
        self.assertEqual(c.evaluate(previous, dict(evidence, input_id='bad'), lambda _: report)['targeted_continuation'], 'EVIDENCE_REJECTED')


if __name__ == '__main__': unittest.main()
