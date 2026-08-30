"""Bounded OpenRouter Profiler/Planner calls on the canonical case runner.

The model is proposal transport only.  This module freezes a small model panel,
adapts strict OpenRouter responses to the existing Profiler and Planner contracts,
and measures development diagnostics after each proposal is frozen.  Rules,
authorization, action execution, reevaluation, and scientific authority remain in
the deterministic repository code.
"""

from __future__ import annotations

import json
import re
from collections.abc import Mapping, Sequence
from copy import deepcopy
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any

from . import case_runner_v1 as runner
from .case_view_v1 import build_case_view
from .openrouter_proposal_transport_v1 import (
    OpenRouterBudgetLedger,
    OpenRouterModelSpec,
    OpenRouterProposalClient,
    OpenRouterProposalTransportError,
    canonical_json_sha256,
    read_openrouter_credential,
    text_sha256,
)
from .profile_proposal_envelope_v1 import (
    ProfileProposalEnvelopeV1Error,
    build_profile_proposal_envelope_schema,
    extract_core_proposal,
    validate_profile_proposal_envelope,
)


REPO_ROOT = Path(__file__).resolve().parents[2]
CAMPAIGN_ROOT = REPO_ROOT / "agent_experiments" / "live_agent_common_flows_v1"
CAMPAIGN_CONFIG_PATH = CAMPAIGN_ROOT / "config" / "live_agent_common_flows_v1.json"
CAMPAIGN_SCHEMA = "live-agent-common-flows-campaign/v1"
COMPARISON_MATRIX_SCHEMA = "live-agent-development-comparison-matrix/v1"
LIVE_AGENT_CAMPAIGN_CLOSED_STATUS = "CLOSED_FROZEN"
LIVE_AGENT_CAMPAIGN_OPEN_STATUS = "AUTHORIZED_FOR_LIVE_CALLS"
LIVE_AGENT_CAMPAIGN_CLOSED_ERROR = (
    "LIVE_AGENT_CAMPAIGN_CLOSED_REQUIRES_NEW_AUTHORIZATION"
)
_TERMINAL_LANGUAGE = re.compile(
    r"(?i)\b(?:SUPPORT_WITHIN_CEILING|CANNOT_SUPPORT_REQUESTED_CLAIM|"
    r"SCIENTIFIC_DISPOSITION|TERMINAL_(?:VERDICT|DISPOSITION)|RULE\s+(?:PASS|FAIL))\b"
)


class LiveAgentCommonFlowsV1Error(ValueError):
    """Raised when live proposal execution would cross a frozen boundary."""


def _read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise LiveAgentCommonFlowsV1Error(f"JSON_ARTIFACT_UNREADABLE:{path.name}") from error
    if not isinstance(value, dict):
        raise LiveAgentCommonFlowsV1Error(f"JSON_OBJECT_REQUIRED:{path.name}")
    return value


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def _prepare_output_root(path: Path) -> Path:
    target = path.resolve()
    if target.exists() and (not target.is_dir() or any(target.iterdir())):
        raise LiveAgentCommonFlowsV1Error("OUTPUT_DIR_MUST_BE_NEW_OR_EMPTY")
    target.mkdir(parents=True, exist_ok=True)
    return target


def _repository_path(raw_path: Any, label: str) -> Path:
    if not isinstance(raw_path, str) or not raw_path:
        raise LiveAgentCommonFlowsV1Error(f"REPOSITORY_PATH_REQUIRED:{label}")
    path = (REPO_ROOT / raw_path).resolve()
    try:
        path.relative_to(REPO_ROOT.resolve())
    except ValueError as error:
        raise LiveAgentCommonFlowsV1Error(f"REPOSITORY_PATH_INVALID:{label}") from error
    if not path.is_file():
        raise LiveAgentCommonFlowsV1Error(f"REPOSITORY_FILE_MISSING:{label}")
    return path


def campaign_budget_ledger_path(config: Mapping[str, Any]) -> Path:
    """Resolve the campaign-owned local ledger without a source-code path binding."""

    raw_path = config.get("budget_ledger_path")
    if not isinstance(raw_path, str) or not raw_path:
        raise LiveAgentCommonFlowsV1Error("CAMPAIGN_BUDGET_LEDGER_PATH_REQUIRED")
    path = (REPO_ROOT / raw_path).resolve()
    try:
        relative = path.relative_to(REPO_ROOT.resolve())
    except ValueError as error:
        raise LiveAgentCommonFlowsV1Error(
            "CAMPAIGN_BUDGET_LEDGER_PATH_INVALID"
        ) from error
    if (
        not relative.parts
        or relative.parts[0] != "local"
        or path.suffix != ".json"
        or (path.exists() and not path.is_file())
    ):
        raise LiveAgentCommonFlowsV1Error("CAMPAIGN_BUDGET_LEDGER_PATH_INVALID")
    return path


