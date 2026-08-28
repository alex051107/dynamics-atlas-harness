"""One bounded OpenRouter client for the exposed Profiler screening experiment.

This module intentionally contains no provider registry, model router, Planner,
tool execution, or scientific decision logic.  It builds one OpenAI-compatible
chat-completions request from a model-visible Profiler packet, records the response,
and hands the parsed proposal to the existing deterministic evaluator.
"""

from __future__ import annotations

import hashlib
import json
import math
import os
import time
import urllib.error
import urllib.request
from collections.abc import Callable, Mapping, Sequence
from pathlib import Path
from typing import Any

from .live_agent_exposed_v1 import (
    PROFILER_ROLE,
    evaluate_profiler_proposal,
    load_json_object,
    sha256_json,
    sha256_text,
    validate_model_visible_packet,
)


OPENROUTER_CHAT_COMPLETIONS_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_PROFILER_CONFIG_SCHEMA = "openrouter-profiler-screening-config/v1"
OPENROUTER_PROFILER_RECEIPT_SCHEMA = "openrouter-profiler-call-receipt/v1"
_EXECUTION_STATUS = "HUMAN_FROZEN_FOR_EXECUTION"
_CASE_WORKSPACE_NAMES = {"xeisd": "xeisd_profiler", "hsp90": "hsp90_profiler"}


class OpenRouterProfilerSweepError(ValueError):
    """Raised when the bounded Profiler screening contract is not satisfied."""


def _canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_file(path: Path) -> str:
    """Hash one frozen local input without reading any environment secret."""

    return hashlib.sha256(path.read_bytes()).hexdigest()


def _as_mapping(value: Any, label: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise OpenRouterProfilerSweepError(f"{label} must be an object")
    return value


def _as_nonempty_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise OpenRouterProfilerSweepError(f"{label} must be a nonempty string")
    return value


def _as_string_list(value: Any, label: str) -> list[str]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes, bytearray)):
        raise OpenRouterProfilerSweepError(f"{label} must be a string list")
    values = [_as_nonempty_string(item, f"{label} item") for item in value]
    if len(values) != len(set(values)):
        raise OpenRouterProfilerSweepError(f"{label} may not repeat values")
    return values


def _is_sha256(value: Any) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 64
        and all(character in "0123456789abcdef" for character in value.lower())
    )


def _positive_finite_number(value: Any) -> bool:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(value)
        and value > 0
    )


def _packet_output_contract(packet: Mapping[str, Any]) -> Mapping[str, Any]:
    contract = packet.get("output_contract")
    return _as_mapping(contract, "packet.output_contract")


