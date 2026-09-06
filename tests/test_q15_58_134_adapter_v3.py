"""Regression checks for the reader-time 58/134 producer binding."""

import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

from dynamics_atlas_harness import q15_apbs_comparison_v1 as q15


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"


def load_script(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


reader = load_script("run_q15_58_134_frozen_reuse_v3")
bridge = load_script("run_q15_58_134_forward_bridge_v3")


class AdapterV3Test(unittest.TestCase):
    def make_bound_report(self, root: Path):
        task = root / "task"
        source_root = task / "outputs" / reader.INTAKE
        source_root.mkdir(parents=True)
        (source_root / "selected_members.json").write_text("[]\n")
        (source_root / "retry1_receipt.json").write_text("{}\n")
        quality = {"source_admission": "COMPLETE", "apbs": {"matches_frozen_export_policy": True}, "frozen_policy": q15.POLICY}
        (source_root / "input_quality_report.json").write_text(json.dumps(quality, sort_keys=True) + "\n")
        report_dir = task / "outputs" / bridge.READER_DIR
        report_dir.mkdir()
        report = {"version": reader.REPORT_VERSION, "frozen_policy": q15.POLICY, "repetitions": [{"pair": "58_134", "condition": "apo", "repetition": "repetion_1", "E": {"mean": 0.2}}]}
        report_path = report_dir / "report.json"
        report_path.write_text(json.dumps(report, sort_keys=True) + "\n")
        reader.write_producer_admission(task, report_path, report)
        return task, report_path, report

    def test_producer_record_rejects_coherent_report_rewrite_and_quality_snapshot_change(self):
        with tempfile.TemporaryDirectory() as temp:
            task, report_path, report = self.make_bound_report(Path(temp))
            self.assertEqual(bridge.validate_producer_binding(task, report_path, report)["version"], reader.PRODUCER_RECORD_VERSION)
            rewritten = copy.deepcopy(report)
            rewritten["repetitions"][0]["condition"] = "holo"
            report_path.write_text(json.dumps(rewritten, sort_keys=True) + "\n")
            with self.assertRaisesRegex(ValueError, "PRODUCER_REPORT_BYTES_MISMATCH"):
                bridge.validate_producer_binding(task, report_path, rewritten)
            report_path.write_text(json.dumps(report, sort_keys=True) + "\n")
            quality_path = task / "outputs" / reader.INTAKE / "input_quality_report.json"
            quality_path.write_text(json.dumps({"source_admission": "REJECTED"}) + "\n")
            with self.assertRaisesRegex(ValueError, "SOURCE_SNAPSHOT_BYTES_MISMATCH:input_quality_report"):
                bridge.validate_producer_binding(task, report_path, report)
            quality_path.unlink()
            with self.assertRaisesRegex(ValueError, "REQUIRED_SOURCE_SNAPSHOT_UNAVAILABLE:input_quality_report"):
                bridge.validate_producer_binding(task, report_path, report)


if __name__ == "__main__":
    unittest.main()
