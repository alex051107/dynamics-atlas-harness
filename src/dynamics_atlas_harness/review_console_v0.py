"""Static, read-only source-science review workspace and console for Delivery A.

This module is deliberately scoped to the merged exposed development capsule.
It assembles a human-review queue from existing repository evidence and renders a
local HTML trace.  It does not activate a Rule, execute an action, call a model,
or write canonical scientific state.
"""

from __future__ import annotations

import argparse
import html
import json
import re
from collections.abc import Mapping, Sequence
from datetime import date
from pathlib import Path
from typing import Any

from .case_view_v1 import CaseView, build_case_view, unavailable


REPO_ROOT = Path(__file__).resolve().parents[2]
SOURCE_PACKET_PATH = REPO_ROOT / "evidence" / "rules_v1" / "source_evidence_packets_v1.jsonl"
NARROW_REVIEW_PACKET_PATH = (
    REPO_ROOT
    / "evidence"
    / "minimal_stage2_exposed_conclusions_v1"
    / "narrow_source_science_review_packet_v1.json"
)
RULES_ROOT = REPO_ROOT / "registries" / "rules_v1"
F04R02_OVERLAY_PATH = (
    REPO_ROOT / "evidence" / "real_case_vertical_slice_v1" / "hsp90_f04r02_rule_overlay_v1.json"
)
DEFAULT_CAPSULE_ROOT = (
    REPO_ROOT
    / "evidence"
    / "paper_blind_exposed_v1"
    / "development_runs"
    / "exposed_paper_blind_scientific_decision_capsule_v1"
)
DEFAULT_REVIEW_WORKSPACE = REPO_ROOT / "review" / "source_science_v1"
SOURCE_SCIENCE_ADVISORY_PATH = (
    REPO_ROOT
    / "evidence"
    / "source_science_advisory_v1"
    / "advisory_reconciliation.json"
)

REVIEW_DISPOSITIONS = (
    "APPROVE_AS_WRITTEN",
    "APPROVE_WITH_BOUNDED_REVISION",
    "DEFER_INSUFFICIENT_SOURCE_GROUNDING",
    "REJECT_NOT_REUSABLE",
    "NOT_APPLICABLE_TO_CURRENT_CASE",
)

POSITIVE_REVIEW_DISPOSITIONS = (
    "APPROVE_AS_WRITTEN",
    "APPROVE_WITH_BOUNDED_REVISION",
)

REVIEW_FORM_STATUSES = ("DRAFT", "COMPLETED")

# The older narrow review packet predates the final runtime names.  These aliases
# only point reviewers to the current repository contracts; they do not change a
# runtime Rule or create a new authority.
_RUNTIME_SUBRULE_ALIASES = {
    "F01R01_CASE_CLAIM_CONTRACT_PRESENT": "F01R01_CASE_CLAIM_DECLARATION",
    "F01R02_CASE_REQUESTED_WORDING_IN_SCOPE": "F01R02_CASE_REQUESTED_WORDING_SCOPE",
    "F03R01_SOURCE_NATIVE_MEASUREMENT_DECLARATION": "F03R01_SOURCE_NATIVE_MEASUREMENT",
    "F06R01_SOURCE_EVIDENCE_ROLE_DECLARATION": "F06R01_SOURCE_EVIDENCE_ROLE",
    "F06R02_EDGE_CROSS_SOURCE_COMPARABILITY": "F06R02_EDGE_COMPARABILITY",
}

_URL_PATTERN = re.compile(r"https?://[^\s<>()]+")


class ReviewConsoleError(ValueError):
    """Raised when required review evidence cannot be presented faithfully."""


def _read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ReviewConsoleError(f"JSON_UNREADABLE:{path}") from error
    if not isinstance(value, dict):
        raise ReviewConsoleError(f"JSON_OBJECT_REQUIRED:{path}")
    return value


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as error:
        raise ReviewConsoleError(f"JSONL_UNREADABLE:{path}") from error
    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as error:
            raise ReviewConsoleError(f"JSONL_INVALID:{path}:{line_number}") from error
        if not isinstance(value, dict):
            raise ReviewConsoleError(f"JSONL_OBJECT_REQUIRED:{path}:{line_number}")
        records.append(value)
    return records