def load_campaign_config(path: Path = CAMPAIGN_CONFIG_PATH) -> dict[str, Any]:
    """Load and validate the human-frozen call matrix without reading a credential."""

    config = _read_json(path)
    if config.get("schema_version") != "live-agent-common-flows-campaign-config/v1":
        raise LiveAgentCommonFlowsV1Error("CAMPAIGN_CONFIG_SCHEMA_INVALID")
    if not isinstance(config.get("campaign_id"), str) or not config["campaign_id"]:
        raise LiveAgentCommonFlowsV1Error("CAMPAIGN_ID_REQUIRED")
    try:
        budget_usd = Decimal(str(config.get("budget_usd")))
    except (InvalidOperation, ValueError) as error:
        raise LiveAgentCommonFlowsV1Error("CAMPAIGN_BUDGET_INVALID") from error
    if not budget_usd.is_finite() or budget_usd <= 0:
        raise LiveAgentCommonFlowsV1Error("CAMPAIGN_BUDGET_INVALID")
    max_completed_calls = config.get("max_completed_calls")
    if (
        not isinstance(max_completed_calls, int)
        or isinstance(max_completed_calls, bool)
        or max_completed_calls <= 0
    ):
        raise LiveAgentCommonFlowsV1Error("CAMPAIGN_MAX_CALLS_INVALID")
    max_attempts = config.get("max_attempts_per_exact_role_case_model")
    if (
        not isinstance(max_attempts, int)
        or isinstance(max_attempts, bool)
        or max_attempts <= 0
    ):
        raise LiveAgentCommonFlowsV1Error("CAMPAIGN_MAX_ATTEMPTS_INVALID")
    max_output_tokens = config.get("max_output_tokens")
    if (
        not isinstance(max_output_tokens, int)
        or isinstance(max_output_tokens, bool)
        or max_output_tokens <= 0
    ):
        raise LiveAgentCommonFlowsV1Error("CAMPAIGN_MAX_OUTPUT_TOKENS_INVALID")
    if config.get("automatic_retries") != 0:
        raise LiveAgentCommonFlowsV1Error("AUTOMATIC_RETRY_FORBIDDEN")
    campaign_budget_ledger_path(config)
    cases = config.get("cases")
    roles = config.get("roles")
    models = config.get("models")
    if (
        not isinstance(cases, list)
        or not cases
        or len(cases) != len(set(cases))
        or not set(cases).issubset(set(runner._CASE_PACKET_REGISTRY))
    ):
        raise LiveAgentCommonFlowsV1Error("CAMPAIGN_CASE_SET_INVALID")
    if roles != ["PROFILER", "PLANNER"]:
        raise LiveAgentCommonFlowsV1Error("CAMPAIGN_ROLE_SET_INVALID")
    if not isinstance(models, list) or not models:
        raise LiveAgentCommonFlowsV1Error("CAMPAIGN_MODEL_PANEL_REQUIRED")
    catalog_path = _repository_path(
        config.get("catalog_snapshot_path"), "catalog_snapshot"
    )
    catalog_snapshot = _read_json(catalog_path)
    catalog_hash = canonical_json_sha256(catalog_snapshot)
    if config.get("catalog_snapshot_sha256") != catalog_hash:
        raise LiveAgentCommonFlowsV1Error("CATALOG_SNAPSHOT_HASH_MISMATCH")
    catalog_records = catalog_snapshot.get("records")
    if not isinstance(catalog_records, list):
        raise LiveAgentCommonFlowsV1Error("CATALOG_SNAPSHOT_RECORDS_INVALID")
    catalog_by_model = {
        record.get("model_id"): record
        for record in catalog_records
        if isinstance(record, dict) and isinstance(record.get("model_id"), str)
    }
    if len(catalog_by_model) != len(catalog_records):
        raise LiveAgentCommonFlowsV1Error("CATALOG_SNAPSHOT_MODEL_IDS_INVALID")
    profile_ids: set[str] = set()
    trial_sum = 0
    for entry in models:
        if not isinstance(entry, dict):
            raise LiveAgentCommonFlowsV1Error("CAMPAIGN_MODEL_ENTRY_INVALID")
        profile_id = entry.get("profile_id")
        trials = entry.get("independent_trials_per_case")
        if not isinstance(profile_id, str) or not profile_id or profile_id in profile_ids:
            raise LiveAgentCommonFlowsV1Error("CAMPAIGN_MODEL_PROFILE_ID_INVALID")
        if not isinstance(trials, int) or isinstance(trials, bool) or trials <= 0:
            raise LiveAgentCommonFlowsV1Error("CAMPAIGN_MODEL_TRIAL_COUNT_INVALID")
        profile_ids.add(profile_id)
        trial_sum += trials
        record = catalog_by_model.get(entry.get("model_id"))
        if not isinstance(record, dict):
            raise LiveAgentCommonFlowsV1Error("CAMPAIGN_MODEL_NOT_IN_CATALOG_SNAPSHOT")
        expected_pairs = {
            "provider_endpoint_tag": "provider_endpoint_tag",
            "expected_provider_display_name": "provider_display_name",
            "input_price_per_million_usd": "prompt_price_per_million_usd",
            "output_price_per_million_usd": "completion_price_per_million_usd",
        }
        if any(
            str(entry.get(config_field)) != str(record.get(catalog_field))
            for config_field, catalog_field in expected_pairs.items()
        ):
            raise LiveAgentCommonFlowsV1Error(
                "CAMPAIGN_MODEL_CATALOG_METADATA_MISMATCH"
            )
        accepted = entry.get("accepted_returned_model_ids")
        if record.get("canonical_returned_model_id") not in (
            accepted if isinstance(accepted, list) else []
        ):
            raise LiveAgentCommonFlowsV1Error(
                "CAMPAIGN_CANONICAL_MODEL_ID_NOT_ACCEPTED"
            )
        supported_parameters = record.get("supported_parameters")
        if not isinstance(supported_parameters, list) or not {
            "max_tokens",
            "response_format",
            "structured_outputs",
        }.issubset(set(supported_parameters)):
            raise LiveAgentCommonFlowsV1Error(
                "CAMPAIGN_ENDPOINT_STRICT_OUTPUT_UNSUPPORTED"
            )
        if record.get("status") != 0 or int(config["max_output_tokens"]) > int(
            record.get("max_completion_tokens", 0)
        ):
            raise LiveAgentCommonFlowsV1Error(
                "CAMPAIGN_ENDPOINT_UNAVAILABLE_OR_OUTPUT_LIMIT_INVALID"
            )
        if entry.get("catalog_snapshot_sha256") != catalog_hash:
            raise LiveAgentCommonFlowsV1Error(
                "CAMPAIGN_MODEL_CATALOG_HASH_MISMATCH"
            )
        _model_spec(entry)
    planned_calls = len(cases) * len(roles) * trial_sum
    if planned_calls > config["max_completed_calls"]:
        raise LiveAgentCommonFlowsV1Error("CAMPAIGN_CALL_PLAN_ARITHMETIC_INVALID")
    prompts = config.get("prompts")
    if not isinstance(prompts, dict) or set(prompts) != set(roles):
        raise LiveAgentCommonFlowsV1Error("CAMPAIGN_PROMPT_SET_INVALID")
    for role in roles:
        record = prompts[role]
        if not isinstance(record, dict):
            raise LiveAgentCommonFlowsV1Error(f"CAMPAIGN_PROMPT_RECORD_INVALID:{role}")
        _repository_path(record.get("path"), f"{role}.prompt")
        if not isinstance(record.get("version"), str) or not record["version"]:
            raise LiveAgentCommonFlowsV1Error(f"CAMPAIGN_PROMPT_VERSION_REQUIRED:{role}")
    return config


