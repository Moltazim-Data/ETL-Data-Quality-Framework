# Portfolio Analysis Report — ETL Data Quality Framework

## Purpose
Show how raw events can be transformed into an analytical dataset with explicit quality checks and validation logs.

## Quality dimensions
- Missing user identifiers
- Malformed email addresses
- Engagement scores outside 0–100
- Traceability of raw-to-cleaned transformation

## Recommended report sections
1. Pipeline overview: raw, cleaned, and flagged row counts.
2. Quality scorecard: missingness, invalid formats, out-of-range values.
3. Issue breakdown by rule and severity.
4. Operational follow-up: upstream fixes versus downstream handling.

## Interpretation guardrails
The repository warns that sample artifacts are synthetic and historical figures may not match a newly generated sample. Run the pipeline and use current logs instead of treating stale figures as validated.

## Suggested action
Track each rule over time and assign ownership to recurring upstream defects.
