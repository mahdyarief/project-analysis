# Athlete Dashboard – Functional Requirements

## CMS – FR-XXX Athlete Dashboard Overview

**Description**  
Provide Coaches with a comprehensive dashboard view summarizing an athlete’s training activity, wellness status, physiological data, and key insights to support day-to-day coaching decisions.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Coach can access the Athlete Dashboard from the Athletes menu.
- The dashboard displays the selected athlete’s profile, current form status, and associated sports.
- All widgets update dynamically based on the selected athlete.
- Data displayed is read-only except where explicitly editable (e.g. notes).
- The dashboard loads within acceptable performance limits (< 2s on standard connection).

## CMS – FR-XXX Activity Distribution Widget

**Description**  
Display a visual breakdown of the athlete’s activity distribution by sport for the selected time range.

**Actor**  
Coach

**Priority**  
Medium

**Acceptance Criteria**

- Activity distribution is displayed as a donut or pie chart.
- Each segment represents a sport category.
- Percentages reflect the proportion of total activity.
- Navigation controls allow cycling through views.
- Hovering a segment reveals exact values.

## CMS – FR-XXX Training Volume Widget

**Description**  
Allow Coaches to view the athlete’s training volume over the last 7 days.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Training volume is shown as a bar chart.
- Each bar represents one day.
- Completed sessions only are counted.
- Zero-activity days are visible.

## CMS – FR-XXX Weight Tracking Widget

**Description**  
Provide a longitudinal view of the athlete’s weight evolution.

**Actor**  
Coach

**Priority**  
Medium

**Acceptance Criteria**

- Weight is displayed as a line chart.
- Time range is configurable.
- Missing data does not break the chart.

## CMS – FR-XXX Activity Time Summary

**Description**  
Display aggregated activity duration for different time scopes.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Shows Today, Week, and Month durations.
- Values update when scope changes.
- Consistent time formatting is applied.

## CMS – FR-XXX Athlete Form Tracking

**Description**  
Visualize the athlete’s perceived form and wellness trends.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Line chart displays form score over time.
- Date navigation is available.
- Multiple metrics can be compared.

## CMS – FR-XXX Selected Wellness Items

**Description**  
Allow Coaches to filter wellness indicators.

**Actor**  
Coach

**Priority**  
Medium

**Acceptance Criteria**

- Coach can toggle wellness items.
- Selected items appear on the graph.
- Colors remain consistent.

## CMS – FR-XXX Records Summary Widget

**Description**  
Display recent performance records.

**Actor**  
Coach

**Priority**  
Low

**Acceptance Criteria**

- Latest records are shown.
- Each record includes discipline and value.
- Full list accessible via link.

## CMS – FR-XXX Injury Overview Widget

**Description**  
Show injury status and history.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Active and past injuries are listed.
- Status labels are visible.
- Detail view is accessible.

## CMS – FR-XXX Physiological Data Widget

**Description**  
Display key physiological metrics.

**Actor**  
Coach

**Priority**  
Medium

**Acceptance Criteria**

- Metrics include weight and FC Max.
- Update dates are shown.
- Units are clearly labeled.

## CMS – FR-XXX Statistics Widget (Sheet)

**Description**  
Open detailed statistics in a side sheet.

**Actor**  
Coach

**Priority**  
Medium

**Acceptance Criteria**

- Sheet opens from dashboard.
- Week/Month/Year views available.
- Multiple breakdown types supported.

## CMS – FR-XXX Coach Notes Panel

**Description**  
Provide a private note space for Coaches.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Notes are coach-only.
- Chronological listing.
- Search functionality available.

## CMS – FR-XXX Create New Coach Note

**Description**  
Allow Coaches to create notes.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- New note editor opens in sheet.
- Title and rich text supported.
- Notes are saved persistently.

## CMS – FR-XXX Edit Existing Coach Note

**Description**  
Allow Coaches to edit notes.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Notes open in read mode.
- Editing is supported.
- Changes are saved correctly.
