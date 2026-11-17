import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"security"))
from expanded_gate import evaluate

class ExpandedGateTests(unittest.TestCase):
    def setUp(self):
        self.sast={"results":[],"errors":[]}
        self.sca={"SchemaVersion":2,"Results":[{"Target":"requirements.txt","Packages":[{"Name":"Jinja2"},{"Name":"MarkupSafe"}]}]}
        self.secrets=[]
    def gate(self):
        return evaluate(self.sast,self.sca,self.secrets)
    def test_clean(self):
        self.assertEqual(self.gate()["decision"],"PASS")
        self.assertFalse(self.gate()["deployment_authorized"])
    def test_sast_blocks(self):
        self.sast["results"]=[{"check_id":"rule","path":"sample.py","extra":{"severity":"ERROR"}}]
        self.assertEqual(self.gate()["decision"],"BLOCK")
    def test_high_dependency_blocks(self):
        self.sca["Results"][0]["Vulnerabilities"]=[{"VulnerabilityID":"synthetic","Severity":"HIGH"}]
        self.assertEqual(self.gate()["decision"],"BLOCK")
    def test_medium_dependency_advisory(self):
        self.sca["Results"][0]["Vulnerabilities"]=[{"VulnerabilityID":"synthetic","Severity":"MEDIUM"}]
        self.assertFalse(self.gate()["findings"][0]["blocking"])
    def test_unknown_dependency_blocks(self):
        self.sca["Results"][0]["Vulnerabilities"]=[{"VulnerabilityID":"synthetic"}]
        self.assertEqual(self.gate()["decision"],"BLOCK")
    def test_secret_blocks(self):
        self.secrets=[{"RuleID":"synthetic","File":"sample.txt","Secret":"not-real"}]
        result=self.gate()
        self.assertEqual(result["decision"],"BLOCK")
        self.assertNotIn("not-real",str(result))
    def test_missing_inventory(self):
        self.sca["Results"]=[]
        with self.assertRaises(ValueError): self.gate()
    def test_scan_error(self):
        self.sast["errors"]=[{"message":"parse error"}]
        with self.assertRaises(ValueError): self.gate()
    def test_invalid_secret_report(self):
        self.secrets={}
        with self.assertRaises(ValueError): self.gate()
