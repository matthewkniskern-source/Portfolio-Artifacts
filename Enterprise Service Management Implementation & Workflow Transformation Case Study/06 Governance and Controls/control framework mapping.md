# Control Framework Mapping

## Purpose

This artifact maps the Enterprise Service Management control model to recognized cybersecurity and governance frameworks.

The intent is not to claim formal compliance.

The intent is to demonstrate that the controls designed throughout this case study align with established control concepts used in real enterprise environments.

The primary references are:

* **NIST Cybersecurity Framework (CSF) 2.0**
* **NIST SP 800-53 Rev. 5**

The operating principle is:

> **Frameworks should help explain why a control matters. They should not replace the operational reason the control exists.**

This artifact builds on:

* [Governance Model](./governance%20model.md)
* [RBAC and Approval Controls](./rbac%20and%20approval%20controls.md)
* [Control Matrix](./control%20matrix.md)
* [Data Governance](../05%20Data%20and%20Configuration%20Model/data%20governance.md)

---

# 1. Mapping Approach

The controls in this case study were designed from operational requirements first.

Framework alignment is applied afterward.

The traceability path is therefore:

```text
Business / Operational Need
          ↓
Requirement
          ↓
Workflow / Control
          ↓
Control Evidence
          ↓
Framework Alignment
```

This avoids designing the service-management process around control citations alone.

---

# 2. NIST CSF 2.0 Functions

The target control environment aligns broadly with the six NIST CSF 2.0 Functions:

| CSF Function | ESM Relevance                                                     |
| ------------ | ----------------------------------------------------------------- |
| Govern       | Policy, ownership, authority, risk, oversight                     |
| Identify     | Services, users, assets, CIs, vendors, dependencies               |
| Protect      | RBAC, approvals, privileged access, access lifecycle              |
| Detect       | Logging, exception reporting, SLA monitoring, control monitoring  |
| Respond      | Incident escalation, failed change response, corrective action    |
| Recover      | Backout, service restoration, remediation, post-event improvement |

The ESM platform crosses all six functions because it manages both operational activity and evidence about that activity.

---

# 3. NIST SP 800-53 Control Families

The primary NIST SP 800-53 Rev. 5 families relevant to this implementation include:

| Family                                         | Relevance                                        |
| ---------------------------------------------- | ------------------------------------------------ |
| AC — Access Control                            | RBAC, least privilege, access authorization      |
| AU — Audit and Accountability                  | Audit logging, traceability, review              |
| CA — Assessment, Authorization, and Monitoring | Control review and validation                    |
| CM — Configuration Management                  | Change control and production configuration      |
| CP — Contingency Planning                      | Recovery and backout considerations              |
| IA — Identification and Authentication         | Identity-dependent authorization                 |
| IR — Incident Response                         | Incident ownership, escalation, response         |
| MA — Maintenance                               | Vendor and technical maintenance activity        |
| PL — Planning                                  | Governance and process design                    |
| PM — Program Management                        | Governance ownership and oversight               |
| RA — Risk Assessment                           | Risk-based change and exception decisions        |
| SA — System and Services Acquisition           | Vendor and service governance                    |
| SI — System and Information Integrity          | Monitoring, failure detection, corrective action |
| SR — Supply Chain Risk Management              | Vendor dependency and external access            |

The mapping remains at the family and control-concept level unless a more specific control is useful.

---

# 4. Governance Mapping

| ESM Control Area     | NIST CSF 2.0      | SP 800-53 Family | Practical Alignment                                         |
| -------------------- | ----------------- | ---------------- | ----------------------------------------------------------- |
| Governance roles     | Govern            | PM / PL          | Defines accountability and decision authority               |
| Control ownership    | Govern            | PM / CA          | Assigns responsibility for operating and reviewing controls |
| Exception governance | Govern            | RA / PM          | Requires risk-based authorization and review                |
| Service ownership    | Govern / Identify | PM / PL          | Establishes accountability for supported services           |
| Governance review    | Govern            | CA / PM          | Validates that controls remain appropriate                  |

The governance model establishes who has authority before the platform enforces how that authority is exercised.

