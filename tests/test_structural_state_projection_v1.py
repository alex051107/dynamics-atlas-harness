import tempfile
import unittest
from pathlib import Path

import numpy as np

from dynamics_atlas_harness.structural_state_projection_v1 import (
    StructuralStateProjectionError,
    run_reference_relative_structural_projection,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
ADK_ROOT = REPO_ROOT / "evidence" / "paper_blind_exposed_v1" / "frozen_inputs" / "adk"


class StructuralStateProjectionV1Tests(unittest.TestCase):
    def test_known_rigid_transform_has_zero_aligned_rmsd(self):
        reference = np.array(
            [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            dtype=float,
        )
        rotation = np.array([[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]])
        sample = reference @ rotation.T + np.array([3.0, -2.0, 5.0])
        with tempfile.TemporaryDirectory() as tmp:
            tmp_root = Path(tmp)
            sample_path = tmp_root / "sample.npy"
            reference_path = tmp_root / "reference.npy"
            second_path = tmp_root / "second.npy"
            np.save(sample_path, sample)
            np.save(reference_path, reference)
            np.save(second_path, reference + np.array([4.0, 0.0, 0.0]))
            result = run_reference_relative_structural_projection(
                sample_id="RIGID_TRANSFORM_SAMPLE",
                sample_coordinate_path=sample_path,
                reference_coordinate_paths={"REFERENCE": reference_path, "SECOND": second_path},
                residue_positions=[1, 2, 3, 4],
                alignment_positions=[0, 1, 2, 3],
                classification_positions=[0, 1, 2, 3],
            )
        reference_distance = next(
            item["aligned_rmsd_angstrom"]
            for item in result["reference_distances"]
            if item["reference_id"] == "REFERENCE"
        )
        self.assertLess(reference_distance, 1e-10)

    def test_nonreference_adk_sample_is_projected_without_rule_result(self):
        result = run_reference_relative_structural_projection(
            sample_id="ADK_1E4V_G10V_CHAIN_A_NONREFERENCE",
            sample_coordinate_path=ADK_ROOT / "1E4V_G10V_chain_A_ca.npy",
            reference_coordinate_paths={
                "ADK_1AKE_CLOSED_REFERENCE": ADK_ROOT / "1AKE_chain_A_ca.npy",
                "ADK_4AKE_OPEN_REFERENCE": ADK_ROOT / "4AKE_chain_A_ca.npy",
            },
            residue_positions=list(range(1, 215)),
            alignment_positions=list(range(214)),
            classification_positions=list(range(214)),
        )
        self.assertEqual(result["sample_kind"], "NONREFERENCE_STATIC_COORDINATE_SAMPLE")
        self.assertEqual(result["rule_effect"], "NO_RULE_RESULT_EMITTED")
        self.assertEqual(result["nearest_reference_geometry"]["reference_id"], "ADK_1AKE_CLOSED_REFERENCE")
        self.assertIn("wild-type equivalence", result["forbidden_claims"])

    def test_reference_self_projection_is_rejected(self):
        reference_path = ADK_ROOT / "1AKE_chain_A_ca.npy"
        with self.assertRaisesRegex(StructuralStateProjectionError, "SAMPLE_MUST_NOT_BE_REFERENCE_ASSET"):
            run_reference_relative_structural_projection(
                sample_id="INVALID_REFERENCE_AS_SAMPLE",
                sample_coordinate_path=reference_path,
                reference_coordinate_paths={
                    "ADK_1AKE_CLOSED_REFERENCE": reference_path,
                    "ADK_4AKE_OPEN_REFERENCE": ADK_ROOT / "4AKE_chain_A_ca.npy",
                },
                residue_positions=list(range(1, 215)),
                alignment_positions=list(range(214)),
                classification_positions=list(range(214)),
            )

    def test_coordinate_equivalent_copy_of_reference_is_rejected(self):
        reference_path = ADK_ROOT / "1AKE_chain_A_ca.npy"
        with tempfile.TemporaryDirectory() as tmp:
            copied_reference_path = Path(tmp) / "copied_reference.npy"
            np.save(copied_reference_path, np.load(reference_path, allow_pickle=False))
            with self.assertRaisesRegex(
                StructuralStateProjectionError,
                "SAMPLE_MUST_NOT_MATCH_REFERENCE_COORDINATES",
            ):
                run_reference_relative_structural_projection(
                    sample_id="INVALID_COPIED_REFERENCE_AS_SAMPLE",
                    sample_coordinate_path=copied_reference_path,
                    reference_coordinate_paths={
                        "ADK_1AKE_CLOSED_REFERENCE": reference_path,
                        "ADK_4AKE_OPEN_REFERENCE": ADK_ROOT / "4AKE_chain_A_ca.npy",
                    },
                    residue_positions=list(range(1, 215)),
                    alignment_positions=list(range(214)),
                    classification_positions=list(range(214)),
                )


if __name__ == "__main__":
    unittest.main()
