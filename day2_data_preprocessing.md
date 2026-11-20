# Day 2 — Data Cleaning and Preprocessing Plan

**Owner:** Nivesh — ML and Model Development  
**Project:** Credit Risk Scoring and Loan Default Analysis  
**Dataset:** `german_credit_data.csv`  
**Branch:** `Nivesh243`

## Objective
Prepare a reliable preprocessing approach for numeric and categorical predictors while preventing information leakage from validation data.

## Data preparation decisions
- Remove columns whose names begin with `Unnamed:`, because they represent an exported index.
- Remove rows only when the target `Risk` is missing.
- Normalize target text by trimming whitespace and converting it to lowercase.
- Map only the expected labels: `good = 0` and `bad = 1`.
- Raise an error if unexpected target labels are found.

## Missing-value strategy
| Feature type | Preprocessing |
|---|---|
| Numeric | Median imputation |
| Categorical | Replace missing values with the explicit category `Unknown` |

The missing values in Savings and Checking accounts represent unavailable categorical information. They should not be converted to numeric zero.

## Leakage prevention
Preprocessing must be fitted only on the training portion of each split. The project implementation uses scikit-learn Pipelines and a ColumnTransformer so imputers, scaling and encoding are learned inside each training fold.

## Train/test design
For the initial baseline evaluation:
- 80% training data and 20% test data.
- Stratified split to preserve the target class proportions.
- Random seed: 42.

For cross-validation, preprocessing is re-fitted independently inside each fold.

## Deliverable
A documented preprocessing design that is implemented in `src/train_baseline.py` and reused by the validation script.

## Quality checks
- Confirm the target contains both classes.
- Confirm only expected target labels are present.
- Confirm exported index columns are excluded.
- Confirm missing-value handling is inside the model pipeline rather than performed using the full dataset before splitting.
