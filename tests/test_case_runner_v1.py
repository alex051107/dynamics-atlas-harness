import hashlib
import json
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path
from unittest.mock import patch

from dynamics_atlas_harness import case_runner_v1 as runner
from dynamics_atlas_harness import exposed_paper_blind_capsule_v1 as capsule
from dynamics_atlas_harness.case_runner_v1 import (
    CaseRunnerV1Error,
    reevaluate_explicitly_linked_rule_results,
    run_case_v1,
)


def _canonical_sha256(value):
    encoded = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


class CaseRunnerV1Tests(unittest.TestCase):
    def test_registered_hsp90_and_adk_each_execute_the_one_selected_action(self):
        expected = {
            capsule.HSP90_PUBLIC_CASE_ID: "HSP90_GROUPED_OBSERVABLE_DEPENDENCE_DESCRIPTION_V1",
            capsule.ADK_PUBLIC_CASE_ID: "ADK_STATIC_REFERENCE_RELATIVE_PROXIMITY_DESCRIPTION_V1",
        }
        with tempfile.TemporaryDirectory() as tmp:
            for index, (case_id, card_id) in enumerate(expected.items()):
                root = Path(tmp) / f"case-{index}"
                manifest = run_case_v1(case_id=case_id, output_dir=root)
                self.assertEqual(manifest["authorization"]["selected_card_ids"], [card_id])
                self.assertEqual(manifest["authorization"]["executed_action_count"], 1)
                self.assertEqual(len(manifest["action_execution"]["evidence_results"]), 1)
                self.assertTrue((root / "actions" / card_id / "evidence_result.json").is_file())
                self.assertEqual(
                    manifest["rule_reevaluation"]["before_rule_results"],
                    manifest["rule_reevaluation"]["after_rule_results"],
                )
                self.assertEqual(
                    manifest["terminal_scientific_state"],
                    "NOT_CALCULATED_BY_CASE_RUNNER",
                )
                serialized = json.dumps(manifest, sort_keys=True)
                self.assertNotIn("/Users/", serialized)
                self.assertFalse(manifest["network_accessed"])
                self.assertFalse(manifest["credentials_accessed"])

                provenance = manifest["proposal_provenance"]
                self.assertEqual(set(provenance), {"profiler", "planner"})
                expected_visible_inputs = {
                    "profiler": capsule.build_agent_visible_packet(
                        runner._CASE_PACKET_REGISTRY[case_id]["packet"]
                    ),
                    "planner": manifest["planner_visible_input"],
                }
                expected_proposals = {
                    "profiler": json.loads(
                        runner._CASE_PACKET_REGISTRY[case_id]["profile_proposal"].read_text(
                            encoding="utf-8"
                        )
                    ),
                    "planner": json.loads(
                        runner._CASE_PACKET_REGISTRY[case_id]["planner_proposal"].read_text(
                            encoding="utf-8"
                        )
                    ),
                }
                for role in ("profiler", "planner"):
                    receipt = provenance[role]
                    artifact_path = root / f"{role}_proposal_provenance.json"
                    self.assertTrue(artifact_path.is_file())
                    self.assertEqual(json.loads(artifact_path.read_text()), receipt)
                    self.assertEqual(receipt["mode"], "RECORDED_PROPOSAL_REPLAY")
                    self.assertEqual(
                        receipt["visible_input"]["canonical_sha256"],
                        _canonical_sha256(expected_visible_inputs[role]),
                    )
                    self.assertEqual(
                        receipt["parsed_proposal"]["canonical_sha256"],
                        _canonical_sha256(expected_proposals[role]),
                    )
                    self.assertIsNone(receipt["provider"]["provider_id"])
                    self.assertEqual(
                        receipt["provider"]["status"], "UNAVAILABLE_NOT_RECORDED"
                    )
                    self.assertIsNone(receipt["model"]["model_id"])
                    self.assertIsNone(receipt["prompt"]["sha256"])
                    self.assertIsNone(receipt["raw_response"]["sha256"])
                    self.assertIsNone(receipt["recorded_timestamp"])
                    self.assertIsNone(receipt["reported_cost"])
                    self.assertFalse(Path(receipt["source_path"]).is_absolute())
                    self.assertNotIn("/Users/", json.dumps(receipt, sort_keys=True))
                self.assertIn(
                    "profiler_proposal_provenance.json", manifest["artifact_paths"]
                )
                self.assertIn(
                    "planner_proposal_provenance.json", manifest["artifact_paths"]
                )

    def test_abstention_executes_zero_actions(self):
        proposal = {
            "case_id": capsule.HSP90_PUBLIC_CASE_ID,
            "decision": "ABSTAIN_NO_ACTION",
            "selected_card_ids": [],
            "rationales": {},
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "abstain"
            manifest = run_case_v1(
                case_id=capsule.HSP90_PUBLIC_CASE_ID,
                output_dir=root,
                planner_proposal=proposal,
            )
            self.assertEqual(manifest["authorization"]["executed_action_count"], 0)
            self.assertEqual(manifest["action_execution"]["evidence_results"], [])
            self.assertFalse((root / "actions").exists())
            planner_receipt = manifest["proposal_provenance"]["planner"]
            self.assertEqual(planner_receipt["mode"], "CALLER_SUPPLIED_IN_MEMORY")
            self.assertIsNone(planner_receipt["source_path"])
            self.assertEqual(
                planner_receipt["source_path_status"],
                "UNAVAILABLE_CALLER_SUPPLIED_IN_MEMORY",
            )

    def test_stale_card_fails_before_any_action_artifact(self):
        stale = deepcopy(dict(capsule._ACTION_CARD_SPECS[0]))
        stale["addresses_ref"] = (
            "F06R02_EDGE_COMPARABILITY::EDGE::HSP90_NMR_MD_CONFORMATIONAL_RELATION"
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "stale"
            with patch.object(runner, "_ACTION_CARD_SPECS", (stale, capsule._ACTION_CARD_SPECS[1])):
                with self.assertRaisesRegex(CaseRunnerV1Error, "SELECTED_ACTION_CARD_NOT_FRESH"):
                    run_case_v1(case_id=capsule.HSP90_PUBLIC_CASE_ID, output_dir=root)
            self.assertTrue(root.is_dir())
            self.assertEqual(list(root.rglob("*")), [])

    def test_cross_case_card_fails_before_any_action_artifact(self):
        proposal = {
            "case_id": capsule.HSP90_PUBLIC_CASE_ID,
            "decision": "SELECT_ACTIONS",
            "selected_card_ids": ["ADK_STATIC_REFERENCE_RELATIVE_PROXIMITY_DESCRIPTION_V1"],
            "rationales": {
                "ADK_STATIC_REFERENCE_RELATIVE_PROXIMITY_DESCRIPTION_V1": "wrong case"
            },
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "cross-case"
            with self.assertRaisesRegex(CaseRunnerV1Error, "SELECTED_ACTION_CARD_CROSS_CASE"):
                run_case_v1(
                    case_id=capsule.HSP90_PUBLIC_CASE_ID,
                    output_dir=root,
                    planner_proposal=proposal,
                )
            self.assertTrue(root.is_dir())
            self.assertEqual(list(root.rglob("*")), [])

    def test_descriptive_evidence_cannot_forge_rule_pass(self):
        forged = {
            "schema_version": "forged-descriptive-result/v1",
            "rule_effect": "NO_ACTIVE_RULE_EFFECT",
            "contract_status": "PASS",
        }
        card_id = "HSP90_GROUPED_OBSERVABLE_DEPENDENCE_DESCRIPTION_V1"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "forged"
            with patch.dict(capsule._CARD_EXECUTORS, {card_id: lambda: forged}):
                with self.assertRaisesRegex(
                    CaseRunnerV1Error, "DESCRIPTIVE_EVIDENCE_CANNOT_FORGE_RULE_PASS"
                ):
                    run_case_v1(case_id=capsule.HSP90_PUBLIC_CASE_ID, output_dir=root)
            self.assertTrue(root.is_dir())
            self.assertEqual(list(root.rglob("*")), [])

    def test_active_evidence_reevaluates_only_its_explicit_same_rule_instance(self):
        before = [
            {"rule_instance_id": "RULE::A", "status": "UNRESOLVED"},
            {"rule_instance_id": "RULE::B", "status": "UNRESOLVED"},
        ]
        evidence = {
            "evidence_result_id": "EVIDENCE::A",
            "case_id": "CASE::TEST",
            "affected_rule_instance_id": "RULE::A",
            "contract_status": "PASS",
        }

        def reevaluate_a(rule_result, evidence_result):
            self.assertEqual(evidence_result["affected_rule_instance_id"], "RULE::A")
            return {**rule_result, "status": "PASS"}

        result = reevaluate_explicitly_linked_rule_results(
            case_id="CASE::TEST",
            before_rule_results=before,
            evidence_results=[evidence],
            reevaluators={"RULE::A": reevaluate_a},
        )
        self.assertEqual(
            {item["rule_instance_id"]: item["status"] for item in result["after_rule_results"]},
            {"RULE::A": "PASS", "RULE::B": "UNRESOLVED"},
        )
        self.assertEqual(result["reevaluated_rule_instance_ids"], ["RULE::A"])
        self.assertTrue(result["evidence_links"][0]["same_rule_instance"])

        with self.assertRaisesRegex(CaseRunnerV1Error, "REEVALUATOR_CHANGED_RULE_INSTANCE_ID"):
            reevaluate_explicitly_linked_rule_results(
                case_id="CASE::TEST",
                before_rule_results=before,
                evidence_results=[evidence],
                reevaluators={
                    "RULE::A": lambda rule_result, _: {
                        **rule_result,
                        "rule_instance_id": "RULE::B",
                        "status": "PASS",
                    }
                },
            )


if __name__ == "__main__":
    unittest.main()
