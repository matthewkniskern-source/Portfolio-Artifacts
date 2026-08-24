# Test Cases

## Purpose

This artifact defines representative validation scenarios for the target Enterprise Service Management environment.

The test set is designed to prove that:

* core workflows function
* controls operate
* exceptions remain visible
* ownership is preserved
* requirements are testable
* the implementation behaves predictably under both normal and failure conditions

The detailed execution evidence would be captured during implementation.

This artifact defines the test intent.

It builds on:

* [Test Strategy](./test%20strategy.md)
* [Requirements Traceability Matrix](../02%20Requirements%20Discovery/requirements%20traceability%20matrix.md)
* [Control Matrix](../06%20Governance%20and%20Controls/control%20matrix.md)
* [Phase Exit Criteria](../08%20Implementation%20Plan/phase%20exit%20criteria.md)

---

# 1. Test Case Format

Each test case uses the following structure:

| Field                 | Purpose            |
| --------------------- | ------------------ |
| Test ID               | Unique reference   |
| Scenario              | Business condition |
| Requirement / Control | Traceability       |
| Preconditions         | Required setup     |
| Expected Result       | Intended outcome   |
| Priority              | Test importance    |

Formal execution may additionally capture:

* actual result
* pass / fail
* evidence
* defect ID
* tester
* execution date

---

# 2. Incident Management Tests

| Test ID   | Scenario                    | Requirement / Control | Preconditions                  | Expected Result                                                         | Priority |
| --------- | --------------------------- | --------------------- | ------------------------------ | ----------------------------------------------------------------------- | -------- |
| TC-INC-01 | Create standard incident    | BR-01, BR-02          | Active user and service        | Incident created with unique record and valid owner                     | High     |
| TC-INC-02 | Identify duplicate incident | BR-14 / WF-06         | Existing related incident      | Technician can link or mark duplicate while preserving history          | Medium   |
| TC-INC-03 | Calculate P1 priority       | BR-03 / FR-05, FR-06  | Impact High, Urgency High      | Priority automatically calculates as P1                                 | Critical |
| TC-INC-04 | Reassign incident           | BR-04 / WF-02         | Active support groups          | Reassignment requires valid destination and retains history/reason      | High     |
| TC-INC-05 | Vendor-dependent incident   | BR-11 / VND-01        | Active vendor relationship     | Internal support group remains owner while vendor dependency is tracked | High     |
| TC-INC-06 | Waiting on requester        | BR-05                 | User information required      | Ticket enters valid waiting state and retains owner                     | Medium   |
| TC-INC-07 | Reopen resolved incident    | BR-13                 | Incident resolved              | Authorized reopen returns record to active workflow                     | Medium   |
| TC-INC-08 | Failed change correlation   | BR-10 / CHG-05        | Incident follows recent change | Incident can be linked to relevant change from both records             | High     |

---

# 3. SLA Tests

| Test ID   | Scenario                | Requirement / Control | Preconditions                    | Expected Result                                                        | Priority |
| --------- | ----------------------- | --------------------- | -------------------------------- | ---------------------------------------------------------------------- | -------- |
| TC-SLA-01 | Approved SLA pause      | BR-05 / WF-05         | Ticket in approved waiting state | SLA pauses and resumes according to defined policy                     | High     |
| TC-SLA-02 | SLA breach escalation   | BR-05 / WF-03         | Active SLA near breach           | Warning and escalation occur at defined thresholds                     | Critical |
| TC-SLA-03 | Invalid pause attempt   | AC-08                 | User lacks exception authority   | SLA cannot be manually excluded without authorized reason              | High     |
| TC-SLA-04 | Resolution stops timer  | BR-05                 | Ticket validly resolved          | SLA stops according to configured rule                                 | Medium   |
| TC-SLA-05 | Waiting vendor handling | BR-11                 | Vendor dependency active         | SLA behavior follows defined policy and vendor wait remains reportable | High     |

---

# 4. Service Request Tests

