# Nivesh — Days 6–11 Final ML Evaluation

- Dataset: `german_credit_data.csv`
- SHA-256: `42be3b82a2e5073bd5ca23bce1d1c31426b78f72d20cd892f3aacaa2ba30a075`
- Rows: 1000 | Features: 9 | Good: 700 | Bad: 300
- Development rows: 800 | Holdout rows: 200
- Python: 3.11.18 | pandas: 3.1.1 | NumPy: 2.4.6 | scikit-learn: 1.9.1
- Positive class: `Risk = bad` (1)
- Thresholds are selected using development out-of-fold predictions only.
- Model selection by development CV PR-AUC: **Random Forest**

## Development 5-fold metrics

| model               | metric            |   mean |    std |
|:--------------------|:------------------|-------:|-------:|
| Logistic Regression | bad_f1            | 0.5625 | 0.0544 |
| Logistic Regression | balanced_accuracy | 0.6815 | 0.0467 |
| Logistic Regression | pr_auc            | 0.5551 | 0.0751 |
| Logistic Regression | roc_auc           | 0.7453 | 0.0620 |
| Random Forest       | bad_f1            | 0.5788 | 0.0474 |
| Random Forest       | balanced_accuracy | 0.6973 | 0.0383 |
| Random Forest       | pr_auc            | 0.5665 | 0.0683 |
| Random Forest       | roc_auc           | 0.7569 | 0.0602 |

## Final holdout comparison

| model               |   development_cv_roc_auc_mean |   development_cv_roc_auc_std |   development_cv_pr_auc_mean |   development_cv_pr_auc_std |   development_cv_balanced_accuracy_mean |   development_cv_bad_f1_mean |   selected_threshold_from_development_oof |   holdout_roc_auc |   holdout_pr_auc |   holdout_bad_precision_at_0_50 |   holdout_bad_recall_at_0_50 |   holdout_bad_f1_at_0_50 |   holdout_bad_precision_at_selected_threshold |   holdout_bad_recall_at_selected_threshold |   holdout_bad_f1_at_selected_threshold |
|:--------------------|------------------------------:|-----------------------------:|-----------------------------:|----------------------------:|----------------------------------------:|-----------------------------:|------------------------------------------:|------------------:|-----------------:|--------------------------------:|-----------------------------:|-------------------------:|----------------------------------------------:|-------------------------------------------:|---------------------------------------:|
| Random Forest       |                        0.7569 |                       0.0602 |                       0.5665 |                      0.0683 |                                  0.6973 |                       0.5788 |                                    0.4500 |            0.7855 |           0.6475 |                          0.5062 |                       0.6833 |                   0.5816 |                                        0.4792 |                                     0.7667 |                                 0.5897 |
| Logistic Regression |                        0.7453 |                       0.0620 |                       0.5551 |                      0.0751 |                                  0.6815 |                       0.5625 |                                    0.4500 |            0.7614 |           0.6132 |                          0.5172 |                       0.7500 |                   0.6122 |                                        0.4796 |                                     0.7833 |                                 0.5949 |

## Threshold analysis

