# Role-Based Access Control

## Roles

### Employee

Can:

* View operational dashboard
* View BI metrics
* View inventory status
* View active reservations
* View discrepancies
* View reconciliation history
* View recent completed-sale activity
* Maintain application text
* Maintain compatibility text
* Maintain related-product recommendations

Cannot:

* Adjust inventory
* Resolve reconciliation exceptions
* Change integration settings
* Change inventory thresholds
* Manage users or roles

### Manager

Includes employee permissions plus:

* Resolve reconciliation exceptions
* Perform authorized inventory adjustments
* Review detailed audit records
* Configure merchandising controls
* Change approved inventory thresholds
* Manage selected operational settings

### Owner / Administrator

Includes manager permissions plus:

* Manage users
* Assign roles
* Change integration configuration
* Change synchronization intervals
* Change reservation duration
* Change system-wide thresholds
* Manage adapter configuration
* Review complete audit history
* Manage system-wide operational settings

## Permission Matrix

| Capability                  | Employee | Manager | Owner / Admin |
| --------------------------- | -------: | ------: | ------------: |
| View dashboard              |      Yes |     Yes |           Yes |
| View BI                     |      Yes |     Yes |           Yes |
| View inventory              |      Yes |     Yes |           Yes |
| View reservations           |      Yes |     Yes |           Yes |
| View discrepancies          |      Yes |     Yes |           Yes |
| View reconciliation history |      Yes |     Yes |           Yes |
| Maintain product metadata   |      Yes |     Yes |           Yes |
| View detailed audit records |  Limited |     Yes |           Yes |
| Resolve discrepancies       |       No |     Yes |           Yes |
| Adjust inventory            |       No |     Yes |           Yes |
| Change low-stock threshold  |       No |     Yes |           Yes |
| Change sync interval        |       No |      No |           Yes |
| Change reservation duration |       No |      No |           Yes |
| Configure integrations      |       No |      No |           Yes |
| Manage users                |       No |      No |           Yes |
| Assign roles                |       No |      No |           Yes |

## Access Rules

* Internal dashboard access requires authentication.
* System-changing actions require authorization.
* Broad visibility does not imply broad modification rights.
* Users shall receive only the permissions assigned to their role.
* Restricted actions shall be rejected server-side.
* UI controls for unauthorized actions should be hidden or disabled.

## Audit Requirements

The following role-related actions shall be audited:

* User creation
* User deactivation
* Role assignment
* Role change
* Permission-impacting configuration changes
* Inventory-adjustment actions
* Reconciliation resolution actions

## Session Control

Internal sessions should support:

* Authenticated login
* Session expiration
* Logout
* Protection against unauthorized dashboard access

## Service Accounts

Automated processes should use service identities distinct from staff accounts.

Examples:

* Inventory sync process
* Metadata sync process
* Reconciliation process
* Completed-sale processor

System-generated audit events shall identify the responsible service process.
