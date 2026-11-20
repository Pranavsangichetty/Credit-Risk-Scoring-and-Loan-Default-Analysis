# Day 3 — Feature Preparation and Model Pipeline

**Owner:** Nivesh — ML and Model Development  
**Project:** Credit Risk Scoring and Loan Default Analysis  
**Dataset:** `german_credit_data.csv`  
**Branch:** `Nivesh243`

## Objective
Convert mixed numeric and categorical inputs into model-ready features using a reproducible pipeline.

## Feature groups
The current project schema identifies:

**Numeric features**
- Age
- Job
- Credit amount
- Duration

**Categorical features**
- Sex
- Housing
- Saving accounts
- Checking account
- Purpose

**Target**
- Risk

## Numeric transformation
The numeric preprocessing pipeline applies:
1. Median imputation for missing numeric values.
2. StandardScaler to standardize numeric feature scales.

Scaling is particularly relevant for Logistic Regression because its optimization can be affected by different feature magnitudes.

## Categorical transformation
The categorical preprocessing pipeline applies:
1. Constant imputation with the category `Unknown`.
2. One-hot encoding.
3. `handle_unknown="ignore"` so categories not seen during fitting do not cause prediction-time errors.

## Combined pipeline
A ColumnTransformer applies the appropriate transformations to each feature group. The transformed features are passed to the selected estimator in a scikit-learn Pipeline.

This design ensures that preprocessing is fitted only on the training data in a hold-out split or individual cross-validation fold.

## Models prepared
- Logistic Regression with class weighting.
- Random Forest with class weighting.

The current baseline implementation uses a fixed random seed for reproducibility. Random Forest is configured with 400 trees and a minimum leaf size of 3.

## Deliverable
The reusable `build_pipeline()` function in `src/train_baseline.py`, which is also imported by `src/validate_baseline.py`.

## Important note
Feature encoding is part of the training pipeline. Do not separately one-hot encode the entire dataset before cross-validation, because that would allow information from validation folds to influence preprocessing.
