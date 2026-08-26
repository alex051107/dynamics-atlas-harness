import json
import tempfile
import unittest
from pathlib import Path

from dynamics_atlas_harness.cli import build_parser, main
from dynamics_atlas_harness.evaluation import (
    build_evaluation_contract,
    evaluate_current_bundle,
)
from dynamics_atlas_harness.registered_operators import (
    load_registered_operator_registry,
    probe_operator,
)
from dynamics_atlas_harness.runplan import build_run_plan


REPO_ROOT = Path(__file__).parents[1]
WORKSPACE_ROOT = REPO_ROOT.parent
HAS_WORKSPACE_ASSETS = (WORKSPACE_ROOT / "autoresearch").is_dir()


class TargetArchitectureTests(unittest.TestCase):
    def test_operator_canary_is_opt_in(self):
        args = build_parser().parse_args(
            [
                "run-prototype",
                "--workspace-root",
                str(WORKSPACE_ROOT),
                "--output-dir",
                "/tmp/unused-target-run",
            ]
        )
        self.assertIsNone(args.canary_operator_id)

    def test_legacy_fixture_registry_is_not_case_routing_registry(self):
        fixture_registry = json.loads(
            (REPO_ROOT / "config" / "operators.json").read_text(encoding="utf-8")
        )
        self.assertEqual(fixture_registry["registry_role"], "LEGACY_FIXTURE_ONLY")
        self.assertEqual(fixture_registry["runtime_scope"], "RUN_FIXTURE_COMMAND_ONLY")
        self.assertIs(fixture_registry["case_routing_allowed"], False)

    def test_registered_operator_loader_enforces_lifecycle_invariants(self):
        current = load_registered_operator_registry(
            REPO_ROOT / "config" / "registered_operators.json"
        )
        self.assertEqual(
            current["registry_id"], "dynamics-atlas-registered-operators/v0.2"
        )

        valid_roster = {
            "operator_id": "fixture.roster.v1",
            "status": "ROSTER_PASS",
            "routable": True,
            "output_contract": "fixture-output/v1",
            "route_match": {"gap_classes": ["NOT_EVALUATED"]},
            "claim_ceiling": "Fixture-only bounded claim.",
        }
        invalid_specs = (
            (
                "NON_ROSTER_ROUTABLE",
                {**valid_roster, "status": "CANARY_PASS", "routable": True},
            ),
            (
                "ROSTER_NOT_ROUTABLE",
                {**valid_roster, "routable": False},
            ),
            (
                "ROSTER_PROMOTION_BLOCKERS_PRESENT",
                {**valid_roster, "promotion_blockers": ["OUTPUT_SCHEMA_PENDING"]},
            ),
            (
                "ROSTER_MISSING_OUTPUT_CONTRACT",
                {**valid_roster, "output_contract": ""},
            ),
            (
                "ROSTER_MISSING_ROUTE_MATCH",
                {**valid_roster, "route_match": {}},
            ),
            (
                "ROSTER_MISSING_CLAIM_CEILING",
                {**valid_roster, "claim_ceiling": ""},
            ),
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            registry_path = Path(temp_dir) / "registered_operators.json"

            def write_registry(spec):
                registry_path.write_text(
                    json.dumps(
                        {
                            "schema_version": "scientific-operator-registry/v0.2",
                            "registry_id": "lifecycle-fixture/v0.1",
                            "operators": {"fixture.roster.v1": spec},
                        }
                    ),
                    encoding="utf-8",
                )

            write_registry(valid_roster)
            loaded = load_registered_operator_registry(registry_path)
            self.assertEqual(
                loaded["operators"]["fixture.roster.v1"]["status"], "ROSTER_PASS"
            )

            for reason, spec in invalid_specs:
                with self.subTest(reason=reason):
                    write_registry(spec)
                    with self.assertRaisesRegex(ValueError, reason):
                        load_registered_operator_registry(registry_path)

    def test_only_roster_pass_and_routable_operator_can_route(self):
        case_graph = {
            "evidence_items": [
                {"source_id": "source-md", "method_id": "MD_TRAJECTORY"}
            ]
        }
        evaluation = {
            "branch": "RUN_PLAN_REQUIRED",
            "case_id": "operator-lifecycle-test",
            "gaps": [
                {
                    "gap_class": "NOT_EVALUATED",
                    "input_path": "source.time_semantics",
                    "target": {
                        "target_type": "SOURCE",
                        "source_ids": ["source-md"],
                    },
                }
            ],
        }
        route_match = {
            "gap_classes": ["NOT_EVALUATED"],
            "target_types": ["SOURCE"],
            "method_ids": ["MD_TRAJECTORY"],
            "input_path_contains": ["time_semantics"],
        }

        for status, routable in (
            ("CANARY_PASS", False),
            ("CANARY_PASS", True),
            ("REGISTERED_BLOCKED", False),
            ("SOFTWARE_CANARY_PASS", True),
            ("ROSTER_PASS", False),
        ):
            with self.subTest(status=status, routable=routable):
                plan = build_run_plan(
                    run_id=f"blocked-{status}-{routable}",
                    case_graph=case_graph,
                    evaluation=evaluation,
                    operator_registry={
                        "operators": {
                            "candidate": {
                                "status": status,
                                "routable": routable,
                                "route_match": route_match,
                            }
                        }
                    },
                )
                self.assertEqual(plan["status"], "BLOCKED")
                self.assertEqual(plan["blocked_gap_count"], 1)

        ready = build_run_plan(
            run_id="roster-pass-routable",
            case_graph=case_graph,
            evaluation=evaluation,
            operator_registry={
                "operators": {
                    "candidate": {
                        "status": "ROSTER_PASS",
                        "routable": True,
                        "route_match": route_match,
                    }
                }
            },
        )
        self.assertEqual(ready["status"], "READY")
        gap_node = next(
            node for node in ready["nodes"] if node["node_type"] == "RESOLVE_GAP"
        )
        self.assertEqual(gap_node["operator_id"], "candidate")

    def test_exact_case_bound_operator_cannot_route_another_case(self):
        registry = load_registered_operator_registry(
            REPO_ROOT / "config" / "registered_operators.json"
        )
        case_graph = {
            "case": {"case_id": "unrelated-md-development-case"},
            "evidence_items": [
                {
                    "source_id": "hsp90_md_round2_directional_packet",
                    "method_id": "MD_TRAJECTORY",
                    "method_profile_id": "hsp90_md_directional_time_anatomy_v0",
                }
            ],
        }
        evaluation = {
            "branch": "RUN_PLAN_REQUIRED",
            "gaps": [
                {
                    "runtime_subrule_id": "F04R02_SOURCE_DECLARED_TIME_ANATOMY_CONTROL",
                    "gap_class": "COMPUTABLE_TIME_ANATOMY_CONTROL_EVIDENCE_MISSING",
                    "input_path": "source.time_semantics.time_anatomy_control",
                    "target": {
                        "target_type": "SOURCE",
                        "source_ids": ["hsp90_md_round2_directional_packet"],
                    },
                }
            ],
        }
        plan = build_run_plan(
            run_id="wrong-case-must-not-route",
            case_graph=case_graph,
            evaluation=evaluation,
            operator_registry={
                "operators": {
                    "hsp90.directional_time_anatomy.v1_case_bound": registry[
                        "operators"
                    ]["hsp90.directional_time_anatomy.v1_case_bound"]
                }
            },
        )
        self.assertEqual(plan["status"], "BLOCKED")
        gap_node = next(
            node for node in plan["nodes"] if node["node_type"] == "RESOLVE_GAP"
        )
        self.assertEqual(gap_node["reason_codes"], ["NO_REGISTERED_OPERATOR_FOR_GAP"])

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
                    "--canary-operator-id",
                    "hsp90.directional_time_anatomy.v0",
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
            self.assertEqual(plan["blocked_gap_count"], 16)
            self.assertEqual(summary["case_gap_resolution_operator_count"], 0)
            self.assertEqual(
                summary["operator_canary_relation"],
                "INDEPENDENT_REGISTRY_CANARY_NOT_ROUTED_FROM_CASE_PLAN",
            )
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
