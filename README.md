# Lab 5: Static Code Analysis - Movie Theater Seat Reservation System

**Name:** Aanya
**SRN:** PES2UG24CS011

## About the program

`theater_system.py` is a seat reservation script for a small cinema. It reserves and releases seats for each show, generates a short ticket code and saves the seating plan to `seats.json`.

## Files

| File | Purpose |
|------|---------|
| `theater_system.py` | The program, with the issues fixed |
| `issues.md` | Table of the issues found and how each was fixed |
| `reflection.md` | Answers to the reflection questions |
| `pylint_report_before.txt`, `pylint_report_after.txt` | Pylint output before and after the fixes |
| `bandit_report_before.txt`, `bandit_report_after.txt` | Bandit output before and after the fixes |
| `flake8_report_before.txt`, `flake8_report_after.txt` | Flake8 output before and after the fixes |

## Commits

1. Original program and the "before" reports
2. Bandit fixes
3. Pylint fixes
4. Flake8 fixes
5. "After" reports, `issues.md` and `reflection.md`

## How to run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pylint bandit flake8
python theater_system.py
pylint theater_system.py
bandit -r theater_system.py
flake8 theater_system.py
```

## Results

| Tool | Before | After |
|------|--------|-------|
| Pylint | 5.87/10 | 10.00/10 |
| Bandit | 2 High, 1 Low | No issues identified |
| Flake8 | 11 warnings | 0 warnings |
