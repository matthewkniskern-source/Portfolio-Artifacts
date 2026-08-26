# Secrets and API Key Handling

## Secret Types

Protected values may include:

* Zoho API credentials
* Lightspeed API credentials
* Middleware service secrets
* Authentication signing keys
* Database credentials
* Administrative tokens

## Storage

Secrets shall not be:

* Hard-coded in application source
* Committed to Git
* Stored in public configuration files
* Embedded in frontend JavaScript
* Written to logs

Secrets should be supplied through:

* Environment variables
* Host-level secret stores
* Container secret management
* Cloud secret-management services where available

## Repository Controls

The public repository shall include:

* `.env.example`
* Placeholder configuration values
* Setup instructions

The repository shall exclude:

* `.env`
* Production credentials
* API tokens
* Private keys
* Live customer secrets

Example:

```text
ZOHO_API_URL=https://mock-zoho.local
ZOHO_API_KEY=replace_me

LIGHTSPEED_API_URL=https://mock-lightspeed.local
LIGHTSPEED_API_KEY=replace_me
```

## Frontend Exposure

Customer-facing and dashboard frontend code shall not contain vendor API credentials.

Frontend requests should flow through the middleware:

```text
Browser
   │
   ▼
Middleware API
   │
   ├── Zoho
   └── Lightspeed
```

## Credential Scope

Production credentials should use the minimum permissions necessary.

Examples:

* Inventory read access
* Inventory adjustment access
* Completed-order read access
* Product pricing read access

Administrative permissions should not be granted where operational permissions are sufficient.

## Rotation

Production credentials should support:

* Periodic rotation
* Immediate replacement if compromised
* Revocation without application redesign

## Service Separation

Where possible, separate credentials should be used for:

* Inventory synchronization
* Completed-sale processing
* Metadata synchronization
* Administrative operations

## Logging

Logs may record:

* Integration name
* Request result
* Error code
* Timestamp

Logs shall not record:

* API keys
* Access tokens
* Refresh tokens
* Passwords
* Signing secrets

## Failed Authentication

Authentication failure
→ Request rejected
→ Failure logged without secret value
→ No fallback to unauthenticated access

## Proof of Concept

The POC shall use mock credentials only.

Example mock values shall be clearly identifiable as non-production data.
