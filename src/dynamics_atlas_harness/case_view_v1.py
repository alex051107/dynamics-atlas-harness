"""Artifact-only read model for exposed Dynamics Atlas development cases.

``build_case_view`` accepts either a recorded capsule case directory or a
``case_runner_v1`` run directory.  It validates the artifact links it follows and
copies recorded values into a UI-friendly read model.  It performs no Rule
evaluation, action execution, or terminal scientific-state calculation.
"""

from __future__ import annotations

import hashlib
import json
from copy import deepcopy
from dataclasses import asdict, dataclass
from decimal import Decimal, InvalidOperation
from pathlib import Path, PurePosixPath
from typing import Any

from .paper_blind_exposed_v1 import PaperBlindPublicPacketError, validate_agent_proposal
from .proposal_provenance_v1 import (
    CALLER_SUPPLIED_IN_MEMORY,
    LIVE_OPENROUTER_PROPOSAL,
    RECORDED_PROPOSAL_REPLAY,
    ProposalProvenanceV1Error,
    build_proposal_provenance_v1,
    canonical_json_sha256,
)
from .profile_proposal_envelope_v1 import (
    ProfileProposalEnvelopeV1Error,
    build_profile_proposal_envelope_schema,
    extract_core_proposal,
    validate_profile_proposal_envelope,
)
from .live_agent_decision_closure_v1 import (
    ACTION_CARD_ID as DECISION_CLOSURE_ACTION_CARD_ID,
    MANIFEST_SCHEMA as DECISION_CLOSURE_MANIFEST_SCHEMA,
    POSITIVE_ARM_ID as DECISION_CLOSURE_POSITIVE_ARM_ID,
    PROFILE_MODE as DECISION_CLOSURE_PROFILE_MODE,
    STOP_ARM_ID as DECISION_CLOSURE_STOP_ARM_ID,
    TARGET_RULE_INSTANCE_ID as DECISION_CLOSURE_TARGET_RULE_ID,
    validate_planner_proposal as validate_decision_closure_planner_proposal,
)


REPO_ROOT = Path(__file__).resolve().parents[2]

_CASE_RUNNER_BOUNDARY = (
    "This runner records exposed-development proposals and deterministic downstream behavior only. "
    "It does not compute a terminal verdict, source-science approval, broad "
    "HSP90 closure, ADK dynamics portability, or Agent effectiveness."
)
_CASE_RUNNER_MANIFEST_INVARIANTS = {
    "schema_version": "dynamics-atlas-case-run/v1",
    "run_scope": "EXPOSED_DEVELOPMENT_ONLY",
    "terminal_scientific_state": "NOT_CALCULATED_BY_CASE_RUNNER",
    "scientific_disposition": "NOT_EVALUATED",
    "source_science_review_status": "PENDING_DOMAIN_REVIEW",
    "boundary": _CASE_RUNNER_BOUNDARY,
}


class CaseViewIntegrityError(ValueError):
    """Raised when a CaseView cannot faithfully project its artifact graph."""

    def __init__(self, code: str, detail: str | None = None) -> None:
        self.code = code
        self.detail = detail
        message = code if detail is None else f"{code}:{detail}"
        super().__init__(message)


def unavailable(reason: str) -> dict[str, str]:
    """Return the explicit sentinel used for optional absent artifacts."""

    return {"availability": "UNAVAILABLE", "reason": reason}


@dataclass(frozen=True)
class CaseView:
    """Validated projection of recorded case/run artifacts.

    Collections remain JSON-shaped because the sole consumer is a static HTML
    renderer.  ``to_dict`` returns a deep copy so callers cannot mutate this read
    model and mistake that mutation for canonical scientific state.
    """

    schema_version: str
    case_id: str
    artifact_kind: str
    artifact_root_name: str
    integrity_status: str
    question: Any
    current_gate: Any
    claim_ceiling: Any
    sources_and_locators: Any
    agent_proposal: Any
    admitted_facts: Any
    rule_instances: list[dict[str, Any]]
    rule_results: list[dict[str, Any]]
    unresolved_obligations: list[dict[str, Any]]
    legal_action_cards: list[dict[str, Any]]
    planner_proposal: Any
    authorization: Any
    executed_actions: Any
    receipts: Any
    descriptive_evidence_no_active_rule_effect: list[dict[str, Any]]
    active_rule_evidence: list[dict[str, Any]]
    exact_control_regression: Any
    before_after_rule_result_links: Any
    conclusion_packet: Any
    human_review_state: Any
    terminal_scientific_state: Any
    boundary: str

    def to_dict(self) -> dict[str, Any]:
        return deepcopy(asdict(self))


def _read_object(path: Path, label: str, *, required: bool = True) -> dict[str, Any] | None:
    if not path.is_file():
        if required:
            raise CaseViewIntegrityError("REQUIRED_ARTIFACT_MISSING", label)
        return None
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise CaseViewIntegrityError("ARTIFACT_MALFORMED", label) from error
    if not isinstance(value, dict):
        raise CaseViewIntegrityError("ARTIFACT_OBJECT_REQUIRED", label)
    return value


def _require_object(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise CaseViewIntegrityError("OBJECT_REQUIRED", label)
    return value


def _require_list(value: Any, label: str) -> list[Any]:
    if not isinstance(value, list):
        raise CaseViewIntegrityError("LIST_REQUIRED", label)
    return value


def _require_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise CaseViewIntegrityError("NONEMPTY_STRING_REQUIRED", label)
    return value.strip()


def _canonical_json_text(value: Any) -> str:
    try:
        return json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
    except (TypeError, ValueError) as error:
        raise CaseViewIntegrityError("LIVE_JSON_VALUE_INVALID") from error


def _text_sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _planner_live_output_schema(planner_input: dict[str, Any]) -> dict[str, Any]:
    """Independently rebuild the current strict Planner proposal schema."""

    case_id = _require_string(planner_input.get("case_id"), "planner_input.case_id")
    cards = _require_list(
        planner_input.get("legal_action_cards"), "planner_input.legal_action_cards"
    )
    card_ids: list[str] = []
    for position, raw_card in enumerate(cards):
        card = _require_object(raw_card, f"planner_input.legal_action_cards[{position}]")
        card_id = _require_string(card.get("card_id"), f"legal_action_cards[{position}].card_id")
        if card_id in card_ids:
            raise CaseViewIntegrityError("DUPLICATE_LIVE_PLANNER_CARD_ID", card_id)
        card_ids.append(card_id)
    rationale_variants: list[dict[str, Any]] = [
        {
            "type": "object",
            "additionalProperties": False,
            "required": [],
            "properties": {},
        }
    ]
    rationale_variants.extend(
        {
            "type": "object",
            "additionalProperties": False,
            "required": [card_id],
            "properties": {card_id: {"type": "string", "minLength": 1}},
        }
        for card_id in card_ids
    )
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
                "items": (
                    {"type": "string", "enum": card_ids}
                    if card_ids
                    else {"type": "string"}
                ),
            },
            "rationales": {"anyOf": rationale_variants},
        },
    }


def _receipt_hash(
    *,
    receipt: dict[str, Any],
    hashes: dict[str, Any],
    hash_field: str,
    alias_field: str,
    observed: str,
    code: str,
) -> None:
    if hashes.get(hash_field) != observed or receipt.get(alias_field) != observed:
        raise CaseViewIntegrityError(code)


def _nonnegative_decimal(value: Any, code: str) -> Decimal:
    if isinstance(value, bool):
        raise CaseViewIntegrityError(code)
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError) as error:
        raise CaseViewIntegrityError(code) from error
    if not result.is_finite() or result < 0:
        raise CaseViewIntegrityError(code)
    return result


def _raw_openrouter_provider(response: dict[str, Any]) -> str | None:
    for candidate in (response.get("provider"), response.get("provider_name")):
        if isinstance(candidate, str) and candidate.strip():
            return candidate.strip()
    metadata = response.get("openrouter_metadata")
    if not isinstance(metadata, dict):
        return None
    for candidate in (metadata.get("provider"), metadata.get("provider_name")):
        if isinstance(candidate, str) and candidate.strip():
            return candidate.strip()
    endpoints = metadata.get("endpoints")
    available = endpoints.get("available") if isinstance(endpoints, dict) else None
    if isinstance(available, list):
        for endpoint in available:
            if isinstance(endpoint, dict) and endpoint.get("selected") is True:
                provider = endpoint.get("provider")
                if isinstance(provider, str) and provider.strip():
                    return provider.strip()
    return None


def _raw_usage_receipt(response: dict[str, Any]) -> dict[str, Any]:
    usage = response.get("usage")
    if not isinstance(usage, dict):
        raise CaseViewIntegrityError("LIVE_RAW_USAGE_OBJECT_REQUIRED")

    def required_count(field: str) -> int:
        value = usage.get(field)
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            raise CaseViewIntegrityError("LIVE_RAW_USAGE_COUNT_INVALID", field)
        return value

    def optional_count(container_name: str, field: str) -> int | None:
        container = usage.get(container_name)
        if not isinstance(container, dict):
            return None
        value = container.get(field)
        return (
            value
            if isinstance(value, int) and not isinstance(value, bool) and value >= 0
            else None
        )

    cost = _nonnegative_decimal(usage.get("cost"), "LIVE_RAW_REPORTED_COST_INVALID")
    return {
        "prompt_tokens": required_count("prompt_tokens"),
        "completion_tokens": required_count("completion_tokens"),
        "total_tokens": required_count("total_tokens"),
        "reasoning_tokens": optional_count(
            "completion_tokens_details", "reasoning_tokens"
        ),
        "cached_tokens": optional_count("prompt_tokens_details", "cached_tokens"),
        "reported_cost_usd": str(cost),
    }


