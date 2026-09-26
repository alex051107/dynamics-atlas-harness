"""NMR tool boundary, provenance and persistence regression checks."""
from pathlib import Path
import json
import tempfile
import unittest
from unittest.mock import patch

from dynamics_atlas_harness.nmr_agent import references, exchange
from dynamics_atlas_harness.nmr_agent.agent import Agent, RunConfig
from dynamics_atlas_harness.nmr_agent.tools import ToolBox
from dynamics_atlas_harness.nmr_agent.atlas_candidate import REQUIRED_TEXT


class CandidateRepairs(unittest.TestCase):
    def test_concurrent_region_interface_keeps_paired_masks(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            (root/"analysis_input.json").write_text(json.dumps({"ground_ppm":{"A1":0,"A2":0,"A3":0},"dw_ppm":{"A1":1,"A2":2,"A3":3}}))
            (root/"references.json").write_text(json.dumps({"references":[
                {"id":"r1","shifts":{"N":{"A1":1,"A2":2,"A3":3}}},
                {"id":"r2","shifts":{"N":{"A1":1,"A2":2}}}]}))
            box=ToolBox(root,root)
            out=box.compare_references(["r1","r2"],regions={"region_a":["A1","A2","A3"]})
            self.assertEqual(out["regions"]["region_a"]["common_residues"],["A1","A2"])
            self.assertEqual(out["pooled"]["common_residues"],["A1","A2"])
            with self.assertRaises(ValueError):box.compare_references(["r1"])

    def test_restart_preserves_fit_identifiers_and_results(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d); (root/"fits").mkdir(); (root/"py").mkdir()
            payload = {"fit_id":"F012", "variant":"WT", "per_residue":{"A1":{"dwN":1.}}}
            (root/"fits/F012.json").write_text(json.dumps(payload))
            (root/"py/P013.py").write_text("print('completed earlier')")
            box = ToolBox(root, root)
            self.assertEqual(box.fits["F012"], payload)
            self.assertEqual(box._new_id("F"), "F014")
            self.assertEqual(json.loads((root/"fits/F012.json").read_text()), payload)

    def test_reference_paths_and_symlinks(self):
        with tempfile.TemporaryDirectory() as d:
            base = Path(d); ws = base / "ws"; ref = ws / "WT/references"; ref.mkdir(parents=True)
            payload = {"shifts": {"A1N": 120.}, "description": "canary"}
            outside = base / "outside.json"; outside.write_text(json.dumps(payload))
            (ref / "legitimate.json").write_text(json.dumps(payload))
            self.assertEqual(references.get_workspace_reference(ws,"WT","legitimate"), payload)
            for variant, name in (("WT", str(outside.with_suffix(""))), ("../", "outside"), ("WT", "../../../outside")):
                with self.assertRaises((PermissionError, ValueError)):
                    references.get_workspace_reference(ws, variant, name)
            (ref / "link.json").symlink_to(outside)
            with self.assertRaises(PermissionError): references.get_workspace_reference(ws, "WT", "link")

    def test_blocked_accessions_are_canonical_and_pdb_paths_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            box = ToolBox(Path(d), Path(d), blocked_bmrb_ids=("52021",))
            with patch("urllib.request.urlopen", side_effect=AssertionError("must not reach network")):
                for entry in ("52021", "052021", " 52021 ", "52021?format=json", "52021/anything"):
                    with self.assertRaises((PermissionError, ValueError)): box.bmrb_entry(entry)
                with self.assertRaises(ValueError): references.pdb_ligand_distances("../../outside",None)

    def test_group_membership_is_a_partition(self):
        for groups in ({"g1":["A1"],"g2":["A1","A2"]}, {"g1":["A1"]}, {"g1":["A1","A2"],"g2":[]}):
            with self.assertRaisesRegex(ValueError, "groups"):
                exchange.fit_two_state([], ["A1","A2"], groups=groups)

    @unittest.skipUnless((Path.home()/"nmr_agent_work/kras_ws_v3/WT/experiments.json").exists(), "optional archived real-data fixture unavailable")
    def test_skipped_profiles_are_not_negative_evidence(self):
        with tempfile.TemporaryDirectory() as d:
            box = ToolBox(Path.home()/"nmr_agent_work/kras_ws_v3", Path(d))
            data = box.screen_dispersion("WT_GDP", "cest_15N_850MHz")
            self.assertEqual(data["n_profiles"], 10)
            self.assertEqual(data["n"], 8)
            self.assertEqual({row["res"] for row in data["skipped"]}, {"Y32", "Y64"})
            self.assertIn("not p-values or counts of conformational states", data["note"])

    @unittest.skipUnless((Path.home()/"nmr_agent_work/kras_ws_v3/WT/experiments.json").exists(), "optional archived real-data fixture unavailable")
    def test_fit_exposes_convergence_and_rejects_unsupported_options(self):
        with tempfile.TemporaryDirectory() as d:
            box = ToolBox(Path.home()/"nmr_agent_work/kras_ws_v3", Path(d))
            names = [e for e in box._v("WT")["experiments"] if "cpmg_15N" in e]
            self.assertTrue(names)
            f = box.fit_exchange("WT", ["D38","I36"], names, dw_init={"D38":3.,"I36":2.})
            for key in ("success","status","nfev","optimality","parameters_at_bounds"):
                self.assertIn(key, f["optimization"])
            with self.assertRaises(ValueError):
                box.fit_exchange("WT", ["D38"], names, model="three_state_star", fix={"pb":.1})

    def test_trimmed_observation_remains_retrievable_and_finish_checks_links(self):
        with tempfile.TemporaryDirectory() as d:
            ws = Path(d)/"ws"; ws.mkdir(); (ws/"TASK.md").write_text("neutral test")
            a = Agent(ws, Path(d)/"run", RunConfig(arm="C", trim_threshold_chars=1, keep_recent_tool_results=1))
            try:
                observed, err = a._execute("read_text", {"path":"TASK.md"})
                self.assertFalse(err)
                oid = observed["observation_id"]
                a.messages += [{"role":"tool","content":json.dumps(observed)}, {"role":"tool","content":"recent"}]
                a._trim()
                self.assertTrue(any(oid in m["content"] and "read_result" in m["content"] for m in a.messages))
                page, err = a._execute("read_result", {"observation_id":oid})
                self.assertFalse(err); self.assertIn("neutral test", page["text"])
                _, err = a._execute("finish", {"report":"report", "atlas_entries":[{}]})
                self.assertTrue(err); self.assertIsNone(a.final_report)
                entry = {key:"explicitly unknown in this fixture" for key in REQUIRED_TEXT}
                entry.update(proposed_tier="candidate", source_observations=["O999999"])
                _, err = a._execute("finish", {"report":"report", "atlas_entries":[entry]})
                self.assertTrue(err)
                entry["source_observations"]=[oid]
                _, err = a._execute("finish", {"report":"report", "atlas_entries":[entry]})
                self.assertFalse(err)
                status=json.loads((a.run_dir/"ATLAS_VALIDATION.json").read_text())
                self.assertEqual(status["domain_review"],"pending")
                self.assertFalse(status["database_import_performed"])
            finally: a.log.close(); a.calls.close()


if __name__ == "__main__": unittest.main(verbosity=2)
