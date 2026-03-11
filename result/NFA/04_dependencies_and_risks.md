# NFA — Dependencies & Risk Register

---

## 1. Dependency Map

### Cross-Story Dependencies (Critical Path)

```
STORY-01 (Admin Login)
    └── STORY-05 (HO List)
    └── STORY-07 (Products)
    └── STORY-09 (Global Orders)
    └── STORY-10 (Admin Account)

STORY-02 (HO Login)
    └── STORY-11 (Dashboard)
    └── STORY-12 (Stores List)
        └── STORY-13 (Store Create)
        └── STORY-14 (Store Detail)
    └── STORY-15 (HO Account)
    └── STORY-16 (Catalogue)
    └── STORY-17 (Templates)
        └── STORY-18 (Template Wizard)
        └── STORY-19 (Template Detail)
    └── STORY-20 (Stock)
        └── STORY-21 (Send Stock)
        └── STORY-22 (Stock History)
    └── STORY-23 (Orders)
    └── STORY-24 (Cart)

STORY-03 (Mobile OTP)
    └── STORY-04 (SEPA Setup) [BLOCKING — must complete before first order]
        └── STORY-26 (Cart & Order Placement) [depends on SEPA mandate]
    └── STORY-25 (Catalogue) [can browse without SEPA, but can't order]
    └── STORY-27 (Orders History)
    └── STORY-28 (Profile)

STORY-07 (Admin Products) [admin defines master catalogue]
    └── STORY-16 (HO Catalogue) [HO catalogue queries admin products]
    └── STORY-25 (Mobile Catalogue) [mobile queries same products]
        └── STORY-26 (Mobile Cart & Orders)
```

---

### Explicit Dependency Table

| Dependent Story | Depends On | Type | Blocker Level |
|----------------|-----------|------|--------------|
| STORY-05 HO List (Admin) | STORY-01 Admin Login | Auth gate | 🔴 Hard |
| STORY-07 Products (Admin) | STORY-01 Admin Login | Auth gate | 🔴 Hard |
| STORY-12 Store List (HO) | STORY-02 HO Login | Auth gate | 🔴 Hard |
| STORY-13 Store Create | STORY-12 Store List | UX flow | 🟡 Soft |
| STORY-16 HO Catalogue | STORY-07 Admin Products | Data dependency | 🔴 Hard |
| STORY-18 Template Wizard | STORY-17 Template List | UX flow | 🟡 Soft |
| STORY-18 T-18-09 PDF Worker | STORY-18 T-18-07,08 Upload+Create | Technical | 🔴 Hard |
| STORY-21 Send Stock | STORY-12 Stores exist | Data dependency | 🔴 Hard |
| STORY-25 Mobile Catalogue | STORY-03 Mobile Login | Auth gate | 🔴 Hard |
| STORY-25 Mobile Catalogue | STORY-07 Admin Products | Data dependency | 🔴 Hard |
| STORY-26 Mobile Cart/Order | STORY-04 SEPA Setup | Payment gate | 🔴 Hard |
| STORY-26 Mobile Cart/Order | STORY-25 Mobile Catalogue | UX flow | 🔴 Hard |
| STORY-27 Mobile Orders | STORY-26 Order Placement | Data dependency | 🟡 Soft |
| STORY-28 Mobile Profile | STORY-04 SEPA Setup | Context | 🟡 Soft |
| STORY-23 HO Orders | STORY-26 Mobile Orders | Data (orders created by Mobile) | 🟡 Soft |

**Legend:** 🔴 Hard = cannot proceed without it · 🟡 Soft = can be developed in parallel, integration needed at end

---

## 2. Layer Dependencies

### Frontend → Backend Contracts

Before a WIRE task can start, **both** the FE component AND the BE endpoint must be ready:

| Feature | FE Ready When | BE Ready When | WIRE Can Start |
|---------|--------------|---------------|---------------|
| Admin Login | Login page UI complete | `/auth/admin/login` returns JWT | Both done |
| HO Login | HO login page UI complete | `/auth/ho/login` + reset endpoints | Both done |
| Mobile OTP | Email + OTP screens done | `/auth/mobile/request-otp` + `/verify-otp` | Both done |
| SEPA Setup | Stripe SDK integrated in FE | SetupIntent endpoint + webhooks ready | Both done |
| Mobile Catalogue | Catalogue screen + product detail | `/mobile/catalogue` endpoints | Both done |
| Mobile Cart | Cart screen complete | Cart CRUD + `/mobile/orders` | Both done |
| Template Upload | Wizard Steps 1-3 done | `/templates/upload` + tag extraction | Both done |

---

## 3. Risk Register

### 🔴 High Risks

