# Day 6 — Feature Inventory and Proposed Binning Plan

**Owner:** Lav Kumar — Data Cleaning and Documentation
**Project:** Credit Risk Scoring and Loan Default Analysis
**Dataset:** `data/interim/german_credit_cleaned.csv`

## Objective
Provide a clear inventory of the cleaned dataset fields and propose candidate bins for review before feature engineering. This document records proposals only; no binning has been applied or evaluated.

## Feature inventory

| Field | Current type | Role | Notes |
|---|---|---|---|
| `Age` | Integer | Predictor | Numeric age in years |
| `Sex` | Categorical | Predictor | Keep as a category; review subgroup implications carefully |
| `Job` | Integer | Predictor | Dataset-coded job category; confirm its meaning before treating it as continuous |
| `Housing` | Categorical | Predictor | Housing category |
| `Saving accounts` | Categorical | Predictor | Includes `Missing` for unavailable values |
| `Checking account` | Categorical | Predictor | Includes `Missing` for unavailable values |
| `Credit amount` | Integer | Predictor | Numeric credit amount |
| `Duration` | Integer | Predictor | Credit duration in months |
| `Purpose` | Categorical | Predictor | Credit purpose category |
| `Risk` | Categorical | Target | Historical labels `good` and `bad`; exclude from predictor features |

The cleaned file has 1,000 rows and 10 columns. Its target counts are 700 `good` and 300 `bad`. The original exported index column is excluded.

## Proposed binning candidates

| Field | Candidate approach for review | Rationale / caution |
|---|---|---|
| `Age` | Compare interpretable age bands, for example under 25, 25–34, 35–44, 45–54, and 55+ | Review sample counts in each band; do not imply these are validated risk thresholds |
| `Credit amount` | Consider quantile-based bands fitted using training data only | Amount is right-skewed; derive cut points from training data and check stability |
| `Duration` | Compare interpretable month ranges, such as 4–12, 13–24, 25–36, and over 36 | Check observed ranges and counts before finalizing boundaries |
| `Job` | Keep the original coded values initially; compare categorical treatment with any justified ordered treatment | Do not assume the numeric codes represent equal intervals |

Do not bin categorical fields or the target. Do not choose cut points by inspecting test-set outcomes. If bins are adopted, learn any data-dependent cut points from each training fold and apply them to its validation fold.

## Review checklist
- [ ] Confirm field meanings and category labels against the dataset documentation.
- [ ] Inspect counts and missing-category frequencies before deciding on bins.
- [ ] Compare candidate binned features with the unbinned baseline.
- [ ] Record the selected boundaries, rationale, and validation evidence after testing.
- [ ] Keep `Risk` out of all predictor transformations.

## Status
This is a proposed feature-review plan, not a completed feature-engineering result. No bins, feature selection, or model-performance claims are reported here.
