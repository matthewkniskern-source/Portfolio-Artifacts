"""Bounded, read-only verification of SGMA v1 CI evidence archives."""
import hashlib
import io
import json
import re
import stat
import zipfile

REQUIRED = frozenset(("trivy.json", "semgrep.json", "sca.json", "gitleaks.json",
                      "gate.json", "expanded-gate.json", "review-evidence.json",
                      "unified-decision.json"))
OPTIONAL = "requirements-assessment.json"
MANIFEST = "evidence-manifest.json"
LIMIT = 20 * 1024 * 1024
SCANNERS = ("trivy-iac", "trivy-sca", "semgrep", "gitleaks")


def _pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate JSON key")
        result[key] = value
    return result


def _invalid_constant(_value):
    raise ValueError("Nonstandard JSON constant")


def _parse(data):
    return json.loads(data.decode("utf-8"), object_pairs_hook=_pairs,
                      parse_constant=_invalid_constant)


def verify_package(data):
    """Return normalized evidence, never raw scanner reports or trusted identity."""
    if not isinstance(data, bytes) or len(data) > LIMIT:
        raise ValueError("Invalid archive size")
    try:
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            entries = archive.infolist()
            names = {entry.filename for entry in entries}
            if len(names) != len(entries) or not REQUIRED | {MANIFEST} <= names:
                raise ValueError("Duplicate or missing archive members")
            if names - REQUIRED - {MANIFEST, OPTIONAL}:
                raise ValueError("Unexpected archive member")
            if sum(entry.file_size for entry in entries) > LIMIT:
                raise ValueError("Expanded archive exceeds limit")
            for entry in entries:
                if (entry.is_dir() or entry.flag_bits & 1 or
                        stat.S_IFMT(entry.external_attr >> 16) not in (0, stat.S_IFREG) or
                        entry.compress_type not in (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED)):
                    raise ValueError("Unsupported archive member")
            manifest = _parse(archive.read(MANIFEST))
            if not isinstance(manifest, dict) or manifest.get("schema_version") != 1:
                raise ValueError("Unsupported manifest")
            files = manifest.get("files")
            if not isinstance(files, dict) or set(files) != REQUIRED:
                raise ValueError("Incomplete or unexpected manifest entries")
            reports = {}
            for name in sorted(REQUIRED):
                raw = archive.read(name)
                record = files[name]
                if (not isinstance(record, dict) or type(record.get("bytes")) is not int or
                        record["bytes"] != len(raw) or
                        record.get("sha256") != hashlib.sha256(raw).hexdigest()):
                    raise ValueError("Report integrity mismatch")
                reports[name] = _parse(raw)
            for key, pattern in (("repository", r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+"),
                                 ("run_id", r"[1-9][0-9]*"), ("attempt", r"[1-9][0-9]*"),
                                 ("commit", r"[0-9a-f]{40}")):
                value = manifest.get(key)
                if not isinstance(value, str) or not re.fullmatch(pattern, value):
                    raise ValueError("Missing or invalid source identifier")
            decision = reports["unified-decision.json"]
            if not isinstance(decision, dict) or decision.get("schema_version") != 1:
                raise ValueError("Invalid unified decision")
            if decision.get("decision") not in ("PASS", "BLOCK", "EXCEPTION APPROVED", "EXCEPTION PENDING"):
                raise ValueError("Incomplete security evaluation")
            # Recompute normalized decision from manifest-covered component reports.
            from unified_gate import combine
            expected = combine(reports["gate.json"], reports["expanded-gate.json"],
                               reports["review-evidence.json"])
            if expected != decision:
                raise ValueError("Inconsistent unified decision")
            for name in ("trivy.json", "sca.json", "semgrep.json"):
                if not isinstance(reports[name], dict):
                    raise ValueError("Invalid scanner report")
            if not isinstance(reports["gitleaks.json"], list):
                raise ValueError("Invalid secret report")
            return {"integrity": "MANIFEST_MATCH", "provenance": "UNAUTHENTICATED",
                    "archive_sha256": hashlib.sha256(data).hexdigest(),
                    "source": {k: manifest[k] for k in ("repository", "run_id", "attempt", "commit")},
                    "workflow": None, "scanned": list(SCANNERS), "evidence": decision,
                    "unverified_optional_reports": [OPTIONAL] if OPTIONAL in names else [],
                    "deployment_authorized": False}
    except (zipfile.BadZipFile, RuntimeError, OSError, KeyError, TypeError,
            AttributeError, RecursionError, NotImplementedError) as exc:
        raise ValueError("Invalid evidence package") from exc
