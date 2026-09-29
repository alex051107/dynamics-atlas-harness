"""Arm S: stuck-point prompt, workflow attached to checkpoints, two-stage finish, per-experiment chi2 (arm S only)."""
import asyncio
import json
import os
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import mcp.types as types

from dynamics_atlas_harness.nmr_agent import exchange as ex
from dynamics_atlas_harness.nmr_agent import mcp_server
from dynamics_atlas_harness.nmr_agent.agent import Agent, RunConfig
from dynamics_atlas_harness.nmr_agent.prompts import BASE, METHOD_NOTES, WORKFLOW, WORKFLOW_ENV, system_prompt

WF_TEXT = "WORKFLOW-BODY-QQQ"


def make_ws(root: Path) -> Path:
    ws = root / "ws"
    ws.mkdir()
    (ws / "TASK.md").write_text("Neutral test task")
    return ws


def fake_fit(per_kind=True, chi2=120.0):
    return ex.FitResult({"kex": 500.0, "pb": 0.05, "dwN[A1]": 1.0}, {"kex": 10.0, "pb": 0.001}, chi2, 100, 4, ["A1"],
                        {"A1": {"chi2": chi2, "n": 100, "dwN": 1.0}}, [], {"success": True},
                        {"cpmg_n": {"chi2": 30.0, "n": 60}, "cest_n": {"chi2": 90.0, "n": 40}} if per_kind else {})


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.ws = make_ws(self.root)
        self.wf = self.root / "wf.md"
        self.wf.write_text(WF_TEXT)
        p = patch.dict(os.environ, {WORKFLOW_ENV: str(self.wf)})
        p.start()
        self.addCleanup(p.stop)
        self.addCleanup(self.tmp.cleanup)
        self.agents = []

    def agent(self, arm, run="run"):
        a = Agent(self.ws, self.root / run, RunConfig(arm=arm))
        self.agents.append(a)
        self.addCleanup(lambda: (a.log.close(), a.calls.close()))
        return a


class SystemPrompt(Base):
    def test_s_prompt_has_stuckpoint_steps_only(self):
        sp = system_prompt("S")
        self.assertTrue(sp.startswith(BASE))
        self.assertIn("Working through an analysis stuck point", sp)
        self.assertIn("5. Before stating conclusions", sp)
        self.assertNotIn("Next step", sp)                   # answer-format paragraph removed
        self.assertNotIn(WORKFLOW_ENV, sp)
        self.assertNotIn(WF_TEXT, sp)
        self.assertNotIn(WORKFLOW.strip()[:40], sp)
        self.assertNotIn(METHOD_NOTES.strip()[:40], sp)
        self.assertEqual(system_prompt("A"), BASE)

    def test_s_requires_workflow_file(self):
        with patch.dict(os.environ, {WORKFLOW_ENV: "/nonexistent/x.md"}):
            with self.assertRaises(FileNotFoundError):
                Agent(self.ws, self.root / "r2", RunConfig(arm="S"))


class Checkpoint(Base):
    def test_workflow_full_once_then_reminder_and_persists_across_restart(self):
        a = self.agent("S")
        self.assertIn("reflect", {s["function"]["name"] for s in a.specs})
        first = a.checkpoint_suffix("the fit raised flags: x")
        self.assertIn(WF_TEXT, first)
        self.assertIn("REFLECTION CHECKPOINT (the fit raised flags: x). Your next call must be reflect.", first)
        second = a.checkpoint_suffix("4 analyses since the last reflection")
        self.assertNotIn(WF_TEXT, second)
        self.assertIn("attached in full at the first checkpoint", second)
        b = self.agent("S")      # tool-server restart in the same run directory
        self.assertNotIn(WF_TEXT, b.checkpoint_suffix("tool error"))

    def test_s_triggers_like_c_and_c_gets_no_workflow(self):
        s, c = self.agent("S", "rs"), self.agent("C", "rc")
        for ag in (s, c):
            self.assertEqual(ag._checkpoint_reason("fit_exchange", {"flags": ["reduced chi2 3 > 2"]}, False),
                             "the fit raised flags: reduced chi2 3 > 2")
            self.assertEqual(ag._checkpoint_reason("python", {}, True), "the tool returned an error")
            ag.analysis_since_reflect = 4
            self.assertIn("4 analyses", ag._checkpoint_reason("show_profile", {}, False))
            self.assertIsNone(ag._checkpoint_reason("inventory", {}, False))
        self.assertNotIn(WF_TEXT, c.checkpoint_suffix("r"))
        self.assertEqual(c.checkpoint_suffix("r"), "\n\nREFLECTION CHECKPOINT (r). Your next call must be reflect.")
        for arm in ("A", "W"):
            self.assertIsNone(self.agent(arm, "r" + arm)._checkpoint_reason("fit_exchange", {"flags": ["x"]}, False))


