# Day 4 — Baseline ML Development

**Owner:** Nivesh (ML and model development)  
**Date:** 19 November 2026  
**Branch:** `Nivesh243`

## Day 1–Day 4 ML workstream

| Day | Focus | ML deliverable / decision |
|---|---|---|
| Day 1 | Understand data and define prediction target | Use the provided `Risk` column. Map `good = 0` and `bad = 1`; confirm that this is a historical risk label. |
| Day 2 | Preprocessing design | Drop the exported row-index column. Treat `NA` in Savings and Checking accounts as missing categorical information. Split before fitting preprocessing. |
| Day 3 | Encoding and model-ready features | Median-impute numeric features, explicitly impute missing categories as `Unknown`, one-hot encode categoricals and scale numeric features inside a pipeline. |
| Day 4 | Baseline modelling and evaluation | Add reproducible Logistic Regression and Random Forest baselines, stratified hold-out validation, class-sensitive metrics and saved predictions. |

## Dataset verification

The repository CSV contains 1,000 rows and these analytical columns:

- Numeric: Age, Job, Credit amount, Duration
- Categorical: Sex, Housing, Saving accounts, Checking account, Purpose
- Target: Risk

The source target distribution is 700 `good` and 300 `bad`. Missing marker counts are 183 for Saving accounts and 394 for Checking account. The blank/unnamed first CSV column is an exported index and is excluded from features.

## Run instructions

From the repository root:

```bash
python -m pip install -r requirements.txt
python src/train_baseline.py --data german_credit_data.csv
```

The script creates:

- `outputs/metrics.json` — hold-out metrics and experiment metadata
- `outputs/holdout_predictions.csv` — test-set labels and predicted bad-risk probabilities
- `outputs/logistic_regression.joblib` — fitted logistic-regression pipeline
- `outputs/random_forest.joblib` — fitted random-forest pipeline

Generated outputs are intentionally not committed as if they had already been run. Execute the script in the project environment and review the actual metrics before reporting results.

## Validation design

- 80/20 train/test split with stratification and random seed 42.
- Preprocessing is fitted only on the training partition through scikit-learn Pipelines.
- Logistic Regression and Random Forest use class weighting to account for the 70:30 class distribution.
- Report bad-class precision, recall and F1, ROC-AUC, average precision (PR-AUC), balanced accuracy and confusion matrix.
- The script uses a default probability threshold of 0.5 for class metrics. Threshold selection should be a separate, documented decision based on error costs.

## Interpretation and limitations

1. This dataset's `good` / `bad` target is not the same as a documented future default event with a defined observation horizon. Use “historical credit-risk label classification” in the report.
2. The dataset has only 1,000 observations; hold-out scores can vary. Add repeated or stratified cross-validation before selecting a final model.
3. Accuracy can hide poor detection of the bad-risk class. Discuss precision/recall trade-offs and the cost of false negatives.
4. Age and Sex are included in the source. Evaluate subgroup performance and fairness implications before any real-world use.
5. These baselines are educational and exploratory, not validated lending decision systems.

## Day 4 completion checklist

- [x] Verify source CSV schema and target distribution.
- [x] Define target mapping and exclude exported index.
- [x] Implement leakage-safe preprocessing pipeline.
- [x] Implement Logistic Regression and Random Forest baselines.
- [x] Add reproducible stratified hold-out evaluation and output generation.
- [ ] Execute in the team's Python environment and review generated metrics.
- [ ] Add cross-validation and threshold analysis after baseline review.
- [ ] Review subgroup/fairness metrics with the project team.