| Test ID   | Scenario                       | Requirement / Control | Preconditions                              | Expected Result                                                       | Priority |
| --------- | ------------------------------ | --------------------- | ------------------------------------------ | --------------------------------------------------------------------- | -------- |
| TC-REQ-01 | A0 request                     | BR-02                 | Low-risk catalog item                      | Request routes directly to fulfillment without manual approval        | Medium   |
| TC-REQ-02 | Hardware request               | BR-06                 | Catalog item requires approval             | Correct approver receives request before fulfillment                  | High     |
| TC-REQ-03 | Prohibited self-approval       | BR-07 / AC-02         | Requester also has approver role           | Self-approval blocked and attempt remains auditable                   | Critical |
| TC-REQ-04 | Rejected request               | BR-06                 | Authorized approver rejects                | Request enters Rejected state with reason and requester notification  | High     |
| TC-REQ-05 | Approval aging                 | BR-06                 | Approval remains unanswered                | Reminder and escalation occur according to rule                       | Medium   |
| TC-REQ-06 | Multi-task fulfillment         | BR-04                 | Request requires several fulfillment tasks | Child tasks created and parent retains overall accountability         | High     |
| TC-REQ-07 | Missing information            | BR-02                 | Required requester data absent             | Request moves to Waiting on Requester rather than invalid fulfillment | Medium   |
| TC-REQ-08 | Request exceeds standard scope | BR-04                 | Work no longer fits catalog item           | Request routes to appropriate Change / Project / Enhancement process  | Medium   |

---

# 5. Change Management Tests

| Test ID   | Scenario                       | Requirement / Control | Preconditions                                | Expected Result                                              | Priority |
| --------- | ------------------------------ | --------------------- | -------------------------------------------- | ------------------------------------------------------------ | -------- |
| TC-CHG-01 | Standard Change                | BR-10 / CHG-07        | Approved Standard Change template            | Change follows pre-authorized pattern                        | Medium   |
| TC-CHG-02 | Normal Change approval         | BR-10 / CHG-01        | Medium-risk change                           | Required approval occurs before scheduling                   | Critical |
| TC-CHG-03 | High-risk approval bypass      | CHG-01                | High-risk change, unauthorized user          | Implementation cannot proceed without required approval      | Critical |
| TC-CHG-04 | Readiness failure              | CHG-02                | Required readiness item missing              | Change cannot proceed to implementation                      | High     |
| TC-CHG-05 | Failed implementation          | CHG-03                | Change validation fails                      | Backout or recovery path activates                           | Critical |
| TC-CHG-06 | Change causes incident         | CHG-05                | Failed change creates service disruption     | Incident and change remain linked                            | High     |
| TC-CHG-07 | Emergency Change               | CHG-06                | Valid emergency condition                    | Expedited approval allowed and retrospective review required | High     |
| TC-CHG-08 | Standard Change scope exceeded | CHG-07                | Proposed work outside template               | Change converts or routes to Normal Change                   | High     |
| TC-CHG-09 | Vendor-implemented change      | BR-11                 | Vendor performs technical work               | Internal Change Owner remains accountable                    | Medium   |
| TC-CHG-10 | Closure without validation     | CHG-04                | Implementation completed, validation missing | Change cannot close as successful                            | Critical |

---

# 6. Knowledge Management Tests

| Test ID   | Scenario                     | Requirement / Control | Preconditions                         | Expected Result                                | Priority |
| --------- | ---------------------------- | --------------------- | ------------------------------------- | ---------------------------------------------- | -------- |
| TC-KNW-01 | Publish valid article        | BR-09                 | Draft article and authorized reviewer | Article progresses through review to Published | Medium   |
| TC-KNW-02 | Restricted technical article | BR-09                 | Restricted audience configured        | Unauthorized users cannot view article         | High     |
| TC-KNW-03 | Link knowledge to incident   | FR-18                 | Active incident and published article | Article relationship retained on incident      | Medium   |
| TC-KNW-04 | Stale article flag           | BR-09                 | Review date exceeded                  | Article enters review or exception process     | Medium   |
| TC-KNW-05 | Retire article               | BR-09                 | Obsolete content                      | Article no longer appears as active guidance   | Medium   |
| TC-KNW-06 | Publish without approval     | FR-19                 | Draft article, no review              | Publication blocked                            | High     |

---

# 7. RBAC and Approval Tests