def _packet_sources(packet: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    sources = packet.get("source_material")
    if not isinstance(sources, list) or not sources:
        raise OpenRouterProfilerSweepError("packet.source_material must be a nonempty list")
    return [_as_mapping(item, "packet.source_material item") for item in sources]


def _packet_edges(packet: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    edges = packet.get("edge_material")
    if not isinstance(edges, list):
        raise OpenRouterProfilerSweepError("packet.edge_material must be a list")
    return [_as_mapping(item, "packet.edge_material item") for item in edges]


def build_profiler_output_schema(packet: Mapping[str, Any]) -> dict[str, Any]:
    """Derive a strict JSON Schema from model-visible packet fields only."""

    packet = _as_mapping(packet, "packet")
    packet_validation = validate_model_visible_packet(packet, PROFILER_ROLE)
    if packet_validation["status"] != "PASS":
        raise OpenRouterProfilerSweepError(
            "model-visible Profiler packet failed preflight: "
            + ", ".join(packet_validation["reason_codes"])
        )
    contract = _packet_output_contract(packet)
    vocabulary = _as_mapping(packet.get("controlled_vocabulary"), "packet.controlled_vocabulary")
    source_ids = [_as_nonempty_string(item.get("source_id"), "source_id") for item in _packet_sources(packet)]
    source_locators = [
        _as_nonempty_string(item.get("source_locator"), "source_locator")
        for item in _packet_sources(packet)
    ]
    edge_ids = [_as_nonempty_string(item.get("edge_id"), "edge_id") for item in _packet_edges(packet)]
    unknown_policy = _as_mapping(packet.get("unknown_policy"), "packet.unknown_policy")
    required_unknown_paths = _as_string_list(
        unknown_policy.get("required_unknown_paths", []), "packet.unknown_policy.required_unknown_paths"
    )
    required_source_fields = _as_string_list(
        contract.get("required_source_fields", []), "packet.output_contract.required_source_fields"
    )
    required_edge_fields = _as_string_list(
        contract.get("required_edge_fields", []), "packet.output_contract.required_edge_fields"
    )
    unknown_item_fields = _as_string_list(
        contract.get("unknown_item_fields", []), "packet.output_contract.unknown_item_fields"
    )

    source_properties: dict[str, Any] = {
        "source_id": {"type": "string", "enum": source_ids},
        "method_or_modality": {
            "type": "string",
            "enum": _as_string_list(vocabulary.get("method_or_modality"), "method_or_modality"),
        },
        "evidence_role": {
            "type": "string",
            "enum": _as_string_list(vocabulary.get("evidence_role"), "evidence_role"),
        },
        "native_observable_kind": {
            "type": "string",
            "enum": _as_string_list(
                vocabulary.get("native_observable_kind"), "native_observable_kind"
            ),
        },
        "estimand_kind": {
            "type": "string",
            "enum": _as_string_list(vocabulary.get("estimand_kind"), "estimand_kind"),
        },
        "time_semantics": {
            "type": "string",
            "enum": _as_string_list(vocabulary.get("time_semantics"), "time_semantics"),
        },
        "source_locator": {"type": "string", "enum": source_locators},
        "sample_system_composition": {"type": "string"},
    }
    edge_properties: dict[str, Any] = {
        "edge_id": {"type": "string", "enum": edge_ids},
        "left_source_id": {"type": "string", "enum": source_ids},
        "right_source_id": {"type": "string", "enum": source_ids},
        "condition_relation": {"type": "string"},
    }
    unknown_properties = {
        "path": {"type": "string", "enum": required_unknown_paths},
        "reason": {"type": "string", "minLength": 1},
        "evidence_pointer": {"type": "string", "minLength": 1},
    }
    return {
        "type": "object",
        "additionalProperties": False,
        "required": _as_string_list(
            contract.get("required_top_level_fields", []),
            "packet.output_contract.required_top_level_fields",
        ),
        "properties": {
            "schema_version": {
                "type": "string",
                "const": _as_nonempty_string(contract.get("schema_version"), "schema_version"),
            },
            "case_id": {"type": "string", "const": _as_nonempty_string(packet.get("case_id"), "case_id")},
            "sources": {
                "type": "array",
                "minItems": len(source_ids),
                "maxItems": len(source_ids),
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": required_source_fields,
                    "properties": source_properties,
                },
            },
            "edges": {
                "type": "array",
                "minItems": len(edge_ids),
                "maxItems": len(edge_ids),
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": required_edge_fields,
                    "properties": edge_properties,
                },
            },
            "unknowns": {
                "type": "array",
                "minItems": len(required_unknown_paths),
                "maxItems": len(required_unknown_paths),
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": unknown_item_fields,
                    "properties": unknown_properties,
                },
            },
        },
    }


