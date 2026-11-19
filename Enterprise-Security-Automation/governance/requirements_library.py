"""Repository-controlled synthetic requirements; composition never grants approval."""
import copy
import hashlib
import json
from pathlib import Path

from requirements_engine import validate

REGISTRY = Path(__file__).resolve().parent / "library" / "registry.json"
GROUPS = ("baseline", "overlays", "manual")


def fingerprint(value):
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                     allow_nan=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def registry():
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        raise ValueError("Unsupported library schema")
    entries = {}
    for row in data["entries"]:
        key = row["id"] + "@" + row["revision"]
        if key in entries or row["kind"] not in {"baseline", "contract", "regulatory"}:
            raise ValueError("Invalid library entry")
        if row["status"] != "repository_controlled":
            raise ValueError("Unrecognized library status")
        if row["kind"] != "baseline" and row["baseline"]:
            raise ValueError("Overlay cannot contain baseline rows")
        if row["kind"] == "baseline" and row["overlays"]:
            raise ValueError("Baseline cannot contain overlay rows")
        entries[key] = row
    active = entries[data["active_baseline"]]
    if active["kind"] != "baseline":
        raise ValueError("Invalid active baseline")
    for key, row in entries.items():
        parent = row["supersedes"]
        if parent is not None and (parent == key or parent not in entries or
                entries[parent]["id"] != row["id"] or entries[parent]["kind"] != row["kind"]):
            raise ValueError("Invalid revision lineage")
        seen = {key}
        while parent is not None:
            if parent in seen:
                raise ValueError("Cyclic revision lineage")
            seen.add(parent)
            parent = entries[parent]["supersedes"]
    return data, entries


def compose(profile_id, revision, overlays):
    data, entries = registry()
    if not isinstance(overlays, list) or any(not isinstance(key, str) for key in overlays):
        raise ValueError("Overlay references must be a list of strings")
    refs = [data["active_baseline"], *overlays]
    if len(refs) != len(set(refs)) or any(key not in entries for key in refs):
        raise ValueError("Duplicate or unknown library reference")
    if any(entries[key]["kind"] == "baseline" for key in overlays):
        raise ValueError("Only the active baseline may be selected")
    if len({entries[key]["id"] for key in refs}) != len(refs):
        raise ValueError("Select only one revision per library entry")
    profile = {"schema_version": 1, "profile_id": profile_id, "revision": revision,
               **{group: [] for group in GROUPS}}
    for key in refs:
        for group in GROUPS:
            profile[group].extend(copy.deepcopy(entries[key][group]))
    validate(profile)
    profile["library"] = {"library_id": data["library_id"],
                          "baseline": refs[0], "overlays": list(overlays),
                          "entry_sha256": {key: fingerprint(entries[key]) for key in refs}}
    return profile


def verify_profile(profile):
    """Verify selected registry rows; ad hoc additions remain proposal-only."""
    if "library" not in profile:
        return {"status": "LEGACY_PROPOSAL", "approval": "NOT_APPROVED"}
    selection = profile["library"]
    expected = compose(profile["profile_id"], profile["revision"], selection["overlays"])
    if selection != expected["library"] or profile["baseline"] != expected["baseline"]:
        raise ValueError("Library references or active baseline do not match registry")
    for group in ("overlays", "manual"):
        if any(row not in profile[group] for row in expected[group]):
            raise ValueError("Selected library requirements cannot be removed or altered")
    return {"status": "REGISTRY_MATCH", "approval": "NOT_APPROVED",
            "library": expected["library"],
            "proposal_sha256": fingerprint(profile)}
