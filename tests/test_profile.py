import json
import unittest
from pathlib import Path

from dynamics_atlas_harness.contracts import validate_case_profile


FIXTURES = Path(__file__).parent / "fixtures"


def load(name: str):
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


class ProfileAdmissionTests(unittest.TestCase):
    def test_valid_synthetic_profile_is_ready(self):
        result = validate_case_profile(load("case_profile_valid.json"), set())
        self.assertEqual(result.status, "PROFILE_READY")
        self.assertTrue(result.selector_access_allowed)

    def test_md_source_without_approved_profile_stops(self):
        result = validate_case_profile(load("case_profile_hsp90_md_missing.json"), set())
        self.assertEqual(result.status, "NEEDS_METHOD_PROFILE")
        self.assertFalse(result.selector_access_allowed)
        self.assertEqual(result.reason_codes, ("NEEDS_METHOD_PROFILE:hsp90-md-trajectory",))

    def test_answer_bearing_key_is_rejected_recursively(self):
        proposal = load("case_profile_valid.json")
        proposal["sources"][0]["reference_answer"] = "hidden"
        result = validate_case_profile(proposal, set())
        self.assertEqual(result.status, "INVALID_PROFILE")
        self.assertIn("ANSWER_BEARING_KEY:$.sources[0].reference_answer", result.reason_codes)

    def test_unregistered_source_type_is_rejected(self):
        proposal = load("case_profile_valid.json")
        proposal["sources"][0]["source_type"] = "md_trajectory"
        result = validate_case_profile(proposal, set())
        self.assertEqual(result.status, "INVALID_PROFILE")
        self.assertIn(
            "UNREGISTERED_SOURCE_TYPE:source-metadata-001:md_trajectory",
            result.reason_codes,
        )

    def test_unknowns_must_be_a_string_list(self):
        proposal = load("case_profile_valid.json")
        proposal["unknowns"] = "nothing"
        result = validate_case_profile(proposal, set())
        self.assertEqual(result.status, "INVALID_PROFILE")
        self.assertIn("INVALID_UNKNOWNS", result.reason_codes)


if __name__ == "__main__":
    unittest.main()
