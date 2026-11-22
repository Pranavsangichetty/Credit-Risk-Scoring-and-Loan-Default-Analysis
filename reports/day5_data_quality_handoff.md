# Day 5 — Data-Quality Handoff

**Owner:** Lav Kumar — Data Cleaning and Documentation
**Project:** Credit Risk Scoring and Loan Default Analysis
**Dataset:** `german_credit_data.csv`
**Cleaned output:** `data/interim/german_credit_cleaned.csv`

## Objective
Provide a stable, reproducible cleaned dataset and summarize the quality checks before model validation and feature review.

## Cleaning summary
- Raw dataset: 1,000 rows × 11 columns.
- Cleaned dataset: 1,000 rows × 10 columns.
- Removed the exported `Unnamed: 0` index from the working copy; the raw file remains unchanged.
- Replaced missing categorical values in `Saving accounts` and `Checking account` with the explicit `Missing` label.
- Dropped no rows and changed no numeric values.
- No imputer or encoder was fitted during cleaning; model preprocessing must be fitted on training data only.

## Quality-check results
| Check | Result |
|---|---|
| Cleaned dataset shape | 1,000 rows × 10 columns |
| Missing values in cleaned dataset | 0 |
| Duplicate rows in cleaned dataset | 0 |
| `Risk` class counts | 700 `good`, 300 `bad` |
| Target classes present | Both `good` and `bad` |
| Exported index column | Excluded |

## Missing-value note
The raw dataset contained 183 missing values in `Saving accounts` and 394 in `Checking account`. These were retained as the categorical label `Missing`; they were not converted to zero or treated as measured account balances.

## Handoff
The cleaned dataset is available at `data/interim/german_credit_cleaned.csv`. The cleaning steps and before/after missingness are documented in `reports/day3_transformation_log.md`. The EDA findings are documented in `reports/day4_eda_summary.md`.

This handoff records the verified data-quality checks. It does not claim that model validation, feature selection, or binning has been completed.