def validate_execution_config(config: Mapping[str, Any]) -> list[dict[str, Any]]:
    """Return fail-closed preflight findings for a future live screening run."""

    config = _as_mapping(config, "screening config")
    findings: list[dict[str, Any]] = []
    if config.get("schema_version") != OPENROUTER_PROFILER_CONFIG_SCHEMA:
        findings.append({"code": "INVALID_CONFIG_SCHEMA"})
    if config.get("execution_status") != _EXECUTION_STATUS:
        findings.append({"code": "MODEL_MATRIX_NOT_HUMAN_FROZEN"})
    if config.get("run_kind") != "SCREENING":
        findings.append({"code": "RUN_KIND_MUST_EQUAL_SCREENING"})
    if config.get("role") != PROFILER_ROLE:
        findings.append({"code": "NON_PROFILER_ROLE_FORBIDDEN"})
    if config.get("temperature") != 0:
        findings.append({"code": "SCREENING_TEMPERATURE_MUST_EQUAL_ZERO"})
    for field in ("max_tokens", "timeout_seconds"):
        value = config.get(field)
        if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
            findings.append({"code": f"INVALID_{field.upper()}"})
    if config.get("calls_per_model_case") != 1:
        findings.append({"code": "SCREENING_CALL_COUNT_MUST_EQUAL_ONE"})
    case_keys = config.get("case_keys")
    if case_keys != ["xeisd", "hsp90"]:
        findings.append({"code": "CASE_SCOPE_MUST_EQUAL_EXPOSED_XEISD_HSP90"})
    for field in ("prompt_path", "sealed_reference_path"):
        if not isinstance(config.get(field), str) or not config[field].strip():
            findings.append({"code": f"MISSING_{field.upper()}"})
    client_stop = config.get("client_side_reported_cost_stop_usd")
    if not _positive_finite_number(client_stop):
        findings.append({"code": "EXPLICIT_FINITE_CLIENT_SIDE_COST_STOP_REQUIRED"})
    account_readback = config.get("account_spend_limit_readback")
    if not isinstance(account_readback, Mapping):
        findings.append({"code": "ACCOUNT_SPEND_LIMIT_READBACK_REQUIRED"})
    elif (
        account_readback.get("status") != "HUMAN_CONFIRMED"
        or not isinstance(account_readback.get("evidence_locator"), str)
        or not account_readback["evidence_locator"].strip()
    ):
        findings.append({"code": "ACCOUNT_SPEND_LIMIT_NOT_HUMAN_CONFIRMED"})
    frozen_inputs = config.get("frozen_inputs")
    if not isinstance(frozen_inputs, Mapping):
        findings.append({"code": "FROZEN_INPUT_HASHES_REQUIRED"})
    else:
        for field in ("prompt_sha256", "sealed_reference_sha256"):
            if not _is_sha256(frozen_inputs.get(field)):
                findings.append({"code": "INVALID_FROZEN_INPUT_HASH", "input": field})
        for field in ("packet_sha256_by_case", "schema_sha256_by_case"):
            hashes = frozen_inputs.get(field)
            if not isinstance(hashes, Mapping) or set(hashes) != {"xeisd", "hsp90"}:
                findings.append({"code": "INVALID_FROZEN_INPUT_HASH_MAP", "input": field})
            else:
                for case_key in ("xeisd", "hsp90"):
                    if not _is_sha256(hashes.get(case_key)):
                        findings.append(
                            {"code": "INVALID_FROZEN_INPUT_HASH", "input": f"{field}.{case_key}"}
                        )
    models = config.get("models")
    if not isinstance(models, list) or not 3 <= len(models) <= 4:
        findings.append({"code": "FROZEN_THREE_TO_FOUR_MODEL_MATRIX_REQUIRED"})
    seen_model_ids: set[str] = set()
    seen_matrix_labels: set[str] = set()
    if not isinstance(models, list):
        models = []
    for index, model in enumerate(models):
        if not isinstance(model, Mapping):
            findings.append({"code": "INVALID_MODEL_SPEC", "index": index})
            continue
        matrix_label = model.get("matrix_label")
        if not isinstance(matrix_label, str) or not matrix_label.strip():
            findings.append({"code": "MISSING_MATRIX_LABEL", "index": index})
        elif matrix_label in seen_matrix_labels:
            findings.append({"code": "DUPLICATE_MATRIX_LABEL", "matrix_label": matrix_label})
        else:
            seen_matrix_labels.add(matrix_label)
        model_id = model.get("model_id")
        provider_only = model.get("provider_only")
        if not isinstance(model_id, str) or not model_id.strip() or model_id == "HUMAN_TO_FREEZE":
            findings.append({"code": "UNFROZEN_MODEL_ID", "index": index})
        elif model_id in seen_model_ids:
            findings.append({"code": "DUPLICATE_MODEL_ID", "model_id": model_id})
        else:
            seen_model_ids.add(model_id)
        if not isinstance(provider_only, list) or len(provider_only) != 1:
            findings.append({"code": "SINGLE_PROVIDER_ONLY_REQUIRED", "index": index})
        elif not isinstance(provider_only[0], str) or not provider_only[0].strip() or provider_only[0] == "HUMAN_TO_FREEZE":
            findings.append({"code": "UNFROZEN_PROVIDER_ONLY", "index": index})
    return findings


def _repository_file(repo_root: Path, relative_path: Any, label: str) -> Path:
    if not isinstance(relative_path, str) or not relative_path.strip():
        raise OpenRouterProfilerSweepError(f"{label} must be a nonempty repository-relative path")
    repo_root = repo_root.resolve()
    candidate = (repo_root / relative_path).resolve()
    try:
        candidate.relative_to(repo_root)
    except ValueError as exc:
        raise OpenRouterProfilerSweepError(f"{label} must remain inside the repository") from exc
    if not candidate.is_file():
        raise OpenRouterProfilerSweepError(f"{label} is unavailable: {candidate}")
    return candidate