def _write_json(path: Path, value: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _canonical_subrule_id(runtime_subrule_id: str) -> str:
    return _RUNTIME_SUBRULE_ALIASES.get(runtime_subrule_id, runtime_subrule_id)


def _compact_contract(contract: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "evaluation_contract_id": contract["evaluation_contract_id"],
        "runtime_subrule_id": contract["runtime_subrule_id"],
        "target_kind": contract["target_kind"],
        "implementation_status": contract["implementation_status"],
        "human_decision_gate_id": contract["human_decision_gate_id"],
        "pass_conditions": contract["pass_conditions"],
        "fail_conditions": contract["fail_conditions"],
        "unresolved_conditions": contract["unresolved_conditions"],
        "result_effects": contract["result_effects"],
    }


def _compact_policy(policy: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "resolution_policy_id": policy["resolution_policy_id"],
        "purpose": policy["purpose"],
        "allowed_routes": policy["allowed_routes"],
        "operator_route_allowed": policy["operator_route_allowed"],
        "unresolved_route": policy["unresolved_route"],
        "fail_route": policy["fail_route"],
        "completion_evidence": policy["completion_evidence"],
        "forbidden_actions": policy["forbidden_actions"],
    }


def _case_directories(capsule_root: Path) -> list[Path]:
    directories = [
        path
        for path in capsule_root.iterdir()
        if path.is_dir() and (path / "human_decision_packet.json").is_file()
    ]
    if not directories:
        raise ReviewConsoleError(f"NO_CASE_PACKETS:{capsule_root}")
    return sorted(directories, key=lambda path: path.name)


def _source_entry(
    *,
    item: Mapping[str, Any],
    packets_by_id: Mapping[str, Mapping[str, Any]],
    bindings_by_subrule: Mapping[str, Mapping[str, Any]],
    contracts_by_subrule: Mapping[str, Mapping[str, Any]],
    policies_by_id: Mapping[str, Mapping[str, Any]],
    runtime_subrules_by_id: Mapping[str, Mapping[str, Any]],
    runtime_subrules_registry_status: str,
    family_overlay_by_id: Mapping[str, Mapping[str, Any]],
    family_overlay_registry_status: str,
    f04_overlay: Mapping[str, Any],
) -> dict[str, Any]:
    review_subrule = str(item["runtime_subrule_id"])
    current_subrule = _canonical_subrule_id(review_subrule)
    evidence_packet_id = str(item["evidence_packet_id"])

    if current_subrule == "F04R02_SOURCE_DECLARED_TIME_ANATOMY_CONTROL":
        runtime_subrule = f04_overlay["runtime_subrule"]
        binding = f04_overlay["binding"]
        contract = f04_overlay["evaluation_contract"]
        policy = f04_overlay["resolution_policy"]
        family_overlay = family_overlay_by_id[str(item["family_id"])]
        return {
            "review_item_id": item["review_item_id"],
            "family_id": item["family_id"],
            "review_packet_runtime_subrule_id": review_subrule,
            "runtime_subrule_id": current_subrule,
            "evidence_packet_id": evidence_packet_id,
            "paper_id": item["paper_id"],
            "primary_source_locator": item["primary_locator"],
            "primary_locator_status": "CASE_BOUND_TRACEABILITY_MAPPING_PENDING",
            "short_source_passage": "No primary-paper passage is currently mapped for this case-bound control. The named reviewer must resolve the dossier/manifest-to-packet mapping before deciding narrow reuse.",
            "passage_kind": "CASE_BOUND_REPOSITORY_ARTIFACT_NOT_PRIMARY_PAPER_PASSAGE",
            "atomic_scientific_statement": item["atomic_statement"],
            "proposed_reusable_review_question": item["proposed_reusable_use"],
            "forbidden_generalization": item["forbidden_generalization"],
            "source_packet_status": "PENDING_SOURCE_TRACEABILITY_MAPPING",
            "traceability_note": item.get("traceability_note"),
            "scientific_question": runtime_subrule["scientific_question"],
            "claim_effect_summary": runtime_subrule["claim_effect_summary"],
            "implementation_status": runtime_subrule["implementation_status"],
            "runtime_subrules_registry_status": runtime_subrules_registry_status,
            "runtime_subrule_origin": "CASE_BOUND_OVERLAY_NOT_RUNTIME_SUBRULES_V1_MEMBER",
            "family_overlay_registry_status": family_overlay_registry_status,
            "family_overlay": dict(family_overlay),
            "binding": dict(binding),
            "evaluation_contract": dict(contract),
            "resolution_policy": dict(policy),
            "claim_ceiling": runtime_subrule["claim_effect_summary"],
            "reviewer_status": "PENDING_DOMAIN_REVIEW",
        }

    packet = packets_by_id.get(evidence_packet_id)
    if packet is None:
        raise ReviewConsoleError(f"SOURCE_PACKET_NOT_FOUND:{evidence_packet_id}")
    binding = bindings_by_subrule.get(current_subrule)
    contract = contracts_by_subrule.get(current_subrule)
    if binding is None or contract is None:
        raise ReviewConsoleError(f"RULE_CONTRACT_NOT_FOUND:{current_subrule}")
    policy_id = str(binding["resolution_policy_id"])
    policy = policies_by_id.get(policy_id)
    if policy is None:
        raise ReviewConsoleError(f"RESOLUTION_POLICY_NOT_FOUND:{policy_id}")
    if binding["evaluation_contract_id"] != contract["evaluation_contract_id"]:
        raise ReviewConsoleError(f"BINDING_CONTRACT_MISMATCH:{current_subrule}")
    runtime_subrule = runtime_subrules_by_id.get(current_subrule)
    if runtime_subrule is None:
        raise ReviewConsoleError(f"RUNTIME_SUBRULE_NOT_FOUND:{current_subrule}")
    family_overlay = family_overlay_by_id.get(str(item["family_id"]))
    if family_overlay is None:
        raise ReviewConsoleError(f"FAMILY_OVERLAY_NOT_FOUND:{item['family_id']}")
    entry = {
        "review_item_id": item["review_item_id"],
        "family_id": item["family_id"],
        "review_packet_runtime_subrule_id": review_subrule,
        "runtime_subrule_id": current_subrule,
        "evidence_packet_id": evidence_packet_id,
        "paper_id": packet["paper_id"],
        "primary_source_locator": packet["source_locator"],
        "primary_locator_status": "REVIEW_DERIVATIVE_LOCATOR_REQUIRES_PRIMARY_PASSAGE_CHECK",
        "short_source_passage": packet["short_passage"],
        "passage_kind": packet["derivative_kind"],
        "atomic_scientific_statement": packet["atomic_paper_statement"],
        "proposed_reusable_review_question": packet["proposed_reusable_use"],
        "forbidden_generalization": packet["forbidden_generalization"],
        "source_packet_status": packet["human_review_status"],
        "traceability_note": packet.get("traceability_note"),
        "scientific_question": runtime_subrule["scientific_question"],
        "claim_effect_summary": runtime_subrule["claim_effect_summary"],
        "implementation_status": runtime_subrule["implementation_status"],
        "runtime_subrules_registry_status": runtime_subrules_registry_status,
        "runtime_subrule_origin": "RUNTIME_SUBRULES_V1",
        "family_overlay_registry_status": family_overlay_registry_status,
        "family_overlay": dict(family_overlay),
        "binding": dict(binding),
        "evaluation_contract": _compact_contract(contract),
        "resolution_policy": _compact_policy(policy),
        "claim_ceiling": packet["forbidden_generalization"],
        "reviewer_status": "PENDING_DOMAIN_REVIEW",
    }
    return entry


def _case_application(
    *,
    case_dir: Path,
    entry: Mapping[str, Any],
) -> dict[str, Any]:
    packet = _read_json(case_dir / "human_decision_packet.json")
    active_results = packet.get("active_rule_results", [])
    if not isinstance(active_results, list):
        raise ReviewConsoleError(f"RULE_RESULTS_LIST_REQUIRED:{case_dir}")
    runtime_subrule_id = str(entry["runtime_subrule_id"])
    matching = [
        result
        for result in active_results
        if isinstance(result, dict)
        and _canonical_subrule_id(str(result.get("runtime_subrule_id", "")))
        == runtime_subrule_id
    ]
    application = {
        "case_id": packet["case_id"],
        "case_directory": case_dir.name,
        "public_case_terminal_disposition": packet["terminal_disposition"],
        "public_case_scientific_disposition": packet["scientific_disposition"],
        "source_science_review_status": packet["source_science_review_status"],
        "active_rule_instances": matching,
        "application_status": "PRESENT_IN_PUBLIC_CASE" if matching else "NOT_SELECTED_IN_PUBLIC_CASE",
    }
    application["reviewed_target"] = _reviewed_target(
        application, str(entry["evaluation_contract"]["target_kind"])
    )
    return application


def _f04_case_application(case_dir: Path, entry: Mapping[str, Any]) -> dict[str, Any]:
    packet = _read_json(case_dir / "human_decision_packet.json")
    application = {
        "case_id": packet["case_id"],
        "case_directory": case_dir.name,
        "public_case_terminal_disposition": packet["terminal_disposition"],
        "public_case_scientific_disposition": packet["scientific_disposition"],
        "source_science_review_status": packet["source_science_review_status"],
        "application_status": "NOT_SELECTED_IN_PUBLIC_CASE",
        "active_rule_instances": [],
    }
    control = packet.get("existing_exact_hsp90_control_regression")
    if isinstance(control, dict) and control.get("exact_control_rule_instance_id"):
        application.update(
            {
                "application_status": "SEPARATE_EXACT_CONTROL_REGRESSION_ONLY",
                "exact_control_rule_instance_id": control["exact_control_rule_instance_id"],
                "exact_control_rule_effect": control.get("exact_control_rule_effect"),
                "public_case_rule_effect": control.get("public_case_rule_effect"),
                "boundary": control.get("boundary"),
            }
        )
    application["reviewed_target"] = _reviewed_target(
        application, str(entry["evaluation_contract"]["target_kind"])
    )
    return application


def _reviewer_form_schema() -> dict[str, Any]:
    nonempty_string = {"type": "string", "minLength": 1, "pattern": r".*\S.*"}
    nullable_string = {"anyOf": [{"type": "null"}, nonempty_string]}
    nullable_date = {
        "anyOf": [
            {"type": "null"},
            {
                "type": "string",
                "format": "date",
                "pattern": r"^\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])$",
            },
        ]
    }
    nullable_disposition = {
        "type": ["string", "null"],
        "enum": [None, *REVIEW_DISPOSITIONS],
    }
    reviewed_target_properties = {
        "target_kind": {"type": "string", "minLength": 1},
        "target_ids": {"type": "array", "items": {"type": "string"}, "uniqueItems": True},
        "rule_instance_ids": {
            "type": "array",
            "items": {"type": "string"},
            "uniqueItems": True,
        },
    }
    case_disposition_properties = {
        "case_id": {"type": "string", "minLength": 1},
        "reviewed_target": {
            "type": "object",
            "required": list(reviewed_target_properties),
            "properties": reviewed_target_properties,
            "additionalProperties": False,
        },
        "disposition": nullable_disposition,
    }
    item_properties = {
        "review_item_id": {"type": "string"},
        "reviewer_name": nullable_string,
        "reviewer_role": nullable_string,
        "review_date": nullable_date,
        "passage_checked": nullable_string,
        "rule_disposition": nullable_disposition,
        "case_application_dispositions": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "object",
                "required": list(case_disposition_properties),
                "properties": case_disposition_properties,
                "additionalProperties": False,
            },
        },
        "required_revision": nullable_string,
        "allowed_scope": nullable_string,
        "claim_ceiling": nullable_string,
        "supporting_note": nullable_string,
    }
    completion_fields = (
        "reviewer_name",
        "reviewer_role",
        "review_date",
        "passage_checked",
        "allowed_scope",
        "claim_ceiling",
        "supporting_note",
    )
    completion_properties = {field: nonempty_string for field in completion_fields}
    completion_properties["review_date"] = {
        "type": "string",
        "format": "date",
        "pattern": r"^\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])$",
    }
    positive_completion = {"properties": completion_properties}
    item_conditions = [
        {
            "if": {
                "properties": {"rule_disposition": {"enum": list(POSITIVE_REVIEW_DISPOSITIONS)}},
                "required": ["rule_disposition"],
            },
            "then": positive_completion,
        },
        {
            "if": {
                "properties": {
                    "case_application_dispositions": {
                        "contains": {
                            "type": "object",
                            "properties": {
                                "disposition": {"enum": list(POSITIVE_REVIEW_DISPOSITIONS)}
                            },
                            "required": ["disposition"],
                        }
                    }
                }
            },
            "then": positive_completion,
        },
        {
            "if": {
                "properties": {
                    "rule_disposition": {"const": "APPROVE_WITH_BOUNDED_REVISION"}
                },
                "required": ["rule_disposition"],
            },
            "then": {"properties": {"required_revision": nonempty_string}},
        },
        {
            "if": {
                "properties": {
                    "case_application_dispositions": {
                        "contains": {
                            "type": "object",
                            "properties": {
                                "disposition": {"const": "APPROVE_WITH_BOUNDED_REVISION"}
                            },
                            "required": ["disposition"],
                        }
                    }
                }
            },
            "then": {"properties": {"required_revision": nonempty_string}},
        },
        {
            "if": {
                "properties": {"review_item_id": {"const": "NDSR-F04R02"}},
                "required": ["review_item_id"],
            },
            "then": {
                "properties": {
                    "rule_disposition": {"not": {"enum": list(POSITIVE_REVIEW_DISPOSITIONS)}},
                    "case_application_dispositions": {
                        "items": {
                            "properties": {
                                "disposition": {
                                    "not": {"enum": list(POSITIVE_REVIEW_DISPOSITIONS)}
                                }
                            }
                        }
                    },
                }
            },
        },
    ]
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "source-science-reviewer-form/v2",
        "title": "Dynamics Atlas named source-science review form",
        "type": "object",
        "required": [
            "schema_version",
            "review_status",
            "allowed_dispositions",
            "instructions",
            "items",
        ],
        "properties": {
            "schema_version": {"const": "source-science-reviewer-form/v2"},
            "review_status": {"enum": list(REVIEW_FORM_STATUSES)},
            "allowed_dispositions": {"type": "array", "const": list(REVIEW_DISPOSITIONS)},
            "instructions": {"type": "string", "minLength": 1},
            "items": {
                "type": "array",
                "minItems": 1,
                "items": {
                    "type": "object",
                    "required": list(item_properties),
                    "properties": item_properties,
                    "allOf": item_conditions,
                    "additionalProperties": False,
                },
            },
        },
        "allOf": [
            {
                "if": {
                    "properties": {"review_status": {"const": "COMPLETED"}},
                    "required": ["review_status"],
                },
                "then": {
                    "properties": {
                        "items": {
                            "items": {
                                "properties": {
                                    **completion_properties,
                                    "rule_disposition": {"enum": list(REVIEW_DISPOSITIONS)},
                                    "case_application_dispositions": {
                                        "items": {
                                            "properties": {
                                                "disposition": {"enum": list(REVIEW_DISPOSITIONS)}
                                            }
                                        }
                                    },
                                }
                            }
                        }
                    }
                },
            }
        ],
        "additionalProperties": False,
    }


