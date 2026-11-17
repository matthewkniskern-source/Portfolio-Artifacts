import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "security"))
from verify_reviews import verify_record, verify_owner_record, BASE

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

class OwnerReviewTests(unittest.TestCase):
    def setUp(self):
        self.record = {"id":"EXC-test","approved_by":"owner","approved_on":"2026-11-17"}
        self.authority = {"github_logins":["owner"],"final_authority":"owner"}
        self.pr = {"number":7,"user":{"login":"owner"},"base":{"ref":BASE},"head":{"sha":"abc"},"merged":True}
        self.comment = {"id":1,"user":{"login":"owner"},"body":"EXCEPTION EXC-test APPROVE abc","created_at":"2026-11-17T12:00:00Z","updated_at":"2026-11-17T12:00:00Z"}
    def check(self, comments=None, reviewed=None):
        return verify_owner_record(self.record,self.pr,[self.comment] if comments is None else comments,self.record if reviewed is None else reviewed,self.authority)
    def test_owner_can_attest_own_pr(self):
        self.assertFalse(self.check()["independent_review"])
    def test_wrong_actor(self):
        self.comment["user"]["login"]="other"
        with self.assertRaises(ValueError): self.check()
    def test_stale_sha(self):
        self.pr["head"]["sha"]="different"
        with self.assertRaises(ValueError): self.check()
    def test_edit_rejected(self):
        self.comment["updated_at"]="2026-11-17T12:01:00Z"
        with self.assertRaises(ValueError): self.check()
    def test_no_attestation(self):
        with self.assertRaises(ValueError): self.check(comments=[])
    def test_rejection_overrides(self):
        rejection={**self.comment,"id":2,"body":"EXCEPTION EXC-test REJECT abc"}
        with self.assertRaises(ValueError): self.check(comments=[self.comment,rejection])
    def test_changed_record(self):
        with self.assertRaises(ValueError): self.check(reviewed={**self.record,"reason":"changed"})
