# Credit Risk Scoring and Loan Default Analysis

An exploratory machine-learning project using the German Credit dataset to study the supplied historical credit-risk label (`good` / `bad`).

> **Important:** The dataset target is a historical risk category, not a directly observed future default event with a defined prediction horizon. This project should not be described as a validated future-default prediction system or used to make real lending decisions.

## Dataset

File: `german_credit_data.csv`

- 1,000 records
- 10 analytical fields: Age, Sex, Job, Housing, Saving accounts, Checking account, Credit amount, Duration, Purpose and Risk
- Target: `Risk` (`good` / `bad`)
- Target encoding used by the baseline: `good = 0`, `bad = 1`
- Missing markers appear in Saving accounts and Checking account; handle them explicitly.
- The exported first column is a row index, not a predictive feature.

## Team responsibilities

| Member | Focus |
|---|---|
| Pranav Kumar | Team lead, coordination and integration |
| Lav Kumar | Data engineering and EDA |
| Divya | Statistical analysis and feature engineering |
| Nivesh | ML and model development |
| Sirisha | Explainability and documentation |
| Raj | BI and dashboard |

## Branch workflow

- `main`: shared stable project branch.
- `Pranavsangichetty`: project coordination, milestones and integration documentation.
- `Nivesh243`: ML preprocessing and baseline modelling.
- Contributor work should be committed to the assigned branch and reviewed through pull requests. Do not push unreviewed work directly to `main`.

## Day 1–Day 4 progress

See [Project Lead Tracker](reports/day1-day4_project_lead_tracker.md) for the milestone plan, dataset facts, decisions, review checklist and next steps.

The baseline model implementation and run instructions are maintained on the `Nivesh243` branch in `src/train_baseline.py` and `reports/day4_baseline_model.md`.

## Evaluation principles

Report the bad-risk class precision, recall and F1, ROC-AUC, PR-AUC and balanced accuracy. Use stratified train/test splitting and keep imputation/encoding inside the model pipeline to avoid leakage. Treat all results as exploratory because the dataset is small.

## Responsible-use note

The source includes Age and Sex. Any analysis involving these attributes requires careful fairness, legal and governance review. Do not use this educational project for real credit approval or denial.