---

# 5. RBAC Mapping

| ESM Control                  | CSF Function     | SP 800-53 Family | Alignment                                         |
| ---------------------------- | ---------------- | ---------------- | ------------------------------------------------- |
| Role-based permissions       | Protect          | AC               | Restricts access based on assigned responsibility |
| Least privilege              | Protect          | AC               | Limits unnecessary capability                     |
| Privileged roles             | Protect          | AC               | Applies stronger controls to elevated access      |
| Sensitive-record restriction | Protect          | AC               | Limits exposure of controlled information         |
| Periodic access review       | Govern / Protect | AC / CA          | Validates continued authorization                 |
| Access revocation            | Protect          | AC               | Removes access when need ends                     |

RBAC provides the basic enforcement boundary around service-management activity.

---

# 6. Approval and Separation-of-Duty Mapping

| ESM Control                | CSF Function     | SP 800-53 Family | Alignment                                           |
| -------------------------- | ---------------- | ---------------- | --------------------------------------------------- |
| Self-approval prevention   | Protect          | AC               | Separates request and authorization                 |
| Scoped approval authority  | Govern / Protect | AC / PM          | Limits who may authorize sensitive actions          |
| Privileged-access approval | Protect          | AC               | Controls elevated access                            |
| Change approval            | Govern / Protect | CM               | Requires authorization before material modification |
| Approval history           | Detect / Govern  | AU               | Preserves evidence of authorization                 |

The approval model supports the principle that technical ability and authorization are not the same thing.

---

# 7. Audit and Accountability Mapping

| ESM Control               | CSF Function    | SP 800-53 Family | Alignment                                   |
| ------------------------- | --------------- | ---------------- | ------------------------------------------- |
| Material-action logging   | Detect          | AU               | Records significant actions                 |
| Approval history          | Detect          | AU               | Preserves authorization evidence            |
| Priority override history | Detect          | AU               | Preserves exception activity                |
| Configuration history     | Detect          | AU / CM          | Records administrative changes              |
| Audit review              | Detect / Govern | AU / CA          | Reviews recorded events for control failure |
| Automation logging        | Detect          | AU               | Preserves automated action history          |

The objective is to reconstruct meaningful actions, not simply collect logs.

---

# 8. Change Management Mapping

| ESM Control                      | CSF Function     | SP 800-53 Family | Alignment                                     |
| -------------------------------- | ---------------- | ---------------- | --------------------------------------------- |
| Risk-based change classification | Govern           | RA / CM          | Applies control based on risk                 |
| Change approval                  | Protect          | CM               | Prevents unauthorized production modification |
| Implementation readiness         | Protect          | CM               | Validates preparation before change           |
| Backout plan                     | Recover          | CM / CP          | Supports recovery from failure                |
| Post-change validation           | Detect           | CM / CA          | Confirms intended outcome                     |
| Emergency-change review          | Govern / Respond | CM / CA          | Reviews accelerated change decisions          |
| Platform configuration control   | Protect          | CM               | Controls changes to the ESM platform itself   |

Change Management is one of the clearest intersections between service-management workflow and cybersecurity governance.

---

# 9. Incident Management Mapping

| ESM Control         | CSF Function     | SP 800-53 Family | Alignment                                         |
| ------------------- | ---------------- | ---------------- | ------------------------------------------------- |
| Incident ownership  | Respond          | IR               | Establishes response accountability               |
| Priority model      | Respond          | IR               | Supports response based on business impact        |
| Escalation          | Respond          | IR               | Moves unresolved issues to appropriate authority  |
| Incident evidence   | Respond / Detect | IR / AU          | Preserves investigation history                   |
| Change correlation  | Detect / Respond | IR / CM          | Links service impact to recent changes            |
| Major Incident path | Respond          | IR               | Provides elevated response for high-impact events |

The case study is not a dedicated security-incident-response program, but the service-management process uses many of the same accountability principles.

---

# 10. Data and Asset Mapping

