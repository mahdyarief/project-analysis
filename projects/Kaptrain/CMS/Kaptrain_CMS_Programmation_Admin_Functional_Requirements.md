# Programmation (Admin) – Functional Requirements

## Scope
This document describes the **Admin-only Programmation features** in Kaptrain, covering:
- Programmations management
- Programmes management
- Creation and edition flows

---

## CMS – FR-XXX List Programmations (Admin)

**Description**  
Allow Admin users to view and manage all programmations created in the system.

**Actor**  
Admin

**Priority**  
High

**Acceptance Criteria**
- Admin can view a list of all programmations.
- Each programmation displays:
  - Cover image
  - Title
  - Target level
  - Description
  - Number of subscribers
  - Creation date
  - Last consultation date
- Admin can access actions:
  - View programmation
  - Edit programmation

---

## CMS – FR-XXX Create a Programmation (Admin)

**Description**  
Allow Admin to create a new programmation.

**Actor**  
Admin

**Priority**  
High

**Acceptance Criteria**
- Admin can open the creation modal from the list.
- Admin must provide:
  - Title
  - Description
  - Target level (Beginner, Intermediate, Confirmed, All)
  - Monthly price
  - Cover image
- Admin can save the programmation.
- Newly created programmation appears in the list.

---

## CMS – FR-XXX List Programmes (Admin)

**Description**  
Allow Admin to manage all training programmes.

**Actor**  
Admin

**Priority**  
High

**Acceptance Criteria**
- Admin can view all programmes.
- Each programme displays:
  - Cover image
  - Programme title
  - Target level
  - Description
  - Number of subscribers
- Admin can access:
  - View programme
  - Edit programme

---

## CMS – FR-XXX Create a Programme (Admin)

**Description**  
Allow Admin to create a new programme.

**Actor**  
Admin

**Priority**  
High

**Acceptance Criteria**
- Admin can open the programme creation modal.
- Admin must provide:
  - Programme title
  - Description
  - Target level
  - Price
  - Cover image
- Admin can save the programme.
- Programme becomes available for programmations.

---

## CMS – FR-XXX Edit a Programme (Admin)

**Description**  
Allow Admin to edit an existing programme.

**Actor**  
Admin

**Priority**  
Medium

**Acceptance Criteria**
- Admin can update:
  - Title
  - Description
  - Level
  - Price
  - Cover image
- Changes are saved immediately.
- Updated data is reflected across all views.
