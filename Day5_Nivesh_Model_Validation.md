# Day 5 — Model Validation and Comparison

**Contributor:** Nivesh  
**Role:** ML / Model Development

## Objective
Validate Logistic Regression and Random Forest using stratified 5-fold cross-validation and compare model performance.

## Validation approach
StratifiedKFold uses five folds, shuffling and random state 42. Out-of-fold probabilities are generated so each observation receives a prediction from a model that did not train on it. All imputation, scaling and encoding occur inside the pipeline and are refitted within each fold.

## Metrics
- ROC-AUC
- PR-AUC (average precision)
- Bad-class precision, recall and F1 at threshold 0.50
- Fold mean and standard deviation for ROC-AUC and PR-AUC
- Threshold analysis from 0.20 through 0.80
- Subgroup metrics for Sex and age bands where available

## Execution
```bash
python -m pip install -r requirements.txt
python src/nivesh_ml_validation.py --data german_credit_data.csv
```

The script creates `outputs/cross_validation_metrics.json` and supporting CSV/PNG files, then writes the results report. The report must be generated from the executed results, not manually populated with estimated scores.