def require_live_agent_campaign_open(config: Mapping[str, Any]) -> None:
    """Bind every live runtime entry point to the current campaign authority."""

    status = config.get("execution_status")
    if status == LIVE_AGENT_CAMPAIGN_CLOSED_STATUS:
        expected_hash = config.get("completion_receipt_sha256")
        try:
            receipt_path = _repository_path(
                config.get("completion_receipt_path"), "completion_receipt"
            )
            receipt = _read_json(receipt_path)
            receipt_cost = Decimal(str(receipt.get("actual_cost_usd")))
            receipt_cap = Decimal(str(receipt.get("maximum_authorized_cost_usd")))
            config_cap = Decimal(str(config.get("budget_usd")))
        except (InvalidOperation, ValueError, AttributeError) as error:
            raise LiveAgentCommonFlowsV1Error(
                "LIVE_AGENT_CAMPAIGN_COMPLETION_RECEIPT_INVALID"
            ) from error
        completed_calls = receipt.get("completed_api_calls")
        max_completed_calls = receipt.get("maximum_authorized_completed_calls")
        if (
            not isinstance(expected_hash, str)
            or not re.fullmatch(r"[0-9a-f]{64}", expected_hash)
            or canonical_json_sha256(receipt) != expected_hash
            or receipt.get("schema_version")
            != "live-agent-common-flows-campaign-completion/v1"
            or receipt.get("campaign_id") != config.get("campaign_id")
            or receipt.get("campaign_state") != LIVE_AGENT_CAMPAIGN_CLOSED_STATUS
            or not isinstance(completed_calls, int)
            or isinstance(completed_calls, bool)
            or completed_calls < 0
            or not isinstance(max_completed_calls, int)
            or isinstance(max_completed_calls, bool)
            or max_completed_calls != config.get("max_completed_calls")
            or completed_calls > max_completed_calls
            or not receipt_cost.is_finite()
            or receipt_cost < 0
            or not receipt_cap.is_finite()
            or receipt_cap != config_cap
            or receipt_cost > receipt_cap
        ):
            raise LiveAgentCommonFlowsV1Error(
                "LIVE_AGENT_CAMPAIGN_COMPLETION_RECEIPT_INVALID"
            )
        raise LiveAgentCommonFlowsV1Error(LIVE_AGENT_CAMPAIGN_CLOSED_ERROR)
    if status != LIVE_AGENT_CAMPAIGN_OPEN_STATUS:
        raise LiveAgentCommonFlowsV1Error(
            "LIVE_AGENT_CAMPAIGN_EXECUTION_STATUS_INVALID"
        )


def _require_campaign_bound_budget(
    config: Mapping[str, Any], budget: OpenRouterBudgetLedger
) -> None:
    """Reject live execution without one persisted campaign-scoped ledger."""

    if (
        not isinstance(budget, OpenRouterBudgetLedger)
        or not budget.persisted
        or budget.state_path != campaign_budget_ledger_path(config)
        or budget.campaign_id != config.get("campaign_id")
        or budget.cap_usd != Decimal(str(config.get("budget_usd")))
        or budget.max_completed_calls != int(config.get("max_completed_calls", 0))
        or budget.max_attempts_per_cell
        != int(config.get("max_attempts_per_exact_role_case_model", 0))
    ):
        raise LiveAgentCommonFlowsV1Error(
            "CAMPAIGN_BOUND_PERSISTED_BUDGET_REQUIRED"
        )


def _model_spec(entry: Mapping[str, Any]) -> OpenRouterModelSpec:
    try:
        prompt_price = Decimal(str(entry["input_price_per_million_usd"])) / Decimal(
            "1000000"
        )
        completion_price = Decimal(
            str(entry["output_price_per_million_usd"])
        ) / Decimal("1000000")
    except (KeyError, ArithmeticError) as error:
        raise LiveAgentCommonFlowsV1Error("CAMPAIGN_MODEL_PRICE_INVALID") from error
    accepted = entry.get("accepted_returned_model_ids")
    if not isinstance(accepted, list):
        raise LiveAgentCommonFlowsV1Error("CAMPAIGN_ACCEPTED_MODEL_IDS_INVALID")
    return OpenRouterModelSpec(
        model_id=str(entry.get("model_id", "")),
        provider_endpoint_tag=str(entry.get("provider_endpoint_tag", "")),
        expected_provider_display_name=str(
            entry.get("expected_provider_display_name", "")
        ),
        prompt_price_per_token_usd=prompt_price,
        completion_price_per_token_usd=completion_price,
        metadata_sha256=str(entry.get("catalog_snapshot_sha256", "")),
        accepted_returned_model_ids=tuple(accepted),
        allowed_service_tiers=tuple(entry.get("allowed_service_tiers", [])),
        include_temperature_zero=entry.get("include_temperature_zero"),
        reasoning_effort=entry.get("reasoning_effort"),
    )


def _model_entry(config: Mapping[str, Any], profile_id: str) -> dict[str, Any]:
    models = config.get("models")
    if not isinstance(models, list):
        raise LiveAgentCommonFlowsV1Error("CAMPAIGN_MODEL_PANEL_REQUIRED")
    matches = [entry for entry in models if entry.get("profile_id") == profile_id]
    if len(matches) != 1:
        raise LiveAgentCommonFlowsV1Error(f"MODEL_PROFILE_NOT_FROZEN:{profile_id}")
    return deepcopy(matches[0])


