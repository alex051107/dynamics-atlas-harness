"""Replay submission events through the real runner with network and Docker mocked.

Does not rewrite old run artifacts or simulate a model's counterfactual reasoning.
"""
import contextlib
import copy
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from unittest.mock import patch

import agent_run as runner

TASK = Path(__file__).resolve().parents[1]
CLAIM = {'text': 'A retained scientific claim', 'type': 'conclusion', 'polarity': 'affirmative'}


def response(content=None, submission=None, input_tokens=100):
    message = {'role': 'assistant', 'content': content}
    if submission is not None:
        message['tool_calls'] = [{'id': 'submit_test', 'type': 'function', 'function': {'name': 'submit', 'arguments': json.dumps(submission)}}]
    return {'id': 'offline_fixture', 'choices': [{'message': message}], 'usage': {'prompt_tokens': input_tokens, 'completion_tokens': 20, 'cost': 0}}


def execute(responses, *, arm='C', facts=None, expire_after_submission=False):
    responses = copy.deepcopy(responses)
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        (root / 'runtime').mkdir()
        (root / 'outputs').mkdir()
        source = root / 'cases' / 'test'
        source.mkdir(parents=True)
        (root / 'runtime' / 'readiness.json').write_text('{"approved_for_development":true}')
        (source / 'QUESTION.txt').write_text('Offline submission fixture')
        (source / 'PUBLIC_FACTS.json').write_text(json.dumps(facts or []))

        def network(*args, **kwargs):
            if not responses:
                raise AssertionError('Unexpected extra model request in offline replay')
            return io.BytesIO(json.dumps(responses.pop(0)).encode())

        def clock():
            return 1501 if expire_after_submission and list((root / 'runs').glob('*/draft_1.json')) else 0

        with patch.object(runner, 'ROOT', root), patch.object(runner, 'credential', return_value='offline_dummy'), patch.object(sys, 'argv', ['agent_run', 'test', arm, '--image', 'offline']), patch.object(runner.urllib.request, 'urlopen', side_effect=network), patch.object(runner.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, 'offline', '')), patch.object(runner.time, 'monotonic', side_effect=clock), contextlib.redirect_stdout(io.StringIO()):
            runner.main()
        receipt_path = next((root / 'runs').glob('*/receipt.json'))
        run = receipt_path.parent
        return {'receipt': json.loads(receipt_path.read_text()), 'answer': (run / 'answer.md').read_text() if (run / 'answer.md').exists() else None, 'drafts': [json.loads(f.read_text()) for f in sorted(run.glob('draft_*.json'))], 'events': [json.loads(line) for line in (run / 'events.jsonl').read_text().splitlines()]}


def main():
    checks = []
    first = {'answer': 'The original evidence-based answer.', 'claims': [CLAIM]}
    result = execute([response(submission=first), response(content='Already submitted.')])
    assert result['answer'] == first['answer'] and result['drafts'][0]['claims'] == first['claims']
    assert result['receipt']['submissions'] == 1
    checks.append('ordinary confirmation preserves explicit answer and claims')

    shorter = {'answer': 'Shorter revision.', 'claims': [{'text': 'A changed claim'}]}
    result = execute([response(submission=first), response(submission=shorter)])
    assert result['answer'] == shorter['answer'] and result['receipt']['status'] == 'COMPLETE'
    assert result['drafts'][-1]['claims'] == shorter['claims']
    checks.append('explicit valid shorter revision replaces prior answer without quality ranking')

    invalid = [None, {'answer': '', 'claims': [CLAIM]}, {'answer': 'text', 'claims': []}, {'answer': 'text'}, {'answer': 'text', 'claims': [{}]}, {'answer': 'text', 'claims': ['invalid']}]
    # None uses a malformed JSON object, not an ordinary message.
    messages = [response(submission=first)]
    for payload in invalid:
        event = response(submission=payload if payload is not None else {})
        messages.append(event)
    messages.append(response(content='Done.'))
    result = execute(messages)
    assert result['answer'] == first['answer'] and len(result['drafts']) == 1
    rejected = [e['value'] for e in result['events'] if e['kind'] == 'submission_rejected']
    assert len(rejected) == len(invalid) and all(e['check_status'] == 'not_checked_invalid_submission' and e['previous_submission_preserved'] for e in rejected)
    checks.append('empty malformed or missing claim records preserve last valid result and do not pass a check')

    result = execute([response(submission=first, input_tokens=160001)])
    assert result['answer'] == first['answer'] and result['receipt']['status'] == 'TOKEN_LIMIT'
    result = execute([response(submission=first)], expire_after_submission=True)
    assert result['answer'] == first['answer'] and result['receipt']['status'] == 'RESOURCE_LIMIT'
    checks.append('token and wall-clock limits preserve answer while recording incomplete termination')

    unknown = {'answer': 'An explicit answer whose relation is not indexed.', 'claims': [dict(CLAIM, evidence_role='independent_validation', result_id='unknown', observation_subset='x', analysis_id='y')]}
    result = execute([response(submission=unknown), response(content='Done.')])
    scope = result['drafts'][0]['check_scope']
    assert scope['status'] == 'no_matching_public_relation' and scope['unverified_targets'] == 1
    assert scope['whole_answer_scientifically_validated'] is False
    checks.append('unmatched explicit target is unverified, never whole-answer pass')

    replays = []
    for run_id, arm in [('T4L_B_3ee1d874', 'B'), ('T4L_C_be4d6c40', 'C')]:
        old_run = TASK / 'runs' / run_id
        events = [json.loads(line) for line in (old_run / 'events.jsonl').read_text().splitlines()]
        responses = [event['value'] for event in events if event['kind'] == 'response'][-2:]
        result = execute(responses, arm=arm, facts=json.loads((TASK / 'cases' / 'T4L' / 'PUBLIC_FACTS.json').read_text()))
        old_draft = json.loads((old_run / 'draft_1.json').read_text())
        assert result['answer'] == old_draft['answer']
        assert result['drafts'][0]['claims'] == old_draft['claims']
        assert result['receipt']['status'] == 'SUBMITTED_NO_EXPLICIT_REVISION'
        replays.append({'run_id': run_id, 'original_final_characters': len((old_run / 'answer.md').read_text()), 'retained_submission_characters_in_replay': len(result['answer']), 'retained_claims_in_replay': len(old_draft['claims']), 'original_files_modified': False})

    readiness = json.loads((TASK / 'runtime' / 'readiness.json').read_text())
    assert readiness['approved_for_development'] is False
    report = {'status': 'PASS', 'scope': 'actual submission handler under mocked network and container; not a model rerun', 'checks': checks, 'saved_event_replays': replays, 'real_model_calls': 0, 'real_scientific_calculations': 0, 'campaign_closed': True, 'historical_run_statuses_unchanged': True}
    destination = TASK / 'outputs' / 'post_development_review' / 'offline_submission_check.json'
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(report, ensure_ascii=False))


if __name__ == '__main__':
    main()
