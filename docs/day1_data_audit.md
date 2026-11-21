# Day 1 — Initial Dataset Audit

## Dataset file
- File: `german_credit_data.csv`
- File size: 53,393 bytes
- Audit status: Initial inspection completed
- Raw file: Preserved unchanged

## Structure
- Rows: 1,000
- Columns: 11
- Duplicate rows: 0

## Columns and data types

| Column | Data type | Missing values |
|---|---|---:|
| Unnamed: 0 | int64 | 0 |
| Age | int64 | 0 |
| Sex | object | 0 |
| Job | int64 | 0 |
| Housing | object | 0 |
| Saving accounts | object | 183 |
| Checking account | object | 394 |
| Credit amount | int64 | 0 |
| Duration | int64 | 0 |
| Purpose | object | 0 |
| Risk | object | 0 |

## Target distribution

| Risk label | Records | Share |
|---|---:|---:|
| good | 700 | 70% |
| bad | 300 | 30% |
| **Total** | **1,000** | **100%** |

## Initial findings
- Missing values are concentrated in `Saving accounts` and `Checking account`.
- The target labels are lowercase `good` and `bad`.
- `Unnamed: 0` may be an index column; verify its values and uniqueness before deciding whether to exclude it.
- Keep the raw CSV unchanged. Any cleaning should produce a separate processed file.

## Pending checks
- Verify the exact header spelling and whether any column name contains extra whitespace.
- Check whether `Unnamed: 0` is a sequential index.
- Inspect categorical values, numeric ranges, and missingness patterns.
- Record cleaning decisions and rationale before applying transformations.

## Scope note
This audit records observed CSV properties only. It does not establish causal relationships or model performance.