def _reviewed_target(application: Mapping[str, Any], target_kind: str) -> dict[str, Any]:
    rule_instance_ids: list[str] = []
    target_ids: list[str] = []
    for result in application.get("active_rule_instances", []):
        if not isinstance(result, Mapping):
            continue
        rule_id = result.get("rule_instance_id")
        if isinstance(rule_id, str):
            rule_instance_ids.append(rule_id)
        target = result.get("target")
        if isinstance(target, Mapping) and isinstance(target.get("id"), str):
            target_ids.append(str(target["id"]))
    exact_rule_id = application.get("exact_control_rule_instance_id")
    if isinstance(exact_rule_id, str):
        rule_instance_ids.append(exact_rule_id)
        parts = exact_rule_id.split("::", 2)
        if len(parts) == 3:
            target_ids.append(parts[2])
    return {
        "target_kind": target_kind,
        "target_ids": sorted(set(target_ids)),
        "rule_instance_ids": sorted(set(rule_instance_ids)),
    }


def validate_source_science_review_form(
    form: Mapping[str, Any], matrix: Mapping[str, Any]
) -> None:
    """Validate review identity, completion state, and exact matrix coverage."""

    status = form.get("review_status")
    if status not in REVIEW_FORM_STATUSES:
        raise ReviewConsoleError("REVIEW_FORM_STATUS_INVALID")
    form_items = form.get("items")
    matrix_items = matrix.get("items")
    if not isinstance(form_items, list) or not isinstance(matrix_items, list):
        raise ReviewConsoleError("REVIEW_FORM_AND_MATRIX_ITEMS_REQUIRED")
    matrix_by_id = {
        str(item["review_item_id"]): item
        for item in matrix_items
        if isinstance(item, Mapping) and isinstance(item.get("review_item_id"), str)
    }
    form_by_id = {
        str(item["review_item_id"]): item
        for item in form_items
        if isinstance(item, Mapping) and isinstance(item.get("review_item_id"), str)
    }
    if len(matrix_by_id) != len(matrix_items):
        raise ReviewConsoleError("MATRIX_REVIEW_ITEM_IDS_INVALID")
    if len(form_by_id) != len(form_items):
        raise ReviewConsoleError("FORM_REVIEW_ITEM_IDS_INVALID")
    missing = sorted(set(matrix_by_id) - set(form_by_id))
    unknown = sorted(set(form_by_id) - set(matrix_by_id))
    if missing:
        raise ReviewConsoleError(f"FORM_CASE_COVERAGE_MISSING:{','.join(missing)}")
    if unknown:
        raise ReviewConsoleError(f"FORM_REVIEW_ITEM_UNKNOWN:{','.join(unknown)}")

    for item_id, raw_form_item in form_by_id.items():
        form_item = _require_mapping(raw_form_item, f"form.{item_id}")
        matrix_item = _require_mapping(matrix_by_id[item_id], f"matrix.{item_id}")
        applications = matrix_item.get("case_applications")
        records = form_item.get("case_application_dispositions")
        if not isinstance(applications, list) or not isinstance(records, list):
            raise ReviewConsoleError(f"CASE_DISPOSITION_RECORDS_REQUIRED:{item_id}")
        expected_by_case = {
            str(application["case_id"]): {
                "case_id": str(application["case_id"]),
                "reviewed_target": _reviewed_target(
                    _require_mapping(application, f"matrix.{item_id}.application"),
                    str(matrix_item["target_kind"]),
                ),
            }
            for application in applications
            if isinstance(application, Mapping) and isinstance(application.get("case_id"), str)
        }
        records_by_case = {
            str(record["case_id"]): record
            for record in records
            if isinstance(record, Mapping) and isinstance(record.get("case_id"), str)
        }
        if len(records_by_case) != len(records):
            raise ReviewConsoleError(f"CASE_DISPOSITION_CASE_IDS_INVALID:{item_id}")
        if set(records_by_case) != set(expected_by_case):
            raise ReviewConsoleError(f"CASE_DISPOSITION_COVERAGE_MISMATCH:{item_id}")
        dispositions = [form_item.get("rule_disposition")]
        for case_id, expected in expected_by_case.items():
            record = _require_mapping(records_by_case[case_id], f"form.{item_id}.{case_id}")
            if record.get("reviewed_target") != expected["reviewed_target"]:
                raise ReviewConsoleError(f"CASE_DISPOSITION_RULE_INSTANCE_MISMATCH:{item_id}:{case_id}")
            disposition = record.get("disposition")
            if disposition not in (None, *REVIEW_DISPOSITIONS):
                raise ReviewConsoleError(f"CASE_DISPOSITION_INVALID:{item_id}:{case_id}")
            dispositions.append(disposition)

        rule_disposition = form_item.get("rule_disposition")
        if rule_disposition not in (None, *REVIEW_DISPOSITIONS):
            raise ReviewConsoleError(f"RULE_DISPOSITION_INVALID:{item_id}")
        positive = any(value in POSITIVE_REVIEW_DISPOSITIONS for value in dispositions)
        completed = status == "COMPLETED"
        required_fields = (
            "reviewer_name",
            "reviewer_role",
            "review_date",
            "passage_checked",
            "allowed_scope",
            "claim_ceiling",
            "supporting_note",
        )
        if positive or completed:
            for field in required_fields:
                value = form_item.get(field)
                if not isinstance(value, str) or not value.strip():
                    raise ReviewConsoleError(f"COMPLETED_REVIEW_FIELD_REQUIRED:{item_id}:{field}")
            try:
                parsed_date = date.fromisoformat(str(form_item["review_date"]))
            except ValueError as error:
                raise ReviewConsoleError(f"REVIEW_DATE_ISO_REQUIRED:{item_id}") from error
            if parsed_date.isoformat() != form_item["review_date"]:
                raise ReviewConsoleError(f"REVIEW_DATE_ISO_REQUIRED:{item_id}")
        if completed and any(value is None for value in dispositions):
            raise ReviewConsoleError(f"COMPLETED_REVIEW_DISPOSITION_REQUIRED:{item_id}")
        if item_id == "NDSR-F04R02" and positive:
            raise ReviewConsoleError("F04_POSITIVE_DISPOSITION_BLOCKED_BY_TRACEABILITY")
        if "APPROVE_WITH_BOUNDED_REVISION" in dispositions:
            revision = form_item.get("required_revision")
            if not isinstance(revision, str) or not revision.strip():
                raise ReviewConsoleError(f"BOUNDED_REVISION_TEXT_REQUIRED:{item_id}")


