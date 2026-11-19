"""Finalize evidence inventory without changing the security decision."""
import hashlib
import json
import sys
from pathlib import Path

from evidence_import import REQUIRED, OPTIONAL, MANIFEST


def record(path):
    raw = path.read_bytes()
    return {"sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}


def finalize(directory, outcome):
    directory = Path(directory)
    path = directory / MANIFEST
    manifest = json.loads(path.read_text(encoding="utf-8"))
    if manifest.get("schema_version") != 1 or set(manifest["files"]) != REQUIRED:
        raise ValueError("Incomplete original evidence inventory")
    for name, stored in manifest["files"].items():
        if record(directory / name) != stored:
            raise ValueError("Original evidence changed before finalization")
    assessment = directory / OPTIONAL
    if outcome not in ("success", "skipped"):
        raise ValueError("Assessment did not complete or skip cleanly")
    if assessment.is_file() != (outcome == "success"):
        raise ValueError("Assessment output does not match outcome")
    if outcome == "success":
        manifest["files"][OPTIONAL] = record(assessment)
    manifest["assessment_outcome"] = outcome
    temp = path.with_suffix(".tmp")
    temp.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    temp.replace(path)
    return manifest


if __name__ == "__main__":
    finalize(Path.cwd(), sys.argv[1])
