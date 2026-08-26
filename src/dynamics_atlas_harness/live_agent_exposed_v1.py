"""Bounded two-case Live-Agent evaluation for the exposed development baseline.

This module intentionally does not introduce an Agent framework.  It sends one
tool-less JSON request at a time to a local model, validates a proposal against a
small task contract, then hands any route proposal back to the already frozen,
deterministic X-EISD/HSP90 authorization boundaries.  It never executes an action.
"""

from __future__ import annotations

import hashlib
import json
import time
import urllib.error
import urllib.request
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

from .contracts import find_forbidden_answer_paths
from .providers import ProfileProvider, ProposalProvider
from .real_case_vertical_slice_v1 import (
    HSP90_CASE_ID,
    HSP90_OPERATOR_ID,
    evaluate_hsp90_time_anatomy_f04r02,
    load_hsp90_case_bundle,
    resolve_hsp90_time_anatomy_obligation,
)
from .registered_operators import load_registered_operator_registry


PROFILER_PROPOSAL_SCHEMA = "agent-profiler-proposal/v1"
PLANNER_PROPOSAL_SCHEMA = "agent-planner-proposal/v1"
PROFILER_ROLE = "PROFILER"
PLANNER_ROLE = "PLANNER"
MODEL_VISIBLE_PACKET_SCHEMA_PREFIX = "agent-model-visible-"
PLANNER_ACTIONS = frozenset(
    {
        "DIRECT_EVALUATION",
        "EXACT_ATTESTATION",
        "REGISTERED_OPERATOR",
        "HUMAN_OR_NEW_DATA",
    }
)
_PROFILER_FORBIDDEN_TEXT = (
    "REGISTERED_OPERATOR",
    "EXACT_ATTESTATION",
    "DIRECT_EVALUATION",
    "HUMAN_OR_NEW_DATA",
    "ROSTER_PASS",
    "SUPPORT_WITHIN_CEILING",
    "CANNOT_SUPPORT_REQUESTED_CLAIM",
    "RULE_CONTRACT_PASS",
    "hsp90.directional_time_anatomy.v1_case_bound",
)
_PLANNER_FORBIDDEN_KEYS = frozenset(
    {"execute", "execute_now", "tool_call", "operator_inputs", "operator_output"}
)


class LiveAgentExposedError(ValueError):
    """Raised when the small exposed-case contract is violated."""


class LocalModelCallError(RuntimeError):
    """Raised after a local model request has already produced a receipt."""