| Test ID    | Scenario                         | Requirement / Control | Preconditions                       | Expected Result                                         | Priority |
| ---------- | -------------------------------- | --------------------- | ----------------------------------- | ------------------------------------------------------- | -------- |
| TC-RBAC-01 | Restricted ticket access         | NFR-02 / AC-01        | User outside authorized scope       | Access denied                                           | Critical |
| TC-RBAC-02 | Service Desk permissions         | AC-01                 | Service Desk role                   | User can operate tickets but cannot administer workflow | High     |
| TC-RBAC-03 | Specialist scope                 | AC-01                 | Specialist role                     | User sees only authorized operational scope             | High     |
| TC-RBAC-04 | Unauthorized privileged approval | AC-03                 | User lacks approval authority       | Approval action denied                                  | Critical |
| TC-RBAC-05 | Self-approval                    | AC-02                 | Requester equals approver           | Approval blocked and logged                             | Critical |
| TC-RBAC-06 | Delegated approval expiration    | AC-01                 | Time-bound delegate exists          | Delegated authority ends automatically                  | High     |
| TC-RBAC-07 | Material request change          | AC-05                 | Approved request changes materially | Reapproval required                                     | High     |
| TC-RBAC-08 | Vendor restricted access         | AC-01                 | Vendor user                         | Vendor cannot view unrelated internal records           | Critical |
| TC-RBAC-09 | Privileged role review           | AC-06                 | Admin role assigned                 | Role appears in periodic access review                  | High     |
| TC-RBAC-10 | User termination                 | AC-10                 | User becomes inactive               | Privileged platform access revoked                      | Critical |

---

# 8. Vendor Access Tests

| Test ID   | Scenario                 | Requirement / Control | Preconditions               | Expected Result                                                          | Priority |
| --------- | ------------------------ | --------------------- | --------------------------- | ------------------------------------------------------------------------ | -------- |
| TC-VND-01 | Vendor request approval  | BR-12 / VND-02        | Active vendor and sponsor   | Access requires approved authorization path                              | Critical |
| TC-VND-02 | Vendor access expiration | BR-12 / VND-03        | Temporary access granted    | Access disables or generates controlled disablement action at expiration | Critical |
| TC-VND-03 | Vendor access extension  | BR-12                 | Access near expiration      | Extension requires new authorization                                     | High     |
| TC-VND-04 | Inactive vendor          | DG-03                 | Vendor record inactive      | New vendor access request blocked                                        | High     |
| TC-VND-05 | Vendor activity tracking | BR-11 / VND-05        | Vendor handling active case | Vendor activity remains linked to internal record and owner              | Medium   |

---

# 9. Data and Relationship Tests

| Test ID   | Scenario                            | Requirement / Control | Preconditions               | Expected Result                                          | Priority |
| --------- | ----------------------------------- | --------------------- | --------------------------- | -------------------------------------------------------- | -------- |
| TC-DAT-01 | Incident service and CI             | BR-08                 | Valid service and CI        | Relationships retained and reportable                    | High     |
| TC-DAT-02 | Inactive support group              | DG-03                 | Group inactive              | New assignment blocked or exception generated            | Critical |
| TC-DAT-03 | Multiple affected CIs               | BR-08                 | Valid change                | Multiple CI relationships supported                      | Medium   |
| TC-DAT-04 | Ticket-to-change relationship       | BR-10                 | Existing ticket and change  | Relationship visible from both records                   | High     |
| TC-DAT-05 | Vendor with internal owner          | BR-11                 | Vendor dependency           | Internal accountability remains structurally represented | High     |
| TC-DAT-06 | Approval parent relationship        | BR-06                 | Approval created            | Approval cannot exist without parent transaction         | High     |
| TC-DAT-07 | Knowledge-to-incident               | BR-09                 | Valid article and incident  | Relationship retained                                    | Medium   |
| TC-DAT-08 | Temporary access without expiration | BR-12                 | Temporary request submitted | Request cannot proceed without expiration                | Critical |
| TC-DAT-09 | Knowledge without owner             | DG-01                 | Draft article               | Publication blocked until owner assigned                 | High     |

---

# 10. Data Governance Tests