def validate_frozen_input_hashes(config: Mapping[str, Any], repo_root: Path) -> list[dict[str, Any]]:
    """Verify frozen local inputs before a caller may read a credential or transport a request."""

    config = _as_mapping(config, "screening config")
    findings = validate_execution_config(config)
    if findings:
        return findings
    frozen_inputs = _as_mapping(config["frozen_inputs"], "screening config.frozen_inputs")
    try:
        prompt_path = _repository_file(repo_root, config["prompt_path"], "prompt_path")
        reference_path = _repository_file(
            repo_root, config["sealed_reference_path"], "sealed_reference_path"
        )
    except OpenRouterProfilerSweepError as exc:
        return [{"code": "FROZEN_INPUT_UNAVAILABLE", "detail": str(exc)}]

    observed_hashes: dict[str, str] = {
        "prompt_sha256": sha256_file(prompt_path),
        "sealed_reference_sha256": sha256_file(reference_path),
    }
    packets: dict[str, Mapping[str, Any]] = {}
    for case_key, workspace in _CASE_WORKSPACE_NAMES.items():
        try:
            packet_path = _repository_file(
                repo_root,
                f"agent_experiments/v1/workspaces/{workspace}/input.json",
                f"{case_key} packet",
            )
            packets[case_key] = load_json_object(packet_path)
        except (OpenRouterProfilerSweepError, ValueError, json.JSONDecodeError) as exc:
            return [{"code": "FROZEN_INPUT_UNAVAILABLE", "detail": str(exc)}]
        observed_hashes[f"packet_sha256_by_case.{case_key}"] = sha256_file(packet_path)
        observed_hashes[f"schema_sha256_by_case.{case_key}"] = sha256_json(
            build_profiler_output_schema(packets[case_key])
        )

    expected_hashes: dict[str, Any] = {
        "prompt_sha256": frozen_inputs["prompt_sha256"],
        "sealed_reference_sha256": frozen_inputs["sealed_reference_sha256"],
        **{
            f"packet_sha256_by_case.{case_key}": frozen_inputs["packet_sha256_by_case"][case_key]
            for case_key in _CASE_WORKSPACE_NAMES
        },
        **{
            f"schema_sha256_by_case.{case_key}": frozen_inputs["schema_sha256_by_case"][case_key]
            for case_key in _CASE_WORKSPACE_NAMES
        },
    }
    return [
        {"code": "FROZEN_INPUT_HASH_MISMATCH", "input": key}
        for key, expected in expected_hashes.items()
        if observed_hashes[key] != expected
    ]


def screening_cells(config: Mapping[str, Any]) -> list[dict[str, str]]:
    """Return the exact single-call screening cells once a configuration is frozen."""

    findings = validate_execution_config(config)
    if findings:
        raise OpenRouterProfilerSweepError(
            "execution configuration is blocked: " + ", ".join(item["code"] for item in findings)
        )
    return [
        {"case_key": case_key, "model_id": model["model_id"], "matrix_label": model["matrix_label"]}
        for model in config["models"]
        for case_key in config["case_keys"]
    ]


def read_openrouter_api_key(environment: Mapping[str, str] | None = None) -> str:
    """Read the one environment-only credential when a later live run is admitted."""

    environment = os.environ if environment is None else environment
    api_key = environment.get("OPENROUTER_API_KEY")
    if not isinstance(api_key, str) or not api_key.strip():
        raise OpenRouterProfilerSweepError("OPENROUTER_API_KEY is required before transport")
    return api_key


def build_profiler_request(
    *,
    model_spec: Mapping[str, Any],
    prompt: str,
    packet: Mapping[str, Any],
    temperature: float,
    max_tokens: int,
) -> dict[str, Any]:
    """Build the one strict, tool-less OpenRouter payload for a Profiler cell."""

    model_spec = _as_mapping(model_spec, "model_spec")
    model_id = _as_nonempty_string(model_spec.get("model_id"), "model_spec.model_id")
    provider_only = _as_string_list(model_spec.get("provider_only"), "model_spec.provider_only")
    if len(provider_only) != 1:
        raise OpenRouterProfilerSweepError("model_spec.provider_only must contain exactly one provider")
    if not isinstance(temperature, (int, float)) or isinstance(temperature, bool) or temperature != 0:
        raise OpenRouterProfilerSweepError("screening temperature must be exactly zero")
    if not isinstance(max_tokens, int) or max_tokens <= 0:
        raise OpenRouterProfilerSweepError("max_tokens must be a positive integer")
    prompt = _as_nonempty_string(prompt, "prompt")
    schema = build_profiler_output_schema(packet)
    return {
        "model": model_id,
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": "Task packet:\n" + _canonical_json(packet)},
        ],
        "temperature": 0,
        "max_tokens": max_tokens,
        "stream": False,
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": "dynamics_atlas_profiler_proposal",
                "strict": True,
                "schema": schema,
            },
        },
        "provider": {
            "allow_fallbacks": False,
            "require_parameters": True,
            "only": provider_only,
        },
    }


def _numeric(value: Any) -> int | float:
    return (
        value
        if isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(value)
        else 0
    )


def _reported_cost_or_none(value: Any) -> float | None:
    """Keep a missing, negative, or non-finite provider cost fail-closed."""

    if (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(value)
        and value >= 0
    ):
        return float(value)
    return None


def _router_metadata(response: Mapping[str, Any]) -> tuple[str, dict[str, Any]]:
    metadata = response.get("openrouter_metadata")
    if not isinstance(metadata, Mapping):
        return "UNKNOWN_METADATA_ABSENT", {"status": "ABSENT"}
    selected_provider = "UNKNOWN_METADATA_ABSENT"
    endpoints = metadata.get("endpoints")
    if isinstance(endpoints, Mapping):
        available = endpoints.get("available")
        if isinstance(available, list):
            for endpoint in available:
                if isinstance(endpoint, Mapping) and endpoint.get("selected") is True:
                    provider = endpoint.get("provider")
                    if isinstance(provider, str) and provider:
                        selected_provider = provider
                        break
    return selected_provider, dict(metadata)


