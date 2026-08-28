import copy
import json
import unittest
from pathlib import Path

from dynamics_atlas_harness.minimal_stage2_exposed_conclusions_v1 import (
    MinimalStage2ConclusionError,
    materialize_stage2_conclusion_packet,
    source_grounding_by_family,
    validate_stage2_conclusion_packet,
)
from dynamics_atlas_harness.real_case_vertical_slice_v1 import VerticalSliceError


REPO_ROOT = Path(__file__).parents[1]
ROUTE_OUTPUT_ROOT = REPO_ROOT / "evidence" / "real_case_vertical_slice_v1" / "outputs"
FAMILY_OVERLAY_PATH = REPO_ROOT / "registries" / "rules_v1" / "family_overlay_v1.json"
SCHEMA_PATH = REPO_ROOT / "schemas" / "rules_v1" / "stage2_conclusion_packet_v1.schema.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class MinimalStage2ExposedConclusionsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.source_grounding = source_grounding_by_family(load_json(FAMILY_OVERLAY_PATH))

    def materialize(self, filename: str, scenario_id: str, *, source_grounding=None) -> dict:
        route_packet = load_json(ROUTE_OUTPUT_ROOT / filename)
        return materialize_stage2_conclusion_packet(
            route_packet=route_packet,
            source_grounding=source_grounding or self.source_grounding,
            scenario_id=scenario_id,
            route_artifact_path=(
                "evidence/real_case_vertical_slice_v1/outputs/" + filename
            ),
        )

    def test_xeisd_complete_metadata_abstains_for_pending_source_review(self):
        packet = self.materialize(
            "xeisd_a1_conclusion_packet.json", "XEISD_A1_COMPLETE_METADATA"
        )

        self.assertEqual(packet["terminal_disposition"], "ABSTAIN_OR_HUMAN_REVIEW")
        self.assertEqual(packet["failed_rule_results"], [])
        self.assertEqual(packet["unresolved_rule_results"], [])
        self.assertEqual(packet["source_science_review_status"], "PENDING_DOMAIN_REVIEW")
        self.assertEqual(
            packet["first_failed_dependency"]["dependency_kind"],
            "SOURCE_SCIENCE_REVIEW_GATE",
        )
        self.assertEqual(packet["route_disposition"], "RELATION_REVIEWABLE")

    def test_xeisd_missing_composition_abstains_at_source_rule(self):
        packet = self.materialize(
            "xeisd_a2_conclusion_packet.json", "XEISD_A2_MISSING_COMPOSITION"
        )

        self.assertEqual(packet["terminal_disposition"], "ABSTAIN_OR_HUMAN_REVIEW")
        self.assertEqual(len(packet["unresolved_rule_results"]), 3)
        self.assertEqual(
            packet["first_failed_dependency"]["rule_instance_id"],
            "F02R01_SOURCE_SAMPLE_SYSTEM_COMPOSITION_DECLARATION::SOURCE::xeisd_random_candidate_pool",
        )
        self.assertEqual(packet["first_failed_dependency"]["status"], "UNRESOLVED")

    def test_xeisd_explicit_condition_mismatch_cannot_support_relation(self):
        packet = self.materialize(
            "xeisd_a3_conclusion_packet.json", "XEISD_A3_EXPLICIT_CONDITION_MISMATCH"
        )

        self.assertEqual(
            packet["terminal_disposition"], "CANNOT_SUPPORT_REQUESTED_CLAIM"
        )
        self.assertEqual(len(packet["failed_rule_results"]), 2)
        self.assertEqual(
            packet["first_failed_dependency"]["rule_instance_id"],
            "F02R02_EDGE_CONDITION_COMPATIBILITY::EDGE::xeisd_random_pool_vs_j_coupling_question",
        )
        self.assertEqual(packet["first_failed_dependency"]["status"], "FAIL")
        self.assertEqual(packet["route_disposition"], "RELATION_BLOCKED")

    def test_hsp90_contract_pass_abstains_while_source_science_is_pending(self):
        packet = self.materialize(
            "hsp90_b1_rule_to_operator/conclusion_packet.json",
            "HSP90_B1_OPERATOR_CONTRACT_PASS",
        )

        self.assertEqual(packet["terminal_disposition"], "ABSTAIN_OR_HUMAN_REVIEW")
        self.assertEqual(packet["failed_rule_results"], [])
        self.assertEqual(packet["unresolved_rule_results"], [])
        self.assertEqual(packet["route_disposition"], "RULE_CONTRACT_PASS")
        self.assertEqual(len(packet["operator_receipts"]), 1)
        self.assertEqual(
            packet["first_failed_dependency"]["dependency_kind"], "EVIDENCE_RESULT"
        )
        self.assertEqual(
            packet["evidence_results"][0]["result"]["scientific_evaluation_status"],
            "PENDING_HUMAN_VALIDATION",
        )
        self.assertTrue(
            any("PENDING_HUMAN_VALIDATION" in item for item in packet["human_review_items"])
        )

    def test_hsp90_pending_evidence_blocks_support_even_if_source_review_is_verified(self):
        verified = {family_id: "VERIFIED" for family_id in self.source_grounding}
        packet = self.materialize(
            "hsp90_b1_rule_to_operator/conclusion_packet.json",
            "HSP90_B1_VERIFIED_SOURCE_REVIEW_PENDING_EVIDENCE",
            source_grounding=verified,
        )

        self.assertEqual(packet["source_science_review_status"], "VERIFIED")
        self.assertEqual(packet["terminal_disposition"], "ABSTAIN_OR_HUMAN_REVIEW")
        self.assertEqual(
            packet["first_failed_dependency"]["status"], "PENDING_HUMAN_VALIDATION"
        )

    def test_synthetic_verified_source_gate_proves_support_contract_without_upgrading_real_case(self):
        verified = {family_id: "VERIFIED" for family_id in self.source_grounding}
        packet = self.materialize(
            "xeisd_a1_conclusion_packet.json",
            "XEISD_A1_SYNTHETIC_VERIFIED_SOURCE_GATE",
            source_grounding=verified,
        )

        self.assertEqual(packet["terminal_disposition"], "SUPPORT_WITHIN_CEILING")
        self.assertIsNone(packet["first_failed_dependency"])
        self.assertEqual(packet["advisory_rule_results"][0]["status"], "NOT_APPLICABLE")
        self.assertTrue(packet["human_final_authority"])

    def test_xeisd_route_rejects_truncated_required_rule_inventory_before_support(self):
        route_packet = load_json(
            ROUTE_OUTPUT_ROOT / "xeisd_a3_conclusion_packet.json"
        )
        failed_ids = set(route_packet["blocking_rule_instance_ids"])
        route_packet["rule_results"] = [
            result
            for result in route_packet["rule_results"]
            if result["rule_instance_id"] not in failed_ids
        ]
        route_packet["selected_rule_instance_ids"] = [
            rule_id
            for rule_id in route_packet["selected_rule_instance_ids"]
            if rule_id not in failed_ids
        ]
        route_packet["blocking_rule_instance_ids"] = []
        route_packet["route_disposition"] = "RELATION_REVIEWABLE"
        verified = {family_id: "VERIFIED" for family_id in self.source_grounding}

        with self.assertRaisesRegex(VerticalSliceError, "frozen inventory"):
            materialize_stage2_conclusion_packet(
                route_packet=route_packet,
                source_grounding=verified,
                scenario_id="XEISD_A3_TRUNCATED_RULE_INVENTORY",
                route_artifact_path="evidence/real_case_vertical_slice_v1/outputs/xeisd_a3_conclusion_packet.json",
            )

    def test_xeisd_route_rejects_source_local_claim_relabel_before_relation_cannot_support(self):
        route_packet = load_json(
            ROUTE_OUTPUT_ROOT / "xeisd_a3_conclusion_packet.json"
        )
        route_packet["requested_claim"] = (
            "A source-local observation from xeisd_random_candidate_pool is valid."
        )
        verified = {family_id: "VERIFIED" for family_id in self.source_grounding}

        with self.assertRaisesRegex(VerticalSliceError, "exact frozen relation claim"):
            materialize_stage2_conclusion_packet(
                route_packet=route_packet,
                source_grounding=verified,
                scenario_id="XEISD_A3_SOURCE_LOCAL_CLAIM_RELABEL",
                route_artifact_path="evidence/real_case_vertical_slice_v1/outputs/xeisd_a3_conclusion_packet.json",
            )

    def test_xeisd_relation_block_rejects_a_source_targeted_failed_rule(self):
        route_packet = load_json(
            ROUTE_OUTPUT_ROOT / "xeisd_a3_conclusion_packet.json"
        )
        failed_id = route_packet["blocking_rule_instance_ids"][0]
        failed_result = next(
            result
            for result in route_packet["rule_results"]
            if result["rule_instance_id"] == failed_id
        )
        failed_result["target"] = {
            "kind": "SOURCE",
            "id": "xeisd_random_candidate_pool",
        }
        route_packet["route_disposition"] = "ABSTAIN"
        verified = {family_id: "VERIFIED" for family_id in self.source_grounding}

        with self.assertRaisesRegex(VerticalSliceError, "relation-blocked route"):
            materialize_stage2_conclusion_packet(
                route_packet=route_packet,
                source_grounding=verified,
                scenario_id="XEISD_A3_SOURCE_TARGETED_RELATION_BLOCK",
                route_artifact_path="evidence/real_case_vertical_slice_v1/outputs/xeisd_a3_conclusion_packet.json",
            )

    def test_hsp90_route_rejects_unknown_evidence_status_before_support(self):
        route_packet = load_json(
            ROUTE_OUTPUT_ROOT / "hsp90_b1_rule_to_operator/conclusion_packet.json"
        )
        route_packet["operator_results"][0]["evidence_result"][
            "scientific_evaluation_status"
        ] = "UNRECOGNIZED_STATUS"
        verified = {family_id: "VERIFIED" for family_id in self.source_grounding}

        with self.assertRaisesRegex(VerticalSliceError, "linked validated evidence"):
            materialize_stage2_conclusion_packet(
                route_packet=route_packet,
                source_grounding=verified,
                scenario_id="HSP90_B1_UNKNOWN_EVIDENCE_STATUS",
                route_artifact_path="evidence/real_case_vertical_slice_v1/outputs/hsp90_b1_rule_to_operator/conclusion_packet.json",
            )

    def test_stage2_validator_rejects_unknown_hsp90_evidence_status_before_support(self):
        verified = {family_id: "VERIFIED" for family_id in self.source_grounding}
        invalid = self.materialize(
            "hsp90_b1_rule_to_operator/conclusion_packet.json",
            "HSP90_B1_FINAL_PACKET_UNKNOWN_EVIDENCE_STATUS",
            source_grounding=verified,
        )
        invalid["evidence_results"][0]["result"][
            "scientific_evaluation_status"
        ] = "UNRECOGNIZED_STATUS"
        invalid["terminal_disposition"] = "SUPPORT_WITHIN_CEILING"
        invalid["first_failed_dependency"] = None

        with self.assertRaisesRegex(MinimalStage2ConclusionError, "PENDING_HUMAN_VALIDATION"):
            validate_stage2_conclusion_packet(invalid, source_grounding=verified)

    def test_stage2_validator_rejects_xeisd_source_local_claim_relabel(self):
        invalid = self.materialize(
            "xeisd_a3_conclusion_packet.json",
            "XEISD_A3_FINAL_PACKET_SOURCE_LOCAL_CLAIM_RELABEL",
        )
        invalid["requested_claim"] = "A source-local observation is valid."

        with self.assertRaisesRegex(MinimalStage2ConclusionError, "exact frozen relation claim"):
            validate_stage2_conclusion_packet(
                invalid, source_grounding=self.source_grounding
            )

    def test_validator_rejects_manual_terminal_upgrade(self):
        packet = self.materialize(
            "xeisd_a1_conclusion_packet.json", "XEISD_A1_COMPLETE_METADATA"
        )
        invalid = copy.deepcopy(packet)
        invalid["terminal_disposition"] = "SUPPORT_WITHIN_CEILING"

        with self.assertRaises(MinimalStage2ConclusionError):
            validate_stage2_conclusion_packet(
                invalid, source_grounding=self.source_grounding
            )

    def test_validator_rejects_unrelated_review_record_and_forged_support(self):
        packet = self.materialize(
            "xeisd_a1_conclusion_packet.json", "XEISD_A1_COMPLETE_METADATA"
        )
        invalid = copy.deepcopy(packet)
        invalid["source_science_review_records"] = [
            {
                "family_id": "F99_UNRELATED",
                "human_decision_gate_id": "HDG-RULES-V1-SOURCE-SCIENCE-REVIEW",
                "source_grounding_decision": "VERIFIED",
            }
        ]
        invalid["source_science_review_status"] = "VERIFIED"
        invalid["terminal_disposition"] = "SUPPORT_WITHIN_CEILING"
        invalid["first_failed_dependency"] = None

        with self.assertRaises(MinimalStage2ConclusionError):
            validate_stage2_conclusion_packet(
                invalid, source_grounding=self.source_grounding
            )

    def test_validator_rejects_correct_family_forged_source_review_approval(self):
        packet = self.materialize(
            "xeisd_a1_conclusion_packet.json", "XEISD_A1_COMPLETE_METADATA"
        )
        invalid = copy.deepcopy(packet)
        for record in invalid["source_science_review_records"]:
            record["source_grounding_decision"] = "VERIFIED"
        invalid["source_science_review_status"] = "VERIFIED"
        invalid["provenance"]["source_grounding_input"] = {
            record["family_id"]: record["source_grounding_decision"]
            for record in invalid["source_science_review_records"]
        }
        invalid["terminal_disposition"] = "SUPPORT_WITHIN_CEILING"
        invalid["first_failed_dependency"] = None

        with self.assertRaises(MinimalStage2ConclusionError):
            validate_stage2_conclusion_packet(
                invalid, source_grounding=self.source_grounding
            )

    def test_validator_rejects_missing_required_source_review_record_before_support(self):
        verified = {family_id: "VERIFIED" for family_id in self.source_grounding}
        invalid = self.materialize(
            "xeisd_a1_conclusion_packet.json",
            "XEISD_A1_SOURCE_REVIEW_OMISSION",
            source_grounding=verified,
        )
        removed_record = invalid["source_science_review_records"].pop()
        del invalid["provenance"]["source_grounding_input"][
            removed_record["family_id"]
        ]

        with self.assertRaisesRegex(
            MinimalStage2ConclusionError,
            "cover each required RuleResult family exactly once",
        ):
            validate_stage2_conclusion_packet(invalid, source_grounding=verified)

    def test_schema_declares_only_the_stage2_wrapper_fields(self):
        schema = load_json(SCHEMA_PATH)
        packet = self.materialize(
            "xeisd_a1_conclusion_packet.json", "XEISD_A1_COMPLETE_METADATA"
        )

        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(set(packet), set(schema["required"]))
        self.assertEqual(
            schema["properties"]["terminal_disposition"]["enum"],
            [
                "SUPPORT_WITHIN_CEILING",
                "CANNOT_SUPPORT_REQUESTED_CLAIM",
                "ABSTAIN_OR_HUMAN_REVIEW",
            ],
        )
