## APP – FR-XXX Temps d’activité (Widget – suivi du temps d’entraînement)

**Description**  
Allow users to view their validated activity time across multiple timeframes (Today, This Week, This Month, This Year) and receive automated recommendations to upgrade their practice level based on sustained training volume.

**Actor**  
Athlete (primary)

**Priority**  
High

**Acceptance Criteria**
- User can access the **“Temps d’activité”** widget from **Mes statistiques**.
- The widget displays four timeframes with total validated activity time:
  - **Aujourd’hui** – total duration of validated training sessions for the current day.
  - **Cette semaine** – total activity time aggregated for the current ISO week.
  - **Ce mois‑ci** – total activity time aggregated for the current month.
  - **Cette année** – total activity time aggregated for the current year.
- Each timeframe displays activity duration in **hours and minutes**.
- A distinct color indicator is shown next to each timeframe according to the design.
- The system monitors the athlete’s **average validated training time over the last 4 consecutive weeks**.
- If the calculated weekly average is **greater than the upper boundary** of the athlete's current practice level:
  - A modal appears proposing a **practice level upgrade**.
  - The modal includes:
    - Current level label and weekly hour range.
    - Proposed new level label and weekly hour range.
    - A confirmation button: **“Passer au niveau supérieur”**.
    - A dismissal button: **“Garder mon niveau actuel”**.
- Upon confirmation:
  - The athlete’s practice level is immediately updated.
  - The modal closes.
- Upon dismissal:
  - The modal closes without applying any changes.
- If no upgrade criteria are met, no modal or suggestion is displayed.
- If the system has insufficient activity data, the widget displays zeros or placeholders accordingly.
