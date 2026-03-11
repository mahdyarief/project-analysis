# NFA — Sprint Plan

> **Sprint Duration:** 2 weeks each
> **Team:** Assumed 2 FE devs + 2 BE devs + 1 PM + 1 QA
> **Velocity Target:** ~70 SP per sprint (conservative; accounts for setup overhead in S1)
> **Kanban Columns:** `Backlog` → `To Do` → `In Progress` → `QA` → `Done`

---

## 🏗️ SPRINT 1 — "Walking Skeleton"

**Goal:** By end of Sprint 1, a user can: authenticate into all 3 apps, the admin can manage Head Offices + basic data, and a store owner can browse the catalogue and manage their profile. The security and payment infrastructure is fully operational.

**Sprint 1 Focus:** Authentication, foundational data management, navigation shell, SEPA setup, basic CRUD operations.

**Target Velocity: 70–75 SP**

---

### Sprint 1 — Stories & Tasks

| Story | Layer | Task | SP | Dependency |
|-------|-------|------|----|-----------|
| **STORY-01 Admin Login** | `[FE]` | T-01-01: Login screen UI | 3 | — |
| | `[BE]` | T-01-02: POST /auth/admin/login | 3 | — |
| | `[WIRE]` | T-01-03: Connect login to API | 2 | T-01-01, T-01-02 |
| **STORY-02 HO Login** | `[FE]` | T-02-01: HO login screen | 3 | — |
| | `[FE]` | T-02-02: Forgot Password UI | 3 | T-02-01 |
| | `[BE]` | T-02-03: POST /auth/ho/login | 2 | — |
| | `[BE]` | T-02-04: POST /auth/ho/forgot-password | 3 | — |
| | `[BE]` | T-02-05: POST /auth/ho/reset-password | 2 | T-02-04 |
| | `[WIRE]` | T-02-06: Connect all HO auth flows | 3 | T-02-01, T-02-03 |
| **STORY-03 Mobile OTP Login** | `[FE]` | T-03-01: Email input screen | 2 | — |
| | `[FE]` | T-03-02: OTP entry screen | 3 | T-03-01 |
| | `[BE]` | T-03-03: POST /auth/mobile/request-otp | 3 | — |
| | `[BE]` | T-03-04: POST /auth/mobile/verify-otp | 2 | T-03-03 |
| | `[WIRE]` | T-03-05: Connect OTP flow | 3 | T-03-01, T-03-03 |
| **STORY-04 SEPA Setup** | `[FE]` | T-04-01: SEPA setup screen (Stripe SDK) | 5 | STORY-03 ✅ |
| | `[BE]` | T-04-02: POST /payments/sepa/setup | 8 | — |
| | `[WIRE]` | T-04-03: Connect Stripe SDK → SetupIntent | 5 | T-04-01, T-04-02 |
| **STORY-05 HO List (Admin)** | `[FE]` | T-05-01: HO list page | 3 | STORY-01 ✅ |
| | `[BE]` | T-05-02: GET /admin/head-offices | 3 | — |
| | `[WIRE]` | T-05-03: Connect + search/filter | 2 | T-05-01, T-05-02 |

**Sprint 1 Sub-total: ~74 SP** ✅

---

### Sprint 1 — Rationale

1. **Auth first (all apps):** Zero features work without login. All three apps need their auth flow in place before any other screen is useful.
2. **SEPA early:** Store owners can't place orders without a SEPA mandate. Stripe integration is complex (webhook setup, testing sandbox), so it must be de-risked in Sprint 1.
3. **HO List for Admin:** Gives admins a workable entry point — they can see and navigate to Head Offices, which validates the multi-tenant architecture.
4. **Scope discipline:** Template management, stock, complex catalogue is deferred to Sprint 2. Only the foundation is laid.

---

## 🚀 SPRINT 2 — "Value Delivery"

**Goal:** By end of Sprint 2, a store owner can browse the full catalogue on mobile and place a real order. Head Office managers can manage their stores, view stock, and use the full order workflow. Admins can manage products and suppliers.

**Sprint 2 Focus:** Core business workflows — store management, stock, orders, mobile catalogue + ordering, admin product/supplier management.

**Target Velocity: 70–80 SP**

---

### Sprint 2 — Stories & Tasks

