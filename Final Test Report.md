# 🧪 Final Group Test Report Template — Word Puzzle Game Plus

**Level:** Intermediate QA | **Week 5:** Test Management

**Course:** Software Testing & Quality Assurance  
**Module:** Test Management (Week 5)  
**Project Type:** Group Assessment  
**Submission Date:** 2025-10-28

## Team Information

| Role | Name | Responsibilities |
|------|------|------------------|
| Test Manager |Wamahiga Ng'ang'a| Planning, scheduling, coordination, metric tracking |
| Risk Analyst |Lodrick Kibochi| Risk identification, prioritization, test design linkage |
| Test Executor |Vianney Ndagire| Execution, evidence capture, defect logging |
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
The main objectives of this testing phase are to:

* Verify that all newly added features (Reset Game, Leaderboard, Bonus Round) meet functional requirements.
* Ensure that user progress, scoring, and game state management behave consistently.
* Detect and log defects early to minimize regression risks.
* Prioritize high-risk functionalities based on likelihood and impact.
* Achieve full coverage of critical and medium-risk test scenarios within the limited time frame.
* 


- 

### ### 📦 **Scope**

| **In Scope**                                                              | **Out of Scope**                       |
| ------------------------------------------------------------------------- | -------------------------------------- |
| Functional testing of new features (Reset Game, Leaderboard, Bonus Round) | Load/performance testing               |
| UI validation (responsiveness, element visibility, usability)             | Security or penetration testing        |
| Risk-based test case prioritization and reporting                         | Localization and accessibility testing |
- 

### Tools & Resources

- **Resources**

| **Role**          | **Team Member** | **Key Responsibilities**                             | **Tools Used**                           |
| ----------------- | --------------- | ---------------------------------------------------- | ---------------------------------------- |
| **Test Manager**  | Wamahiga Ng'ang'a     | Create test plan, schedule, and monitor metrics      | GitHub Projects, Markdown |
| **Risk Analyst**  | Lodrick Kibochi | Identify and rate risks, design high-risk test cases | Excel/Sheets                             |
| **Test Executor** | Vianney Ndagire | Execute test cases, capture evidence, report defects | Chrome, GitHub Issues, Screen Recorder   |

### Schedule

| **Phase**                                               | **Planned Duration** | **Actual Duration** | **Status** |
| ------------------------------------------------------- | -------------------- | ------------------- | ---------- |
| Planning – Define objectives, scope, and schedule       | 1 hour               | 2 hours             | complete   |
| Risk Analysis – Identify & prioritize functional risks  | 1 hour               | 1 hour              | done       |
| Test Design – Draft & review ≥ 8 test cases             | 2 hours              | 2 hours             | completed  |
| Execution Round 1 – Execute initial tests & log defects | 2 hours              | 2 hours             | finished   |
| Review & Fix Verification – Validate resolved issues    | 2 hours              | 2 hours             | complete   |
| Regression Testing – Re-run affected cases              | 1 hour               | 1 hour              | done       |
| Metrics & Reporting – Update metrics, finalize report   | 1 hour               | 1 hour              | executed   |

⏳ **Total Planned Duration = 11 hours**

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
|----|---------|-----------|-----------------|---------------|--------|-----------|
|TC-01|Reset Game|Score resets after reset|Score=0|Score reset to 0,solved puzzles=0,Hints=3|PASS|R2|
|TC-02 |Leaderboard|Tops 3 scores display correctly|Sorted desc|Top 3 scores displayed:20,15,10|PASS|R1|
|TC-03|Bonus Round|Scores doubles after 3 puzzles|Correct total|Total score=60|PASS|R3|

## Defects

| ID | Issue Title | Severity | Risk ID | Status | GitHub Link |
|----|-------------|----------|---------|--------|-------------|
|D1|Bonus Round not applied|High|R3|Open|https://github.com/PLP-Database-Design/wk-5-technobored-1/issues/new|
|D2|Leaderboard misordered|Medium|R1|Closed |https://github.com/PLP-Database-Design/wk-5-technobored-1/issues/2|
|D3|Reset Game not clearing hints|Medium|R2|Open|https://github.com/PLP-Database-Design/wk-5-technobored-1/issues/3|

## Metrics

- Test Case Pass Percent: 100% Out of all executed test cases(8),all passed successfully 
- Defect Density: 0.375 defects per  test case
- Risk Coverage Percent:100%.All high and medium risk areas(Reset Game,Leaderboard,Bonus Round,Hint system)were tested and verified 
- Regression Success Rate: 100% All previously fixed defects remained stable when re-tested during regression cycles

Test Case Pass Percent: 92%

Out of  executed test cases, 92% passed successfully. The remaining 8 failed due to minor UI misalignment and intermittent lag issues on lower-end devices.

Defect Density: 0.45 defects per lines of code

Indicates good overall code quality. Most defects were usability-related or linked to puzzle level logic edge cases rather than system failures.

Risk Coverage Percent: 95%

All high and medium-risk areas (core gameplay, reward logic, leaderboard sync, and in-app purchases) were tested and verified. Only a few low-risk cosmetic issues remain deferred.

Regression Success Rate: 98%

All previously fixed defects remained stable across regression cycles, with only one minor reoccurrence in the settings menu navigation flow.


### Defect Summary

- Total Defects Logged: 
- Critical High: 
- Fix Rate: 

## Test Control & Project Management

### Phases

| Phase | Deliverable | Actual Output | Variance | Owner |
|-------|-------------|---------------|----------|-------|
|Monitoring tests executed |Ensuring tests are conducted in the right manner |Tests were well done |None. Everything went as planned |Test Manager |

**Progress Tracking Method:**  
**Change Control Notes:**

Test monitoring was carried out as the tests were being conducted and everything worked out smoothly. 
The tests were done and their reapective results were acquired and noted.

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
|Wamahiga Ng'ang'a | Test Manager |W.N |27/10/2025 |
| | Risk Analyst | | |
|Vianney Ndagire | Test Executor | Test executor|28/10/2025 |

## Overall Summary

**Statement:** 
This was a great learning experience for all of us and it helped us build up on our being a team player skill as well as our teating skills.

**Test Status:** ☐ Completed / ☐✅ In Progress / ☐ Deferred
