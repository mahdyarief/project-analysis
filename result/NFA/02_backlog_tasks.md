# NFA — Full Backlog: Tasks split by FE / BE / Wiring

> **Format:** `[LAYER] Task Title` — Story Point
> **Layers:** `[FE]` Frontend · `[BE]` Backend · `[WIRE]` Wiring/Integration
> **Estimation:** Fibonacci (1, 2, 3, 5, 8, 13)

---

## EPIC-01 · Authentication & Access Control

### STORY-01 · Admin Panel Login (Email + Password)

| # | Layer | Task | SP |
|---|-------|------|----|
| T-01-01 | `[FE]` | Build login screen: email/password form, error states (invalid credentials, server error), loading state | 3 |
| T-01-02 | `[BE]` | POST /auth/admin/login — validate credentials, return JWT + refresh token | 3 |
| T-01-03 | `[WIRE]` | Connect login form to API: handle JWT storage, redirect on success, toast on error | 2 |

**Sub-total: 8 SP**

---

### STORY-02 · Head Office Login (Email + Password + Validation States)

| # | Layer | Task | SP |
|---|-------|------|----|
| T-02-01 | `[FE]` | Build HO login screen: form + field validation states + error/success feedback UI | 3 |
| T-02-02 | `[FE]` | Build "Forgot Password" flow: email input → confirmation screen | 3 |
| T-02-03 | `[BE]` | POST /auth/ho/login — validate credentials, return JWT + refresh token | 2 |
| T-02-04 | `[BE]` | POST /auth/ho/forgot-password — send password reset email with token | 3 |
| T-02-05 | `[BE]` | POST /auth/ho/reset-password — validate token, update password | 2 |
| T-02-06 | `[WIRE]` | Connect HO login + forgot password forms to API; handle all response states | 3 |

**Sub-total: 16 SP**

---

### STORY-03 · Mobile App Login (OTP / Passwordless)

| # | Layer | Task | SP |
|---|-------|------|----|
| T-03-01 | `[FE]` | Build mobile login screen: email input form + "Send OTP" CTA | 2 |
| T-03-02 | `[FE]` | Build OTP entry screen: 6-digit input, resend timer, error/success states | 3 |
| T-03-03 | `[BE]` | POST /auth/mobile/request-otp — generate & email OTP (TTL: 5 min) | 3 |
| T-03-04 | `[BE]` | POST /auth/mobile/verify-otp — validate OTP, return JWT + refresh token | 2 |
| T-03-05 | `[WIRE]` | Connect email → OTP screens to API; manage JWT in secure storage; redirect to SEPA setup if first login | 3 |

**Sub-total: 13 SP**

---

### STORY-04 · Mobile App — First-Time SEPA Setup

| # | Layer | Task | SP |
|---|-------|------|----|
| T-04-01 | `[FE]` | Build SEPA mandate setup screen: Stripe.js/Stripe SDK SEPA form, confirmation screen | 5 |
| T-04-02 | `[BE]` | POST /payments/sepa/setup — create Stripe SetupIntent for SEPA; webhooks for mandate confirmation | 8 |
| T-04-03 | `[WIRE]` | Connect Stripe SDK to SetupIntent flow; handle mandate success/error; gate catalogue access | 5 |

**Sub-total: 18 SP**

---

## EPIC-02 · Admin Panel — Network (Head Office) Management

### STORY-05 · Head Office List

| # | Layer | Task | SP |
|---|-------|------|----|
| T-05-01 | `[FE]` | Build HO list page: data table, search input, country filter dropdown, loading/empty states | 3 |
| T-05-02 | `[BE]` | GET /admin/head-offices — paginated list with search + country filter query params | 3 |
| T-05-03 | `[WIRE]` | Connect list page to API; implement search debounce + filter; navigate to HO environment | 2 |

**Sub-total: 8 SP**

---

### STORY-06 · Head Office Detail

| # | Layer | Task | SP |
|---|-------|------|----|
| T-06-01 | `[FE]` | Build HO detail view/drawer: display all HO info fields | 2 |
| T-06-02 | `[BE]` | GET /admin/head-offices/:id — return full HO record | 1 |
| T-06-03 | `[WIRE]` | Connect detail view to API | 1 |

