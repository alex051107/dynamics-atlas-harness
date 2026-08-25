import json
import tempfile
import unittest
from pathlib import Path

from dynamics_atlas_harness.cli import main
from dynamics_atlas_harness.evaluation import (
    build_evaluation_contract,
    evaluate_current_bundle,
)
from dynamics_atlas_harness.registered_operators import (
    load_registered_operator_registry,
    probe_operator,
)


REPO_ROOT = Path(__file__).parents[1]
WORKSPACE_ROOT = REPO_ROOT.parent
HAS_WORKSPACE_ASSETS = (WORKSPACE_ROOT / "autoresearch").is_dir()


class TargetArchitectureTests(unittest.TestCase):
    def test_sufficient_contract_takes_direct_bounded_route(self):
        case_graph = {
            "case": {
                "case_id": "direct-contract-fixture",
                "scientific_claim": "Is the declared review bundle complete?",
                "requested_claim_level": "SOURCE_LOCAL_CONSISTENCY",
            }
        }
        selector_output = {
            "authority_boundary": {"claim_ceiling": "REVIEW_OBLIGATIONS_ONLY"},
            "obligations": [
                {
                    "obligation_id": "obligation-1",
                    "rule_id": "rule-1",
                    "target": {"target_type": "CASE"},
                    "claim_scope": "SOURCE_LOCAL_CONSISTENCY",
                    "required_check": "Check one frozen field.",
                    "evidence_evaluation_required": True,
                }
            ],
            "unresolved_inputs": [],
        }
        contract = build_evaluation_contract(case_graph, selector_output)
        result = evaluate_current_bundle(
            contract=contract,
            selector_output=selector_output,
            evidence_results=[
                {
                    "obligation_id": "obligation-1",
                    "contract_status": "ACCEPTED_BY_CONTRACT",
                }
            ],
        )
        self.assertEqual(result["branch"], "DIRECT_BOUNDED_RESULT")
        self.assertEqual(result["bundle_status"], "SUFFICIENT_FOR_DECLARED_CONTRACT")
        self.assertEqual(result["review_status"], "HUMAN_REVIEW_REQUIRED")

    @unittest.skipUnless(HAS_WORKSPACE_ASSETS, "requires the Dynamics Atlas workspace")
    def test_mdanalysis_operator_is_registered_but_runtime_blocked(self):
        registry = load_registered_operator_registry(
            REPO_ROOT / "config" / "registered_operators.json"
        )
        spec = registry["operators"]["trajectory.structural_state_projection.v1"]
        probe = probe_operator(spec, WORKSPACE_ROOT)
        self.assertEqual(probe["status"], "BLOCKED")
        self.assertTrue(
            any(
                code.startswith("PYTHON_PACKAGE_UNAVAILABLE:MDAnalysis")
                for code in probe["reason_codes"]
            )
        )

    @unittest.skipUnless(HAS_WORKSPACE_ASSETS, "requires the Dynamics Atlas workspace")
    def test_actual_case_selector_runplan_and_existing_operator_canary(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "target-run"
            code = main(
                [
                    "run-prototype",
                    "--workspace-root",
                    str(WORKSPACE_ROOT),
                    "--output-dir",
                    str(output),
                    "--run-id",
                    "test-target-architecture",
                ]
            )
            self.assertEqual(code, 0)
            summary = json.loads((output / "run_summary.json").read_text())
            self.assertEqual(summary["profile_status"], "PROFILE_READY")
            self.assertEqual(summary["rules_selector"], "EXISTING_SELECTOR_INVOKED")
            # Bind these counts to the actual v0.3 index, not the older 51/17 snapshot.
            self.assertEqual(summary["obligation_count"], 59)
            self.assertEqual(summary["unresolved_input_count"], 15)
            self.assertEqual(summary["evaluation_branch"], "RUN_PLAN_REQUIRED")
            self.assertEqual(summary["case_flow_status"], "RUN_PLAN_BLOCKED")
            self.assertEqual(summary["registered_operator_canary_status"], "SUCCEEDED")
            self.assertEqual(summary["semantic_correctness"], "NOT_EVALUATED")

            plan = json.loads((output / "run_plan.json").read_text())
            self.assertEqual(plan["schema_version"], "run-plan/v0.1")
            self.assertGreater(plan["blocked_gap_count"], 0)
            self.assertTrue(
                all(
                    edge["edge_kind"] == "EXECUTION_DEPENDENCY"
                    for edge in plan["execution_edges"]
                )
            )
            self.assertEqual(
                plan["scientific_evidence_edges_source"],
                "CASE_GRAPH_COMPARISONS_NOT_COPIED_HERE",
            )

            receipt = json.loads(
                (output / "operator_canary" / "operator_run_receipt.json").read_text()
            )
            self.assertEqual(receipt["operator_id"], "hsp90.directional_time_anatomy.v0")
            self.assertEqual(receipt["status"], "SUCCEEDED")
            self.assertEqual(receipt["fixed_parameters"]["persistence_saved_frames"], [5, 20, 50])
            evidence = json.loads(
                (output / "operator_canary" / "evidence_result.json").read_text()
            )
            self.assertEqual(evidence["evaluation_status"], "PENDING_HUMAN_VALIDATION")
            self.assertIn("Does not estimate a transition rate", evidence["result"]["forbidden_wording"])


if __name__ == "__main__":
    unittest.main()
