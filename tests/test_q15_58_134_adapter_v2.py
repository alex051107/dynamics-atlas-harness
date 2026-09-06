"""Focused regression tests for the bounded 58/134 source-adapter repair."""

import copy
import importlib.util
from pathlib import Path
import unittest

from dynamics_atlas_harness import q15_apbs_comparison_v1 as q15


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"


def load_script(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


reader = load_script("run_q15_58_134_frozen_reuse_v2")
bridge = load_script("run_q15_58_134_forward_bridge_v2")


def member_map():
    counts = {("58_134_apo", "repetion_1"): 12, ("58_134_apo", "repetion_2"): 14, ("58_134_apo", "repetion_3"): 12,
              ("58_134_1mM_SA", "repetion_1"): 24, ("58_134_1mM_SA", "repetion_2"): 12, ("58_134_1mM_SA", "repetion_3"): 12}
    selected, combined = [], []
    index = 0
    for (directory, repetition), total in counts.items():
        for number in range(total):
            name = f"Figure3/{directory}/{repetition}/{number:03d}__apbs_alex.csv"
            member = {"name": name, "crc32": f"{index:08x}", "expanded_bytes": index + 100}
            selected.append(member)
            combined.append({"member": dict(member), "status": "LOCAL_HEADER_CENTRAL_CRC_LENGTH_MATCH", "condition_directory": directory, "source_repetition": repetition, "path": f"source_members/{name}"})
            index += 1
        name = f"Figure3/{directory}/{repetition}/background_bkg.csv"
        member = {"name": name, "crc32": f"{index:08x}", "expanded_bytes": index + 100}
        selected.append(member)
        combined.append({"member": dict(member), "status": "LOCAL_HEADER_CENTRAL_CRC_LENGTH_MATCH", "condition_directory": directory, "source_repetition": repetition, "path": f"source_members/{name}"})
        index += 1
    return selected, combined


def repetitions():
    rows = []
    for condition, means, medians in (("apo", [.2, .4, .6], [.6, .6, .6]), ("holo", [.4, .6, .8], [.2, .2, .2])):
        for index, (mean, median) in enumerate(zip(means, medians), 1):
            rows.append({"pair": "58_134", "condition": condition, "repetition": f"repetion_{index}", "E": {"mean": mean, "median": median}})
    return rows


class AdapterV2Test(unittest.TestCase):
    def test_member_assignment_and_complete_unique_set_are_required(self):
        selected, combined = member_map()
        apbs, groups = reader.validate_admitted_member_map(selected, combined)
        self.assertEqual(len(apbs), 86)
        self.assertEqual(len(groups), 6)
        swapped = copy.deepcopy(combined)
        swapped[0]["condition_directory"] = "58_134_1mM_SA"
        with self.assertRaisesRegex(ValueError, "SOURCE_ASSIGNMENT_RECEIPT_MISMATCH"):
            reader.validate_admitted_member_map(selected, swapped)
        duplicate = copy.deepcopy(combined)
        duplicate[-1]["member"] = dict(duplicate[0]["member"])
        with self.assertRaisesRegex(ValueError, "SELECTED_OR_RECEIPT_MEMBER_SET_NOT_UNIQUE"):
            reader.validate_admitted_member_map(selected, duplicate)

    def test_historical_median_statistic_is_not_median_of_repetition_means(self):
        rows = repetitions()
        comparison = q15.group_difference(rows)["58_134"]
        diagnostic = reader.direction_diagnostics(rows, comparison)
        self.assertAlmostEqual(diagnostic["equal_repetition_median_effect"], -.4)
        self.assertAlmostEqual(float(__import__("numpy").median(comparison["holo_repetition_means"]) - __import__("numpy").median(comparison["apo_repetition_means"])), .2)
        self.assertEqual(diagnostic["definition"], "mean(within-repetition E.median) holo minus apo; retained from q15_pro19_verification_v1")

    def test_bridge_rebuild_rejects_altered_or_minimal_producer_report(self):
        selected, combined = member_map()
        expected_members, raw_groups = reader.validate_admitted_member_map(selected, combined)
        expected_members = [{key: row[key] for key in ("name", "crc32", "expanded_bytes")} for row in expected_members]
        expected_groups = {"/".join(key): {role: sorted(value) for role, value in values.items()} for key, values in sorted(raw_groups.items())}
        rows = repetitions()
        comparison = q15.group_difference(rows)["58_134"]
        report = {"version": "q15-58-134-frozen-reuse/v2", "frozen_policy": q15.POLICY,
                  "source_receipts": ["q15_58_134_full_input_intake_v1/retry1_receipt.json", "q15_58_134_full_input_intake_v1/input_quality_report.json"],
                  "source_selection": {"pair": "58_134", "member_identity": expected_members, "apbs_members": 86},
                  "source_assignment": {"groups": expected_groups}, "repetitions": rows,
                  "condition_comparisons": {"58_134": comparison}, "diagnostics": {"58_134": bridge._diagnostics(rows, comparison)}}
        rebuilt, diagnostic = bridge.validate_producer_report(report, expected_members, expected_groups)
        self.assertEqual(rebuilt, comparison)
        self.assertEqual(diagnostic, report["diagnostics"]["58_134"])
        altered = copy.deepcopy(report)
        altered["condition_comparisons"]["58_134"]["holo_minus_apo_E"] = -1
        with self.assertRaisesRegex(ValueError, "PRODUCER_COMPARISON_MISMATCH"):
            bridge.validate_producer_report(altered, expected_members, expected_groups)
        minimal = copy.deepcopy(report)
        del minimal["repetitions"]
        with self.assertRaisesRegex(ValueError, "PRODUCER_REPETITION_SUMMARY_UNAVAILABLE"):
            bridge.validate_producer_report(minimal, expected_members, expected_groups)


if __name__ == "__main__":
    unittest.main()
