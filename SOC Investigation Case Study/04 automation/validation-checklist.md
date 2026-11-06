# PowerShell Automation — Validation Checklist

**Status:** Proposed verification cases for the defensive SOC utilities. No execution result or performance claim is recorded here. The scripts and case data are in [this folder](README.md) and [the synthetic evidence directory](../02%20evidence/).

## Find-SuspiciousLogons.ps1

| Case | Input pattern | Expected result |
| --- | --- | --- |
| AUTH-01 | Five failures followed by a success for the same account and source within five minutes | Candidate identified |
| AUTH-02 | Fewer than the configured failure threshold | No candidate |
| AUTH-03 | Success outside configured window | No candidate |
| AUTH-04 | Failures and success from different source assets | Do not merge unrelated sessions |
| AUTH-05 | Repeated overlapping failure windows | Check that duplicate findings are not generated |
| AUTH-06 | Several distinct accounts and devices | Independent grouping and disposition |
| AUTH-07 | CSV missing required columns or invalid timestamps | Explicit failure, not silent success |

A review should also inspect whether `Group-Object Account, SourceAsset` produces the intended grouping on the PowerShell version used, and whether event ordering and window-boundary inclusivity match the stated rule.

## Collect-HostTriage.ps1

- Verify expected artifacts exist for a permitted host and valid time window.
- Run in a test environment with event-log permissions available.
- Verify behavior when Event 4688 auditing is disabled or an expected log is unavailable.
- Confirm an empty event window produces a useful result without fabricating data.
- Check output filenames, timestamps, and permission expectations.

## Export-InvestigationEvidence.ps1

- Verify the expected files are included in a package.
- Independently recalculate file hashes and compare them with the generated manifest.
- Check handling of missing inputs, existing destination paths, and a read-only output directory.
- Ensure filenames and evidence inventories are preserved consistently.

## Recording results

Record actual command lines, PowerShell version, test dataset, expected result, observed result, pass/fail and remediation notes. Do not mark any of these cases passed until executed. The scripts support an **investigation candidate**, not an automatic finding of compromise.
