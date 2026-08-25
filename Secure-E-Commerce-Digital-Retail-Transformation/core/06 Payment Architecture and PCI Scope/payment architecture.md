# Payment Architecture and PCI Scope

## 1. Purpose

This section defines a future-state payment design for One-Punch Anime Emporium that minimizes the retailer's direct exposure to payment-card data.

The preferred architecture uses a third-party hosted or tokenized payment provider rather than allowing the retailer's application to directly collect, store, or process raw cardholder data.

The objective is to support online purchasing while reducing unnecessary payment-security scope.

This is a design and scope-management exercise.

It does not represent PCI DSS certification or a completed compliance assessment.

---

## 2. Payment Design Principle

The retailer should avoid becoming the system that handles raw payment-card data.

The preferred model is:

```text
Customer
   ↓
Retail Website
   ↓
External Hosted Payment Provider
   ↓
Payment Network / Issuer
   ↓
Authorization Result
   ↓
Retail Application Receives Reference + Status
```

The retailer application should receive only the information required to:

* associate payment activity with an order;
* determine payment status;
* reconcile transactions;
* support refunds;
* troubleshoot payment-related exceptions.

Raw cardholder data should remain within the payment provider's controlled environment.

---

# 3. Trust Boundaries

The payment workflow contains several distinct trust boundaries.

```text
Customer Browser
      │
      ▼
Retailer Website / Application
      │
      │  Redirect or Tokenized Payment Interaction
      ▼
Third-Party Payment Provider
      │
      ▼
Payment Network / Financial Institution
```

The primary design goal is to prevent payment-card data from crossing unnecessarily into the retailer-controlled environment.

The retailer remains responsible for protecting:

* order information;
* payment references;
* customer contact information;
* authentication and session information;
* transaction status;
* administrative access.

The payment provider remains responsible for processing sensitive cardholder information within its payment environment.

---

# 4. Payment Data Flow

## 4.1 Customer Checkout

```text
Customer Reviews Cart
        ↓
Checkout Information Validated
        ↓
Order Prepared for Payment
        ↓
Customer Transferred to Hosted Payment Interface
        ↓
Payment Provider Collects Card Data
        ↓
Provider Processes Authorization
        ↓
Provider Returns Transaction Result
        ↓
Retailer Stores Provider Reference + Payment Status
        ↓
Order State Updated
        ↓
Customer Receives Confirmation or Failure Message
```

The retailer should not require raw card data to complete any application-side step.

---

# 5. Data Entering the Retailer Environment

The retailer application may legitimately receive or maintain:

* Order ID
* Customer ID where applicable
* Order amount
* Currency
* Payment provider name
* Provider transaction reference
* Token or non-sensitive payment reference where appropriate
* Authorization status
* Transaction timestamp
* Refund status
* Limited payment-method descriptor where supplied safely by the provider, such as card brand or masked last digits

Only data required for legitimate operational use should be retained.

---

# 6. Data Remaining with the Payment Provider

The retailer application should not intentionally receive or store:

* full payment-card number;
* CVV or CVC;
* PIN data;
* magnetic-stripe data;
* full sensitive authentication data;
* raw payment credentials.

The external payment provider should remain the system responsible for collecting and processing this information.

---

# 7. Token and Reference Handling

The retailer may need a token or provider-generated reference to support transaction management.

Examples include:

* transaction lookup;
* refund initiation;
* payment reconciliation;
* dispute investigation;
* customer-service review.

A token or reference should be treated as sensitive operational information even when it cannot independently be used as a raw payment credential.

Recommended handling includes:

* restrict access to authorized functions;
* do not expose references unnecessarily in customer-facing URLs;
* avoid logging full references where partial values are sufficient;
* protect references in transit;
* retain them only as long as required for legitimate operational purposes.

---

# 8. Order and Payment Separation

Order state and payment state should remain logically separate.

Example:

```text
Order
-----
Pending
Awaiting Payment
Paid
Processing
Completed
Cancelled
Failed

Payment
-------
Initiated
Authorized
Declined
Cancelled
Refunded
Partially Refunded
```

This prevents ambiguous conditions such as assuming that an order is paid merely because checkout was initiated.

A valid order-processing decision should use both states where required.

For example:

```text
Payment Authorized
       +
Valid Order
       ↓
Order May Transition to Paid
```

---

# 9. Failed Payment Behavior

A failed payment must produce a clear non-success state.

Recommended behavior:

```text
Payment Attempt
      ↓
Provider Declines / Fails
      ↓
PaymentStatus = Declined or Failed
      ↓
Order Remains Unpaid
      ↓
Customer Receives Failure Message
      ↓
Cart Preserved Where Practical
      ↓
Customer May Retry
```

The system should not:

* display a successful order confirmation;
* reduce inventory permanently as though the sale completed;
* mark the order as paid;
* create duplicate orders through uncontrolled retry behavior.

---

# 10. Payment Provider Outage

If the payment provider is unavailable:

* checkout should fail safely;
* the customer should receive a clear temporary-unavailability message;
* the cart should be retained where practical;
* the system should avoid repeated automatic payment attempts;
* uncertain transaction states should be reconciled before retrying;
* staff should have a defined escalation path for prolonged outages.

The retailer should not attempt to bypass the provider by collecting card details through an alternate insecure mechanism.

---

# 11. Inventory and Payment Timing

Inventory and payment behavior should be coordinated.

One possible model is:

```text
Checkout Begins
      ↓
Inventory Rechecked
      ↓
Temporary Reservation
      ↓
Payment Authorization
      ↓
┌───────────────────────────┐
│ Authorization Successful? │
└─────────────┬─────────────┘
              │
        No    │    Yes
        ↓     │     ↓
Release       │ Confirm Reservation
Reservation   │
              ↓
        Continue Fulfillment
```

The exact reservation model depends on the production inventory system.

For the academic demonstration, inventory behavior may be simulated.

---

# 12. Refund Considerations

Refunds should be processed through the same approved payment provider used for the original transaction.

Recommended flow:

```text
Refund Requested
      ↓
Validate Order and Payment
      ↓
Authorized Staff Approval
      ↓
Submit Refund Through Provider
      ↓
Receive Provider Result
      ↓
Update Payment Reference
      ↓
Update Order as Appropriate
      ↓
Notify Customer
```

The retailer should store the provider's refund status and reference rather than reconstructing payment-card information.

Refund permissions should be limited to authorized roles.

---

# 13. Reconciliation

The retailer requires enough payment information to compare internal orders with external payment activity.

Typical reconciliation inputs include:

* Order ID
* Order total
* Provider transaction reference
* Authorization amount
* Payment status
* Transaction date
* Refund amount where applicable

Reconciliation should identify conditions such as:

* retailer order exists but payment does not;
* authorized payment exists without corresponding order completion;
* payment amount differs from order total;
* duplicate transaction reference;
* refund state differs between retailer and provider.

Exceptions should require review rather than automatic assumptions.

---

# 14. Logging Restrictions

Payment-related logging should be designed conservatively.

Logs may include:

* Order ID
* Payment event type
* Payment status
* Timestamp
* Provider result code
* Administrative user involved in refund or review activity

Logs should not contain:

* full card number;
* CVV/CVC;
* full payment credentials;
* customer-entered payment fields;
* authentication secrets;
* unnecessary provider tokens.

Where payment references are logged, truncation or masking should be considered where operationally sufficient.

---

# 15. Administrative Access

Payment-related administrative functions should be restricted according to role.

Examples:

| Role                     | Payment Access                                                          |
| ------------------------ | ----------------------------------------------------------------------- |
| Sales Associate          | Limited or none                                                         |
| Store Manager            | View relevant order/payment status                                      |
| E Commerce Administrator | Operational payment review                                              |
| System Administrator     | Technical platform administration; no routine business refund authority |
| Auditor / Reviewer       | Read-only transaction and control evidence                              |
| Customer                 | Own payment result only                                                 |

The detailed RBAC model is maintained in the Security and Access Control section.

---

# 16. PCI Scope Reduction Rationale

Using an externally hosted or appropriately tokenized payment process reduces the amount of payment-card functionality operated directly by the retailer.

The design attempts to limit the retailer-controlled environment to:

* order creation;
* transaction references;
* payment status;
* reconciliation;
* refund initiation;
* operational logging.

The retailer does not intentionally store raw cardholder data.

This does not eliminate PCI DSS responsibilities.

The actual compliance scope would depend on:

* the selected payment integration;
* hosting configuration;
* website architecture;
* administrative processes;
* third-party provider relationship;
* applicable PCI DSS requirements.

The architecture is intended to reduce unnecessary exposure and simplify scope rather than claim exemption.

---

# 17. Third-Party Provider Considerations

Selection of a production payment provider should consider:

* supported hosted or tokenized payment integration;
* transaction security;
* availability;
* refund support;
* fraud controls;
* logging and reporting;
* incident communication;
* service availability;
* support model;
* contractual responsibilities;
* PCI-related documentation;
* integration maintenance requirements.

Specific vendor selection is outside the current case-study scope unless a platform is later chosen for demonstration.

---

# 18. Academic Implementation Boundary

The academic website will not process real payment-card information.

A demonstration checkout may simulate:

* order review;
* required-field validation;
* payment submission;
* successful authorization;
* declined payment;
* order confirmation.

Any simulated payment form should clearly avoid requesting real payment-card data.

Real payment processing remains part of the future-state design only.

---

# 19. Design Outcome

The proposed architecture separates the retailer's business process from direct payment-card handling.

The intended flow is:

```text
Retailer Manages
---------------
Products
Cart
Customer Information
Order
Fulfillment
Payment Status

Payment Provider Manages
------------------------
Card Entry
Sensitive Payment Data
Authorization
Payment Processing
```

This separation allows the retailer to support online commerce while minimizing the amount of sensitive payment data entering its environment and keeping payment responsibilities aligned with a specialized external provider.

