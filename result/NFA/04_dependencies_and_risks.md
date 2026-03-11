# Dependencies & Risk Register: NFA Project

## 🔗 Task Dependencies
The execution plan assumes a rigid "Backend First" approach. The Frontend cannot properly hydrate or implement complex state without the API contracts.

### Sprint 1 Dependencies
*   `[FE] Admin Login UI` is **Blocked By** `[BE] Setup JWT Authentication Service`.
*   `[FE] Mobile Login UI (OTP)` is **Blocked By** `[BE] Implement SendGrid OTP generation API`.
*   `[FE] Admin Layout & Head Office Table` is **Blocked By** `[BE] Develop CRUD endpoints for Head Offices`.
*   `[WIRE]` tasks universally depend on both the corresponding `[FE]` UI and `[BE]` API being marked "Done" and deployed to staging.

### Sprint 2 Dependencies
*   `[FE] HO Dashboard KPI UI` is **Blocked By** `[BE] Dashboard aggregated KPI SQL endpoints`.
*   `[FE] Stripe Bank Checkout Flow` is **Blocked By** the `[BE] Stripe hooks and Cart Sub-Total Engine`.

---

## ⚠️ Known Risks & Blockers

| Risk Level | Category | Description | Mitigation Strategy |
|------------|----------|-------------|---------------------|
| **CRITICAL** | Technical | **InDesign Template Parsing**. Rebuilding a custom `.indd` parser is historically prone to massive edge-case failures. Doing it from scratch could derail the timeline. | *Mitigation:* We have pushed Epic 5 to the general Backlog. Spike a third-party service (e.g., PrintOS or active-PDF) early to offload processing workload. |
| **HIGH** | Financial | **SEPA Mandate Timelines**. Stripe SEPA Direct Debits require explicit micro-deposit verifications that can take up to 14 days. | *Mitigation:* Ensure the Mobile App Profile specifically warns Store Managers of this delay during onboarding, or allow "Credit-based" ordering in the interim. |
| **MEDIUM** | Security | **Admin Credential Rotation**. Figma UX rules explicitly forbid a "Forgot Password" UI for Super Admin personas. | *Mitigation:* Provisioning and rotating Admin keys must be handled via direct Database patches or a secure secondary CLI script. |
| **LOW** | Operational | **Mobile SDK Over-engineering**. Both Web and Mobile teams working synchronously could lead to duplicated business logic in FE states. | *Mitigation:* Ensure the backend strictly handles computations (like Cart Totals). The mobile app must remain a "dumb client" to stay in sync with Web apps. |
