import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"sgma"))
from app import create_app
from requirements_library import compose
from roadmap import fingerprint

class OtIntelligenceTests(unittest.TestCase):
    def setUp(self):
        self.client=create_app(None).test_client()
        self.context={"sector":"district-energy","system":"bas-ddc","customer":"dod",
                      "phase":"commissioning","features":["vendor-access","legacy"]}

    def test_library_and_page(self):
        self.assertEqual(self.client.get("/ot").status_code,200)
        result=self.client.get("/ot/library").json
        self.assertEqual(len(result["controls"]),20)
        self.assertTrue(all(r["relationship"]=="RELATED_UNREVIEWED" for r in result["controls"]))
        self.assertTrue(all(r["acceptance_candidate"] for r in result["controls"]))
        self.assertFalse(result["compliance_certified"])

    def test_context_discovery_scope_and_reasons(self):
        result=self.client.post("/ot/discover",json=self.context).json
        rows={x["id"]:x for x in result["recommendations"]}
        self.assertIn("Declared feature: vendor-access",rows["OT-06"]["recommendation_reasons"])
        self.assertIn("OT-19",rows)
        self.assertIn("OT-20",rows)
        sources={x["id"] for x in result["sources_to_review"]}
        self.assertIn("ufc",sources)
        self.assertNotIn("nerc",sources)
        self.assertEqual(result["context_sha256"],fingerprint(result["context"]))
        self.assertEqual(result["applicability"],"HUMAN_DETERMINATION_REQUIRED")

    def test_sector_reference_not_mandate(self):
        context={**self.context,"sector":"electric","customer":"private"}
        result=self.client.post("/ot/discover",json=context).json
        self.assertTrue(any(x["id"]=="nerc" and x["availability"]=="REFERENCE_ONLY" for x in result["sources_to_review"]))
        self.assertFalse(result["policy_changed"])

    def test_deliverable_contract_interoperability(self):
        payload={"context":self.context,"selected":["OT-06","OT-10"],"contract_id":"OT-DEMO",
                 "revision":"1.0","customer":"Synthetic"}
        response=self.client.post("/ot/deliverables",json=payload)
        self.assertEqual(response.status_code,200)
        result=response.json
        self.assertEqual(result["contract_sha256"],fingerprint(result["contract_draft"]))
        self.assertEqual(result["review_state"],"PENDING_HUMAN_REVIEW")
        self.assertEqual(len(result["traceability_matrix"]),2)
        self.assertTrue(all(x["owner"] is None for x in result["acceptance_checklist"]))
        base=compose("project-a","1",["CON-A@1.1"])
        proposal=self.client.post("/roadmap/compose",json={"base":base,"revision":"2",
            "contract":result["contract_draft"]})
        self.assertEqual(proposal.status_code,200)
        native=proposal.json["proposal"]
        self.assertEqual(native["baseline"],base["baseline"])
        self.assertEqual(native["overlays"],base["overlays"])
        assessment=self.client.post("/assess",json={"profile":native}).json
        self.assertEqual(assessment["effective_rules"]["trivy-sca"]["threshold"],"LOW")
        for row in assessment["requirements"]:
            if row["id"].startswith("DRAFT-OT-"):
                self.assertEqual(row["status"],"REVIEW REQUIRED")
        self.assertFalse(assessment["deployment_authorized"])

    def test_invalid_context_and_selection(self):
        self.assertEqual(self.client.post("/ot/discover",json={**self.context,"features":["legacy","legacy"]}).status_code,400)
        for selected in ([],["OT-99"],["OT-06","OT-06"]):
            self.assertEqual(self.client.post("/ot/deliverables",json={"context":self.context,
                "selected":selected,"contract_id":"OT-DEMO","revision":"1","customer":"Synthetic"}).status_code,400)
