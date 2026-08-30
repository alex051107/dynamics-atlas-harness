import io
import json
import tempfile
import unittest
import urllib.error
from decimal import Decimal
from pathlib import Path

from dynamics_atlas_harness.openrouter_proposal_transport_v1 import (
    OpenRouterBudgetLedger,
    OpenRouterCredential,
    OpenRouterModelSpec,
    OpenRouterProposalClient,
    OpenRouterProposalTransportError,
    build_openrouter_proposal_request,
    read_openrouter_credential,
)


CASE_ID = "CASE::ONE"
ROLE = "PROFILER"
SECRET = "test-openrouter-secret-12345678"
SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": ["case_id", "decision"],
    "properties": {
        "case_id": {"const": CASE_ID},
        "decision": {"type": "string", "enum": ["UNKNOWN", "OBSERVED"]},
    },
}
PROPOSAL = {"case_id": CASE_ID, "decision": "UNKNOWN"}


def model_spec(**overrides):
    values = {
        "model_id": "test/model-exact",
        "provider_endpoint_tag": "test-provider/fp8",
        "expected_provider_display_name": "Test Provider",
        "prompt_price_per_token_usd": Decimal("0.0000002"),
        "completion_price_per_token_usd": Decimal("0.0000012"),
        "request_price_usd": Decimal("0"),
        "metadata_sha256": "a" * 64,
        "accepted_returned_model_ids": (
            "test/model-exact",
            "test/model-canonical-202608",
        ),
        "reasoning_effort": "low",
    }
    values.update(overrides)
    return OpenRouterModelSpec(**values)


def response_body(
    *,
    proposal=PROPOSAL,
    returned_model="test/model-exact",
    provider="Test Provider",
    service_tier="default",
    finish_reason="stop",
    cost=0.0001,
):
    usage = {
        "prompt_tokens": 12,
        "completion_tokens": 34,
        "total_tokens": 46,
        "completion_tokens_details": {"reasoning_tokens": 3},
        "prompt_tokens_details": {"cached_tokens": 2},
    }
    if cost is not None:
        usage["cost"] = cost
    return {
        "id": "gen-test-001",
        "model": returned_model,
        "choices": [
            {
                "finish_reason": finish_reason,
                "message": {"role": "assistant", "content": json.dumps(proposal)},
            }
        ],
        "usage": usage,
        "service_tier": service_tier,
        "openrouter_metadata": {
            "attempt": 1,
            "endpoints": {
                "available": [{"provider": provider, "selected": True}]
            },
        },
    }


class FakeHttpResponse:
    def __init__(self, body, status=200):
        self.body = (
            body if isinstance(body, bytes) else json.dumps(body).encode("utf-8")
        )
        self.status = status

    def read(self):
        return self.body

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return False


def client(open_call, *, cap="5", max_calls=16, attempts=2, budget=None):
    return OpenRouterProposalClient(
        credential=OpenRouterCredential(SECRET, "INHERITED_ENVIRONMENT"),
        budget=(
            budget
            if budget is not None
            else OpenRouterBudgetLedger(
                cap_usd=Decimal(cap),
                max_completed_calls=max_calls,
                max_attempts_per_cell=attempts,
            )
        ),
        open_call=open_call,
    )


def call(client_value, **overrides):
    values = {
        "role": ROLE,
        "case_id": CASE_ID,
        "model_spec": model_spec(),
        "system_prompt": "Return one typed proposal only.",
        "visible_input": {"case_id": CASE_ID, "source": "public"},
        "output_schema": SCHEMA,
        "max_tokens": 100,
        "prompt_version": "TEST_PROMPT_V1",
    }
    values.update(overrides)
    return client_value.call(**values)


