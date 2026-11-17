import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "security"))
from verify_reviews import verify_record, BASE

class ReviewTests(unittest.TestCase):
    def setUp(self):
        self.record = {"id":"EXC-test","approved_by":"reviewer","approved_on":"2026-11-17"}
        self.pr = {"number":7,"user":{"login":"author"},"base":{"ref":BASE},"head":{"sha":"abc"},"merged":True}
        self.review = {"id":1,"user":{"login":"reviewer"},"state":"APPROVED","commit_id":"abc","submitted_at":"2026-11-17T12:00:00Z"}
    def check(self, authorized=None, reviewed=None, reviews=None):
        return verify_record(self.record,self.pr,[self.review] if reviews is None else reviews,self.record if reviewed is None else reviewed,{"reviewer"} if authorized is None else authorized)
    def test_valid(self):
        self.assertEqual(self.check()["review_id"],1)
    def test_self_approval(self):
        self.pr["user"]["login"]="reviewer"
        with self.assertRaises(ValueError): self.check()
    def test_unauthorized(self):
        with self.assertRaises(ValueError): self.check(authorized=set())
    def test_stale_commit(self):
        self.review["commit_id"]="old"
        with self.assertRaises(ValueError): self.check()
    def test_changed_record(self):
        with self.assertRaises(ValueError): self.check(reviewed={**self.record,"reason":"changed"})
    def test_rejected(self):
        self.review["state"]="CHANGES_REQUESTED"
        with self.assertRaises(ValueError): self.check()
    def test_unmerged(self):
        self.pr["merged"]=False
        with self.assertRaises(ValueError): self.check()
    def test_date_mismatch(self):
        self.record["approved_on"]="2026-11-16"
        with self.assertRaises(ValueError): self.check()
