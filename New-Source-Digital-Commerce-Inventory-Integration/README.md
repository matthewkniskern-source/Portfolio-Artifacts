# New Source — Digital Commerce & Inventory Integration

## Executive summary

This project proposes an integration between a public commerce storefront, **Zoho Inventory** (warehouse inventory authority), and **Lightspeed** (retail pricing, checkout and completed-order authority). The current problem is manual stock updates and sales handoffs, which can leave online availability out of sync and make completed-sale reconciliation difficult.

The proposed solution places an adapter-based **middleware layer** between storefront and vendor systems. It would publish stock availability using periodic Zoho synchronization, apply temporary cart reservations without prematurely decrementing warehouse inventory, process confirmed Lightspeed sales with duplicate-event protection, and log exceptions for reconciliation.

**Status: Architecture and requirements documentation, not an implemented Zoho or Lightspeed integration.** The repository contains specifications, flow descriptions, contracts and controls, rather than a deployed middleware application or validated vendor API connection.

## Reviewer pathway

| Artifact | What it covers |
| --- | --- |
| [Current inventory workflow](docs/00-current-state/current-inventory-workflow.md) | Manual handoffs and the starting process |
| [Problem statement](docs/01-business-case/problem-statement.md) | Business and operational objectives |
| [Requirements traceability](docs/02-requirements/requirements-traceability.md) | Capability-to-requirement relationships |
| [Integration architecture](docs/04-architecture/integration-architecture.md) | Zoho/Lightspeed adapters, sync, sale events and reconciliation |
| [API contracts](docs/04-architecture/api-contracts.md) | Proposed interface behavior and data exchange |
| [Source-of-truth model](docs/05-data-and-governance/source-of-truth-model.md) | Allocation of inventory and commerce authority |
| [Threat model](docs/06-security-and-compliance/threat-model.md) | Proposed threat and control assessment |

## Architectural decision points

- **Zoho** governs warehouse stock; **Lightspeed** governs retail prices and transaction completion.
- Middleware tracks available web quantity after active reservations and makes retry/idempotency decisions.
- Failed sync and mismatches should create visible reconciliation exceptions, not silent overwrites.
- Raw payment-card information stays outside middleware and the proposed inventory services.
- Vendor API compatibility, auth flows, webhooks, race conditions and reconciliation must be validated in a controlled proof of concept before rollout.

## Proposed acceptance evidence (not yet captured)

A future executable prototype should demonstrate representative stock reads, reservation expiry, completed sales, duplicate event suppression, failed-vendor recovery, and deterministic reconciliation. No test runs or production performance are claimed here.

See the [documentation folders](docs/) for the remaining data models, workflows, UX and control descriptions.