def build_planner_proposal_schema(planner_input: Mapping[str, Any]) -> dict[str, Any]:
    """Build a provider-portable strict schema over current legal card IDs.

    Cross-field semantics (SELECT requires one card, ABSTAIN requires none, and
    rationale keys must equal the selected IDs) deliberately remain in the
    deterministic ``validate_planner_proposal`` contract.  Keeping those
    semantics out of top-level conditional branches avoids provider-specific
    JSON-Schema failures without weakening authorization.
    """

    case_id = planner_input.get("case_id")
    cards = planner_input.get("legal_action_cards")
    if not isinstance(case_id, str) or not case_id or not isinstance(cards, list):
        raise LiveAgentCommonFlowsV1Error("PLANNER_VISIBLE_INPUT_INVALID")
    card_ids: list[str] = []
    for card in cards:
        card_id = card.get("card_id") if isinstance(card, Mapping) else None
        if not isinstance(card_id, str) or not card_id or card_id in card_ids:
            raise LiveAgentCommonFlowsV1Error("PLANNER_LEGAL_CARD_SET_INVALID")
        card_ids.append(card_id)
    rationale_variants: list[dict[str, Any]] = [
        {
            "type": "object",
            "additionalProperties": False,
            "required": [],
            "properties": {
            },
        }
    ]
    rationale_variants.extend(
        {
            "type": "object",
            "additionalProperties": False,
            "required": [card_id],
            "properties": {
                card_id: {"type": "string", "minLength": 1},
            },
        }
        for card_id in card_ids
    )
    selected_item_schema: dict[str, Any]
    if card_ids:
        selected_item_schema = {"type": "string", "enum": card_ids}
    else:
        selected_item_schema = {"type": "string"}
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "additionalProperties": False,
        "required": ["case_id", "decision", "selected_card_ids", "rationales"],
        "properties": {
            "case_id": {"type": "string", "const": case_id},
            "decision": {
                "type": "string",
                "enum": ["SELECT_ACTIONS", "ABSTAIN_NO_ACTION"],
            },
            "selected_card_ids": {
                "type": "array",
                "uniqueItems": True,
                "minItems": 0,
                "maxItems": 1 if card_ids else 0,
                "items": selected_item_schema,
            },
            "rationales": {
                "anyOf": rationale_variants,
            },
        },
    }


def _prompt(config: Mapping[str, Any], role: str) -> tuple[str, str]:
    prompts = config["prompts"]
    record = prompts[role]
    path = _repository_path(record["path"], f"{role}.prompt")
    return path.read_text(encoding="utf-8"), str(record["version"])


def _terminal_language_count(value: Any) -> int:
    return len(_TERMINAL_LANGUAGE.findall(json.dumps(value, ensure_ascii=False)))


def _persist_failed_calls(output_dir: Path, calls: Mapping[str, Mapping[str, Any]]) -> None:
    for role, artifact in sorted(calls.items()):
        root = output_dir / "failed_live_calls" / role.lower()
        request_payload = artifact.get("request_payload")
        receipt = artifact.get("receipt")
        raw_response = artifact.get("raw_response")
        admitted_proposal = artifact.get("admitted_proposal")
        if isinstance(request_payload, Mapping):
            _write_json(root / "request_payload.json", dict(request_payload))
        if isinstance(receipt, Mapping):
            _write_json(root / "model_call_receipt.json", dict(receipt))
        if isinstance(raw_response, str):
            root.mkdir(parents=True, exist_ok=True)
            (root / "raw_response.txt").write_text(raw_response, encoding="utf-8")
        if isinstance(admitted_proposal, Mapping):
            _write_json(root / "parsed_model_proposal.json", dict(admitted_proposal))


def _load_frozen_live_profiler_artifact(
    *, artifact_root: Path, case_id: str
) -> dict[str, Any]:
    """Re-admit one already-paid Profiler response without another API call."""

    root = artifact_root.resolve()
    try:
        root.relative_to(REPO_ROOT.resolve())
    except ValueError as error:
        raise LiveAgentCommonFlowsV1Error(
            "FROZEN_PROFILER_ARTIFACT_MUST_BE_IN_REPOSITORY"
        ) from error
    request_payload = _read_json(root / "request_payload.json")
    receipt = _read_json(root / "model_call_receipt.json")
    try:
        raw_response = (root / "raw_response.txt").read_text(encoding="utf-8")
        response = json.loads(raw_response)
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise LiveAgentCommonFlowsV1Error(
            "FROZEN_PROFILER_RAW_RESPONSE_UNREADABLE"
        ) from error
    if receipt.get("role") != "PROFILER" or receipt.get("case_id") != case_id:
        raise LiveAgentCommonFlowsV1Error("FROZEN_PROFILER_RECEIPT_IDENTITY_MISMATCH")
    if receipt.get("status") != "ADMITTED_TYPED_PROPOSAL":
        raise LiveAgentCommonFlowsV1Error("FROZEN_PROFILER_TRANSPORT_NOT_ADMITTED")
    hashes = receipt.get("hashes")
    if not isinstance(hashes, Mapping):
        raise LiveAgentCommonFlowsV1Error("FROZEN_PROFILER_HASHES_REQUIRED")
    if hashes.get("request_payload_sha256") != canonical_json_sha256(request_payload):
        raise LiveAgentCommonFlowsV1Error("FROZEN_PROFILER_REQUEST_HASH_MISMATCH")
    if hashes.get("raw_response_sha256") != text_sha256(raw_response):
        raise LiveAgentCommonFlowsV1Error("FROZEN_PROFILER_RAW_HASH_MISMATCH")
    choices = response.get("choices") if isinstance(response, Mapping) else None
    choice = choices[0] if isinstance(choices, list) and len(choices) == 1 else None
    message = choice.get("message") if isinstance(choice, Mapping) else None
    content = message.get("content") if isinstance(message, Mapping) else None
    refusal = message.get("refusal") if isinstance(message, Mapping) else None
    finish_reason = choice.get("finish_reason") if isinstance(choice, Mapping) else None
    if finish_reason != "stop" or refusal is not None or not isinstance(content, str):
        raise LiveAgentCommonFlowsV1Error("FROZEN_PROFILER_RESPONSE_NOT_REUSABLE")
    try:
        envelope = json.loads(content)
    except json.JSONDecodeError as error:
        raise LiveAgentCommonFlowsV1Error(
            "FROZEN_PROFILER_PROPOSAL_NOT_JSON"
        ) from error
    if not isinstance(envelope, dict) or hashes.get(
        "parsed_proposal_sha256"
    ) != canonical_json_sha256(envelope):
        raise LiveAgentCommonFlowsV1Error("FROZEN_PROFILER_PROPOSAL_HASH_MISMATCH")
    core = extract_core_proposal(envelope)
    packet_path = runner._CASE_PACKET_REGISTRY[case_id]["packet"]
    core_admission = runner.capsule.validate_agent_proposal(packet_path, core)
    if core_admission.get("proposal") != core:
        raise LiveAgentCommonFlowsV1Error("FROZEN_PROFILER_CORE_ADMISSION_DIVERGED")
    receipt = deepcopy(receipt)
    try:
        validate_profile_proposal_envelope(packet_path, envelope)
    except ProfileProposalEnvelopeV1Error as error:
        receipt["field_annotation_validation_status"] = "REJECTED_DIAGNOSTIC_ONLY"
        receipt["field_annotation_error_code"] = str(error).split(":", 1)[0]
    else:
        receipt["field_annotation_validation_status"] = "PASS"
        receipt["field_annotation_error_code"] = None
    return {
        "parsed_proposal": core,
        "proposal_envelope": envelope,
        "call_receipt": receipt,
        "raw_response": raw_response,
        "request_payload": request_payload,
        "admitted_proposal": envelope,
    }


