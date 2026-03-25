## APP – FR-XXX Voir et classer statistiques (Widget Management)

**Description**  
Provide users with the ability to view all available statistics widgets, reorder them, and choose which widgets appear on the home dashboard.

**Actor**  
Athlete (primary)

**Priority**  
High

---

### Acceptance Criteria

#### 1. Access & Display of All Statistics
- User can access **Toutes mes statistiques** from the “Mes statistiques” section.
- System displays all available widgets, including but not limited to:
  - Répartition d’activité
  - Volume d’entraînement
  - Suivi de poids
  - Temps d’activité
  - Nombre de pas
  - Charge d’entraînement
  - Suivi de règle (if applicable)
- Widgets show:
  - Title
  - Data preview (chart, number, ring, etc.)
  - Empty state if no data recorded.

#### 2. Widget Sorting & Customization
- User can click **Modifier mes statistiques** to enter the customization mode.
- User can drag and drop widgets to reorder them.
- System saves the new order and persists it across sessions.
- User can remove non‑mandatory widgets from the home screen.
- User can re-add removed widgets from the list of “Statistiques disponibles”.
- Mandatory widgets (e.g., core training stats) cannot be removed, only reordered.

#### 3. Widget Detail Screen
- Selecting a widget opens a **Widget Detail** view.
- Detail view includes:
  - Full chart, data, or detailed breakdown.
  - Short description of what the statistic represents.
  - Option **“Définir comme widget principal”**.
- If set as main widget:
  - System highlights it as the primary widget on the home dashboard.
  - Only one widget can be selected as the principal widget at a time.

#### 4. Data Handling & Empty States
- If the widget has insufficient or missing data:
  - Show an informative empty state (e.g., “Aucune donnée enregistrée”).
  - If applicable, present an action (e.g., “Autorise Kaptrain à accéder au suivi de pas”).

#### 5. Persistence
- All modifications (order, visibility, principal widget selection) are saved locally and synchronized with the backend user profile.
- Order and display preferences remain consistent across devices when user logs in.