def _require_mapping(value: Any, label: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ReviewConsoleError(f"MAPPING_REQUIRED:{label}")
    return value


def _workspace_readme() -> str:
    return """# Dynamics Atlas source-science review workspace

This directory prepares the narrow F01/F02/F03/F04/F06 human/domain review required
after the merged exposed development capsule. It is an evidence map and blank review
form, not a new Rules authority and not a scientific decision.

## What a reviewer should inspect

For every row in `source_passage_index.json` and `case_application_matrix.json`:

1. Open the recorded locator and check the primary passage or case-bound artifact.
2. Decide whether the stated atomic claim supports only the stated reusable use.
3. Check whether the listed HSP90 or ADK application stays inside its claim ceiling.
4. Copy `reviewer_form.json` to a local working file. Keep `review_status` as `DRAFT`
   while any item or case record is incomplete.
5. Record dispositions separately for the reusable Rule question and for each exact
   `case_id` + reviewed target/RuleInstance record. Set `COMPLETED` only after all
   records have a named reviewer, role, ISO date, checked passage, allowed scope,
   claim ceiling, and supporting note.

`F04R02_SOURCE_DECLARED_TIME_ANATOMY_CONTROL` has
`PENDING_SOURCE_TRACEABILITY_MAPPING`. The overlay-required packet labels do not map
to repository records keyed by those labels. A positive F04 disposition is invalid
until a human resolves that mapping; the existing record remains an exact-control
regression with `NO_ACTIVE_RULE_EFFECT` on the public HSP90 case.

## Allowed dispositions

- `APPROVE_AS_WRITTEN`
- `APPROVE_WITH_BOUNDED_REVISION`
- `DEFER_INSUFFICIENT_SOURCE_GROUNDING`
- `REJECT_NOT_REUSABLE`
- `NOT_APPLICABLE_TO_CURRENT_CASE`

A positive disposition requires nonempty reviewer identity, role, ISO review date,
checked passage, allowed scope, claim ceiling, and supporting note. It does not
activate a Rule, Resolution Policy, Evaluation Contract, Operator, or scientific claim.
A later human/project decision must explicitly select any allowed next action.

## Local review-template export

The committed `reviewer_form.json` is a blank local template. Copy it to an untracked
working file before editing. The static console links to the template but has no form,
save endpoint, or scientific-state mutation path. Validate any completed record against
`reviewer_form.schema.json` and the exact case-application matrix before treating it as
a review record.

## Regeneration

Run from the repository root:

```bash
PYTHONPATH=src python scripts/build_source_science_review_workspace_v1.py \\
  --output-dir review/source_science_v1
```

To render the companion read-only trace:

```bash
PYTHONPATH=src python scripts/render_review_console_v0.py \\
  --status governance/current_execution_status.json \\
  --capsule-root evidence/paper_blind_exposed_v1/development_runs/exposed_paper_blind_scientific_decision_capsule_v1 \\
  --review-workspace review/source_science_v1 \\
  --output-dir review_console
```

The resulting `review_console/index.html` is local and static. It contains no mutation
endpoint, credential handling, model call, operator execution, or database.

View the generated workbench with the standard-library static file server:

```bash
python3 -m http.server 8000 --directory review_console
```

Then open `http://127.0.0.1:8000/`. The server exposes files only; it does not add an
execution, review-save, or scientific-state mutation endpoint.
"""


def build_source_science_review_workspace(
    *,
    output_dir: Path,
    capsule_root: Path = DEFAULT_CAPSULE_ROOT,
) -> dict[str, Any]:
    """Build the fixed Delivery A review workspace from existing repository evidence."""

    narrow_packet = _read_json(NARROW_REVIEW_PACKET_PATH)
    source_packets = _read_jsonl(SOURCE_PACKET_PATH)
    packets_by_id = {str(packet["evidence_packet_id"]): packet for packet in source_packets}
    bindings = _read_json(RULES_ROOT / "applicability_bindings_v1.json")["bindings"]
    contracts = _read_json(RULES_ROOT / "evaluation_contracts_v1.json")["contracts"]
    policies = _read_json(RULES_ROOT / "resolution_policies_v1.json")["policies"]
    runtime_subrules_registry = _read_json(RULES_ROOT / "runtime_subrules_v1.json")
    family_overlay_registry = _read_json(RULES_ROOT / "family_overlay_v1.json")
    f04_overlay = _read_json(F04R02_OVERLAY_PATH)
    bindings_by_subrule = {str(item["runtime_subrule_id"]): item for item in bindings}
    contracts_by_subrule = {str(item["runtime_subrule_id"]): item for item in contracts}
    policies_by_id = {str(item["resolution_policy_id"]): item for item in policies}
    runtime_subrules_by_id = {
        str(item["runtime_subrule_id"]): item
        for item in runtime_subrules_registry["runtime_subrules"]
    }
    family_overlay_by_id = {
        str(item["family_id"]): item for item in family_overlay_registry["families"]
    }
    review_items = narrow_packet.get("review_items")
    if not isinstance(review_items, list) or not review_items:
        raise ReviewConsoleError("NARROW_REVIEW_ITEMS_REQUIRED")

    source_entries = [
        _source_entry(
            item=item,
            packets_by_id=packets_by_id,
            bindings_by_subrule=bindings_by_subrule,
            contracts_by_subrule=contracts_by_subrule,
            policies_by_id=policies_by_id,
            runtime_subrules_by_id=runtime_subrules_by_id,
            runtime_subrules_registry_status=str(runtime_subrules_registry["status"]),
            family_overlay_by_id=family_overlay_by_id,
            family_overlay_registry_status=str(family_overlay_registry["status"]),
            f04_overlay=f04_overlay,
        )
        for item in review_items
    ]
    if len({entry["review_item_id"] for entry in source_entries}) != len(source_entries):
        raise ReviewConsoleError("DUPLICATE_REVIEW_ITEM_ID")
    case_dirs = _case_directories(capsule_root)
    matrix_items = []
    for entry in source_entries:
        if entry["runtime_subrule_id"] == "F04R02_SOURCE_DECLARED_TIME_ANATOMY_CONTROL":
            applications = [_f04_case_application(case_dir, entry) for case_dir in case_dirs]
        else:
            applications = [_case_application(case_dir=case_dir, entry=entry) for case_dir in case_dirs]
        matrix_items.append(
            {
                "review_item_id": entry["review_item_id"],
                "family_id": entry["family_id"],
                "runtime_subrule_id": entry["runtime_subrule_id"],
                "target_kind": entry["evaluation_contract"]["target_kind"],
                "exact_applicability_predicate": {
                    "binding_id": entry["binding"]["binding_id"],
                    "predicate": entry["binding"]["applicability"],
                },
                "required_evidence": entry["binding"]["required_evidence_paths"],
                "resolution_policy": entry["resolution_policy"],
                "evaluation_contract": entry["evaluation_contract"],
                "claim_ceiling": entry["claim_ceiling"],
                "forbidden_generalization": entry["forbidden_generalization"],
                "case_applications": applications,
                "current_status": "PENDING_DOMAIN_REVIEW",
            }
        )

    source_index = {
        "schema_version": "source-science-passage-index/v1",
        "workspace_status": "PENDING_DOMAIN_REVIEW",
        "purpose": "Index narrow reusable-use evidence for named human/domain review; primary-passage checking remains a human action.",
        "entries": source_entries,
    }
    application_matrix = {
        "schema_version": "source-science-case-application-matrix/v1",
        "workspace_status": "PENDING_DOMAIN_REVIEW",
        "purpose": "Show the exact current Rule binding, contract, policy, claim ceiling, and exposed-case application without changing runtime authority.",
        "items": matrix_items,
    }
    form = {
        "schema_version": "source-science-reviewer-form/v2",
        "review_status": "DRAFT",
        "allowed_dispositions": list(REVIEW_DISPOSITIONS),
        "instructions": (
            "This local DRAFT is non-authoritative. Only a named human/domain reviewer "
            "may set COMPLETED after checking every referenced passage or case-bound "
            "artifact. Positive dispositions require identity, ISO review date, checked "
            "passage, allowed scope, claim ceiling, and supporting note. F04R02 cannot "
            "receive a positive disposition while traceability remains pending."
        ),
        "items": [
            {
                "review_item_id": matrix_item["review_item_id"],
                "reviewer_name": None,
                "reviewer_role": None,
                "review_date": None,
                "passage_checked": None,
                "rule_disposition": None,
                "case_application_dispositions": [
                    {
                        "case_id": application["case_id"],
                        "reviewed_target": application["reviewed_target"],
                        "disposition": None,
                    }
                    for application in matrix_item["case_applications"]
                ],
                "required_revision": None,
                "allowed_scope": None,
                "claim_ceiling": None,
                "supporting_note": None,
            }
            for matrix_item in matrix_items
        ],
    }
    validate_source_science_review_form(form, application_matrix)

    output_dir.mkdir(parents=True, exist_ok=True)
    _write_json(output_dir / "source_passage_index.json", source_index)
    _write_json(output_dir / "case_application_matrix.json", application_matrix)
    _write_json(output_dir / "reviewer_form.json", form)
    _write_json(output_dir / "reviewer_form.schema.json", _reviewer_form_schema())
    (output_dir / "README.md").write_text(_workspace_readme(), encoding="utf-8")
    return {
        "workspace": str(output_dir),
        "review_item_count": len(source_entries),
        "case_count": len(case_dirs),
        "status": "PENDING_DOMAIN_REVIEW",
    }


def _escape(value: Any) -> str:
    return html.escape(str(value), quote=True)


def _json(value: Any) -> str:
    return _escape(json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False))


