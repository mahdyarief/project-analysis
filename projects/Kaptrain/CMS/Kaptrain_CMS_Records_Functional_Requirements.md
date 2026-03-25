# Kaptrain – CMS Records Functional Requirements

## CMS – FR-023 Records Management
**Description**  
Allow CMS Administrators to manage records associated with different sports.

**Actor**  
Admin

**Priority**  
High

**Acceptance Criteria**
- Admin can view the list of sports available for records.
- Admin can search sports by name.
- Admin can select a sport to view its associated records.
- Records displayed reflect the latest stored data.

---

## CMS – FR-024 View Records by Sport
**Description**  
Allow CMS Administrators to view records grouped under a selected sport.

**Actor**  
Admin

**Priority**  
High

**Acceptance Criteria**
- Admin can select a sport to view its records.
- Records are grouped by category within the selected sport.
- Each record displays its name and associated unit.
- Admin can access actions to add, edit, or delete records.

---

## CMS – FR-025 Create Record
**Description**  
Allow CMS Administrators to create a new record.

**Actor**  
Admin

**Priority**  
High

**Acceptance Criteria**
- Admin can initiate the record creation process.
- Admin must provide a record name.
- Admin can assign one or more categories to the record.
- Admin can select a unit for the record (e.g., time, distance, repetitions, points).
- All required fields must be completed before saving.
- Given valid input, the system creates the record successfully.
- Newly created record appears under the selected sport.
- Admin can cancel record creation without saving.
- Errors prevent record creation.

---

## CMS – FR-026 Add Record Category
**Description**  
Allow CMS Administrators to add new categories for records.

**Actor**  
Admin

**Priority**  
High

**Acceptance Criteria**
- Admin can initiate the add category process while creating or editing a record.
- Admin must provide a category name.
- Category name must be unique within the sport.
- Given valid input, the system creates the category successfully.
- Newly created category becomes available for selection.
- Errors prevent category creation.

---

## CMS – FR-027 Edit Record
**Description**  
Allow CMS Administrators to modify an existing record.

**Actor**  
Admin

**Priority**  
High

**Acceptance Criteria**
- Admin can initiate the edit process for a record.
- Existing record data is loaded for editing.
- Admin can update the record name.
- Admin can update assigned categories.
- Admin can update the unit.
- Given valid updates, the system saves changes successfully.
- Updated record data is reflected immediately.
- Admin can cancel editing without saving.
- Errors do not overwrite existing record data.

---

## CMS – FR-028 Delete Record
**Description**  
Allow CMS Administrators to permanently remove a record.

**Actor**  
Admin

**Priority**  
High

**Acceptance Criteria**
- Admin can initiate the delete action for a record.
- The system requires confirmation before deletion.
- Upon confirmation, the record is permanently deleted.
- Deleted records are no longer visible or usable.
- Errors prevent deletion.