class FinishGate(Base):
    def prime(self, a):
        a.tools.fits["F001"] = {"fit_id": "F001", "flags": ["kex at bound (2)"]}
        a.tools.fits["F002"] = {"fit_id": "F002", "flags": []}
        a.state.reflections += [
            {"decision": "keep_plan", "discrepancy": "residue 5 misfit", "next_action": "go on", "turn": 3},
            {"decision": "keep_plan", "discrepancy": "None.", "next_action": "go on", "turn": 4},
            {"decision": "revise_plan", "discrepancy": "big", "next_action": "x", "turn": 5}]

    def test_first_finish_returns_checklist_second_is_accepted(self):
        a = self.agent("S")
        self.prime(a)
        args = {"report": "R", "atlas_entries": []}
        with patch("dynamics_atlas_harness.nmr_agent.atlas_candidate.validate", return_value=[]):
            r1, e1 = a._execute("finish", args)
            self.assertFalse(e1)
            self.assertIsNone(a.final_report)
            self.assertEqual([x["fit_id"] for x in r1["fits_with_flags"]], ["F001"])
            self.assertEqual(r1["fits_with_flags"][0]["flags"], ["kex at bound (2)"])
            self.assertEqual([x["reflection_no"] for x in r1["kept_plan_despite_discrepancy"]], [1])
            self.assertIn("call finish again", r1["finish_check"])
            r2, e2 = a._execute("finish", args)
            self.assertFalse(e2)
            self.assertEqual(a.final_report, "R")
            self.assertTrue(a._finish_gate_file.exists())

    def test_gate_survives_restart_and_other_arms_finish_directly(self):
        a = self.agent("S")
        with patch("dynamics_atlas_harness.nmr_agent.atlas_candidate.validate", return_value=[]):
            a._execute("finish", {"report": "R", "atlas_entries": []})
            b = self.agent("S")
            b._execute("finish", {"report": "R", "atlas_entries": []})
            self.assertEqual(b.final_report, "R")
            for arm in ("A", "C", "W"):
                x = self.agent(arm, "r" + arm)
                self.prime(x)
                x._execute("finish", {"report": "R", "atlas_entries": []})
                self.assertEqual(x.final_report, "R", arm)

    def test_mcp_server_first_finish_is_not_closed(self):
        server = mcp_server.build(self.ws, self.root / "mcp", "S", (), 6000, 70)

        def call(name, arguments):
            req = types.CallToolRequest(method="tools/call", params=types.CallToolRequestParams(name=name, arguments=arguments))
            res = asyncio.run(server.request_handlers[types.CallToolRequest](req))
            return res.root.content[0].text

        with patch("dynamics_atlas_harness.nmr_agent.atlas_candidate.validate", return_value=[]):
            t1 = call("finish", {"report": "R", "atlas_entries": []})
            self.assertIn("FINISH CHECK", t1)
            self.assertNotIn("Report recorded", t1)
            self.assertFalse((self.root / "mcp" / "REPORT.md").exists())
            t2 = call("finish", {"report": "R", "atlas_entries": []})
            self.assertIn("Report recorded", t2)
            self.assertEqual((self.root / "mcp" / "REPORT.md").read_text(), "R")


class PerExperimentChi2(Base):
    def run_fit(self, arm, with_kind=True):
        a = self.agent(arm, "run" + arm)
        with patch.object(a.tools, "_v", return_value={"cs_n": {}, "r1": {}}), \
             patch.object(a.tools, "_exps", return_value=[SimpleNamespace(name="e1"), SimpleNamespace(name="e2")]), \
             patch.object(ex, "fit_two_state", return_value=fake_fit(with_kind)):
            return a.tools.fit_exchange("WT", ["A1"])

    def test_only_arm_s_reports_by_experiment_type(self):
        out = self.run_fit("S")
        by = out["chi2_by_experiment_type"]
        self.assertEqual(set(by), {"cpmg_n", "cest_n"})
        self.assertEqual(by["cest_n"]["chi2"], 90.0)
        self.assertEqual(by["cest_n"]["n_data"], 40)
        # dof share = (100-4)/100; 90 / (40*0.96)
        self.assertAlmostEqual(by["cest_n"]["reduced_chi2_prorata_dof"], 90 / 38.4, places=3)
        self.assertNotIn("chi2_by_experiment_type", self.run_fit("S", with_kind=False))   # single kind: nothing to split

    def test_arms_a_c_w_output_is_unchanged(self):
        base_keys = {"fit_id", "variant", "model", "mode", "groups", "experiments", "global", "global_err", "chi2", "n_data",
                     "n_params", "reduced_chi2", "aic", "bic", "per_residue", "worst_residues_chi2_per_point", "flags",
                     "notes", "optimization", "seconds", "sign_note"}     # key set of fit_exchange at commit 22b49a0
        for arm in ("A", "C", "W"):
            with_kind = self.run_fit(arm, True)
            without = self.run_fit(arm, False)
            self.assertEqual(set(with_kind), base_keys, arm)
            for d in (with_kind, without):
                d.pop("seconds"), d.pop("fit_id")
            self.assertEqual(json.dumps(with_kind, sort_keys=True), json.dumps(without, sort_keys=True), arm)


if __name__ == "__main__":
    unittest.main()