def _badge(value: Any) -> str:
    label = _escape(value)
    token = re.sub(r"[^a-z0-9]+", "-", str(value).lower()).strip("-")
    return f'<span class="badge badge-{token}">{label}</span>'


def _linkify(value: Any) -> str:
    text = str(value)
    chunks: list[str] = []
    last = 0
    for match in _URL_PATTERN.finditer(text):
        chunks.append(_escape(text[last : match.start()]))
        raw_url = match.group(0)
        url = raw_url.rstrip(".,;:")
        chunks.append(f'<a href="{_escape(url)}">{_escape(url)}</a>')
        chunks.append(_escape(raw_url[len(url) :]))
        last = match.end()
    chunks.append(_escape(text[last:]))
    return "".join(chunks)


def _list(items: Sequence[Any], *, empty: str = "None recorded.") -> str:
    if not items:
        return f'<p class="muted">{_escape(empty)}</p>'
    return "<ul>" + "".join(f"<li>{_linkify(item)}</li>" for item in items) + "</ul>"


def _details(label: str, value: Any, *, open_by_default: bool = False) -> str:
    open_attr = " open" if open_by_default else ""
    return (
        f"<details{open_attr}><summary>{_escape(label)}</summary>"
        f'<pre>{_json(value)}</pre></details>'
    )


def _render_source(source: Mapping[str, Any]) -> str:
    permitted = source.get("permitted_facts", [])
    excluded = source.get("excluded_sections", [])
    return f"""
    <article class="source-card">
      <div class="source-heading"><code>{_escape(source.get('source_id', 'UNKNOWN_SOURCE'))}</code>{_badge(source.get('source_kind', 'UNKNOWN'))}</div>
      <p class="locator">{_linkify(source.get('source_locator', 'UNKNOWN locator'))}</p>
      <h4>Declared facts</h4>{_list(permitted, empty='No declared facts.')}
      <h4>Excluded or unresolved context</h4>{_list(excluded, empty='No exclusions recorded.')}
    </article>
    """


def _render_rule(result: Mapping[str, Any], matrix_by_subrule: Mapping[str, Mapping[str, Any]]) -> str:
    subrule = _canonical_subrule_id(str(result.get("runtime_subrule_id", "UNKNOWN")))
    matrix = matrix_by_subrule.get(subrule)
    extra = ""
    if matrix is not None:
        extra = (
            f"<p><strong>Review target:</strong> {_escape(matrix['target_kind'])} · "
            f"<strong>Policy:</strong> <code>{_escape(matrix['resolution_policy']['resolution_policy_id'])}</code></p>"
        )
    return f"""
    <article class="rule-card">
      <div class="rule-heading"><code>{_escape(result.get('rule_instance_id', 'UNKNOWN_RULE_INSTANCE'))}</code>{_badge(result.get('status', 'UNKNOWN'))}</div>
      <p><strong>Target:</strong> {_escape(result.get('target', {}).get('kind', 'UNKNOWN'))} / <code>{_escape(result.get('target', {}).get('id', 'UNKNOWN'))}</code></p>
      <p><strong>Reasons:</strong> {_escape(', '.join(result.get('reason_codes', [])) or 'None recorded')}</p>
      {extra}
    </article>
    """


def _render_evidence(evidence: Mapping[str, Any]) -> str:
    result = evidence.get("descriptive_result", evidence)
    provenance = result.get("method_provenance", {}) if isinstance(result, dict) else {}
    capability = result.get("capability_kind", evidence.get("card_id", "DESCRIPTIVE_EVIDENCE")) if isinstance(result, dict) else evidence.get("card_id", "DESCRIPTIVE_EVIDENCE")
    limitations = result.get("limitation") if isinstance(result, dict) else None
    forbidden = result.get("forbidden_claims", []) if isinstance(result, dict) else []
    return f"""
    <article class="evidence-card">
      <div class="evidence-heading"><code>{_escape(capability)}</code>{_badge('NO_ACTIVE_RULE_EFFECT')}</div>
      <p><strong>Addresses:</strong> <code>{_escape(evidence.get('addresses_ref', 'NOT_RECORDED'))}</code></p>
      <p><strong>Package / function:</strong> {_escape(provenance.get('package', 'NOT_RECORDED'))} / {_escape(provenance.get('function', 'NOT_RECORDED'))}</p>
      <p><strong>Claim ceiling:</strong> {_escape(result.get('claim_ceiling', evidence.get('claim_ceiling', 'NOT_RECORDED')))}</p>
      <p><strong>Limitation:</strong> {_escape(limitations or 'NOT_RECORDED')}</p>
      <h4>Forbidden claims</h4>{_list(forbidden, empty='None recorded.')}
      {_details('Full descriptive EvidenceResult', evidence)}
    </article>
    """


def _render_exact_control(control: Mapping[str, Any]) -> str:
    if control.get("availability") == "UNAVAILABLE":
        return (
            '<article class="control-card unavailable-card">'
            f"<div class=\"evidence-heading\"><code>EXISTING_EXACT_CONTROL_REGRESSION</code>{_badge('UNAVAILABLE')}</div>"
            f"<p>{_escape(control.get('reason', 'No exact-control artifact is recorded.'))}</p>"
            "</article>"
        )
    if control.get("status") == "NOT_RUN_IN_THIS_CAPSULE_INVOCATION":
        return '<p class="muted">No exact HSP90 control regression belongs to this case.</p>'
    return f"""
    <article class="control-card">
      <div class="evidence-heading"><code>EXISTING_EXACT_CONTROL_REGRESSION</code>{_badge(control.get('exact_control_rule_effect', 'UNKNOWN'))}</div>
      <p><strong>Exact control rule:</strong> <code>{_escape(control.get('exact_control_rule_instance_id', 'NOT_RECORDED'))}</code></p>
      <p><strong>Public case effect:</strong> {_badge(control.get('public_case_rule_effect', 'UNKNOWN'))}</p>
      <p>{_escape(control.get('boundary', 'No boundary text recorded.'))}</p>
      {_details('Exact control trace', control)}
    </article>
    """


