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
                            'checked': {'objective': .9, 'numerical_status': 'PASS', 'candidate_id': 'new', 'parameters': [.9]}}]}
        evidence = {k: req[k] for k in ('request_id', 'input_id', 'rule_instance_id', 'base_result_id')}
        evidence['report_id'] = c.a.q.digest(report)
        after = c.evaluate(previous, evidence, lambda _: report)
        self.assertEqual(after['method_obligations'][0]['status'], 'CONDITIONAL_NUMERICAL_CANDIDATE_AVAILABLE')
        self.assertEqual(after['comparison'], previous['comparison'])
        self.assertFalse(after['complete_question_answer'])
        self.assertEqual(c.request(after)['selected'], [])
        calls = []
        c.dispatch(c.evaluate(after), after, calls.append)
        self.assertEqual(calls, [])
        self.assertEqual(after['method_evidence'], previous['method_evidence'])
        report['runs'][0]['checked'].update(numerical_status='NUMERICAL_STOP_WITH_FEASIBLE_POINT')
        evidence['report_id'] = c.a.q.digest(report)
        stopped = c.evaluate(previous, evidence, lambda _: report)
        self.assertEqual(c.request(stopped)['selected'], [{'reference': 'one', 'owners': ['A'],
                         'parent_candidate_id': 'new', 'initial': [.9]}])
        c.dispatch(c.evaluate(stopped, enabled=False), stopped, calls.append)
        self.assertEqual(calls, [])
        report['runs'][0]['checked'].update(objective=1.1, numerical_status='PASS')
        evidence['report_id'] = c.a.q.digest(report)
        after = c.evaluate(previous, evidence, lambda _: report)
        self.assertEqual(after['method_obligations'][0]['status'], 'LOWER_FEASIBLE_CANDIDATE_REQUIRES_CONTINUATION')
        self.assertEqual(c.evaluate(previous, dict(evidence, input_id='bad'), lambda _: report)['targeted_continuation'], 'EVIDENCE_REJECTED')



class FileReplayTests(unittest.TestCase):
    previous = ContinuationTests.previous
    def advance(self, previous, value, status):
        req = c.request(previous)
        report = {'request_id': req['request_id'], 'optimizer_calls': 1,
                  'runs': [{'reference': 'one', 'parent_candidate_id': req['selected'][0]['parent_candidate_id'],
                            'checked': {'objective': value, 'parameters': [value],
                                        'numerical_status': status, 'candidate_id': str(value)}}]}
        evidence = {k: req[k] for k in ('request_id', 'input_id', 'rule_instance_id', 'base_result_id')}
        evidence['report_id'] = c.a.q.digest(report)
        after = c.evaluate(previous, evidence, lambda _: report)
        return after, c.evidence_anchor(after, evidence)

    def test_earlier_history_mutation_rejected_even_when_latest_is_unchanged(self):
        first, _ = self.advance(self.previous(), .9, 'NUMERICAL_STOP_WITH_FEASIBLE_POINT')
        after, anchor = self.advance(first, .8, 'PASS')
        c.verify_saved_history(after, anchor)
        after['targeted_numerical_history'][0]['runs'][0]['checked']['parameters'] = [.7]
        with self.assertRaisesRegex(ValueError, 'CONSUMED_HISTORY_ARTIFACT_CHANGED'):
            c.verify_saved_history(after, anchor)
        first['targeted_numerical_history'][-1]['runs'][0]['checked']['numerical_status'] = 'PASS'
        with self.assertRaisesRegex(ValueError, 'LATEST_REPORT_HISTORY_MISMATCH'):
            c.request(first)

    def test_two_consecutive_zero_cli_runs_preserve_existing_evidence(self):
        import importlib.util
        import json
        import tempfile
        from pathlib import Path
        from types import SimpleNamespace
        from unittest.mock import patch
        spec = importlib.util.spec_from_file_location('q09_cli_replay_test',
            Path(__file__).resolve().parents[1]/'scripts/run_q09_targeted_continuation_v1.py')
        cli = importlib.util.module_from_spec(spec); spec.loader.exec_module(cli)
        original = self.previous(); after, anchor = self.advance(original, .9, 'PASS')
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); manual = root/'outputs/q09_method_evidence_v1'; manual.mkdir(parents=True)
            (manual/'evidence_result.json').write_text(json.dumps({'report_id': c.a.q.digest(original['method_evidence'])}))
            last = root/'initial'; last.mkdir()
            (last/'rules_after.json').write_text(json.dumps(after)); (last/'evidence_result.json').write_text(json.dumps(anchor))
            with patch.object(cli.a, 'GlobalData', return_value=SimpleNamespace(input_id='input')), patch.object(cli.a, 'optimize_local', side_effect=AssertionError('NO_REAL_FITS')) as fit:
                for name in ['zero1', 'zero2']:
                    out = root/name
                    with patch('sys.argv', ['runner', '--task-root', str(root), '--output', str(out), '--previous-result', str(last/'rules_after.json')]):
                        cli.main()
                    self.assertEqual(json.loads((out/'receipt.json').read_text())['optimizer_calls'], 0)
                    self.assertEqual(json.loads((out/'evidence_result.json').read_text()), anchor)
                    last = out
                fit.assert_not_called()

    def test_manual_descendant_changes_action_without_optimizer_credit(self):
        previous = self.previous()
        report = {'request_id': 'manual', 'input_id': 'input', 'rule_instance_id': 'same',
                  'base_result_id': c.a.q.digest(previous), 'optimizer_calls': 0, 'new_rules_extra': 0,
                  'provenance': 'MANUAL_BACKGROUND_DERIVED_FIXED_POINT_VERIFIED',
                  'runs': [{'reference': 'one', 'parent_candidate_id': 'stopped',
                            'checked': {'objective': .9, 'parameters': [.9], 'numerical_status': 'PASS', 'candidate_id': 'manual-new'}}]}
        evidence = {k: report[k] for k in ('request_id','input_id','rule_instance_id','base_result_id')}
        evidence['report_id'] = c.a.q.digest(report)
        calls = []
        verify = lambda _: (calls.append(True) or report)
        off = c.consume_manual_derived(previous, evidence, verify, enabled=False)
        self.assertEqual(calls, [])
        self.assertEqual(c.request(off)['selected'][0]['parent_candidate_id'], 'stopped')
        after = c.consume_manual_derived(previous, evidence, verify)
        self.assertEqual(c.request(after)['selected'], [])
        self.assertEqual(after['method_evidence'], previous['method_evidence'])
        self.assertFalse(after['complete_question_answer'])
        c.verify_saved_history(after, c.evidence_anchor(after, evidence))
        report['new_rules_extra'] = 1
        with self.assertRaisesRegex(ValueError, 'MANUAL_WORK_CANNOT_RECEIVE_OPERATOR_CREDIT'):
            c.consume_manual_derived(previous, evidence, verify)

if __name__ == '__main__': unittest.main()