| Risk ID | Risk | Impact | Probability | Mitigation |
|---------|------|--------|-------------|-----------|
| R-01 | **Stripe SEPA Sandbox Delays** — SEPA mandates require bank-level testing; Stripe sandbox may not simulate all edge cases accurately | High — blocks mobile ordering in Sprint 1 | High | Start Stripe sandbox setup on Day 1 of Sprint 1; use Stripe test IBAN numbers; involve payment team early |
| R-02 | **InDesign File Parser Failure** — custom InDesign tag extraction logic may fail on non-standard customer files | High — blocks entire template workflow | Medium | Build robust error handling + manual override UI; test with multiple InDesign templates; agree on supported IDML version |
| R-03 | **PDF Generation Queue Scalability** — async PDF generation for many stores simultaneously could overwhelm the queue | High — core platform feature | Medium | Implement rate limiting on job queue; add job priority system; load test before Sprint 3 |
| R-04 | **Multi-tenant Data Isolation Bug** — an HO seeing another HO's stores/orders would be a critical security issue | High — compliance risk | Low-Medium | Mandatory code review for all multi-tenant queries; row-level security in DB; penetration test before launch |

### 🟡 Medium Risks

| Risk ID | Risk | Impact | Probability | Mitigation |
|---------|------|--------|-------------|-----------|
| R-05 | **Mobile App Store Review** — if React Native, Apple/Google review may delay release | Medium — affects mobile delivery timeline | Medium | Submit to stores early; plan 2-week buffer |
| R-06 | **OTP Email Deliverability** — OTP emails going to spam blocks all mobile users | Medium — critical UX | Medium | Use dedicated transactional email service (SendGrid/Postmark); configure SPF/DKIM |
| R-07 | **SEPA Chargebacks** — store owners may dispute SEPA charges | Medium — financial exposure | Low | Implement detailed order receipts; email confirmations before charge |
| R-08 | **Local Price Variable Conflicts** — if multiple items have the same variable name, price edits could be ambiguous | Medium — data integrity | Low | Define clear unique key per item+variable; UI must show item context |

### 🟢 Low Risks

| Risk ID | Risk | Impact | Probability | Mitigation |
|---------|------|--------|-------------|-----------|
| R-09 | **Scope Creep from Template Variations** — HOs may request custom template types not in initial scope | Low | High | Lock template scope to current 4-step wizard; create backlog item for custom types |
| R-10 | **Admin Panel Browser Compatibility** — minimal risk since admin panels are typically Chrome/Edge only | Low | Low | Define supported browsers; add to QA checklist |

---

## 4. Cross-Sprint Blockers

### Sprint 1 Potential Blockers

| Blocker | Risk | Mitigation |
|---------|------|-----------|
| Stripe account not set up / sandbox keys not ready | 🔴 High — blocks STORY-04 entirely | Resolve on Day 1; PM to chase ops team |
| Email service (SMTP/SendGrid) not configured | 🟡 Medium — blocks OTP (STORY-03) and HO forgot password (STORY-02) | Use dev SMTP relay as fallback |
| JWT secret and refresh token strategy not agreed | 🟡 Medium — inconsistent auth across apps | Agree on auth architecture in Sprint 0 planning session |
| API base URL / domain not decided | 🟡 Medium — FE and Mobile can't configure API endpoints | Define staging/prod URLs in Day 1 setup |

### Sprint 2 Potential Blockers

| Blocker | Risk | Mitigation |
|---------|------|-----------|
| Admin products not populated in DB (no test data) | 🔴 High — mobile catalogue is empty; can't test ordering | Create seed script for test products in Sprint 1 |
| Stores not created before stock or order tests | 🟡 Medium — STORY-21 depends on stores existing | Create fixture stores via script or via Sprint 2 task T-12 |
| SEPA mandate not completing in test environment | 🔴 High — blocks STORY-26 entire order flow | Maintain mock/bypass mode for E2E testing |

---

## 5. Dependency Diagram (Text)

```
Sprint 1 Critical Path:
[DB/Infra Setup] → [JWT Auth Setup]
    ├── [Admin Login API] → [Admin Login UI] → [Admin App Shell]
    ├── [HO Login API] → [HO Login UI] → [HO App Shell]  
    └── [Mobile OTP API] → [Mobile OTP UI] → [Mobile App Shell]
                                                └── [SEPA API (Stripe)] → [SEPA UI] → [SEPA Active]

Sprint 2 Critical Path:
[Admin App Shell] → [Products API] → [Products UI]
                                    └── [HO Catalogue API] → [HO Catalogue UI]
                                    └── [Mobile Catalogue API] → [Mobile Catalogue UI]
                                                                └── [Mobile Cart API] → [Mobile Cart UI]
[HO App Shell] → [Stores API] → [Stores UI] → [Store Creation UI+API]
[SEPA Active] → [Mobile Order API] ← [Mobile Cart] → [Order Placed ✅]
```