def _verify_live_openrouter_semantics(
    *,
    role: str,
    visible_input: dict[str, Any],
    parsed_proposal: dict[str, Any],
    request_payload: dict[str, Any],
    raw_response: str,
    live_receipt: dict[str, Any],
    proposal_envelope: dict[str, Any] | None,
    public_packet_source: Path,
) -> None:
    """Bind one live request, provider response, receipt, and routed proposal."""

    hashes = _require_object(live_receipt.get("hashes"), f"{role}.live_call_hashes")
    if hashes.get("canonicalization") != "SORTED_KEYS_COMPACT_JSON_UTF8_V1":
        raise CaseViewIntegrityError("LIVE_HASH_CANONICALIZATION_INVALID", role)

    messages = _require_list(request_payload.get("messages"), f"{role}.messages")
    if len(messages) != 2:
        raise CaseViewIntegrityError("LIVE_REQUEST_MESSAGE_STRUCTURE_INVALID", role)
    system_message = _require_object(messages[0], f"{role}.messages[0]")
    user_message = _require_object(messages[1], f"{role}.messages[1]")
    if set(system_message) != {"role", "content"} or set(user_message) != {
        "role",
        "content",
    }:
        raise CaseViewIntegrityError("LIVE_REQUEST_MESSAGE_STRUCTURE_INVALID", role)
    if system_message.get("role") != "system" or user_message.get("role") != "user":
        raise CaseViewIntegrityError("LIVE_REQUEST_MESSAGE_STRUCTURE_INVALID", role)
    system_prompt = _require_string(
        system_message.get("content"), f"{role}.system_prompt"
    )
    expected_user_content = "Task packet:\n" + _canonical_json_text(visible_input)
    if user_message.get("content") != expected_user_content:
        raise CaseViewIntegrityError("LIVE_REQUEST_VISIBLE_INPUT_MISMATCH", role)

    receipt_prompt_sha = hashes.get("system_prompt_sha256")
    if receipt_prompt_sha != live_receipt.get("prompt_sha256") or receipt_prompt_sha not in {
        _text_sha256(system_prompt),
        # Early campaign prompts were read from newline-terminated text files;
        # request construction stripped that one trailing newline before sending.
        _text_sha256(system_prompt + "\n"),
    }:
        raise CaseViewIntegrityError("LIVE_SYSTEM_PROMPT_HASH_MISMATCH", role)
    visible_sha = canonical_json_sha256(visible_input)
    _receipt_hash(
        receipt=live_receipt,
        hashes=hashes,
        hash_field="visible_input_sha256",
        alias_field="visible_input_sha256",
        observed=visible_sha,
        code="LIVE_VISIBLE_INPUT_HASH_MISMATCH",
    )

    response_format = _require_object(
        request_payload.get("response_format"), f"{role}.response_format"
    )
    if set(response_format) != {"type", "json_schema"} or response_format.get(
        "type"
    ) != "json_schema":
        raise CaseViewIntegrityError("LIVE_RESPONSE_FORMAT_INVALID", role)
    json_schema = _require_object(
        response_format.get("json_schema"), f"{role}.response_format.json_schema"
    )
    if set(json_schema) != {"name", "strict", "schema"}:
        raise CaseViewIntegrityError("LIVE_RESPONSE_FORMAT_INVALID", role)
    if json_schema.get("name") != f"dynamics_atlas_{role}_proposal":
        raise CaseViewIntegrityError("LIVE_RESPONSE_SCHEMA_NAME_MISMATCH", role)
    if json_schema.get("strict") is not True:
        raise CaseViewIntegrityError("LIVE_RESPONSE_SCHEMA_NOT_STRICT", role)
    output_schema = _require_object(
        json_schema.get("schema"), f"{role}.response_format.json_schema.schema"
    )
    expected_schema = (
        build_profile_proposal_envelope_schema(public_packet_source)
        if role == "PROFILER"
        else _planner_live_output_schema(visible_input)
    )
    if output_schema != expected_schema:
        raise CaseViewIntegrityError("LIVE_OUTPUT_SCHEMA_CURRENT_CONTRACT_MISMATCH", role)
    schema_sha = canonical_json_sha256(output_schema)
    _receipt_hash(
        receipt=live_receipt,
        hashes=hashes,
        hash_field="output_schema_sha256",
        alias_field="schema_sha256",
        observed=schema_sha,
        code="LIVE_OUTPUT_SCHEMA_HASH_MISMATCH",
    )

    parameter_profile = _require_object(
        live_receipt.get("request_parameter_profile"),
        f"{role}.request_parameter_profile",
    )
    if set(parameter_profile) != {"temperature_zero_included", "reasoning_effort"}:
        raise CaseViewIntegrityError("LIVE_REQUEST_PARAMETER_PROFILE_INVALID", role)
    temperature_included = parameter_profile.get("temperature_zero_included")
    if not isinstance(temperature_included, bool):
        raise CaseViewIntegrityError("LIVE_REQUEST_PARAMETER_PROFILE_INVALID", role)
    reasoning_effort = parameter_profile.get("reasoning_effort")
    if reasoning_effort is not None and (
        not isinstance(reasoning_effort, str) or not reasoning_effort
    ):
        raise CaseViewIntegrityError("LIVE_REQUEST_PARAMETER_PROFILE_INVALID", role)

    allowed_request_fields = {
        "model",
        "messages",
        "max_tokens",
        "stream",
        "response_format",
        "provider",
    }
    if temperature_included:
        allowed_request_fields.add("temperature")
        if (
            isinstance(request_payload.get("temperature"), bool)
            or request_payload.get("temperature") != 0
        ):
            raise CaseViewIntegrityError("LIVE_REQUEST_TEMPERATURE_MISMATCH", role)
    elif "temperature" in request_payload:
        raise CaseViewIntegrityError("LIVE_REQUEST_TEMPERATURE_MISMATCH", role)
    if reasoning_effort is not None:
        allowed_request_fields.add("reasoning")
        if request_payload.get("reasoning") != {"effort": reasoning_effort}:
            raise CaseViewIntegrityError("LIVE_REQUEST_REASONING_MISMATCH", role)
    elif "reasoning" in request_payload:
        raise CaseViewIntegrityError("LIVE_REQUEST_REASONING_MISMATCH", role)
    if "usage" in request_payload:
        allowed_request_fields.add("usage")
        if request_payload.get("usage") != {"include": True}:
            raise CaseViewIntegrityError("LIVE_REQUEST_USAGE_PARAMETER_INVALID", role)
    if set(request_payload) != allowed_request_fields:
        raise CaseViewIntegrityError("LIVE_REQUEST_FIELDS_INVALID_OR_TOOL_INJECTION", role)

    if request_payload.get("model") != live_receipt.get("requested_model"):
        raise CaseViewIntegrityError("LIVE_REQUEST_MODEL_MISMATCH", role)
    if request_payload.get("stream") is not False:
        raise CaseViewIntegrityError("LIVE_REQUEST_STREAMING_FORBIDDEN", role)
    max_tokens = request_payload.get("max_tokens")
    if not isinstance(max_tokens, int) or isinstance(max_tokens, bool) or max_tokens <= 0:
        raise CaseViewIntegrityError("LIVE_REQUEST_MAX_TOKENS_INVALID", role)
    provider = _require_object(request_payload.get("provider"), f"{role}.provider")
    if set(provider) != {
        "allow_fallbacks",
        "require_parameters",
        "only",
        "max_price",
    }:
        raise CaseViewIntegrityError("LIVE_REQUEST_PROVIDER_FIELDS_INVALID", role)
    if provider.get("allow_fallbacks") is not False or provider.get(
        "require_parameters"
    ) is not True:
        raise CaseViewIntegrityError("LIVE_REQUEST_PROVIDER_POLICY_INVALID", role)
    if provider.get("only") != [live_receipt.get("requested_provider_endpoint_tag")]:
        raise CaseViewIntegrityError("LIVE_REQUEST_PROVIDER_ONLY_MISMATCH", role)
    max_price = _require_object(provider.get("max_price"), f"{role}.provider.max_price")
    if set(max_price) != {"prompt", "completion", "request"}:
        raise CaseViewIntegrityError("LIVE_REQUEST_MAX_PRICE_INVALID", role)
    prompt_price = _nonnegative_decimal(
        max_price.get("prompt"), "LIVE_REQUEST_MAX_PRICE_INVALID"
    )
    completion_price = _nonnegative_decimal(
        max_price.get("completion"), "LIVE_REQUEST_MAX_PRICE_INVALID"
    )
    request_price = _nonnegative_decimal(
        max_price.get("request"), "LIVE_REQUEST_MAX_PRICE_INVALID"
    )

    request_sha = canonical_json_sha256(request_payload)
    _receipt_hash(
        receipt=live_receipt,
        hashes=hashes,
        hash_field="request_payload_sha256",
        alias_field="request_sha256",
        observed=request_sha,
        code="LIVE_REQUEST_PAYLOAD_HASH_MISMATCH",
    )
    preflight = _require_object(live_receipt.get("preflight"), f"{role}.preflight")
    input_ceiling = len(_canonical_json_text(request_payload).encode("utf-8"))
    if (
        preflight.get("input_token_ceiling_basis")
        != "CANONICAL_REQUEST_UTF8_BYTE_COUNT"
        or preflight.get("input_token_ceiling") != input_ceiling
        or preflight.get("max_completion_tokens") != max_tokens
    ):
        raise CaseViewIntegrityError("LIVE_REQUEST_PREFLIGHT_MISMATCH", role)
    expected_worst_cost = (
        prompt_price * Decimal(input_ceiling) / Decimal("1000000")
        + completion_price * Decimal(max_tokens) / Decimal("1000000")
        + request_price
    )
    if _nonnegative_decimal(
        preflight.get("worst_case_cost_usd"), "LIVE_REQUEST_PREFLIGHT_MISMATCH"
    ) != expected_worst_cost:
        raise CaseViewIntegrityError("LIVE_REQUEST_PREFLIGHT_MISMATCH", role)

    try:
        raw = json.loads(raw_response)
    except json.JSONDecodeError as error:
        raise CaseViewIntegrityError("LIVE_RAW_RESPONSE_JSON_INVALID", role) from error
    if not isinstance(raw, dict):
        raise CaseViewIntegrityError("LIVE_RAW_RESPONSE_OBJECT_REQUIRED", role)
    raw_sha = _text_sha256(raw_response)
    _receipt_hash(
        receipt=live_receipt,
        hashes=hashes,
        hash_field="raw_response_sha256",
        alias_field="raw_response_sha256",
        observed=raw_sha,
        code="LIVE_RAW_RESPONSE_HASH_MISMATCH",
    )
    if raw.get("id") != live_receipt.get("response_id"):
        raise CaseViewIntegrityError("LIVE_RAW_RESPONSE_ID_MISMATCH", role)
    if raw.get("model") != live_receipt.get("returned_model"):
        raise CaseViewIntegrityError("LIVE_RAW_RESPONSE_MODEL_MISMATCH", role)
    if _raw_openrouter_provider(raw) != live_receipt.get("actual_provider"):
        raise CaseViewIntegrityError("LIVE_RAW_RESPONSE_PROVIDER_MISMATCH", role)
    if raw.get("service_tier") != live_receipt.get("service_tier"):
        raise CaseViewIntegrityError("LIVE_RAW_RESPONSE_SERVICE_TIER_MISMATCH", role)
    http_status = live_receipt.get("http_status")
    if not isinstance(http_status, int) or isinstance(http_status, bool) or not 200 <= http_status < 300:
        raise CaseViewIntegrityError("LIVE_RECEIPT_HTTP_STATUS_INVALID", role)

    choices = raw.get("choices")
    if not isinstance(choices, list) or len(choices) != 1:
        raise CaseViewIntegrityError("LIVE_RAW_RESPONSE_CHOICE_STRUCTURE_INVALID", role)
    choice = _require_object(choices[0], f"{role}.raw_response.choices[0]")
    if choice.get("finish_reason") != live_receipt.get("finish_reason"):
        raise CaseViewIntegrityError("LIVE_RAW_RESPONSE_FINISH_REASON_MISMATCH", role)
    message = _require_object(choice.get("message"), f"{role}.raw_response.message")
    if message.get("role") != "assistant" or any(
        field in message for field in ("tool_calls", "function_call")
    ):
        raise CaseViewIntegrityError("LIVE_RAW_RESPONSE_MESSAGE_INVALID", role)
    if message.get("refusal") not in (None, "") or live_receipt.get(
        "refusal_status"
    ) != "NOT_REPORTED":
        raise CaseViewIntegrityError("LIVE_RAW_RESPONSE_REFUSAL_MISMATCH", role)
    content = message.get("content")
    if not isinstance(content, str):
        raise CaseViewIntegrityError("LIVE_RAW_RESPONSE_CONTENT_REQUIRED", role)
    try:
        parsed_content = json.loads(content)
    except json.JSONDecodeError as error:
        raise CaseViewIntegrityError("LIVE_RAW_RESPONSE_CONTENT_JSON_INVALID", role) from error
    if not isinstance(parsed_content, dict):
        raise CaseViewIntegrityError("LIVE_RAW_RESPONSE_CONTENT_OBJECT_REQUIRED", role)
    expected_content = proposal_envelope if role == "PROFILER" else parsed_proposal
    if parsed_content != expected_content:
        raise CaseViewIntegrityError("LIVE_RAW_RESPONSE_CONTENT_PROPOSAL_MISMATCH", role)
    parsed_sha = canonical_json_sha256(parsed_content)
    _receipt_hash(
        receipt=live_receipt,
        hashes=hashes,
        hash_field="parsed_proposal_sha256",
        alias_field="parsed_proposal_sha256",
        observed=parsed_sha,
        code="LIVE_RAW_PARSED_PROPOSAL_HASH_MISMATCH",
    )
    if live_receipt.get("routing_proposal_sha256") != canonical_json_sha256(
        parsed_proposal
    ):
        raise CaseViewIntegrityError("LIVE_ROUTING_PROPOSAL_HASH_MISMATCH", role)
    if role == "PROFILER" and live_receipt.get(
        "proposal_envelope_sha256"
    ) != canonical_json_sha256(proposal_envelope):
        raise CaseViewIntegrityError("LIVE_PROFILER_ENVELOPE_HASH_MISMATCH", role)

    raw_usage = _raw_usage_receipt(raw)
    if live_receipt.get("usage") != raw_usage:
        raise CaseViewIntegrityError("LIVE_RAW_RESPONSE_USAGE_MISMATCH", role)
    reported_cost = raw_usage["reported_cost_usd"]
    if (
        live_receipt.get("reported_cost_usd") != reported_cost
        or live_receipt.get("cost_usd") != reported_cost
    ):
        raise CaseViewIntegrityError("LIVE_RAW_RESPONSE_COST_MISMATCH", role)


