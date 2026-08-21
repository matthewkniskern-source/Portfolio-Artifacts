# Lessons Learned

## Purpose

The incident was limited in scope, but it exposed several issues that would be easy to miss if the review stopped at password reset, endpoint isolation, and reimaging the laptop.

The technical response worked.

The more useful question is why a valid IT account, a legitimate shared device, and normal administrative tools were able to produce enough ambiguity to delay a confident disposition.

The lessons below focus on that problem.

---

## The Initial Alert Was Not the Failure

The original authentication alert did what it was designed to do.

Five failed logons followed by a successful authentication generated a medium-severity event for analyst review.

That was appropriate.

Making the initial rule dramatically more sensitive would probably create more noise than value. Users mistype passwords. Services retry credentials. IT staff work from different systems.

The real opportunity was in what happened after the alert.

Authentication, process, endpoint, and network activity existed across several telemetry sources, but the analyst had to assemble the sequence manually.

The better improvement is correlation, not simply more alerting.

---

## Context Changed the Meaning of the Evidence

Most of the individual activity in this incident could be explained away.

PowerShell is normal for help desk work.

whoami, ipconfig, nltest, net view, and SMB are all legitimate Windows administration tools.

TCP 443 is normal network traffic.

Even an ADMIN$ connection can be completely legitimate in the right environment.

What changed the case was the sequence.

A valid IT account authenticated from an unassigned shared laptop before normal staffing, performed rapid discovery, initiated an unusual external PowerShell connection, and then attempted access to another internal endpoint.

The individual events were weak indicators.

The progression was not.

That is the central analytical lesson from the incident.

---

## Administrative Accounts Need a Different Baseline

IT accounts are harder to evaluate using simple behavior rules because the activity that would look unusual for a normal employee may be routine for technical staff.

That does not mean administrative accounts should generate fewer detections.

It means the detections need better context.

For sarnold, useful context included:

- normal workstation
- normal working hours
- expected source subnet
- normal PowerShell use
- typical remote targets
- expected administrative tools
- whether the source device was assigned
- whether a support task existed that explained the activity

The better question was never:

Did sarnold run PowerShell?

It was:

Does this PowerShell activity, from this device, at this time, following this authentication pattern, make sense?

---

## Shared Devices Create an Attribution Problem

IT-LT-017 was a legitimate managed asset.

That helped establish that the source system itself belonged in the environment.

It did very little to establish who was actually using it.

The laptop was powered on, connected, sitting in the help desk area, and not formally checked out.

Once the account owner could not immediately be tied to the device, the asset record stopped providing meaningful attribution.

That does not automatically make the incident a physical security failure.

It does show that shared-device management is part of the security picture.

A device can be fully patched, monitored, domain joined, and protected by EDR while still creating unnecessary exposure if nobody can establish who had custody of it.

---

## Physical and Cyber Controls Intersect

The SOC telemetry established what happened on IT-LT-017.

It did not establish who physically operated it.

That line matters.

There would be little value in forcing a cyber conclusion onto evidence that cannot answer a physical-access question.

At the same time, the location of the laptop cannot simply be ignored because it sits outside the SIEM.

Badge records, help desk access, workstation locking, camera coverage, and shared-device handling may provide context that endpoint telemetry cannot.

The incident is a good example of where physical security and cybersecurity controls overlap without becoming the same investigation.

---

## Failed Lateral Movement Still Matters

The attempted access to IT-WS-031 failed.

That is a positive outcome, but it does not make the event irrelevant.

The failed authentication established that the activity had moved beyond local discovery and into an attempt to use the compromised account against another endpoint.

That materially changed the incident.

A failed action can still establish intent and scope.

The distinction should remain clear:

Lateral movement was attempted.

Lateral movement was not confirmed successful.

That is a stronger finding than either overstating the compromise or dismissing the event because access failed.

---

## The Investigation Benefited From Multiple Telemetry Sources

No single dataset carried the entire case.

Authentication telemetry established the failed-successful logon sequence.

Process telemetry established the discovery activity and PowerShell execution.

Endpoint and firewall telemetry established the unusual external connection.

Network and authentication evidence together established the attempted access to IT-WS-031.

The strongest conclusions appeared where those sources agreed.

That reinforces the value of retaining enough telemetry to correlate:

- user
- host
- process
- destination
- authentication result
- timestamp

Without those relationships, the incident would have been much easier to dismiss as unrelated noise.

---

## Automation Should Reduce Repetition, Not Hide the Investigation

Several parts of the investigation were repetitive enough to automate:

- filtering authentication events
- identifying repeated failure-success patterns
- building investigation windows
- joining processes to network connections
- exporting evidence
- generating hashes and manifests

Those are good automation targets because they save analyst time without making the incident decision for the analyst.

The scripts developed in this case deliberately stop short of declaring activity malicious.

That boundary should remain.

Automation can identify that five failures were followed by a success.

It can identify that PowerShell owned an external connection.

It can identify that the same account later attempted access to another host.

The analyst still has to decide what those facts mean together.

---

## Evidence Boundaries Matter

Several questions remained unresolved:

- how the credentials were obtained
- who physically operated IT-LT-017
- whether the device had been left unlocked
- whether earlier activity existed outside the available window
- what the external destination returned beyond the observed file
- whether the actor had attempted access elsewhere

There is a temptation during incident review to close those gaps with the explanation that seems most likely.

That does not improve the investigation.

If the evidence does not establish something, it should stay open.

A defensible incident record is more useful than a complete story built partly from assumptions.

---

## Containment Was Proportionate to the Evidence

The response isolated the confirmed affected endpoint, secured the compromised account, reviewed the secondary target, and expanded the search for related activity.

It did not treat the entire domain as compromised.

It did not automatically isolate IT-WS-031 simply because access had been attempted.

It did not classify the external connection as confirmed command-and-control without supporting evidence.

That restraint matters.

Good incident response is not only about acting quickly.

It is also about applying the right amount of response to the evidence available.

---

## Primary Lesson

The most important lesson from the incident is that common activity can become meaningful when the sequence stops making operational sense.

No single tool or event solved the case.

The useful signal came from correlation:

authentication anomaly  
→ successful access  
→ administrative discovery  
→ unusual external communication  
→ internal targeting  
→ attempted remote authentication

That is the behavior the environment should become better at recognizing.

The objective going forward is not to alert on more normal activity.

It is to identify when normal-looking activity stops being normal.
