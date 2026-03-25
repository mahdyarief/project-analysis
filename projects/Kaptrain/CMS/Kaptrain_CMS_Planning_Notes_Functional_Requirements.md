# Kaptrain – CMS Planning Notes (Coach) Functional Requirements

## CMS – FR-045 Weekly Planning View

**Description**  
Allow Coaches to view and manage weekly and monthly planning for a selected athlete.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Coach can access the planning view for a selected athlete.
- Coach can switch between weekly and monthly views.
- The system displays all planned sessions for the selected period.
- Planning data reflects the latest saved state.
- Coach can navigate between dates.

---

## CMS – FR-046 Create Planning Note

**Description**  
Allow Coaches to create a planning note spanning one or multiple dates.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Coach can initiate the creation of a planning note.
- Coach must provide a note title.
- Coach must define a start date and end date.
- The system validates date ranges.
- Given valid input, the planning note is saved successfully.
- Newly created planning notes appear in the planning view.

---

## CMS – FR-047 View Planning Note Details

**Description**  
Allow Coaches to view details of an existing planning note.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Coach can select a planning note from the planning view.
- The system displays the note title and date range.
- Planning note details are read-only by default.

---

## CMS – FR-048 Edit Planning Note

**Description**  
Allow Coaches to modify an existing planning note.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Coach can initiate editing of a planning note.
- Coach can update the note title.
- Coach can update the date range.
- Given valid updates, the system saves changes successfully.
- Updated planning notes are reflected immediately.

---

## CMS – FR-049 Delete Planning Note

**Description**  
Allow Coaches to remove an existing planning note.

**Actor**  
Coach

**Priority**  
Medium

**Acceptance Criteria**

- Coach can initiate deletion of a planning note.
- The system requires confirmation before deletion.
- Upon confirmation, the planning note is removed from the planning view.
