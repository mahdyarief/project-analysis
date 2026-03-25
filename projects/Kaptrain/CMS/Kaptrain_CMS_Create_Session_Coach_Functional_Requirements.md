# Kaptrain CMS – Planning – Create Session (Coach) – Functional Requirements

## CMS – FR-066 Open Create Session Panel

**Description**  
Allow Coaches to open the “Create a session” panel from planning (week or month) to create a new session for an athlete.


**Actor**  
Coach


**Priority**  
High


**Acceptance Criteria**
- Coach can click “Add a session” from the planning view.
- A side panel opens with a session creation form.
- Coach can close the panel to cancel creation; no session is created unless saved.

---

## CMS – FR-067 Assign Theme(s) and/or Sport(s) to the Session

**Description**  
Allow Coaches to categorize a session by selecting one or more themes and/or sports.


**Actor**  
Coach


**Priority**  
High


**Acceptance Criteria**
- The panel displays selectable theme chips and sport chips.
- Coach can select/deselect themes and sports.
- Coach can search for and add a sport not listed via “Search for a sport”.
- Selected themes/sports are persisted on save.

---

## CMS – FR-068 Set Session Date

**Description**  
Allow Coaches to define the session date using a date picker.


**Actor**  
Coach


**Priority**  
High


**Acceptance Criteria**
- Coach can set the session date from a date picker control.
- Default date is the day/slot from which the coach initiated creation (when applicable).
- Date is required to save the session.

---

## CMS – FR-069 Set Session Title

**Description**  
Allow Coaches to provide a title for the session.


**Actor**  
Coach


**Priority**  
Medium


**Acceptance Criteria**
- Coach can enter a session title.
- If left empty, the system either prevents saving or applies a sensible default (per product rules).
- Title is displayed in the planning calendar once saved.

---

## CMS – FR-070 Create and Manage Training Blocks

**Description**  
Allow Coaches to structure a session using one or more training blocks, each containing rich content.


**Actor**  
Coach


**Priority**  
High


**Acceptance Criteria**
- Coach can add a new training block (e.g., “Create a new block”).
- Each block has a title field and a rich-text area for instructions/content.
- Coach can use basic formatting (bold/italic/underline, lists) consistent with the editor controls.
- Coach can delete a block; deletion requires confirmation if the block contains content.
- Coach can reorder blocks (via drag handle or explicit controls) if supported by product rules.

---

## CMS – FR-071 Set Intensity Reference per Block

**Description**  
Allow Coaches to assign an intensity reference to a training block.


**Actor**  
Coach


**Priority**  
Medium


**Acceptance Criteria**
- Each training block provides an “Intensity reference” selector (dropdown).
- Coach can select an intensity reference value from predefined options.
- Selected value is saved with the block and visible on subsequent edits.

---

## CMS – FR-072 Link Exercise Videos to the Session

**Description**  
Allow Coaches to associate one or more exercise videos with the session.


**Actor**  
Coach


**Priority**  
High


**Acceptance Criteria**
- Coach can open the “Link exercise videos” modal from the session panel.
- Modal supports searching exercises, filtering (e.g., via “Filter by”), and marking favorites.
- Coach can open an exercise detail view (“More details”) including video preview and target muscles.
- Coach can select one or more exercises and confirm to link them to the session.
- Linked exercises are listed under “Associated exercises” in the session panel.

---

## CMS – FR-073 Save a Training Block as a Template

**Description**  
Allow Coaches to save a training block as a reusable template from within a session.


**Actor**  
Coach


**Priority**  
Medium


**Acceptance Criteria**
- Coach can trigger “Save training block template” from a block action (e.g., star/save icon).
- A modal requests a template title and shows the block content preview.
- Coach can confirm to save the template.
- Saved template becomes available in “Training block models/templates”.

---

## CMS – FR-074 Insert a Training Block Template into the Session

**Description**  
Allow Coaches to insert one of their saved training block templates into a session.


**Actor**  
Coach


**Priority**  
Medium


**Acceptance Criteria**
- Coach can open the “Training block models/templates” list (e.g., “From my templates”).
- Templates can be searched and previewed.
- Coach can insert a template into the session; the inserted block appears in the session’s blocks list.
- Insertion does not modify the original template.

---

## CMS – FR-075 Save Session (Draft / Publish)

**Description**  
Allow Coaches to save a session, with support for saving without publishing and/or publishing depending on workflow.


**Actor**  
Coach


**Priority**  
High


**Acceptance Criteria**
- The session panel provides a primary save action (e.g., “Save session”).
- When supported, coach can “Save without publishing” and/or “Publish” the session.
- On save success, the session appears in the planning calendar on the chosen date.
- On save failure, the system shows an error and the coach’s inputs remain intact.

---

## CMS – FR-076 Validate Session Before Saving

**Description**  
Ensure the session creation form enforces required fields and prevents invalid data.


**Actor**  
Coach


**Priority**  
High


**Acceptance Criteria**
- System prevents saving if required fields are missing (at minimum: date; and other required fields per product rules).
- Inline validation messages are shown near the relevant fields.
- System prevents saving if training blocks contain invalid content (e.g., empty required titles if mandated).

