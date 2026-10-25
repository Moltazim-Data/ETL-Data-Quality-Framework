# Data Quality Audit — Reconciled Demo Run

> **Data note:** These metrics were recalculated from the repository's generated synthetic dataset. They are not a production assessment.

- Records ingested: 1,200
- Records passing core validation: 845
- Pass rate: 70.42%

## Validation findings

- Missing user ID: 32
- Invalid email: 120
- Missing engagement score: 70
- Out-of-range engagement score (including missing values): 157
- Invalid last-login date: 100
- Missing region: 240
- Duplicate rows: 0

## Cleaning policy

Rows are excluded if the user ID is missing, the email format is invalid, the engagement score is missing or outside 0–100, or the last-login date cannot be parsed. Blank regions are retained as `Unknown`. Exact duplicate rows are removed.

**Metric note:** Issue counts overlap because one row may fail multiple checks. The out-of-range score count includes missing scores because missing values do not pass the numeric range check.
