import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from dynamics_atlas_harness import paper_blind_exposed_v1
from dynamics_atlas_harness.paper_blind_exposed_v1 import (
    PaperBlindPublicPacketError,
    build_agent_visible_packet,
    load_public_packet,
    validate_agent_proposal,
    verify_declared_asset_hashes,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
PUBLIC_ROOT = REPO_ROOT / "evidence" / "paper_blind_exposed_v1" / "public"
HSP90_PACKET = PUBLIC_ROOT / "hsp90_public_packet_v1.json"
ADK_PACKET = PUBLIC_ROOT / "adk_public_packet_v1.json"
HSP90_ASSET_IDS = [
    "HSP90_CA46_CA60_DISTANCE_40X1021",
    "HSP90_TRAJECTORY_IDS",
]
ADK_ASSET_IDS = ["ADK_1AKE_CHAIN_A_CA", "ADK_4AKE_CHAIN_A_CA"]


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class PaperBlindExposedV1Tests(unittest.TestCase):
    def test_public_packets_verify_declared_asset_identity_without_parsing_payloads(self):
        for packet_path, expected_asset_ids in (
            (HSP90_PACKET, HSP90_ASSET_IDS),
            (ADK_PACKET, ADK_ASSET_IDS),
        ):
            with self.subTest(packet=packet_path.name):
                packet = load_public_packet(packet_path)
                verification = verify_declared_asset_hashes(packet_path)
                self.assertEqual(
                    [asset["asset_id"] for asset in packet["data_assets"]],
                    expected_asset_ids,
                )
                self.assertEqual(verification["verified_asset_ids"], expected_asset_ids)
                self.assertEqual(
                    verification["verification_scope"],
                    "IDENTITY_AND_PUBLIC_PACKET_BOUNDARY_ONLY",
                )
                self.assertNotIn("development_obligation_id", json.dumps(packet))
                self.assertNotIn("rule_instance_id", json.dumps(packet))
                self.assertNotIn("allowed_capability_ids", json.dumps(packet))

    def test_visible_agent_packet_omits_platform_authority_and_hidden_reference(self):
        visible = build_agent_visible_packet(HSP90_PACKET)
        self.assertEqual(
            set(visible),
            {
                "schema_version",
                "packet_id",
                "case_id",
                "research_question",
                "source_materials",
                "data_assets",
                "agent_proposal_schema",
            },
        )
        self.assertNotIn("platform_authority_envelope", visible)
        self.assertNotIn("hidden_reference_boundary", visible)
        self.assertNotIn("claim_boundary", visible)
        self.assertEqual(
            visible["agent_proposal_schema"]["allowed_output_fields"],
            ["case_id", "proposed_source_ids", "unknowns", "rationale"],
        )

    def test_hidden_reference_and_expected_route_fields_are_rejected(self):
        packet = _load(HSP90_PACKET)
        packet["paper_reported_conclusion"] = "leak"
        with tempfile.TemporaryDirectory() as tmp:
            path = PUBLIC_ROOT / f"temporary_{Path(tmp).name}.json"
            try:
                path.write_text(json.dumps(packet), encoding="utf-8")
                with self.assertRaisesRegex(PaperBlindPublicPacketError, "FORBIDDEN_FIELD"):
                    load_public_packet(path)
            finally:
                path.unlink(missing_ok=True)

    def test_agent_proposal_is_profile_only_and_cannot_select_capabilities(self):
        proposal = {
            "case_id": "HSP90_NTD_EXPOSED_PAPER_BLIND_V1",
            "proposed_source_ids": [
                "HSP90_NMR_METHODS_RESULTS",
                "HSP90_MD_DISTANCE_TRACE",
            ],
            "unknowns": ["NMR-to-MD condition compatibility is not supplied."],
            "rationale": "The public material identifies source facts and unresolved links.",
        }
        admitted = validate_agent_proposal(HSP90_PACKET, proposal)
        self.assertEqual(admitted["proposal_status"], "ADMISSIBLE_NONAUTHORITATIVE")
        self.assertEqual(set(admitted), {"schema_version", "proposal_status", "proposal"})
        proposal["candidate_capability_ids"] = ["SAMPLING_DIAGNOSTICS_V1"]
        with self.assertRaisesRegex(PaperBlindPublicPacketError, "FORBIDDEN_FIELD"):
            validate_agent_proposal(HSP90_PACKET, proposal)

    def test_hash_mismatch_fails_before_any_numeric_or_execution_path(self):
        manifest = _load(paper_blind_exposed_v1.FROZEN_INPUT_MANIFEST_PATH)
        manifest["assets"]["HSP90_TRAJECTORY_IDS"]["sha256"] = "0" * 64
        with tempfile.TemporaryDirectory() as tmp:
            temporary_manifest = Path(tmp) / "manifest.json"
            temporary_manifest.write_text(json.dumps(manifest), encoding="utf-8")
            with patch.object(
                paper_blind_exposed_v1,
                "FROZEN_INPUT_MANIFEST_PATH",
                temporary_manifest,
            ):
                with self.assertRaisesRegex(
                    PaperBlindPublicPacketError, "FROZEN_INPUT_HASH_MISMATCH"
                ):
                    verify_declared_asset_hashes(HSP90_PACKET)


if __name__ == "__main__":
    unittest.main()
