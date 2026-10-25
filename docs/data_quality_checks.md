# Data Quality Checks

Use this checklist when reviewing the ETL pipeline:

- **Schema:** confirm required columns exist and expected types are usable.
- **Completeness:** quantify missing values in required fields.
- **Uniqueness:** identify duplicate business keys or records.
- **Validity:** check dates, numeric ranges, and allowed categories.
- **Consistency:** verify relationships and cross-field rules.
- **Reconciliation:** compare input, accepted, rejected, and output row counts.

## Operational guidance
Keep rejected rows and validation messages available for diagnosis. Record row counts and check outcomes for each run, and avoid silently dropping invalid data.
