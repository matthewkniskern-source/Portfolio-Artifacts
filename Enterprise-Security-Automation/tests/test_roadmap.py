import copy
import hashlib
import json
import os
import sys
import unittest
from pathlib import Path
from unittest.mock import patch
from sqlalchemy import create_engine

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"sgma"))
from app import create_app, metadata
from requirements_library import compose
from roadmap import catalog, profile_export, contract_draft, compare_contract, compose_overlay, decision_queue
from roadmap_store import principal

def example_catalog():
    return {"catalog":{"uuid":"98a5cb12-7012-4f8f-a393-2ab42e10ab45",
        "metadata":{"title":"Synthetic catalog","last-modified":"2026-11-19T00:00:00Z",
                    "version":"1.0","oscal-version":"1.2.3"},
        "groups":[{"id":"ac","title":"Access control","controls":[
            {"id":"ac-1","title":"Example control","controls":[{"id":"ac-1.1","title":"Example enhancement"}]}]}]}}

def draft():
    return {"contract_id":"contract-a","revision":"1","customer":"Synthetic",
            "requirements":[{"id":"DRAFT-01","title":"Report incident",
                "clause":"1.1","statement":"Notify customer","method":"manual",
                "evidence":"Record of notification","applicability":"undetermined"}]}

class RoadmapTests(unittest.TestCase):
    def setUp(self):
        self.client=create_app(None).test_client()

    def test_catalog_projection_preserves_hierarchy_and_content(self):
        doc=example_catalog()
        result=catalog(doc)
        self.assertEqual(result["original"],doc)
        self.assertEqual(result["controls"][1]["parents"],["ac","ac-1"])
        self.assertEqual(result["approval"],"NOT_APPROVED")

    def test_duplicate_control_rejected(self):
        doc=example_catalog()
        doc["catalog"]["groups"][0]["controls"]*=2
        self.assertEqual(self.client.post("/roadmap/catalog",json=doc).status_code,400)

    def test_profile_selected_ids(self):
        result=profile_export(example_catalog(),["ac-1"])
        self.assertEqual(result["document"]["profile"]["imports"][0]["include-controls"][0]["with-ids"],["ac-1"])
        self.assertEqual(result["resolution"],"NOT_EXECUTED")

    def test_profile_unknown_selection(self):
        self.assertEqual(self.client.post("/roadmap/profile",json={"catalog":example_catalog(),"selected":["absent"]}).status_code,400)

    def test_contract_revision_comparison(self):
        before=draft()
        after=copy.deepcopy(before)
        after["revision"]="2"
        after["requirements"][0]["statement"]="Notify within one hour"
        self.assertEqual(compare_contract(before,after)["changed"],["DRAFT-01"])

    def test_nonapplicability_rationale(self):
        row=draft()
        row["requirements"][0]["applicability"]="not_applicable"
        self.assertEqual(self.client.post("/roadmap/contract",json=row).status_code,400)

    def test_overlay_keeps_registry_and_routes_to_manual(self):
        base=compose("project-a","1",["CON-A@1.1"])
        result=compose_overlay(base,example_catalog(),["ac-1"],draft(),"2")
        proposal=result["proposal"]
        self.assertEqual(base["baseline"],proposal["baseline"])
        self.assertEqual(base["library"],proposal["library"])
        response=self.client.post("/assess",json={"profile":proposal})
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json["effective_rules"]["trivy-sca"]["threshold"],"LOW")
        self.assertFalse(response.json["deployment_authorized"])
        self.assertEqual(next(x for x in response.json["requirements"] if x["id"]=="DRAFT-01")["status"],"REVIEW REQUIRED")

    def test_altered_baseline_rejected(self):
        base=compose("project-a","1",[])
        base["baseline"][0]["threshold"]="CRITICAL"
        self.assertEqual(self.client.post("/roadmap/compose",json={"base":base,"revision":"2"}).status_code,400)

    def test_mapping_remains_unapproved(self):
        response=self.client.post("/roadmap/mapping",json={"source":"a","target":"b","relationship":"partial","rationale":"Shared scope"})
        self.assertEqual(response.json["status"],"PROPOSED_UNVERIFIED")
        self.assertFalse(response.json["compliance_certified"])

    def test_queue_does_not_dedupe_by_finding_id(self):
        result=decision_queue({"requirements":[{"id":"A","status":"GAP","finding_ids":["CVE-X"]},
                    {"id":"B","status":"GAP","finding_ids":["CVE-X"]}]})
        self.assertEqual(len(result["records"]),2)
        self.assertEqual(result["source_trust"],"USER_DECLARED_UNVERIFIED")

    def test_preview_denies_persistence(self):
        self.assertEqual(self.client.get("/roadmap/projects/project-a/drafts").status_code,403)

    def test_scoped_authorization_and_immutable_draft(self):
        token="synthetic-test-token-"+"x"*32
        config=[{"id":"tester","role":"contract_coordinator","projects":["project-a"],
                 "token_sha256":hashlib.sha256(token.encode()).hexdigest()}]
        self.assertIsNone(principal(config,token,"project-b","read"))
        engine=create_engine("sqlite://")
        metadata.create_all(engine)
        try:
            client=create_app(engine).test_client()
            headers={"Authorization":"Bearer "+token}
            payload={"kind":"contract","record_key":"contract-a","revision":"1","payload":draft()}
            with patch.dict(os.environ,{"SGMA_ROADMAP_PRINCIPALS":json.dumps(config)}):
                self.assertEqual(client.post("/roadmap/projects/project-a/drafts",json=payload).status_code,403)
                self.assertEqual(client.post("/roadmap/projects/project-a/drafts",json=payload,headers=headers).status_code,201)
                self.assertEqual(client.post("/roadmap/projects/project-a/drafts",json=payload,headers=headers).status_code,409)
                self.assertEqual(client.get("/roadmap/projects/project-b/drafts",headers=headers).status_code,403)
                self.assertEqual(len(client.get("/roadmap/projects/project-a/drafts",headers=headers).json["records"]),1)
        finally:
            engine.dispose()
