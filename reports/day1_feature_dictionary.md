# Day 1 — Feature Dictionary and Explainability

**Owner:** Sirisha — Explainability & Documentation  
**Project:** Credit Risk Scoring and Loan Default Analysis  
**Dataset:** `german_credit_data.csv`

## 1. Credit-Risk Modelling and Explainability

Credit-risk modelling in this project focuses on classifying the historical `Risk` label as `good` or `bad` using the available dataset features.

The dataset contains 1,000 observations with numerical and categorical analytical features. The `Risk` column is used as the prediction target.

Model explainability helps us understand why a machine-learning model produces a particular risk prediction. It can help identify which input features influence the model's prediction and make the model's decision easier to interpret.

## 2. SHAP

**SHAP (SHapley Additive exPlanations)** is a method used to explain machine-learning model predictions.

In this project, SHAP may be used later to:

- Identify which features have the greatest influence on a prediction.
- Understand the contribution of individual features to a model prediction.
- Explain individual customer-level risk predictions.
- Improve the interpretability of the credit-risk model.

SHAP will be considered after the machine-learning model has been developed and evaluated.

## 3. Dataset Feature Dictionary

| Feature | Type | Meaning |
|---|---|---|
| `Age` | Numerical | Age of the applicant. |
| `Job` | Numerical | Job-related value recorded for the applicant. |
| `Credit amount` | Numerical | Credit amount recorded for the applicant. |
| `Duration` | Numerical | Duration of the credit/loan. |
| `Sex` | Categorical | Sex category recorded for the applicant. |
| `Housing` | Categorical | Housing category recorded for the applicant. |
| `Saving accounts` | Categorical | Saving-account category recorded for the applicant. |
| `Checking account` | Categorical | Checking-account category recorded for the applicant. |
| `Purpose` | Categorical | Purpose of the credit/loan. |
| `Risk` | Target | Historical good/bad risk label. |

### Target Label

The `Risk` column is the historical good/bad risk label.

| Original label | Encoded value |
|---|---:|
| `good` | 0 |
| `bad` | 1 |

Therefore, `bad = 1` is the positive class.

### Excluded Column

The first unnamed CSV column is an exported row index and is not a meaningful predictor. It should therefore be excluded from the model features.

## 4. Dataset Limitations

### Dataset Size

The dataset contains **1,000 observations**. Its size should be considered when interpreting model results and their generalisation.

### Historical Risk Labels

The `Risk` column represents a historical good/bad risk label. It is not, by itself, a measured future-default outcome with a defined observation horizon.

Therefore, the historical label should be treated as a historical classification label rather than automatically as a direct measurement of future loan default.

### Missing Categorical Values

The project records missing markers in:

- `Saving accounts` — 183
- `Checking account` — 394

These missing categorical values should not be interpreted as zero account balances.

## 5. Potential Fairness Concerns

### Age

`Age` is included as a numerical feature and may influence model predictions. Its influence should be examined to identify whether predictions behave differently across age groups.

### Sex

`Sex` is included as a categorical feature. Its influence should also be monitored because demographic attributes can create potential fairness concerns in credit-risk modelling.

Further analysis can be used later to check whether model predictions differ systematically across groups.

## 6. Summary

The German Credit dataset contains numerical and categorical features used to predict the historical `Risk` label.

The feature dictionary documents the meaning and type of the analytical features. Explainability methods such as SHAP may later be used to understand which features influence model predictions.

The dataset size, historical nature of the `Risk` labels, missing categorical values, and potential fairness concerns involving `Age` and `Sex` should be considered when interpreting the model.