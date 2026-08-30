"""One bounded live-Planner decision closure over the existing X-EISD route.

The model selects a current legal card or abstains.  Deterministic repository
code remains responsible for authorization, the exact allowlisted lookup,
Rule reevaluation, the existing Stage-2 reducer, and artifact persistence.
"""

from __future__ import annotations

import copy
import hashlib
import json
import re
from decimal import Decimal, InvalidOperation
from pathlib import Path, PurePosixPath
from typing import Any, Mapping, Sequence

from .minimal_stage2_exposed_conclusions_v1 import (
    materialize_stage2_conclusion_packet,
    source_grounding_by_family,
)
from .openrouter_proposal_transport_v1 import (
    OpenRouterBudgetLedger,
    OpenRouterModelSpec,
    OpenRouterProposalClient,
    canonical_json_sha256,
    text_sha256,
)
from .real_case_vertical_slice_v1 import (
    X_EISD_CASE_ID,
    X_EISD_FROZEN_SELECTED_RULE_INSTANCE_IDS,
    apply_lookup_result,
    derive_declaration_attestations,
    evaluate_xeisd_case,
    execute_exact_source_lookup,
    load_json_object,
    load_rules_v1_bundle,
    materialize_xeisd_conclusion_packet,
)


REPO_ROOT = Path(__file__).resolve().parents[2]
CAMPAIGN_ROOT = REPO_ROOT / "agent_experiments" / "live_agent_decision_closure_v1"
CAMPAIGN_CONFIG_PATH = CAMPAIGN_ROOT / "config" / "live_agent_decision_closure_v1.json"

CAMPAIGN_CONFIG_SCHEMA = "live-agent-decision-closure-campaign-config/v1"
CAMPAIGN_OPEN_STATUS = "OPEN_EXPLICITLY_AUTHORIZED_DEVELOPMENT"
CAMPAIGN_CLOSED_STATUS = "CLOSED_FROZEN"
CAMPAIGN_CLOSED_ERROR = "LIVE_AGENT_DECISION_CLOSURE_CAMPAIGN_CLOSED"
MANIFEST_SCHEMA = "live-agent-decision-closure-manifest/v1"
ARM_RECEIPT_SCHEMA = "live-agent-decision-closure-arm-receipt/v1"
EVIDENCE_RESULT_SCHEMA = "live-agent-decision-closure-evidence-result/v1"
SCHEMA_REPAIR_RECEIPT_SCHEMA = "live-agent-decision-closure-schema-repair/v1"
POSITIVE_ARM_ID = "XEISD_LOOKUP_CARD_PRESENT"
STOP_ARM_ID = "XEISD_LOOKUP_CARD_REMOVED"
ACTION_CARD_ID = "XEISD_RANDOM_COMPOSITION_EXACT_LOOKUP_V1"
LOOKUP_ID = "XEI-LOOKUP-RANDOM-DECLARATIONS"
TARGET_RULE_INSTANCE_ID = X_EISD_FROZEN_SELECTED_RULE_INSTANCE_IDS[0]
PROFILE_MODE = "RECORDED_PROFILE_LIVE_PLANNER"
PLANNER_MODE = "LIVE_OPENROUTER_LUNA"
TRANSPORT = "OPENROUTER_EXACT_OPENAI_PROVIDER_STRICT_JSON_SCHEMA_NO_TOOLS"
CLAIM_CEILING = (
    "DEVELOPMENT_DIAGNOSTIC_ONLY; one live Planner counterfactual over an existing "
    "exact X-EISD lookup; NOT_AGENT_VALUE_ESTABLISHED; NOT_SCIENTIFIC_SUPPORT"
)
SOURCE_SCIENCE_REVIEW_STATUS = "PENDING_DOMAIN_REVIEW"
HELD_OUT_STATUS = "NOT_ACCESSED"
SCIENTIFIC_SUPPORT_STATUS = "NOT_ESTABLISHED"
RESULT_STATUS = "LIVE_AGENT_DECISION_CLOSURE_V1_COMPLETE"
CAMPAIGN_BOUNDARY = (
    "One development-only live Planner counterfactual over an existing exact X-EISD "
    "lookup. The positive arm closes one declaration Rule and the existing reducer "
    "remains ABSTAIN; the stop arm executes nothing. This is not source-science "
    "approval, Agent value, transfer, or scientific support."
)

_FROZEN_PLANNER_PROMPT = {
    "path": "agent_experiments/live_agent_decision_closure_v1/prompts/planner_v1.md",
    "version": "LIVE_AGENT_DECISION_CLOSURE_PLANNER_V1_FROZEN",
    "sha256": "167d27369c99bcdbd658584b9e01b3a7b275618bfc68322bb792a55fd8cb63ae",
}
_FROZEN_MODEL = {
    "model_id": "openai/gpt-5.6-luna",
    "accepted_returned_model_ids": [
        "openai/gpt-5.6-luna",
        "openai/gpt-5.6-luna-20260709",
    ],
    "provider_endpoint_tag": "openai",
    "expected_provider_display_name": "OpenAI",
    "allowed_service_tiers": [None, "default"],
    "input_price_per_million_usd": "0.20",
    "output_price_per_million_usd": "1.20",
    "reasoning_effort": "low",
    "include_temperature_zero": False,
    "metadata_sha256": "4032c962a185ecae6f67e83f80dd12ac7974738d9cab89f53d67ef3498110c36",
}
_FROZEN_MAX_OUTPUT_TOKENS = 4096

_ALLOWED_DEPENDENT_TRANSITIONS = {
    TARGET_RULE_INSTANCE_ID,
    "F02R02_EDGE_CONDITION_COMPATIBILITY::EDGE::xeisd_random_pool_vs_j_coupling_question",
    "F06R02_EDGE_COMPARABILITY::EDGE::xeisd_random_pool_vs_j_coupling_question",
}
_TERMINAL_LANGUAGE = re.compile(
    r"SUPPORT_WITHIN_CEILING|CANNOT_SUPPORT_REQUESTED_CLAIM|RULE_CONTRACT_PASS|"
    r"scientific support|final scientific conclusion",
    re.IGNORECASE,
)


class LiveAgentDecisionClosureV1Error(ValueError):
    """Raised when the bounded campaign contract fails closed."""


