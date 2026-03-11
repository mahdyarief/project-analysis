# NFA — Jira Import Ready

> **How to use this file:**
> 1. Create your Jira project (Scrum or Kanban)
> 2. Create the Epics first (Section A)
> 3. Create Stories/Tasks and link to their Epic (Section B)
> 4. Set Story Points per ticket
> 5. Create Sprint 1 and Sprint 2, drag tasks into sprints per column "Sprint"
> 6. Use the "Layer" label on each ticket: `FE`, `BE`, or `WIRE`

---

## A. Epics

| Epic Key | Epic Name | Description |
|----------|-----------|-------------|
| EPIC-01 | Authentication & Access Control | Secure login for all 3 apps: Admin (email/password), Head Office (email/password + forgot password), Mobile (OTP passwordless) + SEPA payment setup |
| EPIC-02 | Admin — Network Management | Super admin ability to list, view, and navigate Head Offices |
| EPIC-03 | Admin — Product, Supplier & Order Management | Admin CRUD for products and suppliers; global order visibility |
| EPIC-04 | Head Office — Dashboard & Analytics | KPI dashboard and "Orders with Issues" alert feed for HO managers |
| EPIC-05 | Head Office — Store Network Management | Store list, creation, detail view, and HO account management |
| EPIC-06 | Head Office — Catalogue & Template Management | Product catalogue browsing and full 4-step InDesign template creation wizard with async PDF generation |
| EPIC-07 | Head Office — Stock & Inventory Management | Warehouse stock view, stock transfers to stores, and movement history |
| EPIC-08 | Head Office — Order Management | HO order list, detail, and cart management |
| EPIC-09 | Mobile App — End-to-End Ordering | Mobile store app: catalogue browse, cart, SEPA order placement, order history, and profile management |

---

## B. Full Task List (Jira Import Format)

### SPRINT 1 TASKS

| ID | Epic | Story | Task Title | Layer | SP | Sprint | Status |
|----|------|-------|-----------|-------|----|----|--------|
| T-01-01 | EPIC-01 | STORY-01 | [FE] Admin login screen: email/password form, error states, loading state | FE | 3 | Sprint 1 | Backlog |
| T-01-02 | EPIC-01 | STORY-01 | [BE] POST /auth/admin/login — validate credentials, return JWT + refresh token | BE | 3 | Sprint 1 | Backlog |
| T-01-03 | EPIC-01 | STORY-01 | [WIRE] Connect admin login form to API: JWT storage, redirect on success, toast on error | WIRE | 2 | Sprint 1 | Backlog |
| T-02-01 | EPIC-01 | STORY-02 | [FE] HO login screen: form + field validation states + error/success feedback | FE | 3 | Sprint 1 | Backlog |
| T-02-02 | EPIC-01 | STORY-02 | [FE] Forgot Password flow UI: email input → confirmation screen | FE | 3 | Sprint 1 | Backlog |
| T-02-03 | EPIC-01 | STORY-02 | [BE] POST /auth/ho/login — validate credentials, return JWT + refresh token | BE | 2 | Sprint 1 | Backlog |
| T-02-04 | EPIC-01 | STORY-02 | [BE] POST /auth/ho/forgot-password — send password reset email with secure token | BE | 3 | Sprint 1 | Backlog |
| T-02-05 | EPIC-01 | STORY-02 | [BE] POST /auth/ho/reset-password — validate token, update password | BE | 2 | Sprint 1 | Backlog |
| T-02-06 | EPIC-01 | STORY-02 | [WIRE] Connect HO login + forgot password forms to API, handle all response states | WIRE | 3 | Sprint 1 | Backlog |
| T-03-01 | EPIC-01 | STORY-03 | [FE] Mobile login screen: email input + "Send OTP" CTA | FE | 2 | Sprint 1 | Backlog |
| T-03-02 | EPIC-01 | STORY-03 | [FE] OTP entry screen: 6-digit input, resend timer, error/success states | FE | 3 | Sprint 1 | Backlog |
| T-03-03 | EPIC-01 | STORY-03 | [BE] POST /auth/mobile/request-otp — generate & email OTP (5 min TTL) | BE | 3 | Sprint 1 | Backlog |
| T-03-04 | EPIC-01 | STORY-03 | [BE] POST /auth/mobile/verify-otp — validate OTP, return JWT + refresh token | BE | 2 | Sprint 1 | Backlog |
| T-03-05 | EPIC-01 | STORY-03 | [WIRE] Connect email → OTP screens to API; manage JWT in secure storage | WIRE | 3 | Sprint 1 | Backlog |
| T-04-01 | EPIC-01 | STORY-04 | [FE] SEPA mandate setup screen: Stripe SDK SEPA form + confirmation screen | FE | 5 | Sprint 1 | Backlog |
| T-04-02 | EPIC-01 | STORY-04 | [BE] POST /payments/sepa/setup — create Stripe SetupIntent; handle SEPA mandate webhooks | BE | 8 | Sprint 1 | Backlog |
| T-04-03 | EPIC-01 | STORY-04 | [WIRE] Connect Stripe SDK to SetupIntent flow; gate catalogue access on mandate completion | WIRE | 5 | Sprint 1 | Backlog |
| T-05-01 | EPIC-02 | STORY-05 | [FE] Admin: Head Office list page — data table, search, country filter, loading/empty states | FE | 3 | Sprint 1 | Backlog |
| T-05-02 | EPIC-02 | STORY-05 | [BE] GET /admin/head-offices — paginated list with search + country filter | BE | 3 | Sprint 1 | Backlog |
| T-05-03 | EPIC-02 | STORY-05 | [WIRE] Connect HO list to API: search debounce + filter; navigate to HO environment | WIRE | 2 | Sprint 1 | Backlog |

