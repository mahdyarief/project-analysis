# Kaptrain – CMS Subscriptions (Abonnements) Functional Requirements

## CMS – FR-020 Subscriptions Management
**Description**  
Allow CMS Administrators to manage subscription plans for users and coaches.

**Actor**  
Admin

**Priority**  
High

**Acceptance Criteria**
- Admin can view all available subscription plans.
- Subscriptions are grouped by target (Users, Coaches).
- Each subscription displays name, pricing, and capacity information.
- Admin can access actions to create or edit subscriptions.
- Displayed data reflects the latest stored state.

---

## CMS – FR-021 Create Subscription
**Description**  
Allow CMS Administrators to create a new subscription plan.

**Actor**  
Admin

**Priority**  
High

**Acceptance Criteria**
- Admin can initiate the subscription creation process.
- Admin must provide a subscription title.
- Admin can define pricing for the subscription:
  - Monthly price
  - Yearly price
- Admin can define athlete capacity limits.
- Admin can mark athlete capacity as unlimited.
- All required fields must be completed before creation.
- Given valid input, the system creates the subscription successfully.
- Newly created subscription appears in the subscriptions list.
- Admin can cancel subscription creation without saving.
- Errors prevent subscription creation.

---

## CMS – FR-022 Edit Subscription
**Description**  
Allow CMS Administrators to modify an existing subscription plan.

**Actor**  
Admin

**Priority**  
High

**Acceptance Criteria**
- Admin can initiate the edit process for a subscription.
- Existing subscription data is loaded for editing.
- Admin can update the subscription title.
- Admin can update pricing values.
- Admin can update athlete capacity settings.
- Given valid updates, the system saves changes successfully.
- Updated subscription data is reflected in the subscriptions list.
- Admin can cancel editing without saving changes.
- Errors do not overwrite existing subscription data.