def run_live_agent_case(
    *,
    case_id: str,
    output_dir: Path,
    model_profile: str,
    client: OpenRouterProposalClient,
    config: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Run both live proposal roles through the existing deterministic runner."""

    config = load_campaign_config() if config is None else deepcopy(dict(config))
    require_live_agent_campaign_open(config)
    _require_campaign_bound_budget(config, client.budget)
    if case_id not in config.get("cases", []):
        raise LiveAgentCommonFlowsV1Error("CASE_NOT_IN_FROZEN_LIVE_CAMPAIGN")
    entry = _model_entry(config, model_profile)
    model_spec = _model_spec(entry)
    packet_path = runner._CASE_PACKET_REGISTRY[case_id]["packet"]
    profiler_prompt, profiler_prompt_version = _prompt(config, "PROFILER")
    planner_prompt, planner_prompt_version = _prompt(config, "PLANNER")
    calls: dict[str, dict[str, Any]] = {}

    def profiler_provider(*, role: str, visible_input: Mapping[str, Any]) -> dict[str, Any]:
        if role != "PROFILER":
            raise LiveAgentCommonFlowsV1Error("PROFILER_PROVIDER_ROLE_MISMATCH")
        artifact = client.call(
            role=role,
            case_id=case_id,
            model_spec=model_spec,
            system_prompt=profiler_prompt,
            visible_input=visible_input,
            output_schema=build_profile_proposal_envelope_schema(packet_path),
            max_tokens=int(config["max_output_tokens"]),
            prompt_version=profiler_prompt_version,
        )
        calls[role] = artifact
        envelope = artifact.get("admitted_proposal")
        if not isinstance(envelope, Mapping):
            raise LiveAgentCommonFlowsV1Error("LIVE_PROFILER_RESPONSE_REJECTED")
        core = extract_core_proposal(envelope)
        core_admission = runner.capsule.validate_agent_proposal(packet_path, core)
        if core_admission.get("proposal") != core:
            raise LiveAgentCommonFlowsV1Error("LIVE_PROFILER_CORE_ADMISSION_DIVERGED")
        receipt = deepcopy(dict(artifact["receipt"]))
        try:
            envelope_admission = validate_profile_proposal_envelope(packet_path, envelope)
        except ProfileProposalEnvelopeV1Error as error:
            receipt["field_annotation_validation_status"] = (
                "REJECTED_DIAGNOSTIC_ONLY"
            )
            receipt["field_annotation_error_code"] = str(error).split(":", 1)[0]
        else:
            if envelope_admission.get("core_admission", {}).get("proposal") != core:
                raise LiveAgentCommonFlowsV1Error(
                    "LIVE_PROFILER_CORE_ADMISSION_DIVERGED"
                )
            receipt["field_annotation_validation_status"] = "PASS"
            receipt["field_annotation_error_code"] = None
        return {
            "parsed_proposal": core,
            "proposal_envelope": dict(envelope),
            "call_receipt": receipt,
            "raw_response": artifact["raw_response"],
            "request_payload": artifact["request_payload"],
        }

    def planner_provider(*, role: str, visible_input: Mapping[str, Any]) -> dict[str, Any]:
        if role != "PLANNER":
            raise LiveAgentCommonFlowsV1Error("PLANNER_PROVIDER_ROLE_MISMATCH")
        artifact = client.call(
            role=role,
            case_id=case_id,
            model_spec=model_spec,
            system_prompt=planner_prompt,
            visible_input=visible_input,
            output_schema=build_planner_proposal_schema(visible_input),
            max_tokens=int(config["max_output_tokens"]),
            prompt_version=planner_prompt_version,
        )
        calls[role] = artifact
        proposal = artifact.get("admitted_proposal")
        if not isinstance(proposal, Mapping):
            raise LiveAgentCommonFlowsV1Error("LIVE_PLANNER_RESPONSE_REJECTED")
        if _terminal_language_count(proposal.get("rationales")):
            raise LiveAgentCommonFlowsV1Error(
                "LIVE_PLANNER_RATIONALE_SMUGGLES_TERMINAL_VERDICT"
            )
        return {
            "parsed_proposal": dict(proposal),
            "call_receipt": artifact["receipt"],
            "raw_response": artifact["raw_response"],
            "request_payload": artifact["request_payload"],
        }

    output_dir = output_dir.resolve()
    if output_dir.exists() and (not output_dir.is_dir() or any(output_dir.iterdir())):
        raise LiveAgentCommonFlowsV1Error("OUTPUT_DIR_MUST_BE_NEW_OR_EMPTY")
    try:
        manifest = runner.run_case_v1(
            case_id=case_id,
            output_dir=output_dir,
            profiler_provider=profiler_provider,
            planner_provider=planner_provider,
        )
        view = build_case_view(output_dir).to_dict()
    except Exception as error:
        output_dir.mkdir(parents=True, exist_ok=True)
        _persist_failed_calls(output_dir, calls)
        failure = {
            "schema_version": "live-agent-case-failure/v1",
            "status": "REJECTED_FAIL_CLOSED",
            "case_id": case_id,
            "model_profile": model_profile,
            "error_code": str(error).split(":", 1)[0],
            "completed_roles": sorted(calls),
            "scientific_disposition": "NOT_EVALUATED",
            "claim_upgrade": False,
        }
        _write_json(output_dir / "live_agent_case_failure.json", failure)
        return {"status": "REJECTED_FAIL_CLOSED", "failure": failure, "calls": calls}
    return {
        "status": "SUCCEEDED",
        "manifest": manifest,
        "case_view": view,
        "calls": calls,
    }


def run_frozen_profiler_live_planner_case(
    *,
    case_id: str,
    output_dir: Path,
    frozen_profiler_artifact_root: Path,
    planner_model_profile: str,
    client: OpenRouterProposalClient,
    config: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Reuse a paid, core-admitted Profiler response and call only the Planner."""

    config = load_campaign_config() if config is None else deepcopy(dict(config))
    require_live_agent_campaign_open(config)
    _require_campaign_bound_budget(config, client.budget)
    if case_id not in config.get("cases", []):
        raise LiveAgentCommonFlowsV1Error("CASE_NOT_IN_FROZEN_LIVE_CAMPAIGN")
    entry = _model_entry(config, planner_model_profile)
    model_spec = _model_spec(entry)
    planner_prompt, planner_prompt_version = _prompt(config, "PLANNER")
    profiler_artifact = _load_frozen_live_profiler_artifact(
        artifact_root=frozen_profiler_artifact_root,
        case_id=case_id,
    )
    calls: dict[str, dict[str, Any]] = {"PROFILER": profiler_artifact}

    def profiler_provider(*, role: str, visible_input: Mapping[str, Any]) -> dict[str, Any]:
        if role != "PROFILER":
            raise LiveAgentCommonFlowsV1Error("PROFILER_PROVIDER_ROLE_MISMATCH")
        expected_visible_hash = profiler_artifact["call_receipt"]["hashes"][
            "visible_input_sha256"
        ]
        if canonical_json_sha256(visible_input) != expected_visible_hash:
            raise LiveAgentCommonFlowsV1Error("FROZEN_PROFILER_VISIBLE_INPUT_MISMATCH")
        return {
            key: deepcopy(value)
            for key, value in profiler_artifact.items()
            if key
            in {
                "parsed_proposal",
                "proposal_envelope",
                "call_receipt",
                "raw_response",
                "request_payload",
            }
        }

    def planner_provider(*, role: str, visible_input: Mapping[str, Any]) -> dict[str, Any]:
        if role != "PLANNER":
            raise LiveAgentCommonFlowsV1Error("PLANNER_PROVIDER_ROLE_MISMATCH")
        artifact = client.call(
            role=role,
            case_id=case_id,
            model_spec=model_spec,
            system_prompt=planner_prompt,
            visible_input=visible_input,
            output_schema=build_planner_proposal_schema(visible_input),
            max_tokens=int(config["max_output_tokens"]),
            prompt_version=planner_prompt_version,
        )
        calls[role] = artifact
        proposal = artifact.get("admitted_proposal")
        if not isinstance(proposal, Mapping):
            raise LiveAgentCommonFlowsV1Error("LIVE_PLANNER_RESPONSE_REJECTED")
        if _terminal_language_count(proposal.get("rationales")):
            raise LiveAgentCommonFlowsV1Error(
                "LIVE_PLANNER_RATIONALE_SMUGGLES_TERMINAL_VERDICT"
            )
        return {
            "parsed_proposal": dict(proposal),
            "call_receipt": artifact["receipt"],
            "raw_response": artifact["raw_response"],
            "request_payload": artifact["request_payload"],
        }

    output_dir = output_dir.resolve()
    if output_dir.exists() and (not output_dir.is_dir() or any(output_dir.iterdir())):
        raise LiveAgentCommonFlowsV1Error("OUTPUT_DIR_MUST_BE_NEW_OR_EMPTY")
    try:
        manifest = runner.run_case_v1(
            case_id=case_id,
            output_dir=output_dir,
            profiler_provider=profiler_provider,
            planner_provider=planner_provider,
        )
        view = build_case_view(output_dir).to_dict()
    except Exception as error:
        output_dir.mkdir(parents=True, exist_ok=True)
        _persist_failed_calls(output_dir, calls)
        failure = {
            "schema_version": "live-agent-case-failure/v1",
            "status": "REJECTED_FAIL_CLOSED",
            "case_id": case_id,
            "model_profile": planner_model_profile,
            "error_code": str(error).split(":", 1)[0],
            "completed_roles": sorted(calls),
            "profiler_transport_reused": True,
            "scientific_disposition": "NOT_EVALUATED",
            "claim_upgrade": False,
        }
        _write_json(output_dir / "live_agent_case_failure.json", failure)
        return {"status": "REJECTED_FAIL_CLOSED", "failure": failure, "calls": calls}
    return {
        "status": "SUCCEEDED",
        "manifest": manifest,
        "case_view": view,
        "calls": calls,
        "profiler_transport_reused": True,
    }


def _flatten_critical_profile_fields(proposal: Mapping[str, Any]) -> dict[str, Any]:
    facts = proposal.get("proposed_case_facts")
    if not isinstance(facts, Mapping):
        return {}
    flat: dict[str, Any] = {}
    case = facts.get("case")
    if isinstance(case, Mapping):
        for field, value in case.items():
            flat[f"CASE.{field}"] = value
    sources = facts.get("sources")
    if isinstance(sources, list):
        for source in sources:
            if not isinstance(source, Mapping) or not isinstance(source.get("source_id"), str):
                continue
            source_id = source["source_id"]
            for field, value in source.items():
                if field != "source_id":
                    flat[f"SOURCE.{source_id}.{field}"] = value
    edges = facts.get("edges")
    if isinstance(edges, list):
        for edge in edges:
            if not isinstance(edge, Mapping) or not isinstance(edge.get("edge_id"), str):
                continue
            edge_id = edge["edge_id"]
            for field, value in edge.items():
                if field != "edge_id":
                    flat[f"EDGE.{edge_id}.{field}"] = value
    return flat


def _rule_agreement(live: Sequence[Any], recorded: Sequence[Any]) -> dict[str, Any]:
    def index(values: Sequence[Any]) -> dict[str, Any]:
        return {
            str(item.get("rule_instance_id")): item
            for item in values
            if isinstance(item, Mapping) and isinstance(item.get("rule_instance_id"), str)
        }

    live_by_id = index(live)
    recorded_by_id = index(recorded)
    shared = sorted(set(live_by_id) & set(recorded_by_id))
    matches = sum(
        (
            live_by_id[rule_id].get("status"),
            live_by_id[rule_id].get("reason_codes"),
        )
        == (
            recorded_by_id[rule_id].get("status"),
            recorded_by_id[rule_id].get("reason_codes"),
        )
        for rule_id in shared
    )
    return {
        "shared_rule_instances": len(shared),
        "matching_status_and_reason_instances": matches,
        "rate": matches / len(shared) if shared else None,
        "inventory_match": set(live_by_id) == set(recorded_by_id),
    }


def _live_comparison_row(
    *,
    result: Mapping[str, Any],
    recorded_manifest: Mapping[str, Any],
    case_id: str,
    model_profile: str,
    trial: int,
) -> dict[str, Any]:
    manifest = result["manifest"]
    calls = result["calls"]
    profile = manifest["proposal_provenance"]["profiler"]["live_call_receipt"]
    planner = manifest["proposal_provenance"]["planner"]["live_call_receipt"]
    profile_core_path = runner._CASE_PACKET_REGISTRY[case_id]["profile_proposal"]
    recorded_core = _read_json(profile_core_path)
    live_core = manifest["fresh_rule_state"]["admission"]["proposal"]
    live_flat = _flatten_critical_profile_fields(live_core)
    recorded_flat = _flatten_critical_profile_fields(recorded_core)
    shared_fields = sorted(set(live_flat) & set(recorded_flat))
    exact_matches = sum(live_flat[field] == recorded_flat[field] for field in shared_fields)
    envelope = calls["PROFILER"]["admitted_proposal"]
    annotation_admission = validate_profile_proposal_envelope(
        runner._CASE_PACKET_REGISTRY[case_id]["packet"], envelope
    )
    diagnostic = annotation_admission["diagnostic_summary"]
    unresolved = sum(
        diagnostic["status_counts"][status]
        for status in ("UNKNOWN", "CONFLICTING_SOURCES", "HUMAN_CHECK_REQUIRED")
    )
    annotation_count = diagnostic["annotation_count"]
    live_rules = manifest["fresh_rule_state"]["rule_results"]
    recorded_rules = recorded_manifest["fresh_rule_state"]["rule_results"]
    selected = manifest["planner_admission"]["selected_card_ids"]
    reference_selected = recorded_manifest["planner_admission"]["selected_card_ids"]
    usage = [profile["usage"], planner["usage"]]
    token_totals = {
        field: sum(int(item.get(field, 0) or 0) for item in usage)
        for field in ("prompt_tokens", "completion_tokens", "total_tokens", "reasoning_tokens")
    }
    total_cost = sum(
        Decimal(str(receipt["reported_cost_usd"])) for receipt in (profile, planner)
    )
    return {
        "case_id": case_id,
        "model_profile": model_profile,
        "requested_model": profile["requested_model"],
        "trial": trial,
        "agent_mode": "LIVE_OPENROUTER",
        "schema_admission_rate": 1.0,
        "critical_field_agreement": {
            "matching": exact_matches,
            "shared": len(shared_fields),
            "rate": exact_matches / len(shared_fields) if shared_fields else None,
            "reference": "RECORDED_PROPOSAL_REPLAY_POST_FREEZE_COMPARISON",
        },
        "appropriate_unknown_rate": {
            "unresolved_annotations": unresolved,
            "all_annotations": annotation_count,
            "rate": unresolved / annotation_count if annotation_count else None,
            "status": "CONSISTENCY_VALIDATED_NOT_GOLD_SCORED",
        },
        "evidence_pointer_validity": "PASS",
        "rule_result_agreement": _rule_agreement(live_rules, recorded_rules),
        "legal_route_agreement": selected == reference_selected,
        "live_selected_card_ids": selected,
        "recorded_selected_card_ids": reference_selected,
        "unsafe_claim_upgrade_count": _terminal_language_count(live_core),
        "deterministic_rejection_count": 0,
        "human_correction_count_estimate": len(shared_fields) - exact_matches,
        "calls": 2,
        "tokens": token_totals,
        "cost_usd": str(total_cost),
        "latency_ms": profile["latency_ms"] + planner["latency_ms"],
        "profiler_response_id": profile["response_id"],
        "planner_response_id": planner["response_id"],
        "development_evidence_status": "DEVELOPMENT_DIAGNOSTIC_ONLY",
        "agent_value_status": "NOT_AGENT_VALUE_ESTABLISHED",
        "scientific_authority": "NONE",
    }


def _planned_cells(config: Mapping[str, Any]) -> list[dict[str, Any]]:
    cells: list[dict[str, Any]] = []
    for case_id in config["cases"]:
        for model in config["models"]:
            for trial in range(1, model["independent_trials_per_case"] + 1):
                cells.append(
                    {
                        "case_id": case_id,
                        "model_profile": model["profile_id"],
                        "requested_model": model["model_id"],
                        "trial": trial,
                        "planned_calls": 2,
                    }
                )
    return cells


def run_live_agent_campaign(
    *,
    output_dir: Path,
    environment: Mapping[str, str] | None = None,
    budget: OpenRouterBudgetLedger | None = None,
    config: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Execute the selected frozen campaign or persist a credential block."""

    config = load_campaign_config() if config is None else deepcopy(dict(config))
    require_live_agent_campaign_open(config)
    if budget is None:
        raise LiveAgentCommonFlowsV1Error(
            "CAMPAIGN_BOUND_PERSISTED_BUDGET_REQUIRED"
        )
    _require_campaign_bound_budget(config, budget)
    output_dir = _prepare_output_root(output_dir)
    _write_json(output_dir / "campaign_config_snapshot.json", config)
    recorded: dict[str, dict[str, Any]] = {}
    for case_id in config["cases"]:
        slug = "hsp90" if case_id.startswith("HSP90") else "adk"
        recorded[case_id] = runner.run_case_v1(
            case_id=case_id,
            output_dir=output_dir / "recorded_replay" / slug,
        )

    planned_cells = _planned_cells(config)
    try:
        credential = read_openrouter_credential(
            repo_root=REPO_ROOT, environment=environment
        )
    except OpenRouterProposalTransportError as error:
        if str(error) != "LIVE_CALL_BLOCKED_MISSING_CREDENTIAL":
            raise
        rows = [
            {
                **cell,
                "result_status": "LIVE_CALL_BLOCKED_MISSING_CREDENTIAL",
                "completed_calls": 0,
                "actual_cost_usd": "0",
            }
            for cell in planned_cells
        ]
        matrix = {
            "schema_version": COMPARISON_MATRIX_SCHEMA,
            "status": "LIVE_CALL_BLOCKED_MISSING_CREDENTIAL",
            "comparison_arms": [
                "NO_AGENT_PLATFORM_AUTHORITY_ONLY_NOT_EXECUTED",
                "RECORDED_PROPOSAL_REPLAY",
                "LIVE_OPENROUTER_BLOCKED",
            ],
            "rows": rows,
            "development_evidence_status": "DEVELOPMENT_DIAGNOSTIC_ONLY",
            "agent_value_status": "NOT_AGENT_VALUE_ESTABLISHED",
        }
        _write_json(output_dir / "live_agent_comparison_matrix.json", matrix)
        manifest = {
            "schema_version": CAMPAIGN_SCHEMA,
            "status": "LIVE_CALL_BLOCKED_MISSING_CREDENTIAL",
            "credential_handling": {
                "attempted_sources": [
                    "INHERITED_ENVIRONMENT",
                    "REPOSITORY_ROOT_DOT_ENV_LOCAL",
                    "REPOSITORY_ROOT_DOT_ENV",
                ],
                "key_value_persisted": False,
                "unrelated_locations_scanned": False,
            },
            "completed_api_calls": 0,
            "actual_cost_usd": "0",
            "recorded_replay_cases": sorted(recorded),
            "live_cells": rows,
            "source_science_review_status": "PENDING_DOMAIN_REVIEW",
            "broad_hsp90_closure_status": "NOT_ESTABLISHED",
            "held_out_status": "NOT_ACCESSED",
            "claim_ceiling": "DEVELOPMENT_DIAGNOSTIC_ONLY; NOT_AGENT_VALUE_ESTABLISHED",
        }
        _write_json(output_dir / "live_agent_campaign_manifest.json", manifest)
        return manifest

    client = OpenRouterProposalClient(credential=credential, budget=budget)
    rows: list[dict[str, Any]] = []
    for cell in planned_cells:
        case_id = cell["case_id"]
        slug = "hsp90" if case_id.startswith("HSP90") else "adk"
        cell_root = (
            output_dir
            / "live_runs"
            / slug
            / cell["model_profile"]
            / f"trial-{cell['trial']}"
        )
        result = run_live_agent_case(
            case_id=case_id,
            output_dir=cell_root,
            model_profile=cell["model_profile"],
            client=client,
            config=config,
        )
        if result["status"] == "SUCCEEDED":
            rows.append(
                {
                    **_live_comparison_row(
                        result=result,
                        recorded_manifest=recorded[case_id],
                        case_id=case_id,
                        model_profile=cell["model_profile"],
                        trial=cell["trial"],
                    ),
                    "result_status": "SUCCEEDED",
                    "artifact_root": cell_root.relative_to(output_dir).as_posix(),
                }
            )
        else:
            completed_receipts = [
                artifact.get("receipt")
                for artifact in result["calls"].values()
                if isinstance(artifact, Mapping)
                and isinstance(artifact.get("receipt"), Mapping)
                and artifact["receipt"].get("transport_status") == "COMPLETED_RESPONSE"
            ]
            cell_cost = sum(
                Decimal(str(receipt.get("reported_cost_usd") or "0"))
                for receipt in completed_receipts
            )
            rows.append(
                {
                    **cell,
                    "result_status": "REJECTED_FAIL_CLOSED",
                    "error_code": result["failure"]["error_code"],
                    "completed_calls": len(completed_receipts),
                    "actual_cost_usd": str(cell_cost),
                    "deterministic_rejection_count": 1,
                    "scientific_authority": "NONE",
                }
            )
    succeeded = sum(row["result_status"] == "SUCCEEDED" for row in rows)
    status = "COMPLETE" if succeeded == len(rows) else "COMPLETE_WITH_FAIL_CLOSED_REJECTIONS"
    matrix = {
        "schema_version": COMPARISON_MATRIX_SCHEMA,
        "status": status,
        "comparison_arms": [
            "NO_AGENT_PLATFORM_AUTHORITY_ONLY_NOT_EXECUTED",
            "RECORDED_PROPOSAL_REPLAY",
            "LIVE_OPENROUTER",
        ],
        "rows": rows,
        "development_evidence_status": "DEVELOPMENT_DIAGNOSTIC_ONLY",
        "agent_value_status": "NOT_AGENT_VALUE_ESTABLISHED",
    }
    _write_json(output_dir / "live_agent_comparison_matrix.json", matrix)
    manifest = {
        "schema_version": CAMPAIGN_SCHEMA,
        "status": status,
        "credential_handling": {
            "source": credential.source,
            "key_value_persisted": False,
            "unrelated_locations_scanned": False,
        },
        "completed_api_calls": budget.completed_calls,
        "actual_cost_usd": str(budget.actual_cost_usd),
        "budget": budget.snapshot(),
        "successful_live_case_runs": succeeded,
        "planned_live_case_runs": len(rows),
        "live_cells": rows,
        "source_science_review_status": "PENDING_DOMAIN_REVIEW",
        "broad_hsp90_closure_status": "NOT_ESTABLISHED",
        "held_out_status": "NOT_ACCESSED",
        "claim_ceiling": "DEVELOPMENT_DIAGNOSTIC_ONLY; NOT_AGENT_VALUE_ESTABLISHED",
    }
    _write_json(output_dir / "live_agent_campaign_manifest.json", manifest)
    return manifest


__all__ = [
    "CAMPAIGN_CONFIG_PATH",
    "LiveAgentCommonFlowsV1Error",
    "build_planner_proposal_schema",
    "campaign_budget_ledger_path",
    "load_campaign_config",
    "require_live_agent_campaign_open",
    "run_live_agent_campaign",
    "run_live_agent_case",
    "run_frozen_profiler_live_planner_case",
]