---

### SPRINT 2 TASKS

| ID | Epic | Story | Task Title | Layer | SP | Sprint | Status |
|----|------|-------|-----------|-------|----|----|--------|
| T-06-01 | EPIC-02 | STORY-06 | [FE] Admin: Head Office detail view/drawer — display all HO info fields | FE | 2 | Sprint 2 | Backlog |
| T-06-02 | EPIC-02 | STORY-06 | [BE] GET /admin/head-offices/:id — return full HO record | BE | 1 | Sprint 2 | Backlog |
| T-06-03 | EPIC-02 | STORY-06 | [WIRE] Connect HO detail view to API | WIRE | 1 | Sprint 2 | Backlog |
| T-07-01 | EPIC-03 | STORY-07 | [FE] Admin: Product list page — data table, search, filter (category/status), pagination | FE | 3 | Sprint 2 | Backlog |
| T-07-02 | EPIC-03 | STORY-07 | [FE] Admin: Add/Edit product form — all fields (name, SKU, image, price, variants), validation | FE | 5 | Sprint 2 | Backlog |
| T-07-03 | EPIC-03 | STORY-07 | [BE] GET /admin/products — paginated + filterable product list | BE | 2 | Sprint 2 | Backlog |
| T-07-04 | EPIC-03 | STORY-07 | [BE] POST /admin/products — create product with full validation | BE | 3 | Sprint 2 | Backlog |
| T-07-05 | EPIC-03 | STORY-07 | [BE] PUT /admin/products/:id — update product | BE | 2 | Sprint 2 | Backlog |
| T-07-06 | EPIC-03 | STORY-07 | [WIRE] Connect product list + form to API; handle image file uploads | WIRE | 3 | Sprint 2 | Backlog |
| T-12-01 | EPIC-05 | STORY-12 | [FE] HO: Store list page — search, filter, paginated table with key info + action buttons | FE | 3 | Sprint 2 | Backlog |
| T-12-02 | EPIC-05 | STORY-12 | [FE] HO: Store list empty state screen | FE | 1 | Sprint 2 | Backlog |
| T-12-03 | EPIC-05 | STORY-12 | [BE] GET /ho/stores — paginated + filterable store list for current HO | BE | 2 | Sprint 2 | Backlog |
| T-12-04 | EPIC-05 | STORY-12 | [WIRE] Connect store list to API | WIRE | 2 | Sprint 2 | Backlog |
| T-13-01 | EPIC-05 | STORY-13 | [FE] HO: Store creation form — general info, legal info, addresses sections with validation | FE | 5 | Sprint 2 | Backlog |
| T-13-02 | EPIC-05 | STORY-13 | [BE] POST /ho/stores — create store with full validation; auto-link to current HO | BE | 3 | Sprint 2 | Backlog |
| T-13-03 | EPIC-05 | STORY-13 | [WIRE] Connect store creation form to API; handle success/error | WIRE | 2 | Sprint 2 | Backlog |
| T-25-01 | EPIC-09 | STORY-25 | [FE] Mobile: Catalogue screen — grid layout, search, filters, loading/empty/error states | FE | 5 | Sprint 2 | Backlog |
| T-25-02 | EPIC-09 | STORY-25 | [FE] Mobile: Product detail screen — images, fields, required inputs, Add to Cart CTA, error + retry | FE | 5 | Sprint 2 | Backlog |
| T-25-03 | EPIC-09 | STORY-25 | [BE] GET /mobile/catalogue — products available to this store (from admin master catalogue) | BE | 2 | Sprint 2 | Backlog |
| T-25-04 | EPIC-09 | STORY-25 | [BE] GET /mobile/catalogue/:id — product detail + available variants | BE | 2 | Sprint 2 | Backlog |
| T-25-05 | EPIC-09 | STORY-25 | [WIRE] Connect mobile catalogue + product detail to API; pass store token for pricing | WIRE | 3 | Sprint 2 | Backlog |
| T-26-01 | EPIC-09 | STORY-26 | [FE] Mobile: Cart screen — item list, quantity +/-, delete item, total display | FE | 3 | Sprint 2 | Backlog |
| T-26-02 | EPIC-09 | STORY-26 | [FE] Mobile: Order confirmation screen (SEPA) — summary + "Confirm Order" CTA + success/error | FE | 3 | Sprint 2 | Backlog |
| T-26-03 | EPIC-09 | STORY-26 | [BE] GET /mobile/cart — fetch current cart state | BE | 1 | Sprint 2 | Backlog |
| T-26-04 | EPIC-09 | STORY-26 | [BE] PUT /mobile/cart — update cart items/quantities | BE | 2 | Sprint 2 | Backlog |
| T-26-05 | EPIC-09 | STORY-26 | [BE] POST /mobile/orders — create order and charge via Stripe SEPA SetupIntent | BE | 8 | Sprint 2 | Backlog |
| T-26-06 | EPIC-09 | STORY-26 | [WIRE] Connect cart → confirmation → success/error flow to API; handle SEPA charge response | WIRE | 5 | Sprint 2 | Backlog |

