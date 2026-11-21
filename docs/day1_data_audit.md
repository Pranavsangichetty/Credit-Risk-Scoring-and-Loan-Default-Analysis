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

## Day 1 — Follow-up verification

### Column names and index
- Printed column names contain no leading or trailing whitespace.
- `Unnamed: 0` contains unique sequential values from 0 through 999.
- It appears to be a row index. Exclude it from modeling only after documenting that decision; preserve the original CSV unchanged.

### Categorical values observed
- `Sex`: `female`, `male`
- `Housing`: `free`, `own`, `rent`
- `Saving accounts`: `little`, `moderate`, `quite rich`, `rich`
- `Checking account`: `little`, `moderate`, `rich`
- `Purpose`: `business`, `car`, `domestic appliances`, `education`, `furniture/equipment`, `radio/TV`, `repairs`, `vacation/others`
- `Risk`: `bad`, `good`

### Numeric ranges observed
| Field | Minimum | Maximum |
|---|---:|---:|
| Age | 19 | 75 |
| Job | 0 | 3 |
| Credit amount | 250 | 18,424 |
| Duration | 4 | 72 |

`Job` is stored as an integer-coded field; confirm the meaning of each code before interpreting it as a numeric measurement.

### Missingness by target
| Field | Risk | Missing | Total | Missing share |
|---|---|---:|---:|---:|
| Saving accounts | good | 151 | 700 | 21.6% |
| Saving accounts | bad | 32 | 300 | 10.7% |
| Checking account | good | 348 | 700 | 49.7% |
| Checking account | bad | 46 | 300 | 15.3% |

Missingness differs across the observed target groups. Investigate and document a handling strategy; these counts alone do not establish why values are missing or which treatment is best.

### Day 1 status
Initial dataset audit and follow-up checks completed. Cleaning and modeling have not been performed.
