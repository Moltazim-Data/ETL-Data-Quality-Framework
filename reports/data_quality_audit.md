# ETL & Data Quality Audit

**Portfolio project:** Abdelhamid Moltazim

## Results
- Records ingested: **1,200**
- Records passing core validation: **861**
- Core validation pass rate: **71.8%**

## Issues detected
| Check | Rows affected |
|---|---:|
| Missing user ID | 80 |
| Invalid email | 120 |
| Missing engagement score | 60 |
| Out-of-range engagement score | 112 |
| Invalid last-login date | 100 |
| Missing region | 265 |
| Duplicate rows | 16 |

## Design choice
Region is standardized to `Unknown` instead of rejecting an otherwise valid record.

> These figures are calculated from the supplied portfolio dataset, not from a real client production system.
