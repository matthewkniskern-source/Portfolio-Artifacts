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

    def test_bundled_authoritative_templates(self):
        from roadmap import load_template
        for key,expected in (("nist-800-171-r3",130),("nist-csf-2",219),("nist-ssdf",61)):
            entry=load_template(key)
            self.assertEqual(len(entry["controls"]),expected)
            self.assertEqual(entry["template"]["review_status"],"PROPOSED_UNREVIEWED")
            self.assertEqual(entry["oscal_version"],"v1.2.2")

    def test_multiple_templates_and_contract_rule(self):
        from roadmap import load_template
        base=compose("project-a","1",["CON-A@1.1"])
        contract=draft()
        contract["requirements"][0].update(method="hybrid",applicability="applicable",
                                          rule={"scanner":"semgrep","threshold":"HIGH"})
        inputs=[{"template":key,"selected":[load_template(key)["controls"][0]["id"]]}
                for key in ("nist-800-171-r3","nist-csf-2")]
        result=compose_overlay(base,None,[],contract,"2",inputs)["proposal"]
        self.assertEqual(result["baseline"],base["baseline"])
        self.assertEqual(len([item for item in result["manual"] if item["id"].startswith("OSCAL-")]),2)
        self.assertTrue(any(x["id"]=="DRAFT-01-manual" for x in result["manual"]))
        self.assertFalse(next(x for x in result["overlays"] if x["id"]=="DRAFT-01")["allow_exceptions"])

    def test_occurrence_consolidation_with_duplicate_cve(self):
        base=compose("project-a","1",["CON-A@1.1"])
        evidence={"schema_version":1,"decision":"BLOCK","findings":[
           {"scanner":"trivy-sca","id":"CVE-X","target":"a","severity":"HIGH","disposition":"blocking"},
           {"scanner":"trivy-sca","id":"CVE-X","target":"b","severity":"HIGH","disposition":"blocking"}]}
        response=self.client.post("/assess",json={"profile":base,"evidence":evidence,"scanned":["trivy-sca"]})
        self.assertEqual(response.status_code,200)
        records=[r for r in decision_queue(response.json)["records"] if "occurrence" in r]
        self.assertEqual(len(records),2)
        self.assertEqual(len({r["record_id"] for r in records}),2)
        for row in records:
            self.assertEqual({x["requirement_id"] for x in row["requirements"]},{"ORG-001","CON-001"})

    def test_exchange_manifest_and_local_references(self):
        import io
        import zipfile
        base=compose("project-a","1",[])
        response=self.client.post("/roadmap/exchange",json={
            "base":base,"revision":"2","contract":draft(),
            "selections":[{"catalog":example_catalog(),"selected":["ac-1"]}]})
        self.assertEqual(response.status_code,200)
        with zipfile.ZipFile(io.BytesIO(response.data)) as archive:
            manifest=json.loads(archive.read("exchange-manifest.json"))
            self.assertEqual(manifest["resolution"],"NOT_EXECUTED")
            self.assertFalse(manifest["deployment_authorized"])
            for name,entry in manifest["files"].items():
                self.assertEqual(hashlib.sha256(archive.read(name)).hexdigest(),entry["sha256"])
            profile=json.loads(archive.read("profile.json"))["profile"]
            self.assertEqual(len(profile["imports"]),3)
            self.assertTrue(all(row["href"] in archive.namelist() for row in profile["imports"]))

    def test_decision_action_has_no_authority(self):
        response=self.client.post("/roadmap/decision-draft",json={"assessment_sha256":"0"*64,
            "record_id":"requirement:ORG-001","proposed_owner":"analyst-a","proposed_action":"investigate",
            "due_date":"2026-11-30","rationale":"Collect evidence"})
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json["decision_state"],"PENDING_HUMAN_REVIEW")
        self.assertFalse(response.json["deployment_authorized"])

    def test_lifecycle_inspection_does_not_grant_compliance(self):
        response=self.client.post("/roadmap/lifecycle",json={"mapping-collection":{
            "uuid":"98a5cb12-7012-4f8f-a393-2ab42e10ab45","metadata":{
            "title":"Synthetic mapping","last-modified":"2026-11-19T00:00:00Z",
            "version":"1","oscal-version":"1.2.3"}}})
        # If the official schema is provisioned this incomplete fixture may be rejected.
        if response.status_code==200:
            self.assertEqual(response.json["semantic_validation"],"NOT_EXECUTED")
            self.assertFalse(response.json["compliance_certified"])
        else:
            self.assertEqual(response.status_code,400)