| model               |   threshold |   accuracy |   balanced_accuracy |   bad_precision |   bad_recall |   bad_f1 |   tn |   fp |   fn |   tp |   predicted_bad |
|:--------------------|------------:|-----------:|--------------------:|----------------:|-------------:|---------:|-----:|-----:|-----:|-----:|----------------:|
| Logistic Regression |      0.1000 |     0.3300 |              0.5179 |          0.3078 |       0.9875 |   0.4693 |   27 |  533 |    3 |  237 |             770 |
| Logistic Regression |      0.1500 |     0.3762 |              0.5449 |          0.3209 |       0.9667 |   0.4818 |   69 |  491 |    8 |  232 |             723 |
| Logistic Regression |      0.2000 |     0.4512 |              0.5938 |          0.3481 |       0.9500 |   0.5095 |  133 |  427 |   12 |  228 |             655 |
| Logistic Regression |      0.2500 |     0.5038 |              0.6193 |          0.3676 |       0.9083 |   0.5234 |  185 |  375 |   22 |  218 |             593 |
| Logistic Regression |      0.3000 |     0.5563 |              0.6485 |          0.3929 |       0.8792 |   0.5431 |  234 |  326 |   29 |  211 |             537 |
| Logistic Regression |      0.3500 |     0.5975 |              0.6661 |          0.4153 |       0.8375 |   0.5552 |  277 |  283 |   39 |  201 |             484 |
| Logistic Regression |      0.4000 |     0.6188 |              0.6717 |          0.4279 |       0.8042 |   0.5586 |  302 |  258 |   47 |  193 |             451 |
| Logistic Regression |      0.4500 |     0.6587 |              0.6932 |          0.4595 |       0.7792 |   0.5781 |  340 |  220 |   53 |  187 |             407 |
| Logistic Regression |      0.5000 |     0.6725 |              0.6815 |          0.4694 |       0.7042 |   0.5633 |  369 |  191 |   71 |  169 |             360 |
| Logistic Regression |      0.5500 |     0.7050 |              0.6893 |          0.5065 |       0.6500 |   0.5693 |  408 |  152 |   84 |  156 |             308 |
| Logistic Regression |      0.6000 |     0.7212 |              0.6711 |          0.5347 |       0.5458 |   0.5402 |  446 |  114 |  109 |  131 |             245 |
| Logistic Regression |      0.6500 |     0.7388 |              0.6682 |          0.5756 |       0.4917 |   0.5303 |  473 |   87 |  122 |  118 |             205 |
| Logistic Regression |      0.7000 |     0.7300 |              0.6262 |          0.5789 |       0.3667 |   0.4490 |  496 |   64 |  152 |   88 |             152 |
| Logistic Regression |      0.7500 |     0.7312 |              0.6009 |          0.6168 |       0.2750 |   0.3804 |  519 |   41 |  174 |   66 |             107 |
| Logistic Regression |      0.8000 |     0.7250 |              0.5655 |          0.6667 |       0.1667 |   0.2667 |  540 |   20 |  200 |   40 |              60 |
| Logistic Regression |      0.8500 |     0.7150 |              0.5357 |          0.7000 |       0.0875 |   0.1556 |  551 |    9 |  219 |   21 |              30 |
| Logistic Regression |      0.9000 |     0.7013 |              0.5057 |          0.5714 |       0.0167 |   0.0324 |  557 |    3 |  236 |    4 |               7 |
| Random Forest       |      0.1000 |     0.3250 |              0.5131 |          0.3057 |       0.9833 |   0.4664 |   24 |  536 |    4 |  236 |             772 |
| Random Forest       |      0.1500 |     0.3850 |              0.5524 |          0.3245 |       0.9708 |   0.4864 |   75 |  485 |    7 |  233 |             718 |
| Random Forest       |      0.2000 |     0.4500 |              0.5905 |          0.3466 |       0.9417 |   0.5067 |  134 |  426 |   14 |  226 |             652 |
| Random Forest       |      0.2500 |     0.4963 |              0.6140 |          0.3639 |       0.9083 |   0.5197 |  179 |  381 |   22 |  218 |             599 |
| Random Forest       |      0.3000 |     0.5500 |              0.6440 |          0.3893 |       0.8792 |   0.5396 |  229 |  331 |   29 |  211 |             542 |
| Random Forest       |      0.3500 |     0.6000 |              0.6690 |          0.4174 |       0.8417 |   0.5580 |  278 |  282 |   38 |  202 |             484 |
| Random Forest       |      0.4000 |     0.6488 |              0.6920 |          0.4518 |       0.8000 |   0.5774 |  327 |  233 |   48 |  192 |             425 |
| Random Forest       |      0.4500 |     0.7000 |              0.7131 |          0.5000 |       0.7458 |   0.5987 |  381 |  179 |   61 |  179 |             358 |
| Random Forest       |      0.5000 |     0.7113 |              0.6973 |          0.5146 |       0.6625 |   0.5792 |  410 |  150 |   81 |  159 |             309 |
| Random Forest       |      0.5500 |     0.7225 |              0.6804 |          0.5349 |       0.5750 |   0.5542 |  440 |  120 |  102 |  138 |             258 |
| Random Forest       |      0.6000 |     0.7400 |              0.6607 |          0.5842 |       0.4625 |   0.5163 |  481 |   79 |  129 |  111 |             190 |
| Random Forest       |      0.6500 |     0.7425 |              0.6351 |          0.6197 |       0.3667 |   0.4607 |  506 |   54 |  152 |   88 |             142 |
| Random Forest       |      0.7000 |     0.7488 |              0.6205 |          0.6857 |       0.3000 |   0.4174 |  527 |   33 |  168 |   72 |             105 |
| Random Forest       |      0.7500 |     0.7212 |              0.5545 |          0.6735 |       0.1375 |   0.2284 |  544 |   16 |  207 |   33 |              49 |
| Random Forest       |      0.8000 |     0.6987 |              0.5086 |          0.4706 |       0.0333 |   0.0623 |  551 |    9 |  232 |    8 |              17 |
| Random Forest       |      0.8500 |     0.7000 |              0.5024 |          0.5000 |       0.0083 |   0.0164 |  558 |    2 |  238 |    2 |               4 |
| Random Forest       |      0.9000 |     0.7000 |              0.5000 |          0.0000 |       0.0000 |   0.0000 |  560 |    0 |  240 |    0 |               0 |

