import copy
import os
import sys
import unittest
import uuid
from pathlib import Path

from sqlalchemy import create_engine, select
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"sgma"))
from app import create_app, metadata, example, evaluate, config_engine, audit

class SGMAStorageTests(unittest.TestCase):
    def setUp(self):
        self.engine=config_engine() if os.getenv("SGMA_TEST_MYSQL")=="1" else create_engine("sqlite://")
        if os.getenv("SGMA_TEST_MYSQL")!="1":
            metadata.create_all(self.engine)
        self.client=create_app(self.engine).test_client()
        self.profile=example()
        self.profile["profile_id"]="test-"+uuid.uuid4().hex
    def tearDown(self):
        self.engine.dispose()
    def test_save_reload_and_revision_conflict(self):
        payload={"profile":self.profile}
        r=self.client.post("/save",json=payload)
        self.assertEqual(r.status_code,201,r.get_json())
        number=r.get_json()["assessment_id"]
        self.assertEqual(self.client.get(f"/history/{number}").get_json()["profile"],self.profile)
        changed=copy.deepcopy(self.profile)
        changed["overlays"][0]["threshold"]="LOW"
        self.assertEqual(self.client.post("/save",json={"profile":changed}).status_code,409)
        changed["revision"]="1.1"
        self.assertEqual(self.client.post("/save",json={"profile":changed}).status_code,201)
        with self.engine.connect() as conn:
            self.assertEqual(conn.execute(select(audit.c.event_type).where(audit.c.assessment_id==number)).scalar_one(),"ASSESSMENT_SAVED")
    def test_baseline_tamper(self):
        self.profile["baseline"][0]["threshold"]="CRITICAL"
        self.assertEqual(self.client.post("/save",json={"profile":self.profile}).status_code,400)
    def test_manual_baseline_tamper(self):
        self.profile["manual"].pop()
        self.assertEqual(self.client.post("/assess",json={"profile":self.profile}).status_code,400)
    def test_unverified_evidence(self):
        r=evaluate({"profile":self.profile,"evidence":{"schema_version":1,"decision":"PASS","findings":[]},"scanned":["trivy-sca"]})
        self.assertEqual(r["evidence_trust"],"USER_DECLARED_UNVERIFIED")
        self.assertFalse(r["deployment_authorized"])
    def test_origin_and_health(self):
        self.assertEqual(self.client.post("/save",json={"profile":self.profile},headers={"Origin":"https://example.invalid"}).status_code,403)
        self.assertEqual(self.client.get("/health").status_code,200)
