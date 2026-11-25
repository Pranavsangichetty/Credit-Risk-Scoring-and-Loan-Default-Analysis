# Day 5 — Executed Model Validation, Threshold and Subgroup Results

**Owner:** Nivesh — ML / Model Development  
**Dataset:** `german_credit_data.csv`  
**Rows evaluated:** 1000  
**Validation:** 5-fold stratified out-of-fold predictions  
**Random state:** 42  

## Executive summary

Both Logistic Regression and Random Forest were evaluated using stratified five-fold out-of-fold predictions. The figures below are generated directly from the execution output; no metric values are manually entered.

## Model comparison

| model               |   roc_auc |   pr_auc_average_precision |   bad_precision_at_0_50 |   bad_recall_at_0_50 |   bad_f1_at_0_50 |   balanced_accuracy_at_0_50 |
|:--------------------|----------:|---------------------------:|------------------------:|---------------------:|-----------------:|----------------------------:|
| random_forest       |    0.7607 |                     0.5975 |                  0.5116 |               0.6633 |           0.5776 |                      0.6960 |
| logistic_regression |    0.7410 |                     0.5462 |                  0.4842 |               0.7133 |           0.5768 |                      0.6938 |

The positive class is `bad = 1`. Precision measures how many records predicted as bad were labelled bad; recall measures how many labelled-bad records were identified. F1 is their harmonic mean. ROC-AUC measures ranking across thresholds; average precision summarizes the precision-recall curve.

## Threshold analysis

| model               |   threshold |   precision_bad |   recall_bad |   f1_bad |   balanced_accuracy |
|:--------------------|------------:|----------------:|-------------:|---------:|--------------------:|
| logistic_regression |      0.2500 |          0.3717 |       0.8933 |   0.5250 |              0.6231 |
| logistic_regression |      0.3500 |          0.4224 |       0.8533 |   0.5651 |              0.6767 |
| logistic_regression |      0.4500 |          0.4602 |       0.7700 |   0.5761 |              0.6914 |
| logistic_regression |      0.5000 |          0.4842 |       0.7133 |   0.5768 |              0.6938 |
| logistic_regression |      0.6000 |          0.5180 |       0.5767 |   0.5457 |              0.6733 |
| logistic_regression |      0.7000 |          0.5803 |       0.3733 |   0.4544 |              0.6288 |
| random_forest       |      0.2500 |          0.3691 |       0.8933 |   0.5224 |              0.6195 |
| random_forest       |      0.3500 |          0.4255 |       0.8467 |   0.5663 |              0.6783 |
| random_forest       |      0.4500 |          0.4834 |       0.7300 |   0.5817 |              0.6979 |
| random_forest       |      0.5000 |          0.5116 |       0.6633 |   0.5776 |              0.6960 |
| random_forest       |      0.6000 |          0.5800 |       0.4833 |   0.5273 |              0.6667 |
| random_forest       |      0.7000 |          0.7200 |       0.3000 |   0.4235 |              0.6250 |

Lowering the threshold generally increases the number of records flagged as bad and can increase recall while reducing precision. Thresholds are diagnostic comparisons only; they are not lending-policy recommendations.

## Subgroup results at threshold 0.50

| model               | dimension   | group   |   n |   bad_label_count |   bad_precision |   bad_recall | note                                                      |
|:--------------------|:------------|:--------|----:|------------------:|----------------:|-------------:|:----------------------------------------------------------|
| logistic_regression | sex         | female  | 310 |               109 |          0.5244 |       0.7890 | Interpret cautiously; small subgroup counts are unstable. |
| logistic_regression | sex         | male    | 690 |               191 |          0.4604 |       0.6702 | Interpret cautiously; small subgroup counts are unstable. |
| logistic_regression | age_band    | 18-25   | 190 |                80 |          0.5385 |       0.7875 | Interpret cautiously; small subgroup counts are unstable. |
| logistic_regression | age_band    | 26-35   | 398 |               118 |          0.4722 |       0.7203 | Interpret cautiously; small subgroup counts are unstable. |
| logistic_regression | age_band    | 36-50   | 299 |                71 |          0.4312 |       0.6620 | Interpret cautiously; small subgroup counts are unstable. |
| logistic_regression | age_band    | 51+     | 113 |                31 |          0.5278 |       0.6129 | Interpret cautiously; small subgroup counts are unstable. |
| random_forest       | sex         | female  | 310 |               109 |          0.5106 |       0.6606 | Interpret cautiously; small subgroup counts are unstable. |
| random_forest       | sex         | male    | 690 |               191 |          0.5121 |       0.6649 | Interpret cautiously; small subgroup counts are unstable. |
| random_forest       | age_band    | 18-25   | 190 |                80 |          0.5085 |       0.7500 | Interpret cautiously; small subgroup counts are unstable. |
| random_forest       | age_band    | 26-35   | 398 |               118 |          0.5211 |       0.6271 | Interpret cautiously; small subgroup counts are unstable. |
| random_forest       | age_band    | 36-50   | 299 |                71 |          0.5227 |       0.6479 | Interpret cautiously; small subgroup counts are unstable. |
| random_forest       | age_band    | 51+     | 113 |                31 |          0.4634 |       0.6129 | Interpret cautiously; small subgroup counts are unstable. |

Subgroup results are descriptive. Review each subgroup sample size (`n`) and bad-label count before interpreting differences. Small groups can produce unstable estimates. This table does not establish fairness, absence of bias, or legal suitability.

## Reproducibility

```bash
python -m pip install -r requirements.txt
python src/train_baseline.py --data german_credit_data.csv
python src/validate_baseline.py --data german_credit_data.csv
python src/build_ml_report.py
```

Generated files:
- `outputs/metrics.json` — stratified 80:20 hold-out results.
- `outputs/holdout_predictions.csv` — hold-out predictions.
- `outputs/cross_validation_metrics.json` — pooled out-of-fold metrics, thresholds and subgroup statistics.
- `outputs/model_comparison.csv` — side-by-side model metrics.
- `outputs/threshold_analysis.csv` — threshold comparison.
- `outputs/subgroup_metrics.csv` — sex and age-band subgroup metrics.

## Limitations

Exploratory cross-validation for the supplied historical good/bad risk label; not validated future-default prediction. Thresholds are diagnostic and must not be treated as lending policy.

The source target is a historical `good` / `bad` credit-risk label. It is not documented here as a directly observed future loan-default event with a defined outcome horizon. Results are exploratory educational classification results, not a validated production lending model. Protected attributes such as Sex and proxy variables require careful governance and legal review before any real-world use.
