import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"sgma"))
from app import create_app
from control_intelligence import (library, reference_extract, control_detail, impact, git_blob,
    NIST53, OT, CSF, CUI, EXTRACT_BLOB, CATALOG_PATH, EXTRACT)

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
        self.assertEqual(git_blob((CATALOG_PATH/EXTRACT).read_bytes()),EXTRACT_BLOB)
        self.assertFalse(self.data["compliance_certified"])

    def test_extract_pin_rejects_mutation(self):
        with patch("control_intelligence.EXTRACT_BLOB","0"*40):
            with self.assertRaises(ValueError):
                reference_extract()

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
