import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).parents[2]
RULES_ROOT = REPO_ROOT / "registries" / "rules_v1"
SCHEMAS_ROOT = REPO_ROOT / "schemas" / "rules_v1"


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def collect_predicate_ops(expression):
    operations = {expression["op"]}
    if expression["op"] in {"ALL", "ANY"}:
        for argument in expression["args"]:
            operations.update(collect_predicate_ops(argument))
    elif expression["op"] == "NOT":
        operations.update(collect_predicate_ops(expression["arg"]))
    return operations


def collect_predicate_paths(expression):
    paths = {
        expression[key]
        for key in ("path", "values_path")
        if isinstance(expression.get(key), str)
    }
    if expression["op"] in {"ALL", "ANY"}:
        for argument in expression["args"]:
            paths.update(collect_predicate_paths(argument))
    elif expression["op"] == "NOT":
        paths.update(collect_predicate_paths(expression["arg"]))
    return paths


class PathRegistryTests(unittest.TestCase):
    def test_every_binding_path_has_a_classified_owner(self):
        registry = read_json(RULES_ROOT / "path_registry_v1.json")
        bindings = read_json(RULES_ROOT / "applicability_bindings_v1.json")
        contracts = read_json(RULES_ROOT / "evaluation_contracts_v1.json")
        known_paths = {item["canonical_path"] for item in registry["paths"]}
        self.assertIn("evaluation_context.rule_results_by_instance", known_paths)
        self.assertFalse(
            any(
                path.startswith("edge.prerequisite_rule_results")
                for path in known_paths
            )
        )
        self.assertTrue(
            {
                "CURRENT_CASEGRAPH_FIELD",
                "DERIVED_FIELD",
                "VNEXT_CASEGRAPH_FIELD",
                "POST_OPERATOR_FIELD",
                "POST_EVALUATION_FIELD",
            }.issubset(set(registry["classification_vocabulary"]))
        )
        for item in registry["paths"]:
            self.assertIn(item["classification"], registry["classification_vocabulary"])
            self.assertTrue(item["owner"])
            self.assertTrue(item["migration_or_derivation"])
        for binding in bindings["bindings"]:
            with self.subTest(binding=binding["binding_id"]):
                binding_paths = set(binding["required_evidence_paths"])
                binding_paths.update(collect_predicate_paths(binding["applicability"]))
                binding_paths.discard("target.kind")
                self.assertTrue(binding_paths.issubset(known_paths))

        for contract in contracts["contracts"]:
            with self.subTest(contract=contract["evaluation_contract_id"]):
                condition_paths = set()
                for field in ("pass_conditions", "fail_conditions", "unresolved_conditions"):
                    for entry in contract[field]:
                        condition_paths.update(collect_predicate_paths(entry["condition"]))
                condition_paths.discard("target.kind")
                self.assertTrue(condition_paths.issubset(known_paths))

    def test_binding_grammar_uses_only_implemented_primitives(self):
        bindings = read_json(RULES_ROOT / "applicability_bindings_v1.json")
        grammar = bindings["grammar"]
        allowed_predicates = set(grammar["predicate_primitives"])
        self.assertIn("PRIOR_RESULT_STATUS", allowed_predicates)
        for binding in bindings["bindings"]:
            self.assertTrue(
                collect_predicate_ops(binding["applicability"]).issubset(allowed_predicates)
            )
            if binding["target_kind"] == "CASE":
                self.assertNotIn("iteration", binding)
            else:
                self.assertIn(binding["iteration"]["op"], grammar["iteration_primitives"])

        contracts = read_json(RULES_ROOT / "evaluation_contracts_v1.json")
        for contract in contracts["contracts"]:
            with self.subTest(contract=contract["evaluation_contract_id"]):
                for field in ("pass_conditions", "fail_conditions", "unresolved_conditions"):
                    for entry in contract[field]:
                        self.assertTrue(
                            collect_predicate_ops(entry["condition"]).issubset(allowed_predicates)
                        )

    def test_requested_schema_files_exist_and_name_required_fields(self):
        expected = {
            "rule_family.schema.json": "family_id",
            "runtime_subrule.schema.json": "runtime_subrule_id",
            "applicability_binding.schema.json": "binding_id",
            "resolution_policy.schema.json": "resolution_policy_id",
            "evaluation_contract.schema.json": "evaluation_contract_id",
            "source_evidence_packet.schema.json": "evidence_packet_id",
        }
        for filename, field in expected.items():
            with self.subTest(schema=filename):
                schema = read_json(SCHEMAS_ROOT / filename)
                self.assertIn(field, schema["required"])

        contract_schema = read_json(SCHEMAS_ROOT / "evaluation_contract.schema.json")
        self.assertTrue(
            {"pass_conditions", "fail_conditions", "unresolved_conditions"}.issubset(
                set(contract_schema["required"])
            )
        )


if __name__ == "__main__":
    unittest.main()
