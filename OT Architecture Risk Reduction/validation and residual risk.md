# Validation and Residual Risk

## Purpose

The target architecture only matters if it works the way it is supposed to.

That means proving two things:

1. **The security controls actually reduce the intended exposure**
2. **The plant still operates correctly after those controls are introduced**

A firewall rule that blocks traffic is not automatically a good control.

If it also breaks operator visibility, stops a required BACnet path, interferes with maintenance, or removes a known fallback operating mode, then the design has created a different problem.

Validation in this case study therefore treats cybersecurity behavior and plant behavior as equally important.

Supporting analysis is available in:

* [Legacy Risk Findings](legacy%20risk%20findings.md)
* [NIST Alignment](nist%20alignment.md)
* [Target Architecture](target%20architecture.md)
* [Risk Reduction Mapping](risk%20reduction%20mapping.md)

---

# Validation Approach

The target state should be tested against the requirements that drove the redesign in the first place.

For each major control, the basic question is:

> **Did we remove access that was not required without breaking access that was?**

That sounds simple, but it is the line that matters.

The validation effort should confirm:

* Intended communication still works
* Unnecessary communication does not
* Privilege matches the role
* Remote access follows the approved path
* Legacy devices remain operational
* Monitoring sees what it is supposed to see
* Operators still have a way to run the plant when higher-level systems are unavailable

---

# 1. Network Segmentation

## What We Are Testing

The target architecture separates:

* Enterprise
* OT DMZ
* Supervisory systems
* Engineering / administrative systems
* Control systems
* Legacy field-network gateways

The point is not to build more zones for the sake of having more zones.

The point is to make sure systems with different jobs and privilege levels do not automatically inherit access to one another.

## Validation

Confirm that:

* Enterprise endpoints cannot directly reach PLCs
* Enterprise endpoints cannot directly reach MS/TP gateways
* Management workstations cannot reach process-control functions
* Operator systems can communicate with the supervisory services they need
* Supervisory systems can reach required control functions
* Engineering systems can reach only approved controller and infrastructure destinations
* DMZ systems cannot communicate arbitrarily into OT
* Unapproved inter-zone traffic is denied

## Expected Result

The plant keeps the communications required for normal operation, while the broad internal reachability present in the legacy environment is gone.

---

# 2. Management Access

## What We Are Testing

Management still needs plant visibility.

Management does not need to become another operator station.

## Validation

Confirm that the management role can:

* View plant status
* Review selected alarms
* See equipment condition
* Review performance information
* Access approved historical data

Confirm that the management role cannot:

* Start or stop equipment
* Change process setpoints
* Modify sequencing
* Perform engineering functions
* Reach controllers directly

## Expected Result

The manager still gets the information needed to manage.

The ability to interfere with plant operation is removed unless a separate operational requirement can actually justify it.

---

# 3. Vendor Remote Access

## What We Are Testing

All remote vendor access should use the target-state path.

The old VPN should be gone.

## Validation

Confirm that:

* The historical vendor VPN has been disabled or removed
* Vendors authenticate through the approved remote-access service
* Remote sessions terminate in the OT DMZ
* Vendors pass through the jump host before reaching OT assets
* Access is limited to approved destinations
* Sessions are logged
* Authentication events are visible
* Access can be disabled when the work is complete
* Old credentials no longer provide an alternate path

## Expected Result

There is one recognized remote-support model.

A vendor should not have a second route into the plant simply because somebody forgot it existed.

---

# 4. Engineering Access

## What We Are Testing

The engineering workstation still needs to be powerful.

What it no longer needs is unlimited reach.

## Validation

Confirm that the workstation can reach:

* Approved PLCs
* Required BACnet controllers
* Approved network or infrastructure systems
* Recovery and configuration resources

Confirm that it cannot reach unrelated systems with no engineering requirement.

Where practical, engineering activity should also be attributable to an authorized user or maintenance event.

## Expected Result

The engineering function remains intact, but a compromised engineering workstation has fewer places to go.

That is the control objective.

---

# 5. Historian and Data Flow

## What We Are Testing

Operations should keep a useful local historian.

Enterprise users should get the data they need without reaching into the plant network.

## Validation

Confirm that:

* The OT historian or collector receives required process data
* Operators and engineering personnel retain access to operational history
* Approved datasets replicate to the DMZ reporting service
* Enterprise users query the DMZ service rather than the OT historian
* Replication follows the intended direction and approved services
* Failure of the enterprise reporting service does not affect plant control
* Failure of the replication path does not stop local historical collection

## Expected Result

Operations keeps its historian.

The business gets its data.

Neither requirement has to borrow the other one's trust.

---

# 6. Legacy MS/TP Containment

## What We Are Testing

The MS/TP devices still have to feed the plant logic.

The target state is supposed to reduce exposure around them, not break them.

## Validation

Confirm that:

* BACnet/IP-to-MS/TP gateways communicate with the controllers that actually need them
* Enterprise systems cannot directly reach the gateways
* General remote vendor access cannot directly reach the field networks
* Required differential-pressure values still reach the control logic
* Required RTD values still reach the control logic
* Flow, status, and permissive information remains available
* A trunk failure generates the expected alarms or degraded behavior
* Restoration returns the system to normal operation

## Expected Result

The legacy field networks keep doing their job.

They simply stop being easier to reach than they need to be.

---

# 7. Passive Monitoring and Anomaly Detection

## What We Are Testing

The monitoring layer should improve visibility without becoming another source of traffic or instability.

In OT, that distinction matters.

## Validation

Confirm visibility into:

* New BACnet devices
* Unexpected communication pairs
* Unusual protocol activity
* Abnormal traffic volume
* Unexpected gateway behavior
* Remote-access events
* Administrative activity
* Significant deviations in process values

