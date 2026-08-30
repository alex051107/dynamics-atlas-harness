from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from decimal import Decimal
from pathlib import Path

from jsonschema import Draft202012Validator

from dynamics_atlas_harness import case_runner_v1 as runner
from dynamics_atlas_harness.case_view_v1 import CaseViewIntegrityError, build_case_view
from dynamics_atlas_harness.live_agent_common_flows_v1 import (
    LIVE_AGENT_CAMPAIGN_CLOSED_ERROR,
    LIVE_AGENT_CAMPAIGN_OPEN_STATUS,
    build_planner_proposal_schema,
    load_campaign_config,
    run_frozen_profiler_live_planner_case,
    run_live_agent_campaign,
    run_live_agent_case,
)
from dynamics_atlas_harness.openrouter_proposal_transport_v1 import (
    OpenRouterBudgetLedger,
    OpenRouterCredential,
    OpenRouterProposalClient,
)


def _contains_unknown(value):
    if isinstance(value, str):
        return "UNKNOWN" in value.upper()
    if isinstance(value, list):
        return any(_contains_unknown(item) for item in value)
    if isinstance(value, dict):
        return any(_contains_unknown(item) for item in value.values())
    return False


def _profile_envelope(core):
    annotations = []
    facts = core["proposed_case_facts"]
    for field, value in facts["case"].items():
        annotations.append(_annotation("CASE", core["case_id"], field, value))
    for source in facts["sources"]:
        for field, value in source.items():
            if field in {"source_id", "evidence_role"}:
                continue
            if field == "time_semantics":
                annotations.append(
                    _annotation(
                        "SOURCE",
                        source["source_id"],
                        "time_semantics.kind",
                        value["kind"],
                    )
                )
            else:
                annotations.append(
                    _annotation("SOURCE", source["source_id"], field, value)
                )
    for edge in facts["edges"]:
        for field, value in edge.items():
            if field in {"edge_id", "left_source_id", "right_source_id"}:
                continue
            annotations.append(_annotation("EDGE", edge["edge_id"], field, value))
    return {**core, "field_annotations": annotations}


def _annotation(target_type, target_id, field, value):
    return {
        "target_type": target_type,
        "target_id": target_id,
        "field": field,
        "status": "UNKNOWN" if _contains_unknown(value) else "EXTRACTED",
        "evidence_pointers": [
            {
                "pointer_type": "PACKET_POINTER",
                "source_id": "PACKET",
                "value": "/research_question",
            }
        ],
        "confidence": 0.5,
    }


class _FakeHttpResponse:
    def __init__(self, value):
        self.status = 200
        self._body = json.dumps(value).encode("utf-8")

    def read(self):
        return self._body

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return False


class _ProposalHttpStub:
    def __init__(self, *, smuggle_planner_verdict=False):
        self.smuggle_planner_verdict = smuggle_planner_verdict
        self.calls = []

    def __call__(self, request, timeout):
        payload = json.loads(request.data.decode("utf-8"))
        visible_text = payload["messages"][1]["content"].split("\n", 1)[1]
        visible = json.loads(visible_text)
        role = (
            "PROFILER"
            if "PROFILER" in payload["response_format"]["json_schema"]["name"]
            else "PLANNER"
        )
        case_id = visible["case_id"]
        if role == "PROFILER":
            key = "hsp90" if case_id.startswith("HSP90") else "adk"
            core = json.loads(
                runner._CASE_PACKET_REGISTRY[case_id]["profile_proposal"].read_text(
                    encoding="utf-8"
                )
            )
            proposal = _profile_envelope(core)
        else:
            cards = visible["legal_action_cards"]
            if cards:
                card_id = cards[0]["card_id"]
                rationale = (
                    "The Rule will SUPPORT_WITHIN_CEILING."
                    if self.smuggle_planner_verdict
                    else "This legal descriptive card addresses the visible unresolved obligation."
                )
                proposal = {
                    "case_id": case_id,
                    "decision": "SELECT_ACTIONS",
                    "selected_card_ids": [card_id],
                    "rationales": {card_id: rationale},
                }
            else:
                proposal = {
                    "case_id": case_id,
                    "decision": "ABSTAIN_NO_ACTION",
                    "selected_card_ids": [],
                    "rationales": {},
                }
        self.calls.append((role, case_id))
        response = {
            "id": f"gen-test-{len(self.calls)}",
            "model": payload["model"],
            "provider": payload["provider"]["only"][0],
            "choices": [
                {
                    "finish_reason": "stop",
                    "message": {"role": "assistant", "content": json.dumps(proposal)},
                }
            ],
            "usage": {
                "prompt_tokens": 100,
                "completion_tokens": 200,
                "total_tokens": 300,
                "cost": 0.0001,
                "completion_tokens_details": {"reasoning_tokens": 5},
                "prompt_tokens_details": {"cached_tokens": 0},
            },
        }
        return _FakeHttpResponse(response)


def _authorized_test_config():
    config = load_campaign_config()
    config["execution_status"] = LIVE_AGENT_CAMPAIGN_OPEN_STATUS
    return config


