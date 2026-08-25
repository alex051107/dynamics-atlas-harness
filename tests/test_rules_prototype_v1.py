import csv
import json
import unittest
from collections import Counter
from pathlib import Path

from dynamics_atlas_harness.runplan import build_run_plan


REPO_ROOT = Path(__file__).parents[1]
RULES_DIR = REPO_ROOT / "rules_prototype" / "v1"


def read_json(name: str):
    return json.loads((RULES_DIR / name).read_text(encoding="utf-8"))


class RulesPrototypeV1Tests(unittest.TestCase):
    def test_exact_eight_seed_families_have_complete_review_contracts(self):
        registry = read_json("seed_rule_registry_v1.json")
        seeds = registry["seed_families"]
        with (RULES_DIR / "legacy_33_rule_reaudit.csv").open(
            newline="", encoding="utf-8"
        ) as handle:
            legacy_by_rule = {
                row["rule_id"]: row for row in csv.DictReader(handle)
            }
        self.assertEqual(registry["status"], "PROPOSAL_ONLY_NOT_RUNTIME_ACTIVE")
        self.assertEqual(registry["active_seed_family_count"], 8)
        self.assertEqual([seed["seed_id"] for seed in seeds], [f"SP{i:02d}" for i in range(1, 9)])

        required = {
            "seed_id",
            "family_name",
            "source_family_ids",
            "runtime_targets",
            "reusable_question",
            "source_anchors",
            "positive_fixture",
            "one_field_negative_fixture",
            "blocking_priority",
            "required_evidence",
            "resolution_policy_id",
            "evaluation_contract_id",
            "outcome_effects",
            "claim_ceiling",
        }
        for seed in seeds:
            self.assertTrue(required.issubset(seed), seed["seed_id"])
            self.assertTrue(seed["source_anchors"], seed["seed_id"])
            for anchor in seed["source_anchors"]:
                legacy = legacy_by_rule[anchor["rule_id"]]
                self.assertEqual(anchor["paper_id"], legacy["paper_id"])
                self.assertEqual(anchor["source_locator"], legacy["source_locator"])
                self.assertTrue(anchor["source_locator"])
                self.assertTrue(anchor["source_passage_summary"])
                self.assertEqual(
                    anchor["passage_kind"], "UPSTREAM_AUTHORING_SUMMARY_NOT_VERBATIM"
                )
            self.assertEqual(set(seed["outcome_effects"]), {"PASS", "FAIL", "UNRESOLVED"})

            positive = seed["positive_fixture"]["input"]
            negative_record = seed["one_field_negative_fixture"]
            negative = negative_record["input"]
            changed = [key for key in positive if positive[key] != negative[key]]
            self.assertEqual(set(positive), set(negative), seed["seed_id"])
            self.assertEqual(changed, [negative_record["changed_path"]], seed["seed_id"])
            self.assertEqual(seed["positive_fixture"]["expected_outcome"], "PASS")
            self.assertEqual(negative_record["expected_outcome"], "UNRESOLVED")

    def test_methodology_exclusions_and_legacy_audit_are_preserved(self):
        methodology = read_json("methodology_map_v1.json")
        families = {row["family_id"]: row for row in methodology["families"]}
        self.assertEqual(set(families), {f"RF{i:02d}" for i in range(1, 15)})
        self.assertEqual(families["RF02"]["prototype_disposition"], "CANDIDATE_PENDING_PRIMARY_CASE")
        self.assertEqual(families["RF07"]["prototype_disposition"], "CANDIDATE_PENDING_MD_REPLAY")
        self.assertEqual(families["RF12"]["prototype_disposition"], "SYSTEM_COMPONENT")

        with (RULES_DIR / "legacy_33_rule_reaudit.csv").open(
            newline="", encoding="utf-8"
        ) as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 33)
        self.assertEqual(
            Counter(row["disposition"] for row in rows),
            Counter({"KEEP": 13, "MERGE": 11, "REVISE": 7, "DEFER": 2}),
        )

    def test_binding_policy_and_evaluation_references_resolve(self):
        seeds = read_json("seed_rule_registry_v1.json")["seed_families"]
        bindings = read_json("seed_bindings_v1.json")
        policies = read_json("resolution_policies_v1.json")
        contracts = read_json("evaluation_contracts_v1.json")
        seed_ids = {seed["seed_id"] for seed in seeds}
        policy_ids = {item["resolution_policy_id"] for item in policies["policies"]}
        contract_ids = {
            item["evaluation_contract_id"] for item in contracts["contracts"]
        }

        self.assertEqual(len(bindings["bindings"]), 8)
        self.assertEqual({item["seed_id"] for item in bindings["bindings"]}, seed_ids)
        self.assertEqual({item["seed_id"] for item in contracts["contracts"]}, seed_ids)
        for seed in seeds:
            self.assertIn(seed["resolution_policy_id"], policy_ids)
            self.assertIn(seed["evaluation_contract_id"], contract_ids)
        for binding in bindings["bindings"]:
            self.assertEqual(binding["activation_status"], "HUMAN_REVIEW_REQUIRED")
            self.assertIn(binding["resolution_policy_id"], policy_ids)
            self.assertIn(binding["evaluation_contract_id"], contract_ids)

    def test_only_roster_pass_operator_can_be_routed(self):
        case_graph = {
            "evidence_items": [{"source_id": "source-md", "method_id": "MD_TRAJECTORY"}]
        }
        evaluation = {
            "branch": "RUN_PLAN_REQUIRED",
            "case_id": "operator-lifecycle-test",
            "gaps": [
                {
                    "gap_class": "NOT_EVALUATED",
                    "input_path": "source.time_semantics",
                    "target": {"target_type": "SOURCE", "source_ids": ["source-md"]},
                }
            ],
        }
        canary_spec = {
            "status": "CANARY_PASS",
            "routable": False,
            "route_match": {
                "gap_classes": ["NOT_EVALUATED"],
                "target_types": ["SOURCE"],
                "method_ids": ["MD_TRAJECTORY"],
                "input_path_contains": ["time_semantics"],
            },
        }
        blocked = build_run_plan(
            run_id="canary-not-routable",
            case_graph=case_graph,
            evaluation=evaluation,
            operator_registry={"operators": {"candidate": canary_spec}},
        )
        self.assertEqual(blocked["status"], "BLOCKED")

        roster_spec = dict(canary_spec, status="ROSTER_PASS", routable=True)
        ready = build_run_plan(
            run_id="roster-routable",
            case_graph=case_graph,
            evaluation=evaluation,
            operator_registry={"operators": {"candidate": roster_spec}},
        )
        self.assertEqual(ready["status"], "READY")
        gap_node = next(node for node in ready["nodes"] if node["node_type"] == "RESOLVE_GAP")
        self.assertEqual(gap_node["operator_id"], "candidate")


if __name__ == "__main__":
    unittest.main()
