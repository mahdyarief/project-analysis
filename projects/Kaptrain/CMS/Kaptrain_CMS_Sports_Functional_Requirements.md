# Kaptrain – CMS Sports Functional Requirements

## CMS – FR-016 Sports Management
**Description**  
Allow CMS Administrators to manage the list of sports that can be associated with exercises and programs.

**Actor**  
Admin

**Priority**  
High

**Acceptance Criteria**
- Admin can view the list of available sports.
- Each sport includes a name and an associated icon.
- Admin can search sports by name.
- Admin can access actions to create, edit, or delete sports.
- Displayed data reflects the latest stored state.

---

## CMS – FR-017 Create Sport
**Description**  
Allow CMS Administrators to create a new sport.

**Actor**  
Admin

**Priority**  
High

**Acceptance Criteria**
- Admin can initiate the sport creation process.
- Admin must provide a sport name.
- Admin can define the sport language.
- Admin can add one or more keywords associated with the sport.
- Admin can provide an optional description.
- Admin can upload an icon representing the sport.
- Sport name must be unique.
- All required fields must be completed before creation.
- Given valid input, the system creates the sport successfully.
- Newly created sport appears in the sports list.
- Admin can cancel sport creation without saving.
- Errors prevent sport creation.

---

## CMS – FR-018 Edit Sport
**Description**  
Allow CMS Administrators to modify an existing sport.

**Actor**  
Admin

**Priority**  
High

**Acceptance Criteria**
- Admin can initiate the edit process for a sport.
- Existing sport data is loaded for editing.
- Admin can update the sport name.
- Admin can update the sport language.
- Admin can update associated keywords.
- Admin can update the sport description.
- Admin can replace or update the sport icon.
- Sport name must remain unique.
- Given valid updates, the system saves changes successfully.
- Updated sport data is reflected in the sports list.
- Admin can cancel editing without saving changes.
- Errors do not overwrite existing sport data.

---

## CMS – FR-019 Delete Sport
**Description**  
Allow CMS Administrators to permanently remove a sport.

**Actor**  
Admin

**Priority**  
High

**Acceptance Criteria**
- Admin can initiate the delete action for a sport.
- The system requires confirmation before deletion.
- Upon confirmation, the sport is permanently deleted.
- Deleted sports are no longer available for selection in exercises or programs.
- If deletion fails, the sport remains unchanged and an error is reported.
