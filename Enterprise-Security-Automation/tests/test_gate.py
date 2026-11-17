import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "security"))
from gate import evaluate

class GateTests(unittest.TestCase):
    def setUp(self):
        self.policy = {"blocked_severities": ["HIGH", "CRITICAL"], "human_approval_required": True}
    def test_pass(self):
        self.assertEqual(evaluate({"Results": [{"Target": "demo"}]}, self.policy)["decision"], "PASS")
    def test_block(self):
        report = {"Results": [{"Target": "demo", "Misconfigurations": [{"ID": "synthetic", "Severity": "HIGH"}]}]}
        self.assertEqual(evaluate(report, self.policy)["decision"], "BLOCK")
    def test_missing(self):
        with self.assertRaises(ValueError):
            evaluate({}, self.policy)
    def test_human_approval(self):
        self.assertTrue(evaluate({"Results": [{"Target": "demo"}]}, self.policy)["human_approval_required"])
