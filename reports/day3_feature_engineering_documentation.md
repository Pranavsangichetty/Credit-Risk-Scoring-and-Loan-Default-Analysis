## 1. Engineered Features

The feature engineering process created transformed and grouped features for credit-risk analysis.

| Engineered Feature | Meaning |
|---|---|
| `checking_status` | Checking account status |
| `duration_bin` | Binned credit duration |
| `saving_status` | Saving account status |
| `credit_bin` | Binned credit amount |
| `age_bin` | Binned age |
| `housing` | Housing category |
| `payment_bin` | Binned monthly payment |
| `purpose_group` | Grouped credit purpose |

Eight engineered features were selected for the final WoE-based analysis.

## 2. WoE and IV Analysis

Weight of Evidence (WoE) and Information Value (IV) were used to evaluate how well each feature separates good and bad credit-risk customers.

### Information Value (IV) Results

| Feature | IV | Decision |
|---|---:|---|
| `checking_status` | 0.662 | Selected |
| `duration_bin` | 0.230 | Selected |
| `saving_status` | 0.189 | Selected |
| `credit_bin` | 0.142 | Selected |
| `age_bin` | 0.093 | Selected |
| `housing` | 0.084 | Selected |
| `payment_bin` | 0.077 | Selected |
| `purpose_group` | 0.066 | Selected |
| `sex` | 0.027 | Excluded |
| `job_group` | 0.008 | Excluded |

The eight features selected for the final WoE-based analysis were `checking_status`, `duration_bin`, `saving_status`, `credit_bin`, `age_bin`, `housing`, `payment_bin`, and `purpose_group`.

The `low_balance_profile` feature was also excluded because it overlaps with checking account status (`r = 0.64`).

## 3. Important Features

The final model used eight selected features. Feature importance was evaluated using IV, drop-one AUC loss, and model contribution share.

### Overall Feature Importance

| Feature | IV | Drop-one AUC Loss | Contribution Share |
|---|---:|---:|---:|
| `checking_status` | 0.662 | 0.0603 | 28.5% |
| `duration_bin` | 0.230 | 0.0041 | 11.9% |
| `saving_status` | 0.189 | 0.0054 | 12.7% |
| `credit_bin` | 0.142 | 0.0093 | 13.0% |
| `age_bin` | 0.093 | 0.0039 | 8.6% |
| `housing` | 0.084 | 0.0022 | 6.3% |
| `payment_bin` | 0.077 | 0.0095 | 12.3% |
| `purpose_group` | 0.066 | 0.0015 | 6.7% |

### Key Findings

- `checking_status` is the most important feature across the analysis, with the highest IV (0.662), highest drop-one AUC loss (0.0603), and highest contribution share (28.5%).
- `credit_bin`, `saving_status`, and `payment_bin` also make meaningful contributions to the model.
- `purpose_group` and `housing` have smaller but still useful contributions.
- The full model using all eight selected features achieved a ROC-AUC of **0.774**.

## 4. Feature Importance and Explainability Notes

Feature importance helps explain which customer characteristics contribute most to the credit-risk model's predictions.

### Explainability Summary

- **`checking_status`** has the strongest overall importance. It contributes the most to distinguishing between good and bad credit-risk customers.
- **`credit_bin`** represents the customer's credit amount and has a meaningful contribution to the model.
- **`saving_status`** provides useful information about the customer's financial position.
- **`payment_bin`** captures information related to the customer's monthly payment level.
- **`duration_bin`** represents the duration of the credit and contributes to risk prediction.
- **`age_bin`** provides additional customer-level risk information.
- **`housing`** and **`purpose_group`** have lower contribution shares but remain useful selected features.

### Features Excluded from the Final Analysis

- **`low_balance_profile`** was excluded because it overlaps with `checking_status` (correlation `r = 0.64`).
- **`sex`** was excluded as a protected characteristic and was not used in the final selected feature set.
- **`job_group`** was excluded because its IV was below 0.02, indicating very limited predictive signal.

### Model Explainability

The feature importance results can be used to explain model predictions by identifying which selected credit-related features have the greatest influence on risk assessment. This supports transparent and interpretable credit-risk analysis.

## 5. Key Observations

- The feature engineering process transformed the original credit-related variables into grouped and binned features suitable for WoE-based analysis.
- Eight engineered features were selected for the final analysis based on their predictive usefulness.
- `checking_status` was the strongest feature according to IV, drop-one AUC loss, and contribution share.
- The full model using the eight selected features achieved a ROC-AUC of **0.774**.
- `low_balance_profile` was excluded because of overlap with `checking_status`.
- `sex` was excluded from the final feature set as a protected characteristic.
- `job_group` was excluded because it showed very low predictive signal.
- Feature importance results provide useful explanations for understanding which factors contribute most to credit-risk predictions.