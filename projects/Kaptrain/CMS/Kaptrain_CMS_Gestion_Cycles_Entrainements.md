# CMS – Gestion des cycles d’entraînements (Training Cycle Management)

## CMS – FR-077 Create a Training Cycle

**Description**  
Allow Coaches to create a training cycle using selected training sessions.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Coach can select one or more training sessions from weekly planning.
- Coach can initiate cycle creation via the “Create cycle” action.
- Coach must provide a cycle name.
- Cycle is created successfully and stored in the system.

---

## CMS – FR-078 Add Metadata to a Training Cycle

**Description**  
Allow Coaches to define metadata for a training cycle, such as sports or themes.

**Actor**  
Coach

**Priority**  
Medium

**Acceptance Criteria**

- Coach can assign one or more sports to the cycle.
- Coach can assign one or more thematic tags.
- Coach can search and add additional sports.
- Metadata is saved with the training cycle.

---

## CMS – FR-079 Save Training Cycle as Template

**Description**  
Allow Coaches to save a training cycle as a reusable template.

**Actor**  
Coach

**Priority**  
Medium

**Acceptance Criteria**

- Coach can save a training cycle as a template.
- Template is added to the Coach’s cycle library.
- Template is reusable across athletes.
- System confirms successful save.

---

## CMS – FR-080 View Training Cycles

**Description**  
Allow Coaches to view their saved training cycles.

**Actor**  
Coach

**Priority**  
Medium

**Acceptance Criteria**

- Coach can open the “My training cycles” panel.
- Training cycles are displayed with name, duration, and session count.
- Coach can scroll through available cycles.
- Coach can select a cycle to preview.

---

## CMS – FR-081 Filter Training Cycles

**Description**  
Allow Coaches to filter training cycles using different criteria.

**Actor**  
Coach

**Priority**  
Low

**Acceptance Criteria**

- Coach can filter cycles by sport.
- Coach can filter cycles by thematic tags.
- Coach can reset all filters.
- Filtered results update immediately.

---

## CMS – FR-082 Preview a Training Cycle

**Description**  
Allow Coaches to preview a training cycle before inserting it.

**Actor**  
Coach

**Priority**  
Medium

**Acceptance Criteria**

- Coach can preview the cycle in weekly or monthly format.
- Preview shows sessions grouped by week.
- Preview does not affect athlete planning.
- Coach can exit preview without changes.

---

## CMS – FR-083 Insert Training Cycle into Planning

**Description**  
Allow Coaches to insert a training cycle into an athlete’s planning.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Coach can select a target week or date range.
- Coach can insert the selected cycle.
- Sessions are distributed correctly across weeks.
- Coach must confirm before insertion.

---

## CMS – FR-084 Delete a Training Cycle

**Description**  
Allow Coaches to delete an existing training cycle.

**Actor**  
Coach

**Priority**  
Low

**Acceptance Criteria**

- Coach can initiate deletion from the cycle panel.
- System requires confirmation before deletion.
- Deleted cycle is removed from the library.
- Deletion does not affect existing planning.
