import io
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "sgma"))
from app import create_app, example
from test_evidence_import import package


class EvidenceWorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.client = create_app(None).test_client()

    def submit(self, raw, profile=None, **extra):
        return self.client.post("/assess-package", data={
            "profile": json.dumps(example() if profile is None else profile),
            "archive": (io.BytesIO(raw), "evidence.zip"), **extra
        })

    def test_preview(self):
        self.assertEqual(self.client.get("/health").json["mode"], "preview")
        self.assertEqual(self.client.get("/history").status_code, 503)
        self.assertEqual(self.client.post("/save", json={}).status_code, 503)

    def test_package_trust(self):
        result = self.submit(package()).json
        self.assertEqual(result["evidence_trust"], "MANIFEST_MATCH_UNAUTHENTICATED")
        self.assertEqual(result["project_association"], "PROPOSED_UNVERIFIED")
        self.assertEqual(len(result["evidence_package"]["scanned"]), 4)
        self.assertFalse(result["deployment_authorized"])
        self.assertFalse(result["compliance_certified"])
        self.assertEqual(result["ci_decision"], "PASS")

    def test_block_preserved(self):
        result = self.submit(package(block=True), scanned="[]").json
        self.assertEqual(result["ci_decision"], "BLOCK")
        self.assertTrue(any(row["status"] == "GAP" for row in result["requirements"]))

    def test_invalid_archive(self):
        for raw in (b"invalid", package(tamper=True), package(missing=True)):
            self.assertEqual(self.submit(raw).status_code, 400)

    def test_baseline_guard(self):
        profile = example()
        profile["baseline"] = []
        self.assertEqual(self.submit(package(), profile).status_code, 400)

    def test_json_remains_unverified(self):
        result = self.client.post("/assess", json={"profile": example(),
            "evidence": {"schema_version": 1, "decision": "PASS", "findings": []},
            "scanned": ["semgrep"], "evidence_trust": "AUTHENTICATED"}).json
        self.assertEqual(result["evidence_trust"], "USER_DECLARED_UNVERIFIED")

    def test_origin_and_content_type(self):
        self.assertEqual(self.client.post("/assess-package", json={}).status_code, 415)
        self.assertEqual(self.client.post("/assess-package", json={},
            headers={"Origin": "https://example.invalid"}).status_code, 403)
