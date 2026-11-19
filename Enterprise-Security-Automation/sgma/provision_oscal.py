"""Offline provision of selected NIST release schemas; no network or ZIP extraction."""
import argparse
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile

RELEASE_SHA256 = "eefb4ec5b1383d3b15fca27e0b63bc84b8661d6ee17e4f92acb437606e9ee982"
MODELS = {"catalog","profile","component-definition","system-security-plan",
          "assessment-plan","assessment-results","plan-of-action-and-milestones","control-mapping"}
TARGET = Path(__file__).resolve().parents[1]/"interoperability"/"oscal"/"schemas"/"1.2.3"

def provision(archive, target=TARGET):
    if archive.stat().st_size > 5_000_000 or hashlib.sha256(archive.read_bytes()).hexdigest()!=RELEASE_SHA256:
        raise ValueError("Release archive does not match published SHA-256")
    payloads={}
    names={"oscal_"+m+"_schema.json" for m in MODELS}
    with ZipFile(archive) as z:
        for item in z.infolist():
            name=Path(item.filename).name
            if name not in names:
                continue
            if name in payloads or item.file_size>4_000_000:
                raise ValueError("Unexpected schema member")
            raw=z.read(item)
            json.loads(raw)
            payloads[name]=raw
    if not {"oscal_catalog_schema.json","oscal_profile_schema.json"}<=payloads.keys():
        raise ValueError("Release archive lacks required catalog/profile schemas")
    target.mkdir(parents=True,exist_ok=True)
    manifest={}
    for name,raw in payloads.items():
        (target/name).write_bytes(raw)
        manifest[name]=hashlib.sha256(raw).hexdigest()
    (target/"schema-manifest.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    return sorted(manifest)

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("archive",type=Path)
    print(provision(parser.parse_args().archive))
