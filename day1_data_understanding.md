# Day 1 — Data Understanding and Target Definition

**Owner:** Nivesh — ML and Model Development  
**Project:** Credit Risk Scoring and Loan Default Analysis  
**Dataset:** `german_credit_data.csv`  
**Branch:** `Nivesh243`

## Objective
Understand the dataset structure and define the prediction target before building machine-learning models.

## Dataset overview
The repository's Day 4 project report records the dataset as 1,000 observations with these analytical columns:

- Numeric: `Age`, `Job`, `Credit amount`, `Duration`
- Categorical: `Sex`, `Housing`, `Saving accounts`, `Checking account`, `Purpose`
- Target: `Risk`

The reported target distribution is 700 `good` and 300 `bad`.

## Target definition
The supplied `Risk` column is the historical good/bad risk label. For modelling, use this mapping:

| Original label | Encoded value |
|---|---:|
| good | 0 |
| bad | 1 |

The positive class is therefore `bad = 1`. Evaluation should pay particular attention to how well the model identifies this class.

## Initial data observations
- The first unnamed CSV column is an exported row index, not a meaningful predictor.
- The project report records 183 missing markers in `Saving accounts` and 394 in `Checking account`.
- These missing categorical values must not be interpreted as zero account balances.

## Decisions for the ML workflow
1. Use `Risk` as the target.
2. Exclude the exported unnamed index from model features.
3. Keep the original good/bad label meaning documented.
4. Treat this as historical credit-risk label classification. The supplied label is not, by itself, a measured future-default outcome with a defined observation horizon.

## Deliverable
This document records the target definition, feature inventory and initial data considerations used to plan preprocessing and modelling.

## Reproducibility
The dataset and implementation are maintained in the repository. The data-loading code validates the expected target labels and fails clearly if unexpected labels are present.
