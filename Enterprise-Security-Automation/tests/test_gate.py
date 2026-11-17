import sys
import unittest
import json
from copy import deepcopy
from datetime import date
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "security"))
from gate import evaluate, EXIT_CODES

class GateTests(unittest.TestCase):
    def setUp(self):
        self.policy = json.loads((ROOT / "governance/requirements.example.json").read_text())
        self.today = date(2026, 11, 17)
        self.item = {"ID": "AWS-0132", "Severity": "HIGH", "CauseMetadata": {"Resource": "aws_s3_bucket_server_side_encryption_configuration.access_logs"}}
    def run_gate(self, items, target="main.tf"):
        return evaluate({"Results": [{"Target": target, "Misconfigurations": items}]}, self.policy, self.today)
    def approve(self):
        self.policy["exceptions"][0].update(status="approved", approved_by="synthetic-test-reviewer", approved_on="2026-11-17", expires_on="2027-02-15")
    def test_pass(self):
        self.assertEqual(self.run_gate([])["decision"], "PASS")
    def test_pending(self):
        result = self.run_gate([self.item])
        self.assertEqual(result["decision"], "EXCEPTION PENDING")
        self.assertEqual(EXIT_CODES[result["decision"]], 2)
        self.assertFalse(result["deployment_authorized"])
    def test_approved_synthetic(self):
        self.approve()
        result = self.run_gate([self.item])
        self.assertEqual(result["decision"], "EXCEPTION APPROVED")
        self.assertEqual(len(result["findings"]), 1)
        self.assertTrue(result["human_approval_required"])
        self.assertFalse(result["deployment_authorized"])
    def test_wrong_resource(self):
        self.approve()
        item = deepcopy(self.item)
        item["CauseMetadata"]["Resource"] = "aws_s3_bucket_server_side_encryption_configuration.evidence"
        self.assertEqual(self.run_gate([item])["decision"], "BLOCK")
    def test_wrong_target(self):
        self.approve()
        self.assertEqual(self.run_gate([self.item], "other.tf")["decision"], "BLOCK")
    def test_wrong_severity(self):
        self.approve()
        item = deepcopy(self.item)
        item["Severity"] = "CRITICAL"
        self.assertEqual(self.run_gate([item])["decision"], "BLOCK")
    def test_expired(self):
        self.approve()
        self.policy["exceptions"][0].update(approved_on="2026-08-01", expires_on="2026-10-30")
        self.assertEqual(self.run_gate([self.item])["decision"], "BLOCK")
    def test_missing_reviewer(self):
        self.approve()
        self.policy["exceptions"][0]["approved_by"] = None
        self.assertEqual(self.run_gate([self.item])["decision"], "BLOCK")
    def test_unrelated_high(self):
        self.approve()
        self.assertEqual(self.run_gate([self.item, {"ID":"OTHER", "Severity":"HIGH"}])["decision"], "BLOCK")
    def test_duplicate_scope(self):
        self.approve()
        self.policy["exceptions"].append(deepcopy(self.policy["exceptions"][0]))
        self.assertEqual(self.run_gate([self.item])["decision"], "BLOCK")
    def test_missing(self):
        with self.assertRaises(ValueError):
            evaluate({}, self.policy)
    def test_advisory_visible(self):
        result = self.run_gate([{"ID":"OTHER", "Severity":"LOW"}])
        self.assertEqual(result["decision"], "PASS")
        self.assertEqual(result["findings"][0]["disposition"], "advisory")
