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
from pathlib import Path
from typing import Any


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

REVIEW_DISPOSITIONS = (
    "APPROVE_AS_WRITTEN",
    "APPROVE_WITH_BOUNDED_REVISION",
    "DEFER_INSUFFICIENT_SOURCE_GROUNDING",
    "REJECT_NOT_REUSABLE",
    "NOT_APPLICABLE_TO_CURRENT_CASE",
)

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
            "source_packet_status": item["source_packet_status"],
            "traceability_note": item.get("traceability_note"),
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
    return {
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
        "binding": dict(binding),
        "evaluation_contract": _compact_contract(contract),
        "resolution_policy": _compact_policy(policy),
        "claim_ceiling": packet["forbidden_generalization"],
        "reviewer_status": "PENDING_DOMAIN_REVIEW",
    }


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
    return {
        "case_id": packet["case_id"],
        "case_directory": case_dir.name,
        "public_case_terminal_disposition": packet["terminal_disposition"],
        "public_case_scientific_disposition": packet["scientific_disposition"],
        "source_science_review_status": packet["source_science_review_status"],
        "active_rule_instances": matching,
        "application_status": "PRESENT_IN_PUBLIC_CASE" if matching else "NOT_SELECTED_IN_PUBLIC_CASE",
    }


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
    return application


def _reviewer_form_schema() -> dict[str, Any]:
    nullable_string = {"type": ["string", "null"]}
    item_properties = {
        "review_item_id": {"type": "string"},
        "reviewer_name": nullable_string,
        "reviewer_role": nullable_string,
        "review_date": nullable_string,
        "passage_checked": nullable_string,
        "rule_disposition": {"type": ["string", "null"], "enum": [None, *REVIEW_DISPOSITIONS]},
        "case_application_disposition": {
            "type": ["string", "null"],
            "enum": [None, *REVIEW_DISPOSITIONS],
        },
        "required_revision": nullable_string,
        "claim_ceiling": nullable_string,
        "notes": nullable_string,
    }
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "source-science-reviewer-form/v1",
        "title": "Dynamics Atlas named source-science review form",
        "type": "object",
        "required": [
            "schema_version",
            "review_status",
            "allowed_dispositions",
            "items",
        ],
        "properties": {
            "schema_version": {"const": "source-science-reviewer-form/v1"},
            "review_status": {"const": "PENDING_DOMAIN_REVIEW"},
            "allowed_dispositions": {"type": "array", "const": list(REVIEW_DISPOSITIONS)},
            "instructions": {"type": "string", "minLength": 1},
            "items": {
                "type": "array",
                "minItems": 1,
                "items": {
                    "type": "object",
                    "required": list(item_properties),
                    "properties": item_properties,
                    "additionalProperties": False,
                },
            },
        },
        "additionalProperties": False,
    }


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
4. Enter a named, dated disposition in `reviewer_form.json` without changing Rule or
   runtime files.

`F04R02_SOURCE_DECLARED_TIME_ANATOMY_CONTROL` intentionally begins with a pending
traceability mapping. Its case dossier and manifest identify a bounded control record,
but this workspace does not invent a primary-paper passage for it.

## Allowed dispositions

- `APPROVE_AS_WRITTEN`
- `APPROVE_WITH_BOUNDED_REVISION`
- `DEFER_INSUFFICIENT_SOURCE_GROUNDING`
- `REJECT_NOT_REUSABLE`
- `NOT_APPLICABLE_TO_CURRENT_CASE`

