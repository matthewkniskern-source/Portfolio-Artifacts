import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"security"))
from unified_gate import combine

class UnifiedTests(unittest.TestCase):
    def setUp(self):
        self.iac={"decision":"EXCEPTION APPROVED","findings":[{"check_id":"AWS-0132","target":"main.tf","severity":"HIGH","disposition":"exception_approved","exception_id":"EXC-0001"}]}
        self.exp={"decision":"PASS","findings":[]}
        self.reviews=[{"exception_id":"EXC-0001"}]
    def test_approved(self):
        self.assertEqual(combine(self.iac,self.exp,self.reviews)["decision"],"EXCEPTION APPROVED")
    def test_missing_attestation_blocks(self):
        self.assertEqual(combine(self.iac,self.exp,[])["decision"],"BLOCK")
    def test_expanded_block_wins(self):
        self.exp={"decision":"BLOCK","findings":[{"scanner":"semgrep","blocking":True}]}
        self.assertEqual(combine(self.iac,self.exp,self.reviews)["decision"],"BLOCK")
    def test_pending(self):
        self.iac={"decision":"EXCEPTION PENDING","findings":[]}
        self.assertEqual(combine(self.iac,self.exp,[])["decision"],"EXCEPTION PENDING")
    def test_no_deployment(self):
        self.assertFalse(combine(self.iac,self.exp,self.reviews)["deployment_authorized"])
    def test_scan_error(self):
        self.exp["decision"]="SCAN ERROR"
        with self.assertRaises(ValueError): combine(self.iac,self.exp,self.reviews)
