# Lab 6: Code and Branch Coverage Analysis Report

**Course / Lab**: Software Testing & Automation (Lab 6)  
**Student Name**: Chidvilas Adi  
**Email**: siddu252789@gmail.com  
**Repository**: [Chidvilas-Adi/L6_L7_62_attendance_eligibility](https://github.com/Chidvilas-Adi/L6_L7_62_attendance_eligibility)  
**Target Module**: `attendance_eligibility.py`  

---

## 1. Executive Summary

This report documents the code and branch coverage analysis conducted on the `attendance_eligibility.py` application. Using `pytest` and Python's `coverage` library, two dedicated test suites were designed and evaluated:
1. **`CodeCoverageTest_attendance_eligibility.py`**: Validates statement/line execution across the application.
2. **`BranchCoverageTest_attendance_eligibility.py`**: Exercises both boolean branches (`True` and `False`) across all conditional decision points.

Both test suites achieved **100% coverage** (surpassing the mandatory $\ge 90\%$ rubric threshold).

---

## 2. Theoretical Background

| Metric | Definition | Significance |
| :--- | :--- | :--- |
| **Line / Statement Coverage** | Measures the percentage of executable lines passed through during test execution. | Confirms whether statements run at least once; does not guarantee that every logical permutation has been verified. |
| **Branch Coverage** | Measures whether every branch of each control structure (e.g., `if`, `elif`, `else`) evaluates to both `True` and `False`. | Prevents false security from line coverage by exposing untested logic and unhandled boundary paths. |

---

## 3. Test Design & Analysis Strategy

The `attendance_eligibility.py` module consists of three primary business logic functions:
1. `attendance_percent(attended, total, medical_leave)`
2. `exam_eligibility(percent, condonation, fees_paid)`
3. `attendance_warning(percent, weeks_left)`

### 3.1 Line Coverage Test Strategy (`CodeCoverageTest_attendance_eligibility.py`)
- **Total Test Cases**: 16 unit tests
- **Validation Scope**:
  - **Input Guard Clauses**: Raised `ValueError` exceptions for non-positive class totals (`total <= 0`), negative attendance counts (`attended < 0`), and attendance exceeding the total (`attended > total`).
  - **Business Rules**:
    - Medical leave capped at an upper limit of 5 days.
    - Credited attendance capped strictly at the total class count.
    - Fee clearance priority: Unpaid fees (`fees_paid=False`) immediately return `"fees pending"`, bypassing attendance percentages.
    - Standard eligibility: $\ge 75\%$ returns `"eligible"`.
    - Condonation logic: $65\% \le \text{percent} < 75\%$ returns `"eligible"` if condonation is granted, or `"condonation required"` if not granted.
    - Detention limit: $< 65\%$ returns `"detained"`.
    - Warning tiers: $\ge 85\%$ returns `None`; $75\% \le \text{percent} < 85\%$ triggers `"reminder"`; $< 75\%$ triggers `"critical"` ($> 4$ weeks left) or `"final notice"` ($\le 4$ weeks left).

### 3.2 Branch Coverage Test Strategy (`BranchCoverageTest_attendance_eligibility.py`)
- **Total Test Cases**: 17 unit tests (including parameterized boundaries)
- **Validation Scope (Exercising Both Branch Outcomes)**:
  - `total <= 0`: Evaluated with $0$ and $-1$ (`True` branch) vs valid totals (`False` branch).
  - `attended < 0 or attended > total`: Evaluated both negative out-of-range (`-1`) and above-total (`11` for total 10) conditions.
  - `medical_leave > 5`: Tested with `medical_leave = 5` (`False` branch) and `medical_leave = 6` (`True` branch).
  - `credited > total`: Tested capping at `total` (`True` branch) vs below `total` (`False` branch).
  - `not fees_paid`: Tested both `True` (fees pending) and `False` (fees cleared).
  - `percent >= 75`: Tested boundary value $75$ and values $< 75$.
  - `condonation` check: Tested $65\% \le \text{percent} < 75\%$ with `condonation=True` and `condonation=False`.
  - `weeks_left > 4`: Tested with $5$ weeks (`True` $\rightarrow$ critical) and $4$ weeks (`False` $\rightarrow$ final notice).

---

## 4. Execution Metrics & Results

### 4.1 Statement Coverage Results
- **Command**:
  ```bash
  coverage erase
  coverage run --source=attendance_eligibility -m pytest CodeCoverageTest_attendance_eligibility.py
  coverage report -m
  ```
- **Report Table**:
  ```text
  ============================= test session starts ==============================
  platform linux -- Python 3.13.18, pytest-8.4.2, pluggy-1.7.0
  rootdir: /content/L6_L7_62_attendance_eligibility/LAB6
  collected 16 items

  CodeCoverageTest_attendance_eligibility.py ................               [100%]

  ============================== 16 passed in 0.07s ==============================
  Name                         Stmts   Miss  Cover   Missing
  ----------------------------------------------------------
  attendance_eligibility.py       29      0   100%
  ----------------------------------------------------------
  TOTAL                           29      0   100%
  ```
- **Outcome**: **100% Statement Coverage** (29/29 statements executed, 0 missed).

### 4.2 Branch Coverage Results
- **Command**:
  ```bash
  coverage erase
  coverage run --branch --source=attendance_eligibility -m pytest BranchCoverageTest_attendance_eligibility.py
  coverage report -m
  ```
- **Report Table**:
  ```text
  ============================= test session starts ==============================
  platform linux -- Python 3.13.18, pytest-8.4.2, pluggy-1.7.0
  rootdir: /content/L6_L7_62_attendance_eligibility/LAB6
  collected 17 items

  BranchCoverageTest_attendance_eligibility.py .................           [100%]

  ============================== 17 passed in 0.08s ==============================
  Name                         Stmts   Miss Branch BrPart  Cover   Missing
  ------------------------------------------------------------------------
  attendance_eligibility.py       29      0     22      0   100%
  ------------------------------------------------------------------------
  TOTAL                           29      0     22      0   100%
  ```
- **Outcome**: **100% Branch Coverage** (22/22 decision branches fully exercised, 0 partial branches).

---

## 5. Artifacts and Deliverables Checklist

| Rubric Requirement | File Name | Status |
| :--- | :--- | :--- |
| **Code Coverage Test Suite** | `LAB6/CodeCoverageTest_attendance_eligibility.py` | Complete (16 tests, 100% coverage) |
| **Branch Coverage Test Suite** | `LAB6/BranchCoverageTest_attendance_eligibility.py` | Complete (17 tests, 100% branch coverage) |
| **Code Coverage Screenshot** | `LAB6/coverage_report_code.png` | Captured (Shows 16 passed, 100% cover) |
| **Branch Coverage Screenshot** | `LAB6/coverage_report_branch.png` | Captured (Shows 17 passed, 22/22 branches covered) |
| **Minimum 2 Commits** | Git Commit Log | Commit 1 (Code Coverage) & Commit 2 (Branch Coverage) |