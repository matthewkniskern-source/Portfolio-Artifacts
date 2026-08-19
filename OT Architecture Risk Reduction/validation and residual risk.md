# Validation and Residual Risk

## Purpose

This document describes how the target-state architecture should be validated after implementation and identifies the principal risks that remain even after the proposed controls are in place.

The objective is not to prove that the environment is risk-free.

The objective is to verify that the architecture behaves as intended, that required plant functions remain available, and that the controls introduced to reduce cyber risk do not create unacceptable operational consequences.

Supporting analysis is available in:

* [Legacy Risk Findings](legacy%20risk%20findings.md)
* [NIST Alignment](nist%20alignment.md)
* [Target Architecture](target%20architecture.md)
* [Risk Reduction Mapping](risk%20reduction%20mapping.md)

---

# Validation Principles

Validation should confirm both cybersecurity behavior and operational behavior.

A control should not be considered successful solely because it blocks traffic or limits access.

It must also preserve the communications and maintenance functions required for safe and reliable plant operation.

The validation process therefore asks two questions:

1. **Did the control reduce the intended cybersecurity exposure?**
2. **Did the plant continue to function as required after the control was introduced?**

---

# 1. Network Segmentation Validation

## Objective

Confirm that the target architecture enforces the intended separation between:

* Enterprise network
* OT DMZ
* Supervisory zone
* Engineering / administrative zone
* Control zone
* Legacy MS/TP gateways

## Validation Activities

Verify that:

* Enterprise endpoints cannot directly reach PLCs or field-network gateways
* Management workstations cannot initiate process-control commands
* Supervisory systems can communicate only with required control services
* Engineering workstations can reach only explicitly authorized controller destinations
* DMZ systems cannot communicate arbitrarily with OT assets
* Legacy field-network gateways are not reachable from enterprise or general remote-access networks
* Unapproved inter-zone traffic is denied

## Expected Result

Required plant communications remain functional while unauthorized or unnecessary communication paths are blocked.

---

# 2. Management Access Validation

## Objective

Confirm that plant management retains required visibility without inherited process-control authority.

## Validation Activities

Verify that the management role can:

* View approved plant status
* Review selected alarms
* Access approved reporting information
* Review historical or trend data where required

Verify that the management role cannot:

* Issue start or stop commands
* Modify supervisory setpoints
* Change plant sequencing
* Perform engineering functions
* Reach controllers directly

## Expected Result

The business requirement for plant visibility remains available while unnecessary command capability is removed.

---

# 3. Vendor Remote-Access Validation

## Objective

Confirm that all approved third-party remote access follows the governed target-state pathway.

## Validation Activities

Verify that:

* The historical vendor VPN is disabled or removed
* Vendor remote sessions terminate through the approved remote-access gateway
* Remote users must traverse the privileged jump host before reaching authorized OT systems
* Sessions are limited to approved destinations
* Authentication events are logged
* Session activity is visible to monitoring systems
* Vendor access can be disabled when no longer required

## Expected Result

No recognized vendor support pathway bypasses the controlled remote-access architecture.

---

# 4. Engineering Access Validation

## Objective

Confirm that the engineering workstation retains necessary high-privilege capability without unrestricted OT reachability.

## Validation Activities

Test access to:

* Authorized PLCs
* Required BACnet controllers
* Approved infrastructure systems
* Recovery and configuration resources

Verify that the workstation cannot reach unrelated systems for which no engineering requirement exists.

Where practical, confirm that administrative activity is logged and attributable to an authorized user or maintenance event.

## Expected Result

Engineering capability remains available but is constrained to documented operational requirements.

---

# 5. Historian and Data-Flow Validation

## Objective

Confirm that operational data can be consumed by enterprise users without requiring direct access to the primary OT environment.

## Validation Activities

Verify that:

* The OT historian or data collector receives required process information
* Approved datasets replicate to the DMZ reporting or historian service
* Enterprise users query the DMZ service rather than the OT historian
* Replication direction and allowed services match the intended architecture
* Failure of the enterprise-facing reporting service does not interrupt plant control
* Failure of the replication path does not interrupt local historian collection

## Expected Result

Operational reporting remains available while enterprise data consumption is separated from control-system access.

---

# 6. Legacy MS/TP Containment Validation

## Objective

Confirm that operationally necessary legacy MS/TP devices remain functional while exposure around their gateways is reduced.

## Validation Activities

Verify that:

* BACnet/IP-to-MS/TP gateways communicate only with required control systems
* Enterprise endpoints cannot access the gateways directly
* Remote vendor sessions cannot access MS/TP networks unless specifically authorized
* Required differential-pressure, temperature, flow, status, and permissive values continue reaching plant logic
* Loss of an MS/TP trunk produces the expected alarms or degraded behavior
* Restoration of the trunk returns the system to expected operation

## Expected Result

Legacy field networks continue supporting automatic plant control without remaining broadly exposed to unrelated network zones.

---

# 7. Passive Monitoring and Anomaly Detection Validation

## Objective

Confirm that monitoring improves visibility without introducing unacceptable traffic or process interference.

## Validation Activities

Verify monitoring visibility into:

