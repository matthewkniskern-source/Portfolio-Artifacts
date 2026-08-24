# AI Governance

## Purpose

This artifact defines the governance boundaries for AI-assisted capabilities within the target Enterprise Service Management environment.

AI introduces useful capabilities, but it also introduces new failure modes around:

* decision authority
* data exposure
* inaccurate recommendations
* opaque reasoning
* model change
* overreliance
* automation drift

The objective is not to block AI use.

It is to make sure AI remains inside the same accountability structure as the rest of the ESM operating model.

The operating principle is:

> **AI may assist the process. It should not quietly become the process owner.**

This artifact builds on:

* [AI Assisted Service Management](./ai%20assisted%20service%20management.md)
* [Automation Opportunities](./automation%20opportunities.md)
* [Governance Model](../06%20Governance%20and%20Controls/governance%20model.md)
* [RBAC and Approval Controls](../06%20Governance%20and%20Controls/rbac%20and%20approval%20controls.md)
* [Control Matrix](../06%20Governance%20and%20Controls/control%20matrix.md)

---

# 1. AI Governance Objectives

The governance model should ensure that:

* AI use cases have defined business purpose
* data access remains controlled
* human authority is preserved
* high-risk decisions are not delegated improperly
* AI-generated activity is attributable
* failures can be corrected
* model and configuration changes are controlled
* performance is monitored
* AI features can be disabled without breaking core service delivery

The goal is usable AI with bounded authority.

---

# 2. Governance Principles

## 2.1 AI Does Not Create Authority

An AI feature may:

* summarize
* recommend
* classify
* detect patterns
* draft content

It does not gain authority simply because its recommendation appears inside the platform.

Authority still comes from:

* role
* approval
* policy
* service ownership
* delegated responsibility

---

## 2.2 Human Accountability Remains

Every material AI-assisted outcome should remain attributable to a human role or process owner.

Example:

```text id="1avz0h"
AI Suggestion
     ↓
Human Review
     ↓
Decision
     ↓
Recorded Outcome
```

The human reviewer is responsible for the final controlled action.

---

## 2.3 AI Access Must Respect Existing Controls

AI should operate within the same access boundaries as the user or process invoking it.

It should not expose:

* restricted tickets
* privileged access details
* confidential vendor information
* internal security data
* sensitive user records

to someone who could not access that information directly.

---

## 2.4 AI Must Fail Safely

If AI is unavailable or produces an unusable result:

```text id="1q8znc"
AI Failure
   ↓
Normal Workflow
```

The core service process continues.

AI assistance should not become a hidden single point of failure.

---

## 2.5 AI Behavior Must Be Change-Controlled

Material changes to AI behavior should follow the same discipline as other production configuration.

Examples include:

* new model
* new data source
* expanded data scope
* changed prompt logic
* new autonomous capability
* changed confidence threshold

---

# 3. AI Governance Roles

| Role                   | Responsibility                            |
| ---------------------- | ----------------------------------------- |
| Executive / IT Sponsor | Approves strategic use of AI              |
| Process Owner          | Defines acceptable AI use within workflow |
| Service Owner          | Accepts service-specific AI use           |
| Security / Risk        | Defines data and control boundaries       |
| Platform Owner         | Owns technical implementation             |
| Data Owner             | Governs data used by AI                   |
| AI Feature Owner       | Owns performance and behavior             |
| Support Users          | Review and use AI outputs                 |
| Auditor / Reviewer     | Reviews control evidence and exceptions   |

One person may hold several roles in a midsize organization.

The responsibilities should still remain explicit.

---

# 4. AI Use-Case Approval

Before enabling a material AI capability, the organization should answer:

| Question                         | Decision Need          |
| -------------------------------- | ---------------------- |
| What problem is being solved?    | Business justification |
| What data will be used?          | Data boundary          |
| What can the AI do?              | Capability scope       |
| What can it not do?              | Authority boundary     |
| Who reviews the output?          | Accountability         |
| What happens when it is wrong?   | Failure handling       |
| How will usefulness be measured? | Performance            |
| How can it be disabled?          | Operational fallback   |

If these questions cannot be answered clearly, the feature is not ready for production.

---

# 5. AI Risk Classification

AI use cases should be classified by operational impact.

| Risk Level                | Example                                               |
| ------------------------- | ----------------------------------------------------- |
| Low                       | Summarization, search enhancement                     |
| Medium                    | Categorization, duplicate suggestion                  |
| High                      | Recommendations affecting access or change            |
| Prohibited Autonomous Use | Independent approval, privilege grant, control bypass |