| Test ID  | Scenario                | Requirement / Control | Preconditions                     | Expected Result                                      | Priority |
| -------- | ----------------------- | --------------------- | --------------------------------- | ---------------------------------------------------- | -------- |
| TC-DG-01 | Service without owner   | DG-01                 | Active service record             | Governance exception generated or activation blocked | High     |
| TC-DG-02 | Invalid reference value | DG-02                 | Inactive value exists             | Invalid value unavailable for new transaction        | High     |
| TC-DG-03 | Knowledge review date   | DG-04                 | Published article                 | Required review date maintained                      | Medium   |
| TC-DG-04 | Expired vendor record   | DG-03                 | Vendor inactive                   | New dependency/access association blocked            | High     |
| TC-DG-05 | Retired CI history      | DG-05                 | Retired CI linked to old incident | Historical relationship remains visible              | Medium   |
| TC-DG-06 | Data-quality reporting  | DG-06                 | Known quality exception exists    | Exception appears in governance reporting            | High     |
| TC-DG-07 | Approval rule update    | DG-05                 | Historical approval exists        | Rule changes do not rewrite historical evidence      | Critical |

---

# 11. Automation Tests

| Test ID   | Scenario                  | Requirement / Control | Preconditions                        | Expected Result                                  | Priority |
| --------- | ------------------------- | --------------------- | ------------------------------------ | ------------------------------------------------ | -------- |
| TC-AUT-01 | Automatic routing         | BR-04 / AUT-01        | Valid service ownership              | Ticket routes to correct support group           | High     |
| TC-AUT-02 | Routing failure           | AUT-03                | Service has no valid group           | Exception created and assigned for manual triage | Critical |
| TC-AUT-03 | SLA warning               | BR-05                 | SLA reaches warning threshold        | Notification / escalation triggers               | High     |
| TC-AUT-04 | Approval reminder         | BR-06                 | Approval aging threshold reached     | Reminder sent correctly                          | Medium   |
| TC-AUT-05 | Fulfillment task creation | BR-02                 | Approved repeatable request          | Required tasks created                           | High     |
| TC-AUT-06 | Integration failure       | AUT-03                | Downstream fulfillment unavailable   | Manual fulfillment task created                  | Critical |
| TC-AUT-07 | Access expiration         | VND-03                | Temporary access active              | Disablement or controlled exception occurs       | Critical |
| TC-AUT-08 | Approval bypass attempt   | AUT-04 / AC-02        | Automation reaches controlled action | Required approval cannot be skipped              | Critical |
| TC-AUT-09 | Execution logging         | AUT-02                | Automation performs material action  | Execution remains auditable                      | High     |
| TC-AUT-10 | Unsafe input              | AUT-01                | Required data invalid or absent      | Automation stops safely                          | Critical |

---

# 12. Governance and Control Tests

| Test ID   | Scenario                                 | Requirement / Control | Preconditions                      | Expected Result                                      | Priority |
| --------- | ---------------------------------------- | --------------------- | ---------------------------------- | ---------------------------------------------------- | -------- |
| TC-GOV-01 | Unauthorized privileged request approval | AC-03                 | User lacks authority               | Action denied                                        | Critical |
| TC-GOV-02 | Controlled self-approval                 | AC-02                 | Requester also approver            | Action blocked                                       | Critical |
| TC-GOV-03 | Failed automatic vendor revocation       | VND-04                | Revocation integration unavailable | Manual disablement task created and owned            | Critical |
| TC-GOV-04 | SLA exception                            | AC-08                 | User requests exception            | Authorized reason and role required                  | High     |
| TC-GOV-05 | Priority override                        | AC-07                 | Authorized override performed      | Old/new value, reason, actor retained                | High     |
| TC-GOV-06 | Closure data missing                     | WF-04                 | Required closure field absent      | Closure blocked                                      | High     |
| TC-GOV-07 | Production workflow change               | CHG-08                | Config change requested            | Controlled change process and audit history required | Critical |
| TC-GOV-08 | Automation failure                       | AUT-03                | Rule fails                         | Visible assigned exception created                   | Critical |
| TC-GOV-09 | Sensitive record                         | AC-01                 | Unauthorized role                  | Record access denied                                 | Critical |
| TC-GOV-10 | Expired governance exception             | AUD-04                | Exception past review date         | Appears in governance review / escalation            | High     |

---