**Sub-total: 4 SP**

---

## EPIC-03 · Admin Panel — Product, Supplier & Order Management

### STORY-07 · Product Management (Admin)

| # | Layer | Task | SP |
|---|-------|------|----|
| T-07-01 | `[FE]` | Build product list page: data table, search, filter (category, status), pagination | 3 |
| T-07-02 | `[FE]` | Build add/edit product form: all fields (name, SKU, image, price, variants), validation | 5 |
| T-07-03 | `[BE]` | GET /admin/products — paginated + filterable product list | 2 |
| T-07-04 | `[BE]` | POST /admin/products — create product with validation | 3 |
| T-07-05 | `[BE]` | PUT /admin/products/:id — update product | 2 |
| T-07-06 | `[WIRE]` | Connect product list + form to API; handle file uploads for images | 3 |

**Sub-total: 18 SP**

---

### STORY-08 · Supplier Management (Admin)

| # | Layer | Task | SP |
|---|-------|------|----|
| T-08-01 | `[FE]` | Build supplier list: search, country filter, paginated table | 3 |
| T-08-02 | `[FE]` | Build supplier create/edit form: all fields + validation | 3 |
| T-08-03 | `[BE]` | GET /admin/suppliers — paginated + filterable | 2 |
| T-08-04 | `[BE]` | POST + PUT /admin/suppliers — create/update supplier | 3 |
| T-08-05 | `[WIRE]` | Connect forms + list to API | 2 |

**Sub-total: 13 SP**

---

### STORY-09 · Global Orders View (Admin)

| # | Layer | Task | SP |
|---|-------|------|----|
| T-09-01 | `[FE]` | Build global orders page: list table with filters (HO, status, date), pagination | 3 |
| T-09-02 | `[FE]` | Build order detail view: all order info fields | 2 |
| T-09-03 | `[BE]` | GET /admin/orders — all orders across all HOs, paginated + filtered | 3 |
| T-09-04 | `[BE]` | GET /admin/orders/:id — order detail | 1 |
| T-09-05 | `[WIRE]` | Connect order list + detail to API | 2 |

**Sub-total: 11 SP**

---

### STORY-10 · Admin Account Management

| # | Layer | Task | SP |
|---|-------|------|----|
| T-10-01 | `[FE]` | Build account page: view profile, edit profile form | 2 |
| T-10-02 | `[BE]` | GET + PUT /admin/account — fetch and update profile | 2 |
| T-10-03 | `[WIRE]` | Connect to API; handle update success/error | 1 |

**Sub-total: 5 SP**

---

## EPIC-04 · Head Office — Dashboard & Analytics

### STORY-11 · KPI Dashboard

| # | Layer | Task | SP |
|---|-------|------|----|
| T-11-01 | `[FE]` | Build dashboard page: KPI cards, network overview widgets, responsive layout | 5 |
| T-11-02 | `[FE]` | Build "Orders with Issues" block: list with status badges and quick-action links | 3 |
| T-11-03 | `[BE]` | GET /ho/dashboard/kpis — aggregate KPI data (orders, revenue, stores) | 5 |
| T-11-04 | `[BE]` | GET /ho/dashboard/orders-with-issues — list problematic orders with reasons | 3 |
| T-11-05 | `[WIRE]` | Connect dashboard components to APIs; implement auto-refresh (polling or SSE) | 3 |

**Sub-total: 19 SP**

---

## EPIC-05 · Head Office — Store Network Management

### STORY-12 · Store List

| # | Layer | Task | SP |
|---|-------|------|----|
| T-12-01 | `[FE]` | Build stores list: search, filter, paginated table with key info columns + actions | 3 |
| T-12-02 | `[FE]` | Build empty state screen (no stores yet) | 1 |
| T-12-03 | `[BE]` | GET /ho/stores — paginated + filterable store list | 2 |
| T-12-04 | `[WIRE]` | Connect store list to API | 2 |

**Sub-total: 8 SP**

---

### STORY-13 · Store Creation

