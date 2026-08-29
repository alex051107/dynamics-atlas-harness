"""Focused fixture-only tests for the exposed proposal smoke segment."""

from __future__ import annotations

import copy
import unittest
from pathlib import Path

from dynamics_atlas_harness.exposed_proposal_smoke_v1 import (
    ExposedProposalSmokeError,
    load_exposed_planner_fixtures,
    materialize_exposed_planner_proposal,
)


EXPERIMENT_ROOT = Path(__file__).parents[1] / "agent_experiments" / "v1"


class ExposedProposalSmokeV1Tests(unittest.TestCase):
    def test_both_recorded_cases_materialize_without_transport(self) -> None:
        for case_key in ("xeisd", "hsp90"):
            receipt = materialize_exposed_planner_proposal(
                case_key, experiment_root=EXPERIMENT_ROOT
            )
            with self.subTest(case_key=case_key):
                self.assertEqual(receipt["status"], "PASS")
                self.assertEqual(receipt["model_transport_invocations"], 0)
                proposal = receipt["canonical_proposal"]
                self.assertFalse(proposal["execution_requested"])
                self.assertEqual(proposal["scientific_disposition"], "NOT_EVALUATED")
                self.assertEqual(
                    proposal["claim_ceiling_acknowledgement"],
                    "NO_SCIENTIFIC_DISPOSITION",
                )

    def test_fixture_loader_rejects_unknown_case(self) -> None:
        with self.assertRaises(ExposedProposalSmokeError):
            load_exposed_planner_fixtures("unknown", experiment_root=EXPERIMENT_ROOT)

    def test_materializer_rejects_disallowed_card_and_escalation_fields(self) -> None:
        packet, selection = load_exposed_planner_fixtures(
            "xeisd", experiment_root=EXPERIMENT_ROOT
        )
        disallowed = {
            "selected_card_ids": [a["card_id"] for a in selection["proposed_actions"]],
            "rationales": {
                a["card_id"]: a["rationale"] for a in selection["proposed_actions"]
            },
        }
        disallowed["selected_card_ids"] = ["unregistered-card"]
        from dynamics_atlas_harness.live_agent_exposed_v1 import (
            materialize_planner_card_selection,
        )

        disallowed["execute_now"] = True
        receipt = materialize_planner_card_selection(disallowed, packet)
        self.assertEqual(receipt["status"], "FAIL")
        self.assertIsNone(receipt["canonical_proposal"])
        self.assertTrue(
            any("FIELD_FORBIDDEN" in reason for reason in receipt["reason_codes"])
        )

    def test_materializer_rejects_scientific_or_execution_escalation(self) -> None:
        packet, selection = load_exposed_planner_fixtures(
            "xeisd", experiment_root=EXPERIMENT_ROOT
        )
        from dynamics_atlas_harness.live_agent_exposed_v1 import (
            materialize_planner_card_selection,
        )

        for field, value in (
            ("execution_requested", True),
            ("scientific_disposition", "SUPPORT"),
        ):
            escalated = copy.deepcopy(selection)
            escalated[field] = value
            receipt = materialize_planner_card_selection(escalated, packet)
            with self.subTest(field=field):
                self.assertEqual(receipt["status"], "FAIL")
                self.assertIsNone(receipt["canonical_proposal"])
                self.assertTrue(
                    any("FIELD_FORBIDDEN" in reason for reason in receipt["reason_codes"])
                )


if __name__ == "__main__":
    unittest.main()
