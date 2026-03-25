# Kaptrain CMS – Athlete Dashboard (Extended Functional Requirements)

## CMS – FR-XXX View Injuries List

**Description**  
Allow Coaches to view a consolidated list of all injuries associated with an athlete directly from the Athlete Dashboard.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- The system displays a list of injuries with status labels (In progress, Treated).
- Each injury item shows the injury name, start or completion date, and current status.
- Coach can expand or reduce an injury card to see more or fewer details.
- Injuries are ordered by most recent first.

## CMS – FR-XXX Add a New Injury

**Description**  
Allow Coaches to create and register a new injury for an athlete.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Coach can initiate injury creation via an “Add” button.
- Coach must define the injury area using a selectable body diagram or dropdown.
- Coach can provide an injury name and description.
- Coach can save the injury with a default status of “In progress”.
- Newly added injuries appear immediately in the injuries list.

## CMS – FR-XXX Edit an Existing Injury

**Description**  
Allow Coaches to modify an existing injury record.

**Actor**  
Coach

**Priority**  
Medium

**Acceptance Criteria**

- Coach can edit injury area, name, and description.
- Coach can update the injury status (In progress / Treated).
- Changes are saved explicitly via a “Save changes” action.
- Updated information is reflected instantly in the injuries list.

## CMS – FR-XXX Visual Injury Mapping

**Description**  
Provide a visual representation of injury location on a human body diagram.

**Actor**  
Coach

**Priority**  
Medium

**Acceptance Criteria**

- Injury areas are highlighted on front and back body diagrams.
- The highlighted area matches the selected injury area.
- Multiple injuries can be visualized independently.

## CMS – FR-XXX View Physiological Data

**Description**  
Allow Coaches to view detailed physiological data for an athlete.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- The system displays general metrics (Weight, Height, Max HR).
- Sport-specific metrics are grouped by discipline (Running, Cycling).
- Each metric displays its value and last update date.
- Data is read-only from the dashboard view.

## CMS – FR-XXX View Records Overview

**Description**  
Allow Coaches to view a categorized overview of athlete performance records.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Records are grouped by sport category (Bodybuilding, Crossfit, Rowing, etc.).
- Each category displays the number of recorded entries.
- Categories without records are clearly indicated.

## CMS – FR-XXX View Records by Category

**Description**  
Allow Coaches to drill down into records for a specific sport category.

**Actor**  
Coach

**Priority**  
Medium

**Acceptance Criteria**

- Coach can search and sort records within a category.
- Each record displays exercise name and best performance value.
- Records without data are labeled “No record”.

## CMS – FR-XXX View Record Details

**Description**  
Allow Coaches to view detailed performance data for a specific record.

**Actor**  
Coach

**Priority**  
Medium

**Acceptance Criteria**

- The system displays a performance chart over selectable time ranges.
- Coach can switch between predefined periods (7 days, 1 month, 3 months, etc.).
- A historical list of recorded values is displayed with dates.

## CMS – FR-XXX View Extended Record History

**Description**  
Allow Coaches to analyze long-term performance progression for a specific record.

**Actor**  
Coach

**Priority**  
Low

**Acceptance Criteria**

- Historical data supports long-term comparison.
- Data points are chronologically ordered.
- The system ensures consistent units across all values.