| # | Layer | Task | SP |
|---|-------|------|----|
| T-13-01 | `[FE]` | Build store creation form: general info section, legal info section, addresses section, multi-section validation | 5 |
| T-13-02 | `[BE]` | POST /ho/stores — create store with full validation; auto-link to current HO | 3 |
| T-13-03 | `[WIRE]` | Connect creation form to API; handle success (navigate to store detail) / error | 2 |

**Sub-total: 10 SP**

---

### STORY-14 · Store Detail View

| # | Layer | Task | SP |
|---|-------|------|----|
| T-14-01 | `[FE]` | Build store detail drawer/page: info tab, compliance tab, activity tab | 5 |
| T-14-02 | `[BE]` | GET /ho/stores/:id — full store record with compliance and activity | 3 |
| T-14-03 | `[WIRE]` | Connect detail view to API; implement tab switching | 2 |

**Sub-total: 10 SP**

---

### STORY-15 · HO Account & User Management

| # | Layer | Task | SP |
|---|-------|------|----|
| T-15-01 | `[FE]` | Build account page: HO info display, user list table | 3 |
| T-15-02 | `[FE]` | Build user edit form/drawer | 2 |
| T-15-03 | `[BE]` | GET /ho/account — HO details + users list | 2 |
| T-15-04 | `[BE]` | PUT /ho/users/:id — update user info | 2 |
| T-15-05 | `[WIRE]` | Connect account page and user edit form to API | 2 |

**Sub-total: 11 SP**

---

## EPIC-06 · Head Office — Catalogue & Template Management

### STORY-16 · Product Catalogue (HO)

| # | Layer | Task | SP |
|---|-------|------|----|
| T-16-01 | `[FE]` | Build catalogue page: product grid/list, loading state, empty state, error state | 3 |
| T-16-02 | `[FE]` | Build filter/search bar: category, type (template/standard), text search | 2 |
| T-16-03 | `[BE]` | GET /ho/catalogue — return products available to this HO (templates + standards) | 2 |
| T-16-04 | `[WIRE]` | Connect catalogue to API | 1 |

**Sub-total: 8 SP**

---

### STORY-17 · Template List & Archive

| # | Layer | Task | SP |
|---|-------|------|----|
| T-17-01 | `[FE]` | Build template list page: loading/empty/populated states, archive action with confirmation modal | 3 |
| T-17-02 | `[BE]` | GET /ho/templates — paginated template list with status | 2 |
| T-17-03 | `[BE]` | PATCH /ho/templates/:id/archive — archive template, stop PDF generation | 2 |
| T-17-04 | `[WIRE]` | Connect template list + archive action to API | 2 |

**Sub-total: 9 SP**

---

### STORY-18 · Template Creation Wizard (4-Step)

| # | Layer | Task | SP |
|---|-------|------|----|
| T-18-01 | `[FE]` | Step 1 UI: format/support selector (card-based selection) | 2 |
| T-18-02 | `[FE]` | Step 2 UI: template name input + InDesign file upload with progress | 3 |
| T-18-03 | `[FE]` | Upload success screen: display detected InDesign tags list | 3 |
| T-18-04 | `[FE]` | Step 3 UI: tag-to-system-field mapping interface (dropdown per detected tag) | 5 |
| T-18-05 | `[FE]` | Step 4 UI: summary review (name, product, variable mapping) + "Create" CTA | 3 |
| T-18-06 | `[FE]` | Template created success feedback: "PDF generation started in background" notification | 2 |
| T-18-07 | `[BE]` | POST /ho/templates/upload — receive InDesign file; parse + extract variable tags; return tag list | 8 |
| T-18-08 | `[BE]` | POST /ho/templates — create template record with mapping; queue async PDF generation job | 8 |
| T-18-09 | `[BE]` | Background worker: PDF generation per store using template + store data | 13 |
| T-18-10 | `[WIRE]` | Orchestrate 4-step wizard: manage step state, send files, handle tag detection response | 5 |
| T-18-11 | `[WIRE]` | Connect final submission to template creation API; navigate to template detail on success | 3 |

**Sub-total: 55 SP**

---

