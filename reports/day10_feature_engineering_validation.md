# Day 10 — Feature Engineering and WoE/IV Validation

**Owner:** Lav Kumar — Data Cleaning and Documentation
**Project:** Credit Risk Scoring and Loan Default Analysis
**Validation date:** 26 November 2026
**Source:** `german_credit_data.csv`
**Engineered output:** `data/processed/german_credit_engineered.csv`
**WoE output:** `data/processed/german_credit_woe.csv`
**WoE/IV summary:** `data/processed/woe_iv_tables.csv`

## 1. Validation summary

The Day 9 feature-engineering and feature-importance notebooks were executed successfully. The saved notebooks contain no cell errors. The following checks were run against the raw and generated CSV files.

| Check | Observed result | Status |
|---|---:|---|
| Raw dataset size | 1,000 rows × 11 columns | Passed |
| Engineered dataset size | 1,000 rows × 26 columns | Passed |
| WoE dataset size | 1,000 rows × 9 columns | Passed |
| WoE/IV summary size | 37 rows × 9 columns | Passed |
| Duplicate rows in raw dataset | 0 | Passed |
| Duplicate rows in engineered dataset | 0 | Passed |
| Missing values in WoE dataset | 0 | Passed |
| Missing values in WoE/IV summary | 0 | Passed |
| Engineered `bad` label matches `Risk` mapping | Yes | Passed |
| WoE target matches engineered target row by row | Yes | Passed |
| WoE feature values are finite | Yes | Passed |

## 2. Missing-value handling

The raw dataset contains 577 missing values: 183 in `Saving accounts` and 394 in `Checking account`.

The engineered dataset retains those nulls in the original source columns. The derived fields handle them explicitly:
- `checking_status` represents missing checking-account entries as `no account` (394 records).
- `saving_status` represents missing savings-account entries as `no record` (183 records).

The WoE dataset contains no missing values. This report does not claim that the original source columns in the engineered dataset are null-free.

## 3. Target and output consistency

The raw and engineered datasets each contain 700 `good` and 300 `bad` records. The engineered `bad` field matches the mapping `good → 0`, `bad → 1`.

The WoE output retains the same target distribution, and its `bad` column matches the engineered target row by row. The WoE output contains eight feature columns plus the target.

The WoE output has 154 repeated full rows. Identical encoded feature patterns and target labels can occur for different customers; this count alone does not establish duplicate source records.

## 4. Feature selection and reported analysis

Notebook 06 reports eight selected features:
- Checking account status
- Duration
- Saving account status
- Credit amount
- Age
- Housing
- Monthly payment
- Purpose group

The notebook reports checking account status as the strongest feature (IV 0.659; drop-one ROC-AUC loss 0.0603). It excludes `low_balance_profile` due to overlap with checking account status, `Sex` as a protected characteristic, and `job_group` for low IV.

Notebook 06 reports cross-validated ROC-AUC of 0.774 using repeated 5-fold validation. This is the notebook's reported result, not an independently reproduced model evaluation in this report.

## 5. Limitations and follow-up

- The WoE/IV and feature-importance outputs were checked for structure, target consistency, missing values, and finite numeric values.
- The checks here do not independently recompute every WoE/IV value or the model metrics.
- Feature binning and selection were performed before the cross-validation used for the reported model results. The reported ROC-AUC should therefore be treated as preliminary; a fully leakage-safe evaluation should fit binning, WoE transformations, and feature selection inside each training fold.
- The dataset target is a historical `good` / `bad` label, not a directly observed future default event with a defined prediction horizon.
- This educational analysis must not be used for real lending decisions.

## 6. Conclusion

The generated outputs have consistent row counts and target labels, and the WoE dataset has no missing or non-finite values. The derived account-status fields explicitly represent missing account information. The Day 9 outputs are suitable for further review, subject to the modelling limitations and follow-up work above.
