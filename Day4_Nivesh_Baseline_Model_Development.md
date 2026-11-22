# Day 4 — Baseline Model Development

**Contributor:** Nivesh  
**Role:** ML / Model Development

## Objective
Build baseline classifiers for the historical credit-risk label using Logistic Regression and Random Forest.

## Preprocessing
- Remove exported unnamed index columns.
- Map `Risk`: `good = 0`, `bad = 1`.
- Numeric columns: median imputation and standard scaling.
- Categorical columns: impute missing values as `Unknown` and apply one-hot encoding.
- Fit preprocessing only on training folds using scikit-learn Pipelines.

## Models
- Logistic Regression with balanced class weights.
- Random Forest with balanced class weights.

## Evaluation
The complete executable workflow in `src/nivesh_ml_validation.py` performs stratified 5-fold out-of-fold evaluation and reports ROC-AUC, average precision, bad-class precision, recall, F1 and balanced accuracy. Threshold analysis is included.

## Execution
```bash
python -m pip install -r requirements.txt
python src/nivesh_ml_validation.py --data german_credit_data.csv
```

Actual results must be taken from the generated files. No estimated values are reported here.