### STORY-19 · Template Detail View

| # | Layer | Task | SP |
|---|-------|------|----|
| T-19-01 | `[FE]` | Build template detail page: status, PDF generation progress per store, variable mapping display | 5 |
| T-19-02 | `[BE]` | GET /ho/templates/:id — template details + per-store PDF generation status | 3 |
| T-19-03 | `[WIRE]` | Connect detail page to API; implement real-time progress (polling or WebSocket) | 3 |

**Sub-total: 11 SP**

---

## EPIC-07 · Head Office — Stock & Inventory Management

### STORY-20 · Warehouse Stock View

| # | Layer | Task | SP |
|---|-------|------|----|
| T-20-01 | `[FE]` | Build stock page: total value header, unit count, product list table with search/filter/export | 5 |
| T-20-02 | `[FE]` | Build loading, empty, and error UI states for stock page | 2 |
| T-20-03 | `[BE]` | GET /ho/stock — warehouse stock summary + product list + totals | 3 |
| T-20-04 | `[WIRE]` | Connect stock page to API; implement CSV export | 2 |

**Sub-total: 12 SP**

---

### STORY-21 · Send Stock to Store

| # | Layer | Task | SP |
|---|-------|------|----|
| T-21-01 | `[FE]` | Build "Send Stock" panel/drawer: store selector dropdown, product + quantity inputs, validation | 5 |
| T-21-02 | `[FE]` | Build confirmation and success/error feedback screens | 2 |
| T-21-03 | `[BE]` | POST /ho/stock/transfers — validate available qty, create stock transfer record | 5 |
| T-21-04 | `[WIRE]` | Connect send stock panel to API; refresh stock view on success | 2 |

**Sub-total: 14 SP**

---

### STORY-22 · Stock Movement History

| # | Layer | Task | SP |
|---|-------|------|----|
| T-22-01 | `[FE]` | Build stock history tab/page: chronological log table, filter by type (in/out) + period, export button | 5 |
| T-22-02 | `[BE]` | GET /ho/stock/history — paginated movement log with filters + CSV export | 3 |
| T-22-03 | `[WIRE]` | Connect history page to API; implement date range filter + export | 2 |

**Sub-total: 10 SP**

---

## EPIC-08 · Head Office — Order Management

### STORY-23 · HO Order List

| # | Layer | Task | SP |
|---|-------|------|----|
| T-23-01 | `[FE]` | Build HO orders list: filter by store/status/date, loading/empty/error states | 3 |
| T-23-02 | `[FE]` | Build order detail view from HO perspective | 3 |
| T-23-03 | `[BE]` | GET /ho/orders — paginated order list for this HO's stores | 2 |
| T-23-04 | `[BE]` | GET /ho/orders/:id — full order detail | 1 |
| T-23-05 | `[WIRE]` | Connect order list + detail to API | 2 |

**Sub-total: 11 SP**

---

### STORY-24 · HO Cart (Order Review Before Confirmation)

| # | Layer | Task | SP |
|---|-------|------|----|
| T-24-01 | `[FE]` | Build cart page: empty state, filled state with item list, quantity adjusters, destination selector, subtotal/shipping/total summary | 5 |
| T-24-02 | `[FE]` | Build cart modification modal/drawer | 3 |
| T-24-03 | `[BE]` | GET /ho/cart — current cart state | 1 |
| T-24-04 | `[BE]` | PUT /ho/cart — update quantities, destinations | 3 |
| T-24-05 | `[WIRE]` | Connect cart page to API; real-time total recalculation | 3 |

**Sub-total: 15 SP**

---

## EPIC-09 · Mobile App — End-to-End Ordering

### STORY-25 · Mobile Catalogue Browse

| # | Layer | Task | SP |
|---|-------|------|----|
| T-25-01 | `[FE]` | Build catalogue screen: grid layout, search bar, filters (category, type), loading/empty/error states | 5 |
| T-25-02 | `[FE]` | Build product detail screen: images, fields, required inputs, "Add to Cart" CTA, error + retry states | 5 |
| T-25-03 | `[BE]` | GET /mobile/catalogue — product list available to this store | 2 |
| T-25-04 | `[BE]` | GET /mobile/catalogue/:id — product detail + available variants | 2 |
| T-25-05 | `[WIRE]` | Connect catalogue + product detail to API; pass store token for pricing | 3 |