def _render_active_evidence(evidence: Mapping[str, Any]) -> str:
    return f"""
    <article class="evidence-card active-evidence-card">
      <div class="evidence-heading"><code>{_escape(evidence.get('evidence_result_id', evidence.get('card_id', 'ACTIVE_RULE_EVIDENCE')))}</code>{_badge('ACTIVE_RULE_EVIDENCE')}</div>
      <p><strong>Affected RuleInstance:</strong> <code>{_escape(evidence.get('affected_rule_instance_id', 'NOT_RECORDED'))}</code></p>
      {_details('Full active-Rule EvidenceResult', evidence)}
    </article>
    """


def _render_optional(label: str, value: Any, *, open_by_default: bool = False) -> str:
    if isinstance(value, Mapping) and value.get("availability") == "UNAVAILABLE":
        return (
            '<article class="unavailable-card">'
            f"<div class=\"evidence-heading\"><code>{_escape(label)}</code>{_badge('UNAVAILABLE')}</div>"
            f"<p>{_escape(value.get('reason', 'Optional artifact unavailable.'))}</p>"
            "</article>"
        )
    return _details(label, value, open_by_default=open_by_default)


def _render_case_overview(view: CaseView) -> str:
    sources = view.sources_and_locators
    if isinstance(sources, Sequence) and not isinstance(sources, (str, bytes)):
        source_html = "".join(
            _render_source(source)
            for source in sources
            if isinstance(source, Mapping)
        )
    else:
        source_html = _render_optional("SOURCES_AND_LOCATORS", sources)
    return f"""
    <article class="case-section case-overview" id="overview-{_escape(view.artifact_root_name)}">
      <div class="case-kicker">{_escape(view.artifact_kind)} · {_escape(view.artifact_root_name.upper())}</div>
      <h2>{_escape(view.case_id)}</h2>
      <p class="question">{_escape(view.question)}</p>
      <div class="status-strip">
        <div><span>Artifact integrity</span>{_badge(view.integrity_status)}</div>
        <div><span>Current gate</span>{_badge(view.current_gate)}</div>
        <div><span>Recorded terminal state</span>{_badge(view.terminal_scientific_state)}</div>
      </div>
      <div class="two-column">
        <div><h3>Sources and locators</h3>{source_html}</div>
        <div>
          <h3>Authority boundary</h3>
          <p>{_escape(view.boundary)}</p>
          {_details('Claim ceiling', view.claim_ceiling, open_by_default=True)}
          {_details('AGENT_PROPOSAL', view.agent_proposal)}
          {_details('PLATFORM_ADMITTED_FACT', view.admitted_facts)}
        </div>
      </div>
    </article>
    """


def _render_case_trace(
    view: CaseView, matrix_by_subrule: Mapping[str, Mapping[str, Any]]
) -> str:
    descriptive = "".join(
        _render_evidence(item)
        for item in view.descriptive_evidence_no_active_rule_effect
    ) or '<p class="muted">No descriptive evidence recorded.</p>'
    active = "".join(_render_active_evidence(item) for item in view.active_rule_evidence)
    if not active:
        active = (
            '<p class="muted">No broad public-case ACTIVE_RULE_EVIDENCE is recorded. '
            "No active RuleResult update.</p>"
        )
    unresolved = [
        {
            "ref": item.get("ref", item.get("development_obligation_ref", "UNKNOWN")),
            "status": item.get("status", "UNKNOWN"),
            "reason_codes": item.get("reason_codes", []),
        }
        for item in view.unresolved_obligations
        if isinstance(item, Mapping)
    ]
    return f"""
    <article class="case-section trace-case" id="trace-{_escape(view.artifact_root_name)}">
      <div class="case-kicker">SOURCE → RULE → EVIDENCE TRACE</div>
      <h2>{_escape(view.case_id)}</h2>
      <h3>RULE_RESULT</h3>
      <p class="muted">UNKNOWN / unresolved is preserved verbatim. The workbench does not infer a replacement value.</p>
      <div class="card-grid">{''.join(_render_rule(rule, matrix_by_subrule) for rule in view.rule_results)}</div>
      <div class="two-column">
        <div>{_details('RuleInstances', view.rule_instances, open_by_default=True)}{_details('Unresolved obligations', unresolved, open_by_default=True)}</div>
        <div>{_details('Fresh legal action cards', view.legal_action_cards, open_by_default=True)}{_details('Planner AGENT_PROPOSAL', view.planner_proposal)}{_details('Deterministic authorization', view.authorization)}</div>
      </div>
      <h3>Evidence lanes</h3>
      <div class="evidence-lanes">
        <div><h4>DESCRIPTIVE_EVIDENCE_NO_ACTIVE_RULE_EFFECT</h4>{descriptive}</div>
        <div><h4>ACTIVE_RULE_EVIDENCE</h4>{active}</div>
        <div><h4>EXISTING_EXACT_CONTROL_REGRESSION</h4>{_render_exact_control(view.exact_control_regression)}</div>
      </div>
    </article>
    """


def _render_case_conclusion(view: CaseView) -> str:
    return f"""
    <article class="case-section conclusion-case" id="conclusion-{_escape(view.artifact_root_name)}">
      <div class="case-kicker">CONCLUSION AND PROVENANCE</div>
      <h2>{_escape(view.case_id)}</h2>
      <div class="two-column">
        <div>{_render_optional('CONCLUSION_PACKET', view.conclusion_packet, open_by_default=True)}{_render_optional('Before/after same-Rule links', view.before_after_rule_result_links)}</div>
        <div>{_details('Executed actions', view.executed_actions)}{_details('Receipts and provenance', view.receipts, open_by_default=True)}</div>
      </div>
    </article>
    """


def _render_case_human_review(view: CaseView) -> str:
    return f"""
    <article class="human-case-card">
      <div class="review-heading"><code>{_escape(view.case_id)}</code>{_badge(view.current_gate)}</div>
      {_details('HUMAN_REVIEW state', view.human_review_state, open_by_default=True)}
    </article>
    """


def _render_case(
    *,
    case_dir: Path,
    matrix_by_subrule: Mapping[str, Mapping[str, Any]],
) -> str:
    packet = _read_json(case_dir / "human_decision_packet.json")
    visible = _read_json(case_dir / "agent_visible_input.json")
    planner_input = _read_json(case_dir / "planner_visible_input.json")
    planner_admission = _read_json(case_dir / "planner_proposal_admission.json")
    selected = _read_json(case_dir / "arm_c_selected_public_actions.json")
    rules = packet.get("active_rule_results", [])
    evidence = packet.get("descriptive_evidence_results_no_active_rule_effect", [])
    sources = visible.get("source_materials", [])
    resolution = packet.get("resolution_options", [])
    return f"""
    <section class="case-section" id="{_escape(case_dir.name)}">
      <div class="case-kicker">EXPOSED DEVELOPMENT CASE · {_escape(case_dir.name.upper())}</div>
      <h2>{_escape(packet['case_id'])}</h2>
      <p class="question">{_escape(packet['requested_claim'])}</p>
      <div class="status-strip">
        <div><span>Terminal disposition</span>{_badge(packet['terminal_disposition'])}</div>
        <div><span>Scientific disposition</span>{_badge(packet['scientific_disposition'])}</div>
        <div><span>Source-science status</span>{_badge(packet['source_science_review_status'])}</div>
      </div>

      <div class="two-column">
        <div>
          <h3>Evidence sources</h3>
          {''.join(_render_source(source) for source in sources)}
        </div>
        <div>
          <h3>Decision boundary</h3>
          <h4>Human review items</h4>{_list(packet.get('human_review_items', []))}
          <h4>Forbidden claims</h4>{_list(packet.get('forbidden_claims', []))}
          <h4>Blocking unresolved RuleInstances</h4>{_list(packet.get('blocking_unresolved_rule_instances', []))}
        </div>
      </div>

      <h3>Rules</h3>
      <p class="muted">UNRESOLVED means the repository preserves an explicit UNKNOWN / unresolved state; it is not an invitation to infer a result.</p>
      <div class="card-grid">{''.join(_render_rule(rule, matrix_by_subrule) for rule in rules)}</div>

      <h3>Planner and authorization</h3>
      <div class="two-column">
        <div>{_details('Fresh unresolved state and legal cards', planner_input, open_by_default=True)}</div>
        <div>{_details('Recorded proposal admission and deterministic authorization', planner_admission, open_by_default=True)}{_details('Selected execution trace', selected)}</div>
      </div>

      <h3>Evidence actions</h3>
      <div class="evidence-lanes">
        <div><h4>DESCRIPTIVE_EVIDENCE_NO_ACTIVE_RULE_EFFECT</h4>{''.join(_render_evidence(item) for item in evidence) or '<p class="muted">No descriptive evidence recorded.</p>'}</div>
        <div><h4>ACTIVE_RULE_EVIDENCE</h4><p class="muted">No broad public-case active-Rule evidence is recorded in this capsule.</p></div>
        <div><h4>EXISTING_EXACT_CONTROL_REGRESSION</h4>{_render_exact_control(packet.get('existing_exact_hsp90_control_regression', {}))}</div>
      </div>

      <h3>Resolution options</h3>
      <div class="card-grid">{''.join(_details(str(item.get('addresses_ref', 'UNRESOLVED_REFERENCE')), item) for item in resolution)}</div>
    </section>
    """


