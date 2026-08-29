import json
import tempfile
import unittest
from pathlib import Path

from dynamics_atlas_harness.sampling_diagnostics_v1 import (
    SamplingDiagnosticsError,
    run_grouped_observable_sampling_diagnostics,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
FROZEN_ROOT = REPO_ROOT / "evidence" / "paper_blind_exposed_v1" / "frozen_inputs" / "hsp90"


class SamplingDiagnosticsV1Tests(unittest.TestCase):
    def test_frozen_hsp90_rows_preserve_trajectory_and_construct_group_identity(self):
        result = run_grouped_observable_sampling_diagnostics(
            observable_path=FROZEN_ROOT / "ca46_ca60_distance_40x1021.npy",
            trajectory_group_manifest_path=FROZEN_ROOT / "trajectory_group_manifest_v1.json",
            observable_id="HSP90_CA46_CA60_DISTANCE",
            analysis_window_label="FROZEN_1021_FRAME_OBSERVED_WINDOW",
        )
        self.assertEqual(result["row_count"], 40)
        self.assertEqual(result["frames_per_trajectory"], 1021)
        self.assertEqual(len(result["per_trajectory"]), 40)
        self.assertEqual(len({item["trajectory_id"] for item in result["per_trajectory"]}), 40)
        self.assertEqual(
            {item["group_id"]: item["trajectory_count"] for item in result["within_group_summaries"]},
            {"R46A_ES": 20, "R60A_GS": 20},
        )
        self.assertEqual(result["rule_effect"], "NO_RULE_RESULT_EMITTED")
        self.assertIn("simulation globally equilibrated", result["forbidden_claims"])

    def test_group_manifest_row_count_mismatch_fails_closed(self):
        manifest_path = FROZEN_ROOT / "trajectory_group_manifest_v1.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["rows"] = manifest["rows"][:-1]
        with tempfile.TemporaryDirectory() as tmp:
            broken_manifest = Path(tmp) / "manifest.json"
            broken_manifest.write_text(json.dumps(manifest), encoding="utf-8")
            with self.assertRaisesRegex(
                SamplingDiagnosticsError,
                "TRAJECTORY_ID_COUNT_DOES_NOT_MATCH_OBSERVABLE_ROWS",
            ):
                run_grouped_observable_sampling_diagnostics(
                    observable_path=FROZEN_ROOT / "ca46_ca60_distance_40x1021.npy",
                    trajectory_group_manifest_path=broken_manifest,
                    observable_id="HSP90_CA46_CA60_DISTANCE",
                    analysis_window_label="FROZEN_1021_FRAME_OBSERVED_WINDOW",
                )


if __name__ == "__main__":
    unittest.main()
