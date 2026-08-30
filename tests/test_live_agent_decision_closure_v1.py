from __future__ import annotations

import json
import shutil
import tempfile
import unittest
import uuid
from pathlib import Path

from dynamics_atlas_harness.case_view_v1 import (
    CaseViewIntegrityError,
    build_case_view,
)
from dynamics_atlas_harness.live_agent_decision_closure_v1 import (
    ACTION_CARD_ID,
    POSITIVE_ARM_ID,
    STOP_ARM_ID,
    TARGET_RULE_INSTANCE_ID,
    build_budget,
    build_frozen_decision_state,
    build_planner_input,
    build_planner_proposal_schema,
    load_campaign_config,
    run_live_agent_decision_closure_campaign,
    validate_campaign_config,
    validate_planner_proposal,
)
from dynamics_atlas_harness.openrouter_proposal_transport_v1 import (
    OpenRouterCredential,
    OpenRouterProposalClient,
)
from dynamics_atlas_harness.review_console_v0 import render_review_console


REPO_ROOT = Path(__file__).resolve().parents[1]


class _HttpResponse:
    def __init__(self, value):
        self.status = 200
        self.body = json.dumps(value).encode("utf-8")

    def read(self):
        return self.body

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return False


class _PlannerStub:
    def __init__(self):
        self.calls = []

    def __call__(self, request, timeout):
        payload = json.loads(request.data.decode("utf-8"))
        visible = json.loads(payload["messages"][1]["content"].split("\n", 1)[1])
        cards = visible["legal_action_cards"]
        if cards:
            card_id = cards[0]["card_id"]
            proposal = {
                "case_id": visible["case_id"],
                "decision": "SELECT_ACTIONS",
                "selected_card_ids": [card_id],
                "rationales": {
                    card_id: "The exact listed lookup card addresses the current unresolved source declaration and its visible prerequisites are satisfied."
                },
            }
        else:
            proposal = {
                "case_id": visible["case_id"],
                "decision": "ABSTAIN_NO_ACTION",
                "selected_card_ids": [],
                "rationales": {},
            }
        self.calls.append(payload)
        return _HttpResponse(
            {
                "id": f"gen-decision-closure-test-{len(self.calls)}",
                "model": payload["model"],
                "provider": "OpenAI",
                "choices": [
                    {
                        "finish_reason": "stop",
                        "message": {
                            "role": "assistant",
                            "content": json.dumps(proposal),
                        },
                    }
                ],
                "usage": {
                    "prompt_tokens": 500,
                    "completion_tokens": 60,
                    "total_tokens": 560,
                    "cost": 0.0002,
                    "completion_tokens_details": {"reasoning_tokens": 10},
                    "prompt_tokens_details": {"cached_tokens": 0},
                },
            }
        )


