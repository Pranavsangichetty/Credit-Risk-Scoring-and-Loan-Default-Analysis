# Day9 Rerun Validation Leakage Check

**Project:** Credit Risk Scoring and Loan Default Analysis  
**Assigned owner:** Nivesh — ML / Model Development  
**Dataset:** `german_credit_data.csv`  
**Models:** Logistic Regression and Random Forest  
**Target:** `Risk` (`bad` = positive class 1; `good` = class 0)

> **Results integrity:** This is a day-specific submission record and execution specification. Do not fill in guessed scores. Actual metrics must be copied from the generated output files after running the workflow against the repository's original dataset.

## Reproduce
From the repository root, install dependencies and run:

```bash
python -m pip install -r requirements.txt
python src/run_final_evaluation.py --data german_credit_data.csv
```

The script writes the numerical evidence under `outputs/` and the consolidated report under `reports/`.

# Day 9 — Re-run, validate and check preprocessing leakage

## Objective
Re-run Logistic Regression and Random Forest, verify stratified five-fold validation and audit preprocessing leakage.

## Leakage checks
- The target column `Risk` is removed from the predictor matrix before training.
- Imputation, scaling and one-hot encoding are inside each scikit-learn `Pipeline`.
- Each cross-validation fold fits preprocessing only on that fold's training rows.
- The hold-out partition is not used for fitting, feature preprocessing or threshold selection.
- Check the feature list for identifiers or fields that could reveal the target.
- Review feature timing/domain meaning manually: pipeline design cannot detect a predictor recorded after the outcome.

## Evidence files
- `outputs/final_evaluation_metrics.json` (including leakage audit/configuration)
- `outputs/stratified_5fold_metrics_by_fold.csv`
- `outputs/run_metadata.json` (if emitted by the execution version)

## Result entry
Record the actual run timestamp, random seed, dataset row count and audit findings after execution.