def _json_object(value: Any, label: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise LiveAgentExposedError(f"{label} must be a JSON object")
    return value


def _canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_json(value: Any) -> str:
    return hashlib.sha256(_canonical_json(value).encode("utf-8")).hexdigest()


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def load_json_object(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise LiveAgentExposedError(f"cannot read JSON object {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise LiveAgentExposedError(f"expected JSON object: {path}")
    return value


def _string_values(value: Any) -> list[str]:
    if isinstance(value, Mapping):
        values: list[str] = []
        for item in value.values():
            values.extend(_string_values(item))
        return values
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        values = []
        for item in value:
            values.extend(_string_values(item))
        return values
    return [value] if isinstance(value, str) else []


def _text_reason_codes(value: Any, forbidden: Sequence[str]) -> list[str]:
    upper_text = "\n".join(_string_values(value)).upper()
    return [f"FORBIDDEN_TEXT:{token}" for token in forbidden if token.upper() in upper_text]


def _forbidden_key_paths(
    value: Any, forbidden_keys: frozenset[str], path: str = "$"
) -> list[str]:
    """Return every recursively nested prohibited key path."""

    paths: list[str] = []
    if isinstance(value, Mapping):
        for key, item in value.items():
            key_text = str(key)
            child_path = f"{path}.{key_text}"
            if key_text.casefold() in forbidden_keys:
                paths.append(child_path)
            paths.extend(_forbidden_key_paths(item, forbidden_keys, child_path))
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        for index, item in enumerate(value):
            paths.extend(_forbidden_key_paths(item, forbidden_keys, f"{path}[{index}]"))
    return paths


def _validate_ollama_endpoint(endpoint: str) -> None:
    """Allow only the exact local Ollama JSON endpoint used by this slice."""

    try:
        parsed = urlsplit(endpoint)
        port = parsed.port
    except ValueError as exc:
        raise LiveAgentExposedError("invalid local Ollama endpoint") from exc
    if (
        parsed.scheme != "http"
        or parsed.hostname != "127.0.0.1"
        or port != 11434
        or parsed.path != "/api/generate"
        or parsed.username is not None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment
    ):
        raise LiveAgentExposedError(
            "only http://127.0.0.1:11434/api/generate is permitted"
        )


def _status_receipt(
    *,
    schema_version: str,
    case_id: str | None,
    status: str,
    reason_codes: Sequence[str],
    **extra: Any,
) -> dict[str, Any]:
    return {
        "schema_version": schema_version,
        "case_id": case_id,
        "status": status,
        "reason_codes": list(reason_codes),
        **extra,
    }


def model_visible_workspace_report(workspaces_root: Path) -> dict[str, Any]:
    """Prove that model-visible files exclude gold, test, output, and registry cues."""

    forbidden_name_fragments = (
        "sealed",
        "gold",
        "expected",
        "conclusion",
        "output",
        "test",
        "registry",
    )
    forbidden_contents = (
        "SUPPORT_WITHIN_CEILING",
        "CANNOT_SUPPORT_REQUESTED_CLAIM",
        "RULE_CONTRACT_PASS",
        "RELATION_REVIEWABLE",
    )
    reason_codes: list[str] = []
    files: list[str] = []
    if not workspaces_root.is_dir():
        return _status_receipt(
            schema_version="model-visible-workspace-report/v1",
            case_id=None,
            status="FAIL",
            reason_codes=["MODEL_VISIBLE_WORKSPACES_MISSING"],
            files=files,
        )
    for path in sorted(workspaces_root.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(workspaces_root).as_posix()
        files.append(relative)
        if any(fragment in relative.casefold() for fragment in forbidden_name_fragments):
            reason_codes.append(f"FORBIDDEN_MODEL_VISIBLE_FILENAME:{relative}")
        try:
            contents = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            reason_codes.append(f"NON_TEXT_MODEL_VISIBLE_FILE:{relative}")
            continue
        for token in forbidden_contents:
            if token in contents:
                reason_codes.append(f"FORBIDDEN_MODEL_VISIBLE_CONTENT:{relative}:{token}")
    return _status_receipt(
        schema_version="model-visible-workspace-report/v1",
        case_id=None,
        status="PASS" if not reason_codes else "FAIL",
        reason_codes=reason_codes,
        files=files,
        filesystem_access="NOT_EXPOSED_TO_MODEL_TRANSPORT",
    )


def _packet_case_id(packet: Mapping[str, Any]) -> str | None:
    case_id = packet.get("case_id")
    return case_id if isinstance(case_id, str) and case_id else None


def validate_model_visible_packet(packet: Mapping[str, Any], role: str) -> dict[str, Any]:
    """Validate one packet before it is sent to the local, tool-less transport."""

    packet = _json_object(packet, "model-visible packet")
    case_id = _packet_case_id(packet)
    reasons: list[str] = []
    schema_version = packet.get("schema_version")
    if not isinstance(schema_version, str) or not schema_version.startswith(
        MODEL_VISIBLE_PACKET_SCHEMA_PREFIX
    ):
        reasons.append("INVALID_MODEL_VISIBLE_PACKET_SCHEMA")
    if packet.get("visibility") != "MODEL_VISIBLE_ONLY":
        reasons.append("INVALID_MODEL_VISIBLE_VISIBILITY")
    if case_id is None:
        reasons.append("MISSING_CASE_ID")
    reasons.extend(f"ANSWER_BEARING_KEY:{path}" for path in find_forbidden_answer_paths(packet))
    if role == PROFILER_ROLE:
        reasons.extend(_text_reason_codes(packet, _PROFILER_FORBIDDEN_TEXT))
        if not isinstance(packet.get("source_material"), list):
            reasons.append("MISSING_SOURCE_MATERIAL")
        if not isinstance(packet.get("output_contract"), Mapping):
            reasons.append("MISSING_PROFILER_OUTPUT_CONTRACT")
    elif role == PLANNER_ROLE:
        if not isinstance(packet.get("selected_rule_instances"), list):
            reasons.append("MISSING_SELECTED_RULE_INSTANCES")
        if not isinstance(packet.get("permitted_action_cards"), list):
            reasons.append("MISSING_PERMITTED_ACTION_CARDS")
    else:
        reasons.append("UNKNOWN_AGENT_ROLE")
    return _status_receipt(
        schema_version="model-visible-packet-validation/v1",
        case_id=case_id,
        status="PASS" if not reasons else "FAIL",
        reason_codes=reasons,
        role=role,
        packet_sha256=sha256_json(packet),
    )


class LocalOllamaJsonProvider(ProfileProvider, ProposalProvider):
    """One local JSON-only provider for the two exposed roles.

    The class deliberately accepts already-loaded prompts and packet mappings.  The
    transport sends no filesystem paths, tools, registry handles, or credentials.
    """

    def __init__(
        self,
        *,
        model: str,
        endpoint: str,
        profiler_prompt: str,
        planner_prompt: str,
        timeout_seconds: int = 90,
        allow_one_json_repair: bool = True,
    ) -> None:
        if not model.strip():
            raise LiveAgentExposedError("local model name must be nonempty")
        _validate_ollama_endpoint(endpoint)
        self.provider_id = f"ollama-local-json:{model}"
        self.model = model
        self.endpoint = endpoint
        self._prompts = {PROFILER_ROLE: profiler_prompt, PLANNER_ROLE: planner_prompt}
        self.timeout_seconds = timeout_seconds
        self.allow_one_json_repair = allow_one_json_repair
        self.last_receipt: dict[str, Any] | None = None
        self.last_raw_response: str | None = None

    @staticmethod
    def transport_payload(*, model: str, prompt: str) -> dict[str, Any]:
        """Return the exact tool-less local-transport request body."""

        return {
            "model": model,
            "prompt": prompt,
            "format": "json",
            "stream": False,
            "options": {"temperature": 0, "num_predict": 1200},
        }

    def _post(self, prompt: str) -> str:
        payload = self.transport_payload(model=self.model, prompt=prompt)
        request = urllib.request.Request(
            self.endpoint,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(request, timeout=self.timeout_seconds) as response:
            body = json.loads(response.read().decode("utf-8"))
        raw = body.get("response") if isinstance(body, Mapping) else None
        if not isinstance(raw, str):
            raise LocalModelCallError("LOCAL_MODEL_RESPONSE_MISSING_TEXT")
        return raw

    @staticmethod
    def _parse_object(raw: str) -> dict[str, Any] | None:
        try:
            value = json.loads(raw.strip())
        except json.JSONDecodeError:
            return None
        return value if isinstance(value, dict) else None

    def _propose(self, role: str, packet: Mapping[str, Any]) -> dict[str, Any]:
        packet_validation = validate_model_visible_packet(packet, role)
        if packet_validation["status"] != "PASS":
            self.last_receipt = _status_receipt(
                schema_version="local-model-call-receipt/v1",
                case_id=_packet_case_id(packet),
                status="BLOCKED",
                reason_codes=packet_validation["reason_codes"],
                role=role,
                provider_id=self.provider_id,
                model=self.model,
                tool_calls=0,
            )
            self.last_raw_response = None
            raise LocalModelCallError("MODEL_VISIBLE_PACKET_REJECTED")

        prompt = self._prompts[role] + "\n\nTask packet:\n" + _canonical_json(packet)
        raw_responses: list[str] = []
        started = time.perf_counter()
        error_code: str | None = None
        try:
            raw_responses.append(self._post(prompt))
        except (OSError, urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError, LocalModelCallError) as exc:
            error_code = f"LOCAL_MODEL_TRANSPORT_ERROR:{type(exc).__name__}"
        proposal = self._parse_object(raw_responses[-1]) if raw_responses else None
        repaired = False
        if proposal is None and error_code is None and self.allow_one_json_repair:
            repaired = True
            repair_prompt = (
                "Your preceding response was not one JSON object. Return exactly one JSON object "
                "that follows the supplied output contract. Do not add prose, markdown, tools, "
                "or new facts.\n\nTask packet:\n" + _canonical_json(packet)
            )
            try:
                raw_responses.append(self._post(repair_prompt))
            except (OSError, urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError, LocalModelCallError) as exc:
                error_code = f"LOCAL_MODEL_REPAIR_TRANSPORT_ERROR:{type(exc).__name__}"
            proposal = self._parse_object(raw_responses[-1]) if raw_responses else None
        elapsed_ms = round((time.perf_counter() - started) * 1000, 3)
        self.last_raw_response = raw_responses[-1] if raw_responses else None
        reason_codes: list[str] = []
        if error_code is not None:
            reason_codes.append(error_code)
        if proposal is None and error_code is None:
            reason_codes.append("LOCAL_MODEL_INVALID_JSON_AFTER_BOUNDED_REPAIR")
        self.last_receipt = _status_receipt(
            schema_version="local-model-call-receipt/v1",
            case_id=_packet_case_id(packet),
            status="SUCCEEDED" if proposal is not None else "FAILED",
            reason_codes=reason_codes,
            role=role,
            provider_id=self.provider_id,
            model=self.model,
            transport="LOCAL_LOOPBACK_HTTP_JSON_NO_TOOLS",
            prompt_sha256=sha256_text(prompt),
            input_sha256=sha256_json(packet),
            response_sha256=sha256_text(self.last_raw_response) if self.last_raw_response else None,
            latency_ms=elapsed_ms,
            call_count=len(raw_responses),
            bounded_json_repair_attempted=repaired,
            tool_calls=0,
            cost_usd=None,
            cost_status="LOCAL_UNMETERED_NOT_ESTIMATED",
        )
        if proposal is None:
            raise LocalModelCallError(reason_codes[0] if reason_codes else "LOCAL_MODEL_FAILED")
        return proposal

    def propose_profile(self, request_view: Mapping[str, Any]) -> dict[str, Any]:
        return self._propose(PROFILER_ROLE, request_view)

    def propose(self, bounded_view: Mapping[str, Any]) -> dict[str, Any]:
        return self._propose(PLANNER_ROLE, bounded_view)


def _source_index(proposal: Mapping[str, Any]) -> dict[str, Mapping[str, Any]]:
    sources = proposal.get("sources")
    if not isinstance(sources, list):
        return {}
    result: dict[str, Mapping[str, Any]] = {}
    for source in sources:
        if isinstance(source, Mapping) and isinstance(source.get("source_id"), str):
            result[source["source_id"]] = source
    return result


def _edge_index(proposal: Mapping[str, Any]) -> dict[str, Mapping[str, Any]]:
    edges = proposal.get("edges")
    if not isinstance(edges, list):
        return {}
    result: dict[str, Mapping[str, Any]] = {}
    for edge in edges:
        if isinstance(edge, Mapping) and isinstance(edge.get("edge_id"), str):
            result[edge["edge_id"]] = edge
    return result


def _packet_source_ids(packet: Mapping[str, Any]) -> set[str]:
    material = packet.get("source_material")
    if not isinstance(material, list):
        return set()
    return {
        item["source_id"]
        for item in material
        if isinstance(item, Mapping) and isinstance(item.get("source_id"), str)
    }


def _packet_edge_ids(packet: Mapping[str, Any]) -> set[str]:
    material = packet.get("edge_material")
    if not isinstance(material, list):
        return set()
    return {
        item["edge_id"]
        for item in material
        if isinstance(item, Mapping) and isinstance(item.get("edge_id"), str)
    }


def validate_profiler_projection(
    proposal: Mapping[str, Any], packet: Mapping[str, Any]
) -> dict[str, Any]:
    """Typed validation without accessing Rules, routes, Operators, or gold data."""

    packet = _json_object(packet, "profiler packet")
    case_id = _packet_case_id(packet)
    reasons: list[str] = []
    if not isinstance(proposal, Mapping):
        return _status_receipt(
            schema_version="profiler-proposal-validation/v1",
            case_id=case_id,
            status="FAIL",
            reason_codes=["PROPOSAL_NOT_OBJECT"],
        )
    if proposal.get("schema_version") != PROFILER_PROPOSAL_SCHEMA:
        reasons.append("INVALID_PROFILER_PROPOSAL_SCHEMA")
    if proposal.get("case_id") != case_id:
        reasons.append("CASE_ID_MISMATCH")
    reasons.extend(f"ANSWER_BEARING_KEY:{path}" for path in find_forbidden_answer_paths(proposal))
    reasons.extend(_text_reason_codes(proposal, _PROFILER_FORBIDDEN_TEXT))
    contract = packet.get("output_contract")
    contract = contract if isinstance(contract, Mapping) else {}
    required_top_level = contract.get("required_top_level_fields", [])
    for field in required_top_level:
        if field not in proposal:
            reasons.append(f"MISSING_TOP_LEVEL_FIELD:{field}")
    source_ids = _packet_source_ids(packet)
    sources = _source_index(proposal)
    if set(sources) != source_ids:
        reasons.append("SOURCE_ID_SET_MISMATCH")
    vocab = packet.get("controlled_vocabulary")
    vocab = vocab if isinstance(vocab, Mapping) else {}
    required_source_fields = contract.get("required_source_fields", [])
    packet_sources = {
        item.get("source_id"): item
        for item in packet.get("source_material", [])
        if isinstance(item, Mapping)
    }
    for source_id, source in sources.items():
        for field in required_source_fields:
            if field not in source:
                reasons.append(f"MISSING_SOURCE_FIELD:{source_id}:{field}")
        for field in (
            "method_or_modality",
            "evidence_role",
            "native_observable_kind",
            "estimand_kind",
            "time_semantics",
        ):
            allowed = vocab.get(field)
            if isinstance(allowed, list) and source.get(field) not in allowed:
                reasons.append(f"OUT_OF_VOCABULARY:{source_id}:{field}")
        allowed_locator = packet_sources.get(source_id, {}).get("source_locator")
        if source.get("source_locator") != allowed_locator:
            reasons.append(f"INVALID_EVIDENCE_POINTER:{source_id}")
        if source.get("sample_system_composition") != "UNKNOWN":
            reasons.append(f"MISSING_OR_FABRICATED_UNKNOWN:{source_id}:sample_system_composition")
    edge_ids = _packet_edge_ids(packet)
    edges = _edge_index(proposal)
    if set(edges) != edge_ids:
        reasons.append("EDGE_ID_SET_MISMATCH")
    packet_edges = {
        item.get("edge_id"): item
        for item in packet.get("edge_material", [])
        if isinstance(item, Mapping)
    }
    required_edge_fields = contract.get("required_edge_fields", [])
    for edge_id, edge in edges.items():
        for field in required_edge_fields:
            if field not in edge:
                reasons.append(f"MISSING_EDGE_FIELD:{edge_id}:{field}")
        packet_edge = packet_edges.get(edge_id, {})
        for endpoint in ("left_source_id", "right_source_id"):
            if edge.get(endpoint) != packet_edge.get(endpoint):
                reasons.append(f"INVALID_EDGE_ENDPOINT:{edge_id}:{endpoint}")
        if edge.get("condition_relation") != "UNKNOWN":
            reasons.append(f"MISSING_OR_FABRICATED_UNKNOWN:{edge_id}:condition_relation")
    unknowns = proposal.get("unknowns")
    if not isinstance(unknowns, list):
        reasons.append("INVALID_UNKNOWNS")
    else:
        for index, item in enumerate(unknowns):
            if not isinstance(item, Mapping):
                reasons.append(f"UNKNOWN_NOT_OBJECT:{index}")
                continue
            for field in contract.get("unknown_item_fields", []):
                if not isinstance(item.get(field), str) or not item[field].strip():
                    reasons.append(f"MISSING_UNKNOWN_FIELD:{index}:{field}")
    return _status_receipt(
        schema_version="profiler-proposal-validation/v1",
        case_id=case_id,
        status="PASS" if not reasons else "FAIL",
        reason_codes=reasons,
        source_count=len(sources),
        edge_count=len(edges),
    )


def compare_profiler_projection(
    proposal: Mapping[str, Any], sealed_reference: Mapping[str, Any]
) -> dict[str, Any]:
    """Compare critical facts and required UNKNOWNs to a sealed human reference."""

    proposal = _json_object(proposal, "profiler proposal")
    sealed_reference = _json_object(sealed_reference, "sealed profiler reference")
    case_id = proposal.get("case_id") if isinstance(proposal.get("case_id"), str) else None
    cases = sealed_reference.get("cases")
    reference = cases.get(case_id) if isinstance(cases, Mapping) and case_id else None
    if not isinstance(reference, Mapping):
        return _status_receipt(
            schema_version="profiler-reference-comparison/v1",
            case_id=case_id,
            status="FAIL",
            reason_codes=["SEALED_REFERENCE_CASE_MISSING"],
            critical_differences=[],
        )
    differences: list[dict[str, Any]] = []
    source_index = _source_index(proposal)
    for source_reference in reference.get("critical_sources", []):
        if not isinstance(source_reference, Mapping):
            continue
        source_id = source_reference.get("source_id")
        actual = source_index.get(source_id) if isinstance(source_id, str) else None
        if actual is None:
            differences.append({"kind": "CRITICAL_SOURCE_MISSING", "source_id": source_id})
            continue
        for field, expected in source_reference.items():
            if actual.get(field) != expected:
                differences.append(
                    {
                        "kind": "CRITICAL_SOURCE_FACT_MISMATCH",
                        "source_id": source_id,
                        "field": field,
                        "expected": expected,
                        "observed": actual.get(field),
                    }
                )
    edge_index = _edge_index(proposal)
    for edge_reference in reference.get("critical_edges", []):
        if not isinstance(edge_reference, Mapping):
            continue
        edge_id = edge_reference.get("edge_id")
        actual = edge_index.get(edge_id) if isinstance(edge_id, str) else None
        if actual is None:
            differences.append({"kind": "CRITICAL_EDGE_MISSING", "edge_id": edge_id})
            continue
        for field, expected in edge_reference.items():
            if actual.get(field) != expected:
                differences.append(
                    {
                        "kind": "CRITICAL_EDGE_FACT_MISMATCH",
                        "edge_id": edge_id,
                        "field": field,
                        "expected": expected,
                        "observed": actual.get(field),
                    }
                )
    unknown_paths = {
        item.get("path")
        for item in proposal.get("unknowns", [])
        if isinstance(item, Mapping) and isinstance(item.get("path"), str)
    }
    for path in reference.get("required_unknown_paths", []):
        if path not in unknown_paths:
            differences.append({"kind": "REQUIRED_UNKNOWN_MISSING", "path": path})
    return _status_receipt(
        schema_version="profiler-reference-comparison/v1",
        case_id=case_id,
        status="PASS" if not differences else "FAIL",
        reason_codes=[] if not differences else [item["kind"] for item in differences],
        critical_differences=differences,
    )


def evaluate_profiler_proposal(
    proposal: Mapping[str, Any], packet: Mapping[str, Any], sealed_reference: Mapping[str, Any]
) -> dict[str, Any]:
    """Return free-form, vocabulary-assisted, and full-harness views of one proposal."""

    proposal_mapping = proposal if isinstance(proposal, Mapping) else {}
    free_form_reasons = [
        f"ANSWER_BEARING_KEY:{path}" for path in find_forbidden_answer_paths(proposal_mapping)
    ]
    if not isinstance(proposal, Mapping):
        free_form_reasons.append("PROPOSAL_NOT_OBJECT")
    typed = validate_profiler_projection(proposal_mapping, packet)
    comparison = compare_profiler_projection(proposal_mapping, sealed_reference)
    full_pass = typed["status"] == "PASS" and comparison["status"] == "PASS"
    return {
        "schema_version": "profiler-evaluation/v1",
        "case_id": _packet_case_id(packet),
        "free_form": _status_receipt(
            schema_version="free-form-view/v1",
            case_id=_packet_case_id(packet),
            status="PASS" if not free_form_reasons else "FAIL",
            reason_codes=free_form_reasons,
        ),
        "vocabulary_assisted": typed,
        "bounded_harness": _status_receipt(
            schema_version="bounded-profiler-harness-view/v1",
            case_id=_packet_case_id(packet),
            status="PASS" if full_pass else "FAIL",
            reason_codes=[]
            if full_pass
            else ["TYPED_VALIDATION_OR_SEALED_COMPARISON_FAILED"],
            comparison=comparison,
        ),
        "comparison_sampling_boundary": "The three views evaluate the same recorded model proposal; they are not independent model samples.",
    }


def _planner_cards(packet: Mapping[str, Any]) -> dict[str, Mapping[str, Any]]:
    cards = packet.get("permitted_action_cards")
    if not isinstance(cards, list):
        return {}
    return {
        card["card_id"]: card
        for card in cards
        if isinstance(card, Mapping) and isinstance(card.get("card_id"), str)
    }


def validate_planner_proposal(
    proposal: Mapping[str, Any], packet: Mapping[str, Any]
) -> dict[str, Any]:
    """Validate a route proposal without invoking an attestation or Operator."""

    packet = _json_object(packet, "planner packet")
    case_id = _packet_case_id(packet)
    reasons: list[str] = []
    if not isinstance(proposal, Mapping):
        return _status_receipt(
            schema_version="planner-proposal-validation/v1",
            case_id=case_id,
            status="FAIL",
            reason_codes=["PROPOSAL_NOT_OBJECT"],
        )
    if proposal.get("schema_version") != PLANNER_PROPOSAL_SCHEMA:
        reasons.append("INVALID_PLANNER_PROPOSAL_SCHEMA")
    if proposal.get("case_id") != case_id:
        reasons.append("CASE_ID_MISMATCH")
    reasons.extend(f"ANSWER_BEARING_KEY:{path}" for path in find_forbidden_answer_paths(proposal))
    reasons.extend(
        f"FORBIDDEN_PLANNER_KEY:{path}"
        for path in _forbidden_key_paths(proposal, _PLANNER_FORBIDDEN_KEYS)
    )
    if proposal.get("execution_requested") is not False:
        reasons.append("EXECUTION_REQUESTED_OR_UNDECLARED")
    if proposal.get("scientific_disposition") != "NOT_EVALUATED":
        reasons.append("UNSAFE_SCIENTIFIC_DISPOSITION")
    if proposal.get("claim_ceiling_acknowledgement") != "NO_SCIENTIFIC_DISPOSITION":
        reasons.append("MISSING_CLAIM_CEILING_ACKNOWLEDGEMENT")
    cards = _planner_cards(packet)
    actions = proposal.get("proposed_actions")
    if not isinstance(actions, list) or not actions:
        reasons.append("MISSING_PROPOSED_ACTIONS")
        actions = []
    seen_cards: set[str] = set()
    for index, action in enumerate(actions):
        if not isinstance(action, Mapping):
            reasons.append(f"ACTION_NOT_OBJECT:{index}")
            continue
        card_id = action.get("card_id")
        card = cards.get(card_id) if isinstance(card_id, str) else None
        if card is None:
            reasons.append(f"ACTION_CARD_NOT_PERMITTED:{index}")
            continue
        seen_cards.add(card_id)
        if action.get("action") not in PLANNER_ACTIONS:
            reasons.append(f"ACTION_NOT_IN_ROUTE_VOCABULARY:{index}")
        for field in ("action", "target_rule_instance_id"):
            if action.get(field) != card.get(field):
                reasons.append(f"ACTION_DOES_NOT_MATCH_CARD:{index}:{field}")
        if "operator_id" in card and action.get("operator_id") != card.get("operator_id"):
            reasons.append(f"UNREGISTERED_OR_WRONG_OPERATOR:{index}")
        if "operator_id" not in card and action.get("operator_id") is not None:
            reasons.append(f"OPERATOR_NOT_PERMITTED_FOR_CARD:{index}")
        if not isinstance(action.get("rationale"), str) or not action["rationale"].strip():
            reasons.append(f"MISSING_ACTION_RATIONALE:{index}")
    return _status_receipt(
        schema_version="planner-proposal-validation/v1",
        case_id=case_id,
        status="PASS" if not reasons else "FAIL",
        reason_codes=reasons,
        proposed_card_ids=sorted(seen_cards),
        execution_performed=False,
    )


def compare_planner_proposal(
    proposal: Mapping[str, Any], sealed_reference: Mapping[str, Any]
) -> dict[str, Any]:
    proposal = _json_object(proposal, "planner proposal")
    sealed_reference = _json_object(sealed_reference, "sealed planner reference")
    case_id = proposal.get("case_id") if isinstance(proposal.get("case_id"), str) else None
    cases = sealed_reference.get("cases")
    reference = cases.get(case_id) if isinstance(cases, Mapping) and case_id else None
    if not isinstance(reference, Mapping):
        return _status_receipt(
            schema_version="planner-reference-comparison/v1",
            case_id=case_id,
            status="FAIL",
            reason_codes=["SEALED_REFERENCE_CASE_MISSING"],
            differences=[],
        )
    actions = proposal.get("proposed_actions")
    actions = actions if isinstance(actions, list) else []
    action_cards = {
        action.get("card_id")
        for action in actions
        if isinstance(action, Mapping) and isinstance(action.get("card_id"), str)
    }
    required_cards = set(reference.get("required_cards", []))
    differences: list[dict[str, Any]] = []
    if action_cards != required_cards:
        differences.append(
            {
                "kind": "ACTION_CARD_SET_MISMATCH",
                "required_cards": sorted(required_cards),
                "observed_cards": sorted(action_cards),
            }
        )
    for field in ("scientific_disposition", "execution_requested"):
        if proposal.get(field) != reference.get(field):
            differences.append(
                {
                    "kind": "PLANNER_SAFETY_FIELD_MISMATCH",
                    "field": field,
                    "expected": reference.get(field),
                    "observed": proposal.get(field),
                }
            )
    return _status_receipt(
        schema_version="planner-reference-comparison/v1",
        case_id=case_id,
        status="PASS" if not differences else "FAIL",
        reason_codes=[] if not differences else [item["kind"] for item in differences],
        differences=differences,
    )


def authorize_planner_proposal(
    proposal: Mapping[str, Any], packet: Mapping[str, Any], repo_root: Path
) -> dict[str, Any]:
    """Use frozen authorization checks only; never execute a proposed action."""

    typed = validate_planner_proposal(proposal, packet)
    case_id = _packet_case_id(packet)
    if typed["status"] != "PASS":
        return _status_receipt(
            schema_version="planner-deterministic-authorization/v1",
            case_id=case_id,
            status="REJECTED",
            reason_codes=typed["reason_codes"],
            execution_performed=False,
            registered_operator_calls=0,
        )
    cards = _planner_cards(packet)
    actions = proposal.get("proposed_actions", [])
    if case_id != HSP90_CASE_ID:
        return _status_receipt(
            schema_version="planner-deterministic-authorization/v1",
            case_id=case_id,
            status="AUTHORIZED_NO_EXECUTION",
            reason_codes=[],
            authorized_actions=[
                {
                    "card_id": action["card_id"],
                    "action": action["action"],
                    "authorization_kind": "EXACT_ALLOWLISTED_ATTESTATION_ONLY",
                }
                for action in actions
                if isinstance(action, Mapping)
            ],
            execution_performed=False,
            registered_operator_calls=0,
        )
    if len(actions) != 1 or not isinstance(actions[0], Mapping):
        return _status_receipt(
            schema_version="planner-deterministic-authorization/v1",
            case_id=case_id,
            status="REJECTED",
            reason_codes=["HSP90_REQUIRES_ONE_EXACT_ACTION"],
            execution_performed=False,
            registered_operator_calls=0,
        )
    action = actions[0]
    card = cards.get(action.get("card_id"))
    if not isinstance(card, Mapping) or card.get("operator_id") != HSP90_OPERATOR_ID:
        return _status_receipt(
            schema_version="planner-deterministic-authorization/v1",
            case_id=case_id,
            status="REJECTED",
            reason_codes=["HSP90_EXACT_OPERATOR_CARD_MISSING"],
            execution_performed=False,
            registered_operator_calls=0,
        )
    evidence_root = repo_root / "evidence" / "real_case_vertical_slice_v1"
    bundle = load_hsp90_case_bundle(evidence_root)
    registry = load_registered_operator_registry(repo_root / "config" / "registered_operators.json")
    fresh_rule = evaluate_hsp90_time_anatomy_f04r02(
        case_graph=bundle["case_graph"],
        rule_overlay=bundle["rule_overlay"],
        input_manifest=bundle["input_manifest"],
    )
    resolution = resolve_hsp90_time_anatomy_obligation(
        rule_result=fresh_rule,
        case_graph=bundle["case_graph"],
        rule_overlay=bundle["rule_overlay"],
        operator_registry=registry,
        input_manifest=bundle["input_manifest"],
        workspace_root=repo_root,
    )
    if resolution.get("status") != "ROUTABLE" or resolution.get("operator_id") != action.get("operator_id"):
        return _status_receipt(
            schema_version="planner-deterministic-authorization/v1",
            case_id=case_id,
            status="REJECTED",
            reason_codes=["HSP90_EXACT_ROUTE_NOT_AUTHORIZED"],
            resolution=resolution,
            execution_performed=False,
            registered_operator_calls=0,
        )
    return _status_receipt(
        schema_version="planner-deterministic-authorization/v1",
        case_id=case_id,
        status="AUTHORIZED_NO_EXECUTION",
        reason_codes=[],
        resolution=resolution,
        execution_performed=False,
        registered_operator_calls=0,
    )


def evaluate_planner_proposal(
    proposal: Mapping[str, Any],
    packet: Mapping[str, Any],
    sealed_reference: Mapping[str, Any],
    repo_root: Path,
) -> dict[str, Any]:
    """Return the three bounded views of one Planner proposal."""

    proposal_mapping = proposal if isinstance(proposal, Mapping) else {}
    free_form_reasons = [
        f"ANSWER_BEARING_KEY:{path}" for path in find_forbidden_answer_paths(proposal_mapping)
    ]
    if not isinstance(proposal, Mapping):
        free_form_reasons.append("PROPOSAL_NOT_OBJECT")
    typed = validate_planner_proposal(proposal_mapping, packet)
    comparison = compare_planner_proposal(proposal_mapping, sealed_reference)
    authorization = authorize_planner_proposal(proposal_mapping, packet, repo_root)
    full_pass = (
        typed["status"] == "PASS"
        and comparison["status"] == "PASS"
        and authorization["status"] == "AUTHORIZED_NO_EXECUTION"
    )
    return {
        "schema_version": "planner-evaluation/v1",
        "case_id": _packet_case_id(packet),
        "free_form": _status_receipt(
            schema_version="free-form-view/v1",
            case_id=_packet_case_id(packet),
            status="PASS" if not free_form_reasons else "FAIL",
            reason_codes=free_form_reasons,
        ),
        "vocabulary_assisted": typed,
        "bounded_harness": _status_receipt(
            schema_version="bounded-planner-harness-view/v1",
            case_id=_packet_case_id(packet),
            status="PASS" if full_pass else "FAIL",
            reason_codes=[]
            if full_pass
            else ["TYPED_VALIDATION_OR_COMPARISON_OR_AUTHORIZATION_FAILED"],
            comparison=comparison,
            deterministic_authorization=authorization,
        ),
        "comparison_sampling_boundary": "The three views evaluate the same recorded model proposal; they are not independent model samples.",
    }
