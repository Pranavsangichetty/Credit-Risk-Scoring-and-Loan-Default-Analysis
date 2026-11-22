# Day 6 — ML Execution, 5-Fold Validation and Model Comparison

**Contributor:** Nivesh  
**Role:** ML / Model Development  
**Project:** Credit Risk Scoring and Loan Default Analysis  
**Date:** 21 November 2026

## Assigned responsibilities
1. Execute Logistic Regression and Random Forest.
2. Generate actual stratified 5-fold validation metrics.
3. Compare ROC-AUC, PR-AUC, bad-class precision, recall and F1.
4. Share threshold analysis and subgroup results.
5. Provide `outputs/cross_validation_metrics.json` and an updated results report.

## Experimental protocol
The supplied target `Risk` is mapped as `good = 0` and `bad = 1`; bad is treated as the positive class. The script performs stratified five-fold cross-validation and obtains out-of-fold probabilities so each row is evaluated by a model that did not train on that row. Numeric and categorical preprocessing is fitted inside each fold through a scikit-learn pipeline.

## Models
- Logistic Regression with balanced class weights.
- Random Forest with 500 trees, minimum leaf size 3 and balanced class weights.

## Evaluation
The execution script calculates out-of-fold ROC-AUC and average precision (PR-AUC), fold-level ROC-AUC and PR-AUC mean/standard deviation, and bad-class precision, recall and F1 at threshold 0.50. It also evaluates thresholds 0.20, 0.30, 0.40, 0.50, 0.60, 0.70 and 0.80.

## Subgroup review
Where available, results are broken down by Sex and age bands. Each row includes sample size, actual bad-label count, predicted bad count, precision, recall and F1. These descriptive results require sample-size review and do not establish fairness.

## Run command
```bash
python -m pip install -r requirements.txt
python src/nivesh_ml_validation.py --data german_credit_data.csv
```

## Deliverables generated after execution
- `outputs/cross_validation_metrics.json`
- `outputs/model_comparison.csv`
- `outputs/threshold_analysis.csv`
- `outputs/subgroup_metrics.csv`
- `outputs/oof_predictions.csv`
- `outputs/roc_curve_5fold.png`
- `outputs/precision_recall_curve_5fold.png`
- `reports/Nivesh_Day4_Day6_ML_Results.md`

## Results status
**Pending execution against the original project dataset.** Numerical scores are intentionally not included in this document before execution. Do not submit estimated or illustrative values as actual model results.

## Limitations
The source target is a historical `good`/`bad` risk label. It is not automatically equivalent to a measured future loan-default event. This work is an educational historical-label classification exercise, not a validated production lending system.
