# CMS – Messagerie (Messaging)

## Overview

The Messagerie module enables direct, contextual, and continuous communication between Coaches and Athletes. It supports training follow-ups, recovery feedback, injury discussions, and daily coordination, while remaining tightly connected to the athlete’s training context.

---

## CMS – FR-XXX View Messaging Inbox

**Description**  
Allow the Coach to access a centralized list of all messaging conversations with athletes.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- The Coach can access the Messagerie from the main navigation.
- The inbox displays a list of athlete conversations.
- Each conversation shows athlete info, last message preview, and timestamp.
- Conversations are sorted by latest activity.
- Unread conversations are visually highlighted.

---

## CMS – FR-XXX Filter Conversations (All / Unread)

**Description**  
Allow the Coach to filter conversations based on read status.

**Actor**  
Coach

**Priority**  
Medium

**Acceptance Criteria**

- Filter options include “Toutes” and “Non lues”.
- Selecting “Non lues” displays only unread conversations.
- Filters apply instantly without page reload.

---

## CMS – FR-XXX Search Conversations

**Description**  
Allow the Coach to search conversations by athlete name.

**Actor**  
Coach

**Priority**  
Medium

**Acceptance Criteria**

- Search input is available in the conversation list.
- Results update dynamically while typing.
- Partial matches are supported.

---

## CMS – FR-XXX View Conversation Thread

**Description**  
Allow the Coach to open and read a full conversation.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Messages are displayed chronologically.
- Coach and Athlete messages are visually distinct.
- Each message shows content and timestamp.
- Thread auto-scrolls to the latest message.

---

## CMS – FR-XXX Athlete Context Header

**Description**  
Display athlete context at the top of the conversation.

**Actor**  
Coach

**Priority**  
Medium

**Acceptance Criteria**

- Athlete name, avatar, and status are visible.
- Associated sports are shown as tags.
- Information is read-only.

---

## CMS – FR-XXX Send Message

**Description**  
Allow the Coach to send text messages.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Text input is available.
- Messages can be sent via button or Enter.
- Sent messages appear instantly.
- Empty messages cannot be sent.

---

## CMS – FR-XXX Receive Message

**Description**  
Allow the Coach to receive athlete messages.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Incoming messages appear in real time.
- Conversation order updates.
- Unread indicators appear if not opened.

---

## CMS – FR-XXX Mark Messages as Read

**Description**  
Automatically mark messages as read when viewed.

**Actor**  
System

**Priority**  
High

**Acceptance Criteria**

- Messages are marked read when conversation is opened.
- Unread indicators are removed.

---

## CMS – FR-XXX Unread Indicators

**Description**  
Highlight unread conversations.

**Actor**  
System

**Priority**  
Medium

**Acceptance Criteria**

- Visual indicators appear for unread messages.
- Indicators disappear once messages are read.

---

## CMS – FR-XXX Persist Message History

**Description**  
Ensure message history is preserved.

**Actor**  
System

**Priority**  
High

**Acceptance Criteria**

- Messages persist across sessions.
- No data loss occurs.

---

## CMS – FR-XXX Empty States

**Description**  
Handle empty inbox and empty conversations.

**Actor**  
System

**Priority**  
Low

**Acceptance Criteria**

- Clear empty-state messaging is displayed.
- UI remains consistent.

---

## CMS – FR-XXX Performance & Responsiveness

**Description**  
Ensure messaging is performant and responsive.

**Actor**  
System

**Priority**  
Medium

**Acceptance Criteria**

- Conversations load quickly.
- Message sending does not reload the page.
- Layout adapts to screen size.
