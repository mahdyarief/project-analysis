
# Kaptrain CMS – Mes informations – Functional Requirements

## Overview
The **Mes informations** page allows a Coach to manage their personal profile, account security, subscription visibility, and account lifecycle actions. This section is critical for identity management, billing transparency, and user autonomy.

---

## CMS – FR-XXX View Profile Information

**Description**  
Allow the Coach to view their personal and account-related information.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**
- Coach can view profile photo (avatar).
- Coach can view full name.
- Coach can view role and onboarding date.
- Coach can view personal information:
  - First name
  - Last name
  - Date of birth
  - Gender
  - Email address
  - Phone number
- Coach can view subscription plan details:
  - Plan name
  - Billing cycle
  - Monthly price
  - License usage (e.g. athletes used / available)
- Coach can access payment management via Stripe portal.

---

## CMS – FR-XXX Edit Personal Information

**Description**  
Allow the Coach to update their personal profile information.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**
- Coach can open the edit profile modal.
- Coach can update:
  - First name
  - Last name
  - Date of birth (day, month, year)
  - Gender
  - Email address
  - Phone number
- Validation is applied to required fields.
- Changes are saved only when the Coach confirms.
- Updated data is reflected immediately on the profile page.

---

## CMS – FR-XXX Change Profile Avatar

**Description**  
Allow the Coach to update their profile picture.

**Actor**  
Coach

**Priority**  
Medium

**Acceptance Criteria**
- Coach can open the avatar edit modal.
- Coach can upload an image file (JPG or PNG).
- Minimum image size requirements are enforced.
- Preview of the selected image is displayed.
- Coach can confirm or cancel the upload.
- New avatar is displayed after successful update.

---

## CMS – FR-XXX Reset Password

**Description**  
Allow the Coach to securely change their password.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**
- Coach can access the change password section.
- Coach must provide:
  - Current password
  - New password
  - Confirm new password
- New password must meet security rules.
- Confirmation password must match.
- Coach receives confirmation upon successful update.
- Invalid inputs display appropriate error messages.

---

## CMS – FR-XXX Delete Account

**Description**  
Allow the Coach to permanently delete their account.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**
- Coach can initiate account deletion.
- System displays a clear warning explaining consequences.
- Coach must explicitly confirm the deletion.
- Coach can cancel the action before confirmation.
- Upon confirmation:
  - Account is permanently deleted.
  - All associated data is removed.
  - Coach is logged out immediately.

---

## CMS – FR-XXX Manage Subscription & Payment

**Description**  
Allow the Coach to manage billing details via an external payment portal.

**Actor**  
Coach

**Priority**  
Medium

**Acceptance Criteria**
- Coach can access the Stripe customer portal.
- Coach can:
  - View invoices
  - Update payment method
  - Manage subscription plan
- All payment actions are handled securely outside the CMS.

---

## Notes
- All actions must comply with data protection and security standards.
- Destructive actions (password reset, account deletion) must require explicit confirmation.
- UI should clearly differentiate editable vs read-only information.
