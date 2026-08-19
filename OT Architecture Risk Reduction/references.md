# References

## Purpose

This page contains the primary authoritative sources used to support the cybersecurity guidance, control mapping, and architecture decisions in this case study.

The project relies primarily on NIST publications rather than secondary summaries so that the design rationale can be traced back to the source guidance.

---

## NIST SP 800-82 Rev. 3

**National Institute of Standards and Technology.**
*Guide to Operational Technology (OT) Security.*
NIST Special Publication 800-82, Revision 3. September 2023.

NIST SP 800-82 Rev. 3 is the primary OT-specific reference for this case study.

It provides guidance for securing operational technology while accounting for the performance, reliability, and safety requirements that distinguish OT from conventional enterprise IT.

This project uses SP 800-82 Rev. 3 primarily to support decisions involving:

* OT network segmentation
* Security boundaries
* IT/OT separation
* Remote access
* Legacy-system constraints
* Monitoring
* Compensating controls
* Operational resilience

**Official NIST publication:**
`https://csrc.nist.gov/pubs/sp/800/82/r3/final`

---

## NIST Cybersecurity Framework CSF 2.0

**National Institute of Standards and Technology.**
*The NIST Cybersecurity Framework (CSF) 2.0.*
NIST Cybersecurity White Paper 29. February 2024.

CSF 2.0 provides the higher-level cybersecurity outcomes used throughout the case study.

It is used to connect architecture decisions to broader risk-management concepts such as:

* Govern
* Identify
* Protect
* Detect
* Respond
* Recover

NIST describes CSF 2.0 as a framework for helping organizations understand, assess, prioritize, and communicate cybersecurity risk rather than prescribing one specific implementation method.

**Official NIST publication:**
`https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20`

---

## NIST SP 800-53 Rev. 5

**National Institute of Standards and Technology.**
*Security and Privacy Controls for Information Systems and Organizations.*
NIST Special Publication 800-53, Revision 5.

SP 800-53 provides the control-level traceability used selectively in the case study.

The publication provides a broad catalog of security and privacy controls that can be tailored to organizational risk and system requirements.

The case study uses selected controls primarily from areas such as:

* Access Control
* Boundary Protection
* Internal System Connections
* Mobile and External Systems
* Configuration Management
* Supply Chain Risk Management
* Contingency and Resilience

The project does not claim complete implementation of the SP 800-53 catalog.

Controls are referenced where they provide useful traceability to a specific risk finding or architecture decision.

**Official NIST publication:**
`https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final`

---

## Revision Note

NIST initiated development of **SP 800-82 Rev. 4** in January 2026.

At the time this case study was developed, Rev. 4 remained in the pre-draft stage, while **SP 800-82 Rev. 3 remained the current final published OT security guide**.

For that reason, Rev. 3 is used as the primary OT reference throughout this artifact.

---

## Use of References

These publications are used as supporting guidance rather than as a substitute for engineering judgment.

The case study follows the general relationship:

> **Operating Requirement → Risk Finding → NIST Guidance → Architecture Decision → Validation**

Where a NIST control or framework outcome is referenced, the intent is to show why the control is relevant to the identified condition.

It is not intended to imply formal certification, authorization, or full compliance with the referenced publication.