def _client(stub, *, state_path=None, campaign_id=None):
    return OpenRouterProposalClient(
        credential=OpenRouterCredential(
            "test-live-agent-secret-12345678", "INHERITED_ENVIRONMENT"
        ),
        budget=OpenRouterBudgetLedger(
            cap_usd=Decimal("5"),
            max_completed_calls=16,
            max_attempts_per_cell=2,
            campaign_id=campaign_id,
            state_path=state_path,
        ),
        open_call=stub,
    )


class LiveAgentCommonFlowsV1Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.root = Path(cls.temp.name)
        cls.stub = _ProposalHttpStub()
        cls.config = _authorized_test_config()
        cls.result = run_live_agent_case(
            case_id="HSP90_NTD_EXPOSED_PAPER_BLIND_V1",
            output_dir=cls.root / "live-hsp90",
            model_profile="luna",
            client=_client(
                cls.stub,
                state_path=cls.root / "live-hsp90-budget.json",
                campaign_id=cls.config["campaign_id"],
            ),
            config=cls.config,
        )

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_live_profiler_and_planner_use_the_same_deterministic_runner(self):
        self.assertEqual(self.result["status"], "SUCCEEDED")
        manifest = self.result["manifest"]
        self.assertEqual(manifest["agent_mode"], "LIVE_OPENROUTER")
        self.assertTrue(manifest["network_accessed"])
        self.assertEqual(len(self.stub.calls), 2)
        self.assertEqual(
            [role for role, _ in self.stub.calls], ["PROFILER", "PLANNER"]
        )
        self.assertEqual(manifest["authorization"]["executed_action_count"], 1)
        self.assertEqual(
            manifest["rule_reevaluation"]["before_rule_results"],
            manifest["rule_reevaluation"]["after_rule_results"],
        )
        self.assertEqual(
            manifest["terminal_scientific_state"],
            "NOT_CALCULATED_BY_CASE_RUNNER",
        )
        self.assertEqual(self.result["case_view"]["integrity_status"], "PASS")
        diagnostic = self.result["case_view"]["agent_proposal"][
            "field_annotation_diagnostic"
        ]
        self.assertEqual(diagnostic["routing_effect"], "NONE_DIAGNOSTIC_ONLY")
        self.assertEqual(diagnostic["scientific_authority"], "NONE")

    def test_live_receipt_request_raw_response_and_envelope_are_fail_closed(self):
        source = self.root / "live-hsp90"
        mutations = (
            ("live_calls/profiler/raw_response.txt", "tampered"),
            ("live_calls/profiler/request_payload.json", {"tampered": True}),
            ("live_calls/profiler/proposal_envelope.json", {"tampered": True}),
        )
        for index, (relative, replacement) in enumerate(mutations):
            target = self.root / f"tampered-{index}"
            shutil.copytree(source, target)
            path = target / relative
            if isinstance(replacement, str):
                path.write_text(replacement, encoding="utf-8")
            else:
                path.write_text(json.dumps(replacement), encoding="utf-8")
            with self.assertRaises(CaseViewIntegrityError):
                build_case_view(target)

    def test_planner_schema_excludes_removed_and_cross_case_cards(self):
        planner_input = self.result["manifest"]["planner_visible_input"]
        schema = build_planner_proposal_schema(planner_input)
        current_id = planner_input["legal_action_cards"][0]["card_id"]
        valid = {
            "case_id": planner_input["case_id"],
            "decision": "SELECT_ACTIONS",
            "selected_card_ids": [current_id],
            "rationales": {current_id: "Use the visible legal card."},
        }
        Draft202012Validator(schema).validate(valid)
        invalid = {
            **valid,
            "selected_card_ids": ["CROSS_CASE_OR_REMOVED_CARD"],
            "rationales": {
                "CROSS_CASE_OR_REMOVED_CARD": "Attempt an unavailable card."
            },
        }
        self.assertTrue(list(Draft202012Validator(schema).iter_errors(invalid)))

    def test_planner_cross_field_semantics_remain_deterministic_after_schema_repair(self):
        planner_input = self.result["manifest"]["planner_visible_input"]
        schema = build_planner_proposal_schema(planner_input)
        card_id = planner_input["legal_action_cards"][0]["card_id"]
        contradictory = {
            "case_id": planner_input["case_id"],
            "decision": "ABSTAIN_NO_ACTION",
            "selected_card_ids": [card_id],
            "rationales": {card_id: "Contradictory transport-valid proposal."},
        }
        # The provider-portable schema constrains identities and shapes only.
        Draft202012Validator(schema).validate(contradictory)
        with self.assertRaisesRegex(
            runner.capsule.ExposedPaperBlindCapsuleError,
            "PLANNER_ABSTAIN_MUST_SELECT_ZERO",
        ):
            runner.capsule.validate_planner_proposal(
                planner_input, contradictory
            )
        self.assertNotIn("anyOf", schema)
        for variant in schema["properties"]["rationales"]["anyOf"]:
            self.assertFalse(variant["additionalProperties"])

    def test_planner_terminal_verdict_language_is_rejected_before_execution(self):
        stub = _ProposalHttpStub(smuggle_planner_verdict=True)
        result = run_live_agent_case(
            case_id="HSP90_NTD_EXPOSED_PAPER_BLIND_V1",
            output_dir=self.root / "smuggled-verdict",
            model_profile="luna",
            client=_client(
                stub,
                state_path=self.root / "smuggled-verdict-budget.json",
                campaign_id=self.config["campaign_id"],
            ),
            config=self.config,
        )
        self.assertEqual(result["status"], "REJECTED_FAIL_CLOSED")
        self.assertEqual(
            result["failure"]["error_code"],
            "LIVE_PLANNER_RATIONALE_SMUGGLES_TERMINAL_VERDICT",
        )
        self.assertFalse((self.root / "smuggled-verdict" / "actions").exists())

    def test_missing_credential_preserves_recorded_work_and_blocks_only_live_cells(self):
        output = self.root / "missing-credential-campaign"
        budget = OpenRouterBudgetLedger(
            cap_usd=Decimal("5"),
            max_completed_calls=16,
            max_attempts_per_cell=2,
            campaign_id=self.config["campaign_id"],
            state_path=self.root / "missing-credential-budget.json",
        )
        manifest = run_live_agent_campaign(
            output_dir=output,
            environment={},
            budget=budget,
            config=self.config,
        )
        self.assertEqual(
            manifest["status"], "LIVE_CALL_BLOCKED_MISSING_CREDENTIAL"
        )
        self.assertEqual(manifest["completed_api_calls"], 0)
        self.assertEqual(manifest["actual_cost_usd"], "0")
        self.assertEqual(len(manifest["recorded_replay_cases"]), 2)
        self.assertFalse(manifest["credential_handling"]["key_value_persisted"])
        self.assertTrue((output / "recorded_replay" / "hsp90" / "case_run_manifest_v1.json").is_file())
        self.assertTrue((output / "recorded_replay" / "adk" / "case_run_manifest_v1.json").is_file())

    def test_closed_campaign_blocks_all_direct_runtime_entries_before_output_or_http(self):
        closed = load_campaign_config()
        stub = _ProposalHttpStub()
        client = _client(
            stub,
            state_path=self.root / "closed-direct-budget.json",
            campaign_id=closed["campaign_id"],
        )
        outputs = [
            self.root / "closed-live-case",
            self.root / "closed-frozen-profiler-case",
            self.root / "closed-live-campaign",
        ]
        calls = (
            lambda: run_live_agent_case(
                case_id="HSP90_NTD_EXPOSED_PAPER_BLIND_V1",
                output_dir=outputs[0],
                model_profile="minimax",
                client=client,
                config=closed,
            ),
            lambda: run_frozen_profiler_live_planner_case(
                case_id="HSP90_NTD_EXPOSED_PAPER_BLIND_V1",
                output_dir=outputs[1],
                frozen_profiler_artifact_root=self.root / "must-not-be-read",
                planner_model_profile="minimax",
                client=client,
                config=closed,
            ),
            lambda: run_live_agent_campaign(
                output_dir=outputs[2],
                environment={},
                budget=client.budget,
                config=closed,
            ),
        )
        for call in calls:
            with self.assertRaisesRegex(
                ValueError, LIVE_AGENT_CAMPAIGN_CLOSED_ERROR
            ):
                call()
        self.assertEqual(stub.calls, [])
        self.assertFalse(any(path.exists() for path in outputs))

    def test_open_runtime_requires_persisted_campaign_bound_budget(self):
        stub = _ProposalHttpStub()
        in_memory_client = _client(stub)
        case_output = self.root / "in-memory-budget-case"
        campaign_output = self.root / "missing-budget-campaign"
        with self.assertRaisesRegex(
            ValueError, "CAMPAIGN_BOUND_PERSISTED_BUDGET_REQUIRED"
        ):
            run_live_agent_case(
                case_id="HSP90_NTD_EXPOSED_PAPER_BLIND_V1",
                output_dir=case_output,
                model_profile="luna",
                client=in_memory_client,
                config=self.config,
            )
        with self.assertRaisesRegex(
            ValueError, "CAMPAIGN_BOUND_PERSISTED_BUDGET_REQUIRED"
        ):
            run_live_agent_campaign(
                output_dir=campaign_output,
                environment={},
                config=self.config,
            )
        self.assertEqual(stub.calls, [])
        self.assertFalse(case_output.exists())
        self.assertFalse(campaign_output.exists())

    def test_frozen_panel_has_exact_16_call_arithmetic_and_no_hidden_fallback(self):
        config = load_campaign_config()
        self.assertEqual(config["max_completed_calls"], 16)
        self.assertEqual(config["automatic_retries"], 0)
        planned = (
            len(config["cases"])
            * len(config["roles"])
            * sum(model["independent_trials_per_case"] for model in config["models"])
        )
        self.assertEqual(planned, 16)
        self.assertEqual(
            {model["profile_id"] for model in config["models"]},
            {"luna", "deepseek", "minimax"},
        )


if __name__ == "__main__":
    unittest.main()
