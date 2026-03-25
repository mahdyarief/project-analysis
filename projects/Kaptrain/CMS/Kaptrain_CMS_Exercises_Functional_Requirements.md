# Kaptrain – CMS Exercises Functional Requirements

## CMS – FR-006 Exercises Management
**Description**  
Allow CMS users to explore exercises while restricting exercise creation and modification to Administrators.

**Actor**  
Admin, Coach

**Priority**  
High

**Acceptance Criteria**
- Admin and Coach can view the list of exercises.
- Admin and Coach can search exercises by name.
- Admin and Coach can filter exercises using available criteria.
- Admin and Coach can sort exercises.
- Admin and Coach can mark exercises as favorites.
- Favorite status is saved per user.
- Admin and Coach can view exercise details.
- Admin can add new exercises.
- Admin can edit existing exercises.
- Admin can delete exercises.
- Coach cannot add, edit, or delete exercises.
- Displayed exercise data reflects the latest stored state.

---

## CMS – FR-007 Create Exercise
**Description**  
Allow CMS Administrators to create a new exercise by defining its metadata, content, media, and classification attributes.

**Actor**  
Admin

**Priority**  
High

**Acceptance Criteria**
- Admin can initiate the exercise creation process.
- Admin must provide a name for the exercise.
- Admin can define the exercise language.
- Admin can provide a textual description.
- Admin can assign thematic categories.
- Admin can associate sports.
- Admin can specify required materials.
- Admin can define primary and secondary muscle groups.
- Admin can upload and validate a required exercise video.
- Admin can define multiple step-by-step instructions.
- Admin can classify the exercise using predefined attributes.
- Required fields must be completed before creation.
- Successful creation makes the exercise available in the list.
- Admin can cancel creation without saving.
- Errors prevent exercise creation.

---

## CMS – FR-008 Edit Exercise
**Description**  
Allow CMS Administrators to modify an existing exercise.

**Actor**  
Admin

**Priority**  
High

**Acceptance Criteria**
- Admin can edit an existing exercise.
- Existing data is loaded for editing.
- Admin can update metadata, media, instructions, and classifications.
- Video replacements are validated.
- Required fields must remain valid.
- Changes are saved successfully.
- Admin can cancel editing without saving.
- Errors do not overwrite existing data.

---

## CMS – FR-009 Delete Exercise
**Description**  
Allow CMS Administrators to permanently remove an exercise.

**Actor**  
Admin

**Priority**  
High

**Acceptance Criteria**
- Admin can initiate deletion.
- Deletion requires confirmation.
- Deleted exercises are removed from the system.
- Deleted exercises are no longer usable.
- Errors prevent deletion.

---

## CMS – FR-010 Exercise Detail
**Description**  
Allow CMS users to view detailed information about an exercise.

**Actor**  
Admin, Coach

**Priority**  
High

**Acceptance Criteria**
- Users can view exercise details.
- Details include metadata, instructions, classifications, and media.
- Data reflects the latest saved version.
- Coach users have read-only access.

---

## CMS – FR-011 Duplicate Exercise
**Description**  
Allow CMS Administrators to duplicate an existing exercise.

**Actor**  
Admin

**Priority**  
High

**Acceptance Criteria**
- Admin can duplicate an exercise.
- Duplicated exercises copy all relevant data.
- Duplicated exercises are independent from originals.
- Original exercises remain unchanged.
- Duplicated exercises appear in the list.
- Errors prevent duplication.
