# Kaptrain CMS – Modèle de bloc d’entraînement  
Functional Requirements

## Overview
The *Modèle de bloc d’entraînement* feature allows coaches to create, manage, and reuse standardized training blocks. These blocks are designed to speed up program creation by encapsulating recurring training structures, exercises, and intensity parameters.

This module is accessible from **Bibliothèque > Blocs d’entraînement**.

---

## CMS – FR-XXX View Training Block Models List

**Description**  
Allow Coaches to view all existing training block models in a structured list.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**
- The system displays a list of all training block models.
- Each block shows:
  - Block name
  - Short description or objective
  - Number of exercises included
- Blocks are displayed as cards.
- A search input allows filtering by block name or keyword.
- The list is paginated or lazily loaded if the dataset is large.

---

## CMS – FR-XXX Create Training Block Model

**Description**  
Allow Coaches to create a new training block model from scratch.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**
- Coach can click “Nouveau modèle”.
- A creation panel (sheet/modal) opens.
- Coach can define:
  - Block title (mandatory)
  - Block description
  - Training objective (e.g. endurance, strength, mobility)
- Coach can save the block.
- Newly created block appears in the list immediately.

---

## CMS – FR-XXX Edit Training Block Model

**Description**  
Allow Coaches to modify an existing training block model.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**
- Coach can open an existing block in edit mode.
- Coach can update:
  - Title
  - Description
  - Training parameters
- Changes are saved explicitly via a “Save” button.
- Updated information is reflected in the block list.

---

## CMS – FR-XXX Configure Training Parameters

**Description**  
Allow Coaches to define detailed training parameters inside a block.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**
- Coach can define training metrics such as:
  - Intensity reference (e.g. VMA, FTP)
  - Zone (Z1–Z5)
  - Duration or distance
  - Number of series and repetitions
- Coach can switch between Time / Distance / Zone modes.
- Parameters are validated before saving.

---

## CMS – FR-XXX Manage Intervals

**Description**  
Allow Coaches to add and manage interval structures inside a training block.

**Actor**  
Coach

**Priority**  
Medium

**Acceptance Criteria**
- Coach can add one or multiple intervals.
- Each interval can define:
  - Work duration
  - Recovery duration
  - Intensity zone
- Coach can reorder or remove intervals.
- The interval structure is visually clear and readable.

---

## CMS – FR-XXX Associate Exercises to Block

**Description**  
Allow Coaches to associate exercises from the library to a training block.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**
- Coach can add exercises via “Ajouter des exercices”.
- Exercises are selected from the exercise library.
- Multiple exercises can be added.
- Added exercises are displayed as cards with thumbnails.
- Coach can remove an exercise from the block.

---

## CMS – FR-XXX Delete Training Block Model

**Description**  
Allow Coaches to delete an existing training block model.

**Actor**  
Coach

**Priority**  
Medium

**Acceptance Criteria**
- Coach can initiate deletion from the edit panel.
- A confirmation dialog is required.
- Upon confirmation, the block is permanently removed.
- Deleted block no longer appears in the list.

---

## CMS – FR-XXX Reuse Training Block in Programs

**Description**  
Allow Coaches to reuse training block models when building programs or cycles.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**
- Training blocks are selectable when creating sessions or cycles.
- Selected block auto-populates exercises and parameters.
- Coach can override values after insertion without modifying the original model.

---

## Non-Functional Requirements

- UI must remain responsive on desktop and tablet.
- Editing actions must not affect other blocks unintentionally.
- Data persistence must be reliable with autosave protection against accidental closure.

---

## Dependencies

- Exercise Library
- Training Cycles
- Session Builder