* New or unexpected BACnet devices
* New communication relationships
* Unexpected protocol use
* Abnormal traffic volume
* Unexpected controller-to-gateway behavior
* Remote-access events
* Administrative activity
* Significant deviations in process values

Create controlled test conditions where appropriate, such as:

* An unauthorized test endpoint attempting communication
* A simulated unexpected connection attempt
* A known maintenance event
* A deliberately changed process value within safe testing limits

Confirm that cybersecurity observations can be correlated with normal plant operating context.

## Expected Result

Abnormal activity can be identified without disrupting sensitive OT communications.

---

# 8. Maintenance Access Validation

## Objective

Confirm that required equipment-level troubleshooting remains possible without granting mobile devices broad OT access.

## Validation Activities

Verify that:

* Company maintenance laptops can connect to approved equipment service ports
* Vendor laptops can connect only during approved maintenance activity
* Direct service connections do not automatically provide general OT network access
* Temporary vendor access is removed at completion of the task
* Maintenance activity is documented where appropriate

## Expected Result

Specialized troubleshooting capability is preserved while temporary endpoints remain constrained to their intended maintenance function.

---

# 9. Local and Degraded Operation Validation

## Objective

Confirm that cybersecurity controls do not eliminate the plant's ability to operate during supervisory-system impairment.

## Validation Activities

Where operationally safe and authorized, confirm that:

* PLCs maintain appropriate local logic if SCADA/BAS communications are unavailable
* Local equipment controls remain functional
* The central physical control board remains available
* Operators can maintain a reduced but coordinated plant configuration
* Supervisory-system restoration does not create unexpected process behavior

## Expected Result

Loss of centralized supervisory capability does not automatically result in complete loss of physical plant control.

---

# 10. Governance Validation

## Objective

Confirm that administrative responsibility is explicit rather than dependent on informal institutional knowledge.

## Validation Activities

Verify that ownership is assigned for:

* Network boundaries
* Firewall policy
* Controller administration
* Engineering workstation administration
* Vendor access approval
* Account lifecycle management
* Asset inventory
* Monitoring
* Backups
* Configuration management
* Incident coordination
* System retirement

Verify that legacy access paths discovered during assessment have an assigned disposition:

* Retain and govern
* Replace
* Disable
* Remove

## Expected Result

Critical cybersecurity responsibilities have identifiable owners and do not depend solely on individual memory or tenure.

---

# Validation Evidence

A real implementation should retain evidence sufficient to demonstrate that controls were tested and behaved as intended.

Representative evidence may include:

* Approved network diagrams
* Firewall-rule review records
* Access-control test results
* Remote-access logs
* Authentication records
* Monitoring alerts
* Historian replication test results
* Backup and recovery records
* Maintenance-access documentation
* Configuration baselines
* Asset inventories
* Change records
* Operator acceptance testing

This case study does not generate production evidence but identifies the evidence that would be expected during implementation.

---

# Residual Risk

The target architecture reduces several significant legacy risks but does not eliminate risk.

Important residual risks include:

## Privileged Engineering Systems

The engineering workstation remains capable of making consequential changes to authorized control systems.

Segmentation reduces reachability but does not remove the risk of compromise or misuse of a legitimately privileged asset.

---

## Authorized Vendor Access

Remote vendor access remains a potentially high-impact pathway.

Even when governed through a jump host and monitored gateway, compromise of authorized credentials or misuse during a legitimate session remains possible.

---

## Legacy Field Devices

BACnet MS/TP devices continue operating with limited native security capabilities.

Their risk is reduced primarily through containment, gateway control, monitoring, and operational procedures rather than through security functionality on the devices themselves.

---

## Boundary Configuration

Firewalls, access rules, routing policies, and segmentation controls can be misconfigured.

The target architecture therefore depends on accurate configuration, change control, and periodic review.

---

## Monitoring Limitations

Anomaly detection may identify unusual behavior without immediately establishing whether the cause is:

* Cyber compromise
* Equipment failure
* Instrument drift
* Calibration error
* Maintenance activity
* Legitimate process transition

Cybersecurity monitoring therefore requires operational context and qualified interpretation.

---

## Maintenance Activity

Temporary direct service access creates an unavoidable period of elevated exposure.

The risk can be managed but not completely removed when specialized maintenance requires direct connection to equipment.

---

## Governance Drift

Access models, vendor relationships, personnel, equipment, and business requirements will change over time.

A secure architecture can gradually return to a legacy condition if:

* Old accounts are not removed
* Temporary paths become permanent
* Firewall exceptions accumulate
* Documentation becomes outdated
* Ownership becomes unclear

Periodic review is therefore necessary to preserve the intended security posture.

---

# Validation Conclusion

The target-state architecture should be considered successful only if it demonstrates both:

**Reduced Cybersecurity Exposure**
and
**Preserved Operational Capability**

The validation strategy therefore emphasizes segmentation, access control, monitoring, governed remote access, legacy-system containment, and continued local plant operation.

Residual risk remains, particularly around privileged users, vendors, legacy devices, and configuration management.

The objective is not zero risk.

The objective is a plant architecture in which remaining risks are **visible, constrained, governed, and operationally understood**.