def _assert_case_id(value: Any, case_id: str, label: str) -> None:
    if value != case_id:
        raise CaseViewIntegrityError("CROSS_CASE_ARTIFACT", label)


def _rule_identity(result: dict[str, Any], label: str) -> dict[str, Any]:
    rule_instance_id = _require_string(result.get("rule_instance_id"), f"{label}.rule_instance_id")
    runtime_subrule_id = _require_string(
        result.get("runtime_subrule_id"), f"{label}.runtime_subrule_id"
    )
    target = _require_object(result.get("target"), f"{label}.target")
    _require_string(target.get("kind"), f"{label}.target.kind")
    _require_string(target.get("id"), f"{label}.target.id")
    return {
        "rule_instance_id": rule_instance_id,
        "runtime_subrule_id": runtime_subrule_id,
        "target": deepcopy(target),
    }


def _rule_index(results: Any, label: str) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    raw_results = _require_list(results, label)
    normalized: list[dict[str, Any]] = []
    by_id: dict[str, dict[str, Any]] = {}
    for position, raw in enumerate(raw_results):
        result = _require_object(raw, f"{label}[{position}]")
        identity = _rule_identity(result, f"{label}[{position}]")
        rule_id = identity["rule_instance_id"]
        if rule_id in by_id:
            raise CaseViewIntegrityError("DUPLICATE_RULE_INSTANCE_ID", rule_id)
        copied = deepcopy(result)
        normalized.append(copied)
        by_id[rule_id] = copied
    return normalized, by_id


def _safe_repository_reference(raw_path: Any, label: str) -> Path:
    relative = _require_string(raw_path, label)
    posix = PurePosixPath(relative)
    if posix.is_absolute() or ".." in posix.parts:
        raise CaseViewIntegrityError("UNSAFE_ARTIFACT_REFERENCE", label)
    candidate = (REPO_ROOT / Path(*posix.parts)).resolve()
    try:
        candidate.relative_to(REPO_ROOT.resolve())
    except ValueError as error:
        raise CaseViewIntegrityError("UNSAFE_ARTIFACT_REFERENCE", label) from error
    if not candidate.is_file():
        raise CaseViewIntegrityError("STALE_ARTIFACT_REFERENCE", label)
    return candidate


def _proposal_from_receipt(receipt: dict[str, Any], case_id: str, label: str) -> dict[str, Any]:
    path = _safe_repository_reference(receipt.get("recorded_proposal_path"), f"{label}.path")
    expected_sha = _require_string(receipt.get("recorded_proposal_sha256"), f"{label}.sha256")
    observed_sha = hashlib.sha256(path.read_bytes()).hexdigest()
    if observed_sha != expected_sha:
        raise CaseViewIntegrityError("STALE_ARTIFACT_REFERENCE_HASH", label)
    proposal = _read_object(path, label)
    assert proposal is not None
    _assert_case_id(proposal.get("case_id"), case_id, label)
    return proposal


def _input_snapshot(
    *,
    loaded: dict[str, dict[str, Any]],
    input_provenance: dict[str, Any],
    snapshot_name: str,
    case_id: str,
) -> dict[str, Any]:
    records = _require_object(
        input_provenance.get("snapshot_artifacts"), "input_provenance.snapshot_artifacts"
    )
    record = _require_object(
        records.get(snapshot_name), f"input_provenance.snapshot_artifacts.{snapshot_name}"
    )
    path = _require_string(record.get("path"), f"snapshot_artifacts.{snapshot_name}.path")
    value = loaded.get(path)
    if value is None:
        raise CaseViewIntegrityError("REQUIRED_INPUT_SNAPSHOT_MISSING", snapshot_name)
    expected_sha = _require_string(
        record.get("canonical_sha256"),
        f"snapshot_artifacts.{snapshot_name}.canonical_sha256",
    )
    if canonical_json_sha256(value) != expected_sha:
        raise CaseViewIntegrityError("STALE_INPUT_SNAPSHOT_HASH", snapshot_name)
    if "case_id" in value:
        _assert_case_id(value.get("case_id"), case_id, snapshot_name)
    return deepcopy(value)


def _verify_proposal_receipt(
    *,
    receipt: dict[str, Any],
    case_id: str,
    role: str,
    mode: Any,
    source_path: Any,
    visible_input: dict[str, Any],
    parsed_proposal: dict[str, Any],
    admission_evaluation: dict[str, Any],
    loaded: dict[str, Any],
    public_packet_source: Path,
) -> None:
    _assert_case_id(receipt.get("case_id"), case_id, f"{role}.proposal_provenance")
    if receipt.get("role") != role:
        raise CaseViewIntegrityError("PROPOSAL_RECEIPT_ROLE_MISMATCH", role)
    if receipt.get("mode") != mode:
        raise CaseViewIntegrityError("PROPOSAL_RECEIPT_MODE_MISMATCH", role)
    if receipt.get("source_path") != source_path:
        raise CaseViewIntegrityError("PROPOSAL_RECEIPT_SOURCE_PATH_MISMATCH", role)
    checks = (
        (receipt.get("visible_input"), visible_input, "visible_input"),
        (receipt.get("parsed_proposal"), parsed_proposal, "parsed_proposal"),
        (
            receipt.get("contract_admission_evaluation"),
            admission_evaluation,
            "contract_admission_evaluation",
        ),
    )
    for raw_record, value, label in checks:
        record = _require_object(raw_record, f"{role}.{label}")
        expected = _require_string(
            record.get("canonical_sha256"), f"{role}.{label}.canonical_sha256"
        )
        if canonical_json_sha256(value) != expected:
            raise CaseViewIntegrityError("STALE_PROPOSAL_RECEIPT_HASH", f"{role}.{label}")
    if mode == RECORDED_PROPOSAL_REPLAY:
        _verify_repository_source_snapshot(
            snapshot=parsed_proposal,
            source_path=source_path,
            label=f"{role}.recorded_proposal",
            source_required_code="RECORDED_PROPOSAL_SOURCE_REQUIRED",
        )
    elif mode == CALLER_SUPPLIED_IN_MEMORY:
        if source_path is not None:
            raise CaseViewIntegrityError("IN_MEMORY_PROPOSAL_SOURCE_FORBIDDEN", role)
    elif mode == LIVE_OPENROUTER_PROPOSAL:
        if source_path is not None:
            raise CaseViewIntegrityError("LIVE_PROPOSAL_SOURCE_FORBIDDEN", role)
        live_receipt = _require_object(
            receipt.get("live_call_receipt"), f"{role}.live_call_receipt"
        )
        live_root = f"live_calls/{role.lower()}"
        standalone_receipt = loaded.get(f"{live_root}/model_call_receipt.json")
        if standalone_receipt != live_receipt:
            raise CaseViewIntegrityError("LIVE_CALL_RECEIPT_ARTIFACT_MISMATCH", role)
        request_payload = loaded.get(f"{live_root}/request_payload.json")
        if not isinstance(request_payload, dict):
            raise CaseViewIntegrityError("LIVE_REQUEST_PAYLOAD_ARTIFACT_MISSING", role)
        expected_request_sha = _require_string(
            _require_object(live_receipt.get("hashes"), f"{role}.live_call_hashes").get(
                "request_payload_sha256"
            ),
            f"{role}.request_payload_sha256",
        )
        if canonical_json_sha256(request_payload) != expected_request_sha:
            raise CaseViewIntegrityError("LIVE_REQUEST_PAYLOAD_HASH_MISMATCH", role)
        raw_response = loaded.get(f"{live_root}/raw_response.txt")
        if not isinstance(raw_response, str):
            raise CaseViewIntegrityError("LIVE_RAW_RESPONSE_ARTIFACT_MISSING", role)
        observed_raw_sha = hashlib.sha256(raw_response.encode("utf-8")).hexdigest()
        expected_raw_sha = _require_string(
            _require_object(live_receipt.get("hashes"), f"{role}.live_call_hashes").get(
                "raw_response_sha256"
            ),
            f"{role}.raw_response_sha256",
        )
        if observed_raw_sha != expected_raw_sha:
            raise CaseViewIntegrityError("LIVE_RAW_RESPONSE_HASH_MISMATCH", role)
        envelope = loaded.get(f"{live_root}/proposal_envelope.json")
        if role == "PROFILER":
            if not isinstance(envelope, dict):
                raise CaseViewIntegrityError("LIVE_PROFILER_ENVELOPE_REQUIRED")
            expected_envelope_sha = _require_string(
                live_receipt.get("proposal_envelope_sha256"),
                "PROFILER.proposal_envelope_sha256",
            )
            if canonical_json_sha256(envelope) != expected_envelope_sha:
                raise CaseViewIntegrityError("LIVE_PROFILER_ENVELOPE_HASH_MISMATCH")
            annotation_status = live_receipt.get(
                "field_annotation_validation_status"
            )
            annotation_error = live_receipt.get("field_annotation_error_code")
            try:
                envelope_admission = validate_profile_proposal_envelope(
                    public_packet_source, envelope
                )
            except ProfileProposalEnvelopeV1Error as error:
                observed_error = str(error).split(":", 1)[0]
                if (
                    annotation_status != "REJECTED_DIAGNOSTIC_ONLY"
                    or annotation_error != observed_error
                ):
                    raise CaseViewIntegrityError(
                        "LIVE_PROFILER_ANNOTATION_DIAGNOSTIC_DIVERGED"
                    ) from error
                envelope_admission = None
            else:
                if annotation_status != "PASS" or annotation_error is not None:
                    raise CaseViewIntegrityError(
                        "LIVE_PROFILER_ANNOTATION_STATUS_DIVERGED"
                    )
            if extract_core_proposal(envelope) != parsed_proposal:
                raise CaseViewIntegrityError("LIVE_PROFILER_ROUTING_CORE_MISMATCH")
            observed_core_admission = validate_agent_proposal(
                public_packet_source, parsed_proposal
            )
            if observed_core_admission != admission_evaluation:
                raise CaseViewIntegrityError("LIVE_PROFILER_CORE_ADMISSION_MISMATCH")
            if (
                envelope_admission is not None
                and envelope_admission.get("core_admission") != admission_evaluation
            ):
                raise CaseViewIntegrityError("LIVE_PROFILER_CORE_ADMISSION_MISMATCH")
        elif envelope is not None or live_receipt.get("proposal_envelope_sha256") is not None:
            raise CaseViewIntegrityError("LIVE_PLANNER_ENVELOPE_FORBIDDEN")
        _verify_live_openrouter_semantics(
            role=role,
            visible_input=visible_input,
            parsed_proposal=parsed_proposal,
            request_payload=request_payload,
            raw_response=raw_response,
            live_receipt=live_receipt,
            proposal_envelope=envelope if isinstance(envelope, dict) else None,
            public_packet_source=public_packet_source,
        )
    else:
        raise CaseViewIntegrityError("PROPOSAL_MODE_INVALID", role)
    evaluator = (
        "validate_agent_proposal" if role == "PROFILER" else "validate_planner_proposal"
    )
    try:
        expected_receipt = build_proposal_provenance_v1(
            role=role,
            mode=mode,
            visible_input=visible_input,
            parsed_proposal=parsed_proposal,
            contract_evaluator=evaluator,
            contract_admission_evaluation=admission_evaluation,
            source_path=source_path,
            live_call_receipt=(
                receipt.get("live_call_receipt")
                if mode == LIVE_OPENROUTER_PROPOSAL
                else None
            ),
        )
    except ProposalProvenanceV1Error as error:
        raise CaseViewIntegrityError("PROPOSAL_RECEIPT_CONTRACT_INVALID", role) from error
    if receipt != expected_receipt:
        raise CaseViewIntegrityError("PROPOSAL_RECEIPT_CONTENT_MISMATCH", role)


