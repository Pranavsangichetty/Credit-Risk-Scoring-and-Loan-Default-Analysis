# Day 2 — Feature Documentation

**Owner:** Sirisha — Explainability & Documentation  
**Project:** Credit Risk Scoring and Loan Default Analysis  
**Dataset:** `german_credit_data.csv`

## 1. Features

The dataset contains the following analytical features:

- `Age`
- `Job`
- `Credit amount`
- `Duration`
- `Sex`
- `Housing`
- `Saving accounts`
- `Checking account`
- `Purpose`
- `Risk`

The exported `Unnamed: 0` column is not considered an analytical feature because it represents only the row number.

## 2. Data Types

| Feature | Data Type | Description |
|---|---|---|
| Age | Numeric | Age of the applicant |
| Job | Categorical | Job skill level/category |
| Credit amount | Numeric | Amount of credit requested |
| Duration | Numeric | Duration of the credit |
| Sex | Categorical | Sex of the applicant |
| Housing | Categorical | Housing status |
| Saving accounts | Categorical | Savings account category |
| Checking account | Categorical | Checking account category |
| Purpose | Categorical | Purpose of the credit |
| Risk | Categorical | Historical credit-risk label (`good` / `bad`) |

## 3. Missing Values

- Missing values are present in `Saving accounts` and `Checking account`.
- Instead of removing these observations, the missing values are retained as a separate category named `missing`.
- This allows the analysis to keep observations that contain missing account information.

## 4. Key Observations

- The exported `Unnamed: 0` column is a row number and is removed from the analysis.
- `Saving accounts` and `Checking account` missing values are retained as a separate `missing` category.
- `Job` is treated as a categorical feature by converting it to string type.
- Rare `Purpose` categories such as `repairs`, `domestic appliances`, and `vacation/others` are grouped into `other`.
- The `Risk` variable is converted into a binary `bad` indicator, where `bad = 1` and `good = 0`.