# Kaptrain CMS – Modèles de cycles d’entraînement (Library)

## CMS – FR-XXX View Training Cycle Models List

**Description**  
Allow Coaches to view the list of available training cycle models within the Library. Training cycle models are structured programs composed of multiple sessions over several weeks.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Coach can access the “Cycles d’entraînement” section from the Library.
- The system displays a list/grid of available cycle models.
- Each cycle card shows:
  - Cycle title
  - Short description
  - Total duration (in weeks)
  - Total number of sessions
- The list supports vertical scrolling.
- Empty state is displayed if no cycle models exist.

## CMS – FR-XXX Search Training Cycle Models

**Description**  
Allow Coaches to search training cycle models by title or keyword.

**Actor**  
Coach

**Priority**  
Medium

**Acceptance Criteria**

- Coach can enter text in the search input.
- The list updates dynamically based on the search query.
- Search matches cycle title and description.
- Clearing the search input restores the full list.

## CMS – FR-XXX Preview Training Cycle Model

**Description**  
Allow Coaches to preview the content of a training cycle model before using it.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Coach can click “Prévisualiser” on a cycle card.
- A preview panel or modal opens.
- Preview displays:
  - Cycle name
  - Description
  - Weekly structure
  - Sessions per week
- Coach can close the preview and return to the list.

## CMS – FR-XXX Create Training Cycle Model

**Description**  
Allow Coaches to create a new training cycle model from the Library.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Coach can click “Nouveau modèle”.
- A creation form is displayed.
- Coach can define:
  - Cycle name (required)
  - Description (optional)
  - Duration in weeks
  - Sessions per week
- Coach can save the cycle model.
- Newly created model appears in the list.

## CMS – FR-XXX Validate Required Fields When Creating Cycle

**Description**  
Ensure mandatory fields are validated when creating a training cycle model.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Cycle name is mandatory.
- Duration and session structure must be defined.
- System prevents saving if required fields are missing.
- Validation errors are clearly displayed.

## CMS – FR-XXX Persist Training Cycle Model

**Description**  
Ensure newly created training cycle models are persisted and reusable.

**Actor**  
System

**Priority**  
High

**Acceptance Criteria**

- Created cycle models are stored in the system.
- Models remain available after page reload.
- Models can be reused later for planning insertion.

## CMS – FR-XXX Display Cycle Metadata

**Description**  
Display metadata for each training cycle model to help Coaches choose appropriately.

**Actor**  
System

**Priority**  
Low

**Acceptance Criteria**

- Each cycle card displays:
  - Number of weeks
  - Number of sessions
- Metadata is consistent with cycle configuration.

## CMS – FR-XXX Access Control for Training Cycle Models

**Description**  
Ensure only Coaches can access and manage training cycle models.

**Actor**  
System

**Priority**  
High

**Acceptance Criteria**

- Only authenticated Coaches can view the “Cycles d’entraînement” section.
- Athletes cannot access or manage cycle models.
