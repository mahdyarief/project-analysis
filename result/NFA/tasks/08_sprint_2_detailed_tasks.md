# Sprint 2: "Value Delivery" - Detailed Features

## Feature 1: Dashboard KPI Aggregations (Head Office)
**Description:** SQL aggregations pulling total spend, total count of historic orders, active stores tally, top templates ordered, and "eShop Adoption" rates.
**Acceptance Criteria:**
- [x] API pulls real-time SQL count/sums in under 200ms latency.
- [x] Returns payload shaped precisely for the Widget components to consume gracefully.
**Tech Notes:** Avoid `SELECT *`. Heavy use of `GROUP BY` required on the Postgres instance.

## Feature 2: Head Office Dashboard Layout
**Description:** Generate the main view connecting to the KPI aggregates. Features interactive list widgets for "Orders with Issues". Clicking *any* metric or widget slides out a Right Drawer providing tabular breakdown data.
**Acceptance Criteria:**
- [x] Skeleton Loaders display globally until data hydration completes.
- [x] If API returns 500 block, component fails out to an Error Boundary state bearing a functional "Try again" trigger.
- [x] Drawers overlay the current router path without changing the URL.
**Tech Notes:** Recommend using framer-motion or standard CSS transitions for smooth drawer overlay paths. React Error Boundaries are critical for the "Try Again" fallback.

## Feature 3: Stripe SEPA Mandate Webhook Setup
**Description:** Create a webhook listener accepting payloads verifying when a local Store's bank has authorized the SEPA Direct Debit mandate.
**Acceptance Criteria:**
- [x] Endpoint rejects requests failing Stripe Signature validation.
- [x] Authorized payload updates the Store `payment_status` column allowing checkout usage.
**Tech Notes:** Utilize raw body parsing for stripe construction. Ensure idempotent handling of duplicate webhooks.

## Feature 4: Catalog Cart Sub-totaling Engine
**Description:** Develop the backend cart object which tallies up the `local_price` parameter per line item and produces a finalized Checkout payload containing the `subTotal`, calculated `shipping` overhead, and the absolute `total`.
**Acceptance Criteria:**
- [x] Calculation executes natively on the server utilizing current DB prices (frontend inputs are ignored for security).
- [x] Cart supports multi-entity checkout (different quantities allocated to different store IDs).
**Tech Notes:** Store currency as `integer` (e.g. `$100.00` = `10000` cents) to prevent JS floating point computation chaos.

---
**(Subset generated for brevity, following the exact deep-dive methodology for all 74 SP of Sprint 2 tasks...)**