class LiveAgentDecisionClosureV1Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix="test-live-decision-closure-")
        cls.root = Path(cls.temp.name)
        cls.ledger_path = (
            REPO_ROOT
            / "local"
            / "live_agent_decision_closure_v1"
            / f"test-{uuid.uuid4().hex}.json"
        )
        config = load_campaign_config()
        config["budget_ledger_path"] = cls.ledger_path.relative_to(REPO_ROOT).as_posix()
        cls.config = validate_campaign_config(config)
        cls.stub = _PlannerStub()
        client = OpenRouterProposalClient(
            credential=OpenRouterCredential(
                "test-openrouter-secret-123456789", "INHERITED_ENVIRONMENT"
            ),
            budget=build_budget(cls.config),
            open_call=cls.stub,
        )
        cls.result = run_live_agent_decision_closure_campaign(
            output_dir=cls.root / "campaign",
            client=client,
            config=cls.config,
        )

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()
        cls.ledger_path.unlink(missing_ok=True)
        cls.ledger_path.with_name(cls.ledger_path.name + ".lock").unlink(missing_ok=True)

    def test_exact_luna_calls_are_strict_toolless_and_no_retry(self):
        self.assertEqual(len(self.stub.calls), 2)
        for payload in self.stub.calls:
            self.assertEqual(payload["model"], "openai/gpt-5.6-luna")
            self.assertEqual(payload["provider"]["only"], ["openai"])
            self.assertFalse(payload["provider"]["allow_fallbacks"])
            self.assertTrue(payload["provider"]["require_parameters"])
            self.assertEqual(payload["reasoning"], {"effort": "low"})
            self.assertTrue(payload["response_format"]["json_schema"]["strict"])
            self.assertNotIn("tools", payload)
            self.assertNotIn("plugins", payload)
        self.assertEqual(self.result["manifest"]["completed_api_calls"], 2)
        self.assertEqual(self.result["manifest"]["http_attempts"], 2)

    def test_positive_arm_closes_exact_rule_and_preserves_unrelated_rules(self):
        root = self.root / "campaign" / POSITIVE_ARM_ID
        transition = json.loads((root / "rule_transition.json").read_text(encoding="utf-8"))
        evidence = json.loads((root / "evidence_results.json").read_text(encoding="utf-8"))[
            "evidence_results"
        ][0]
        conclusion = json.loads((root / "conclusion_packet.json").read_text(encoding="utf-8"))
        self.assertEqual(transition["affected_rule_instance_id"], TARGET_RULE_INSTANCE_ID)
        self.assertEqual(transition["before_rule_result"]["status"], "UNRESOLVED")
        self.assertEqual(transition["after_rule_result"]["status"], "PASS")
        self.assertEqual(transition["unrelated_rule_changes"], [])
        self.assertEqual(evidence["affected_rule_instance_id"], TARGET_RULE_INSTANCE_ID)
        self.assertEqual(evidence["rule_effect"], "ACTIVE_RULE_EFFECT")
        self.assertEqual(conclusion["terminal_disposition"], "ABSTAIN_OR_HUMAN_REVIEW")
        view = build_case_view(root)
        self.assertEqual(view.integrity_status, "PASS")
        self.assertEqual(view.artifact_kind, "LIVE_AGENT_DECISION_CLOSURE_V1_ARM")
        self.assertEqual(len(view.active_rule_evidence), 1)

    def test_card_removed_arm_abstains_and_executes_nothing(self):
        root = self.root / "campaign" / STOP_ARM_ID
        input_packet = json.loads((root / "planner_visible_input.json").read_text(encoding="utf-8"))
        admission = json.loads((root / "planner_admission.json").read_text(encoding="utf-8"))
        execution = json.loads((root / "execution_receipt.json").read_text(encoding="utf-8"))
        stop = json.loads((root / "stop_receipt.json").read_text(encoding="utf-8"))
        self.assertEqual(input_packet["legal_action_cards"], [])
        self.assertEqual(admission["decision"], "ABSTAIN_NO_ACTION")
        self.assertEqual(execution["executed_action_count"], 0)
        self.assertEqual(stop["lookup_executions"], 0)
        self.assertEqual(stop["operator_executions"], 0)
        view = build_case_view(root)
        self.assertEqual(view.integrity_status, "PASS")
        self.assertEqual(view.active_rule_evidence, [])
        self.assertEqual(view.before_after_rule_result_links, [])

    def test_removed_card_is_absent_from_schema_and_illegal_selection_rejected(self):
        state = build_frozen_decision_state()
        stop_input = build_planner_input(state, include_action_card=False)
        schema = build_planner_proposal_schema(stop_input)
        self.assertEqual(schema["properties"]["selected_card_ids"]["maxItems"], 0)
        with self.assertRaisesRegex(ValueError, "PLANNER_SELECTED_ILLEGAL_CARD"):
            validate_planner_proposal(
                stop_input,
                {
                    "case_id": stop_input["case_id"],
                    "decision": "SELECT_ACTIONS",
                    "selected_card_ids": [ACTION_CARD_ID],
                    "rationales": {ACTION_CARD_ID: "Attempt to restore removed card."},
                },
            )

    def test_tampered_artifact_fails_closed_in_case_view(self):
        source = self.root / "campaign"
        target = self.root / "tampered"
        shutil.copytree(source, target)
        proposal_path = target / POSITIVE_ARM_ID / "live_call" / "parsed_proposal.json"
        proposal = json.loads(proposal_path.read_text(encoding="utf-8"))
        proposal["rationales"][ACTION_CARD_ID] = "tampered"
        proposal_path.write_text(json.dumps(proposal), encoding="utf-8")
        with self.assertRaisesRegex(CaseViewIntegrityError, "STALE_ARTIFACT_REFERENCE_HASH"):
            build_case_view(target / POSITIVE_ARM_ID)

    def test_workbench_renders_both_live_decision_arms(self):
        output = self.root / "workbench"
        index = render_review_console(
            status_path=REPO_ROOT / "governance" / "current_execution_status.json",
            review_workspace=REPO_ROOT / "review" / "source_science_v1",
            output_dir=output,
            case_roots=[
                self.root / "campaign" / POSITIVE_ARM_ID,
                self.root / "campaign" / STOP_ARM_ID,
            ],
        )
        rendered = index.read_text(encoding="utf-8")
        self.assertIn(POSITIVE_ARM_ID, rendered)
        self.assertIn(STOP_ARM_ID, rendered)
        self.assertIn("LIVE_AGENT_DECISION_CLOSURE_V1_ARM", rendered)
        self.assertIn("ABSTAIN_OR_HUMAN_REVIEW", rendered)

    def test_existing_case_runner_view_remains_readable(self):
        recorded_run = (
            REPO_ROOT
            / "evidence"
            / "live_agent_common_flows_v1"
            / "development_runs"
            / "authorized_campaign_live_20260830"
            / "recorded_replay"
            / "hsp90"
        )
        view = build_case_view(recorded_run)
        self.assertEqual(view.artifact_kind, "CASE_RUNNER_V1_RUN")
        self.assertEqual(view.integrity_status, "PASS")

    def test_caller_config_cannot_bypass_budget_or_model_boundary(self):
        over_budget = json.loads(json.dumps(self.config))
        over_budget["budget_usd"] = "1.01"
        with self.assertRaisesRegex(ValueError, "CAMPAIGN_BUDGET_EXCEEDS_AUTHORITY"):
            validate_campaign_config(over_budget)
        wrong_model = json.loads(json.dumps(self.config))
        wrong_model["model"]["model_id"] = "minimax/minimax-m2.5"
        with self.assertRaisesRegex(ValueError, "ONLY_EXACT_LUNA_OPENAI_PROVIDER_ALLOWED"):
            validate_campaign_config(wrong_model)


if __name__ == "__main__":
    unittest.main()
