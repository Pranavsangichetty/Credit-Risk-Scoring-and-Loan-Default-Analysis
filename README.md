# Nivesh — Credit Risk ML Model Development Submission

**Project:** Credit Risk Scoring and Loan Default Analysis  
**Owner:** Nivesh — ML / Model Development  
**Scope:** Day 4 baseline modelling and Day 5–6 validation deliverables

## Important status
This package contains the executable validation workflow and documentation. It does **not** contain fabricated model scores or a substitute dataset. Run it against the project's actual `german_credit_data.csv` to create the final numerical results.

## Run
Place `german_credit_data.csv` in the project root, then:

```bash
python -m pip install -r requirements.txt
python src/nivesh_ml_validation.py --data german_credit_data.csv
```

## Models and validation
- Logistic Regression (`class_weight="balanced"`)
- Random Forest (500 trees; `class_weight="balanced"`)
- Stratified 5-fold cross-validation
- Out-of-fold predicted probabilities
- Positive class: `Risk == "bad"` encoded as 1
- Threshold analysis: 0.20 to 0.80
- Subgroup analysis: `Sex` and age bands when available

Preprocessing is part of each scikit-learn pipeline. Numeric columns are median-imputed and scaled; categorical columns are imputed with `Unknown` and one-hot encoded. Each fold fits preprocessing only on its training partition.

## Generated output
- `outputs/cross_validation_metrics.json`
- `outputs/model_comparison.csv`
- `outputs/threshold_analysis.csv`
- `outputs/subgroup_metrics.csv`
- `outputs/oof_predictions.csv`
- `outputs/roc_curve_5fold.png`
- `outputs/precision_recall_curve_5fold.png`
- `reports/Nivesh_Day4_Day6_ML_Results.md`

## Metric interpretation
ROC-AUC measures ranking across thresholds. PR-AUC is reported as average precision. Bad-class precision measures the proportion of predicted-bad records that are actually labelled bad. Bad-class recall measures the proportion of actual bad-labelled records identified. F1 is the harmonic mean of precision and recall.

## Limitations
The supplied `Risk` field is a historical good/bad label. Unless the dataset documentation defines an observed future-default outcome and observation horizon, results must be described as historical credit-risk classification, not proven future-default prediction. Subgroup metrics are descriptive and do not establish fairness or legal suitability.
