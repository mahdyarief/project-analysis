# 📱 Task List: Mobile Responsiveness - Kaptrain CMS (Athletes Section)

This document outlines the specific development tasks required to make the Athletes section of the Kaptrain CMS fully responsive, following the patterns identified in the Figma design (node `28:88090`).

## 🏗️ 1. Global Navigation & Layout
- [ ] **[FE] Sidebar Optimization**: Implement the collapsible burger menu for mobile.
- [ ] **[FE] Global Header**: Adjust the top bar to include condensed status indicators and a fixed "Home/Back" context navigation.

## 👥 2. Athletes Management
- [ ] **[FE] Athlete List (Card View)**:
    - [ ] Convert `Athlete List` table into a card-based vertical layout.
    - [ ] Implement a "Filter Overlay" for search, status, and category filtering.
- [ ] **[FE] Athlete Profile & Details**:
    - [ ] **Header Stack**: Vertical stack for name, status, and quick action buttons.
    - [ ] **Calendar Strip**: Transition the large calendar grid into a 7-day horizontal scrollable strip.
- [ ] **[FE] Notifications**:
    - [ ] Implement full-screen vertical list for notifications.
    - [ ] Add swipe-to-read/dismiss gestures for mobile users.
- [ ] **[FE] Messenger**:
    - [ ] Create the mobile chat interface (Hide sidebar conversations, focus on active thread).
    - [ ] Optimize the message input field (sticky to bottom of viewport).
- [ ] **[FE] Invitations**:
    
    

## 📅 3. Training & Planning (The "Cycles" Module)
- [ ] **[FE] Training Planner (Cycles View)**: 
    - [ ] Transform the desktop Week-Grid into a vertical "Cycle/Daily" list.
    - [ ] Add "Day Expand/Collapse" functionality to manage vertical space.
- [ ] **[WIRE] Mobile Interactions**:
    - [ ] Implement logic for "Move Mode" to handle session rescheduling without drag-and-drop.
    - [ ] Add long-press context menus for session actions (Edit, Cancel, Copy).
- [ ] **[FE] Creation & Modification Panels**:
    - [ ] **Création de séance**: Adapt the modal/panel to a full-screen drawer.
    - [ ] **Création de bloc**: Simplify the multi-column table input into a step-by-step mobile form.
    - [ ] **Modification/Cancellation**: Implement mobile-friendly confirmation overlays and alerts.

## 🎨 4. Design Standards & Polish
- [ ] **Typography**: Scale headers for `375px` width; ensure minimum `16px` for all body and input text.
- [ ] **Touch Targets**: Ensure all buttons and list items have a `44px` minimum hit area.
- [ ] **Spacing**: Apply standard `16px` or `20px` gutters for mobile consistency.
- [ ] **Loading States**: Implement skeleton loaders for the Athlete Card list and Planner Cycle list.
