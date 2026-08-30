import json
import re
import unittest
from copy import deepcopy
from pathlib import Path

from jsonschema import Draft202012Validator

from dynamics_atlas_harness.paper_blind_exposed_v1 import (
    project_admitted_proposal_to_rules_casegraph,
    validate_agent_proposal,
)
from dynamics_atlas_harness.profile_proposal_envelope_v1 import (
    ANNOTATION_STATUSES,
    ProfileProposalEnvelopeV1Error,
    build_profile_annotation_diagnostic_summary,
    build_profile_proposal_envelope_schema,
    extract_core_proposal,
    validate_profile_proposal_envelope,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
PUBLIC_ROOT = REPO_ROOT / "evidence" / "paper_blind_exposed_v1" / "public"
PROFILER_ROOT = (
    REPO_ROOT / "evidence" / "paper_blind_exposed_v1" / "agent_runs" / "profiler"
)
HSP90_PACKET = PUBLIC_ROOT / "hsp90_public_packet_v1.json"
HSP90_PROPOSAL = PROFILER_ROOT / "hsp90_proposal.json"
_UNKNOWN_TOKEN = re.compile(r"\bUNKNOWN\b", flags=re.IGNORECASE)


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _contains_unknown(value) -> bool:
    if isinstance(value, str):
        return _UNKNOWN_TOKEN.search(value) is not None
    if isinstance(value, list):
        return any(_contains_unknown(item) for item in value)
    if isinstance(value, dict):
        return any(_contains_unknown(item) for item in value.values())
    return False


def _critical_targets(proposal: dict) -> list[tuple[str, str, str, object]]:
    facts = proposal["proposed_case_facts"]
    targets = [
        ("CASE", proposal["case_id"], field, facts["case"][field])
        for field in (
            "scientific_claim",
            "requested_claim_level",
            "intended_use",
            "declared_request_scope",
            "forbidden_upgrades",
        )
    ]
    for source in facts["sources"]:
        for field in (
            "construct_and_condition",
            "sample_composition",
            "native_observable",
            "estimand",
            "time_semantics.kind",
            "spatial_support",
            "unit_or_aggregation",
        ):
            value = (
                source["time_semantics"]["kind"]
                if field == "time_semantics.kind"
                else source[field]
            )
            targets.append(("SOURCE", source["source_id"], field, value))
    for edge in facts["edges"]:
        for field in (
            "relation_type",
            "condition_relation",
            "bridge_status",
            "validation_independence",
            "shared_error_status",
        ):
            targets.append(("EDGE", edge["edge_id"], field, edge[field]))
    return targets


def _valid_envelope() -> dict:
    proposal = _load(HSP90_PROPOSAL)
    packet = _load(HSP90_PACKET)
    annotations = []
    for target_type, target_id, field, value in _critical_targets(proposal):
        annotations.append(
            {
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
                "confidence": 0.8,
            }
        )

    first_source = packet["source_materials"][0]
    annotations[5]["evidence_pointers"] = [
        {
            "pointer_type": "SOURCE_LOCATOR",
            "source_id": first_source["source_id"],
            "value": first_source["source_locator"],
        }
    ]
    annotations[7]["evidence_pointers"] = [
        {
            "pointer_type": "PERMITTED_FACT",
            "source_id": first_source["source_id"],
            "value": first_source["permitted_facts"][0],
        }
    ]
    return {**proposal, "field_annotations": annotations}


def _annotation(envelope: dict, target_type: str, target_id: str, field: str) -> dict:
    return next(
        item
        for item in envelope["field_annotations"]
        if (item["target_type"], item["target_id"], item["field"])
        == (target_type, target_id, field)
    )


class ProfileProposalEnvelopeV1Tests(unittest.TestCase):
    def test_schema_is_strict_and_accepts_one_compatible_envelope(self):
        schema = build_profile_proposal_envelope_schema(HSP90_PACKET)
        Draft202012Validator.check_schema(schema)
        Draft202012Validator(schema).validate(_valid_envelope())
        self.assertEqual(
            schema["required"],
            [
                "case_id",
                "proposed_case_facts",
                "unknowns",
                "rationale",
                "field_annotations",
            ],
        )
        self.assertEqual(
            schema["properties"]["field_annotations"]["items"]["properties"]["status"][
                "enum"
            ],
            list(ANNOTATION_STATUSES),
        )

        def assert_all_object_schemas_are_closed(value):
            if isinstance(value, dict):
                if value.get("type") == "object":
                    self.assertIs(value.get("additionalProperties"), False)
                for child in value.values():
                    assert_all_object_schemas_are_closed(child)
            elif isinstance(value, list):
                for child in value:
                    assert_all_object_schemas_are_closed(child)

        assert_all_object_schemas_are_closed(schema)

    def test_core_is_unchanged_and_is_the_only_rules_projection_input(self):
        envelope = _valid_envelope()
        expected_core = _load(HSP90_PROPOSAL)
        extracted = extract_core_proposal(envelope)
        self.assertEqual(extracted, expected_core)
        extracted["rationale"] = "mutated copy"
        self.assertEqual(envelope["rationale"], expected_core["rationale"])

        validated = validate_profile_proposal_envelope(HSP90_PACKET, envelope)
        direct_admission = validate_agent_proposal(HSP90_PACKET, expected_core)
        self.assertEqual(validated["core_admission"], direct_admission)
        self.assertEqual(validated["routing_input"]["kind"], "EXISTING_CORE_ADMISSION_ONLY")
        self.assertEqual(
            project_admitted_proposal_to_rules_casegraph(
                HSP90_PACKET, validated["core_admission"]
            ),
            project_admitted_proposal_to_rules_casegraph(HSP90_PACKET, direct_admission),
        )
        self.assertEqual(validated["diagnostic_summary"]["coverage_status"], "COMPLETE")
        self.assertEqual(validated["diagnostic_summary"]["routing_effect"], "NONE_DIAGNOSTIC_ONLY")
        self.assertEqual(
            build_profile_annotation_diagnostic_summary(HSP90_PACKET, envelope),
            validated["diagnostic_summary"],
        )

    def test_duplicate_dangling_and_incomplete_targets_fail_closed(self):
        base = _valid_envelope()
        mutations = []

        duplicate = deepcopy(base)
        duplicate["field_annotations"].append(deepcopy(duplicate["field_annotations"][0]))
        mutations.append((duplicate, "DUPLICATE_ANNOTATION_TARGET"))

        dangling = deepcopy(base)
        dangling["field_annotations"][0]["target_id"] = "NOT_A_CASE"
        mutations.append((dangling, "ANNOTATION_TARGET_DANGLING_OR_NONCRITICAL"))

        incomplete = deepcopy(base)
        incomplete["field_annotations"].pop()
        mutations.append((incomplete, "CRITICAL_ANNOTATION_COVERAGE_INCOMPLETE"))

        for envelope, error_code in mutations:
            with self.subTest(error_code=error_code):
                with self.assertRaisesRegex(ProfileProposalEnvelopeV1Error, error_code):
                    validate_profile_proposal_envelope(HSP90_PACKET, envelope)

    def test_only_public_locators_facts_and_visible_packet_pointers_are_accepted(self):
        base = _valid_envelope()
        packet = _load(HSP90_PACKET)
        first_source_id = packet["source_materials"][0]["source_id"]
        second_source_fact = packet["source_materials"][1]["permitted_facts"][0]
        mutations = []

        bad_locator = deepcopy(base)
        bad_locator["field_annotations"][0]["evidence_pointers"] = [
            {
                "pointer_type": "SOURCE_LOCATOR",
                "source_id": first_source_id,
                "value": "unregistered locator",
            }
        ]
        mutations.append((bad_locator, "SOURCE_LOCATOR_NOT_PERMITTED"))

        cross_source_fact = deepcopy(base)
        cross_source_fact["field_annotations"][0]["evidence_pointers"] = [
            {
                "pointer_type": "PERMITTED_FACT",
                "source_id": first_source_id,
                "value": second_source_fact,
            }
        ]
        mutations.append((cross_source_fact, "PERMITTED_FACT_POINTER_NOT_PERMITTED"))

        hidden_pointer = deepcopy(base)
        hidden_pointer["field_annotations"][0]["evidence_pointers"] = [
            {
                "pointer_type": "PACKET_POINTER",
                "source_id": "PACKET",
                "value": "/platform_authority_envelope/scientific_disposition",
            }
        ]
        mutations.append((hidden_pointer, "PACKET_POINTER_DANGLING"))

        for envelope, error_code in mutations:
            with self.subTest(error_code=error_code):
                with self.assertRaisesRegex(ProfileProposalEnvelopeV1Error, error_code):
                    validate_profile_proposal_envelope(HSP90_PACKET, envelope)

    def test_status_core_consistency_confidence_and_envelope_shape_fail_closed(self):
        base = _valid_envelope()
        case_id = base["case_id"]
        source_id = base["proposed_case_facts"]["sources"][0]["source_id"]
        mutations = []

        unknown_over_known = deepcopy(base)
        _annotation(
            unknown_over_known, "CASE", case_id, "scientific_claim"
        )["status"] = "UNKNOWN"
        mutations.append((unknown_over_known, "UNKNOWN_STATUS_CORE_VALUE_MISMATCH"))

        known_over_unknown = deepcopy(base)
        _annotation(
            known_over_unknown, "SOURCE", source_id, "sample_composition"
        )["status"] = "EXTRACTED"
        mutations.append((known_over_unknown, "KNOWN_STATUS_CORE_VALUE_MISMATCH"))

        invalid_status = deepcopy(base)
        invalid_status["field_annotations"][0]["status"] = "MODEL_GUESS"
        mutations.append((invalid_status, "ANNOTATION_STATUS_INVALID"))

        invalid_confidence = deepcopy(base)
        invalid_confidence["field_annotations"][0]["confidence"] = 1.01
        mutations.append((invalid_confidence, "ANNOTATION_CONFIDENCE_OUT_OF_RANGE"))

        for envelope, error_code in mutations:
            with self.subTest(error_code=error_code):
                with self.assertRaisesRegex(ProfileProposalEnvelopeV1Error, error_code):
                    validate_profile_proposal_envelope(HSP90_PACKET, envelope)

        extra_field = {**deepcopy(base), "scientific_disposition": "SUPPORT"}
        with self.assertRaisesRegex(
            ProfileProposalEnvelopeV1Error, "ENVELOPE_FIELDS_DO_NOT_MATCH_CONTRACT"
        ):
            extract_core_proposal(extra_field)


if __name__ == "__main__":
    unittest.main()
