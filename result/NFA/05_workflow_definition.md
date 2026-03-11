# NFA — Workflow Definition

---

## 1. Kanban Board Structure

```
┌──────────┐  ┌────────┐  ┌─────────────┐  ┌────────┐  ┌──────┐
│ BACKLOG  │→ │ TO DO  │→ │ IN PROGRESS │→ │   QA   │→ │ DONE │
└──────────┘  └────────┘  └─────────────┘  └────────┘  └──────┘
```

| Column | Purpose | Who Manages |
|--------|---------|-------------|
| **Backlog** | All planned stories not yet started | PM |
| **To Do** | Stories committed to the current sprint — ready to pick up | Dev Team |
| **In Progress** | Actively being developed | Developer |
| **QA** | Code done, deployed to Staging, awaiting testing | QA Engineer |
| **Done** | QA passed, PO approved, merged to main | PM / PO |

---

## 2. Task Flow Rules

### From Backlog → To Do
- PM moves stories from Backlog to **To Do** at Sprint Planning
- Story must have: title, description, acceptance criteria, story points, layer tag, sprint assignment
- Only stories with all fields filled can be moved to **To Do**

### From To Do → In Progress
- Developer picks up the task and self-assigns
- Developer creates a feature branch: `feature/STORY-XX-short-description`
- Developer updates Jira ticket: assigns themselves, moves to **In Progress**, adds start date

### From In Progress → QA
A developer moves a task to **QA** ONLY when ALL of the following are true:
1. ✅ Feature branch code is complete and self-reviewed
2. ✅ Unit tests written and passing locally
3. ✅ Code PR submitted and peer reviewed (at least 1 approval)
4. ✅ Feature branch merged into the **`staging`** branch
5. ✅ Code successfully deployed to the **Staging environment**
6. ✅ Jira ticket updated with:
   - "Testing Steps" or "Acceptance Criteria" filled in the ticket
   - Link to the Staging URL/screen to test
   - Any test accounts or credentials needed

> ❌ "Works on my machine" is NOT acceptable as a reason to move to QA.

### From QA → Done
QA Engineer moves a task to **Done** ONLY when ALL of the following are true:
1. ✅ All acceptance criteria verified against Figma/spec
2. ✅ All high/critical bugs filed and resolved
3. ✅ Product Owner (or Proxy) has reviewed and signed off
4. ✅ Feature branch **merged into `main`**
5. ✅ Successfully deployed to **Production** (or tagged for next release)

---

## 3. Definition of "Ready for QA"

A ticket is **Ready for QA** when:

- [ ] The feature is deployed to the **Staging environment** (not just local)
- [ ] The QA engineer can access the Staging environment without help from the developer
- [ ] The Jira ticket contains **step-by-step testing instructions**
- [ ] All required **test data is pre-seeded** (test user accounts, test products, test SEPA IBAN)
- [ ] Any **feature flags** required to enable the feature are toggled ON in Staging
- [ ] The **API layer** (BE) is returning correct responses for all expected inputs

---

## 4. Definition of "Done"

A ticket is **Done** when:

- [ ] **QA verified**: QA engineer has confirmed all acceptance criteria are met
- [ ] **Bug-free**: No High or Critical bugs are open against this story
- [ ] **PO sign-off**: Product Owner (or PM acting as proxy) has approved the feature
- [ ] **Merged to main**: The feature's PR is successfully merged to the `main` branch
- [ ] **Production deployed**: The feature is live in the production environment (or included in the next release tag)
- [ ] **Jira ticket closed**: Ticket status set to Done, resolution date recorded

---

## 5. Bug Severity Definitions (for QA)

| Severity | Definition | Action |
|----------|-----------|--------|
| 🔴 **Critical** | App crashes, data loss, security vulnerability, payment failure | Block story — must fix before Done |
| 🟠 **High** | Core functionality broken (can't login, can't place order), major UX broken | Block story — must fix before Done |
| 🟡 **Medium** | Feature partially works with workaround available | Fix in current sprint if time allows; otherwise next sprint |
| 🟢 **Low** | Minor cosmetic issue, typo, non-critical UX polish | Create backlog item; not a blocker for Done |

---

## 6. Layer-Specific Workflow Notes

### Frontend (FE) Tasks
- All FE tasks must match the **Figma spec**: layout, spacing, color, loading states, empty states, error states
- FE is not blocked by BE being ready — use **mock data / fixtures** to develop FE components
- FE code review checklist: responsive layout, accessibility (WCAG AA), no console errors, loading states handled

### Backend (BE) Tasks
- All BE tasks must have **unit tests** covering happy path + at least 2 edge cases
- API must follow contract defined in the **API Spec doc** (to be created in Sprint 0)
- BE tasks that touch payments (Stripe) require **webhook testing** before moving to QA

### Wiring (WIRE) Tasks
- Wiring tasks begin only when both FE and BE tasks are in **QA or Done**
- Wiring task scope: connecting API calls, handling auth headers, managing loading/error states end-to-end
- Wiring QA requires **E2E testing** on Staging — not just unit or component tests

---

## 7. Sprint Ceremony Schedule

| Ceremony | Frequency | Duration | Owner |
|----------|-----------|----------|-------|
| Sprint Planning | Start of each sprint | 2h | PM |
| Daily Standup | Every day | 15 min | Team (async OK) |
| Sprint Review | End of each sprint | 1h | PM + PO |
| Sprint Retrospective | End of each sprint | 45 min | PM |
| Backlog Refinement | Mid-sprint | 1h | PM + Tech Lead |