A positive disposition does not automatically activate a Rule, Resolution Policy,
Evaluation Contract, Operator, or scientific claim. A later human/project decision must
explicitly select any allowed next action.

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
    f04_overlay = _read_json(F04R02_OVERLAY_PATH)
    bindings_by_subrule = {str(item["runtime_subrule_id"]): item for item in bindings}
    contracts_by_subrule = {str(item["runtime_subrule_id"]): item for item in contracts}
    policies_by_id = {str(item["resolution_policy_id"]): item for item in policies}
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
        "schema_version": "source-science-reviewer-form/v1",
        "review_status": "PENDING_DOMAIN_REVIEW",
        "allowed_dispositions": list(REVIEW_DISPOSITIONS),
        "instructions": "Only a named human/domain reviewer may complete these fields after checking the referenced passage or case-bound artifact.",
        "items": [
            {
                "review_item_id": entry["review_item_id"],
                "reviewer_name": None,
                "reviewer_role": None,
                "review_date": None,
                "passage_checked": None,
                "rule_disposition": None,
                "case_application_disposition": None,
                "required_revision": None,
                "claim_ceiling": None,
                "notes": None,
            }
            for entry in source_entries
        ],
    }

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
              <p><strong>Short passage:</strong> {_escape(entry['short_source_passage'])}</p>
              <p><strong>Atomic statement:</strong> {_escape(entry['atomic_scientific_statement'])}</p>
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
    capsule_root: Path,
    review_workspace: Path,
    output_dir: Path,
) -> Path:
    """Render a static HTML review trace without a server, API, or mutation path."""

    status = _read_json(status_path)
    source_index = _read_json(review_workspace / "source_passage_index.json")
    matrix = _read_json(review_workspace / "case_application_matrix.json")
    form = _read_json(review_workspace / "reviewer_form.json")
    matrix_by_subrule = {
        str(item["runtime_subrule_id"]): item for item in matrix.get("items", []) if isinstance(item, dict)
    }
    case_sections = "".join(
        _render_case(case_dir=case_dir, matrix_by_subrule=matrix_by_subrule)
        for case_dir in _case_directories(capsule_root)
    )
    queue = _render_review_queue(source_index, matrix, form)
    next_action = status.get("next_allowed_action", {})
    html_document = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Dynamics Atlas · Source-science review</title>
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
    .source-heading, .rule-heading, .evidence-heading, .review-heading {{ display: flex; align-items: flex-start; justify-content: space-between; gap: .75rem; }}
    .locator {{ font-size: .88rem; color: var(--muted); }}
    .muted {{ color: var(--muted); }}
    .evidence-lanes {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1rem; }}
    .evidence-lanes > div {{ border-top: 3px solid var(--teal); padding-top: .5rem; min-width: 0; }}
    details {{ margin: .6rem 0; background: #f9fbfb; border: 1px solid var(--line); padding: .45rem .65rem; }}
    summary {{ cursor: pointer; color: var(--teal); font-weight: 650; }}
    .queue {{ margin-top: 4rem; border-top: 5px solid var(--ink); padding-top: 1.5rem; }}
    .queue-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(25rem, 1fr)); gap: .9rem; }}
    footer {{ margin-top: 4rem; border-top: 1px solid var(--line); padding-top: 1rem; color: var(--muted); font-size: .85rem; }}
    @media (max-width: 860px) {{ .masthead, .two-column, .evidence-lanes, .status-strip {{ grid-template-columns: 1fr; }} .shell {{ padding: 1rem 1rem 3rem; }} }}
  </style>
</head>
<body>
  <main class="shell">
    <header class="masthead">
      <div>
        <div class="eyebrow">DYNAMICS ATLAS · READ-ONLY EVIDENCE LEDGER</div>
        <h1>Source-science review</h1>
        <p class="thesis">A human trace of what the exposed HSP90 and ADK capsules recorded, what each Rule still leaves unresolved, and what a named domain reviewer must check before any scientific authority can move.</p>
      </div>
      <aside class="gate-card">
        <div class="eyebrow">CURRENT GATE</div>
        <p>{_badge(next_action.get('action', 'NOT_RECORDED'))}</p>
        <p>{_escape(next_action.get('exit_gate', 'No exit condition recorded.'))}</p>
      </aside>
    </header>
    {case_sections}
    <section class="queue">
      <div class="eyebrow">NAMED HUMAN / DOMAIN REVIEW QUEUE</div>
      <h2>Primary-passage and application checks</h2>
      <p class="question">Every entry is pending. This view exposes the recorded locator, narrow proposed use, contract boundary, and blank reviewer fields. It does not make a disposition.</p>
      <div class="queue-grid">{queue}</div>
    </section>
    <footer>Generated locally from repository artifacts. Static HTML only: no model call, operator execution, API credential, database, mutation endpoint, or scientific approval.</footer>
  </main>
</body>
</html>
"""
    html_document = "\n".join(line.rstrip() for line in html_document.splitlines()) + "\n"
    output_dir.mkdir(parents=True, exist_ok=True)
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
    parser.add_argument("--capsule-root", type=Path, required=True)
    parser.add_argument("--review-workspace", type=Path, default=DEFAULT_REVIEW_WORKSPACE)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args(argv)
    output_path = render_review_console(
        status_path=args.status,
        capsule_root=args.capsule_root,
        review_workspace=args.review_workspace,
        output_dir=args.output_dir,
    )
    print(output_path)
    return 0