| ESM Control               | CSF Function       | SP 800-53 Family | Alignment                                      |
| ------------------------- | ------------------ | ---------------- | ---------------------------------------------- |
| Service inventory         | Identify           | PM / CM          | Identifies managed services                    |
| Asset relationships       | Identify           | CM               | Connects operational records to managed assets |
| CI relationships          | Identify           | CM               | Supports configuration context                 |
| Data ownership            | Govern             | PM               | Assigns accountable data owner                 |
| Controlled reference data | Protect / Identify | CM               | Maintains reliable configuration information   |
| Stale-data review         | Detect             | CA / CM          | Identifies inaccurate or outdated records      |

The objective is enough asset and configuration context to support decisions without building a CMDB larger than the organization can maintain.

---

# 11. Vendor and External Access Mapping

| ESM Control                 | CSF Function      | SP 800-53 Family | Alignment                                               |
| --------------------------- | ----------------- | ---------------- | ------------------------------------------------------- |
| Internal vendor sponsor     | Govern            | SR / SA          | Maintains internal accountability                       |
| Vendor-access approval      | Protect           | AC / SR          | Controls external access                                |
| Access expiration           | Protect           | AC               | Limits access duration                                  |
| Vendor activity record      | Detect            | AU / SR          | Preserves external activity context                     |
| Vendor dependency mapping   | Identify          | SR               | Identifies externally supported services or CIs         |
| Manual revocation exception | Respond / Protect | AC               | Provides corrective path when automation is unavailable |

Vendor governance is treated as both an access-control issue and a service-dependency issue.

---

# 12. Data Governance Mapping

| ESM Control             | CSF Function      | SP 800-53 Family | Alignment                                 |
| ----------------------- | ----------------- | ---------------- | ----------------------------------------- |
| Defined data owners     | Govern            | PM               | Establishes accountability                |
| Authoritative sources   | Identify / Govern | CM / PM          | Reduces conflicting system-of-record data |
| Reference-data control  | Protect           | CM               | Maintains consistent configuration        |
| Data-quality monitoring | Detect            | CA / SI          | Identifies integrity problems             |
| Historical preservation | Detect            | AU               | Retains operational evidence              |
| Correction workflow     | Respond           | SI               | Restores data integrity                   |

Data governance supports the reliability of every workflow and automation built on top of it.

---

# 13. Automation Mapping

| ESM Control               | CSF Function     | SP 800-53 Family | Alignment                                |
| ------------------------- | ---------------- | ---------------- | ---------------------------------------- |
| Automation rule ownership | Govern           | CM / PM          | Assigns accountability                   |
| Controlled deployment     | Protect          | CM               | Prevents untested rule changes           |
| Execution logging         | Detect           | AU               | Preserves automated action evidence      |
| Failure detection         | Detect           | SI               | Identifies automation malfunction        |
| Manual exception path     | Respond          | SI               | Restores operation when automation fails |
| Rule testing              | Govern / Protect | CA / CM          | Validates automation before production   |

Automation is treated as production configuration.

That means automation itself must be governed.

---

# 14. AI-Assisted Service Management Mapping

AI-specific controls in this case study align with existing governance concepts rather than being treated as an entirely separate control universe.

| AI Control                    | CSF Function     | SP 800-53 Concept | Alignment                                                      |
| ----------------------------- | ---------------- | ----------------- | -------------------------------------------------------------- |
| Human review                  | Govern / Protect | AC / CA           | Keeps controlled decisions under authorized human authority    |
| Restricted autonomous actions | Protect          | AC                | Prevents AI from independently exercising sensitive privileges |
| AI attribution                | Detect           | AU                | Preserves provenance                                           |
| Feedback / correction         | Respond          | SI                | Supports correction of poor recommendations                    |
| Controlled deployment         | Govern           | CM                | Treats AI configuration as managed production change           |
| Sensitive-data boundaries     | Protect          | AC                | Restricts AI exposure to controlled information                |

More detailed AI controls are maintained in:

[AI Governance](../07%20Automation%20and%20AI/ai%20governance.md)

---

# 15. Control Matrix Crosswalk

The following provides a consolidated mapping of the primary control families defined in the [Control Matrix](./control%20matrix.md).

