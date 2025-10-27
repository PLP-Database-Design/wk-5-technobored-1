# 🧪 Final Group Test Report Template — Word Puzzle Game Plus

**Level:** Intermediate QA | **Week 5:** Test Management

**Course:** Software Testing & Quality Assurance  
**Module:** Test Management (Week 5)  
**Project Type:** Group Assessment  
**Submission Date:** 2025-10-28

## Team Information

| Role | Name | Responsibilities |
|------|------|------------------|
| Test Manager | | Planning, scheduling, coordination, metric tracking |
| Risk Analyst | | Risk identification, prioritization, test design linkage |
| Test Executor | | Execution, evidence capture, defect logging |

## Group Rules

- Each student must belong to only one group.
- Duplicate membership or multiple submissions will result in invalidation.
- Every group member must contribute towards this project

## Project Overview

**System Under Test:** Word Puzzle Game Plus  
**Technology Stack:** HTML, CSS, JavaScript  
**Environment:** Chrome Browser (Desktop)

### Features Under Test

| Feature | Description | Risk Category |
|---------|-------------|---------------|
| Reset Game | Clears score and progress instantly | |
| Leaderboard | Stores top 3 scores in localStorage | |
| Bonus Round | Every 3 puzzles → doubles score | |

## Test Plan

### Objectives

- 

### Scope

**In Scope:**
- 

**Out of Scope:**
- 

### Tools & Resources

- 

### Schedule

| Phase | Planned Duration | Actual Duration | Status |
|-------|------------------|-----------------|--------|
| | | | |

## Risk Analysis
| ID     | Feature                   | Risk Description                                                                    | Likelihood | Impact | Priority   | Mitigation Strategy                                                          |
| ------ | ------------------------- | ----------------------------------------------------------------------------------- | ---------- | ------ | ---------- | ---------------------------------------------------------------------------- |
| **R1** | **Leaderboard**           | LocalStorage may fail or be unavailable, causing loss of saved scores               | Medium     | High   | **High**   | Implement fallback to in-memory storage and error handling for failed writes |
| **R2** | **Reset Game**            | Reset may not properly clear score or progress, leading to inconsistent state       | Medium     | Medium | **Medium** | Add test cases verifying all variables (score, solved, hint) reset correctly |
| **R3** | **Bonus Round**           | Bonus logic may trigger incorrectly (e.g., after wrong count) or not apply score ×2 | Medium     | High   | **High**   | Validate logic with unit and functional testing across multiple rounds       |
| **R4** | **Hint System**           | Multiple hints could be triggered, reducing score repeatedly or breaking balance    | Low        | Medium | **Medium** | Lock hint button after one use until next puzzle loads                       |
| **R5** | **User Input Validation** | Blank or invalid inputs may pass unchecked, affecting game flow                     | High       | Medium | **High**   | Implement front-end input validation and ensure error messages are clear     |
| **R6** | **UI Responsiveness**     | Game layout may break on smaller screens, hiding controls or leaderboard            | Medium     | Low    | **Medium** | Perform responsive UI tests and CSS media query validation                   |
| **R7** | **Data Consistency**      | Leaderboard may display incorrect rankings after multiple updates                   | Low        | High   | **Medium** | Re-sort and update leaderboard after every score submission                  |


# Risk Evaluation

Each risk was evaluated based on Likelihood, Impact, and Priority.

Likelihood: The probability of the risk occurring.

Impact: The severity of the risk if it occurs.

Priority: Combined measure used to rank mitigation urgency.

## Mitigation Actions (by Feature)

<!-- Feature 1: Reset Game -->

Risk: Reset button may not clear all states properly (e.g., score resets but timer doesn’t).
Impact: Medium → Players get inconsistent results.
Mitigation Action:

Test multiple states before/after reset to confirm full reset.

Add a confirmation modal before reset.

Log game state before reset for debugging.

<!-- Feature 2: Leaderboard -->

Risk: localStorage fails to save or retrieve scores correctly.
Impact: High → Loss of player data or inaccurate rankings.
Mitigation Action:

Validate browser storage support.

Implement fallback (session-based array).

Add input validation for stored scores.

Include try-catch around storage calls.

 <!-- Feature 3: Bonus Round -->

Risk: Score doubling logic may misfire or repeat.
Impact: High → Inflated or lost scores.
Mitigation Action:

Write unit tests for bonus multiplier logic.

Add condition checks for puzzle count before doubling.

Display clear notification when bonus is applied.

Verify rounding and math precision.

### Risk Coverage
Risk Coverage

Testing coverage was tracked through a risk matrix.
| Metric                    | Value     |
| ------------------------- | --------- |
| Total Risks Identified    | 7         |
| Risks Mitigated           | 6         |
| Risks Pending Review      | 1         |
| **Tested Risks Coverage** | **85.7%** |
| **Untested Risks**        | **14.3%** |


## Test Cases

| ID | Feature | Objective | Expected Result | Actual Result | Status | Risk Link |
|----|---------|-----------|----------------|---------------|--------|-----------|
| | | | | | | |

## Defects

| ID | Issue Title | Severity | Risk ID | Status | GitHub Link |
|----|-------------|----------|---------|--------|-------------|
| | | | | | |

## Metrics

- Test Case Pass Percent: 
- Defect Density: 
- Risk Coverage Percent: 
- Regression Success Rate: 

### Defect Summary

- Total Defects Logged: 
- Critical High: 
- Fix Rate: 

## Test Control & Project Management

### Phases

| Phase | Deliverable | Actual Output | Variance | Owner |
|-------|-------------|---------------|----------|-------|
| | | | | |

**Progress Tracking Method:**  
**Change Control Notes:**

## Lessons Learned

- Most Defect Prone Feature: 
- Risk Analysis Impact: 
- Team Communication Effectiveness: 
- Improvements for Next Cycle: 

## Attachments

- 

## Sign Off

| Name | Role | Initials | Date |
|------|------|-----------|------|
| | Test Manager | | |
| | Risk Analyst | | |
| | Test Executor | | |

## Overall Summary

**Statement:** 

**Test Status:** ☐ Completed / ☐ In Progress / ☐ Deferred