## Holdout subgroup diagnostics

| model               | attribute   | group   |   n |   actual_bad |   predicted_bad |   bad_precision |   bad_recall |   bad_f1 | note   |
|:--------------------|:------------|:--------|----:|-------------:|----------------:|----------------:|-------------:|---------:|:-------|
| Logistic Regression | Sex         | female  |  61 |           20 |              40 |          0.4500 |       0.9000 |   0.6000 |        |
| Logistic Regression | Sex         | male    | 139 |           40 |              58 |          0.5000 |       0.7250 |   0.5918 |        |
| Logistic Regression | Age band    | 18-25   |  44 |           20 |              30 |          0.5333 |       0.8000 |   0.6400 |        |
| Logistic Regression | Age band    | 26-35   |  66 |           21 |              32 |          0.5625 |       0.8571 |   0.6792 |        |
| Logistic Regression | Age band    | 36-50   |  61 |           14 |              20 |          0.4500 |       0.6429 |   0.5294 |        |
| Logistic Regression | Age band    | 51+     |  29 |            5 |              16 |          0.2500 |       0.8000 |   0.3810 |        |
| Random Forest       | Sex         | female  |  61 |           20 |              35 |          0.4571 |       0.8000 |   0.5818 |        |
| Random Forest       | Sex         | male    | 139 |           40 |              61 |          0.4918 |       0.7500 |   0.5941 |        |
| Random Forest       | Age band    | 18-25   |  44 |           20 |              29 |          0.4828 |       0.7000 |   0.5714 |        |
| Random Forest       | Age band    | 26-35   |  66 |           21 |              33 |          0.5455 |       0.8571 |   0.6667 |        |
| Random Forest       | Age band    | 36-50   |  61 |           14 |              20 |          0.5000 |       0.7143 |   0.5882 |        |
| Random Forest       | Age band    | 51+     |  29 |            5 |              14 |          0.2857 |       0.8000 |   0.4211 |        |

Subgroup figures are descriptive diagnostics only; they do not establish fairness or legal suitability. Small groups may be unstable.

## Leakage and reproducibility notes

- Imputation, scaling and one-hot encoding are inside each scikit-learn pipeline and refitted within each training fold.
- The holdout set is excluded from threshold selection and model selection.
- Dataset SHA-256, Python/package versions, seed and split/class counts are recorded in the JSON output.
- Manual domain review is still required to rule out semantic/post-outcome leakage in source features.

## Limitations

The target is the dataset's historical good/bad Risk label. It is not established here as a directly observed future-default event with a defined horizon. This is an educational classification exercise, not a validated production lending model.

## Generated evidence

- `outputs/final_evaluation_metrics.json`
- `outputs/final_model_comparison.csv`
- `outputs/stratified_5fold_metrics_by_fold.csv`
- `outputs/development_oof_threshold_analysis.csv`
- `outputs/holdout_predictions.csv`
- `outputs/holdout_subgroup_metrics.csv`
- Holdout ROC/PR plots and fitted model artifacts in `outputs/`
