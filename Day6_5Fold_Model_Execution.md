# Day6 5Fold Model Execution

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

# Day 6 — Model execution and 5-fold cross-validation

## Objective
Execute Logistic Regression and Random Forest and evaluate their performance using five-fold cross-validation.

## Work performed by the workflow
1. Load the original credit-risk dataset and validate the `Risk` target.
2. Encode `bad` as 1 and `good` as 0.
3. Build separate preprocessing/model pipelines for Logistic Regression and Random Forest.
4. Run five-fold validation on the development data and calculate fold-level metrics.
5. Consolidate mean and standard deviation of the cross-validation metrics.

## Metrics to report
ROC-AUC, PR-AUC (average precision), bad-class precision, bad-class recall, bad-class F1, accuracy and balanced accuracy.

## Evidence files
- `outputs/stratified_5fold_metrics_by_fold.csv`
- `outputs/final_evaluation_metrics.json`

## Result entry
Actual scores are pending execution on the repository dataset. Do not report assumed or illustrative numbers as measured results.