Risk level determines:

* review strength
* testing
* monitoring
* approval
* change-control requirements

---

# 6. Low-Risk AI

Low-risk uses include:

* ticket summarization
* knowledge suggestion
* response drafting
* search improvement

Controls generally include:

* attribution
* user review
* normal RBAC
* feedback
* fallback workflow

These are the strongest early adoption candidates.

---

# 7. Medium-Risk AI

Medium-risk use cases include:

* categorization
* CI suggestion
* duplicate detection
* trend identification

Controls should include:

* human confirmation
* confidence indication where available
* correction capability
* performance monitoring
* auditability

The AI may shape the workflow.

It should not silently control it.

---

# 8. High-Risk AI

High-risk assistance includes recommendations affecting:

* privileged access
* high-impact change
* security-sensitive routing
* exception handling
* risk decisions

In these cases:

```text id="ch4vph"
AI Recommendation
      ↓
Authorized Human
      ↓
Independent Decision
```

The AI may provide context.

It should not make the final controlled decision.

---

# 9. Prohibited Autonomous Actions

The target model prohibits AI from independently:

* approving privileged access
* approving vendor access
* authorizing high-risk change
* overriding required approval
* bypassing separation of duties
* modifying audit history
* changing RBAC
* granting itself broader data access
* disabling required governance controls

These boundaries should be enforced technically where possible.

---

# 10. AI Data Access

AI features should only access data required for the approved use case.

Possible data sources include:

* ticket content
* service
* category
* CI
* knowledge
* change history
* vendor activity
* assignment history

Access should follow least privilege.

A feature designed to summarize incidents should not automatically receive unrestricted access to every data domain.

---

# 11. Retrieval and Context Boundaries

Where AI retrieves supporting records, the retrieval layer should enforce:

* user access
* role
* service scope
* sensitivity
* record status

Example:

```text id="hfyv3b"
User Query
   ↓
Access Validation
   ↓
Approved Context
   ↓
AI Response
```

The AI should not decide whether the user is allowed to see the data.

That decision belongs to the access-control layer.

---

# 12. Sensitive Data Governance

Sensitive data may include:

* personal information
* privileged credentials
* access details
* security incidents
* vendor confidential data
* internal architecture
* legal or HR information

AI use involving sensitive data should require:

* defined purpose
* approved platform capability
* access restriction
* retention understanding
* logging where appropriate

The exact requirements depend on organizational policy and the AI service architecture.

---

# 13. AI Attribution

Material AI contributions should be identifiable.

Examples:

* AI-generated summary
* AI-suggested category
* AI-drafted response
* AI-created knowledge draft
* AI-detected duplicate

Attribution may include:

* feature used
* timestamp
* user invoking it
* accepted / modified / rejected outcome

This supports both accountability and improvement.

---

# 14. AI Output Review

Human review requirements should match risk.

| Output                | Review                        |
| --------------------- | ----------------------------- |
| Summary               | Validate before relying on it |
| Draft response        | Review before send            |
| Category suggestion   | Confirm                       |
| Duplicate suggestion  | Confirm relationship          |
| Knowledge draft       | Review before publication     |
| Trend finding         | Analyst interpretation        |
| Access recommendation | Authorized decision maker     |
| Change recommendation | Change authority / owner      |

Review should be meaningful.

A required click with no realistic opportunity to assess the recommendation is not strong human oversight.

---

# 15. Confidence and Uncertainty

Where supported, AI should expose confidence or uncertainty in a usable way.

Examples:

* high-confidence match
* low-confidence classification
* several possible related incidents

The system should avoid presenting uncertain output as fact.

Where confidence is low, the workflow should favor manual review.

---

# 16. AI Error Handling

Common failure modes include:

* hallucinated information
* incorrect categorization
* false duplicate
* missing context
* outdated knowledge
* overconfident recommendation
* sensitive-data leakage
* inconsistent response

The workflow should allow:

* reject
* correct
* replace
* report
* trace

---

# 17. AI Feedback

Feedback should be captured where useful.

Examples:

```text id="0zodfh"
Recommendation
   ↓
Accepted
Modified
Rejected
```

or:

```text id="3d239a"
Knowledge Suggestion
      ↓
Helpful / Not Helpful
```

Feedback can support:

* feature evaluation
* prompt refinement
* data-quality improvement
* use-case retirement

---

# 18. AI Performance Monitoring

Useful measures include:

| Metric                         | Purpose                         |
| ------------------------------ | ------------------------------- |
| Acceptance Rate                | Measures usefulness             |
| Modification Rate              | Measures partial quality        |
| Rejection Rate                 | Identifies weak recommendations |
| Accuracy                       | Measures classification quality |
| False Duplicate Rate           | Measures correlation risk       |
| Correction Rate                | Tracks incorrect output         |
| AI Feature Availability        | Measures operational dependency |
| Sensitive-Data Exception Count | Detects governance failure      |
| Human Review Compliance        | Confirms oversight              |
| AI-Related Incident Count      | Measures adverse impact         |

Performance should be reviewed by use case.

A single aggregate AI score is not meaningful.

---

# 19. Model Drift and Behavior Change

AI behavior may change because of:

* model update
* prompt change
* new data
* changed workflow context
* changed knowledge base
* integration change

The organization should monitor whether previously acceptable behavior degrades over time.

A feature that worked well at launch is not permanently validated.

---

# 20. AI Change Control

Material AI changes should follow:

```text id="9r2cr1"
Change Requested
      ↓
Impact Review
      ↓
Test
      ↓
Approval
      ↓
Production
      ↓
Monitor
```

Change documentation should identify:

* changed capability
* affected use cases
* new data access
* expected behavior
* test results
* rollback option

---

# 21. Model or Provider Change

Changing the underlying model or provider should not be treated as a routine technical swap if it materially changes:

* data handling
* output quality
* response behavior
* retention
* access
* reliability

The use case should be revalidated.

---

# 22. Prompt and Instruction Governance

Where prompts or system instructions materially shape AI behavior, those instructions should be treated as controlled configuration.

Changes should be:

* documented
* tested
* approved
* versioned where practical

A prompt can change business behavior as effectively as a workflow rule.

---

# 23. Knowledge Grounding

Where AI uses organizational knowledge, the quality of that output depends on the source content.

Only appropriate knowledge should be used.

Stale or retired articles should not normally remain active grounding sources.

Example:

```text id="5mmjra"
Knowledge Article
      ↓
Published / Current?
   ↙             ↘
 Yes              No
 ↓                 ↓
Available        Excluded
```

AI does not solve stale knowledge.

It can amplify it.

---

# 24. AI and Data Quality

Poor structured data can produce poor AI recommendations.

Examples:

* wrong service owner
* stale CI
* incorrect category
* duplicate vendor records
* outdated knowledge

AI performance issues should therefore be investigated for both:

* model behavior
* source-data quality

---

# 25. AI Security Controls

Representative controls include:

* RBAC enforcement
* least-privilege retrieval
* sensitive-data restriction
* restricted autonomous actions
* audit attribution
* controlled configuration
* approved integration
* failure logging

Security controls around AI should reuse existing governance mechanisms wherever possible.

---

# 26. AI Audit Evidence

Representative evidence includes:

* approved use-case record
* data-scope definition
* test results
* AI feature configuration
* attribution history
* human review records
* performance reports
* error / exception records
* change history
* remediation actions

Not every AI interaction needs full audit retention.

Evidence depth should scale with risk.

---

# 27. AI Exception Governance

Material exceptions should be documented.

Examples:

* temporary expanded data access
* degraded human-review workflow
* unplanned model fallback
* incorrect AI behavior with operational impact

Exception records should include:

* issue
* scope
* owner
* risk
* compensating action
* expiration or remediation target

---

# 28. AI Incident Handling

If AI causes material operational or security impact, the event should enter the normal incident process.

Example:

```text id="ug1x3t"
AI Output
   ↓
Incorrect Controlled Action
   ↓
Operational Impact
   ↓
Incident
   ↓
Corrective Action
```

The AI feature should not sit outside normal incident accountability.

---

# 29. Disable / Rollback Capability

Material AI features should have a practical method to:

* disable
* revert
* restrict
* fall back to manual process

Example:

```text id="q9ggg9"
AI Feature Degraded
      ↓
Disable Feature
      ↓
Manual Workflow Continues
```

This is especially important during early adoption.

---

# 30. AI Third-Party Governance

Where AI capability is provided by an external vendor, governance should consider:

* data handling
* access
* availability
* contractual terms
* service dependency
* incident response
* model change
* support escalation

The AI provider becomes another service dependency.

Vendor governance still applies.

---

# 31. AI Lifecycle

Each use case should follow a defined lifecycle.

```text id="td3h1d"
Proposed
  ↓
Risk Assessed
  ↓
Approved
  ↓
Tested
  ↓
Deployed
  ↓
Monitored
  ↓
Changed / Retired
```

This prevents experimental features from quietly becoming permanent production behavior.

---

# 32. AI Use-Case Register

A simple register should identify:

| Field            | Purpose                     |
| ---------------- | --------------------------- |
| Use Case ID      | Unique reference            |
| Business Purpose | Why it exists               |
| Owner            | Accountability              |
| Risk Level       | Governance strength         |
| Data Used        | Data boundary               |
| Human Review     | Oversight                   |
| Status           | Proposed / Active / Retired |
| Metrics          | Performance                 |
| Last Review      | Governance evidence         |

The register should remain small enough to maintain.

---

# 33. Representative AI Controls

| Control ID | Control                               | Type                   |
| ---------- | ------------------------------------- | ---------------------- |
| AI-01      | Human review for controlled decisions | Preventive             |
| AI-02      | AI action attribution                 | Detective              |
| AI-03      | Restricted autonomous actions         | Preventive             |
| AI-04      | Feedback and correction               | Corrective             |
| AI-05      | AI use-case approval                  | Preventive             |
| AI-06      | Data-access boundary enforcement      | Preventive             |
| AI-07      | AI change control                     | Preventive             |
| AI-08      | AI performance monitoring             | Detective              |
| AI-09      | AI failure fallback                   | Corrective             |
| AI-10      | AI exception management               | Detective / Corrective |

These controls should be consolidated into the existing [Control Matrix](../06%20Governance%20and%20Controls/control%20matrix.md) during final repository polish.

---

# 34. Testing Mapping

Representative tests include:

| Test ID   | Scenario                                           |
| --------- | -------------------------------------------------- |
| TC-AIG-01 | AI cannot access record outside user authorization |
| TC-AIG-02 | Privileged approval remains human-controlled       |
| TC-AIG-03 | AI-generated output remains attributable           |
| TC-AIG-04 | AI recommendation can be rejected and corrected    |
| TC-AIG-05 | AI outage does not block core workflow             |
| TC-AIG-06 | Retired knowledge excluded from AI grounding       |
| TC-AIG-07 | Material prompt change follows change control      |
| TC-AIG-08 | Low-confidence output requires review              |
| TC-AIG-09 | AI feature can be disabled without service loss    |
| TC-AIG-10 | AI governance exception appears in review          |

These will be formalized in:

[Testing and UAT](../09%20Testing%20and%20UAT/test%20cases.md)

---

# 35. AI Governance Metrics

| Metric                         | Purpose                      |
| ------------------------------ | ---------------------------- |
| Approved AI Use Cases          | Measure governed scope       |
| Unapproved AI Feature Count    | Detect governance gaps       |
| Human Review Compliance        | Validate oversight           |
| AI Error Rate                  | Measure quality              |
| AI Correction Rate             | Measure remediation demand   |
| AI Exception Age               | Identify unresolved exposure |
| Sensitive-Data Violation Count | Detect access failure        |
| AI Change Failure Rate         | Measure configuration risk   |
| AI-Related Incident Count      | Measure operational impact   |
| Retired / Disabled Use Cases   | Show lifecycle management    |

Metrics should be interpreted by use case and risk level.

---

# 36. AI Governance Guardrails

## Do Not Treat AI as a New Approval Role

AI can support a decision.

It should not become the approver.

## Do Not Expand Data Access for Convenience

A better answer is not automatically worth broader access.

## Do Not Hide AI Output Inside Human Records

Material AI assistance should remain identifiable.

## Do Not Assume Vendor AI Is Governed Because It Is Embedded

A platform feature still needs internal use-case review.

## Do Not Make Core Service Delivery Dependent on AI Without a Deliberate Decision

Fallback should remain viable.

## Do Not Keep AI Because It Looks Modern

If the feature creates more review work than value, change it or remove it.

---

# 37. AI Governance Success Criteria

The AI governance model is design-ready when:

* AI use-case owners are identified
* risk levels are defined
* authority boundaries are explicit
* prohibited autonomous actions are defined
* data-access boundaries are documented
* human review expectations are defined
* attribution is supported
* performance measures are defined
* change control is defined
* fallback behavior exists
* exception handling is defined
* representative tests exist

---

# 38. AI Governance Conclusion

AI can make the service-management environment better without becoming another uncontrolled layer of complexity.

The useful boundary is straightforward.

Let AI help people:

* find
* summarize
* categorize
* correlate
* draft
* analyze

Keep people accountable for:

* approval
* access
* risk
* exception
* change authority
* final controlled action

That preserves the value of AI without confusing recommendation with authority.

The target model does not assume AI is always right.

It assumes AI can be useful when the organization knows where its authority ends.

**Next:** [Implementation Plan](../08%20Implementation%20Plan/implementation%20plan.md)