Controlled test conditions can be used where safe and appropriate, such as:

* An unauthorized test endpoint attempting communication
* A known rejected connection attempt
* A planned maintenance event
* A controlled process change within safe operating limits

The monitoring should also be compared against actual plant conditions.

A strange data point is not automatically a cyber event.

It may be:

* A failed sensor
* Instrument drift
* Calibration error
* Maintenance activity
* A process upset
* A perfectly legitimate operating transition

## Expected Result

The monitoring layer improves situational awareness without interfering with normal control traffic.

Security personnel gain better visibility, but operator and controls knowledge remains part of the interpretation.

---

# 8. Maintenance Access

## What We Are Testing

Maintenance still has to work.

That includes direct service-port access where the equipment requires it.

## Validation

Confirm that:

* Company maintenance laptops can reach approved service interfaces
* Vendor laptops can connect during approved service activity
* Those connections do not automatically expose the broader OT network
* Access is limited to the equipment being serviced
* Temporary vendor access is removed when the task is complete
* Maintenance activity is documented where appropriate

## Expected Result

Technicians can still troubleshoot and recover equipment.

The maintenance path stays a maintenance path instead of becoming a general-purpose OT connection.

---

# 9. Local and Degraded Operation

## What We Are Testing

The target architecture must not remove the plant's ability to operate when SCADA/BAS is unavailable.

This is one of the most important operational checks in the entire redesign.

## Validation

Where safe and authorized, confirm that:

* PLCs continue executing appropriate local logic
* Local equipment controls remain available
* The central physical control board remains usable
* Operators can run a reduced but coordinated plant configuration
* Manual/local operation does not depend on enterprise systems
* Restoring supervisory control does not introduce unexpected process behavior

## Expected Result

Loss of supervisory capability is still a serious event.

It is not automatically a total loss of the plant.

That distinction should survive the cybersecurity redesign.

---

# 10. Governance and Ownership

## What We Are Testing

The target state is supposed to eliminate the kind of ownership ambiguity that allows old accounts, VPNs, firewall rules, and access paths to survive indefinitely.

## Validation

Confirm that somebody is clearly accountable for:

* OT network boundaries
* Firewall policy
* Controller administration
* Engineering workstation administration
* Vendor access approval
* Account lifecycle
* Asset inventory
* Monitoring
* Backup and recovery
* Configuration management
* Incident coordination
* System retirement

Legacy access paths discovered during assessment should also have a documented disposition:

* Keep and govern
* Replace
* Disable
* Remove

## Expected Result

The environment no longer depends on institutional memory to explain who owns a critical connection or security decision.

Shared responsibility is fine.

Undefined responsibility is not.

---

# Validation Evidence

A real implementation should retain enough evidence to show that the controls were actually tested.

That may include:

* Updated network diagrams
* Firewall-rule reviews
* Access-control test results
* Authentication logs
* Remote-access logs
* Monitoring alerts
* Historian replication tests
* Backup and recovery records
* Maintenance records
* Configuration baselines
* Asset inventories
* Change records
* Operator acceptance testing

This case study does not claim to produce live production evidence.

It defines the evidence that should exist if the target architecture were implemented.

---

# Residual Risk

The target architecture reduces a lot of unnecessary exposure.

It does not remove risk from the plant.

That would not be a credible claim.

## Engineering Systems

The engineering workstation remains one of the most powerful systems in the environment.

Segmentation limits what it can reach.

It does not change the fact that an authorized engineering session can make consequential changes to the systems it is allowed to manage.

---

## Vendor Access

Approved vendor access remains a third-party risk.

A jump host, better authentication, and logging make that access easier to control and observe.

They do not make a compromised vendor credential harmless.

---

## Legacy Field Devices

The MS/TP devices still have limited native security capability.

Their protection depends heavily on:

* Gateway containment
* Segmentation
* Monitoring
* Process awareness
* Physical access controls
* Operational procedures

That is a compensating-control model, not a claim that the legacy devices themselves became secure.

---

## Boundary Configuration

Firewalls and segmentation only work as well as their configuration.

Bad rules, temporary exceptions, poor change control, or stale access can gradually rebuild the same broad trust the target architecture was meant to remove.

That means the rulebase itself becomes something that needs to be reviewed over time.

---

## Monitoring Limits

Anomaly detection is useful.

It is not magic.

OT behavior changes for plenty of legitimate reasons, and a tool may not know the difference between a cyber event and a plant behaving strangely because a valve stuck or an RTD went bad.

Monitoring has to be paired with operational context.

---

## Maintenance Activity

Direct service work creates temporary exposure by design.

That risk can be reduced through scope, supervision, endpoint requirements, and access control.

It cannot be completely eliminated while still allowing technicians and vendors to service equipment.

---

## Governance Drift

This may be the easiest residual risk to underestimate.

Architectures age.

People change jobs. Vendors change. Equipment gets replaced. Temporary exceptions become permanent. Documentation falls behind. Somebody opens a firewall rule to get through a maintenance window and nobody closes it.

That is how the target state eventually becomes the next legacy state.

Periodic review is therefore part of maintaining the architecture, not an optional administrative exercise.

---

# Validation Conclusion

The target architecture should only be considered successful if it delivers both:

> **Less cybersecurity exposure**

and

> **A plant that still works**

The validation approach checks segmentation, privilege, remote access, engineering reachability, data flow, legacy-device containment, monitoring, maintenance, manual operation, and ownership.

The remaining risk is not ignored or hidden behind the architecture.

It is identified and managed.

The end state is not zero risk.

It is a plant where the remaining risks are more visible, more constrained, and much harder to turn into uncontrolled access across the environment.