**Sub-total: 17 SP**

---

### STORY-26 · Mobile Cart & Order Placement

| # | Layer | Task | SP |
|---|-------|------|----|
| T-26-01 | `[FE]` | Build cart screen: item list, quantity +/-, delete item, total display | 3 |
| T-26-02 | `[FE]` | Build order confirmation screen (SEPA): summary + "Confirm Order" CTA + success/error feedback | 3 |
| T-26-03 | `[BE]` | GET /mobile/cart — fetch current cart | 1 |
| T-26-04 | `[BE]` | PUT /mobile/cart — update cart items/quantities | 2 |
| T-26-05 | `[BE]` | POST /mobile/orders — create order, charge via SEPA SetupIntent | 8 |
| T-26-06 | `[WIRE]` | Connect cart → confirmation → success flow to API; handle SEPA charge response | 5 |

**Sub-total: 22 SP**

---

### STORY-27 · Mobile Orders List & Detail

| # | Layer | Task | SP |
|---|-------|------|----|
| T-27-01 | `[FE]` | Build orders list screen: search, filter by status, loading/empty/error states | 3 |
| T-27-02 | `[FE]` | Build order detail screen: all fields + "Duplicate Order" button | 3 |
| T-27-03 | `[FE]` | Build "Edit Local Price" modal: price input for a specific item variable | 2 |
| T-27-04 | `[BE]` | GET /mobile/orders — paginated + filtered order list for this store | 2 |
| T-27-05 | `[BE]` | GET /mobile/orders/:id — full order detail | 1 |
| T-27-06 | `[BE]` | POST /mobile/orders/:id/duplicate — clone order for re-order | 3 |
| T-27-07 | `[BE]` | PATCH /mobile/orders/:orderId/items/:itemId/price — update local price | 2 |
| T-27-08 | `[WIRE]` | Connect orders list + detail + duplicate + price edit to API | 3 |

**Sub-total: 19 SP**

---

### STORY-28 · Mobile Profile & SEPA Management

| # | Layer | Task | SP |
|---|-------|------|----|
| T-28-01 | `[FE]` | Build profile screen: display user info + SEPA mandate status card | 2 |
| T-28-02 | `[FE]` | Build edit profile form + navigate to Stripe SEPA activation | 3 |
| T-28-03 | `[BE]` | GET /mobile/profile — user profile + SEPA mandate status from Stripe | 2 |
| T-28-04 | `[BE]` | PUT /mobile/profile — update user profile | 2 |
| T-28-05 | `[WIRE]` | Connect profile page + edit form + deep link to Stripe session | 3 |

**Sub-total: 12 SP**

---

## 📊 Backlog Summary by Epic

| Epic | Stories | Total SP | FE SP | BE SP | Wire SP |
|------|---------|----------|-------|-------|---------|
| EPIC-01 Auth | 4 | 55 | 16 | 18 | 13+8 |
| EPIC-02 Admin Network | 2 | 12 | 5 | 4 | 3 |
| EPIC-03 Admin Products/Suppliers/Orders | 4 | 47 | 18 | 14 | 8 |
| EPIC-04 HO Dashboard | 1 | 19 | 8 | 8 | 3 |
| EPIC-05 HO Stores | 4 | 29 | 16 | 10 | 6 |
| EPIC-06 HO Catalogue/Templates | 4 | 83 | 26 | 38 | 11+8 |
| EPIC-07 HO Stock | 3 | 36 | 14 | 11 | 6 |
| EPIC-08 HO Orders/Cart | 2 | 26 | 14 | 7 | 5 |
| EPIC-09 Mobile | 4 | 70 | 26 | 25 | 14+5 |
| **TOTAL** | **28** | **~377 SP** | | | |

> ⚠️ Note: 377 SP is the full product scope. Sprint planning covers the first 2 sprints (~140 SP at 70 SP/sprint with a 2-week cadence).
