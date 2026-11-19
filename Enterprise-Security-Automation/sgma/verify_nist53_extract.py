"""Compare the vendored partial control extract to the complete upstream JSON, offline."""
import argparse
import json
from pathlib import Path
from control_intelligence import verify_sha256, reference_extract, UPSTREAM_BLOB, UPSTREAM_SHA256, walk_controls

def verify(path):
    path=Path(path)
    if path.stat().st_size>16_000_000:
        raise ValueError("Full catalog exceeds offline verification limit")
    raw=path.read_bytes()
    digest=verify_sha256(raw,UPSTREAM_SHA256)
    source=json.loads(raw)["catalog"]
    extract,_=reference_extract()
    if source["uuid"]!=extract["source"]["catalog_uuid"] or source["metadata"]!=extract["source"]["metadata"]:
        raise ValueError("Catalog metadata differs")
    expected={control["id"]:{"family":group["id"],"control":control}
              for group in source["groups"] for control in group["controls"]}
    if any(expected.get(row["control"]["id"])!=row for row in extract["controls"]):
        raise ValueError("Extracted control differs from upstream")
    total=sum(1 for group in source["groups"] for control in group["controls"] for _ in walk_controls(control,[]))
    selected=sum(1 for row in extract["controls"] for _ in walk_controls(row["control"],[]))
    return {"upstream_git_blob":UPSTREAM_BLOB,"upstream_raw_sha256":digest,"full_controls":total,
            "selected_controls_including_enhancements":selected,"matched_subtrees":len(extract["controls"]),
            "status":"EXACT_PARSED_CONTENT_MATCH","approval":"NOT_APPROVED"}

if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("catalog",help="Locally obtained complete pinned upstream JSON")
    print(json.dumps(verify(parser.parse_args().catalog),indent=2))
