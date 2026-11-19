import sys
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"sgma"))
from app import create_app
from control_intelligence import (library, reference_extract, control_detail, impact, build_library, verify_sha256,
    NIST53, OT, CSF, CUI, EXTRACT_BLOB, EXTRACT_SHA256, UPSTREAM_BLOB, UPSTREAM_SHA256,
    CATALOG_SHA256, CATALOG_PATH, EXTRACT)
from verify_nist53_extract import verify

class ControlIntelligenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=library()
        cls.nodes={n["node_id"]:n for n in cls.data["nodes"]}

    def test_source_identity_and_counts(self):
        self.assertEqual(self.data["counts"],{"nodes":651,"edges":37,"sources":5})
        sources={s["id"]:s for s in self.data["sources"]}
        self.assertEqual(sources[NIST53]["control_count"],221)
        self.assertEqual(sources[NIST53]["source_class"],"UPSTREAM_CONTROL_EXTRACT")
        self.assertEqual(sources[NIST53]["revision"],"5.2.0")
        self.assertEqual(sources[OT]["source_class"],"SGMA_DERIVED_UNREVIEWED")
        self.assertEqual(hashlib.sha256((CATALOG_PATH/EXTRACT).read_bytes()).hexdigest(),EXTRACT_SHA256)
        self.assertEqual(sources[NIST53]["extract_git_blob"],EXTRACT_BLOB)
        self.assertEqual(sources[NIST53]["git_blob"],UPSTREAM_BLOB)
        self.assertEqual(sources[NIST53]["upstream_raw_sha256"],UPSTREAM_SHA256)
        for key,digest in CATALOG_SHA256.items():
            self.assertEqual(sources[key]["raw_sha256"],digest)
        self.assertFalse(self.data["compliance_certified"])

    def test_extract_pin_rejects_mutation(self):
        raw=(CATALOG_PATH/EXTRACT).read_bytes()
        # Whitespace-only mutation preserves JSON meaning but changes the exact bytes.
        self.assertEqual(json.loads(raw),json.loads(raw+b" "))
        with tempfile.TemporaryDirectory() as directory:
            (Path(directory)/EXTRACT).write_bytes(raw+b" ")
            with patch("control_intelligence.CATALOG_PATH",Path(directory)):
                with self.assertRaisesRegex(ValueError,"SHA-256"):
                    reference_extract()

    def test_full_catalog_tamper_and_verifier_fixture(self):
        extract,_=reference_extract()
        groups={}
        for entry in extract["controls"]:
            groups.setdefault(entry["family"],[]).append(entry["control"])
        fixture={"catalog":{"uuid":extract["source"]["catalog_uuid"],
            "metadata":extract["source"]["metadata"],
            "groups":[{"id":key,"controls":controls} for key,controls in groups.items()]}}
        raw=json.dumps(fixture).encode("utf-8")
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/"fixture.json"
            path.write_bytes(raw)
            # Synthetic fixture tests verifier behavior; never claims to be the full official catalog.
            with patch("verify_nist53_extract.UPSTREAM_SHA256",hashlib.sha256(raw).hexdigest()):
                self.assertEqual(verify(path)["matched_subtrees"],20)
                path.write_bytes(raw+b" ")
                with self.assertRaisesRegex(ValueError,"SHA-256"):
                    verify(path)
            with self.assertRaisesRegex(ValueError,"SHA-256"):
                verify(path)

    def test_existing_catalog_mutation_rejected(self):
        path=CATALOG_PATH/"NIST_SP800-171_rev3_catalog.json"
        raw=path.read_bytes()
        original=Path.read_bytes
        def changed(candidate):
            return raw+b" " if candidate==path else original(candidate)
        with patch.object(Path,"read_bytes",changed):
            with self.assertRaisesRegex(ValueError,"SHA-256"):
                build_library()

    def test_sha256_known_vector(self):
        self.assertEqual(verify_sha256(b"abc",
            "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"),
            hashlib.sha256(b"abc").hexdigest())
        with self.assertRaisesRegex(ValueError,"SHA-256"):
            verify_sha256(b"abd",hashlib.sha256(b"abc").hexdigest())

    def test_every_edge_resolves_and_carries_source_hashes(self):
        self.assertEqual(len({e["edge_id"] for e in self.data["edges"]}),37)
        for edge in self.data["edges"]:
            self.assertEqual(edge["source_sha256"],self.nodes[edge["source_node"]]["source_sha256"])
            self.assertEqual(edge["target_sha256"],self.nodes[edge["target_node"]]["source_sha256"])
            self.assertEqual(edge["relationship"],"related")
            self.assertEqual(edge["evidence_transfer"],"NOT_AUTHORIZED")
            self.assertFalse(edge["transitive_inference"])

    def test_vendor_access_retains_three_source_records(self):
        result=control_detail(OT+":OT-06")
        self.assertEqual({e["other_node"]["node_id"] for e in result["relationships"]},
                         {NIST53+":ac-17",CUI+":SP_800_171_03.01.12"})
        source=control_detail(NIST53+":ac-17")["control"]
        self.assertEqual(source["source_control"]["id"],"ac-17")
        self.assertTrue(source["source_control"]["parts"])
        self.assertEqual(source["source_control"]["title"],source["title"])

    def test_impact_is_direct_only_not_affected_projects(self):
        result=impact({"changed_nodes":[NIST53+":ac-17"]})
        self.assertEqual(result["review_candidates"][0]["direct_review_candidates"],[OT+":OT-06"])
        self.assertEqual(result["affected_projects"],"NOT_EVALUATED")
        self.assertFalse(result["deployment_authorized"])

    def test_routes_and_invalid_node(self):
        client=create_app(None).test_client()
        self.assertEqual(client.get("/controls").status_code,200)
        self.assertEqual(client.get("/controls/library").status_code,200)
        self.assertEqual(client.get("/controls/detail",query_string={"id":CSF+":ID.AM-01"}).status_code,200)
        self.assertEqual(client.get("/controls/detail",query_string={"id":"missing"}).status_code,400)
        for changed in ([],["missing"],[OT+":OT-06",OT+":OT-06"]):
            self.assertEqual(client.post("/controls/impact",json={"changed_nodes":changed}).status_code,400)