# 13. AI-Assisted Service Management Tests

| Test ID  | Scenario                    | Requirement / Control | Preconditions                       | Expected Result                                             | Priority |
| -------- | --------------------------- | --------------------- | ----------------------------------- | ----------------------------------------------------------- | -------- |
| TC-AI-01 | Suggested category          | BR-17 / AI-01         | AI feature active                   | Human retains final category decision                       | Medium   |
| TC-AI-02 | AI attribution              | AI-02                 | AI generates material content       | AI contribution remains identifiable                        | High     |
| TC-AI-03 | Privileged approval         | AI-03                 | AI available during access workflow | AI cannot independently approve request                     | Critical |
| TC-AI-04 | Incorrect recommendation    | AI-04                 | User rejects AI output              | Recommendation can be corrected without workflow disruption | Medium   |
| TC-AI-05 | Restricted record retrieval | AI-06                 | User lacks source-record access     | AI cannot expose restricted information                     | Critical |
| TC-AI-06 | Duplicate suggestion        | AI-01                 | Similar incidents exist             | Technician confirmation required before duplicate linkage   | High     |
| TC-AI-07 | Knowledge draft             | AI-01                 | AI creates draft                    | Draft cannot auto-publish                                   | High     |
| TC-AI-08 | AI outage                   | AI-09                 | AI service unavailable              | Core ticket workflow continues                              | Critical |
| TC-AI-09 | Low-confidence routing      | AI-01                 | Weak classification confidence      | Manual confirmation required                                | High     |
| TC-AI-10 | AI configuration change     | AI-07                 | Material model/prompt change        | Controlled change process required                          | High     |

---

# 14. Migration and Cutover Tests

| Test ID   | Scenario                  | Requirement / Control         | Preconditions            | Expected Result                                             | Priority |
| --------- | ------------------------- | ----------------------------- | ------------------------ | ----------------------------------------------------------- | -------- |
| TC-MIG-01 | Active user migration     | Data migration scope approved | Source user active       | User loads correctly with intended role data                | High     |
| TC-MIG-02 | Inactive user exclusion   | Data migration scope approved | Source user inactive     | User excluded from active role population                   | High     |
| TC-MIG-03 | Support-group mapping     | Target groups defined         | Legacy group mapped      | Record routes to valid target group                         | Critical |
| TC-MIG-04 | Active ticket migration   | Active record selected        | Source record valid      | Ownership, status, and legacy reference preserved           | Critical |
| TC-MIG-05 | Historical ticket archive | Archive decision approved     | Closed historical record | Record remains retrievable without entering active workflow | Medium   |
| TC-MIG-06 | Knowledge cleanup         | Legacy knowledge available    | Obsolete article present | Article excluded or retired                                 | Medium   |
| TC-MIG-07 | Approval mapping          | Active approvers identified   | Invalid approver exists  | Invalid mapping flagged before go-live                      | Critical |
| TC-MIG-08 | Migration reconciliation  | Test load complete            | Expected counts known    | Loaded records reconcile or documented exceptions exist     | Critical |
| TC-CUT-01 | Production smoke test     | Cutover complete              | Production enabled       | Core incident flow operates end to end                      | Critical |
| TC-CUT-02 | Legacy intake redirect    | New intake enabled            | Legacy channel active    | Users are redirected or records enter managed workflow      | High     |

---

# 15. Reporting Tests

| Test ID   | Scenario                 | Requirement / Control | Preconditions                  | Expected Result                              | Priority |
| --------- | ------------------------ | --------------------- | ------------------------------ | -------------------------------------------- | -------- |
| TC-RPT-01 | SLA dashboard            | BR-15                 | Known ticket sample            | Dashboard values reconcile to source records | High     |
| TC-RPT-02 | Reassignment metric      | BR-15                 | Known reassignment history     | Report counts expected transitions           | Medium   |
| TC-RPT-03 | Failed change report     | BR-10                 | Known failed change            | Failed outcome appears correctly             | High     |
| TC-RPT-04 | Vendor dependency report | BR-11                 | Known vendor-dependent records | Report identifies affected records/services  | Medium   |
| TC-RPT-05 | Approval aging report    | BR-06                 | Known pending approvals        | Aging reflects actual approval timestamps    | High     |
| TC-RPT-06 | Data-quality exceptions  | DG-06                 | Known invalid reference        | Exception appears in report                  | High     |

