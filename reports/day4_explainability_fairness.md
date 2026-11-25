# Day 4 — Explainability and Fairness Analysis

## 1. Objective

The objective of Day 4 is to explain the Random Forest credit-risk model using SHAP and evaluate model performance across different customer subgroups based on Sex and Age.

## 2. SHAP Analysis

SHAP (SHapley Additive exPlanations) was used to understand how individual features contribute to the model's bad-risk prediction.

The trained Random Forest model was analyzed after applying the same preprocessing pipeline used during model training.

### SHAP output files

- `outputs/shap/shap_summary.png`
- `outputs/shap/shap_feature_importance.png`
- `outputs/shap/shap_feature_importance.csv`

## 3. Important Features from SHAP

The main features with the highest mean absolute SHAP values were:

| Feature | Mean Absolute SHAP |
|---|---:|
| Checking account — Unknown | 0.09477 |
| Duration | 0.06270 |
| Checking account — little | 0.04780 |
| Credit amount | 0.03782 |
| Saving accounts — little | 0.03238 |
| Age | 0.02278 |
| Housing — own | 0.01803 |
| Checking account — moderate | 0.01787 |
| Saving accounts — Unknown | 0.01708 |
| Purpose — radio/TV | 0.01505 |

### Feature interpretation

- **Checking account:** Checking-account categories have a strong influence on the model's bad-risk prediction.
- **Duration:** Higher loan duration generally contributes more toward bad-risk prediction.
- **Credit amount:** Higher credit amounts generally show a stronger contribution toward bad-risk prediction.
- **Saving accounts:** The `little` savings category has a relatively strong contribution.
- **Age:** Age has a measurable influence on the prediction. Lower age values tend to contribute more toward bad-risk prediction in the SHAP analysis.
- **Housing:** The `own` housing category has a noticeable contribution, mainly toward lower bad-risk prediction.
- **Purpose:** Some loan-purpose categories, particularly `radio/TV`, have a measurable contribution.

SHAP values represent model contribution and do not prove that a feature causes loan default.

## 4. Sex Subgroup Fairness Analysis

The model was evaluated separately for female and male customers.

| Sex | Samples | Actual Bad Rate | Predicted Bad Rate | Accuracy | Precision | Recall | F1 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Female | 310 | 35.16% | 39.68% | 85.16% | 75.61% | 85.32% | 80.17% |
| Male | 690 | 27.68% | 29.13% | 87.54% | 76.12% | 80.10% | 78.06% |

### Observation

The female subgroup has a higher actual bad-risk rate and a higher predicted bad-risk rate than the male subgroup. Model performance is relatively similar across the two groups, although recall is higher for the female subgroup.

## 5. Age Subgroup Fairness Analysis

Customers were divided into three age groups:

- Young: `<30`
- Middle: `30–44`
- Older: `45+`

| Age Group | Samples | Actual Bad Rate | Predicted Bad Rate | Accuracy | Precision | Recall | F1 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Young (<30) | 371 | 36.93% | 42.05% | 83.02% | 73.72% | 83.94% | 78.50% |
| Middle (30–44) | 428 | 26.40% | 25.70% | 89.49% | 80.91% | 78.76% | 79.82% |
| Older (45+) | 201 | 24.88% | 28.86% | 88.06% | 72.41% | 84.00% | 77.78% |

### Observation

The Young subgroup has the highest actual and predicted bad-risk rates. The model performance varies across age groups, with the Middle subgroup having the highest accuracy and the Young subgroup having the lowest accuracy.

## 6. Fairness Summary

The subgroup analysis shows differences in prediction rates and performance metrics across Sex and Age groups.

These differences should be treated as areas for further investigation rather than direct evidence that the model is unfair. Additional evaluation using an independent holdout dataset and formal fairness metrics would provide a stronger fairness assessment.

## 7. Limitation

The subgroup analysis in this step was performed on the complete dataset of 1,000 records. Therefore, these results are descriptive and should not be treated as unbiased holdout-set performance estimates.

The model was also loaded using scikit-learn 1.9.1 while it was originally saved using scikit-learn 1.8.0, which generated an `InconsistentVersionWarning`. The analysis completed successfully despite this warning.

## 8. Output Files

The following files were generated during Day 4:

- `outputs/shap/shap_summary.png`
- `outputs/shap/shap_feature_importance.png`
- `outputs/shap/shap_feature_importance.csv`
- `outputs/fairness/sex_fairness_results.csv`
- `outputs/fairness/age_fairness_results.csv`

## 9. Conclusion

SHAP analysis provided model-level explanations of the most influential features in the Random Forest credit-risk model. Fairness analysis compared model behavior across Sex and Age subgroups.

The results provide an explainability and subgroup-performance assessment that can be used for further model review and documentation.