---

### SPRINT 3+ BACKLOG (Deferred)

| ID | Epic | Story | Task Title | Layer | SP | Sprint | Status |
|----|------|-------|-----------|-------|----|----|--------|
| T-08-01 | EPIC-03 | STORY-08 | [FE] Admin: Supplier list page | FE | 3 | Sprint 3 | Backlog |
| T-08-02 | EPIC-03 | STORY-08 | [FE] Admin: Supplier create/edit form | FE | 3 | Sprint 3 | Backlog |
| T-08-03 | EPIC-03 | STORY-08 | [BE] GET /admin/suppliers | BE | 2 | Sprint 3 | Backlog |
| T-08-04 | EPIC-03 | STORY-08 | [BE] POST + PUT /admin/suppliers | BE | 3 | Sprint 3 | Backlog |
| T-08-05 | EPIC-03 | STORY-08 | [WIRE] Connect supplier CRUD to API | WIRE | 2 | Sprint 3 | Backlog |
| T-09-01 | EPIC-03 | STORY-09 | [FE] Admin: Global orders list with filters | FE | 3 | Sprint 3 | Backlog |
| T-09-02 | EPIC-03 | STORY-09 | [FE] Admin: Order detail view | FE | 2 | Sprint 3 | Backlog |
| T-09-03 | EPIC-03 | STORY-09 | [BE] GET /admin/orders | BE | 3 | Sprint 3 | Backlog |
| T-09-04 | EPIC-03 | STORY-09 | [BE] GET /admin/orders/:id | BE | 1 | Sprint 3 | Backlog |
| T-09-05 | EPIC-03 | STORY-09 | [WIRE] Connect order list + detail | WIRE | 2 | Sprint 3 | Backlog |
| T-11-01 | EPIC-04 | STORY-11 | [FE] HO: Dashboard KPI cards + network overview widgets | FE | 5 | Sprint 3 | Backlog |
| T-11-02 | EPIC-04 | STORY-11 | [FE] HO: "Orders with Issues" block | FE | 3 | Sprint 3 | Backlog |
| T-11-03 | EPIC-04 | STORY-11 | [BE] GET /ho/dashboard/kpis | BE | 5 | Sprint 3 | Backlog |
| T-11-04 | EPIC-04 | STORY-11 | [BE] GET /ho/dashboard/orders-with-issues | BE | 3 | Sprint 3 | Backlog |
| T-11-05 | EPIC-04 | STORY-11 | [WIRE] Connect dashboard to APIs + auto-refresh | WIRE | 3 | Sprint 3 | Backlog |
| T-14-01 | EPIC-05 | STORY-14 | [FE] HO: Store detail drawer — info, compliance, activity tabs | FE | 5 | Sprint 3 | Backlog |
| T-14-02 | EPIC-05 | STORY-14 | [BE] GET /ho/stores/:id — full record with compliance + activity | BE | 3 | Sprint 3 | Backlog |
| T-14-03 | EPIC-05 | STORY-14 | [WIRE] Connect store detail | WIRE | 2 | Sprint 3 | Backlog |
| T-16-01 | EPIC-06 | STORY-16 | [FE] HO: Catalogue page — product grid, loading/empty/error states | FE | 3 | Sprint 3 | Backlog |
| T-16-02 | EPIC-06 | STORY-16 | [FE] HO: Catalogue filter/search bar | FE | 2 | Sprint 3 | Backlog |
| T-16-03 | EPIC-06 | STORY-16 | [BE] GET /ho/catalogue | BE | 2 | Sprint 3 | Backlog |
| T-16-04 | EPIC-06 | STORY-16 | [WIRE] Connect HO catalogue to API | WIRE | 1 | Sprint 3 | Backlog |
| T-17-01 | EPIC-06 | STORY-17 | [FE] HO: Template list — states + archive with confirmation | FE | 3 | Sprint 3 | Backlog |
| T-17-02 | EPIC-06 | STORY-17 | [BE] GET /ho/templates | BE | 2 | Sprint 3 | Backlog |
| T-17-03 | EPIC-06 | STORY-17 | [BE] PATCH /ho/templates/:id/archive | BE | 2 | Sprint 3 | Backlog |
| T-17-04 | EPIC-06 | STORY-17 | [WIRE] Connect template list + archive | WIRE | 2 | Sprint 3 | Backlog |
| T-18-01 | EPIC-06 | STORY-18 | [FE] Template wizard Step 1: format/support selector | FE | 2 | Sprint 3 | Backlog |
| T-18-02 | EPIC-06 | STORY-18 | [FE] Template wizard Step 2: name + InDesign upload with progress | FE | 3 | Sprint 3 | Backlog |
| T-18-03 | EPIC-06 | STORY-18 | [FE] Upload success: display detected InDesign tags | FE | 3 | Sprint 3 | Backlog |
| T-18-04 | EPIC-06 | STORY-18 | [FE] Template wizard Step 3: tag-to-field mapping interface | FE | 5 | Sprint 3 | Backlog |
| T-18-05 | EPIC-06 | STORY-18 | [FE] Template wizard Step 4: summary review + Create CTA | FE | 3 | Sprint 3 | Backlog |
| T-18-06 | EPIC-06 | STORY-18 | [FE] Template created: PDF generation started feedback notification | FE | 2 | Sprint 3 | Backlog |
| T-18-07 | EPIC-06 | STORY-18 | [BE] POST /ho/templates/upload — parse InDesign, extract variable tags | BE | 8 | Sprint 3 | Backlog |
| T-18-08 | EPIC-06 | STORY-18 | [BE] POST /ho/templates — create template, queue async PDF generation | BE | 8 | Sprint 3 | Backlog |
| T-18-09 | EPIC-06 | STORY-18 | [BE] Background worker: per-store PDF generation from template | BE | 13 | Sprint 3 | Backlog |
| T-18-10 | EPIC-06 | STORY-18 | [WIRE] Orchestrate 4-step wizard: step state management, file upload, tag detection response | WIRE | 5 | Sprint 3 | Backlog |
| T-18-11 | EPIC-06 | STORY-18 | [WIRE] Connect final submission to template creation API | WIRE | 3 | Sprint 3 | Backlog |
| T-20-01 | EPIC-07 | STORY-20 | [FE] HO: Warehouse stock page — totals + product list with search/filter/export | FE | 5 | Sprint 3 | Backlog |
| T-20-02 | EPIC-07 | STORY-20 | [FE] HO: Stock page loading/empty/error UI states | FE | 2 | Sprint 3 | Backlog |
| T-20-03 | EPIC-07 | STORY-20 | [BE] GET /ho/stock | BE | 3 | Sprint 3 | Backlog |
| T-20-04 | EPIC-07 | STORY-20 | [WIRE] Connect stock page + CSV export | WIRE | 2 | Sprint 3 | Backlog |
| T-21-01 | EPIC-07 | STORY-21 | [FE] HO: Send Stock panel — store selector, product + quantity inputs, validation | FE | 5 | Sprint 3 | Backlog |
| T-21-02 | EPIC-07 | STORY-21 | [FE] HO: Send Stock confirmation + success/error feedback | FE | 2 | Sprint 3 | Backlog |
| T-21-03 | EPIC-07 | STORY-21 | [BE] POST /ho/stock/transfers — validate qty, create transfer record | BE | 5 | Sprint 3 | Backlog |
| T-21-04 | EPIC-07 | STORY-21 | [WIRE] Connect send stock panel to API | WIRE | 2 | Sprint 3 | Backlog |
| T-22-01 | EPIC-07 | STORY-22 | [FE] HO: Stock history — log table, filter by type + period, export | FE | 5 | Sprint 3 | Backlog |
| T-22-02 | EPIC-07 | STORY-22 | [BE] GET /ho/stock/history — paginated + filtered log + CSV export | BE | 3 | Sprint 3 | Backlog |
| T-22-03 | EPIC-07 | STORY-22 | [WIRE] Connect history page + filters + export | WIRE | 2 | Sprint 3 | Backlog |
| T-27-01 | EPIC-09 | STORY-27 | [FE] Mobile: Orders list — search, filter by status, loading/empty/error states | FE | 3 | Sprint 3 | Backlog |
| T-27-02 | EPIC-09 | STORY-27 | [FE] Mobile: Order detail — all fields + Duplicate Order button | FE | 3 | Sprint 3 | Backlog |
| T-27-03 | EPIC-09 | STORY-27 | [FE] Mobile: Edit Local Price modal | FE | 2 | Sprint 3 | Backlog |
| T-27-04 | EPIC-09 | STORY-27 | [BE] GET /mobile/orders — paginated + filtered | BE | 2 | Sprint 3 | Backlog |
| T-27-05 | EPIC-09 | STORY-27 | [BE] GET /mobile/orders/:id | BE | 1 | Sprint 3 | Backlog |
| T-27-06 | EPIC-09 | STORY-27 | [BE] POST /mobile/orders/:id/duplicate | BE | 3 | Sprint 3 | Backlog |
| T-27-07 | EPIC-09 | STORY-27 | [BE] PATCH /mobile/orders/:orderId/items/:itemId/price | BE | 2 | Sprint 3 | Backlog |
| T-27-08 | EPIC-09 | STORY-27 | [WIRE] Connect orders list + detail + duplicate + price edit | WIRE | 3 | Sprint 3 | Backlog |
| T-28-01 | EPIC-09 | STORY-28 | [FE] Mobile: Profile screen — user info + SEPA mandate status card | FE | 2 | Sprint 3 | Backlog |
| T-28-02 | EPIC-09 | STORY-28 | [FE] Mobile: Edit profile form + Stripe SEPA activation deep link | FE | 3 | Sprint 3 | Backlog |
| T-28-03 | EPIC-09 | STORY-28 | [BE] GET /mobile/profile — user profile + SEPA mandate status | BE | 2 | Sprint 3 | Backlog |
| T-28-04 | EPIC-09 | STORY-28 | [BE] PUT /mobile/profile — update user profile | BE | 2 | Sprint 3 | Backlog |
| T-28-05 | EPIC-09 | STORY-28 | [WIRE] Connect profile + edit form + Stripe session deep link | WIRE | 3 | Sprint 3 | Backlog |

---

## C. Sprint Summary

| Sprint | Total SP | FE Tasks | BE Tasks | WIRE Tasks |
|--------|----------|----------|----------|-----------|
| Sprint 1 | 74 SP | 20 SP | 26 SP | 18+10 SP |
| Sprint 2 | 79 SP | 35 SP | 26 SP | 16+2 SP |
| Sprint 3+ | ~224 SP | ~80 SP | ~90 SP | ~54 SP |
| **Total** | **~377 SP** | | | |