def _provider_provenance(
    *,
    response: Mapping[str, Any] | None,
    request_payload: Mapping[str, Any],
    actual_provider: str,
    router_metadata: Mapping[str, Any],
) -> tuple[str, list[str]]:
    """Verify the one requested model/provider path; never treat routing as a fallback."""

    reason_codes: list[str] = []
    requested_model = request_payload.get("model")
    returned_model = response.get("model") if isinstance(response, Mapping) else None
    if returned_model != requested_model:
        reason_codes.append("RETURNED_MODEL_MISMATCH")
    provider = request_payload.get("provider")
    provider_only = provider.get("only") if isinstance(provider, Mapping) else None
    expected_provider = provider_only[0] if isinstance(provider_only, list) and provider_only else None
    if not isinstance(expected_provider, str) or not expected_provider:
        reason_codes.append("REQUESTED_PROVIDER_CONSTRAINT_INVALID")
    elif not isinstance(actual_provider, str) or actual_provider.startswith("UNKNOWN_"):
        reason_codes.append("ROUTER_PROVIDER_METADATA_MISSING")
    elif actual_provider.casefold() != expected_provider.casefold():
        reason_codes.append("ACTUAL_PROVIDER_MISMATCH")
    attempt = router_metadata.get("attempt")
    if not isinstance(attempt, int) or isinstance(attempt, bool) or attempt != 1:
        reason_codes.append("ROUTER_ATTEMPT_MUST_EQUAL_ONE")
    return ("PASS" if not reason_codes else "FAIL"), reason_codes


def _response_content(response: Mapping[str, Any]) -> str | None:
    choices = response.get("choices")
    if not isinstance(choices, list) or not choices:
        return None
    first = choices[0]
    if not isinstance(first, Mapping):
        return None
    message = first.get("message")
    if not isinstance(message, Mapping):
        return None
    content = message.get("content")
    return content if isinstance(content, str) else None