| Story | Layer | Task | SP | Dependency |
|-------|-------|------|----|-----------|
| **STORY-06 HO Detail (Admin)** | `[FE]` | T-06-01: HO detail view | 2 | STORY-05 ✅ |
| | `[BE]` | T-06-02: GET /admin/head-offices/:id | 1 | — |
| | `[WIRE]` | T-06-03: Connect detail | 1 | T-06-01 |
| **STORY-07 Products (Admin)** | `[FE]` | T-07-01: Product list page | 3 | STORY-01 ✅ |
| | `[FE]` | T-07-02: Add/Edit product form | 5 | — |
| | `[BE]` | T-07-03: GET /admin/products | 2 | — |
| | `[BE]` | T-07-04: POST /admin/products | 3 | — |
| | `[BE]` | T-07-05: PUT /admin/products/:id | 2 | T-07-04 |
| | `[WIRE]` | T-07-06: Connect product CRUD | 3 | T-07-01, T-07-03 |
| **STORY-12 Store List (HO)** | `[FE]` | T-12-01: Stores list page | 3 | STORY-02 ✅ |
| | `[FE]` | T-12-02: Empty state | 1 | — |
| | `[BE]` | T-12-03: GET /ho/stores | 2 | — |
| | `[WIRE]` | T-12-04: Connect store list | 2 | T-12-01 |
| **STORY-13 Store Create (HO)** | `[FE]` | T-13-01: Store creation form | 5 | STORY-12 ✅ |
| | `[BE]` | T-13-02: POST /ho/stores | 3 | — |
| | `[WIRE]` | T-13-03: Connect creation form | 2 | T-13-01 |
| **STORY-25 Mobile Catalogue** | `[FE]` | T-25-01: Catalogue screen | 5 | STORY-03 ✅ |
| | `[FE]` | T-25-02: Product detail screen | 5 | T-25-01 |
| | `[BE]` | T-25-03: GET /mobile/catalogue | 2 | STORY-07 ✅ |
| | `[BE]` | T-25-04: GET /mobile/catalogue/:id | 2 | — |
| | `[WIRE]` | T-25-05: Connect catalogue to API | 3 | T-25-01, T-25-03 |
| **STORY-26 Mobile Cart & Order** | `[FE]` | T-26-01: Cart screen | 3 | STORY-25 ✅ |
| | `[FE]` | T-26-02: Order confirmation screen | 3 | T-26-01 |
| | `[BE]` | T-26-03: GET /mobile/cart | 1 | — |
| | `[BE]` | T-26-04: PUT /mobile/cart | 2 | — |
| | `[BE]` | T-26-05: POST /mobile/orders (SEPA charge) | 8 | STORY-04 ✅ |
| | `[WIRE]` | T-26-06: Connect cart → order flow | 5 | T-26-01, T-26-05 |

**Sprint 2 Sub-total: ~79 SP** ✅

---

### Sprint 2 — Rationale

1. **Store Management before Ordering:** Stores must exist in the system before stock or mobile orders can be processed — store creation comes first in Sprint 2.
2. **Product Management (Admin) before Mobile Catalogue:** The mobile catalogue queries products managed by admins — the master data must exist first.
3. **Mobile Catalogue + Cart are the revenue engine:** This is the sprint's hero deliverable. A store owner can browse, add to cart, and pay via SEPA for the first time.
4. **Deferred to Sprint 3+:** Template management (complex), stock movement history, dashboard analytics, full order management, HO cart — these require the foundational data established in S1 and S2.

---

## 🗓️ Sprint Timeline Overview

```
Week 1-2  → SPRINT 1 — Walking Skeleton
             ✅ Auth (Admin, HO, Mobile OTP)
             ✅ SEPA Setup (Stripe)
             ✅ Admin: HO List
             → QA & Review

Week 3-4  → SPRINT 2 — Value Delivery
             ✅ Admin: Products + Suppliers
             ✅ HO: Store List + Create
             ✅ Mobile: Catalogue + Cart + Order
             → QA & Review

Sprint 3+  → (Out of current scope)
             Template Wizard & PDF Generation
             Stock Management
             Dashboard & Analytics
             Full Order Management (HO)
             Mobile: Orders History, Profile
```

---

## 📊 Sprint Velocity Summary

| Sprint | SP Target | Stories In Scope |
|--------|-----------|-----------------|
| Sprint 1 | ~74 SP | STORY-01, 02, 03, 04, 05 |
| Sprint 2 | ~79 SP | STORY-06, 07, 12, 13, 25, 26 |
| Sprint 3+ | ~224 SP | All remaining stories |