---

# 16. Priority 1 Go-Live Test Set

The following tests should be treated as minimum critical validation before go-live:

| Test ID    | Critical Behavior                      |
| ---------- | -------------------------------------- |
| TC-INC-03  | P1 priority calculation                |
| TC-SLA-02  | SLA escalation                         |
| TC-REQ-03  | Self-approval prevention               |
| TC-CHG-03  | High-risk approval enforcement         |
| TC-CHG-05  | Failed-change recovery                 |
| TC-CHG-10  | Change validation requirement          |
| TC-RBAC-01 | Restricted record access               |
| TC-RBAC-04 | Privileged approval restriction        |
| TC-RBAC-05 | Self-approval block                    |
| TC-RBAC-08 | Vendor access boundary                 |
| TC-RBAC-10 | Access revocation                      |
| TC-VND-02  | Vendor access expiration               |
| TC-DAT-02  | Inactive-group restriction             |
| TC-DAT-08  | Temporary access expiration required   |
| TC-AUT-02  | Automation failure visibility          |
| TC-AUT-08  | Automation cannot bypass approval      |
| TC-GOV-07  | Production configuration control       |
| TC-AI-03   | AI cannot approve privileged access    |
| TC-AI-05   | AI respects data boundary              |
| TC-AI-08   | AI outage does not block core workflow |
| TC-MIG-04  | Active-ticket continuity               |
| TC-MIG-08  | Migration reconciliation               |
| TC-CUT-01  | Production smoke test                  |

Failure of one of these should receive direct go-live review.

---

# 17. Negative Test Set

The implementation should deliberately attempt prohibited actions.

Representative negative tests include:

| Test       | Prohibited Condition                          |
| ---------- | --------------------------------------------- |
| TC-REQ-03  | Requester self-approves                       |
| TC-CHG-03  | High-risk change bypasses approval            |
| TC-KNW-06  | Draft knowledge publishes without review      |
| TC-RBAC-01 | Unauthorized record access                    |
| TC-RBAC-04 | Unauthorized privileged approval              |
| TC-RBAC-08 | Vendor views unrelated record                 |
| TC-DAT-02  | Ticket assigned to inactive group             |
| TC-DAT-08  | Temporary access submitted without expiration |
| TC-AUT-08  | Automation skips approval                     |
| TC-AI-03   | AI approves sensitive action                  |
| TC-AI-05   | AI exposes restricted information             |

The expected result is not merely a failed action.

Where appropriate, the attempt should also generate evidence.

---

# 18. Test Execution Status

Formal execution may use:

| Status           | Meaning                                              |
| ---------------- | ---------------------------------------------------- |
| Not Run          | Awaiting execution                                   |
| Pass             | Expected behavior confirmed                          |
| Fail             | Expected behavior not achieved                       |
| Blocked          | Dependency prevents execution                        |
| Conditional Pass | Primary objective achieved with accepted minor issue |

Critical control failures should not receive Conditional Pass solely to improve the overall pass rate.

---

# 19. Defect Linkage

Where a test fails:

```text id="815udp"
Test Case
   ↓
Failed
   ↓
Defect
   ↓
Correction
   ↓
Retest
```

The test ID should remain linked to the defect until:

* correction passes retest
* or the remaining risk is formally accepted

---

# 20. Test Case Success Criteria

The test catalog is sufficient when:

* each core workflow has positive coverage
* critical controls have negative coverage
* exception paths are represented
* data relationships are tested
* automation failure behavior is tested
* AI boundaries are tested
* migration and cutover are represented
* critical go-live scenarios are identifiable
* requirements and controls can be traced to validation

---

# 21. Test Cases Conclusion

The purpose of this test set is not to prove that every feature in the platform works.

It is to prove that the service-management model behaves correctly where the organization actually depends on it.

That means testing:

* the expected path
* the failure path
* the unauthorized path
* the recovery path

A strong implementation should be able to show not only that users can perform the right action, but that the system responds correctly when someone tries to perform the wrong one.

**Next:** [UAT Plan](./uat%20plan.md)