class OpenRouterProfilerJsonClient:
    """One concrete OpenRouter transport for the bounded Profiler experiment."""

    def __init__(
        self,
        *,
        api_key: str,
        timeout_seconds: int = 90,
        open_call: Callable[..., Any] = urllib.request.urlopen,
    ) -> None:
        self._api_key = _as_nonempty_string(api_key, "OPENROUTER_API_KEY")
        if not isinstance(timeout_seconds, int) or timeout_seconds <= 0:
            raise OpenRouterProfilerSweepError("timeout_seconds must be a positive integer")
        self.timeout_seconds = timeout_seconds
        self._open_call = open_call

    def call(
        self,
        *,
        model_spec: Mapping[str, Any],
        prompt: str,
        packet: Mapping[str, Any],
        temperature: float,
        max_tokens: int,
    ) -> dict[str, Any]:
        """Make exactly one request; failures produce a receipt and never retry."""

        request_payload = build_profiler_request(
            model_spec=model_spec,
            prompt=prompt,
            packet=packet,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        packet = _as_mapping(packet, "packet")
        request_bytes = _canonical_json(request_payload).encode("utf-8")
        request = urllib.request.Request(
            OPENROUTER_CHAT_COMPLETIONS_URL,
            data=request_bytes,
            headers={
                "Authorization": f"Bearer {self._api_key}",
                "Content-Type": "application/json",
                "X-OpenRouter-Metadata": "enabled",
            },
            method="POST",
        )
        started = time.monotonic()
        response: dict[str, Any] | None = None
        raw_text = ""
        reason_codes: list[str] = []
        http_status: int | None = None
        try:
            with self._open_call(request, timeout=self.timeout_seconds) as http_response:
                http_status = getattr(http_response, "status", None)
                raw_text = http_response.read().decode("utf-8")
                response_value = json.loads(raw_text)
                if isinstance(response_value, Mapping):
                    response = dict(response_value)
                else:
                    reason_codes.append("OPENROUTER_RESPONSE_NOT_OBJECT")
        except urllib.error.HTTPError as exc:
            http_status = exc.code
            raw_text = exc.read().decode("utf-8", errors="replace")
            reason_codes.append(f"HTTP_ERROR:{exc.code}")
        except urllib.error.URLError as exc:
            reason_codes.append("TRANSPORT_ERROR")
        except (OSError, UnicodeDecodeError, json.JSONDecodeError):
            reason_codes.append("OPENROUTER_RESPONSE_UNREADABLE")
        latency_ms = round((time.monotonic() - started) * 1000)

        parsed_proposal: dict[str, Any] | None = None
        if response is not None:
            content = _response_content(response)
            if content is None:
                reason_codes.append("OPENROUTER_RESPONSE_CONTENT_MISSING")
            else:
                try:
                    parsed_value = json.loads(content)
                except json.JSONDecodeError:
                    reason_codes.append("MODEL_CONTENT_NOT_JSON_OBJECT")
                else:
                    if isinstance(parsed_value, Mapping):
                        parsed_proposal = dict(parsed_value)
                    else:
                        reason_codes.append("MODEL_CONTENT_NOT_JSON_OBJECT")
        actual_provider, router_metadata = _router_metadata(response or {})
        transport_status = "SUCCEEDED" if response is not None else "FAILED"
        proposal_parse_status = (
            "PARSED_JSON_OBJECT" if parsed_proposal is not None else "FAILED"
        )
        provider_provenance_status, provider_provenance_reason_codes = _provider_provenance(
            response=response,
            request_payload=request_payload,
            actual_provider=actual_provider,
            router_metadata=router_metadata,
        )
        usage_raw = response.get("usage", {}) if response is not None else {}
        usage_raw = usage_raw if isinstance(usage_raw, Mapping) else {}
        usage = {
            "prompt_tokens": _numeric(usage_raw.get("prompt_tokens")),
            "completion_tokens": _numeric(usage_raw.get("completion_tokens")),
            "total_tokens": _numeric(usage_raw.get("total_tokens")),
            "cost": _reported_cost_or_none(usage_raw.get("cost")),
        }
        if usage["cost"] is None:
            reason_codes.append("REPORTED_COST_UNAVAILABLE")
        receipt = {
            "schema_version": OPENROUTER_PROFILER_RECEIPT_SCHEMA,
            "status": "TRANSPORT_SUCCEEDED" if transport_status == "SUCCEEDED" else "TRANSPORT_FAILED",
            "transport_status": transport_status,
            "proposal_parse_status": proposal_parse_status,
            "provider_provenance_status": provider_provenance_status,
            "provider_provenance_reason_codes": provider_provenance_reason_codes,
            "typed_contract_status": "NOT_EVALUATED",
            "sealed_reference_status": "NOT_EVALUATED",
            "screening_candidate_status": "NOT_EVALUATED",
            "case_id": packet.get("case_id"),
            "role": PROFILER_ROLE,
            "transport": "OPENROUTER_CHAT_COMPLETIONS_JSON_SCHEMA_NO_TOOLS",
            "requested_model": request_payload["model"],
            "returned_model": response.get("model") if isinstance(response, Mapping) else None,
            "requested_provider_constraints": request_payload["provider"],
            "actual_provider": actual_provider,
            "router_metadata": router_metadata,
            "prompt_sha256": sha256_text(prompt),
            "packet_sha256": sha256_json(packet),
            "schema_sha256": sha256_json(request_payload["response_format"]["json_schema"]["schema"]),
            "request_sha256": sha256_text(request_bytes.decode("utf-8")),
            "response_sha256": sha256_text(raw_text),
            "latency_ms": latency_ms,
            "call_count": 1,
            "tool_calls": 0,
            "http_status": http_status,
            "usage": usage,
            "cost_usd": usage["cost"],
            "reason_codes": reason_codes,
            "scientific_disposition": "NOT_EVALUATED",
        }
        return {
            "raw_response": raw_text,
            "parsed_proposal": parsed_proposal,
            "receipt": receipt,
        }


def deterministic_hallucination_markers(evaluation: Mapping[str, Any]) -> dict[str, int]:
    """Count only evaluator-recorded fact/UNKNOWN contract failures; no LLM judge."""

    typed = evaluation.get("typed_contract_view")
    typed = typed if isinstance(typed, Mapping) else {}
    sealed = evaluation.get("sealed_reference_and_authorization_view")
    sealed = sealed if isinstance(sealed, Mapping) else {}
    comparison = sealed.get("sealed_reference_comparison")
    comparison = comparison if isinstance(comparison, Mapping) else {}
    differences = comparison.get("critical_differences")
    differences = differences if isinstance(differences, list) else []
    typed_reasons = typed.get("reason_codes")
    typed_reasons = typed_reasons if isinstance(typed_reasons, list) else []
    return {
        "critical_fact_mismatch_count": sum(
            1
            for item in differences
            if isinstance(item, Mapping)
            and item.get("kind") in {"CRITICAL_SOURCE_FACT_MISMATCH", "CRITICAL_EDGE_FACT_MISMATCH"}
        ),
        "required_unknown_missing_count": sum(
            1
            for item in differences
            if isinstance(item, Mapping) and item.get("kind") == "REQUIRED_UNKNOWN_MISSING"
        ),
        "fabricated_non_unknown_count": sum(
            1
            for reason in typed_reasons
            if isinstance(reason, str) and reason.startswith("MISSING_OR_FABRICATED_UNKNOWN:")
        ),
    }


def write_call_artifacts(
    *,
    cell_root: Path,
    call_artifact: Mapping[str, Any],
    evaluation: Mapping[str, Any] | None,
) -> dict[str, str]:
    """Persist the response, proposal, receipt, and evaluation for one completed cell."""

    cell_root = cell_root.resolve()
    cell_root.mkdir(parents=True, exist_ok=False)
    raw_path = cell_root / "raw_response.txt"
    proposal_path = cell_root / "proposal.json"
    receipt_path = cell_root / "model_call_receipt.json"
    evaluation_path = cell_root / "evaluation.json"
    raw_path.write_text(str(call_artifact["raw_response"]), encoding="utf-8")
    proposal = call_artifact.get("parsed_proposal")
    if proposal is not None:
        proposal_path.write_text(json.dumps(proposal, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    receipt = dict(_as_mapping(call_artifact.get("receipt"), "call_artifact.receipt"))
    receipt.update(
        {
            "raw_response_path": raw_path.name,
            "parsed_proposal_path": proposal_path.name if proposal is not None else None,
            "evaluation_path": evaluation_path.name if evaluation is not None else None,
        }
    )
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if evaluation is not None:
        evaluation_path.write_text(json.dumps(evaluation, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {
        "raw_response_path": raw_path.name,
        "parsed_proposal_path": proposal_path.name if proposal is not None else "NOT_CREATED",
        "model_call_receipt_path": receipt_path.name,
        "evaluation_path": evaluation_path.name if evaluation is not None else "NOT_CREATED",
    }


def _evaluation_view_status(evaluation: Mapping[str, Any] | None, view: str) -> str:
    if not isinstance(evaluation, Mapping):
        return "NOT_EVALUATED"
    result = evaluation.get(view)
    return result.get("status") if isinstance(result, Mapping) and isinstance(result.get("status"), str) else "NOT_EVALUATED"


def _finalize_screening_receipt(
    receipt: Mapping[str, Any], evaluation: Mapping[str, Any] | None
) -> dict[str, Any]:
    """Keep transport, provenance, and deterministic capability outcomes distinct."""

    finalized = dict(receipt)
    typed_status = _evaluation_view_status(evaluation, "typed_contract_view")
    sealed_status = _evaluation_view_status(
        evaluation, "sealed_reference_and_authorization_view"
    )
    finalized["typed_contract_status"] = typed_status
    finalized["sealed_reference_status"] = sealed_status
    if finalized.get("transport_status") != "SUCCEEDED":
        screening_status = "TRANSPORT_FAILED"
    elif finalized.get("provider_provenance_status") != "PASS":
        screening_status = "PROVENANCE_REJECTED"
    elif finalized.get("proposal_parse_status") != "PARSED_JSON_OBJECT":
        screening_status = "CAPABILITY_REJECTED"
    elif finalized.get("cost_usd") is None:
        screening_status = "REPORTED_COST_UNAVAILABLE"
    elif typed_status != "PASS" or sealed_status != "PASS":
        screening_status = "CAPABILITY_REJECTED"
    else:
        screening_status = "PASS"
    finalized["screening_candidate_status"] = screening_status
    return finalized


def run_screening(
    *,
    config: Mapping[str, Any],
    repo_root: Path,
    output_root: Path,
    api_key: str,
    client: OpenRouterProfilerJsonClient | None = None,
) -> dict[str, Any]:
    """Run only a pre-frozen Profiler screening matrix; no retry or follow-on sweep."""

    repo_root = repo_root.resolve()
    config_findings = validate_execution_config(config)
    frozen_input_findings = validate_frozen_input_hashes(config, repo_root)
    if config_findings or frozen_input_findings:
        findings = config_findings + [
            finding for finding in frozen_input_findings if finding not in config_findings
        ]
        raise OpenRouterProfilerSweepError(
            "execution configuration is blocked: " + ", ".join(item["code"] for item in findings)
        )
    cells = screening_cells(config)
    output_root = output_root.resolve()
    if output_root.exists():
        raise OpenRouterProfilerSweepError(f"refusing to overwrite screening output: {output_root}")
    config = _as_mapping(config, "screening config")
    prompt = _repository_file(repo_root, config["prompt_path"], "prompt_path").read_text(
        encoding="utf-8"
    )
    sealed_reference = load_json_object(
        _repository_file(repo_root, config["sealed_reference_path"], "sealed_reference_path")
    )
    timeout_seconds = config.get("timeout_seconds")
    if not isinstance(timeout_seconds, int):
        raise OpenRouterProfilerSweepError("timeout_seconds must be an integer")
    if client is None:
        client = OpenRouterProfilerJsonClient(api_key=api_key, timeout_seconds=timeout_seconds)
    output_root.mkdir(parents=True, exist_ok=False)
    total_cost = 0.0
    stop_later_cells_reason: str | None = None
    cell_results: list[dict[str, Any]] = []
    for index, cell in enumerate(cells):
        if stop_later_cells_reason is not None:
            cell_results.append(
                {
                    **cell,
                    "screening_candidate_status": "BLOCKED_REPORTED_COST_UNAVAILABLE",
                    "reason_codes": [stop_later_cells_reason],
                    "call_count": 0,
                }
            )
            continue
        if total_cost >= float(config["client_side_reported_cost_stop_usd"]):
            cell_results.append(
                {
                    **cell,
                    "screening_candidate_status": "BLOCKED_CLIENT_SIDE_COST_STOP",
                    "reason_codes": ["BUDGET_EXHAUSTED_BEFORE_CELL"],
                    "call_count": 0,
                }
            )
            continue
        workspace = _CASE_WORKSPACE_NAMES[cell["case_key"]]
        packet = load_json_object(repo_root / "agent_experiments" / "v1" / "workspaces" / workspace / "input.json")
        model_spec = next(model for model in config["models"] if model["model_id"] == cell["model_id"])
        call_artifact = client.call(
            model_spec=model_spec,
            prompt=prompt,
            packet=packet,
            temperature=config["temperature"],
            max_tokens=config["max_tokens"],
        )
        proposal = call_artifact.get("parsed_proposal")
        evaluation = (
            evaluate_profiler_proposal(proposal, packet, sealed_reference)
            if isinstance(proposal, Mapping)
            else None
        )
        receipt = _finalize_screening_receipt(
            _as_mapping(call_artifact["receipt"], "call receipt"), evaluation
        )
        reported_cost = _reported_cost_or_none(receipt.get("cost_usd"))
        if reported_cost is None:
            receipt["cost_usd"] = None
            receipt["usage"] = {**_as_mapping(receipt.get("usage", {}), "receipt.usage"), "cost": None}
            receipt["reason_codes"] = list(receipt.get("reason_codes", []))
            if "REPORTED_COST_UNAVAILABLE" not in receipt["reason_codes"]:
                receipt["reason_codes"].append("REPORTED_COST_UNAVAILABLE")
            receipt["screening_candidate_status"] = "REPORTED_COST_UNAVAILABLE"
            stop_later_cells_reason = "PREVIOUS_CELL_REPORTED_COST_UNAVAILABLE"
        call_artifact = {**call_artifact, "receipt": receipt}
        paths = write_call_artifacts(
            cell_root=output_root / f"{index + 1:02d}_{cell['case_key']}_{cell['matrix_label']}",
            call_artifact=call_artifact,
            evaluation=evaluation,
        )
        if reported_cost is not None:
            total_cost += reported_cost
        cell_results.append(
            {
                **cell,
                "screening_candidate_status": receipt["screening_candidate_status"],
                "transport_status": receipt["transport_status"],
                "provider_provenance_status": receipt["provider_provenance_status"],
                "typed_contract_status": receipt["typed_contract_status"],
                "sealed_reference_status": receipt["sealed_reference_status"],
                "call_count": receipt["call_count"],
                "cost_usd": receipt["cost_usd"],
                "latency_ms": receipt["latency_ms"],
                "actual_provider": receipt["actual_provider"],
                "reason_codes": receipt["reason_codes"],
                "hallucination_markers": deterministic_hallucination_markers(evaluation)
                if evaluation is not None
                else None,
                "paths": paths,
            }
        )
    run_receipt = {
        "schema_version": "openrouter-profiler-screening-run-receipt/v1",
        "run_kind": "SCREENING",
        "role": PROFILER_ROLE,
        "planned_cells": len(cells),
        "completed_cells": sum(1 for item in cell_results if item["call_count"] == 1),
        "total_reported_cost_usd": total_cost,
        "client_side_reported_cost_stop_usd": config["client_side_reported_cost_stop_usd"],
        "account_spend_limit_readback": config["account_spend_limit_readback"],
        "config_sha256": sha256_json(config),
        "prompt_sha256": sha256_text(prompt),
        "planner_model_calls": 0,
        "operator_calls": 0,
        "tool_calls": 0,
        "end_to_end": "NOT_RUN",
        "scientific_disposition": "NOT_EVALUATED",
        "cell_results": cell_results,
        "budget_boundary": "The client stops later cells only after reported cost reaches the configured stop. It cannot prevent one accepted request from exceeding that value. A separate account/key spending limit or deliberately limited balance is human-confirmed before live use.",
    }
    (output_root / "run_receipt.json").write_text(
        json.dumps(run_receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return run_receipt