def _verify_repository_source_snapshot(
    *,
    snapshot: dict[str, Any],
    source_path: Any,
    label: str,
    source_required_code: str,
) -> Path:
    if source_path is None:
        raise CaseViewIntegrityError(source_required_code, label)
    source_path_resolved = _safe_repository_reference(source_path, label)
    source = _read_object(source_path_resolved, label)
    assert source is not None
    if source != snapshot:
        raise CaseViewIntegrityError("REPOSITORY_SOURCE_SNAPSHOT_MISMATCH", label)
    return source_path_resolved


def _validate_case_runner_manifest(manifest: dict[str, Any]) -> None:
    for field, expected in _CASE_RUNNER_MANIFEST_INVARIANTS.items():
        observed = manifest.get(field)
        if type(observed) is not type(expected) or observed != expected:
            raise CaseViewIntegrityError("CASE_RUNNER_MANIFEST_INVARIANT_MISMATCH", field)
    input_provenance = _require_object(
        manifest.get("input_provenance"), "manifest.input_provenance"
    )
    modes = (
        input_provenance.get("profile_mode"),
        input_provenance.get("planner_mode"),
    )
    allowed_modes = {
        RECORDED_PROPOSAL_REPLAY,
        CALLER_SUPPLIED_IN_MEMORY,
        LIVE_OPENROUTER_PROPOSAL,
    }
    if any(mode not in allowed_modes for mode in modes):
        raise CaseViewIntegrityError("CASE_RUNNER_PROPOSAL_MODE_INVALID")
    live_count = sum(mode == LIVE_OPENROUTER_PROPOSAL for mode in modes)
    expected_agent_mode = (
        "LIVE_OPENROUTER"
        if live_count == 2
        else (
            "MIXED_RECORDED_OR_IN_MEMORY_AND_LIVE"
            if live_count == 1
            else "RECORDED_OR_IN_MEMORY"
        )
    )
    if manifest.get("agent_mode") != expected_agent_mode:
        raise CaseViewIntegrityError(
            "CASE_RUNNER_MANIFEST_INVARIANT_MISMATCH", "agent_mode"
        )
    for field in ("network_accessed", "credentials_accessed", "external_model_transport"):
        observed = manifest.get(field)
        if not isinstance(observed, bool) or observed is not bool(live_count):
            raise CaseViewIntegrityError(
                "CASE_RUNNER_MANIFEST_INVARIANT_MISMATCH", field
            )


def _expected_profiler_visible_input(public_packet: dict[str, Any]) -> dict[str, Any]:
    required = (
        "packet_id",
        "case_id",
        "research_question",
        "source_materials",
        "data_assets",
        "agent_proposal_schema",
    )
    for field in required:
        if field not in public_packet:
            raise CaseViewIntegrityError("PUBLIC_PACKET_VISIBLE_INPUT_FIELD_MISSING", field)
    return {
        "schema_version": "paper-blind-agent-visible-input/v1",
        **{field: deepcopy(public_packet[field]) for field in required},
    }


def _planner_admission_consistency(
    *,
    case_id: str,
    planner_proposal: dict[str, Any],
    planner_admission: dict[str, Any],
) -> None:
    required_proposal_fields = {"case_id", "decision", "selected_card_ids", "rationales"}
    if set(planner_proposal) != required_proposal_fields:
        raise CaseViewIntegrityError("PLANNER_PROPOSAL_FIELDS_INVALID")
    _assert_case_id(planner_proposal.get("case_id"), case_id, "planner_proposal")
    decision = planner_proposal.get("decision")
    selected = [
        _require_string(value, "planner_proposal.selected_card_id")
        for value in _require_list(
            planner_proposal.get("selected_card_ids"), "planner_proposal.selected_card_ids"
        )
    ]
    if len(selected) != len(set(selected)):
        raise CaseViewIntegrityError("DUPLICATE_SELECTED_CARD_ID")
    if (decision == "SELECT_ACTIONS" and len(selected) != 1) or (
        decision == "ABSTAIN_NO_ACTION" and selected
    ):
        raise CaseViewIntegrityError("PLANNER_PROPOSAL_SELECTION_STATE_MISMATCH")
    if decision not in {"SELECT_ACTIONS", "ABSTAIN_NO_ACTION"}:
        raise CaseViewIntegrityError("PLANNER_PROPOSAL_DECISION_INVALID")
    rationales = _require_object(planner_proposal.get("rationales"), "planner_proposal.rationales")
    if set(rationales) != set(selected):
        raise CaseViewIntegrityError("PLANNER_PROPOSAL_RATIONALE_SET_MISMATCH")
    normalized_rationales = {
        card_id: _require_string(rationales[card_id], f"planner_proposal.rationale.{card_id}")
        for card_id in selected
    }
    expected_admission = {
        "schema_version": "paper-blind-planner-proposal-admission/v2",
        "proposal_status": "ADMISSIBLE_CARD_SELECTION_ONLY",
        "case_id": case_id,
        "decision": decision,
        "selected_card_ids": selected,
        "rationales": normalized_rationales,
        "execution_authorization": "AUTHORIZED_EXACT_SELECTED_CAPSULE_ACTIONS_ONLY",
        "scientific_disposition": "NOT_EVALUATED",
    }
    if planner_admission != expected_admission:
        raise CaseViewIntegrityError("PLANNER_ADMISSION_PROPOSAL_MISMATCH")


def _public_packet_consistency(
    *, manifest: dict[str, Any], public_packet: dict[str, Any]
) -> None:
    if manifest.get("research_question") != public_packet.get("research_question"):
        raise CaseViewIntegrityError("PUBLIC_PACKET_QUESTION_MISMATCH")
    authority = _require_object(
        public_packet.get("platform_authority_envelope"),
        "public_case_packet.platform_authority_envelope",
    )
    packet_claim_boundary = _require_object(
        authority.get("claim_boundary"),
        "public_case_packet.platform_authority_envelope.claim_boundary",
    )
    if manifest.get("claim_boundary") != packet_claim_boundary:
        raise CaseViewIntegrityError("PUBLIC_PACKET_CLAIM_BOUNDARY_MISMATCH")


