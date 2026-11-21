# Day 2 — Data Quality and Missingness Audit

## Scope
Read-only data quality checks on `german_credit_data.csv`. The raw dataset was not modified.

## Missingness
- `Saving accounts`: 183 missing (18.3%).
- `Checking account`: 394 missing (39.4%).
- All other columns: no missing values.

### Missingness by Risk
| Column | Risk | Total | Missing | Missing % |
|---|---|---:|---:|---:|
| Saving accounts | bad | 300 | 32 | 10.67% |
| Saving accounts | good | 700 | 151 | 21.57% |
| Checking account | bad | 300 | 46 | 15.33% |
| Checking account | good | 700 | 348 | 49.71% |

Missingness rates differ between the Risk groups. This is a descriptive association and does not establish causation.

## Duplicate Checks
- Full-row duplicates: 0
- Duplicates excluding `Unnamed: 0`: 0

## Basic Value Checks
- Age <= 0: 0
- Job outside 0–3: 0
- Credit amount <= 0: 0
- Duration <= 0: 0
- Risk values other than `good` or `bad`: 0

## Numeric Ranges
| Column | Min | Max |
|---|---:|---:|
| Age | 19 | 75 |
| Job | 0 | 3 |
| Credit amount | 250 | 18424 |
| Duration | 4 | 72 |

## Category Frequencies
- Sex: male 690, female 310
- Housing: own 713, rent 179, free 108
- Saving accounts: little 603, moderate 103, quite rich 63, rich 48, missing 183
- Checking account: missing 394, little 274, moderate 269, rich 63
- Purpose: car 337, radio/TV 280, furniture/equipment 181, business 97, education 59, repairs 22, domestic appliances 12, vacation/others 12
- Risk: good 700, bad 300

## Decision / Next Steps
- Keep the raw CSV unchanged.
- Do not impute missing values or remove columns in this audit step.
- Review and agree on a missing-value handling strategy before cleaning.
- Confirm the meaning of the `Job` codes from an authoritative dataset description before assigning labels.
