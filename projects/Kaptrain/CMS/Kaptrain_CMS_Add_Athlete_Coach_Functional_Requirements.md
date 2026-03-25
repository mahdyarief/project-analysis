# Kaptrain – CMS Add Athlete (Coach) Functional Requirements

## CMS – FR-043 Invite Athlete(s)
**Description**  
Allow Coaches to invite one or more athletes to join their roster by sending invitations via email and/or sharing an invitation code/link.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**
- Coach can initiate the “Add an athlete” flow from the Athletes module.
- Coach can enter one or more athlete email addresses for invitation.
- The system validates email format before sending invitations.
- Coach can add additional email input fields to invite multiple athletes in one action.
- Coach can remove an email entry before sending invitations.
- The system sends invitations to all valid provided email addresses.
- If any invitation fails, the system reports which invitations failed and does not silently ignore failures.

---

## CMS – FR-044 Invitation Code & Link Sharing
**Description**  
Allow Coaches to invite athletes using an invitation code and/or shareable link.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**
- The system provides an invitation code associated with the Coach.
- The Coach can copy the invitation code and share it with athletes.
- The system provides a shareable invitation link.
- The Coach can copy the invitation link.
- Invitation code/link can be used by athletes to connect to the Coach account through the athlete onboarding flow.
- The system enforces that invitation code/link usage results in a pending confirmation (or equivalent approval step) before the athlete is fully linked to the Coach, if required by business rules.
