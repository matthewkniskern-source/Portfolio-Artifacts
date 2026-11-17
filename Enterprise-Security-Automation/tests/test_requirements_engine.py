import json
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"governance"))
from requirements_engine import assess

class RequirementsTests(unittest.TestCase):
    def setUp(self):
        self.profile=json.loads((ROOT/"governance/profiles/synthetic-project-a.json").read_text())
        self.evidence={"schema_version":1,"decision":"PASS","findings":[{"scanner":"trivy-sca","id":"TEST-CVE","severity":"MEDIUM","disposition":"advisory"}]}
    def test_overlay_strengthens(self):
        r=assess(self.profile,self.evidence,["trivy-sca"])
        self.assertEqual(r["effective_rules"]["trivy-sca"]["threshold"],"MEDIUM")
        self.assertEqual(next(x for x in r["requirements"] if x["id"]=="CON-001")["status"],"GAP")
        self.assertEqual(r["ci_decision"],"PASS")
    def test_weaker_overlay_cannot_lower_baseline(self):
        self.profile["overlays"][0]["threshold"]="CRITICAL"
        self.profile["overlays"][0]["allow_exceptions"]=True
        r=assess(self.profile)
        self.assertEqual(r["effective_rules"]["trivy-sca"]["threshold"],"HIGH")
        self.assertFalse(r["effective_rules"]["trivy-sca"]["allow_exceptions"])
    def test_missing_evidence(self):
        self.assertEqual(assess(self.profile)["requirements"][0]["status"],"EVIDENCE MISSING")
    def test_no_authority(self):
        r=assess(self.profile,self.evidence,["trivy-sca"])
        self.assertFalse(r["deployment_authorized"])
        self.assertFalse(r["policy_changed"])
        self.assertFalse(r["compliance_certified"])
    def test_duplicate(self):
        self.profile["overlays"][0]["id"]="ORG-001"
        with self.assertRaises(ValueError): assess(self.profile)
    def test_baseline_not_disabled(self):
        self.profile["baseline"][0]["applicability"]="not_applicable"
        self.profile["baseline"][0]["rationale"]="demo"
        with self.assertRaises(ValueError): assess(self.profile)
    def test_na_requires_reason(self):
        self.profile["overlays"][0]["applicability"]="not_applicable"
        with self.assertRaises(ValueError): assess(self.profile)
    def test_manual_review(self):
        self.assertEqual(assess(self.profile)["requirements"][-1]["status"],"REVIEW REQUIRED")
    def test_invalid_evidence(self):
        with self.assertRaises(ValueError): assess(self.profile,{"decision":"PASS"})
    def test_exception_not_generalized(self):
        self.evidence["findings"]=[{"scanner":"trivy-sca","id":"TEST","severity":"HIGH","disposition":"exception_approved"}]
        r=assess(self.profile,self.evidence,["trivy-sca"])
        self.assertEqual(r["requirements"][0]["status"],"GAP")
