# Day7 Stratified CV Comparison Threshold Analysis

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

# Day 7 — Stratified cross-validation, model comparison and threshold analysis

## Objective
Run stratified five-fold cross-validation, compare both classifiers and investigate decision thresholds.

## Work performed by the workflow
1. Preserve class proportions using `StratifiedKFold` with five folds and a fixed random seed.
2. Generate out-of-fold predicted probabilities for the development partition.
3. Compare Logistic Regression and Random Forest using fold-level and aggregated metrics.
4. Evaluate multiple probability thresholds using development out-of-fold predictions.
5. Select a candidate threshold using development bad-class F1, with recall and threshold as tie-breakers.

## Evidence files
- `outputs/stratified_5fold_metrics_by_fold.csv`
- `outputs/final_model_comparison.csv`
- `outputs/development_oof_threshold_analysis.csv`
- `outputs/oof_predictions.csv`

## Interpretation
A lower threshold can increase bad-class recall while also increasing false positives. The threshold must be selected using development data only; the hold-out set must not influence threshold selection.

## Result entry
Actual fold metrics and the recommended threshold are pending execution on the original dataset.
