import json
import tempfile
import unittest
from pathlib import Path

from dynamics_atlas_harness.live_agent_exposed_v1 import load_json_object, sha256_json
from dynamics_atlas_harness.openrouter_profiler_sweep_v1 import (
    OPENROUTER_PROFILER_CONFIG_SCHEMA,
    OpenRouterProfilerJsonClient,
    OpenRouterProfilerSweepError,
    build_profiler_output_schema,
    build_profiler_request,
    read_openrouter_api_key,
    run_screening,
    screening_cells,
    sha256_file,
    validate_execution_config,
    validate_frozen_input_hashes,
)


REPO_ROOT = Path(__file__).parents[1]
EXPERIMENT_ROOT = REPO_ROOT / "agent_experiments" / "v1"
DEFAULT_CONFIG = EXPERIMENT_ROOT / "config" / "openrouter_profiler_screening_v1.json"
SEALED_REFERENCE = EXPERIMENT_ROOT / "sealed_references" / "profiler_reference_v1.json"


class FakeHttpResponse:
    def __init__(self, body, status=200):
        self._body = json.dumps(body).encode("utf-8")
        self.status = status

    def read(self):
        return self._body

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return False


def valid_config():
    return {
        "schema_version": OPENROUTER_PROFILER_CONFIG_SCHEMA,
        "execution_status": "HUMAN_FROZEN_FOR_EXECUTION",
        "run_kind": "SCREENING",
        "role": "PROFILER",
        "case_keys": ["xeisd", "hsp90"],
        "prompt_path": "agent_experiments/v1/prompts/profiler_v1.md",
        "sealed_reference_path": "agent_experiments/v1/sealed_references/profiler_reference_v1.json",
        "temperature": 0,
        "max_tokens": 1200,
        "timeout_seconds": 90,
        "calls_per_model_case": 1,
        "client_side_reported_cost_stop_usd": 10.0,
        "account_spend_limit_readback": {
            "status": "HUMAN_CONFIRMED",
            "evidence_locator": "test://human-confirmed-account-limit",
        },
        "frozen_inputs": {
            "prompt_sha256": "0" * 64,
            "sealed_reference_sha256": "0" * 64,
            "packet_sha256_by_case": {"xeisd": "0" * 64, "hsp90": "0" * 64},
            "schema_sha256_by_case": {"xeisd": "0" * 64, "hsp90": "0" * 64},
        },
        "models": [
            {"matrix_label": "LOW_COST", "model_id": "test/low", "provider_only": ["test-a"]},
            {"matrix_label": "MID_COST", "model_id": "test/mid", "provider_only": ["test-b"]},
            {"matrix_label": "CONTROL", "model_id": "test/control", "provider_only": ["test-c"]},
        ],
    }


def proposal_for_packet(packet, sealed_reference):
    case = sealed_reference["cases"][packet["case_id"]]
    sources = [
        {**reference, "sample_system_composition": "UNKNOWN"}
        for reference in case["critical_sources"]
    ]
    edges = [
        {**reference, "condition_relation": "UNKNOWN"}
        for reference in case["critical_edges"]
    ]
    return {
        "schema_version": "agent-profiler-proposal/v1",
        "case_id": packet["case_id"],
        "sources": sources,
        "edges": edges,
        "unknowns": [
            {
                "path": path,
                "reason": "not supplied in packet",
                "evidence_pointer": "packet",
            }
            for path in case["required_unknown_paths"]
        ],
    }


class OpenRouterProfilerSweepTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.packet = load_json_object(
            EXPERIMENT_ROOT / "workspaces" / "xeisd_profiler" / "input.json"
        )
        cls.reference = load_json_object(SEALED_REFERENCE)
        cls.prompt = (EXPERIMENT_ROOT / "prompts" / "profiler_v1.md").read_text(
            encoding="utf-8"
        )
        cls.model = valid_config()["models"][0]

    def frozen_config(self):
        config = valid_config()
        packet_hashes = {}
        schema_hashes = {}
        for case_key, workspace in (("xeisd", "xeisd_profiler"), ("hsp90", "hsp90_profiler")):
            packet_path = EXPERIMENT_ROOT / "workspaces" / workspace / "input.json"
            packet = load_json_object(packet_path)
            packet_hashes[case_key] = sha256_file(packet_path)
            schema_hashes[case_key] = sha256_json(build_profiler_output_schema(packet))
        config["frozen_inputs"] = {
            "prompt_sha256": sha256_file(EXPERIMENT_ROOT / "prompts" / "profiler_v1.md"),
            "sealed_reference_sha256": sha256_file(SEALED_REFERENCE),
            "packet_sha256_by_case": packet_hashes,
            "schema_sha256_by_case": schema_hashes,
        }
        return config

    def test_packet_derived_schema_and_request_are_strict_single_provider_and_toolless(self):
        schema = build_profiler_output_schema(self.packet)
        request = build_profiler_request(
            model_spec=self.model,
            prompt=self.prompt,
            packet=self.packet,
            temperature=0,
            max_tokens=1200,
        )

        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(request["response_format"]["type"], "json_schema")
        self.assertTrue(request["response_format"]["json_schema"]["strict"])
        self.assertEqual(request["provider"]["only"], ["test-a"])
        self.assertFalse(request["provider"]["allow_fallbacks"])
        self.assertTrue(request["provider"]["require_parameters"])
        self.assertNotIn("tools", request)
        self.assertNotIn("tool_choice", request)
        self.assertNotIn("models", request)

    def test_initial_configuration_is_not_callable_without_human_matrix_budget_and_hashes(self):
        initial = load_json_object(DEFAULT_CONFIG)
        codes = {item["code"] for item in validate_execution_config(initial)}

        self.assertIn("MODEL_MATRIX_NOT_HUMAN_FROZEN", codes)
        self.assertIn("EXPLICIT_FINITE_CLIENT_SIDE_COST_STOP_REQUIRED", codes)
        self.assertIn("ACCOUNT_SPEND_LIMIT_NOT_HUMAN_CONFIRMED", codes)
        self.assertIn("FROZEN_THREE_TO_FOUR_MODEL_MATRIX_REQUIRED", codes)
        with self.assertRaises(OpenRouterProfilerSweepError):
            screening_cells(initial)

    def test_execution_config_rejects_nonfinite_budget_nonzero_temperature_and_duplicate_labels(self):
        config = valid_config()
        config["client_side_reported_cost_stop_usd"] = float("nan")
        config["temperature"] = 0.1
        config["models"][1]["matrix_label"] = "LOW_COST"
        codes = {item["code"] for item in validate_execution_config(config)}

        self.assertIn("EXPLICIT_FINITE_CLIENT_SIDE_COST_STOP_REQUIRED", codes)
        self.assertIn("SCREENING_TEMPERATURE_MUST_EQUAL_ZERO", codes)
        self.assertIn("DUPLICATE_MATRIX_LABEL", codes)

    def test_frozen_input_hash_preflight_rejects_mismatch_before_transport(self):
        config = self.frozen_config()
        config["frozen_inputs"]["packet_sha256_by_case"]["xeisd"] = "0" * 64
        findings = validate_frozen_input_hashes(config, REPO_ROOT)

        self.assertEqual(
            findings,
            [{"code": "FROZEN_INPUT_HASH_MISMATCH", "input": "packet_sha256_by_case.xeisd"}],
        )

    def test_missing_environment_key_fails_before_any_transport(self):
        with self.assertRaisesRegex(OpenRouterProfilerSweepError, "OPENROUTER_API_KEY"):
            read_openrouter_api_key({})

    def test_successful_response_records_transport_and_provider_provenance_without_persisting_credential(self):
        proposal = proposal_for_packet(self.packet, self.reference)
        response = {
            "model": "test/low",
            "choices": [{"message": {"content": json.dumps(proposal)}}],
            "usage": {"prompt_tokens": 12, "completion_tokens": 34, "total_tokens": 46, "cost": 0.001},
            "openrouter_metadata": {
                "requested": "test/low",
                "strategy": "direct",
                "attempt": 1,
                "endpoints": {"available": [{"provider": "TEST-A", "selected": True}]},
            },
        }
        requests = []

        def fake_open(request, timeout):
            requests.append((request, timeout))
            return FakeHttpResponse(response)

        artifact = OpenRouterProfilerJsonClient(
            api_key="test-secret-not-to-persist", open_call=fake_open
        ).call(
            model_spec=self.model,
            prompt=self.prompt,
            packet=self.packet,
            temperature=0,
            max_tokens=1200,
        )

        receipt = artifact["receipt"]
        self.assertEqual(len(requests), 1)
        self.assertEqual(receipt["transport_status"], "SUCCEEDED")
        self.assertEqual(receipt["proposal_parse_status"], "PARSED_JSON_OBJECT")
        self.assertEqual(receipt["provider_provenance_status"], "PASS")
        self.assertEqual(receipt["actual_provider"], "TEST-A")
        self.assertEqual(receipt["usage"]["cost"], 0.001)
        self.assertEqual(artifact["parsed_proposal"], proposal)
        self.assertNotIn("test-secret-not-to-persist", json.dumps(artifact))
        self.assertEqual(requests[0][0].get_header("X-openrouter-metadata"), "enabled")

    def test_provider_model_or_attempt_mismatch_is_provenance_rejected(self):
        proposal = proposal_for_packet(self.packet, self.reference)
        response = {
            "model": "test/not-requested",
            "choices": [{"message": {"content": json.dumps(proposal)}}],
            "openrouter_metadata": {
                "attempt": 2,
                "endpoints": {"available": [{"provider": "other-provider", "selected": True}]},
            },
        }

        artifact = OpenRouterProfilerJsonClient(
            api_key="test-key", open_call=lambda request, timeout: FakeHttpResponse(response)
        ).call(
            model_spec=self.model,
            prompt=self.prompt,
            packet=self.packet,
            temperature=0,
            max_tokens=1200,
        )

        receipt = artifact["receipt"]
        self.assertEqual(receipt["transport_status"], "SUCCEEDED")
        self.assertEqual(receipt["provider_provenance_status"], "FAIL")
        self.assertEqual(
            set(receipt["provider_provenance_reason_codes"]),
            {"RETURNED_MODEL_MISMATCH", "ACTUAL_PROVIDER_MISMATCH", "ROUTER_ATTEMPT_MUST_EQUAL_ONE"},
        )

    def test_invalid_response_is_fail_closed_without_retry(self):
        requests = []

        def fake_open(request, timeout):
            requests.append(request)
            return FakeHttpResponse({"model": "test/low", "choices": []})

        artifact = OpenRouterProfilerJsonClient(api_key="test-key", open_call=fake_open).call(
            model_spec=self.model,
            prompt=self.prompt,
            packet=self.packet,
            temperature=0,
            max_tokens=1200,
        )

        self.assertEqual(len(requests), 1)
        self.assertEqual(artifact["receipt"]["transport_status"], "SUCCEEDED")
        self.assertEqual(artifact["receipt"]["proposal_parse_status"], "FAILED")
        self.assertIn("OPENROUTER_RESPONSE_CONTENT_MISSING", artifact["receipt"]["reason_codes"])
        self.assertIsNone(artifact["parsed_proposal"])

    def test_screening_matrix_is_exactly_models_times_two_cases_with_no_other_role(self):
        cells = screening_cells(valid_config())

        self.assertEqual(len(cells), 6)
        self.assertEqual({cell["case_key"] for cell in cells}, {"xeisd", "hsp90"})
        self.assertNotIn("planner", json.dumps(cells).lower())
        self.assertNotIn("operator", json.dumps(cells).lower())

    def test_mocked_screening_persists_receipts_and_never_calls_planner_or_operator(self):
        config = self.frozen_config()
        self_reference = self.reference

        class FakeClient:
            def __init__(self):
                self.calls = []

            def call(self, *, model_spec, prompt, packet, temperature, max_tokens):
                self.calls.append((model_spec["model_id"], packet["case_id"]))
                proposal = proposal_for_packet(packet, self_reference)
                return {
                    "raw_response": json.dumps({"choices": [{"message": {"content": json.dumps(proposal)}}]}),
                    "parsed_proposal": proposal,
                    "receipt": {
                        "status": "TRANSPORT_SUCCEEDED",
                        "transport_status": "SUCCEEDED",
                        "proposal_parse_status": "PARSED_JSON_OBJECT",
                        "provider_provenance_status": "PASS",
                        "provider_provenance_reason_codes": [],
                        "case_id": packet["case_id"],
                        "call_count": 1,
                        "cost_usd": 0.001,
                        "latency_ms": 1,
                        "actual_provider": model_spec["provider_only"][0],
                        "reason_codes": [],
                    },
                }

        fake_client = FakeClient()
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_root = Path(temporary_directory) / "screening"
            receipt = run_screening(
                config=config,
                repo_root=REPO_ROOT,
                output_root=output_root,
                api_key="not-used-by-fake-client",
                client=fake_client,
            )

            self.assertEqual(len(fake_client.calls), 6)
            self.assertEqual(receipt["planned_cells"], 6)
            self.assertEqual(receipt["completed_cells"], 6)
            self.assertEqual(receipt["planner_model_calls"], 0)
            self.assertEqual(receipt["operator_calls"], 0)
            self.assertEqual(receipt["end_to_end"], "NOT_RUN")
            self.assertTrue((output_root / "run_receipt.json").is_file())
            self.assertEqual(
                {item["screening_candidate_status"] for item in receipt["cell_results"]}, {"PASS"}
            )
            self.assertFalse(any(output_root.rglob("request_payload.json")))

    def test_semantically_invalid_parsed_proposal_is_capability_rejected(self):
        config = self.frozen_config()

        class FakeClient:
            def call(self, *, model_spec, prompt, packet, temperature, max_tokens):
                return {
                    "raw_response": "{}",
                    "parsed_proposal": {},
                    "receipt": {
                        "status": "TRANSPORT_SUCCEEDED",
                        "transport_status": "SUCCEEDED",
                        "proposal_parse_status": "PARSED_JSON_OBJECT",
                        "provider_provenance_status": "PASS",
                        "provider_provenance_reason_codes": [],
                        "case_id": packet["case_id"],
                        "call_count": 1,
                        "cost_usd": 0.001,
                        "latency_ms": 1,
                        "actual_provider": model_spec["provider_only"][0],
                        "reason_codes": [],
                    },
                }

        with tempfile.TemporaryDirectory() as temporary_directory:
            receipt = run_screening(
                config=config,
                repo_root=REPO_ROOT,
                output_root=Path(temporary_directory) / "screening",
                api_key="not-used-by-fake-client",
                client=FakeClient(),
            )

        self.assertEqual(
            {item["screening_candidate_status"] for item in receipt["cell_results"]},
            {"CAPABILITY_REJECTED"},
        )
        self.assertEqual(
            {item["typed_contract_status"] for item in receipt["cell_results"]}, {"FAIL"}
        )

    def test_client_side_reported_cost_stop_blocks_later_cells_after_one_over_cap_call(self):
        config = self.frozen_config()
        config["client_side_reported_cost_stop_usd"] = 0.01

        class FakeClient:
            def __init__(self):
                self.call_count = 0

            def call(self, *, model_spec, prompt, packet, temperature, max_tokens):
                self.call_count += 1
                proposal = proposal_for_packet(packet, OpenRouterProfilerSweepTests.reference)
                return {
                    "raw_response": "{}",
                    "parsed_proposal": proposal,
                    "receipt": {
                        "status": "TRANSPORT_SUCCEEDED",
                        "transport_status": "SUCCEEDED",
                        "proposal_parse_status": "PARSED_JSON_OBJECT",
                        "provider_provenance_status": "PASS",
                        "provider_provenance_reason_codes": [],
                        "case_id": packet["case_id"],
                        "call_count": 1,
                        "cost_usd": 0.02,
                        "latency_ms": 1,
                        "actual_provider": model_spec["provider_only"][0],
                        "reason_codes": [],
                    },
                }

        fake_client = FakeClient()
        with tempfile.TemporaryDirectory() as temporary_directory:
            receipt = run_screening(
                config=config,
                repo_root=REPO_ROOT,
                output_root=Path(temporary_directory) / "screening",
                api_key="not-used-by-fake-client",
                client=fake_client,
            )

        self.assertEqual(fake_client.call_count, 1)
        self.assertEqual(receipt["completed_cells"], 1)
        self.assertEqual(
            sum(
                item["screening_candidate_status"] == "BLOCKED_CLIENT_SIDE_COST_STOP"
                for item in receipt["cell_results"]
            ),
            5,
        )

    def test_missing_reported_cost_stops_later_cells_fail_closed(self):
        config = self.frozen_config()

        class FakeClient:
            def __init__(self):
                self.call_count = 0

            def call(self, *, model_spec, prompt, packet, temperature, max_tokens):
                self.call_count += 1
                proposal = proposal_for_packet(packet, OpenRouterProfilerSweepTests.reference)
                return {
                    "raw_response": "{}",
                    "parsed_proposal": proposal,
                    "receipt": {
                        "status": "TRANSPORT_SUCCEEDED",
                        "transport_status": "SUCCEEDED",
                        "proposal_parse_status": "PARSED_JSON_OBJECT",
                        "provider_provenance_status": "PASS",
                        "provider_provenance_reason_codes": [],
                        "case_id": packet["case_id"],
                        "call_count": 1,
                        "cost_usd": None,
                        "latency_ms": 1,
                        "actual_provider": model_spec["provider_only"][0],
                        "reason_codes": [],
                    },
                }

        fake_client = FakeClient()
        with tempfile.TemporaryDirectory() as temporary_directory:
            receipt = run_screening(
                config=config,
                repo_root=REPO_ROOT,
                output_root=Path(temporary_directory) / "screening",
                api_key="not-used-by-fake-client",
                client=fake_client,
            )

        self.assertEqual(fake_client.call_count, 1)
        self.assertEqual(receipt["completed_cells"], 1)
        self.assertEqual(receipt["cell_results"][0]["screening_candidate_status"], "REPORTED_COST_UNAVAILABLE")
        self.assertEqual(
            sum(
                item["screening_candidate_status"] == "BLOCKED_REPORTED_COST_UNAVAILABLE"
                for item in receipt["cell_results"]
            ),
            5,
        )


if __name__ == "__main__":
    unittest.main()
