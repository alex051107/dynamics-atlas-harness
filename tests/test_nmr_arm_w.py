import hashlib
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from dynamics_atlas_harness.nmr_agent.prompts import (BASE, WORKFLOW_ENV, system_prompt,
                                                      workflow_file_info)


class ArmW(unittest.TestCase):
    def test_arm_w_appends_workflow_file_and_records_hash(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "note.md"
            f.write_text("NOTE-BODY-XYZ")
            with patch.dict(os.environ, {WORKFLOW_ENV: str(f)}):
                sp = system_prompt("W")
                info = workflow_file_info()
            self.assertTrue(sp.startswith(BASE))
            self.assertIn("Below is a working note distilled from how experienced protein-dynamics NMR scientists", sp)
            self.assertTrue(sp.endswith("NOTE-BODY-XYZ"))
            self.assertEqual(info["workflow_sha256"], hashlib.sha256(b"NOTE-BODY-XYZ").hexdigest())
            self.assertEqual(system_prompt("A"), BASE)

    def test_arm_w_fails_without_file(self):
        env = {k: v for k, v in os.environ.items() if k != WORKFLOW_ENV}
        with patch.dict(os.environ, env, clear=True):
            with self.assertRaises(FileNotFoundError):
                system_prompt("W")
        with patch.dict(os.environ, {WORKFLOW_ENV: "/nonexistent/x.md"}):
            with self.assertRaises(FileNotFoundError):
                system_prompt("W")


if __name__ == "__main__":
    unittest.main()