def _render_review_queue(
    source_index: Mapping[str, Any], matrix: Mapping[str, Any], form: Mapping[str, Any]
) -> str:
    form_by_id = {str(item["review_item_id"]): item for item in form["items"]}
    matrix_by_id = {str(item["review_item_id"]): item for item in matrix["items"]}
    cards = []
    for entry in source_index["entries"]:
        item_id = str(entry["review_item_id"])
        matrix_item = matrix_by_id[item_id]
        blank = form_by_id[item_id]
        cards.append(
            f"""
            <article class="review-card">
              <div class="review-heading"><code>{_escape(item_id)}</code>{_badge(entry['reviewer_status'])}</div>
              <p><strong>Family:</strong> {_escape(entry['family_id'])}<br><strong>Runtime subrule:</strong> <code>{_escape(entry['runtime_subrule_id'])}</code></p>
              <p><strong>Locator:</strong> {_linkify(entry['primary_source_locator'])}</p>
              <p><strong>Locator status:</strong> {_escape(entry['primary_locator_status'])}</p>
              <p><strong>Passage kind:</strong> {_escape(entry['passage_kind'])}</p>
              <p><strong>Source packet status:</strong> {_badge(entry['source_packet_status'])}</p>
              <p><strong>Traceability note:</strong> {_escape(entry.get('traceability_note') or 'No separate traceability note recorded.')}</p>
              <p><strong>Short passage:</strong> {_escape(entry['short_source_passage'])}</p>
              <p><strong>Atomic statement:</strong> {_escape(entry['atomic_scientific_statement'])}</p>
              <p><strong>Scientific question:</strong> {_escape(entry['scientific_question'])}</p>
              <p><strong>Runtime claim effect:</strong> {_escape(entry['claim_effect_summary'])}</p>
              <p><strong>Implementation status:</strong> {_badge(entry['implementation_status'])}</p>
              <p><strong>Registry authority:</strong> {_badge(entry['runtime_subrules_registry_status'])}</p>
              <p><strong>Family source grounding:</strong> {_badge(entry['family_overlay']['source_grounding_decision'])} · <strong>Runtime readiness:</strong> {_badge(entry['family_overlay']['runtime_readiness'])}</p>
              <p><strong>Narrow reusable use:</strong> {_escape(entry['proposed_reusable_review_question'])}</p>
              <p><strong>Forbidden generalization:</strong> {_escape(entry['forbidden_generalization'])}</p>
              <p><strong>Claim ceiling:</strong> {_escape(entry['claim_ceiling'])}</p>
              {_details('Exact applicability, evidence, policy, and contract', matrix_item, open_by_default=False)}
              {_details('Blank named-review fields', blank, open_by_default=False)}
            </article>
            """
        )
    return "".join(cards)


