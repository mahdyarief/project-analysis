# Kaptrain – CMS Coach Subscription Management Functional Requirements

## CMS – FR-034 Manage Subscription
**Description**  
Allow Coaches to view, manage, and upgrade their own subscription plan based on available offerings.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**
- Coach can access the subscription management page.
- The system displays the current active subscription plan for the Coach.
- The system displays available subscription plans.
- Subscription plans display pricing information for monthly and yearly billing.
- The system highlights the current active plan.
- The system indicates the most recommended or popular plan when applicable.

---

## CMS – FR-035 Change Subscription Plan
**Description**  
Allow Coaches to change or upgrade their subscription plan.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**
- Coach can switch between monthly and yearly billing options.
- Coach can select a different subscription plan.
- The system displays pricing differences when changing plans.
- Coach can confirm a subscription change.
- Upon confirmation, the subscription is updated successfully.
- The updated subscription takes effect according to billing rules.
- The system displays a confirmation after a successful change.

---

## CMS – FR-036 Subscription Constraints
**Description**  
Define functional constraints and limitations related to Coach subscription plans.

**Actor**  
Coach

**Priority**  
Medium

**Acceptance Criteria**
- The system enforces athlete capacity limits based on the active subscription.
- If a subscription includes unlimited capacity, no athlete limit is applied.
- Features available to the Coach are restricted according to the active subscription plan.
- Subscription restrictions are applied immediately after plan changes.

---

## CMS – FR-037 Contact for Custom Plans
**Description**  
Allow Coaches to request a custom subscription plan when standard plans do not meet their needs.

**Actor**  
Coach

**Priority**  
Low

**Acceptance Criteria**
- Coach can initiate a request for a custom subscription plan.
- The system provides a way to contact the platform for custom subscription inquiries.
