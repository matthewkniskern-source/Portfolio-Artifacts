import hashlib
import io
import json
import sys
import unittest
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "security"))
from evidence_import import verify_package
from expanded_gate import evaluate
from unified_gate import combine


def package(block=False, tamper=False, missing=False, extra=False, duplicate=False,
            inconsistent=False, bad_source=False, assessment=None, assessment_tamper=False):
    sast = {"errors": [], "results": []}
    if block:
        sast["results"].append({"check_id": "synthetic-rule", "path": "fixture.py"})
    sca = {"SchemaVersion": 2, "Results": [{"Target": "fixture",
           "Packages": [{"Name": "jinja2"}, {"Name": "markupsafe"}]}]}
    expanded = evaluate(sast, sca, [])
    gate = {"decision": "PASS", "findings": []}
    result = combine(gate, expanded, [])
    if inconsistent:
        result["decision"] = "PASS" if block else "BLOCK"
    reports = {"trivy.json": {"Results": [{"Target": "fixture"}]},
               "semgrep.json": sast, "sca.json": sca, "gitleaks.json": [],
               "gate.json": gate, "expanded-gate.json": expanded,
               "review-evidence.json": [], "unified-decision.json": result}
    data = {name: json.dumps(value).encode() for name, value in reports.items()}
    manifest = {"schema_version": 1, "repository": "example/synthetic",
                "run_id": "123", "attempt": "1", "commit": "a" * 40,
                "files": {name: {"sha256": hashlib.sha256(raw).hexdigest(),
                                 "bytes": len(raw)} for name, raw in data.items()}}
    if bad_source:
        manifest["commit"] = "unknown"
    if assessment is not None:
        data["requirements-assessment.json"] = b'{"approval":"NOT_APPROVED"}'
        if assessment == "covered":
            raw = data["requirements-assessment.json"]
            manifest["files"]["requirements-assessment.json"] = {"sha256": hashlib.sha256(raw).hexdigest(), "bytes":len(raw)}
            manifest["assessment_outcome"] = "success"
        if assessment == "missing_coverage":
            manifest["assessment_outcome"] = "success"
        if assessment_tamper:
            data["requirements-assessment.json"] += b" "
    data["evidence-manifest.json"] = json.dumps(manifest).encode()
    if tamper:
        data["semgrep.json"] += b" "
    if missing:
        del data["sca.json"]
    if extra:
        data["../unexpected.json"] = b"{}"
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w") as archive:
        for name, raw in data.items():
            archive.writestr(name, raw)
        if duplicate:
            archive.writestr("sca.json", data["sca.json"])
    return stream.getvalue()


class EvidenceImportTests(unittest.TestCase):
    def test_clean(self):
        result = verify_package(package())
        self.assertEqual(result["integrity"], "MANIFEST_MATCH")
        self.assertEqual(result["provenance"], "UNAUTHENTICATED")
        self.assertEqual(len(result["scanned"]), 4)
        self.assertEqual(result["evidence"]["decision"], "PASS")
        self.assertFalse(result["deployment_authorized"])
        self.assertIsNone(result["workflow"])

    def test_block_is_valid_evidence(self):
        self.assertEqual(verify_package(package(block=True))["evidence"]["decision"], "BLOCK")

    def test_rejections(self):
        for options in ({"tamper": True}, {"missing": True}, {"extra": True},
                        {"duplicate": True}, {"inconsistent": True}, {"bad_source": True}):
            with self.subTest(options=options), self.assertRaises(ValueError):
                verify_package(package(**options))

    def test_legacy_optional_is_unverified(self):
        self.assertEqual(verify_package(package(assessment="legacy"))["unverified_optional_reports"], ["requirements-assessment.json"])

    def test_manifested_assessment_integrity(self):
        self.assertEqual(verify_package(package(assessment="covered"))["unverified_optional_reports"], [])
        for options in ({"assessment":"covered","assessment_tamper":True}, {"assessment":"missing_coverage"}):
            with self.assertRaises(ValueError):
                verify_package(package(**options))

    def test_invalid_zip(self):
        with self.assertRaises(ValueError):
            verify_package(b"not an archive")