class OpenRouterProposalTransportV1Tests(unittest.TestCase):
    def test_request_is_exact_provider_strict_schema_and_toolless(self):
        payload = build_openrouter_proposal_request(
            role=ROLE,
            case_id=CASE_ID,
            model_spec=model_spec(),
            system_prompt="Return one typed proposal only.",
            visible_input={"case_id": CASE_ID},
            output_schema=SCHEMA,
            max_tokens=16000,
        )

        self.assertEqual(payload["model"], "test/model-exact")
        self.assertEqual(payload["provider"]["only"], ["test-provider/fp8"])
        self.assertEqual(
            payload["provider"]["max_price"],
            {"prompt": 0.2, "completion": 1.2, "request": 0.0},
        )
        self.assertFalse(payload["provider"]["allow_fallbacks"])
        self.assertTrue(payload["provider"]["require_parameters"])
        self.assertNotIn("temperature", payload)
        self.assertEqual(payload["reasoning"], {"effort": "low"})
        self.assertEqual(payload["response_format"]["type"], "json_schema")
        self.assertTrue(payload["response_format"]["json_schema"]["strict"])
        self.assertFalse(
            payload["response_format"]["json_schema"]["schema"][
                "additionalProperties"
            ]
        )
        for forbidden in (
            "tools",
            "tool_choice",
            "plugins",
            "models",
            "previous_response_id",
        ):
            self.assertNotIn(forbidden, payload)

    def test_credential_resolution_is_env_then_exact_repo_files_and_never_repr_secret(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / ".env").write_text(
                "UNRELATED=ignore\nOPENROUTER_API_KEY=env-file-secret\n",
                encoding="utf-8",
            )
            (root / ".env.local").write_text(
                "OPENROUTER_API_KEY='local-file-secret'\nOTHER=ignore\n",
                encoding="utf-8",
            )

            inherited = read_openrouter_credential(
                repo_root=root, environment={"OPENROUTER_API_KEY": SECRET}
            )
            local = read_openrouter_credential(repo_root=root, environment={})
            (root / ".env.local").unlink()
            plain = read_openrouter_credential(repo_root=root, environment={})

        self.assertEqual(inherited.source, "INHERITED_ENVIRONMENT")
        self.assertEqual(local.source, "REPOSITORY_ENV_LOCAL")
        self.assertEqual(plain.source, "REPOSITORY_ENV")
        for credential, secret in (
            (inherited, SECRET),
            (local, "local-file-secret"),
            (plain, "env-file-secret"),
        ):
            self.assertNotIn(secret, repr(credential))
            self.assertNotIn(secret, str(credential))

        requests = []
        client_value = client(lambda request, timeout: requests.append(request))
        with self.assertRaisesRegex(
            OpenRouterProposalTransportError,
            "SECRET_DETECTED_IN_REQUEST_PAYLOAD",
        ):
            call(client_value, system_prompt=f"Never persist {SECRET}")
        self.assertEqual(requests, [])

    def test_success_records_complete_receipt_hashes_usage_and_cost_without_secret(self):
        requests = []

        def fake_open(request, timeout):
            requests.append((request, timeout))
            return FakeHttpResponse(response_body())

        client_value = client(fake_open)
        artifact = call(client_value)
        receipt = artifact["receipt"]

        self.assertEqual(len(requests), 1)
        self.assertEqual(receipt["status"], "ADMITTED_TYPED_PROPOSAL")
        self.assertEqual(receipt["response_id"], "gen-test-001")
        self.assertEqual(receipt["finish_reason"], "stop")
        self.assertEqual(receipt["requested_model"], receipt["returned_model"])
        self.assertEqual(receipt["requested_provider_endpoint_tag"], "test-provider/fp8")
        self.assertEqual(receipt["expected_provider_display_name"], receipt["actual_provider"])
        self.assertEqual(receipt["service_tier"], "default")
        self.assertEqual(receipt["provider_provenance_status"], "EXACT_MATCH")
        self.assertEqual(receipt["returned_model_provenance_status"], "EXACT_REQUEST_ID")
        self.assertEqual(receipt["prompt_version"], "TEST_PROMPT_V1")
        self.assertTrue(receipt["recorded_at"].endswith("Z"))
        self.assertEqual(receipt["usage"]["reasoning_tokens"], 3)
        self.assertEqual(receipt["usage"]["cached_tokens"], 2)
        self.assertEqual(receipt["reported_cost_usd"], "0.0001")
        self.assertEqual(receipt["campaign_budget"]["completed_calls"], 1)
        self.assertEqual(receipt["campaign_budget"]["actual_cost_usd"], "0.0001")
        self.assertTrue(receipt["hashes"]["raw_response_sha256"])
        self.assertTrue(receipt["hashes"]["parsed_proposal_sha256"])
        self.assertEqual(
            receipt["prompt_sha256"], receipt["hashes"]["system_prompt_sha256"]
        )
        self.assertEqual(receipt["cost_usd"], receipt["reported_cost_usd"])
        self.assertEqual(artifact["admitted_proposal"], PROPOSAL)
        self.assertEqual(receipt["automatic_retries"], 0)
        serialized = json.dumps(artifact, sort_keys=True)
        self.assertNotIn(SECRET, serialized)
        self.assertNotIn("Authorization", serialized)

    def test_preflight_budget_blocks_before_transport_and_counts_explicit_attempts(self):
        requests = []

        def fake_open(request, timeout):
            requests.append(request)
            return FakeHttpResponse(response_body())

        too_small = client(fake_open, cap="0.000001")
        with self.assertRaisesRegex(
            OpenRouterProposalTransportError,
            "WORST_CASE_NEXT_REQUEST_EXCEEDS_REMAINING_BUDGET",
        ):
            call(too_small)
        self.assertEqual(requests, [])

        two_attempts = client(fake_open, attempts=2)
        call(two_attempts)
        call(two_attempts)
        with self.assertRaisesRegex(
            OpenRouterProposalTransportError, "MAX_ATTEMPTS_FOR_EXACT_CELL_REACHED"
        ):
            call(two_attempts)
        self.assertEqual(two_attempts.budget.completed_calls, 2)

        one_completed = client(fake_open, max_calls=1)
        call(one_completed)
        with self.assertRaisesRegex(
            OpenRouterProposalTransportError, "MAX_COMPLETED_API_CALLS_REACHED"
        ):
            call(
                one_completed,
                case_id="CASE::TWO",
                visible_input={"case_id": "CASE::TWO"},
                output_schema={
                    **SCHEMA,
                    "properties": {
                        **SCHEMA["properties"],
                        "case_id": {"const": "CASE::TWO"},
                    },
                },
            )

    def test_persisted_campaign_accumulates_cost_calls_and_attempts_across_instances(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            state_path = Path(temporary_directory) / "campaign-budget.json"

            def persisted_ledger():
                return OpenRouterBudgetLedger(
                    cap_usd=Decimal("5"),
                    max_completed_calls=16,
                    max_attempts_per_cell=2,
                    campaign_id="LIVE_AGENT_COMMON_FLOWS_V1_20260830",
                    state_path=state_path,
                )

            first = client(
                lambda request, timeout: FakeHttpResponse(response_body(cost=0.0001)),
                budget=persisted_ledger(),
            )
            call(first)
            second = client(
                lambda request, timeout: FakeHttpResponse(response_body(cost=0.0002)),
                budget=persisted_ledger(),
            )
            second_artifact = call(second)
            third_ledger = persisted_ledger()

            self.assertEqual(third_ledger.completed_calls, 2)
            self.assertEqual(third_ledger.actual_cost_usd, Decimal("0.0003"))
            self.assertEqual(
                second_artifact["receipt"]["campaign_budget"]["persistence"],
                "ATOMIC_JSON",
            )
            self.assertEqual(
                second_artifact["receipt"]["campaign_budget"]["campaign_id"],
                "LIVE_AGENT_COMMON_FLOWS_V1_20260830",
            )
            with self.assertRaisesRegex(
                OpenRouterProposalTransportError,
                "MAX_ATTEMPTS_FOR_EXACT_CELL_REACHED",
            ):
                call(
                    client(
                        lambda request, timeout: FakeHttpResponse(response_body()),
                        budget=third_ledger,
                    )
                )

            persisted_text = state_path.read_text(encoding="utf-8")
            persisted_state = json.loads(persisted_text)
            self.assertEqual(persisted_state["completed_calls"], 2)
            self.assertEqual(persisted_state["actual_cost_usd"], "0.0003")
            self.assertEqual(persisted_state["attempts_by_cell"][0]["attempts"], 2)
            self.assertIsNone(persisted_state["inflight_reservation"])
            self.assertNotIn(SECRET, persisted_text)
            self.assertNotIn("Authorization", persisted_text)
            self.assertNotIn("Bearer", persisted_text)

            one_call_path = Path(temporary_directory) / "one-call-budget.json"
            one_call = OpenRouterBudgetLedger(
                cap_usd="5",
                max_completed_calls=1,
                max_attempts_per_cell=2,
                campaign_id="LIVE_AGENT_COMMON_FLOWS_V1_20260830",
                state_path=one_call_path,
            )
            call(
                client(
                    lambda request, timeout: FakeHttpResponse(response_body()),
                    budget=one_call,
                )
            )
            restarted_one_call = OpenRouterBudgetLedger(
                cap_usd="5",
                max_completed_calls=1,
                max_attempts_per_cell=2,
                campaign_id="LIVE_AGENT_COMMON_FLOWS_V1_20260830",
                state_path=one_call_path,
            )
            with self.assertRaisesRegex(
                OpenRouterProposalTransportError,
                "MAX_COMPLETED_API_CALLS_REACHED",
            ):
                restarted_one_call.reserve(
                    role="PLANNER",
                    case_id=CASE_ID,
                    model_id="test/model-exact",
                    worst_case_cost_usd=Decimal("0.1"),
                )

    def test_persisted_campaign_fails_closed_on_unresolved_reservation_or_cost(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            inflight_path = Path(temporary_directory) / "inflight.json"
            first = OpenRouterBudgetLedger(
                cap_usd="5",
                max_completed_calls=16,
                max_attempts_per_cell=2,
                campaign_id="LIVE_AGENT_COMMON_FLOWS_V1_20260830",
                state_path=inflight_path,
            )
            first.reserve(
                role=ROLE,
                case_id=CASE_ID,
                model_id="test/model-exact",
                worst_case_cost_usd=Decimal("0.1"),
            )
            restarted = OpenRouterBudgetLedger(
                cap_usd="5",
                max_completed_calls=16,
                max_attempts_per_cell=2,
                campaign_id="LIVE_AGENT_COMMON_FLOWS_V1_20260830",
                state_path=inflight_path,
            )
            with self.assertRaisesRegex(
                OpenRouterProposalTransportError,
                "BUDGET_BLOCKED_UNRESOLVED_INFLIGHT_RESERVATION",
            ):
                restarted.reserve(
                    role="PLANNER",
                    case_id=CASE_ID,
                    model_id="test/model-exact",
                    worst_case_cost_usd=Decimal("0.1"),
                )

            missing_cost_path = Path(temporary_directory) / "missing-cost.json"
            missing_cost_ledger = OpenRouterBudgetLedger(
                cap_usd="5",
                max_completed_calls=16,
                max_attempts_per_cell=2,
                campaign_id="LIVE_AGENT_COMMON_FLOWS_V1_20260830",
                state_path=missing_cost_path,
            )
            artifact = call(
                client(
                    lambda request, timeout: FakeHttpResponse(
                        response_body(cost=None)
                    ),
                    budget=missing_cost_ledger,
                )
            )
            restarted_missing_cost = OpenRouterBudgetLedger(
                cap_usd="5",
                max_completed_calls=16,
                max_attempts_per_cell=2,
                campaign_id="LIVE_AGENT_COMMON_FLOWS_V1_20260830",
                state_path=missing_cost_path,
            )
            self.assertEqual(artifact["receipt"]["status"], "REJECTED_FAIL_CLOSED")
            with self.assertRaisesRegex(
                OpenRouterProposalTransportError,
                "BUDGET_BLOCKED_PREVIOUS_REPORTED_COST_UNAVAILABLE",
            ):
                restarted_missing_cost.reserve(
                    role="PLANNER",
                    case_id=CASE_ID,
                    model_id="test/model-exact",
                    worst_case_cost_usd=Decimal("0.1"),
                )

    def test_missing_reported_cost_rejects_and_blocks_every_later_call(self):
        client_value = client(
            lambda request, timeout: FakeHttpResponse(response_body(cost=None))
        )
        artifact = call(client_value)

        self.assertEqual(artifact["receipt"]["status"], "REJECTED_FAIL_CLOSED")
        self.assertIn(
            "REPORTED_COST_UNAVAILABLE", artifact["receipt"]["reason_codes"]
        )
        self.assertIsNone(artifact["admitted_proposal"])
        self.assertFalse(client_value.budget.reported_cost_available)
        with self.assertRaisesRegex(
            OpenRouterProposalTransportError,
            "BUDGET_BLOCKED_PREVIOUS_REPORTED_COST_UNAVAILABLE",
        ):
            call(
                client_value,
                case_id="CASE::TWO",
                visible_input={"case_id": "CASE::TWO"},
                output_schema={
                    **SCHEMA,
                    "properties": {
                        **SCHEMA["properties"],
                        "case_id": {"const": "CASE::TWO"},
                    },
                },
            )

    def test_model_or_provider_mismatch_is_rejected_but_charged_once(self):
        accepted_alias = call(
            client(
                lambda request, timeout: FakeHttpResponse(
                    response_body(returned_model="test/model-canonical-202608")
                )
            )
        )
        self.assertEqual(
            accepted_alias["receipt"]["returned_model_provenance_status"],
            "ACCEPTED_CANONICAL_ID",
        )
        self.assertIsNotNone(accepted_alias["admitted_proposal"])

        client_value = client(
            lambda request, timeout: FakeHttpResponse(
                response_body(returned_model="other/model", provider="Other Provider")
            )
        )
        artifact = call(client_value)

        self.assertEqual(artifact["receipt"]["status"], "REJECTED_FAIL_CLOSED")
        self.assertEqual(
            set(artifact["receipt"]["reason_codes"]),
            {"RETURNED_MODEL_MISMATCH", "ACTUAL_PROVIDER_MISMATCH"},
        )
        self.assertIsNone(artifact["admitted_proposal"])
        self.assertEqual(client_value.budget.actual_cost_usd, Decimal("0.0001"))
        self.assertEqual(client_value.budget.completed_calls, 1)

    def test_incomplete_or_invalid_schema_response_never_retries_or_admits(self):
        responses = [
            response_body(finish_reason="length"),
            response_body(proposal={"case_id": CASE_ID, "decision": "FORGED"}),
        ]
        requests = []

        def fake_open(request, timeout):
            requests.append(request)
            return FakeHttpResponse(responses[len(requests) - 1])

        client_value = client(fake_open)
        incomplete = call(client_value)
        invalid = call(client_value)

        self.assertEqual(len(requests), 2)
        self.assertIn("INCOMPLETE_MAX_TOKENS", incomplete["receipt"]["reason_codes"])
        self.assertIsNone(incomplete["admitted_proposal"])
        self.assertIn(
            "PARSED_PROPOSAL_SCHEMA_INVALID", invalid["receipt"]["reason_codes"]
        )
        self.assertIsNone(invalid["admitted_proposal"])
        self.assertEqual(incomplete["receipt"]["automatic_retries"], 0)
        self.assertEqual(invalid["receipt"]["automatic_retries"], 0)

    def test_secret_bearing_http_error_body_is_omitted_and_never_hashed(self):
        provider_shaped_secret = "sk" + "-or-v1-" + "another-secret-99999999"

        def fake_open(request, timeout):
            raise urllib.error.HTTPError(
                request.full_url,
                400,
                "Bad Request",
                {},
                io.BytesIO(
                    f"Authorization: Bearer {SECRET}\n{provider_shaped_secret}".encode(
                        "utf-8"
                    )
                ),
            )

        artifact = call(client(fake_open))
        receipt = artifact["receipt"]

        self.assertIsNone(artifact["raw_response"])
        self.assertEqual(
            receipt["raw_response_persistence_status"], "OMITTED_SECRET_DETECTED"
        )
        self.assertIsNone(receipt["hashes"]["raw_response_sha256"])
        self.assertIn("SECRET_DETECTED_IN_PROVIDER_BODY", receipt["reason_codes"])
        self.assertNotIn(SECRET, json.dumps(artifact, sort_keys=True))


if __name__ == "__main__":
    unittest.main()