def render_review_console(
    *,
    status_path: Path,
    review_workspace: Path,
    output_dir: Path,
    capsule_root: Path = DEFAULT_CAPSULE_ROOT,
    case_roots: Sequence[Path] | None = None,
) -> Path:
    """Render a static HTML review trace without a server, API, or mutation path.

    Explicit ``case_roots`` may point to any mix of CaseView-compatible capsule case
    or ``case_runner_v1`` run directories.  When omitted, the existing
    ``capsule_root`` discovery behavior is preserved.
    """

    status = _read_json(status_path)
    source_index = _read_json(review_workspace / "source_passage_index.json")
    matrix = _read_json(review_workspace / "case_application_matrix.json")
    form = _read_json(review_workspace / "reviewer_form.json")
    form_schema = _read_json(review_workspace / "reviewer_form.schema.json")
    validate_source_science_review_form(form, matrix)
    advisory = _read_json(SOURCE_SCIENCE_ADVISORY_PATH) if SOURCE_SCIENCE_ADVISORY_PATH.is_file() else unavailable(
        "The optional nine-item source-science advisory reconciliation is not present in this checkout."
    )
    matrix_by_subrule = {
        str(item["runtime_subrule_id"]): item for item in matrix.get("items", []) if isinstance(item, dict)
    }
    artifact_roots = list(case_roots) if case_roots else _case_directories(capsule_root)
    case_views = [build_case_view(case_root) for case_root in artifact_roots]
    overview_sections = "".join(_render_case_overview(view) for view in case_views)
    trace_sections = "".join(
        _render_case_trace(view, matrix_by_subrule) for view in case_views
    )
    conclusion_sections = "".join(_render_case_conclusion(view) for view in case_views)
    human_case_sections = "".join(_render_case_human_review(view) for view in case_views)
    queue = _render_review_queue(source_index, matrix, form)
    next_action = status.get("next_allowed_action", {})
    html_document = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Dynamics Atlas · Static engineering workbench</title>
  <style>
    :root {{
      --ink: #16232f;
      --paper: #edf3f5;
      --panel: #ffffff;
      --line: #bdd0d7;
      --teal: #0c6b78;
      --mint: #cce8df;
      --amber: #b06d00;
      --muted: #5a6a73;
      --danger: #8c3845;
      --mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      --serif: Iowan Old Style, Palatino Linotype, Book Antiqua, Georgia, serif;
    }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; background: var(--paper); color: var(--ink); font: 16px/1.5 system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
    a {{ color: var(--teal); overflow-wrap: anywhere; }}
    code, pre {{ font-family: var(--mono); }}
    code {{ font-size: .84em; overflow-wrap: anywhere; }}
    pre {{ white-space: pre-wrap; overflow-wrap: anywhere; font-size: .78rem; background: #f3f7f8; border: 1px solid var(--line); padding: 1rem; border-radius: .4rem; }}
    h1, h2, h3 {{ font-family: var(--serif); line-height: 1.08; }}
    h1 {{ font-size: clamp(2.2rem, 5vw, 4.5rem); margin: .15rem 0 .6rem; letter-spacing: -.04em; }}
    h2 {{ font-size: clamp(1.55rem, 3vw, 2.3rem); margin: .2rem 0 1rem; }}
    h3 {{ font-size: 1.45rem; margin-top: 2.5rem; border-top: 1px solid var(--line); padding-top: 1rem; }}
    h4 {{ margin: .75rem 0 .25rem; font-size: .84rem; text-transform: uppercase; letter-spacing: .08em; color: var(--muted); }}
    p {{ margin: .55rem 0; }}
    ul {{ margin: .45rem 0; padding-left: 1.2rem; }}
    li {{ margin: .22rem 0; }}
    .shell {{ max-width: 1520px; margin: 0 auto; padding: 2rem clamp(1rem, 4vw, 4rem) 5rem; }}
    .view-nav {{ display: flex; flex-wrap: wrap; gap: .55rem; margin: 1rem 0 0; }}
    .view-nav a {{ background: var(--panel); border: 1px solid var(--line); padding: .45rem .7rem; text-decoration: none; font: 700 .72rem/1.2 var(--mono); }}
    .masthead {{ display: grid; grid-template-columns: minmax(0, 1.8fr) minmax(15rem, .8fr); gap: 2rem; padding: 2rem 0 2.4rem; border-bottom: 5px solid var(--ink); }}
    .eyebrow, .case-kicker {{ color: var(--teal); font: 700 .72rem/1.2 var(--mono); letter-spacing: .13em; }}
    .thesis {{ font: 1.18rem/1.45 var(--serif); max-width: 48rem; }}
    .gate-card {{ border-left: 5px solid var(--amber); padding: 1rem 1.2rem; background: #fff9ed; align-self: end; }}
    .gate-card p {{ margin: .4rem 0; }}
    .case-section {{ margin-top: 4rem; }}
    .question {{ max-width: 66rem; font: 1.12rem/1.45 var(--serif); }}
    .status-strip {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: .75rem; margin: 1.25rem 0 1.5rem; }}
    .status-strip > div {{ background: var(--panel); border: 1px solid var(--line); padding: .85rem; min-width: 0; }}
    .status-strip span {{ display: block; color: var(--muted); font-size: .75rem; text-transform: uppercase; letter-spacing: .08em; margin-bottom: .35rem; }}
    .badge {{ display: inline-block; max-width: 100%; overflow-wrap: anywhere; padding: .25rem .45rem; border-radius: .22rem; background: #e4ecee; color: var(--ink); font: 700 .69rem/1.2 var(--mono); }}
    .badge-pending-domain-review, .badge-abstain-or-human-review, .badge-unresolved {{ background: #fff0ce; color: #734900; }}
    .badge-not-evaluated, .badge-no-active-rule-effect {{ background: #dce9f4; color: #234e71; }}
    .badge-pass, .badge-active-rule-effect {{ background: var(--mint); color: #145040; }}
    .two-column {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1rem; }}
    .card-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(18rem, 1fr)); gap: .8rem; }}
    .source-card, .rule-card, .evidence-card, .control-card, .review-card {{ background: var(--panel); border: 1px solid var(--line); padding: 1rem; margin: .75rem 0; box-shadow: 0 1px 0 rgba(22,35,47,.04); }}
    .human-case-card, .unavailable-card, .integrity-example {{ background: var(--panel); border: 1px solid var(--line); padding: 1rem; margin: .75rem 0; }}
    .unavailable-card {{ border-left: 4px solid var(--muted); }}
    .integrity-example {{ border-left: 5px solid var(--danger); background: #fff4f4; }}
    .source-heading, .rule-heading, .evidence-heading, .review-heading {{ display: flex; align-items: flex-start; justify-content: space-between; gap: .75rem; }}
    .locator {{ font-size: .88rem; color: var(--muted); }}
    .muted {{ color: var(--muted); }}
    .evidence-lanes {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1rem; }}
    .evidence-lanes > div {{ border-top: 3px solid var(--teal); padding-top: .5rem; min-width: 0; }}
    details {{ margin: .6rem 0; background: #f9fbfb; border: 1px solid var(--line); padding: .45rem .65rem; }}
    summary {{ cursor: pointer; color: var(--teal); font-weight: 650; }}
    .queue {{ margin-top: 4rem; border-top: 5px solid var(--ink); padding-top: 1.5rem; }}
    .primary-view {{ margin-top: 4rem; border-top: 5px solid var(--ink); padding-top: 1.5rem; }}
    .queue-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(25rem, 1fr)); gap: .9rem; }}
    footer {{ margin-top: 4rem; border-top: 1px solid var(--line); padding-top: 1rem; color: var(--muted); font-size: .85rem; }}
    @media (max-width: 860px) {{ .masthead, .two-column, .evidence-lanes, .status-strip {{ grid-template-columns: 1fr; }} .shell {{ padding: 1rem 1rem 3rem; }} }}
  </style>
</head>
<body>
  <main class="shell">
    <header class="masthead">
      <div>
        <div class="eyebrow">DYNAMICS ATLAS · STATIC READ-ONLY WORKBENCH</div>
        <h1>Case evidence and human review</h1>
        <p class="thesis">Artifact-only CaseViews for the exposed HSP90 and ADK development cases: admitted facts, Rules, separate evidence lanes, recorded conclusions, provenance, and the still-pending named review gate.</p>
        <nav class="view-nav" aria-label="Primary workbench views">
          <a href="#case-overview">1 · Case Overview</a>
          <a href="#trace">2 · Source → Rule → Evidence Trace</a>
          <a href="#conclusion">3 · Conclusion and Provenance</a>
          <a href="#human-review">4 · Human Review</a>
        </nav>
      </div>
      <aside class="gate-card">
        <div class="eyebrow">CURRENT GATE</div>
        <p>{_badge(next_action.get('action', 'NOT_RECORDED'))}</p>
        <p>{_escape(next_action.get('exit_gate', 'No exit condition recorded.'))}</p>
      </aside>
    </header>
    <section class="primary-view" id="case-overview">
      <div class="eyebrow">PRIMARY VIEW 1</div>
      <h1>Case Overview</h1>
      {overview_sections}
    </section>
    <section class="primary-view" id="trace">
      <div class="eyebrow">PRIMARY VIEW 2</div>
      <h1>Source → Rule → Evidence Trace</h1>
      {trace_sections}
    </section>
    <section class="primary-view" id="conclusion">
      <div class="eyebrow">PRIMARY VIEW 3</div>
      <h1>Conclusion and Provenance</h1>
      <p class="question">A recorded ConclusionPacket is displayed as an artifact. A case_runner_v1 run that records NOT_CALCULATED_BY_CASE_RUNNER remains explicitly unavailable rather than receiving a synthetic conclusion.</p>
      {conclusion_sections}
    </section>
    <section class="primary-view queue" id="human-review">
      <div class="eyebrow">PRIMARY VIEW 4</div>
      <h1>Human Review</h1>
      <div class="card-grid">{human_case_sections}</div>
      <div class="two-column">
        <div>{_render_optional('ADVISORY_RECONCILIATION_NOT_OFFICIAL_DISPOSITION', advisory, open_by_default=True)}</div>
        <div>{_details('OFFICIAL_REVIEW_TEMPLATE_BLANK', form, open_by_default=True)}</div>
      </div>
      <p class="muted">The advisory packet is engineering/source-audit preparation only. It cannot populate the separate official named-review identity or disposition fields.</p>
      <div class="eyebrow">NAMED HUMAN / DOMAIN REVIEW QUEUE</div>
      <h2>Primary-passage and application checks</h2>
      <p class="question">Every entry is pending. This view exposes passage kind, source-packet status, traceability, narrow proposed use, registry authority, exact case/RuleInstance keys, and blank reviewer fields. It does not make a disposition.</p>
      <p><a href="reviewer_form.json" download>Export/copy the local DRAFT review template</a> · <a href="reviewer_form.schema.json" download>download its validation schema</a> · the page cannot save or mutate either file.</p>
      <aside class="integrity-example">
        <div class="review-heading"><code>INTEGRITY_ERROR_EXAMPLE</code>{_badge('REQUIRED_ARTIFACT_MISSING')}</div>
        <p>If a required case/run artifact is absent, malformed, cross-case, or stale, <code>build_case_view</code> raises <code>CaseViewIntegrityError</code> and the case is not rendered. This example is a visible fail-closed state, not an active error in HSP90 or ADK.</p>
      </aside>
      <div class="queue-grid">{queue}</div>
    </section>
    <footer>Generated locally from repository artifacts. Static HTML only: no model call, operator execution, API credential, database, mutation endpoint, or scientific approval.</footer>
  </main>
</body>
</html>
"""
    html_document = "\n".join(line.rstrip() for line in html_document.splitlines()) + "\n"
    output_dir.mkdir(parents=True, exist_ok=True)
    _write_json(output_dir / "reviewer_form.json", form)
    _write_json(output_dir / "reviewer_form.schema.json", form_schema)
    output_path = output_dir / "index.html"
    output_path.write_text(html_document, encoding="utf-8")
    return output_path


def _build_main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build the bounded Delivery A source-science workspace.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_REVIEW_WORKSPACE)
    parser.add_argument("--capsule-root", type=Path, default=DEFAULT_CAPSULE_ROOT)
    args = parser.parse_args(argv)
    result = build_source_science_review_workspace(
        output_dir=args.output_dir,
        capsule_root=args.capsule_root,
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


def _render_main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Render the static Dynamics Atlas Review Console v0.")
    parser.add_argument("--status", type=Path, required=True)
    parser.add_argument(
        "--capsule-root",
        type=Path,
        default=DEFAULT_CAPSULE_ROOT,
        help="Capsule parent directory used when no explicit --case-root is supplied.",
    )
    parser.add_argument(
        "--case-root",
        dest="case_roots",
        action="append",
        type=Path,
        help=(
            "Explicit CaseView-compatible capsule case or case-run root. "
            "Repeat to render multiple roots instead of capsule-root discovery."
        ),
    )
    parser.add_argument("--review-workspace", type=Path, default=DEFAULT_REVIEW_WORKSPACE)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args(argv)
    output_path = render_review_console(
        status_path=args.status,
        capsule_root=args.capsule_root,
        case_roots=args.case_roots,
        review_workspace=args.review_workspace,
        output_dir=args.output_dir,
    )
    print(output_path)
    return 0
