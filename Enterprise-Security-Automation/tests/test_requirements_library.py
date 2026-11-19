import copy
import io
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "sgma"))
from app import create_app, example
from requirements_library import compose, registry
from test_evidence_import import package


class RequirementsLibraryTests(unittest.TestCase):
    def setUp(self):
        self.client = create_app(None).test_client()

    def assess(self, profile):
        return self.client.post("/assess", json={"profile": profile})

    def test_registry_read_only(self):
        data = self.client.get("/library").json
        self.assertEqual(data["active_baseline"], "ORG-BASE@1.0")
        self.assertEqual(self.client.post("/library", json=data).status_code, 405)
        self.assertEqual(len(registry()[1]), 3)

    def test_legacy_compatibility(self):
        result = self.assess(example()).json
        self.assertEqual(result["requirements_library"]["status"], "LEGACY_PROPOSAL")

    def test_compose_revision_precedence(self):
        for ref, threshold in (("CON-A@1.0", "MEDIUM"), ("CON-A@1.1", "LOW")):
            response = self.client.post("/library/compose", json={
                "profile_id": "project-a", "revision": "2", "overlays": [ref]})
            self.assertEqual(response.status_code, 200)
            result = self.assess(response.json).json
            self.assertEqual(result["effective_rules"]["trivy-sca"]["threshold"], threshold)
            self.assertEqual(result["requirements_library"]["approval"], "NOT_APPROVED")
            self.assertFalse(result["policy_changed"])

    def test_baseline_only(self):
        profile = compose("project-a", "2", [])
        self.assertEqual(len(profile["baseline"]), 4)
        self.assertEqual([r["id"] for r in profile["manual"]], ["MAN-002"])

    def test_invalid_selection(self):
        for refs in (["CON-A@9"], ["CON-A@1.0", "CON-A@1.1"],
                     ["ORG-BASE@1.0"], ["CON-A@1.0", "CON-A@1.0"]):
            self.assertEqual(self.client.post("/library/compose", json={
                "profile_id": "project-a", "revision": "2", "overlays": refs}).status_code, 400)

    def test_selected_rows_cannot_be_weakened(self):
        original = compose("project-a", "2", ["CON-A@1.1"])
        for group in ("baseline", "overlays", "manual"):
            changed = copy.deepcopy(original)
            changed[group].pop()
            self.assertEqual(self.assess(changed).status_code, 400)
        changed = copy.deepcopy(original)
        changed["overlays"][0]["threshold"] = "CRITICAL"
        self.assertEqual(self.assess(changed).status_code, 400)

    def test_reference_hash_mismatch(self):
        profile = compose("project-a", "2", ["CON-A@1.0"])
        profile["library"]["entry_sha256"]["CON-A@1.0"] = "0" * 64
        self.assertEqual(self.assess(profile).status_code, 400)

    def test_ad_hoc_addition_remains_draft(self):
        profile = compose("project-a", "2", ["CON-A@1.0"])
        profile["overlays"].append({**profile["overlays"][0], "id": "DRAFT-001", "threshold": "LOW"})
        result = self.assess(profile).json
        self.assertEqual(result["effective_rules"]["trivy-sca"]["threshold"], "LOW")
        self.assertEqual(result["requirements_library"]["approval"], "NOT_APPROVED")

    def test_archive_assessment_preserves_library_trace(self):
        profile = compose("project-a", "2", ["CON-A@1.1"])
        response = self.client.post("/assess-package", data={
            "profile": json.dumps(profile),
            "archive": (io.BytesIO(package(block=True)), "evidence.zip")})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["ci_decision"], "BLOCK")
        self.assertEqual(response.json["requirements_library"]["library"], profile["library"])
        self.assertEqual(response.json["evidence_trust"], "MANIFEST_MATCH_UNAUTHENTICATED")
