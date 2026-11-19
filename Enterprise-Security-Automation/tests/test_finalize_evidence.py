import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "security"))
from finalize_evidence import finalize, record
from evidence_import import REQUIRED, OPTIONAL, MANIFEST


class FinalizeEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in REQUIRED:
            (self.root / name).write_text("{}")
        self.original = {"schema_version":1, "files":{n:record(self.root/n) for n in REQUIRED}}
        (self.root / MANIFEST).write_text(json.dumps(self.original))

    def test_success_preserves_original_records(self):
        (self.root / OPTIONAL).write_text('{"status":"REVIEW REQUIRED"}')
        result = finalize(self.root, "success")
        self.assertEqual(result["files"][OPTIONAL], record(self.root / OPTIONAL))
        self.assertEqual({n:result["files"][n] for n in REQUIRED}, self.original["files"])

    def test_skipped(self):
        self.assertEqual(finalize(self.root,"skipped")["assessment_outcome"],"skipped")

    def test_missing_expected_and_failed(self):
        for outcome in ("success", "failure", "cancelled"):
            with self.assertRaises(ValueError):
                finalize(self.root,outcome)
        self.assertEqual(json.loads((self.root/MANIFEST).read_text()),self.original)

    def test_unexpected_assessment(self):
        (self.root/OPTIONAL).write_text("{}")
        with self.assertRaises(ValueError):
            finalize(self.root,"skipped")

    def test_existing_evidence_tamper(self):
        (self.root/"semgrep.json").write_text("{} ")
        with self.assertRaises(ValueError):
            finalize(self.root,"skipped")
