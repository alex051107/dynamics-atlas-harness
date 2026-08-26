import copy
import json
import unittest
from pathlib import Path

from dynamics_atlas_harness.real_case_vertical_slice_v1 import (
    X_EISD_CASE_ID,
    X_EISD_EDGE_ID,
    VerticalSliceError,
    apply_lookup_result,
    derive_declaration_attestations,
    evaluate_xeisd_case,
    execute_exact_source_lookup,
    load_rules_v1_bundle,
    materialize_xeisd_conclusion_packet,
    validate_xeisd_projection,
)
from dynamics_atlas_harness.rules_prototype_v1 import rule_instance_id


REPO_ROOT = Path(__file__).parents[2]
EVIDENCE_ROOT = REPO_ROOT / "evidence" / "real_case_vertical_slice_v1"
RULES_ROOT = REPO_ROOT / "registries" / "rules_v1"
FROZEN_BASE_PROJECTION_PATH = (
    EVIDENCE_ROOT / "frozen_inputs" / "xeisd" / "base_projection_manifest_v1.json"
)


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


class XeisdVerticalSliceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.seed = read_json(EVIDENCE_ROOT / "xeisd_case_projection_seed_v1.json")
        cls.allowlist = read_json(EVIDENCE_ROOT / "xeisd_source_lookup_allowlist_v1.json")
        cls.bundle = load_rules_v1_bundle(RULES_ROOT)

    def _request(self, lookup_id):
        entry = next(item for item in self.allowlist["entries"] if item["lookup_id"] == lookup_id)
        return {
            "lookup_id": lookup_id,
            "case_id": X_EISD_CASE_ID,
            "target_kind": entry["target_kind"],
            "target_id": entry["target_id"],
            "locator_id": entry["locator_id"],
        }

    def _lookup(self, lookup_id):
        return execute_exact_source_lookup(
            allowlist=self.allowlist,
            request=self._request(lookup_id),
            workspace_root=REPO_ROOT,
        )

    def _complete_case(self):
        case_graph = copy.deepcopy(self.seed)
        lookup_results = []
        for lookup_id in (
            "XEI-LOOKUP-RANDOM-DECLARATIONS",
            "XEI-LOOKUP-JCOUPLING-DECLARATIONS",
            "XEI-LOOKUP-RANDOM-JCOUPLING-EDGE",
        ):
            result = self._lookup(lookup_id)
            lookup_results.append(result)
            case_graph = apply_lookup_result(case_graph=case_graph, lookup_result=result)
        return derive_declaration_attestations(
            case_graph=case_graph, lookup_results=lookup_results
        ), lookup_results

    def _evaluate(self, case_graph):
        return evaluate_xeisd_case(case_graph=case_graph, **self.bundle)

    @staticmethod
    def _result_by_id(results, subrule_id, target_kind, target_id):
        stable_id = rule_instance_id(subrule_id, target_kind, target_id)
        return next(result for result in results if result["rule_instance_id"] == stable_id)

    def test_seed_is_a_provenance_preserving_subprojection_of_frozen_base_manifest(self):
        validate_xeisd_projection(self.seed)
        base_manifest = read_json(FROZEN_BASE_PROJECTION_PATH)
        raw_sources = {
            item["source_id"]: item for item in base_manifest["evidence_items"]
        }
        raw_edges = {
            item["comparison_id"]: item for item in base_manifest["comparisons"]
        }

        self.assertEqual(
            self.seed["case"]["parent_case_id"], base_manifest["case"]["case_id"]
        )
        self.assertNotEqual(
            self.seed["case"]["case_id"], base_manifest["case"]["case_id"]
        )
        self.assertEqual(
            self.seed["projection_provenance"]["base_asset_id"],
            "xeisd-rich-casegraph-v0.3",
        )
        self.assertEqual(
            self.seed["projection_provenance"]["workspace_relative_base_asset_path"],
            "evidence/real_case_vertical_slice_v1/frozen_inputs/xeisd/base_projection_manifest_v1.json",
        )
        self.assertEqual(
            self.seed["projection_provenance"]["base_asset_sha256"],
            base_manifest["source_asset"]["upstream_sha256"],
        )
        for source in self.seed["evidence_items"]:
            raw_source = raw_sources[source["source_id"]]
            for field in (
                "native_observable",
                "estimand",
                "spatial_support",
                "unit_or_aggregation",
            ):
                self.assertEqual(source[field], raw_source[field])
        self.assertEqual(
            self.seed["comparisons"][0]["shared_claim"],
            raw_edges[X_EISD_EDGE_ID]["shared_claim"],
        )

    def test_lookup_and_conclusion_contract_schemas_keep_the_route_boundaries(self):
        lookup_schema = read_json(
            REPO_ROOT / "schemas" / "rules_v1" / "source_lookup_result_v1.schema.json"
        )
        conclusion_schema = read_json(
            REPO_ROOT / "schemas" / "rules_v1" / "conclusion_packet_v1.schema.json"
        )
        self.assertEqual(lookup_schema["properties"]["case_id"]["const"], X_EISD_CASE_ID)
        self.assertEqual(
            lookup_schema["properties"]["lookup_kind"]["const"],
            "EXACT_REVIEW_DERIVATIVE_ATTESTATION",
        )
        self.assertIn("SOURCE_LOOKUP", lookup_schema["properties"]["route"]["enum"])
        self.assertIn("REGISTERED_OPERATOR", conclusion_schema["properties"]["terminal_route"]["enum"])
        self.assertNotIn("const", conclusion_schema["properties"]["case_id"])
        self.assertIn("operator_results", conclusion_schema["required"])
        self.assertIn("route_disposition", conclusion_schema["required"])
        self.assertEqual(
            conclusion_schema["properties"]["scientific_disposition"]["const"],
            "NOT_EVALUATED",
        )

    def test_a0_raw_projection_fails_closed_before_lookup(self):
        pending = derive_declaration_attestations(case_graph=self.seed, lookup_results=[])
        results = self._evaluate(pending)
        self.assertEqual(
            self._result_by_id(
                results,
                "F02R01_SOURCE_SAMPLE_SYSTEM_COMPOSITION_DECLARATION",
                "SOURCE",
                "xeisd_random_candidate_pool",
            )["status"],
            "UNRESOLVED",
        )
        self.assertEqual(
            self._result_by_id(
                results,
                "F02R02_EDGE_CONDITION_COMPATIBILITY",
                "EDGE",
                X_EISD_EDGE_ID,
            )["status"],
            "UNRESOLVED",
        )
        self.assertEqual(
            self._result_by_id(
                results,
                "F06R02_EDGE_COMPARABILITY",
                "EDGE",
                X_EISD_EDGE_ID,
            )["status"],
            "UNRESOLVED",
        )

    def test_a1_exact_lookup_then_direct_evaluation_reaches_bounded_review_gate(self):
        complete, lookup_results = self._complete_case()
        self.assertTrue(all(result["status"] == "FOUND" for result in lookup_results))
        self.assertTrue(
            all(
                result["lookup_kind"] == "EXACT_REVIEW_DERIVATIVE_ATTESTATION"
                for result in lookup_results
            )
        )
        self.assertTrue(all(result["route"] == "SOURCE_LOOKUP" for result in lookup_results))
        self.assertTrue(all(result["next_evaluation"] == "DIRECT_EVALUATION" for result in lookup_results))

        results = self._evaluate(complete)
        for subrule_id, target_kind, target_id in (
            ("F02R01_SOURCE_SAMPLE_SYSTEM_COMPOSITION_DECLARATION", "SOURCE", "xeisd_random_candidate_pool"),
            ("F02R01_SOURCE_SAMPLE_SYSTEM_COMPOSITION_DECLARATION", "SOURCE", "xeisd_j_coupling_fit"),
            ("F02R02_EDGE_CONDITION_COMPATIBILITY", "EDGE", X_EISD_EDGE_ID),
            ("F03R01_SOURCE_NATIVE_MEASUREMENT", "SOURCE", "xeisd_random_candidate_pool"),
            ("F03R01_SOURCE_NATIVE_MEASUREMENT", "SOURCE", "xeisd_j_coupling_fit"),
            ("F06R02_EDGE_COMPARABILITY", "EDGE", X_EISD_EDGE_ID),
        ):
            self.assertEqual(
                self._result_by_id(results, subrule_id, target_kind, target_id)["status"],
                "PASS",
            )
        packet = materialize_xeisd_conclusion_packet(
            case_graph=complete,
            rule_results=results,
            lookup_results=lookup_results,
            scenario_id="A1_COMPLETE_LOOKUP_THEN_DIRECT",
        )
        self.assertEqual(packet["terminal_route"], "DIRECT_EVALUATION")
        self.assertEqual(packet["route_disposition"], "RELATION_REVIEWABLE")
        self.assertEqual(packet["scientific_disposition"], "NOT_EVALUATED")
        self.assertFalse(packet["unsafe_claim_upgrade"])
        self.assertEqual(packet["operator_results"], [])
        self.assertEqual(len(packet["nonblocking_rule_results"]), 1)
        self.assertEqual(packet["nonblocking_rule_results"][0]["status"], "NOT_APPLICABLE")

    def test_a2_removed_composition_yields_lookup_then_abstain(self):
        complete, _ = self._complete_case()
        complete["evidence_items"][0].pop("sample_composition")
        results = self._evaluate(complete)
        missing_lookup = execute_exact_source_lookup(
            allowlist=self.allowlist,
            request={
                "lookup_id": "XEI-LOOKUP-MISSING-COMPOSITION",
                "case_id": X_EISD_CASE_ID,
                "target_kind": "SOURCE",
                "target_id": "xeisd_random_candidate_pool",
                "locator_id": "XEI-M04",
            },
            workspace_root=REPO_ROOT,
        )
        packet = materialize_xeisd_conclusion_packet(
            case_graph=complete,
            rule_results=results,
            lookup_results=[missing_lookup],
            scenario_id="A2_MISSING_COMPOSITION",
        )
        self.assertEqual(missing_lookup["status"], "NOT_FOUND")
        self.assertEqual(packet["terminal_route"], "HUMAN_OR_NEW_DATA")
        self.assertEqual(packet["route_disposition"], "ABSTAIN")
        self.assertEqual(
            packet["first_failed_dependency"]["rule_instance_id"],
            rule_instance_id(
                "F02R01_SOURCE_SAMPLE_SYSTEM_COMPOSITION_DECLARATION",
                "SOURCE",
                "xeisd_random_candidate_pool",
            ),
        )

    def test_a3_explicit_condition_mismatch_blocks_only_the_relation(self):
        complete, lookup_results = self._complete_case()
        complete["comparisons"][0]["condition_relation"] = "MISMATCH"
        results = self._evaluate(complete)
        self.assertEqual(
            self._result_by_id(
                results,
                "F02R02_EDGE_CONDITION_COMPATIBILITY",
                "EDGE",
                X_EISD_EDGE_ID,
            )["status"],
            "FAIL",
        )
        self.assertEqual(
            self._result_by_id(
                results,
                "F06R02_EDGE_COMPARABILITY",
                "EDGE",
                X_EISD_EDGE_ID,
            )["status"],
            "FAIL",
        )
        self.assertEqual(
            self._result_by_id(
                results,
                "F02R01_SOURCE_SAMPLE_SYSTEM_COMPOSITION_DECLARATION",
                "SOURCE",
                "xeisd_random_candidate_pool",
            )["status"],
            "PASS",
        )
        packet = materialize_xeisd_conclusion_packet(
            case_graph=complete,
            rule_results=results,
            lookup_results=lookup_results,
            scenario_id="A3_EXPLICIT_CONDITION_MISMATCH",
        )
        self.assertEqual(packet["route_disposition"], "RELATION_BLOCKED")
        self.assertEqual(packet["scientific_disposition"], "NOT_EVALUATED")
        self.assertEqual(packet["first_failed_dependency"]["status"], "FAIL")

    def test_lookup_rejects_wrong_target_duplicate_receipt_and_unsafe_patch(self):
        wrong_target = execute_exact_source_lookup(
            allowlist=self.allowlist,
            request={
                **self._request("XEI-LOOKUP-RANDOM-DECLARATIONS"),
                "target_id": "xeisd_j_coupling_fit",
            },
            workspace_root=REPO_ROOT,
        )
        self.assertEqual(wrong_target["status"], "NOT_ALLOWED")
        self.assertEqual(
            wrong_target["lookup_kind"], "EXACT_REVIEW_DERIVATIVE_ATTESTATION"
        )

        receipt = self._lookup("XEI-LOOKUP-RANDOM-DECLARATIONS")
        applied = apply_lookup_result(case_graph=self.seed, lookup_result=receipt)
        with self.assertRaisesRegex(VerticalSliceError, "may not be applied twice"):
            apply_lookup_result(case_graph=applied, lookup_result=receipt)

        unsafe_allowlist = copy.deepcopy(self.allowlist)
        unsafe_allowlist["entries"][0]["field_updates"][
            "sample_system_composition_declaration_status"
        ] = "DECLARED"
        with self.assertRaisesRegex(VerticalSliceError, "unauthorized target-field update"):
            execute_exact_source_lookup(
                allowlist=unsafe_allowlist,
                request=self._request("XEI-LOOKUP-RANDOM-DECLARATIONS"),
                workspace_root=REPO_ROOT,
            )

        duplicate_allowlist = copy.deepcopy(self.allowlist)
        duplicate_allowlist["entries"].append(copy.deepcopy(duplicate_allowlist["entries"][0]))
        with self.assertRaisesRegex(VerticalSliceError, "must be unique"):
            execute_exact_source_lookup(
                allowlist=duplicate_allowlist,
                request=self._request("XEI-LOOKUP-RANDOM-DECLARATIONS"),
                workspace_root=REPO_ROOT,
            )

    def test_lookup_fails_closed_when_the_frozen_derivative_hash_changes(self):
        altered_allowlist = copy.deepcopy(self.allowlist)
        altered_allowlist["entries"][0]["fixture_sha256"] = "0" * 64
        result = execute_exact_source_lookup(
            allowlist=altered_allowlist,
            request=self._request("XEI-LOOKUP-RANDOM-DECLARATIONS"),
            workspace_root=REPO_ROOT,
        )
        self.assertEqual(result["status"], "FIXTURE_HASH_MISMATCH")
        self.assertEqual(result["route"], "HUMAN_OR_NEW_DATA")
        self.assertEqual(
            result["reason_code"], "ALLOWLISTED_FIXTURE_HASH_MISMATCH"
        )


if __name__ == "__main__":
    unittest.main()
