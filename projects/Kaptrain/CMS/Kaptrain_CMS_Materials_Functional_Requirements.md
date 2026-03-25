# Kaptrain – CMS Materials Functional Requirements

## CMS – FR-012 Materials Management
**Description**  
Allow CMS Administrators to manage the list of materials that can be associated with exercises.

**Actor**  
Admin

**Priority**  
High

**Acceptance Criteria**
- Admin can view the list of available materials.
- Each material includes a name and an associated icon.
- Admin can search materials by name.
- Admin can access actions to create, edit, or delete materials.
- Displayed data reflects the latest stored state.

---

## CMS – FR-013 Create Material
**Description**  
Allow CMS Administrators to create a new material that can be used in exercises.

**Actor**  
Admin

**Priority**  
High

**Acceptance Criteria**
- Admin can initiate the material creation process.
- Admin must provide a material name.
- Admin can define the material language.
- Admin can upload an icon representing the material.
- Material name must be unique.
- All required fields must be completed before creation.
- Given valid input, the system creates the material successfully.
- Newly created material appears in the materials list.
- Admin can cancel material creation without saving.
- Errors prevent material creation.

---

## CMS – FR-014 Edit Material
**Description**  
Allow CMS Administrators to modify an existing material.

**Actor**  
Admin

**Priority**  
High

**Acceptance Criteria**
- Admin can initiate the edit process for a material.
- Existing material data is loaded for editing.
- Admin can update the material name.
- Admin can update the material language.
- Admin can replace or update the material icon.
- Material name must remain unique.
- Given valid updates, the system saves changes successfully.
- Updated material data is reflected in the materials list.
- Admin can cancel editing without saving changes.
- Errors do not overwrite existing material data.

---

## CMS – FR-015 Delete Material
**Description**  
Allow CMS Administrators to permanently remove a material.

**Actor**  
Admin

**Priority**  
High

**Acceptance Criteria**
- Admin can initiate the delete action for a material.
- The system requires confirmation before deletion.
- Upon confirmation, the material is permanently deleted.
- Deleted materials are no longer available for selection in exercises.
- If deletion fails, the material remains unchanged and an error is reported.
