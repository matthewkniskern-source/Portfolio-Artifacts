# Retention and Logging

## Logged Events

The system shall log:

* Inventory synchronization attempts
* Synchronization failures
* Reservation creation
* Reservation completion
* Reservation expiration
* Completed-sale processing
* Duplicate sale events
* Inventory decrements
* Reconciliation activity
* Manual inventory adjustments
* Authentication events
* Role and permission changes
* Integration configuration changes

## Application Logs

Application logs should include:

* Timestamp
* Service or component
* Event type
* Result
* Relevant SKU or object identifier
* Order, reservation, or reconciliation reference where applicable
* Error code where applicable

## Excluded Log Data

Logs shall not contain:

* Payment-card numbers
* CVV data
* Raw payment credentials
* API secrets
* Authentication tokens
* Passwords
* Sensitive production credentials

## Log Levels

Recommended levels:

* `INFO` — normal operational events
* `WARN` — discrepancies, retries, stale data
* `ERROR` — failed integration or processing events

## Operational Retention

POC retention may remain configurable.

Recommended production categories:

| Record Type            | Retention Approach                    |
| ---------------------- | ------------------------------------- |
| Application logs       | Short-term operational retention      |
| Integration logs       | Medium-term troubleshooting retention |
| Reservation history    | Medium-term operational retention     |
| Reconciliation records | Longer-term operational retention     |
| Audit records          | Longer-term governance retention      |
| BI aggregates          | Retain as required for trend analysis |

## Audit Separation

Audit records should remain logically separate from routine application logs.

Audit history shall not depend on transient application log retention.

## Reservation Cleanup

Expired reservations may be removed from active storage after:

* Final status recorded
* Availability restored
* Required traceability retained

## Failed Event Retention

Failed integration and transaction events shall remain available long enough to support:

* Retry
* Investigation
* Reconciliation
* Root-cause review

## Log Access

* Employees may view limited operational status.
* Managers may review detailed operational logs where required.
* Owners / administrators may access full system and audit history.

## Configuration

Retention periods and logging verbosity shall be configurable without modifying core application logic.
