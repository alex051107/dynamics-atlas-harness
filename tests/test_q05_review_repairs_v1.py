"""Real Q05 projection and counterfactual claim/lineage behavior; no science scores."""
import copy
import json
import tempfile
from pathlib import Path
import unittest

from dynamics_atlas_harness.paper_blind_exposed_v1 import (
    project_admitted_proposal_to_rules_casegraph, validate_agent_proposal,
    PaperBlindPublicPacketError,
)
from dynamics_atlas_harness.real_case_vertical_slice_v1 import load_rules_v1_bundle
from dynamics_atlas_harness.rules_prototype_v1 import evaluate_active_rules

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "evidence/paper_blind_exposed_v1/public/q05_public_fact_packet_v1.json"
PROPOSAL = ROOT / "research/paper_result_reproduction_screen_v1/q05_fact_proposal_v1.json"


class Q05ReviewRepairTests(unittest.TestCase):
    def setUp(self):
        proposal = json.loads(PROPOSAL.read_text())
        self.graph = project_admitted_proposal_to_rules_casegraph(
            PACKET, validate_agent_proposal(PACKET, proposal)
        )
        self.bundle = load_rules_v1_bundle(ROOT / "registries/rules_v1")

    def results(self, graph, subrule):
        return [r for r in evaluate_active_rules(case_graph=graph, **self.bundle)
                if r["runtime_subrule_id"] == subrule]

    def test_joint_fit_without_validation_claim_is_not_an_independence_test(self):
        for edge in self.graph["comparisons"]:
            self.assertEqual(edge["relation_type"], "JOINT_ENSEMBLE_FIT")
            self.assertNotIn("validation_claim", edge)
        results = self.results(self.graph, "F06R03_EDGE_VALIDATION_INDEPENDENCE")
        self.assertEqual(len(results), 2)
        self.assertTrue(all(r["status"] == "NOT_APPLICABLE" for r in results))

    def test_real_validation_claim_using_same_data_is_still_blocked(self):
        graph = copy.deepcopy(self.graph)
        for edge in graph["comparisons"]:
            edge.update(validation_claim="Independent validation of the fitted ensemble",
                        validation_independence="SAME_DATA",
                        shared_error_status="NO_MATERIAL_SHARED_ERROR_IDENTIFIED",
                        data_lineage_status="REVIEWED")
        results = self.results(graph, "F06R03_EDGE_VALIDATION_INDEPENDENCE")
        self.assertEqual(len(results), 2)
        self.assertTrue(all(r["status"] == "FAIL" for r in results))
        self.assertTrue(all("VALIDATION_INDEPENDENCE_CONTRADICTED" in r["reason_codes"]
                            for r in results))

    def test_unverified_lineage_remains_unresolved_with_specific_reason(self):
        results = self.results(self.graph, "F06R01_SOURCE_EVIDENCE_ROLE")
        self.assertEqual(len(results), 3)
        self.assertTrue(all(r["status"] == "UNRESOLVED" for r in results))
        self.assertTrue(all(r["reason_codes"] ==
                            ["SOURCE_PROPOSED_LINEAGE_REQUIRES_VERIFICATION"]
                            for r in results))
        for source in self.graph["evidence_items"]:
            self.assertEqual(source["data_lineage_status"], "AGENT_PROPOSED_UNVERIFIED")

    def test_contradicted_lineage_is_not_downgraded_to_unverified(self):
        graph = copy.deepcopy(self.graph)
        for source in graph["evidence_items"]:
            source["data_lineage_status"] = "CONTRADICTED"
        results = self.results(graph, "F06R01_SOURCE_EVIDENCE_ROLE")
        self.assertEqual(len(results), 3)
        self.assertTrue(all(r["status"] == "FAIL" for r in results))
        self.assertTrue(all("SOURCE_LINEAGE_CONTRADICTED" in r["reason_codes"]
                            for r in results))

    def project_packet(self, packet):
        with tempfile.TemporaryDirectory() as tmp:
            path = PACKET.parent / f"temporary_{Path(tmp).name}.json"
            try:
                path.write_text(json.dumps(packet))
                admitted = validate_agent_proposal(path, json.loads(PROPOSAL.read_text()))
                return project_admitted_proposal_to_rules_casegraph(path, admitted)
            finally:
                path.unlink(missing_ok=True)

    def test_platform_validation_request_survives_real_intake(self):
        for independence, lineage, expected in (
            ("INDEPENDENT", "REVIEWED", "PASS"),
            ("SAME_DATA", "REVIEWED", "FAIL"),
            ("UNKNOWN", "REVIEWED", "UNRESOLVED"),
            ("INDEPENDENT", None, "UNRESOLVED"),
        ):
            with self.subTest(independence=independence, lineage=lineage):
                packet = json.loads(PACKET.read_text())
                edges = packet["platform_authority_envelope"]["rules_projection_authority"]["comparisons"]
                for edge in edges:
                    edge.update(validation_claim="Independent validation of fitted ensemble",
                                validation_independence=independence,
                                shared_error_status="NO_MATERIAL_SHARED_ERROR_IDENTIFIED")
                    if lineage is not None:
                        edge["validation_lineage_status"] = lineage
                graph = self.project_packet(packet)
                results = self.results(graph, "F06R03_EDGE_VALIDATION_INDEPENDENCE")
                self.assertEqual(len(results), 2)
                self.assertEqual({r["status"] for r in results}, {expected})
                for edge in graph["comparisons"]:
                    self.assertEqual(edge["validation_claim"], edges[0]["validation_claim"])
                    self.assertEqual(edge["data_lineage_status"], lineage or "UNKNOWN")

    def test_lineage_without_request_is_rejected_at_intake(self):
        packet = json.loads(PACKET.read_text())
        packet["platform_authority_envelope"]["rules_projection_authority"]["comparisons"][0]["validation_lineage_status"] = "REVIEWED"
        with self.assertRaisesRegex(PaperBlindPublicPacketError, "INVALID_RULES_PROJECTION_VALIDATION_LINEAGE"):
            self.project_packet(packet)

    def test_joint_fit_does_not_gain_scientific_pass_from_declaration_repairs(self):
        graph = copy.deepcopy(self.graph)
        for source in graph["evidence_items"]:
            source["sample_system_composition_declaration_status"] = "DECLARED"
            source["native_measurement_declaration_status"] = "DECLARED"
        for edge in graph["comparisons"]:
            edge.update(condition_relation="MATCHED", bridge_status="DECLARED",
                        relation_type="QUALITATIVE_TRIANGULATION")
        control = self.results(graph, "F06R02_EDGE_COMPARABILITY")
        self.assertEqual(len(control), 2)
        self.assertEqual({r["status"] for r in control}, {"PASS"})
        for edge in graph["comparisons"]:
            edge["relation_type"] = "JOINT_ENSEMBLE_FIT"
        results = self.results(graph, "F06R02_EDGE_COMPARABILITY")
        self.assertEqual(len(results), 2)
        self.assertEqual({r["status"] for r in results}, {"UNRESOLVED"})


if __name__ == "__main__":
    unittest.main()