def _canonical_json_text(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8")


def _prepare_output_dir(path: Path) -> Path:
    resolved = path.resolve()
    if resolved.exists() and (not resolved.is_dir() or any(resolved.iterdir())):
        raise LiveAgentDecisionClosureV1Error("OUTPUT_DIR_MUST_BE_NEW_OR_EMPTY")
    resolved.mkdir(parents=True, exist_ok=True)
    return resolved


def _repository_path(raw: Any, label: str) -> Path:
    if not isinstance(raw, str) or not raw:
        raise LiveAgentDecisionClosureV1Error(f"REPOSITORY_PATH_REQUIRED:{label}")
    posix = PurePosixPath(raw)
    if posix.is_absolute() or ".." in posix.parts:
        raise LiveAgentDecisionClosureV1Error(f"REPOSITORY_PATH_INVALID:{label}")
    path = (REPO_ROOT / Path(*posix.parts)).resolve()
    try:
        path.relative_to(REPO_ROOT.resolve())
    except ValueError as error:
        raise LiveAgentDecisionClosureV1Error(
            f"REPOSITORY_PATH_INVALID:{label}"
        ) from error
    return path


def _require_exact_keys(value: Mapping[str, Any], expected: set[str], label: str) -> None:
    if set(value) != expected:
        raise LiveAgentDecisionClosureV1Error(f"FIELDS_INVALID:{label}")


def _require_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise LiveAgentDecisionClosureV1Error(f"NONEMPTY_STRING_REQUIRED:{label}")
    return value.strip()


def _require_decimal(value: Any, label: str) -> Decimal:
    try:
        parsed = Decimal(str(value))
    except (InvalidOperation, ValueError) as error:
        raise LiveAgentDecisionClosureV1Error(f"DECIMAL_REQUIRED:{label}") from error
    if not parsed.is_finite():
        raise LiveAgentDecisionClosureV1Error(f"FINITE_DECIMAL_REQUIRED:{label}")
    return parsed


def _validate_planner_input(value: Mapping[str, Any]) -> dict[str, Any]:
    expected = {
        "schema_version",
        "case_id",
        "planner_boundary",
        "unresolved_items",
        "legal_action_cards",
        "required_output",
    }
    if set(value) != expected or value.get("schema_version") != "paper-blind-planner-visible-input/v2":
        raise LiveAgentDecisionClosureV1Error("PLANNER_INPUT_SCHEMA_INVALID")
    if value.get("case_id") != X_EISD_CASE_ID:
        raise LiveAgentDecisionClosureV1Error("PLANNER_INPUT_CASE_ID_MISMATCH")
    unresolved = value.get("unresolved_items")
    cards = value.get("legal_action_cards")
    if not isinstance(unresolved, list) or not isinstance(cards, list):
        raise LiveAgentDecisionClosureV1Error("PLANNER_INPUT_CONTENT_INVALID")
    refs: set[str] = set()
    for position, item in enumerate(unresolved):
        if not isinstance(item, Mapping):
            raise LiveAgentDecisionClosureV1Error("PLANNER_UNRESOLVED_ITEM_INVALID")
        ref = _require_string(item.get("ref"), f"unresolved_items[{position}].ref")
        if ref in refs:
            raise LiveAgentDecisionClosureV1Error("PLANNER_UNRESOLVED_REF_DUPLICATE")
        refs.add(ref)
    card_ids: set[str] = set()
    for position, card in enumerate(cards):
        if not isinstance(card, Mapping):
            raise LiveAgentDecisionClosureV1Error("PLANNER_CARD_INVALID")
        card_id = _require_string(card.get("card_id"), f"legal_action_cards[{position}].card_id")
        if card_id in card_ids:
            raise LiveAgentDecisionClosureV1Error("PLANNER_CARD_DUPLICATE")
        card_ids.add(card_id)
        if card.get("case_id") != X_EISD_CASE_ID:
            raise LiveAgentDecisionClosureV1Error("PLANNER_CARD_CASE_SCOPE_INVALID")
        if _require_string(card.get("addresses_ref"), "planner_card.addresses_ref") not in refs:
            raise LiveAgentDecisionClosureV1Error("PLANNER_CARD_ADDRESS_NOT_FRESH_UNRESOLVED")
    return copy.deepcopy(dict(value))


def validate_planner_proposal(
    planner_input: Mapping[str, Any], proposal: Mapping[str, Any]
) -> dict[str, Any]:
    """Admit only a current exact card selection or explicit zero-card abstention."""

    packet = _validate_planner_input(planner_input)
    if set(proposal) != {"case_id", "decision", "selected_card_ids", "rationales"}:
        raise LiveAgentDecisionClosureV1Error("PLANNER_PROPOSAL_FIELDS_INVALID")
    if proposal.get("case_id") != X_EISD_CASE_ID:
        raise LiveAgentDecisionClosureV1Error("PLANNER_PROPOSAL_CASE_ID_MISMATCH")
    decision = proposal.get("decision")
    if decision not in {"SELECT_ACTIONS", "ABSTAIN_NO_ACTION"}:
        raise LiveAgentDecisionClosureV1Error("PLANNER_DECISION_INVALID")
    selected = proposal.get("selected_card_ids")
    if (
        not isinstance(selected, list)
        or any(not isinstance(item, str) or not item for item in selected)
        or len(selected) != len(set(selected))
    ):
        raise LiveAgentDecisionClosureV1Error("PLANNER_SELECTED_CARD_IDS_INVALID")
    if decision == "SELECT_ACTIONS" and not selected:
        raise LiveAgentDecisionClosureV1Error("PLANNER_SELECT_REQUIRES_CARD")
    if decision == "ABSTAIN_NO_ACTION" and selected:
        raise LiveAgentDecisionClosureV1Error("PLANNER_ABSTAIN_MUST_SELECT_ZERO")
    cards = {card["card_id"]: card for card in packet["legal_action_cards"]}
    if not set(selected).issubset(cards):
        raise LiveAgentDecisionClosureV1Error("PLANNER_SELECTED_ILLEGAL_CARD")
    refs = {item["ref"] for item in packet["unresolved_items"]}
    for card_id in selected:
        card = cards[card_id]
        if card.get("case_id") != X_EISD_CASE_ID:
            raise LiveAgentDecisionClosureV1Error("PLANNER_SELECTED_CROSS_CASE_CARD")
        if card.get("addresses_ref") not in refs:
            raise LiveAgentDecisionClosureV1Error("PLANNER_SELECTED_CARD_NOT_FRESH")
    rationales = proposal.get("rationales")
    if not isinstance(rationales, Mapping) or set(rationales) != set(selected):
        raise LiveAgentDecisionClosureV1Error("PLANNER_RATIONALES_DO_NOT_MATCH_SELECTION")
    normalized_rationales = {
        card_id: _require_string(rationales[card_id], f"rationales.{card_id}")
        for card_id in selected
    }
    return {
        "schema_version": "paper-blind-planner-proposal-admission/v2",
        "proposal_status": "ADMISSIBLE_CARD_SELECTION_ONLY",
        "case_id": X_EISD_CASE_ID,
        "decision": decision,
        "selected_card_ids": list(selected),
        "rationales": normalized_rationales,
        "execution_authorization": "REQUIRES_SEPARATE_DETERMINISTIC_AUTHORIZATION",
        "scientific_disposition": "NOT_EVALUATED",
    }


def build_planner_proposal_schema(planner_input: Mapping[str, Any]) -> dict[str, Any]:
    """Build the existing provider-portable schema over only current card IDs."""

    packet = _validate_planner_input(planner_input)
    card_ids = [card["card_id"] for card in packet["legal_action_cards"]]
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
            "properties": {card_id: {"type": "string"}},
        }
        for card_id in card_ids
    )
    return {
        "type": "object",
        "additionalProperties": False,
        "required": ["case_id", "decision", "selected_card_ids", "rationales"],
        "properties": {
            "case_id": {"type": "string", "enum": [X_EISD_CASE_ID]},
            "decision": {
                "type": "string",
                "enum": ["SELECT_ACTIONS", "ABSTAIN_NO_ACTION"],
            },
            "selected_card_ids": {
                "type": "array",
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


def validate_campaign_config(config: Mapping[str, Any]) -> dict[str, Any]:
    config = copy.deepcopy(dict(config))
    required = {
        "schema_version",
        "campaign_id",
        "execution_status",
        "completion_receipt_path",
        "completion_receipt_sha256",
        "budget_ledger_path",
        "budget_usd",
        "max_http_attempts",
        "max_completed_calls",
        "max_attempts_per_exact_role_case_model",
        "automatic_retries",
        "schema_compatibility_repairs_allowed",
        "schema_compatibility_repairs_used",
        "schema_compatibility_repair",
        "semantic_prompt_tuning_allowed",
        "case_id",
        "profile_mode",
        "planner_prompt",
        "model",
        "max_output_tokens",
        "claim_ceiling",
        "source_science_review_status",
        "held_out_status",
    }
    _require_exact_keys(config, required, "campaign_config")
    if config.get("schema_version") != CAMPAIGN_CONFIG_SCHEMA:
        raise LiveAgentDecisionClosureV1Error("CAMPAIGN_CONFIG_SCHEMA_INVALID")
    _require_string(config.get("campaign_id"), "campaign_id")
    if config.get("case_id") != X_EISD_CASE_ID or config.get("profile_mode") != PROFILE_MODE:
        raise LiveAgentDecisionClosureV1Error("CAMPAIGN_CASE_OR_PROFILE_MODE_INVALID")
    if config.get("execution_status") not in {CAMPAIGN_OPEN_STATUS, CAMPAIGN_CLOSED_STATUS}:
        raise LiveAgentDecisionClosureV1Error("CAMPAIGN_EXECUTION_STATUS_INVALID")
    budget = _require_decimal(config.get("budget_usd"), "budget_usd")
    if budget <= 0 or budget > Decimal("1.00"):
        raise LiveAgentDecisionClosureV1Error("CAMPAIGN_BUDGET_EXCEEDS_AUTHORITY")
    if (
        config.get("max_http_attempts") != 6
        or config.get("max_completed_calls") != 4
        or config.get("max_attempts_per_exact_role_case_model") != 6
    ):
        raise LiveAgentDecisionClosureV1Error("CAMPAIGN_CALL_LIMITS_INVALID")
    if config.get("automatic_retries") != 0:
        raise LiveAgentDecisionClosureV1Error("AUTOMATIC_RETRIES_FORBIDDEN")
    if config.get("schema_compatibility_repairs_allowed") != 1:
        raise LiveAgentDecisionClosureV1Error("SCHEMA_REPAIR_LIMIT_INVALID")
    repairs_used = config.get("schema_compatibility_repairs_used")
    if not isinstance(repairs_used, int) or isinstance(repairs_used, bool) or not 0 <= repairs_used <= 1:
        raise LiveAgentDecisionClosureV1Error("SCHEMA_REPAIR_COUNT_INVALID")
    repair = config.get("schema_compatibility_repair")
    if repairs_used == 0 and repair is not None:
        raise LiveAgentDecisionClosureV1Error("UNUSED_SCHEMA_REPAIR_RECORD_FORBIDDEN")
    if repairs_used == 1:
        if not isinstance(repair, Mapping):
            raise LiveAgentDecisionClosureV1Error("SCHEMA_REPAIR_RECORD_REQUIRED")
        repair = dict(repair)
        _require_exact_keys(
            repair,
            {
                "failure_root",
                "request_file_sha256",
                "raw_response_file_sha256",
                "receipt_file_sha256",
                "provider_error_code",
                "unsupported_keyword",
                "repair_scope",
            },
            "schema_compatibility_repair",
        )
        if (
            repair.get("provider_error_code") != "invalid_json_schema"
            or repair.get("unsupported_keyword") != "uniqueItems"
            or repair.get("repair_scope")
            != "OPENAI_STRICT_SCHEMA_SUBSET_NORMALIZATION_ONLY"
        ):
            raise LiveAgentDecisionClosureV1Error("SCHEMA_REPAIR_RECORD_INVALID")
        repair_root = _repository_path(repair.get("failure_root"), "failure_root")
        allowed_failure_root = (
            REPO_ROOT
            / "evidence"
            / "live_agent_decision_closure_v1"
            / "development_runs"
        ).resolve()
        try:
            repair_root.relative_to(allowed_failure_root)
        except ValueError as error:
            raise LiveAgentDecisionClosureV1Error(
                "SCHEMA_REPAIR_FAILURE_ROOT_OUTSIDE_EVIDENCE"
            ) from error
        repair_files = {
            "request_file_sha256": repair_root
            / POSITIVE_ARM_ID
            / "live_call"
            / "request_payload.json",
            "raw_response_file_sha256": repair_root
            / POSITIVE_ARM_ID
            / "live_call"
            / "raw_response.txt",
            "receipt_file_sha256": repair_root
            / POSITIVE_ARM_ID
            / "live_call"
            / "model_call_receipt.json",
        }
        for hash_key, artifact_path in repair_files.items():
            expected_hash = repair.get(hash_key)
            if (
                not isinstance(expected_hash, str)
                or not re.fullmatch(r"[0-9a-f]{64}", expected_hash)
                or not artifact_path.is_file()
                or hashlib.sha256(artifact_path.read_bytes()).hexdigest()
                != expected_hash
            ):
                raise LiveAgentDecisionClosureV1Error(
                    f"SCHEMA_REPAIR_ARTIFACT_HASH_MISMATCH:{hash_key}"
                )
    if config.get("semantic_prompt_tuning_allowed") != 0:
        raise LiveAgentDecisionClosureV1Error("SEMANTIC_PROMPT_TUNING_FORBIDDEN")
    if config.get("max_output_tokens") != _FROZEN_MAX_OUTPUT_TOKENS:
        raise LiveAgentDecisionClosureV1Error("MAX_OUTPUT_TOKENS_INVALID")
    ledger_path = _repository_path(config.get("budget_ledger_path"), "budget_ledger_path")
    allowed_ledger_root = (REPO_ROOT / "local" / "live_agent_decision_closure_v1").resolve()
    if ledger_path.parent != allowed_ledger_root or ledger_path.suffix != ".json":
        raise LiveAgentDecisionClosureV1Error("BUDGET_LEDGER_PATH_OUTSIDE_CAMPAIGN_LOCAL_ROOT")

    prompt = config.get("planner_prompt")
    model = config.get("model")
    if not isinstance(prompt, Mapping) or not isinstance(model, Mapping):
        raise LiveAgentDecisionClosureV1Error("CAMPAIGN_PROMPT_OR_MODEL_INVALID")
    _require_exact_keys(dict(prompt), {"path", "version", "sha256"}, "planner_prompt")
    if dict(prompt) != _FROZEN_PLANNER_PROMPT:
        raise LiveAgentDecisionClosureV1Error("PLANNER_PROMPT_NOT_FROZEN")
    prompt_path = _repository_path(prompt.get("path"), "planner_prompt")
    if not prompt_path.is_file() or text_sha256(prompt_path.read_text(encoding="utf-8")) != prompt.get("sha256"):
        raise LiveAgentDecisionClosureV1Error("PLANNER_PROMPT_HASH_MISMATCH")
    _require_exact_keys(
        dict(model),
        {
            "model_id",
            "accepted_returned_model_ids",
            "provider_endpoint_tag",
            "expected_provider_display_name",
            "allowed_service_tiers",
            "input_price_per_million_usd",
            "output_price_per_million_usd",
            "reasoning_effort",
            "include_temperature_zero",
            "metadata_sha256",
        },
        "model",
    )
    if dict(model) != _FROZEN_MODEL:
        raise LiveAgentDecisionClosureV1Error("FROZEN_LUNA_MODEL_CONTRACT_MISMATCH")
    if (
        config.get("claim_ceiling") != CLAIM_CEILING
        or config.get("source_science_review_status") != SOURCE_SCIENCE_REVIEW_STATUS
        or config.get("held_out_status") != HELD_OUT_STATUS
    ):
        raise LiveAgentDecisionClosureV1Error("CAMPAIGN_SCIENTIFIC_BOUNDARY_MISMATCH")

    completion_path = config.get("completion_receipt_path")
    completion_sha = config.get("completion_receipt_sha256")
    if config["execution_status"] == CAMPAIGN_OPEN_STATUS:
        if completion_path is not None or completion_sha is not None:
            raise LiveAgentDecisionClosureV1Error("OPEN_CAMPAIGN_COMPLETION_RECEIPT_FORBIDDEN")
    else:
        completion_file = _repository_path(completion_path, "completion_receipt_path")
        allowed_completion_root = (
            REPO_ROOT
            / "evidence"
            / "live_agent_decision_closure_v1"
            / "development_runs"
        ).resolve()
        try:
            completion_file.relative_to(allowed_completion_root)
        except ValueError as error:
            raise LiveAgentDecisionClosureV1Error(
                "COMPLETION_RECEIPT_OUTSIDE_EVIDENCE_ROOT"
            ) from error
        if completion_file.name != "live_agent_decision_closure_manifest_v1.json":
            raise LiveAgentDecisionClosureV1Error("COMPLETION_RECEIPT_FILENAME_INVALID")
        if not isinstance(completion_sha, str) or not re.fullmatch(
            r"[0-9a-f]{64}", completion_sha
        ):
            raise LiveAgentDecisionClosureV1Error("COMPLETION_RECEIPT_HASH_INVALID")
    return copy.deepcopy(config)


def load_campaign_config(path: Path = CAMPAIGN_CONFIG_PATH) -> dict[str, Any]:
    return validate_campaign_config(load_json_object(path))


def campaign_budget_ledger_path(config: Mapping[str, Any]) -> Path:
    return _repository_path(config.get("budget_ledger_path"), "budget_ledger_path")


def validate_campaign_completion_receipt(
    config: Mapping[str, Any],
) -> dict[str, Any]:
    """Bind one closed campaign config to its frozen aggregate receipt."""

    config = validate_campaign_config(config)
    if config.get("execution_status") != CAMPAIGN_CLOSED_STATUS:
        raise LiveAgentDecisionClosureV1Error("CAMPAIGN_NOT_CLOSED")
    receipt_path = _repository_path(
        config.get("completion_receipt_path"), "completion_receipt_path"
    )
    receipt_hash = config.get("completion_receipt_sha256")
    if (
        not receipt_path.is_file()
        or hashlib.sha256(receipt_path.read_bytes()).hexdigest() != receipt_hash
    ):
        raise LiveAgentDecisionClosureV1Error("CAMPAIGN_COMPLETION_RECEIPT_INVALID")
    receipt = load_json_object(receipt_path)
    if (
        receipt.get("schema_version") != MANIFEST_SCHEMA
        or receipt.get("campaign_id") != config.get("campaign_id")
        or receipt.get("campaign_state") != "COMPLETED_CALLS_FROZEN"
        or receipt.get("case_id") != X_EISD_CASE_ID
        or receipt.get("profile_mode") != PROFILE_MODE
        or receipt.get("planner_mode") != PLANNER_MODE
        or receipt.get("transport") != TRANSPORT
        or receipt.get("affected_rule_instance_id") != TARGET_RULE_INSTANCE_ID
        or receipt.get("positive_arm_id") != POSITIVE_ARM_ID
        or receipt.get("stop_arm_id") != STOP_ARM_ID
        or receipt.get("positive_transition") != "UNRESOLVED_TO_PASS"
        or receipt.get("stop_transition") != "UNRESOLVED_TO_UNRESOLVED"
        or receipt.get("positive_terminal_disposition")
        != "ABSTAIN_OR_HUMAN_REVIEW"
        or receipt.get("stop_terminal_disposition") != "ABSTAIN_OR_HUMAN_REVIEW"
        or receipt.get("claim_ceiling") != CLAIM_CEILING
        or receipt.get("source_science_review_status")
        != SOURCE_SCIENCE_REVIEW_STATUS
        or receipt.get("held_out_status") != HELD_OUT_STATUS
        or receipt.get("scientific_support_status") != SCIENTIFIC_SUPPORT_STATUS
        or receipt.get("result_status") != RESULT_STATUS
        or receipt.get("boundary") != CAMPAIGN_BOUNDARY
    ):
        raise LiveAgentDecisionClosureV1Error("CAMPAIGN_COMPLETION_RECEIPT_INVALID")

    completed_calls = receipt.get("completed_api_calls")
    http_attempts = receipt.get("http_attempts")
    if (
        not isinstance(completed_calls, int)
        or isinstance(completed_calls, bool)
        or not 1 <= completed_calls <= config["max_completed_calls"]
        or not isinstance(http_attempts, int)
        or isinstance(http_attempts, bool)
        or not completed_calls <= http_attempts <= config["max_http_attempts"]
        or (
            config["schema_compatibility_repairs_used"] == 1
            and http_attempts < completed_calls + 1
        )
    ):
        raise LiveAgentDecisionClosureV1Error("CAMPAIGN_COMPLETION_CALL_TOTALS_INVALID")
    actual_cost = _require_decimal(receipt.get("actual_cost_usd"), "actual_cost_usd")
    cap = _require_decimal(config.get("budget_usd"), "budget_usd")
    if actual_cost < 0 or actual_cost > cap:
        raise LiveAgentDecisionClosureV1Error("CAMPAIGN_COMPLETION_COST_INVALID")

    budget = receipt.get("budget")
    if not isinstance(budget, Mapping):
        raise LiveAgentDecisionClosureV1Error("CAMPAIGN_COMPLETION_BUDGET_INVALID")
    _require_exact_keys(
        dict(budget),
        {
            "actual_cost_usd",
            "campaign_id",
            "cap_usd",
            "completed_calls",
            "max_attempts_per_cell",
            "max_completed_calls",
            "persistence",
            "remaining_budget_usd",
            "reported_cost_available",
            "unresolved_inflight_reservation",
        },
        "completion_receipt.budget",
    )
    remaining = _require_decimal(
        budget.get("remaining_budget_usd"), "remaining_budget_usd"
    )
    if (
        budget.get("campaign_id") != config["campaign_id"]
        or _require_decimal(budget.get("cap_usd"), "budget.cap_usd") != cap
        or _require_decimal(budget.get("actual_cost_usd"), "budget.actual_cost_usd")
        != actual_cost
        or budget.get("completed_calls") != completed_calls
        or budget.get("max_completed_calls") != config["max_completed_calls"]
        or budget.get("max_attempts_per_cell")
        != config["max_attempts_per_exact_role_case_model"]
        or budget.get("persistence") != "ATOMIC_JSON"
        or remaining != cap - actual_cost
        or budget.get("reported_cost_available") is not True
        or budget.get("unresolved_inflight_reservation") is not False
    ):
        raise LiveAgentDecisionClosureV1Error("CAMPAIGN_COMPLETION_BUDGET_INVALID")
    return copy.deepcopy(receipt)


def require_campaign_open(config: Mapping[str, Any]) -> None:
    config = validate_campaign_config(config)
    if config.get("execution_status") == CAMPAIGN_OPEN_STATUS:
        return
    validate_campaign_completion_receipt(config)
    raise LiveAgentDecisionClosureV1Error(CAMPAIGN_CLOSED_ERROR)


def build_budget(config: Mapping[str, Any]) -> OpenRouterBudgetLedger:
    config = validate_campaign_config(config)
    return OpenRouterBudgetLedger(
        cap_usd=Decimal(str(config["budget_usd"])),
        max_completed_calls=int(config["max_completed_calls"]),
        max_attempts_per_cell=int(config["max_attempts_per_exact_role_case_model"]),
        campaign_id=str(config["campaign_id"]),
        state_path=campaign_budget_ledger_path(config),
    )


def _contains_schema_keyword(value: Any, keyword: str) -> bool:
    if isinstance(value, Mapping):
        return keyword in value or any(
            _contains_schema_keyword(item, keyword) for item in value.values()
        )
    if isinstance(value, list):
        return any(_contains_schema_keyword(item, keyword) for item in value)
    return False


def reconcile_schema_compatibility_repair(
    *,
    config: Mapping[str, Any],
    budget: OpenRouterBudgetLedger,
) -> dict[str, Any] | None:
    """Bind and reconcile the one observed pre-generation schema rejection."""

    config = validate_campaign_config(config)
    if config["schema_compatibility_repairs_used"] == 0:
        return None
    repair = dict(config["schema_compatibility_repair"])
    repair_root = _repository_path(repair["failure_root"], "failure_root")
    live_root = repair_root / POSITIVE_ARM_ID / "live_call"
    request = load_json_object(live_root / "request_payload.json")
    raw_response = load_json_object(live_root / "raw_response.txt")
    receipt = load_json_object(live_root / "model_call_receipt.json")
    raw_error = raw_response.get("error")
    raw_metadata = raw_error.get("metadata") if isinstance(raw_error, Mapping) else None
    nested_raw = raw_metadata.get("raw") if isinstance(raw_metadata, Mapping) else None
    try:
        nested_error = json.loads(nested_raw)["error"] if isinstance(nested_raw, str) else None
    except (json.JSONDecodeError, KeyError, TypeError) as error:
        raise LiveAgentDecisionClosureV1Error(
            "SCHEMA_REPAIR_PROVIDER_ERROR_UNREADABLE"
        ) from error
    request_schema = (
        request.get("response_format", {})
        .get("json_schema", {})
        .get("schema")
    )
    if (
        receipt.get("status") != "REJECTED_FAIL_CLOSED"
        or receipt.get("transport_status") != "TRANSPORT_FAILED"
        or receipt.get("http_status") != 400
        or receipt.get("response_id") is not None
        or receipt.get("reported_cost_usd") is not None
        or receipt.get("reason_codes") != ["HTTP_ERROR:400"]
        or receipt.get("requested_model") != "openai/gpt-5.6-luna"
        or receipt.get("hashes", {}).get("request_payload_sha256")
        != canonical_json_sha256(request)
        or receipt.get("hashes", {}).get("raw_response_sha256")
        != hashlib.sha256(
            (live_root / "raw_response.txt").read_text(encoding="utf-8").encode("utf-8")
        ).hexdigest()
        or raw_response.get("id") is not None
        or "choices" in raw_response
        or "usage" in raw_response
        or not isinstance(raw_metadata, Mapping)
        or raw_metadata.get("provider_name") != "OpenAI"
        or raw_metadata.get("provider_error_code") != "invalid_json_schema"
        or not isinstance(nested_error, Mapping)
        or nested_error.get("code") != "invalid_json_schema"
        or "uniqueItems" not in str(nested_error.get("message"))
        or not isinstance(request_schema, Mapping)
        or not _contains_schema_keyword(request_schema, "uniqueItems")
    ):
        raise LiveAgentDecisionClosureV1Error(
            "SCHEMA_REPAIR_PRE_GENERATION_EVIDENCE_INVALID"
        )
    usage = receipt.get("usage")
    if not isinstance(usage, Mapping) or any(value is not None for value in usage.values()):
        raise LiveAgentDecisionClosureV1Error(
            "SCHEMA_REPAIR_PRE_GENERATION_USAGE_PRESENT"
        )
    current_schema = build_planner_proposal_schema(
        build_planner_input(build_frozen_decision_state(), include_action_card=True)
    )
    if any(
        _contains_schema_keyword(current_schema, keyword)
        for keyword in ("uniqueItems", "minLength", "const", "$schema")
    ):
        raise LiveAgentDecisionClosureV1Error(
            "SCHEMA_REPAIR_CURRENT_SCHEMA_NOT_NORMALIZED"
        )
    before = budget.snapshot()
    receipt_path = repair_root / "schema_compatibility_repair_receipt.json"
    if before["reported_cost_available"] is False:
        budget.reconcile_first_pre_generation_schema_rejection(
            role="PLANNER",
            case_id=X_EISD_CASE_ID,
            model_id="openai/gpt-5.6-luna",
        )
    elif not receipt_path.is_file():
        raise LiveAgentDecisionClosureV1Error(
            "SCHEMA_REPAIR_LEDGER_ALREADY_OPEN_WITHOUT_RECEIPT"
        )
    after = budget.snapshot()
    if (
        after["reported_cost_available"] is not True
        or after["completed_calls"] != 0
        or after["actual_cost_usd"] != "0"
        or budget.attempts_by_cell
        != {("PLANNER", X_EISD_CASE_ID, "openai/gpt-5.6-luna"): 1}
    ):
        raise LiveAgentDecisionClosureV1Error(
            "SCHEMA_REPAIR_LEDGER_RECONCILIATION_INVALID"
        )
    reconciliation = {
        "schema_version": SCHEMA_REPAIR_RECEIPT_SCHEMA,
        "campaign_id": config["campaign_id"],
        "status": "RECONCILED_ONE_PRE_GENERATION_SCHEMA_REJECTION",
        "repair_number": 1,
        "provider": "OpenAI",
        "model": "openai/gpt-5.6-luna",
        "http_status": 400,
        "provider_error_code": "invalid_json_schema",
        "unsupported_keyword": "uniqueItems",
        "response_id": None,
        "api_reported_usage": None,
        "api_reported_cost_usd": None,
        "budget_accounted_cost_usd": "0",
        "attempt_count_preserved": 1,
        "schema_repair_scope": repair["repair_scope"],
        "prompt_changed": False,
        "semantic_expectation_changed": False,
        "prior_artifact_hashes": {
            "request_payload_file_sha256": repair["request_file_sha256"],
            "raw_response_file_sha256": repair["raw_response_file_sha256"],
            "model_call_receipt_file_sha256": repair["receipt_file_sha256"],
        },
        "budget_after_reconciliation": after,
        "boundary": "The provider rejected the unsupported schema before generation and returned no response ID, usage, or cost. This receipt unlocks only the single documented schema-only repair; it does not claim an admitted model proposal.",
    }
    if receipt_path.is_file():
        if load_json_object(receipt_path) != reconciliation:
            raise LiveAgentDecisionClosureV1Error(
                "SCHEMA_REPAIR_RECONCILIATION_RECEIPT_MISMATCH"
            )
    else:
        _write_json(receipt_path, reconciliation)
    return reconciliation


def _model_spec(config: Mapping[str, Any]) -> OpenRouterModelSpec:
    model = config["model"]
    return OpenRouterModelSpec(
        model_id=str(model["model_id"]),
        provider_endpoint_tag=str(model["provider_endpoint_tag"]),
        expected_provider_display_name=str(model["expected_provider_display_name"]),
        accepted_returned_model_ids=tuple(model["accepted_returned_model_ids"]),
        allowed_service_tiers=tuple(model["allowed_service_tiers"]),
        prompt_price_per_token_usd=Decimal(str(model["input_price_per_million_usd"])) / Decimal("1000000"),
        completion_price_per_token_usd=Decimal(str(model["output_price_per_million_usd"])) / Decimal("1000000"),
        reasoning_effort=model["reasoning_effort"],
        include_temperature_zero=bool(model["include_temperature_zero"]),
        metadata_sha256=model["metadata_sha256"],
    )


def _remove_random_composition(complete_graph: Mapping[str, Any]) -> dict[str, Any]:
    graph = copy.deepcopy(dict(complete_graph))
    sources = graph.get("evidence_items")
    if not isinstance(sources, list):
        raise LiveAgentDecisionClosureV1Error("X_EISD_EVIDENCE_ITEMS_MISSING")
    source = next(
        (
            item
            for item in sources
            if isinstance(item, dict)
            and item.get("source_id") == "xeisd_random_candidate_pool"
        ),
        None,
    )
    if not isinstance(source, dict):
        raise LiveAgentDecisionClosureV1Error("X_EISD_RANDOM_SOURCE_MISSING")
    source.pop("sample_composition", None)
    source.pop("sample_system_composition_declaration_status", None)
    attestations = source.get("lookup_attestations")
    if not isinstance(attestations, list):
        raise LiveAgentDecisionClosureV1Error("X_EISD_LOOKUP_ATTESTATIONS_INVALID")
    source["lookup_attestations"] = [item for item in attestations if item != LOOKUP_ID]
    return graph


def _rule_by_id(results: Sequence[Mapping[str, Any]], rule_id: str) -> dict[str, Any]:
    matches = [dict(item) for item in results if item.get("rule_instance_id") == rule_id]
    if len(matches) != 1:
        raise LiveAgentDecisionClosureV1Error(f"EXPECTED_ONE_RULE_RESULT:{rule_id}")
    return copy.deepcopy(matches[0])


def _status_transitions(
    before: Sequence[Mapping[str, Any]], after: Sequence[Mapping[str, Any]]
) -> list[dict[str, str]]:
    before_by_id = {str(item["rule_instance_id"]): str(item["status"]) for item in before}
    after_by_id = {str(item["rule_instance_id"]): str(item["status"]) for item in after}
    if set(before_by_id) != set(after_by_id):
        raise LiveAgentDecisionClosureV1Error("RULE_INVENTORY_CHANGED")
    return [
        {
            "rule_instance_id": rule_id,
            "before_status": before_by_id[rule_id],
            "after_status": after_by_id[rule_id],
        }
        for rule_id in sorted(before_by_id)
        if before_by_id[rule_id] != after_by_id[rule_id]
    ]


def _lookup_entry(allowlist: Mapping[str, Any]) -> dict[str, Any]:
    entries = allowlist.get("entries")
    if not isinstance(entries, list):
        raise LiveAgentDecisionClosureV1Error("LOOKUP_ALLOWLIST_ENTRIES_INVALID")
    matches = [entry for entry in entries if isinstance(entry, Mapping) and entry.get("lookup_id") == LOOKUP_ID]
    if len(matches) != 1:
        raise LiveAgentDecisionClosureV1Error("EXACT_LOOKUP_ENTRY_MISSING")
    return copy.deepcopy(dict(matches[0]))


def _resolution_policy(policy_id: str) -> dict[str, Any]:
    registry = load_json_object(REPO_ROOT / "registries" / "rules_v1" / "resolution_policies_v1.json")
    policies = registry.get("policies")
    if not isinstance(policies, list):
        raise LiveAgentDecisionClosureV1Error("RESOLUTION_POLICY_REGISTRY_INVALID")
    matches = [item for item in policies if isinstance(item, Mapping) and item.get("resolution_policy_id") == policy_id]
    if len(matches) != 1:
        raise LiveAgentDecisionClosureV1Error("RESOLUTION_POLICY_MISSING")
    policy = copy.deepcopy(dict(matches[0]))
    if policy.get("unresolved_route") != "SOURCE_LOOKUP" or "SOURCE_LOOKUP" not in policy.get("allowed_routes", []):
        raise LiveAgentDecisionClosureV1Error("SOURCE_LOOKUP_NOT_ALLOWED_BY_POLICY")
    return policy


def build_frozen_decision_state() -> dict[str, Any]:
    evidence_root = REPO_ROOT / "evidence" / "real_case_vertical_slice_v1"
    complete_graph = load_json_object(evidence_root / "outputs" / "xeisd_a1_complete_casegraph.json")
    before_graph = _remove_random_composition(complete_graph)
    rules_bundle = load_rules_v1_bundle(REPO_ROOT / "registries" / "rules_v1")
    before_results = evaluate_xeisd_case(case_graph=before_graph, **rules_bundle)
    target = _rule_by_id(before_results, TARGET_RULE_INSTANCE_ID)
    if target.get("status") != "UNRESOLVED" or target.get("claim_effect", {}).get("route") != "SOURCE_LOOKUP":
        raise LiveAgentDecisionClosureV1Error("TARGET_RULE_NOT_LOOKUP_UNRESOLVED")
    policy = _resolution_policy(str(target["resolution_policy_id"]))
    allowlist = load_json_object(evidence_root / "xeisd_source_lookup_allowlist_v1.json")
    entry = _lookup_entry(allowlist)
    request = {
        "lookup_id": LOOKUP_ID,
        "case_id": X_EISD_CASE_ID,
        "target_kind": str(entry["target_kind"]),
        "target_id": str(entry["target_id"]),
        "locator_id": str(entry["locator_id"]),
    }
    if target.get("target") != {"kind": request["target_kind"], "id": request["target_id"]}:
        raise LiveAgentDecisionClosureV1Error("LOOKUP_TARGET_RULE_IDENTITY_MISMATCH")
    unresolved = []
    for result in before_results:
        if result.get("status") == "UNRESOLVED":
            unresolved.append(
                {
                    "kind": "ACTIVE_RULE_INSTANCE",
                    "ref": result["rule_instance_id"],
                    "status": "UNRESOLVED",
                    "gap_type": result.get("claim_effect", {}).get("decision_class", "UNRESOLVED_RULE"),
                    "reason_codes": list(result.get("reason_codes", [])),
                    "source": {
                        "runtime_subrule_id": result.get("runtime_subrule_id"),
                        "evaluation_contract_id": result.get("evaluation_contract_id"),
                        "resolution_policy_id": result.get("resolution_policy_id"),
                    },
                }
            )
    card = {
        "card_id": ACTION_CARD_ID,
        "case_id": X_EISD_CASE_ID,
        "addresses_ref": TARGET_RULE_INSTANCE_ID,
        "action_kind": "EXACT_ATTESTATION",
        "route": "SOURCE_LOOKUP",
        "description": "Read the one predeclared local review derivative at its exact allowlisted locator and attach only its bounded field update.",
        "lookup_id": LOOKUP_ID,
        "requested_locator_id": request["locator_id"],
        "resolution_policy_id": policy["resolution_policy_id"],
        "prerequisites": [
            "The current target RuleInstance is UNRESOLVED and requests SOURCE_LOOKUP.",
            "The exact lookup ID, target, locator, fixture hash, and local path are already allowlisted.",
        ],
        "prohibitions": [
            "No web search, undeclared source discovery, RAG, or free-text extraction.",
            "No scientific support, shared-population, independence, mechanism, or final-conclusion claim.",
        ],
        "required_asset_ids": [LOOKUP_ID],
    }
    return {
        "case_id": X_EISD_CASE_ID,
        "profile_mode": PROFILE_MODE,
        "recorded_profile": before_graph,
        "before_rule_results": before_results,
        "target_rule_result": target,
        "unresolved_items": sorted(unresolved, key=lambda item: item["ref"]),
        "legal_card": card,
        "lookup_request": request,
        "allowlist": allowlist,
        "rules_bundle": rules_bundle,
    }


def build_planner_input(state: Mapping[str, Any], *, include_action_card: bool) -> dict[str, Any]:
    cards = [copy.deepcopy(state["legal_card"])] if include_action_card else []
    packet = {
        "schema_version": "paper-blind-planner-visible-input/v2",
        "case_id": X_EISD_CASE_ID,
        "planner_boundary": "Select only a listed current card or abstain. Do not execute, invent a card, modify a Rule, or state a scientific conclusion.",
        "unresolved_items": copy.deepcopy(state["unresolved_items"]),
        "legal_action_cards": cards,
        "required_output": {
            "case_id": "same as input",
            "decision": "SELECT_ACTIONS or ABSTAIN_NO_ACTION",
            "selected_card_ids": "listed card IDs only; empty only for ABSTAIN_NO_ACTION",
            "rationales": "object keyed exactly by selected card ID",
        },
    }
    _validate_planner_input(packet)
    return packet


def _attempt_count(budget: OpenRouterBudgetLedger) -> int:
    budget.snapshot()
    return sum(budget.attempts_by_cell.values())


def _call_planner(
    *,
    client: OpenRouterProposalClient,
    config: Mapping[str, Any],
    planner_input: Mapping[str, Any],
) -> dict[str, Any]:
    if _attempt_count(client.budget) >= int(config["max_http_attempts"]):
        raise LiveAgentDecisionClosureV1Error("MAX_HTTP_ATTEMPTS_REACHED")
    prompt_record = config["planner_prompt"]
    prompt = _repository_path(prompt_record["path"], "planner_prompt").read_text(encoding="utf-8")
    call = client.call(
        role="PLANNER",
        case_id=X_EISD_CASE_ID,
        model_spec=_model_spec(config),
        system_prompt=prompt,
        visible_input=planner_input,
        output_schema=build_planner_proposal_schema(planner_input),
        max_tokens=int(config["max_output_tokens"]),
        prompt_version=str(prompt_record["version"]),
    )
    receipt = copy.deepcopy(call["receipt"])
    proposal = call.get("parsed_proposal")
    receipt["routing_proposal_sha256"] = (
        canonical_json_sha256(proposal) if isinstance(proposal, Mapping) else None
    )
    receipt["proposal_envelope_sha256"] = None
    call = copy.deepcopy(call)
    call["receipt"] = receipt
    return call


def _admit_and_authorize(
    *, arm_id: str, planner_input: Mapping[str, Any], call: Mapping[str, Any]
) -> tuple[dict[str, Any], dict[str, Any]]:
    receipt = call.get("receipt")
    proposal = call.get("admitted_proposal")
    if not isinstance(receipt, Mapping) or receipt.get("status") != "ADMITTED_TYPED_PROPOSAL" or not isinstance(proposal, Mapping):
        raise LiveAgentDecisionClosureV1Error("LIVE_PLANNER_TRANSPORT_REJECTED")
    if _TERMINAL_LANGUAGE.search(_canonical_json_text(proposal)):
        raise LiveAgentDecisionClosureV1Error("PLANNER_SCIENTIFIC_VERDICT_LANGUAGE_FORBIDDEN")
    try:
        admission = validate_planner_proposal(planner_input, proposal)
    except LiveAgentDecisionClosureV1Error as error:
        raise LiveAgentDecisionClosureV1Error("PLANNER_PROPOSAL_DETERMINISTIC_REJECTION") from error
    selected = admission["selected_card_ids"]
    if arm_id == POSITIVE_ARM_ID:
        if admission["decision"] != "SELECT_ACTIONS" or selected != [ACTION_CARD_ID]:
            raise LiveAgentDecisionClosureV1Error("POSITIVE_ARM_EXACT_CARD_NOT_SELECTED")
        authorization = {
            "schema_version": "live-agent-decision-closure-authorization/v1",
            "case_id": X_EISD_CASE_ID,
            "arm_id": arm_id,
            "status": "AUTHORIZED_EXACT_ALLOWLISTED_LOOKUP",
            "selected_card_ids": selected,
            "authorized_action_count": 1,
            "authorization_basis": [
                "CURRENT_UNRESOLVED_RULE_REQUESTS_SOURCE_LOOKUP",
                "CURRENT_CARD_ADDRESSES_EXACT_RULEINSTANCE",
                "EXACT_LOOKUP_ID_TARGET_LOCATOR_AND_HASH_PREDECLARED",
            ],
            "model_execution_authority": "NONE",
            "scientific_disposition": "NOT_EVALUATED",
        }
    elif arm_id == STOP_ARM_ID:
        if admission["decision"] != "ABSTAIN_NO_ACTION" or selected:
            raise LiveAgentDecisionClosureV1Error("STOP_ARM_MUST_ABSTAIN_WITH_ZERO_CARDS")
        authorization = {
            "schema_version": "live-agent-decision-closure-authorization/v1",
            "case_id": X_EISD_CASE_ID,
            "arm_id": arm_id,
            "status": "AUTHORIZED_ABSTENTION_ZERO_EXECUTION",
            "selected_card_ids": [],
            "authorized_action_count": 0,
            "authorization_basis": ["NO_CURRENT_LEGAL_ACTION_CARD_SELECTED"],
            "model_execution_authority": "NONE",
            "scientific_disposition": "NOT_EVALUATED",
        }
    else:
        raise LiveAgentDecisionClosureV1Error("ARM_ID_INVALID")
    return admission, authorization


def _source_grounding() -> dict[str, str]:
    overlay = load_json_object(REPO_ROOT / "registries" / "rules_v1" / "family_overlay_v1.json")
    return source_grounding_by_family(overlay)


def _positive_execution(state: Mapping[str, Any]) -> dict[str, Any]:
    before_graph = state["recorded_profile"]
    before_results = state["before_rule_results"]
    lookup_result = execute_exact_source_lookup(
        allowlist=state["allowlist"],
        request=state["lookup_request"],
        workspace_root=REPO_ROOT,
    )
    if lookup_result.get("status") != "FOUND" or lookup_result.get("route") != "SOURCE_LOOKUP":
        raise LiveAgentDecisionClosureV1Error("EXACT_LOOKUP_EXECUTION_FAILED")
    after_graph = apply_lookup_result(case_graph=before_graph, lookup_result=lookup_result)
    after_graph = derive_declaration_attestations(
        case_graph=after_graph, lookup_results=[lookup_result]
    )
    after_results = evaluate_xeisd_case(case_graph=after_graph, **state["rules_bundle"])
    before_target = _rule_by_id(before_results, TARGET_RULE_INSTANCE_ID)
    after_target = _rule_by_id(after_results, TARGET_RULE_INSTANCE_ID)
    if before_target.get("status") != "UNRESOLVED" or after_target.get("status") != "PASS":
        raise LiveAgentDecisionClosureV1Error("SAME_RULE_UNRESOLVED_TO_PASS_NOT_OBSERVED")
    transitions = _status_transitions(before_results, after_results)
    changed_ids = {item["rule_instance_id"] for item in transitions}
    if TARGET_RULE_INSTANCE_ID not in changed_ids or not changed_ids.issubset(_ALLOWED_DEPENDENT_TRANSITIONS):
        raise LiveAgentDecisionClosureV1Error("UNRELATED_RULEINSTANCE_CHANGED")
    evidence_result = {
        "schema_version": EVIDENCE_RESULT_SCHEMA,
        "evidence_result_id": "XEISD-RANDOM-COMPOSITION-LOOKUP-EVIDENCE::LIVE_AGENT_DECISION_CLOSURE_V1",
        "case_id": X_EISD_CASE_ID,
        "card_id": ACTION_CARD_ID,
        "evidence_result_class": "SOURCE_LOOKUP_RESULT",
        "route": "SOURCE_LOOKUP",
        "rule_effect": "ACTIVE_RULE_EFFECT",
        "affected_rule_instance_id": TARGET_RULE_INSTANCE_ID,
        "active_rule_effect": "ACTIVE_RULE_EFFECT",
        "active_rule_transition": {
            "before_status": "UNRESOLVED",
            "after_status": "PASS",
            "same_rule_identity": True,
        },
        "lookup_result": copy.deepcopy(lookup_result),
        "validation_status": "PASS_EXACT_ALLOWLIST_HASH_LOCATOR",
        "scientific_disposition": "NOT_EVALUATED",
        "claim_ceiling": "Exact exposed-development declaration attestation only; no source-science approval or scientific support.",
    }
    route_packet = materialize_xeisd_conclusion_packet(
        case_graph=after_graph,
        rule_results=after_results,
        lookup_results=[lookup_result],
        scenario_id=POSITIVE_ARM_ID,
    )
    conclusion = materialize_stage2_conclusion_packet(
        route_packet=route_packet,
        source_grounding=_source_grounding(),
        scenario_id=POSITIVE_ARM_ID,
        route_artifact_path=f"{POSITIVE_ARM_ID}/route_packet.json",
    )
    if conclusion.get("terminal_disposition") != "ABSTAIN_OR_HUMAN_REVIEW":
        raise LiveAgentDecisionClosureV1Error("POSITIVE_ARM_REDUCER_STATE_CHANGED")
    return {
        "execution_receipt": {
            "schema_version": "live-agent-decision-closure-execution/v1",
            "case_id": X_EISD_CASE_ID,
            "arm_id": POSITIVE_ARM_ID,
            "execution_status": "ONE_EXACT_LOOKUP_EXECUTED",
            "selected_card_ids": [ACTION_CARD_ID],
            "executed_action_count": 1,
            "operator_execution_count": 0,
            "network_accessed_by_scientific_action": False,
        },
        "lookup_result": lookup_result,
        "evidence_results": [evidence_result],
        "after_graph": after_graph,
        "after_rule_results": after_results,
        "rule_transition": {
            "affected_rule_instance_id": TARGET_RULE_INSTANCE_ID,
            "before_rule_result": before_target,
            "after_rule_result": after_target,
            "all_changed_rule_statuses": transitions,
            "allowed_dependent_rule_instance_ids": sorted(_ALLOWED_DEPENDENT_TRANSITIONS),
            "unrelated_rule_changes": [],
        },
        "route_packet": route_packet,
        "conclusion_packet": conclusion,
    }


def _stop_execution(state: Mapping[str, Any]) -> dict[str, Any]:
    before_results = state["before_rule_results"]
    target = _rule_by_id(before_results, TARGET_RULE_INSTANCE_ID)
    route_packet = materialize_xeisd_conclusion_packet(
        case_graph=state["recorded_profile"],
        rule_results=before_results,
        lookup_results=[],
        scenario_id=STOP_ARM_ID,
    )
    conclusion = materialize_stage2_conclusion_packet(
        route_packet=route_packet,
        source_grounding=_source_grounding(),
        scenario_id=STOP_ARM_ID,
        route_artifact_path=f"{STOP_ARM_ID}/route_packet.json",
    )
    if conclusion.get("terminal_disposition") != "ABSTAIN_OR_HUMAN_REVIEW":
        raise LiveAgentDecisionClosureV1Error("STOP_ARM_REDUCER_STATE_CHANGED")
    return {
        "execution_receipt": {
            "schema_version": "live-agent-decision-closure-execution/v1",
            "case_id": X_EISD_CASE_ID,
            "arm_id": STOP_ARM_ID,
            "execution_status": "ABSTAINED_ZERO_EXECUTION",
            "selected_card_ids": [],
            "executed_action_count": 0,
            "lookup_execution_count": 0,
            "operator_execution_count": 0,
            "network_accessed_by_scientific_action": False,
        },
        "lookup_result": None,
        "evidence_results": [],
        "after_graph": copy.deepcopy(state["recorded_profile"]),
        "after_rule_results": copy.deepcopy(before_results),
        "rule_transition": {
            "affected_rule_instance_id": TARGET_RULE_INSTANCE_ID,
            "before_rule_result": target,
            "after_rule_result": copy.deepcopy(target),
            "all_changed_rule_statuses": [],
            "unrelated_rule_changes": [],
        },
        "route_packet": route_packet,
        "conclusion_packet": conclusion,
        "stop_receipt": {
            "schema_version": "live-agent-decision-closure-stop-receipt/v1",
            "case_id": X_EISD_CASE_ID,
            "arm_id": STOP_ARM_ID,
            "legal_action_card_count": 0,
            "planner_decision": "ABSTAIN_NO_ACTION",
            "scientific_action_executions": 0,
            "lookup_executions": 0,
            "operator_executions": 0,
            "rule_status": "UNRESOLVED",
            "terminal_disposition": "ABSTAIN_OR_HUMAN_REVIEW",
        },
    }


def _persist_live_call(arm_root: Path, call: Mapping[str, Any]) -> list[str]:
    call_root = arm_root / "live_call"
    _write_json(call_root / "request_payload.json", call["request_payload"])
    raw = call.get("raw_response")
    if not isinstance(raw, str):
        raise LiveAgentDecisionClosureV1Error("SAFE_RAW_RESPONSE_REQUIRED")
    _write_text(call_root / "raw_response.txt", raw)
    _write_json(call_root / "model_call_receipt.json", call["receipt"])
    proposal = call.get("parsed_proposal")
    if isinstance(proposal, Mapping):
        _write_json(call_root / "parsed_proposal.json", proposal)
    return [
        "live_call/request_payload.json",
        "live_call/raw_response.txt",
        "live_call/model_call_receipt.json",
        "live_call/parsed_proposal.json",
    ]


def _file_record(root: Path, relative: str) -> dict[str, Any]:
    path = root / relative
    if not path.is_file():
        raise LiveAgentDecisionClosureV1Error(f"ARTIFACT_MISSING:{relative}")
    return {
        "path": relative,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "kind": "TEXT" if path.suffix == ".txt" else "JSON",
    }


def run_live_agent_decision_closure_campaign(
    *,
    output_dir: Path,
    client: OpenRouterProposalClient,
    config: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Run the planned positive and card-removed Planner calls exactly once each."""

    config = load_campaign_config() if config is None else validate_campaign_config(config)
    require_campaign_open(config)
    expected_budget = campaign_budget_ledger_path(config)
    if (
        client.budget.campaign_id != config.get("campaign_id")
        or client.budget.state_path != expected_budget
        or client.budget.cap_usd != Decimal(str(config["budget_usd"]))
        or client.budget.max_completed_calls != int(config["max_completed_calls"])
    ):
        raise LiveAgentDecisionClosureV1Error("CAMPAIGN_BUDGET_BINDING_MISMATCH")
    output_dir = _prepare_output_dir(output_dir)
    state = build_frozen_decision_state()
    base_state_hash = canonical_json_sha256(
        {
            "recorded_profile": state["recorded_profile"],
            "before_rule_results": state["before_rule_results"],
            "unresolved_items": state["unresolved_items"],
        }
    )
    root_artifacts: list[str] = []
    _write_json(output_dir / "campaign_config_snapshot.json", config)
    _write_json(output_dir / "recorded_profile.json", state["recorded_profile"])
    _write_json(output_dir / "before_rule_results.json", state["before_rule_results"])
    root_artifacts.extend(
        ["campaign_config_snapshot.json", "recorded_profile.json", "before_rule_results.json"]
    )

    arm_summaries: list[dict[str, Any]] = []
    all_artifacts = list(root_artifacts)
    for arm_id, include_card in (
        (POSITIVE_ARM_ID, True),
        (STOP_ARM_ID, False),
    ):
        arm_root = output_dir / arm_id
        planner_input = build_planner_input(state, include_action_card=include_card)
        _write_json(arm_root / "planner_visible_input.json", planner_input)
        call = _call_planner(client=client, config=config, planner_input=planner_input)
        relative_artifacts = ["planner_visible_input.json"]
        relative_artifacts.extend(_persist_live_call(arm_root, call))
        admission, authorization = _admit_and_authorize(
            arm_id=arm_id, planner_input=planner_input, call=call
        )
        execution = _positive_execution(state) if arm_id == POSITIVE_ARM_ID else _stop_execution(state)
        _write_json(arm_root / "planner_admission.json", admission)
        _write_json(arm_root / "planner_authorization.json", authorization)
        _write_json(arm_root / "execution_receipt.json", execution["execution_receipt"])
        _write_json(
            arm_root / "evidence_results.json",
            {
                "case_id": X_EISD_CASE_ID,
                "arm_id": arm_id,
                "evidence_results": execution["evidence_results"],
            },
        )
        _write_json(arm_root / "after_casegraph.json", execution["after_graph"])
        _write_json(arm_root / "after_rule_results.json", execution["after_rule_results"])
        _write_json(arm_root / "rule_transition.json", execution["rule_transition"])
        _write_json(arm_root / "route_packet.json", execution["route_packet"])
        _write_json(arm_root / "conclusion_packet.json", execution["conclusion_packet"])
        relative_artifacts.extend(
            [
                "planner_admission.json",
                "planner_authorization.json",
                "execution_receipt.json",
                "evidence_results.json",
                "after_casegraph.json",
                "after_rule_results.json",
                "rule_transition.json",
                "route_packet.json",
                "conclusion_packet.json",
            ]
        )
        if arm_id == STOP_ARM_ID:
            _write_json(arm_root / "stop_receipt.json", execution["stop_receipt"])
            relative_artifacts.append("stop_receipt.json")
        arm_receipt = {
            "schema_version": ARM_RECEIPT_SCHEMA,
            "campaign_id": config["campaign_id"],
            "case_id": X_EISD_CASE_ID,
            "arm_id": arm_id,
            "profile_mode": PROFILE_MODE,
            "base_state_sha256": base_state_hash,
            "legal_action_card_count": len(planner_input["legal_action_cards"]),
            "planner_decision": admission["decision"],
            "selected_card_ids": admission["selected_card_ids"],
            "authorization_status": authorization["status"],
            "executed_action_count": execution["execution_receipt"]["executed_action_count"],
            "affected_rule_instance_id": TARGET_RULE_INSTANCE_ID,
            "before_status": execution["rule_transition"]["before_rule_result"]["status"],
            "after_status": execution["rule_transition"]["after_rule_result"]["status"],
            "terminal_disposition": execution["conclusion_packet"]["terminal_disposition"],
            "model": call["receipt"]["requested_model"],
            "provider": call["receipt"]["actual_provider"],
            "response_id": call["receipt"]["response_id"],
            "reported_cost_usd": call["receipt"]["reported_cost_usd"],
            "result_status": "SUCCEEDED",
        }
        _write_json(arm_root / "arm_receipt.json", arm_receipt)
        relative_artifacts.append("arm_receipt.json")
        arm_summaries.append(arm_receipt)
        all_artifacts.extend(f"{arm_id}/{path}" for path in relative_artifacts)

    budget = client.budget.snapshot()
    if budget["completed_calls"] != 2:
        raise LiveAgentDecisionClosureV1Error("EXPECTED_EXACTLY_TWO_COMPLETED_CALLS")
    matrix = {
        "schema_version": "live-agent-decision-closure-paired-matrix/v1",
        "campaign_id": config["campaign_id"],
        "case_id": X_EISD_CASE_ID,
        "agent_mode": PROFILE_MODE,
        "arms": arm_summaries,
        "paired_counterfactual_status": "PASS",
        "claim_ceiling": config["claim_ceiling"],
    }
    _write_json(output_dir / "paired_arm_matrix.json", matrix)
    all_artifacts.append("paired_arm_matrix.json")
    artifact_records = [_file_record(output_dir, relative) for relative in sorted(all_artifacts)]
    manifest = {
        "schema_version": MANIFEST_SCHEMA,
        "campaign_id": config["campaign_id"],
        "campaign_state": "COMPLETED_CALLS_FROZEN",
        "case_id": X_EISD_CASE_ID,
        "profile_mode": PROFILE_MODE,
        "planner_mode": PLANNER_MODE,
        "transport": TRANSPORT,
        "base_state_sha256": base_state_hash,
        "positive_arm_id": POSITIVE_ARM_ID,
        "stop_arm_id": STOP_ARM_ID,
        "affected_rule_instance_id": TARGET_RULE_INSTANCE_ID,
        "positive_transition": "UNRESOLVED_TO_PASS",
        "positive_terminal_disposition": "ABSTAIN_OR_HUMAN_REVIEW",
        "stop_transition": "UNRESOLVED_TO_UNRESOLVED",
        "stop_terminal_disposition": "ABSTAIN_OR_HUMAN_REVIEW",
        "completed_api_calls": budget["completed_calls"],
        "http_attempts": _attempt_count(client.budget),
        "actual_cost_usd": budget["actual_cost_usd"],
        "budget": budget,
        "artifacts": artifact_records,
        "source_science_review_status": config["source_science_review_status"],
        "held_out_status": config["held_out_status"],
        "claim_ceiling": config["claim_ceiling"],
        "scientific_support_status": SCIENTIFIC_SUPPORT_STATUS,
        "result_status": RESULT_STATUS,
        "boundary": CAMPAIGN_BOUNDARY,
    }
    _write_json(output_dir / "live_agent_decision_closure_manifest_v1.json", manifest)
    return {
        "manifest": manifest,
        "matrix": matrix,
        "output_dir": str(output_dir),
    }


__all__ = [
    "ACTION_CARD_ID",
    "CAMPAIGN_CONFIG_PATH",
    "CAMPAIGN_BOUNDARY",
    "CAMPAIGN_CLOSED_ERROR",
    "CAMPAIGN_CLOSED_STATUS",
    "CAMPAIGN_OPEN_STATUS",
    "CLAIM_CEILING",
    "HELD_OUT_STATUS",
    "LiveAgentDecisionClosureV1Error",
    "PLANNER_MODE",
    "POSITIVE_ARM_ID",
    "PROFILE_MODE",
    "RESULT_STATUS",
    "SCIENTIFIC_SUPPORT_STATUS",
    "SOURCE_SCIENCE_REVIEW_STATUS",
    "STOP_ARM_ID",
    "TARGET_RULE_INSTANCE_ID",
    "TRANSPORT",
    "build_budget",
    "build_frozen_decision_state",
    "build_planner_input",
    "campaign_budget_ledger_path",
    "load_campaign_config",
    "require_campaign_open",
    "run_live_agent_decision_closure_campaign",
    "validate_campaign_completion_receipt",
    "validate_planner_proposal",
    "validate_campaign_config",
]