def _evidence_lanes(evidence_results: Any, case_id: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    descriptive: list[dict[str, Any]] = []
    active: list[dict[str, Any]] = []
    for position, raw in enumerate(_require_list(evidence_results, "evidence_results")):
        evidence = _require_object(raw, f"evidence_results[{position}]")
        if "case_id" in evidence:
            _assert_case_id(evidence.get("case_id"), case_id, f"evidence_results[{position}]")
        descriptive_result = evidence.get("descriptive_result")
        nested_effect = (
            descriptive_result.get("rule_effect")
            if isinstance(descriptive_result, dict)
            else None
        )
        is_descriptive = (
            evidence.get("rule_effect") == "NO_ACTIVE_RULE_EFFECT"
            or nested_effect == "NO_ACTIVE_RULE_EFFECT"
            or evidence.get("action_kind") == "DESCRIPTIVE_ANALYSIS_ONLY"
        )
        is_active = (
            evidence.get("rule_effect") == "ACTIVE_RULE_EFFECT"
            or evidence.get("active_rule_effect") == "ACTIVE_RULE_EFFECT"
        )
        if is_descriptive and is_active:
            raise CaseViewIntegrityError("EVIDENCE_EFFECT_MARKERS_CONFLICT")
        if is_descriptive:
            if evidence.get("affected_rule_instance_id") is not None:
                raise CaseViewIntegrityError("DESCRIPTIVE_EVIDENCE_LINKED_ACTIVE_RULE")
            if evidence.get("active_rule_effect") not in (None, "NO_ACTIVE_RULE_EFFECT"):
                raise CaseViewIntegrityError("DESCRIPTIVE_EVIDENCE_HAS_ACTIVE_RULE_EFFECT")
            descriptive.append(deepcopy(evidence))
        elif is_active:
            _require_string(
                evidence.get("evidence_result_id"),
                f"evidence_results[{position}].evidence_result_id",
            )
            _require_string(
                evidence.get("affected_rule_instance_id"),
                f"evidence_results[{position}].affected_rule_instance_id",
            )
            active.append(deepcopy(evidence))
        else:
            raise CaseViewIntegrityError("EVIDENCE_EFFECT_CLASSIFICATION_UNKNOWN")
    return descriptive, active


def _validated_reevaluation_links(
    *,
    reevaluation: dict[str, Any],
    before_by_id: dict[str, dict[str, Any]],
    after_by_id: dict[str, dict[str, Any]],
    active_evidence: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    for rule_id in before_by_id:
        if _rule_identity(before_by_id[rule_id], "before_rule_result") != _rule_identity(
            after_by_id[rule_id], "after_rule_result"
        ):
            raise CaseViewIntegrityError("RULE_INSTANCE_IDENTITY_CHANGED", rule_id)

    changed_ids = {
        rule_id for rule_id in before_by_id if before_by_id[rule_id] != after_by_id[rule_id]
    }
    raw_reevaluated = _require_list(
        reevaluation.get("reevaluated_rule_instance_ids"),
        "rule_reevaluation.reevaluated_rule_instance_ids",
    )
    reevaluated_ids = [
        _require_string(value, "reevaluated_rule_instance_id") for value in raw_reevaluated
    ]
    if len(reevaluated_ids) != len(set(reevaluated_ids)):
        raise CaseViewIntegrityError("DUPLICATE_REEVALUATED_RULE_INSTANCE_ID")
    if set(reevaluated_ids) != changed_ids:
        raise CaseViewIntegrityError("REEVALUATED_RULE_CHANGE_SET_MISMATCH")

    active_by_id: dict[str, dict[str, Any]] = {}
    active_targets: dict[str, str] = {}
    for evidence in active_evidence:
        evidence_id = _require_string(
            evidence.get("evidence_result_id"), "active_evidence.evidence_result_id"
        )
        affected = _require_string(
            evidence.get("affected_rule_instance_id"),
            "active_evidence.affected_rule_instance_id",
        )
        if evidence_id in active_by_id:
            raise CaseViewIntegrityError("DUPLICATE_ACTIVE_EVIDENCE_RESULT_ID", evidence_id)
        if affected in active_targets.values():
            raise CaseViewIntegrityError("MULTIPLE_ACTIVE_EVIDENCE_FOR_RULE_INSTANCE", affected)
        active_by_id[evidence_id] = evidence
        active_targets[evidence_id] = affected

    links: list[dict[str, Any]] = []
    linked_rule_ids: set[str] = set()
    linked_evidence_ids: set[str] = set()
    for position, raw in enumerate(
        _require_list(reevaluation.get("evidence_links"), "rule_reevaluation.evidence_links")
    ):
        link = _require_object(raw, f"evidence_links[{position}]")
        affected = _require_string(
            link.get("affected_rule_instance_id"),
            f"evidence_links[{position}].affected_rule_instance_id",
        )
        evidence_id = _require_string(
            link.get("evidence_result_id"), f"evidence_links[{position}].evidence_result_id"
        )
        if affected in linked_rule_ids or evidence_id in linked_evidence_ids:
            raise CaseViewIntegrityError("DUPLICATE_RULE_REEVALUATION_LINK")
        if affected not in before_by_id or affected not in after_by_id:
            raise CaseViewIntegrityError("STALE_RULE_RESULT_LINK", affected)
        if active_targets.get(evidence_id) != affected:
            raise CaseViewIntegrityError("ACTIVE_EVIDENCE_LINK_MISMATCH", evidence_id)
        if link.get("same_rule_instance") is not True:
            raise CaseViewIntegrityError("SAME_RULE_INSTANCE_ATTESTATION_REQUIRED", affected)
        if link.get("before_status") != before_by_id[affected].get("status"):
            raise CaseViewIntegrityError("REEVALUATION_BEFORE_STATUS_MISMATCH", affected)
        if link.get("after_status") != after_by_id[affected].get("status"):
            raise CaseViewIntegrityError("REEVALUATION_AFTER_STATUS_MISMATCH", affected)
        linked_rule_ids.add(affected)
        linked_evidence_ids.add(evidence_id)
        links.append(deepcopy(link))

    if linked_rule_ids != changed_ids or linked_evidence_ids != set(active_by_id):
        raise CaseViewIntegrityError("ACTIVE_EVIDENCE_REEVALUATION_LINK_SET_MISMATCH")
    return links


def _selected_card_consistency(
    *,
    case_id: str,
    planner_input: dict[str, Any],
    planner_admission: dict[str, Any],
    execution: dict[str, Any],
) -> None:
    _assert_case_id(planner_input.get("case_id"), case_id, "planner_visible_input")
    _assert_case_id(planner_admission.get("case_id"), case_id, "planner_admission")
    _assert_case_id(execution.get("case_id"), case_id, "selected_action_execution")
    legal_cards = _require_list(planner_input.get("legal_action_cards"), "legal_action_cards")
    legal_ids: set[str] = set()
    for position, raw in enumerate(legal_cards):
        card = _require_object(raw, f"legal_action_cards[{position}]")
        _assert_case_id(card.get("case_id"), case_id, f"legal_action_cards[{position}]")
        legal_ids.add(_require_string(card.get("card_id"), f"legal_action_cards[{position}].card_id"))
    admitted = [
        _require_string(value, "planner_admission.selected_card_id")
        for value in _require_list(
            planner_admission.get("selected_card_ids"),
            "planner_admission.selected_card_ids",
        )
    ]
    executed = [
        _require_string(value, "execution.selected_card_id")
        for value in _require_list(
            execution.get("selected_card_ids"), "execution.selected_card_ids"
        )
    ]
    if len(admitted) != len(set(admitted)):
        raise CaseViewIntegrityError("DUPLICATE_SELECTED_CARD_ID")
    if admitted != executed:
        raise CaseViewIntegrityError("STALE_SELECTED_CARD_REFERENCE")
    if any(card_id not in legal_ids for card_id in admitted):
        raise CaseViewIntegrityError("STALE_LEGAL_ACTION_CARD_REFERENCE")
    evidence = _require_list(execution.get("evidence_results"), "execution.evidence_results")
    evidence_card_ids = [
        _require_string(_require_object(item, "evidence_result").get("card_id"), "evidence_result.card_id")
        for item in evidence
    ]
    if admitted != evidence_card_ids:
        raise CaseViewIntegrityError("STALE_EXECUTED_ACTION_REFERENCE")
    decision = planner_admission.get("decision")
    if admitted:
        if decision != "SELECT_ACTIONS" or len(admitted) != 1:
            raise CaseViewIntegrityError("PLANNER_ADMISSION_SELECTION_STATE_MISMATCH")
        expected_execution_status = "SELECTED_ACTIONS_EXECUTED"
    else:
        if decision != "ABSTAIN_NO_ACTION":
            raise CaseViewIntegrityError("PLANNER_ADMISSION_SELECTION_STATE_MISMATCH")
        expected_execution_status = "NO_ACTION_SELECTED"
    if execution.get("execution_status") != expected_execution_status:
        raise CaseViewIntegrityError("EXECUTION_STATUS_MISMATCH")


def _authorization_consistency(
    *,
    case_id: str,
    planner_admission: dict[str, Any],
    authorization: dict[str, Any],
    execution: dict[str, Any],
) -> None:
    _assert_case_id(authorization.get("case_id"), case_id, "planner_authorization")
    admitted = _require_list(
        planner_admission.get("selected_card_ids"), "planner_admission.selected_card_ids"
    )
    authorized = _require_list(
        authorization.get("selected_card_ids"), "authorization.selected_card_ids"
    )
    if authorized != admitted:
        raise CaseViewIntegrityError("AUTHORIZATION_SELECTION_MISMATCH")
    expected_status = (
        "AUTHORIZED_EXACTLY_ONE_SELECTED_CARD"
        if admitted
        else "AUTHORIZED_ABSTENTION_ZERO_ACTIONS"
    )
    if authorization.get("schema_version") != "case-runner-authorization/v1":
        raise CaseViewIntegrityError("AUTHORIZATION_SCHEMA_VERSION_MISMATCH")
    if authorization.get("status") != expected_status:
        raise CaseViewIntegrityError("AUTHORIZATION_STATUS_MISMATCH")
    evidence = _require_list(execution.get("evidence_results"), "execution.evidence_results")
    executed_action_count = authorization.get("executed_action_count")
    if (
        not isinstance(executed_action_count, int)
        or isinstance(executed_action_count, bool)
        or executed_action_count != len(evidence)
    ):
        raise CaseViewIntegrityError("AUTHORIZATION_EXECUTED_ACTION_COUNT_MISMATCH")


def _build_capsule_case_view(root: Path) -> CaseView:
    artifacts = {
        name: _read_object(root / f"{name}.json", name)
        for name in (
            "human_decision_packet",
            "agent_visible_input",
            "arm_b_recorded_profile_rules",
            "planner_visible_input",
            "planner_proposal_admission",
            "arm_c_selected_public_actions",
            "profiler_proposal_provenance",
            "planner_proposal_provenance",
            "unresolved_obligation_classification",
            "asset_identity_verification",
        )
    }
    packet = artifacts["human_decision_packet"]
    assert packet is not None
    case_id = _require_string(packet.get("case_id"), "human_decision_packet.case_id")
    for name in (
        "agent_visible_input",
        "planner_visible_input",
        "planner_proposal_admission",
        "unresolved_obligation_classification",
        "asset_identity_verification",
    ):
        artifact = artifacts[name]
        assert artifact is not None
        _assert_case_id(artifact.get("case_id"), case_id, name)

    profile_rules = artifacts["arm_b_recorded_profile_rules"]
    planner_input = artifacts["planner_visible_input"]
    planner_admission = artifacts["planner_proposal_admission"]
    selected = artifacts["arm_c_selected_public_actions"]
    unresolved = artifacts["unresolved_obligation_classification"]
    profiler_receipt = artifacts["profiler_proposal_provenance"]
    planner_receipt = artifacts["planner_proposal_provenance"]
    assert all(
        value is not None
        for value in (
            profile_rules,
            planner_input,
            planner_admission,
            selected,
            unresolved,
            profiler_receipt,
            planner_receipt,
        )
    )
    assert isinstance(profile_rules, dict)
    assert isinstance(planner_input, dict)
    assert isinstance(planner_admission, dict)
    assert isinstance(selected, dict)
    assert isinstance(unresolved, dict)
    assert isinstance(profiler_receipt, dict)
    assert isinstance(planner_receipt, dict)

    profile_admission = _require_object(profile_rules.get("admission"), "profile_admission")
    profile_proposal = _require_object(profile_admission.get("proposal"), "profile_proposal")
    _assert_case_id(profile_proposal.get("case_id"), case_id, "profile_proposal")
    projected = _require_object(profile_rules.get("projected_casegraph"), "projected_casegraph")
    projected_case = _require_object(projected.get("case"), "projected_casegraph.case")
    _assert_case_id(projected_case.get("case_id"), case_id, "projected_casegraph.case")

    selected_admission = _require_object(selected.get("planner_admission"), "selected.planner_admission")
    selected_execution = _require_object(selected.get("selected_execution"), "selected.selected_execution")
    _assert_case_id(selected.get("case_id"), case_id, "arm_c_selected_public_actions")
    if selected_admission != planner_admission:
        raise CaseViewIntegrityError("STALE_PLANNER_ADMISSION_REFERENCE")
    _selected_card_consistency(
        case_id=case_id,
        planner_input=planner_input,
        planner_admission=planner_admission,
        execution=selected_execution,
    )

    rich_rules, rich_by_id = _rule_index(profile_rules.get("rule_results"), "profile_rule_results")
    compact_rules, compact_by_id = _rule_index(packet.get("active_rule_results"), "active_rule_results")
    unresolved_rules, unresolved_by_id = _rule_index(
        unresolved.get("active_rule_results"), "unresolved_classification.active_rule_results"
    )
    if set(rich_by_id) != set(compact_by_id) or set(compact_by_id) != set(unresolved_by_id):
        raise CaseViewIntegrityError("STALE_RULE_RESULT_REFERENCE")
    for rule_id, compact in compact_by_id.items():
        rich = rich_by_id[rule_id]
        unresolved_copy = unresolved_by_id[rule_id]
        for field in ("runtime_subrule_id", "status", "target", "reason_codes"):
            if compact.get(field) != rich.get(field) or compact.get(field) != unresolved_copy.get(field):
                raise CaseViewIntegrityError("STALE_RULE_RESULT_REFERENCE", rule_id)

    profile_raw = _proposal_from_receipt(profiler_receipt, case_id, "profiler_proposal")
    planner_raw = _proposal_from_receipt(planner_receipt, case_id, "planner_proposal")
    if profile_raw != profile_proposal:
        raise CaseViewIntegrityError("STALE_PROFILE_PROPOSAL_REFERENCE")
    descriptive, active = _evidence_lanes(selected_execution.get("evidence_results"), case_id)
    if descriptive != packet.get("descriptive_evidence_results_no_active_rule_effect"):
        raise CaseViewIntegrityError("STALE_EVIDENCE_RESULT_REFERENCE")

    exact_file = _read_object(root / "existing_exact_hsp90_control_regression.json", "exact_control", required=False)
    embedded_exact = packet.get("existing_exact_hsp90_control_regression")
    if exact_file is not None and embedded_exact != exact_file:
        raise CaseViewIntegrityError("STALE_EXACT_CONTROL_REFERENCE")
    if not isinstance(embedded_exact, dict) or embedded_exact.get("status") == "NOT_RUN_IN_THIS_CAPSULE_INVOCATION":
        exact_control: Any = unavailable("No exact control regression belongs to this case artifact.")
    else:
        exact_control = deepcopy(embedded_exact)

    sources = _require_list(artifacts["agent_visible_input"].get("source_materials"), "source_materials")  # type: ignore[union-attr]
    obligations = _require_list(unresolved.get("development_obligations"), "development_obligations")
    legal_cards = _require_list(planner_input.get("legal_action_cards"), "legal_action_cards")
    rule_instances = [_rule_identity(result, "rule_result") for result in rich_rules]
    return CaseView(
        schema_version="dynamics-atlas-case-view/v1",
        case_id=case_id,
        artifact_kind="RECORDED_EXPOSED_CAPSULE_CASE",
        artifact_root_name=root.name,
        integrity_status="PASS",
        question=packet.get("requested_claim", artifacts["agent_visible_input"].get("research_question")),  # type: ignore[union-attr]
        current_gate=packet.get("source_science_review_status", "UNKNOWN"),
        claim_ceiling={
            "requested_claim": packet.get("requested_claim", "UNKNOWN"),
            "forbidden_claims": deepcopy(packet.get("forbidden_claims", [])),
        },
        sources_and_locators=deepcopy(sources),
        agent_proposal={
            "kind": "AGENT_PROPOSAL",
            "proposal": profile_raw,
            "provenance": deepcopy(profiler_receipt),
        },
        admitted_facts={
            "kind": "PLATFORM_ADMITTED_FACT",
            "admission": deepcopy(profile_admission),
            "projected_casegraph": deepcopy(projected),
        },
        rule_instances=rule_instances,
        rule_results=rich_rules,
        unresolved_obligations=deepcopy(obligations),
        legal_action_cards=deepcopy(legal_cards),
        planner_proposal={
            "kind": "AGENT_PROPOSAL",
            "proposal": planner_raw,
            "provenance": deepcopy(planner_receipt),
        },
        authorization=deepcopy(planner_admission),
        executed_actions=deepcopy(selected_execution),
        receipts={
            "profiler_provenance": deepcopy(profiler_receipt),
            "planner_provenance": deepcopy(planner_receipt),
            "asset_identity_verification": deepcopy(artifacts["asset_identity_verification"]),
        },
        descriptive_evidence_no_active_rule_effect=descriptive,
        active_rule_evidence=active,
        exact_control_regression=exact_control,
        before_after_rule_result_links=unavailable(
            "The recorded capsule exposes no broad same-Rule before/after evidence link."
        ),
        conclusion_packet={"kind": "CONCLUSION_PACKET", "artifact": deepcopy(packet)},
        human_review_state={
            "kind": "HUMAN_REVIEW",
            "status": packet.get("source_science_review_status", "UNKNOWN"),
            "items": deepcopy(packet.get("human_review_items", [])),
        },
        terminal_scientific_state=packet.get("terminal_disposition", "UNKNOWN"),
        boundary=(
            "This view copies the recorded capsule state. It does not recalculate a "
            "terminal disposition or promote descriptive/exact-control evidence."
        ),
    )


_RUN_REQUIRED_ARTIFACTS = (
    "inputs/public_case_packet.json",
    "inputs/profiler_visible_input.json",
    "inputs/profile_proposal.json",
    "inputs/planner_proposal.json",
    "profiler_proposal_provenance.json",
    "planner_proposal_provenance.json",
    "fresh_rule_state.json",
    "planner_visible_input.json",
    "planner_authorization.json",
    "selected_action_execution.json",
    "rule_reevaluation.json",
    "case_run_manifest_v1.json",
)


def _manifest_artifact_paths(root: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    raw_paths = _require_list(manifest.get("artifact_paths"), "manifest.artifact_paths")
    if len(raw_paths) != len(set(raw_paths)):
        raise CaseViewIntegrityError("DUPLICATE_ARTIFACT_REFERENCE")
    path_set: set[str] = set()
    loaded: dict[str, Any] = {}
    for position, raw_path in enumerate(raw_paths):
        relative = _require_string(raw_path, f"manifest.artifact_paths[{position}]")
        posix = PurePosixPath(relative)
        if posix.is_absolute() or ".." in posix.parts:
            raise CaseViewIntegrityError("UNSAFE_ARTIFACT_REFERENCE", relative)
        path_set.add(posix.as_posix())
        path = (root / Path(*posix.parts)).resolve()
        try:
            path.relative_to(root.resolve())
        except ValueError as error:
            raise CaseViewIntegrityError("UNSAFE_ARTIFACT_REFERENCE", relative) from error
        if posix.suffix == ".txt":
            if not path.is_file():
                raise CaseViewIntegrityError("REQUIRED_ARTIFACT_MISSING", relative)
            try:
                value = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as error:
                raise CaseViewIntegrityError("ARTIFACT_MALFORMED", relative) from error
        else:
            value = _read_object(path, relative)
            assert value is not None
        loaded[posix.as_posix()] = value
    missing = sorted(set(_RUN_REQUIRED_ARTIFACTS) - path_set)
    if missing:
        raise CaseViewIntegrityError("REQUIRED_ARTIFACT_REFERENCE_MISSING", ",".join(missing))
    return loaded


def _build_case_run_view(root: Path) -> CaseView:
    manifest = _read_object(root / "case_run_manifest_v1.json", "case_run_manifest_v1")
    assert manifest is not None
    _validate_case_runner_manifest(manifest)
    case_id = _require_string(manifest.get("case_id"), "manifest.case_id")
    loaded = _manifest_artifact_paths(root, manifest)
    profiler_provenance = loaded["profiler_proposal_provenance.json"]
    planner_provenance = loaded["planner_proposal_provenance.json"]
    fresh = loaded["fresh_rule_state.json"]
    planner_input = loaded["planner_visible_input.json"]
    authorization = loaded["planner_authorization.json"]
    execution = loaded["selected_action_execution.json"]
    reevaluation = loaded["rule_reevaluation.json"]
    for label, artifact in (
        ("fresh_rule_state", fresh),
        ("profiler_proposal_provenance", profiler_provenance),
        ("planner_proposal_provenance", planner_provenance),
        ("planner_visible_input", planner_input),
        ("planner_authorization", authorization),
        ("selected_action_execution", execution),
        ("rule_reevaluation", reevaluation),
    ):
        if "case_id" in artifact:
            _assert_case_id(artifact.get("case_id"), case_id, label)

    expected_copies = (
        (manifest.get("fresh_rule_state"), fresh, "fresh_rule_state"),
        (manifest.get("planner_visible_input"), planner_input, "planner_visible_input"),
        (manifest.get("authorization"), authorization, "planner_authorization"),
        (manifest.get("action_execution"), execution, "selected_action_execution"),
        (manifest.get("rule_reevaluation"), reevaluation, "rule_reevaluation"),
    )
    for embedded, standalone, label in expected_copies:
        if embedded != standalone:
            raise CaseViewIntegrityError("STALE_EMBEDDED_ARTIFACT_REFERENCE", label)
    proposal_provenance = _require_object(
        manifest.get("proposal_provenance"), "manifest.proposal_provenance"
    )
    if proposal_provenance.get("profiler") != profiler_provenance:
        raise CaseViewIntegrityError(
            "STALE_EMBEDDED_ARTIFACT_REFERENCE", "profiler_proposal_provenance"
        )
    if proposal_provenance.get("planner") != planner_provenance:
        raise CaseViewIntegrityError(
            "STALE_EMBEDDED_ARTIFACT_REFERENCE", "planner_proposal_provenance"
        )

    planner_admission = _require_object(manifest.get("planner_admission"), "manifest.planner_admission")
    _assert_case_id(planner_admission.get("case_id"), case_id, "planner_admission")
    _selected_card_consistency(
        case_id=case_id,
        planner_input=planner_input,
        planner_admission=planner_admission,
        execution=execution,
    )
    _authorization_consistency(
        case_id=case_id,
        planner_admission=planner_admission,
        authorization=authorization,
        execution=execution,
    )

    before, before_by_id = _rule_index(reevaluation.get("before_rule_results"), "before_rule_results")
    after, after_by_id = _rule_index(reevaluation.get("after_rule_results"), "after_rule_results")
    fresh_results, fresh_by_id = _rule_index(fresh.get("rule_results"), "fresh_rule_state.rule_results")
    if set(before_by_id) != set(after_by_id) or set(before_by_id) != set(fresh_by_id):
        raise CaseViewIntegrityError("STALE_RULE_RESULT_REFERENCE")
    for rule_id in before_by_id:
        if before_by_id[rule_id] != fresh_by_id[rule_id]:
            raise CaseViewIntegrityError("STALE_RULE_RESULT_REFERENCE", rule_id)

    descriptive, active = _evidence_lanes(execution.get("evidence_results"), case_id)
    links = _validated_reevaluation_links(
        reevaluation=reevaluation,
        before_by_id=before_by_id,
        after_by_id=after_by_id,
        active_evidence=active,
    )
    selected_ids = _require_list(execution.get("selected_card_ids"), "execution.selected_card_ids")
    for card_id, evidence in zip(selected_ids, _require_list(execution.get("evidence_results"), "evidence_results")):
        relative = f"actions/{card_id}/evidence_result.json"
        if loaded.get(relative) != evidence:
            raise CaseViewIntegrityError("STALE_EVIDENCE_RESULT_REFERENCE", relative)

    input_provenance = _require_object(manifest.get("input_provenance"), "input_provenance")
    public_packet = _input_snapshot(
        loaded=loaded,
        input_provenance=input_provenance,
        snapshot_name="public_case_packet",
        case_id=case_id,
    )
    public_packet_source = _verify_repository_source_snapshot(
        snapshot=public_packet,
        source_path=input_provenance.get("public_case_packet"),
        label="public_case_packet",
        source_required_code="REPOSITORY_PUBLIC_PACKET_SOURCE_REQUIRED",
    )
    _public_packet_consistency(manifest=manifest, public_packet=public_packet)
    profiler_visible_input = _input_snapshot(
        loaded=loaded,
        input_provenance=input_provenance,
        snapshot_name="profiler_visible_input",
        case_id=case_id,
    )
    profile_proposal = _input_snapshot(
        loaded=loaded,
        input_provenance=input_provenance,
        snapshot_name="profile_proposal",
        case_id=case_id,
    )
    planner_proposal = _input_snapshot(
        loaded=loaded,
        input_provenance=input_provenance,
        snapshot_name="planner_proposal",
        case_id=case_id,
    )
    planner_input_snapshot = _input_snapshot(
        loaded=loaded,
        input_provenance=input_provenance,
        snapshot_name="planner_visible_input",
        case_id=case_id,
    )
    if planner_input_snapshot != planner_input:
        raise CaseViewIntegrityError("STALE_PLANNER_VISIBLE_INPUT_SNAPSHOT")
    sources = deepcopy(public_packet.get("source_materials", []))
    admission = _require_object(fresh.get("admission"), "fresh_rule_state.admission")
    expected_profiler_input = _expected_profiler_visible_input(public_packet)
    if profiler_visible_input != expected_profiler_input:
        raise CaseViewIntegrityError("PROFILER_VISIBLE_INPUT_PUBLIC_PACKET_MISMATCH")
    try:
        expected_profile_admission = validate_agent_proposal(
            public_packet_source, profile_proposal
        )
    except PaperBlindPublicPacketError as error:
        raise CaseViewIntegrityError("PROFILER_PROPOSAL_CONTRACT_INVALID") from error
    if admission != expected_profile_admission:
        raise CaseViewIntegrityError("PROFILER_ADMISSION_PROPOSAL_MISMATCH")
    _planner_admission_consistency(
        case_id=case_id,
        planner_proposal=planner_proposal,
        planner_admission=planner_admission,
    )
    _verify_proposal_receipt(
        receipt=profiler_provenance,
        case_id=case_id,
        role="PROFILER",
        mode=input_provenance.get("profile_mode"),
        source_path=input_provenance.get("profile_proposal"),
        visible_input=profiler_visible_input,
        parsed_proposal=profile_proposal,
        admission_evaluation=admission,
        loaded=loaded,
        public_packet_source=public_packet_source,
    )
    _verify_proposal_receipt(
        receipt=planner_provenance,
        case_id=case_id,
        role="PLANNER",
        mode=input_provenance.get("planner_mode"),
        source_path=input_provenance.get("planner_proposal"),
        visible_input=planner_input,
        parsed_proposal=planner_proposal,
        admission_evaluation=planner_admission,
        loaded=loaded,
        public_packet_source=public_packet_source,
    )
    projected = _require_object(fresh.get("projected_casegraph"), "fresh_rule_state.projected_casegraph")
    projected_case = _require_object(projected.get("case"), "projected_casegraph.case")
    _assert_case_id(projected_case.get("case_id"), case_id, "projected_casegraph.case")
    obligations = _require_list(fresh.get("development_obligations"), "development_obligations")
    legal_cards = _require_list(planner_input.get("legal_action_cards"), "legal_action_cards")
    rule_instances = [_rule_identity(result, "rule_result") for result in after]
    profiler_envelope = loaded.get("live_calls/profiler/proposal_envelope.json")
    if isinstance(profiler_envelope, dict):
        profiler_live_receipt = _require_object(
            profiler_provenance.get("live_call_receipt"),
            "PROFILER.live_call_receipt",
        )
        if profiler_live_receipt.get("field_annotation_validation_status") == "PASS":
            profiler_diagnostic = validate_profile_proposal_envelope(
                public_packet_source, profiler_envelope
            )["diagnostic_summary"]
        else:
            profiler_diagnostic = {
                "status": "REJECTED_DIAGNOSTIC_ONLY",
                "error_code": profiler_live_receipt.get(
                    "field_annotation_error_code"
                ),
                "routing_effect": "NONE_CORE_ADMISSION_INDEPENDENT",
            }
    else:
        profiler_diagnostic = unavailable(
            "Profiler field annotations are unavailable outside live mode."
        )
    return CaseView(
        schema_version="dynamics-atlas-case-view/v1",
        case_id=case_id,
        artifact_kind="CASE_RUNNER_V1_RUN",
        artifact_root_name=root.name,
        integrity_status="PASS",
        question=manifest.get("research_question", "UNKNOWN"),
        current_gate=manifest.get("source_science_review_status", "UNKNOWN"),
        claim_ceiling=deepcopy(manifest.get("claim_boundary", "UNKNOWN")),
        sources_and_locators=sources,
        agent_proposal={
            "kind": "AGENT_PROPOSAL",
            "proposal": profile_proposal,
            "admission": deepcopy(admission),
            "provenance": deepcopy(profiler_provenance),
            "field_annotation_diagnostic": deepcopy(profiler_diagnostic),
        },
        admitted_facts={
            "kind": "PLATFORM_ADMITTED_FACT",
            "admission": deepcopy(admission),
            "projected_casegraph": deepcopy(projected),
        },
        rule_instances=rule_instances,
        rule_results=after,
        unresolved_obligations=deepcopy(obligations),
        legal_action_cards=deepcopy(legal_cards),
        planner_proposal={
            "kind": "AGENT_PROPOSAL",
            "proposal": planner_proposal,
            "provenance": deepcopy(planner_provenance),
        },
        authorization=deepcopy(authorization),
        executed_actions=deepcopy(execution),
        receipts={
            "input_provenance": deepcopy(input_provenance),
            "profiler_proposal_provenance": deepcopy(profiler_provenance),
            "planner_proposal_provenance": deepcopy(planner_provenance),
            "authorization": deepcopy(authorization),
            "artifact_paths": deepcopy(manifest.get("artifact_paths")),
        },
        descriptive_evidence_no_active_rule_effect=descriptive,
        active_rule_evidence=active,
        exact_control_regression=unavailable(
            "case_runner_v1 does not synthesize or import an exact-control sidecar."
        ),
        before_after_rule_result_links=deepcopy(links),
        conclusion_packet=unavailable(
            "case_runner_v1 does not calculate a ConclusionPacket or terminal verdict."
        ),
        human_review_state={
            "kind": "HUMAN_REVIEW",
            "status": manifest.get("source_science_review_status", "UNKNOWN"),
        },
        terminal_scientific_state=manifest.get("terminal_scientific_state", "UNKNOWN"),
        boundary=_require_string(manifest.get("boundary"), "manifest.boundary"),
    )


def _read_text_artifact(path: Path, label: str) -> str:
    if not path.is_file():
        raise CaseViewIntegrityError("REQUIRED_ARTIFACT_MISSING", label)
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise CaseViewIntegrityError("ARTIFACT_MALFORMED", label) from error


def _validate_decision_closure_artifact_records(
    campaign_root: Path, manifest: dict[str, Any]
) -> set[str]:
    records = _require_list(manifest.get("artifacts"), "manifest.artifacts")
    declared: set[str] = set()
    for position, raw_record in enumerate(records):
        record = _require_object(raw_record, f"manifest.artifacts[{position}]")
        if set(record) != {"path", "sha256", "kind"}:
            raise CaseViewIntegrityError("DECISION_CLOSURE_ARTIFACT_RECORD_INVALID")
        relative = _require_string(record.get("path"), "artifact.path")
        posix = PurePosixPath(relative)
        if posix.is_absolute() or ".." in posix.parts or relative in declared:
            raise CaseViewIntegrityError("UNSAFE_OR_DUPLICATE_ARTIFACT_REFERENCE", relative)
        path = (campaign_root / Path(*posix.parts)).resolve()
        try:
            path.relative_to(campaign_root.resolve())
        except ValueError as error:
            raise CaseViewIntegrityError("UNSAFE_ARTIFACT_REFERENCE", relative) from error
        if not path.is_file():
            raise CaseViewIntegrityError("REQUIRED_ARTIFACT_MISSING", relative)
        expected_sha = _require_string(record.get("sha256"), f"artifact.sha256:{relative}")
        if hashlib.sha256(path.read_bytes()).hexdigest() != expected_sha:
            raise CaseViewIntegrityError("STALE_ARTIFACT_REFERENCE_HASH", relative)
        if record.get("kind") not in {"JSON", "TEXT"}:
            raise CaseViewIntegrityError("DECISION_CLOSURE_ARTIFACT_KIND_INVALID", relative)
        declared.add(relative)
    return declared


def _build_decision_closure_arm_view(root: Path) -> CaseView:
    campaign_root = root.parent
    manifest = _read_object(
        campaign_root / "live_agent_decision_closure_manifest_v1.json",
        "live_agent_decision_closure_manifest_v1",
    )
    assert manifest is not None
    if manifest.get("schema_version") != DECISION_CLOSURE_MANIFEST_SCHEMA:
        raise CaseViewIntegrityError("DECISION_CLOSURE_MANIFEST_SCHEMA_INVALID")
    case_id = _require_string(manifest.get("case_id"), "manifest.case_id")
    if manifest.get("profile_mode") != DECISION_CLOSURE_PROFILE_MODE:
        raise CaseViewIntegrityError("DECISION_CLOSURE_PROFILE_MODE_INVALID")
    arm_id = root.name
    if arm_id not in {
        DECISION_CLOSURE_POSITIVE_ARM_ID,
        DECISION_CLOSURE_STOP_ARM_ID,
    }:
        raise CaseViewIntegrityError("DECISION_CLOSURE_ARM_ID_INVALID", arm_id)
    expected_manifest_arm = (
        manifest.get("positive_arm_id")
        if arm_id == DECISION_CLOSURE_POSITIVE_ARM_ID
        else manifest.get("stop_arm_id")
    )
    if expected_manifest_arm != arm_id:
        raise CaseViewIntegrityError("DECISION_CLOSURE_MANIFEST_ARM_MISMATCH", arm_id)
    declared = _validate_decision_closure_artifact_records(campaign_root, manifest)
    required_root = {"recorded_profile.json", "before_rule_results.json"}
    required_arm = {
        "planner_visible_input.json",
        "live_call/request_payload.json",
        "live_call/raw_response.txt",
        "live_call/model_call_receipt.json",
        "live_call/parsed_proposal.json",
        "planner_admission.json",
        "planner_authorization.json",
        "execution_receipt.json",
        "evidence_results.json",
        "after_casegraph.json",
        "after_rule_results.json",
        "rule_transition.json",
        "route_packet.json",
        "conclusion_packet.json",
        "arm_receipt.json",
    }
    if arm_id == DECISION_CLOSURE_STOP_ARM_ID:
        required_arm.add("stop_receipt.json")
    required_declared = required_root | {f"{arm_id}/{relative}" for relative in required_arm}
    missing = sorted(required_declared - declared)
    if missing:
        raise CaseViewIntegrityError("DECISION_CLOSURE_REQUIRED_ARTIFACT_UNDECLARED", ",".join(missing))

    recorded_profile = _read_object(campaign_root / "recorded_profile.json", "recorded_profile")
    # The frozen RuleResult inventory is a JSON list; read it directly after its
    # byte hash has already been checked against the manifest.
    try:
        before_value = json.loads((campaign_root / "before_rule_results.json").read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise CaseViewIntegrityError("ARTIFACT_MALFORMED", "before_rule_results") from error
    if not isinstance(before_value, list):
        raise CaseViewIntegrityError("LIST_REQUIRED", "before_rule_results")
    before, before_by_id = _rule_index(before_value, "before_rule_results")
    assert recorded_profile is not None

    planner_input = _read_object(root / "planner_visible_input.json", "planner_visible_input")
    request_payload = _read_object(root / "live_call" / "request_payload.json", "request_payload")
    live_receipt = _read_object(root / "live_call" / "model_call_receipt.json", "model_call_receipt")
    planner_proposal = _read_object(root / "live_call" / "parsed_proposal.json", "parsed_proposal")
    planner_admission = _read_object(root / "planner_admission.json", "planner_admission")
    authorization = _read_object(root / "planner_authorization.json", "planner_authorization")
    execution = _read_object(root / "execution_receipt.json", "execution_receipt")
    evidence_wrapper = _read_object(root / "evidence_results.json", "evidence_results")
    transition = _read_object(root / "rule_transition.json", "rule_transition")
    route_packet = _read_object(root / "route_packet.json", "route_packet")
    conclusion = _read_object(root / "conclusion_packet.json", "conclusion_packet")
    arm_receipt = _read_object(root / "arm_receipt.json", "arm_receipt")
    assert all(
        value is not None
        for value in (
            planner_input,
            request_payload,
            live_receipt,
            planner_proposal,
            planner_admission,
            authorization,
            execution,
            evidence_wrapper,
            transition,
            route_packet,
            conclusion,
            arm_receipt,
        )
    )
    for label, artifact in (
        ("planner_input", planner_input),
        ("planner_proposal", planner_proposal),
        ("planner_admission", planner_admission),
        ("authorization", authorization),
        ("execution", execution),
        ("evidence", evidence_wrapper),
        ("arm_receipt", arm_receipt),
    ):
        _assert_case_id(artifact.get("case_id"), case_id, label)
    if arm_receipt.get("arm_id") != arm_id or arm_receipt.get("campaign_id") != manifest.get("campaign_id"):
        raise CaseViewIntegrityError("DECISION_CLOSURE_ARM_RECEIPT_IDENTITY_MISMATCH")
    base_state_sha = canonical_json_sha256(
        {
            "recorded_profile": recorded_profile,
            "before_rule_results": before,
            "unresolved_items": planner_input.get("unresolved_items"),
        }
    )
    if base_state_sha != manifest.get("base_state_sha256") or base_state_sha != arm_receipt.get("base_state_sha256"):
        raise CaseViewIntegrityError("DECISION_CLOSURE_BASE_STATE_HASH_MISMATCH")

    raw_response = _read_text_artifact(
        root / "live_call" / "raw_response.txt", "raw_response"
    )
    _verify_live_openrouter_semantics(
        role="PLANNER",
        visible_input=planner_input,
        parsed_proposal=planner_proposal,
        request_payload=request_payload,
        raw_response=raw_response,
        live_receipt=live_receipt,
        proposal_envelope=None,
        public_packet_source=REPO_ROOT / "README.md",
    )
    try:
        expected_admission = validate_decision_closure_planner_proposal(
            planner_input, planner_proposal
        )
    except ValueError as error:
        raise CaseViewIntegrityError("DECISION_CLOSURE_PLANNER_PROPOSAL_INVALID") from error
    if planner_admission != expected_admission:
        raise CaseViewIntegrityError("DECISION_CLOSURE_PLANNER_ADMISSION_MISMATCH")
    selected = _require_list(planner_admission.get("selected_card_ids"), "selected_card_ids")
    if authorization.get("selected_card_ids") != selected or execution.get("selected_card_ids") != selected:
        raise CaseViewIntegrityError("DECISION_CLOSURE_SELECTION_LINK_MISMATCH")

    try:
        after_value = json.loads((root / "after_rule_results.json").read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise CaseViewIntegrityError("ARTIFACT_MALFORMED", "after_rule_results") from error
    after, after_by_id = _rule_index(after_value, "after_rule_results")
    if set(before_by_id) != set(after_by_id):
        raise CaseViewIntegrityError("RULE_INVENTORY_CHANGED_DURING_REEVALUATION")
    for rule_id in before_by_id:
        if _rule_identity(before_by_id[rule_id], "before") != _rule_identity(after_by_id[rule_id], "after"):
            raise CaseViewIntegrityError("RULE_INSTANCE_IDENTITY_CHANGED", rule_id)
    changed_ids = {
        rule_id
        for rule_id in before_by_id
        if before_by_id[rule_id] != after_by_id[rule_id]
    }
    declared_transitions = {
        item.get("rule_instance_id")
        for item in _require_list(
            transition.get("all_changed_rule_statuses"),
            "all_changed_rule_statuses",
        )
        if isinstance(item, dict)
    }
    if changed_ids != declared_transitions:
        raise CaseViewIntegrityError("DECISION_CLOSURE_RULE_CHANGE_SET_MISMATCH")
    target_before = before_by_id.get(DECISION_CLOSURE_TARGET_RULE_ID)
    target_after = after_by_id.get(DECISION_CLOSURE_TARGET_RULE_ID)
    if target_before is None or target_after is None:
        raise CaseViewIntegrityError("DECISION_CLOSURE_TARGET_RULE_MISSING")
    if transition.get("before_rule_result") != target_before or transition.get("after_rule_result") != target_after:
        raise CaseViewIntegrityError("DECISION_CLOSURE_TARGET_RULE_LINK_MISMATCH")

    evidence_results = _require_list(
        evidence_wrapper.get("evidence_results"), "evidence_results"
    )
    descriptive, active = _evidence_lanes(evidence_results, case_id)
    if route_packet.get("case_id") != case_id or route_packet.get("scenario_id") != arm_id:
        raise CaseViewIntegrityError("DECISION_CLOSURE_ROUTE_IDENTITY_MISMATCH")
    if conclusion.get("case_id") != case_id or conclusion.get("scenario_id") != arm_id:
        raise CaseViewIntegrityError("DECISION_CLOSURE_CONCLUSION_IDENTITY_MISMATCH")
    if conclusion.get("terminal_disposition") != "ABSTAIN_OR_HUMAN_REVIEW":
        raise CaseViewIntegrityError("DECISION_CLOSURE_TERMINAL_DISPOSITION_INVALID")

    if arm_id == DECISION_CLOSURE_POSITIVE_ARM_ID:
        if (
            selected != [DECISION_CLOSURE_ACTION_CARD_ID]
            or authorization.get("status") != "AUTHORIZED_EXACT_ALLOWLISTED_LOOKUP"
            or execution.get("executed_action_count") != 1
            or len(active) != 1
            or active[0].get("affected_rule_instance_id") != DECISION_CLOSURE_TARGET_RULE_ID
            or target_before.get("status") != "UNRESOLVED"
            or target_after.get("status") != "PASS"
        ):
            raise CaseViewIntegrityError("DECISION_CLOSURE_POSITIVE_ARM_INVALID")
    else:
        stop_receipt = _read_object(root / "stop_receipt.json", "stop_receipt")
        assert stop_receipt is not None
        if (
            selected
            or planner_admission.get("decision") != "ABSTAIN_NO_ACTION"
            or authorization.get("status") != "AUTHORIZED_ABSTENTION_ZERO_EXECUTION"
            or execution.get("executed_action_count") != 0
            or evidence_results
            or changed_ids
            or stop_receipt.get("scientific_action_executions") != 0
            or target_before.get("status") != "UNRESOLVED"
            or target_after.get("status") != "UNRESOLVED"
        ):
            raise CaseViewIntegrityError("DECISION_CLOSURE_STOP_ARM_INVALID")

    legal_cards = _require_list(planner_input.get("legal_action_cards"), "legal_action_cards")
    unresolved = _require_list(planner_input.get("unresolved_items"), "unresolved_items")
    links = [
        {
            "rule_instance_id": rule_id,
            "before_status": before_by_id[rule_id].get("status"),
            "after_status": after_by_id[rule_id].get("status"),
            "evidence_result_id": (
                active[0].get("evidence_result_id")
                if active and rule_id == DECISION_CLOSURE_TARGET_RULE_ID
                else None
            ),
            "relationship": (
                "EXACT_AFFECTED_RULEINSTANCE"
                if rule_id == DECISION_CLOSURE_TARGET_RULE_ID
                else "DECLARED_DOWNSTREAM_DEPENDENCY"
            ),
        }
        for rule_id in sorted(changed_ids)
    ]
    return CaseView(
        schema_version="dynamics-atlas-case-view/v1",
        case_id=case_id,
        artifact_kind="LIVE_AGENT_DECISION_CLOSURE_V1_ARM",
        artifact_root_name=arm_id,
        integrity_status="PASS",
        question="Can one exact allowlisted X-EISD declaration lookup resolve the current random-pool composition obligation?",
        current_gate=manifest.get("source_science_review_status", "PENDING_DOMAIN_REVIEW"),
        claim_ceiling=manifest.get("claim_ceiling"),
        sources_and_locators=deepcopy(recorded_profile.get("evidence_items", [])),
        agent_proposal={
            "kind": "RECORDED_PROFILE",
            "mode": DECISION_CLOSURE_PROFILE_MODE,
            "proposal": deepcopy(recorded_profile),
        },
        admitted_facts={
            "kind": "PLATFORM_ADMITTED_RECORDED_PROFILE",
            "projected_casegraph": deepcopy(recorded_profile),
        },
        rule_instances=[_rule_identity(result, "rule_result") for result in after],
        rule_results=after,
        unresolved_obligations=deepcopy(unresolved),
        legal_action_cards=deepcopy(legal_cards),
        planner_proposal={
            "kind": "LIVE_AGENT_PROPOSAL",
            "proposal": deepcopy(planner_proposal),
            "provenance": deepcopy(live_receipt),
        },
        authorization=deepcopy(authorization),
        executed_actions=deepcopy(execution),
        receipts={
            "arm_receipt": deepcopy(arm_receipt),
            "live_model_call": deepcopy(live_receipt),
            "artifact_records": deepcopy(manifest.get("artifacts")),
        },
        descriptive_evidence_no_active_rule_effect=descriptive,
        active_rule_evidence=active,
        exact_control_regression=unavailable("This X-EISD route does not use the HSP90 exact control."),
        before_after_rule_result_links=links,
        conclusion_packet={"kind": "CONCLUSION_PACKET", "artifact": deepcopy(conclusion)},
        human_review_state={
            "kind": "HUMAN_REVIEW",
            "status": manifest.get("source_science_review_status", "PENDING_DOMAIN_REVIEW"),
        },
        terminal_scientific_state=conclusion.get("terminal_disposition"),
        boundary=_require_string(manifest.get("boundary"), "manifest.boundary"),
    )



def build_case_view(case_or_run_root: str | Path) -> CaseView:
    """Project a recorded case/run directory into a validated ``CaseView``.

    The function recognizes the artifact set, validates required artifacts and
    their same-case/fresh references, and leaves optional absence explicit.  It
    never evaluates Rules or computes a conclusion.
    """

    root = Path(case_or_run_root)
    if not root.is_dir():
        raise CaseViewIntegrityError("CASE_OR_RUN_ROOT_UNAVAILABLE", root.name or ".")
    is_run = (root / "case_run_manifest_v1.json").is_file()
    is_capsule_case = (root / "human_decision_packet.json").is_file()
    is_decision_closure_arm = (root / "arm_receipt.json").is_file() and (
        root.parent / "live_agent_decision_closure_manifest_v1.json"
    ).is_file()
    if sum((is_run, is_capsule_case, is_decision_closure_arm)) > 1:
        raise CaseViewIntegrityError("AMBIGUOUS_CASE_OR_RUN_ROOT", root.name)
    if is_decision_closure_arm:
        return _build_decision_closure_arm_view(root)
    if is_run:
        return _build_case_run_view(root)
    if is_capsule_case:
        return _build_capsule_case_view(root)
    raise CaseViewIntegrityError("CASE_OR_RUN_ROOT_UNRECOGNIZED", root.name)
