# Day 3 — Cleaning and Preprocessing Log

## Input and output
- Input: `german_credit_data.csv` (raw file left unchanged)
- Raw shape: 1000 rows × 11 columns
- Output: `data/interim/german_credit_cleaned.csv`
- Output shape: 1000 rows × 10 columns

## Transformations
- Removed `Unnamed: 0` from the working copy only; audit identified it as a sequential index.
- Replaced missing values in categorical columns with the explicit label `Missing` for EDA.
- No rows were dropped; no numeric values were imputed or changed.
- No model imputer or encoder was fitted. Those must be fitted on training data only in the model pipeline.

## Before/after missingness
| Column | Raw missing | Working-copy missing |
|---|---:|---:|
| Unnamed: 0 | 0 | — (column removed) |
| Age | 0 | 0 |
| Sex | 0 | 0 |
| Job | 0 | 0 |
| Housing | 0 | 0 |
| Saving accounts | 183 | 0 |
| Checking account | 394 | 0 |
| Credit amount | 0 | 0 |
| Duration | 0 | 0 |
| Purpose | 0 | 0 |
| Risk | 0 | 0 |