| Internal Controls     | Primary CSF Functions                | Primary 800-53 Families |
| --------------------- | ------------------------------------ | ----------------------- |
| AC-01 through AC-10   | Govern / Protect / Detect            | AC / AU / CA            |
| WF-01 through WF-07   | Protect / Detect / Respond           | IR / AU / SI            |
| CHG-01 through CHG-08 | Govern / Protect / Detect / Recover  | CM / CA / RA / CP       |
| DG-01 through DG-07   | Govern / Identify / Detect           | PM / CM / CA / SI       |
| VND-01 through VND-05 | Govern / Identify / Protect / Detect | SR / SA / AC / AU       |
| AUT-01 through AUT-04 | Govern / Protect / Detect / Respond  | CM / AU / SI            |
| AI-01 through AI-04   | Govern / Protect / Detect / Respond  | AC / AU / CM / SI       |
| AUD-01 through AUD-04 | Detect / Respond / Govern            | AU / CA / SI            |

This is a logical alignment rather than a certification statement.

---

# 16. Example End-to-End Mapping

## Privileged Access

```text
Business Need
    ↓
Privileged Access Request
    ↓
A2 Approval
    ↓
Self-Approval Prevention
    ↓
Provisioning
    ↓
Audit Evidence
    ↓
Periodic Review
```

Framework alignment:

* **CSF:** Govern, Protect, Detect
* **SP 800-53:** AC, AU, CA

---

## Failed Production Change

```text
Change
  ↓
Risk Assessment
  ↓
Authorization
  ↓
Implementation
  ↓
Validation Failure
  ↓
Backout
  ↓
Incident
  ↓
Post-Implementation Review
```

Framework alignment:

* **CSF:** Govern, Protect, Detect, Respond, Recover
* **SP 800-53:** CM, RA, IR, CP, CA

---

## Vendor Access

```text
Vendor Need
   ↓
Internal Sponsor
   ↓
Approval
   ↓
Scoped Access
   ↓
Expiration
   ↓
Revocation
   ↓
Audit Evidence
```

Framework alignment:

* **CSF:** Govern, Identify, Protect, Detect
* **SP 800-53:** SR, AC, AU

---

# 17. Framework Mapping Guardrails

## This Is Not a Compliance Claim

The case study demonstrates alignment.

It does not establish that an organization has implemented every applicable NIST control.

---

## Framework Mapping Does Not Replace Testing

A control can map cleanly to a framework and still fail in production.

Design, testing, evidence, and monitoring remain necessary.

---

## Do Not Force Every Control Into Every Framework Category

Some controls naturally support several framework concepts.

The mapping should highlight the strongest relationship rather than create artificial coverage.

---

## Operational Purpose Comes First

A control should be present because it addresses an actual requirement or risk.

The framework reference helps explain the control.

It should not be the only reason the control exists.

---

# 18. Mapping Maintenance

Framework mapping should be reviewed when:

* significant controls are added
* governance processes change
* RBAC changes materially
* new vendor-access models are introduced
* automation scope expands
* AI-assisted capabilities are deployed
* framework guidance materially changes

The internal control ID should remain the primary implementation reference.

Framework references are supporting context.

---

# 19. Framework Mapping Success Criteria

The mapping is complete when:

* major internal control domains are represented
* relevant CSF Functions are identified
* applicable SP 800-53 families are identified
* mappings remain tied to operational controls
* no compliance claim is implied
* examples demonstrate practical alignment
* framework references remain secondary to implementation evidence

---

# 20. Control Framework Mapping Conclusion

The controls in this case study were not added to make the repository look compliant.

They were added because service-management systems make real operational decisions about:

* access
* ownership
* change
* vendors
* configuration
* exceptions
* automation

Those decisions need controls.

NIST CSF 2.0 and NIST SP 800-53 provide a useful way to show that the resulting design follows established governance, access-control, configuration-management, monitoring, incident-response, and risk-management concepts.

The important distinction is that the framework sits behind the operating model.

It does not replace it.

**Section 06 — Governance and Controls Complete**

**Next:** [Automation Opportunities](../07%20Automation%20and%20AI/automation%20opportunities.md)
