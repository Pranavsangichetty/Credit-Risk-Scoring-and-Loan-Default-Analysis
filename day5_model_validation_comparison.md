# Day 5 — Model Validation and Performance Comparison

**Owner:** Nivesh — ML and Model Development  
**Project:** Credit Risk Scoring and Loan Default Analysis  
**Date:** 20 November 2026  
**Branch:** `Nivesh243`

## Assigned task
Run Logistic Regression and Random Forest, perform 5-fold validation and compare model performance.

## Models evaluated
- Logistic Regression
- Random Forest Classifier

Both use the shared preprocessing pipeline. The validation script uses class weighting and a fixed random seed.

## Validation method
- StratifiedKFold with 5 splits.
- Shuffling enabled.
- Random seed: 42.
- Out-of-fold predicted probabilities generated with `cross_val_predict`.
- Preprocessing is contained within the pipeline and is re-fitted separately for each fold.

This keeps validation-fold information out of the preprocessing fit.

## Metrics and comparison
For each model, the script calculates:
- ROC-AUC
- Average precision (PR-AUC)
- Bad-class precision, recall and F1 at threshold 0.50
- Balanced accuracy
- Threshold analysis at 0.25, 0.35, 0.45, 0.50, 0.60 and 0.70

Threshold analysis makes the precision/recall trade-off visible. A threshold should not be selected as a lending policy from this educational experiment alone.

## Fairness-related subgroup review
The validation script also reports bad-class precision and recall by:
- Sex
- Age bands: 18–25, 26–35, 36–50 and 51+

Subgroup counts must be reviewed alongside metrics. Small groups can produce unstable estimates. This analysis is descriptive and does not establish that a model is fair or legally suitable.

## Run instructions
From the repository root:

```bash
python -m pip install -r requirements.txt
python src/validate_baseline.py --data german_credit_data.csv
```

The script writes:
- `outputs/cross_validation_metrics.json`

It prints the headline ROC-AUC, PR-AUC and threshold-0.50 metrics for both models.

## Model comparison rule
Compare models using ROC-AUC and PR-AUC together with bad-class precision, recall, F1 and balanced accuracy. Do not choose a model using accuracy alone. The operational importance of false negatives and false positives should be discussed with the project team.

## Results
Populate the final comparison with the values produced by the executed validation script. Do not enter estimated or illustrative scores as actual results.

| Metric | Logistic Regression | Random Forest |
|---|---:|---:|
| ROC-AUC | Pending execution | Pending execution |
| PR-AUC (average precision) | Pending execution | Pending execution |
| Bad precision (threshold 0.50) | Pending execution | Pending execution |
| Bad recall (threshold 0.50) | Pending execution | Pending execution |
| Bad F1 (threshold 0.50) | Pending execution | Pending execution |
| Balanced accuracy | Pending execution | Pending execution |

## Interpretation and limitation
The supplied `Risk` field is a historical good/bad label, not a documented future-default outcome with a defined observation window. Therefore, results should be described as exploratory historical credit-risk classification. They should not be represented as validated future-default prediction or used as an automated lending policy.
