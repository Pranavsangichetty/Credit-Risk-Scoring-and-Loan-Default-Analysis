# Credit Risk Scoring and Loan Default Analysis

An exploratory data-analysis and machine-learning project using the German Credit dataset to study the supplied historical credit-risk label (`good` / `bad`).

> **Important:** The dataset target is a historical risk category, not a directly observed future default event with a defined prediction horizon. This educational project is not a validated future-default prediction system and must not be used to make real lending decisions.

## Project objective

Explore customer and credit attributes, understand their relationship with the supplied risk labels, prepare model-ready features, compare baseline classification models and communicate their limitations responsibly.

## Dataset

- File: `german_credit_data.csv`
- Records: 1,000
- Analytical fields: Age, Sex, Job, Housing, Saving accounts, Checking account, Credit amount, Duration, Purpose and Risk
- Target: `Risk` (`good` / `bad`)
- Baseline encoding: `good = 0`, `bad = 1`
- Missing values occur in Saving accounts and Checking account.
- The exported first column is a row index and should not be used as a predictive feature.

## Workflow

1. Data understanding and quality checks
2. Data cleaning and preprocessing
3. Exploratory and statistical analysis
4. Feature engineering, including WoE/IV analysis
5. Logistic Regression and Random Forest baseline modelling
6. Stratified validation and model comparison
7. Explainability, fairness diagnostics and dashboard/reporting

See [Project Architecture](docs/PROJECT_ARCHITECTURE.md) for the workflow and module boundaries.

## Repository workflow and integration policy

- `main` is the consolidated, shared project workspace. It should contain canonical, reviewed deliverables only.
- `Pranavsangichetty` is the team-lead branch for coordination records, worklogs and integration documentation.
- `lav-kumar`, `Divya-Akbari`, `Nivesh243`, `Sirisha` and the confirmed Raj branch are contributor development branches.
- We do **not** merge every file from every contributor branch automatically. Review the file-level diff and integrate only relevant, non-duplicative, sufficiently verified deliverables through focused pull requests.
- Keep drafts, temporary experiments, duplicate files, personal worklogs and unverified generated metrics on their source branch until they are ready.

Read the [Project Integration Checklist](docs/PROJECT_INTEGRATION_CHECKLIST.md) before submitting or reviewing a pull request.

## Current shared deliverables

- Divya's statistical-analysis and feature-engineering notebooks and PDF summaries are integrated through PR #9.
- Nivesh's baseline training/validation scripts and supporting ML documentation are integrated through PR #10.
- Day 6 project-lead coordination and integration status are recorded through PR #11.
- Day 8 selected ML execution outputs, metrics, threshold/subgroup summaries and report builder are integrated through PR #22.
- Lav's data-quality validation report is integrated through PR #25.
- Day 9 WoE/IV tables and feature-importance notebook updates are integrated through PR #26.
- Training and validation code is available under `src/`; dependencies are in `requirements.txt`.

## Project progress and team coordination

- [Day 1–Day 4 Project Lead Tracker](reports/day1-day4_project_lead_tracker.md)
- [Day 5 Project Lead Tracker](reports/day5_project_lead_tracker.md)
- [Day 6 Project Lead Tracker](reports/day6_project_lead_tracker.md)
- [Day 8 Project Lead Tracker](reports/day8_project_lead_tracker.md)
- [Day 9 Project Lead Tracker](reports/day9_project_lead_tracker.md)
- [Day 10–11 Final Integration Tracker](reports/day10_day11_final_integration_tracker.md)
- [Team Lead Worklog](docs/TEAM_LEAD_WORKLOG.md)

## Evaluation principles

Report bad-risk class precision, recall and F1, ROC-AUC, PR-AUC and balanced accuracy. Use stratified splitting and keep imputation/encoding inside the model pipeline and cross-validation folds to reduce leakage. The dataset is small, so treat results as exploratory and do not rely on accuracy alone.

Do not publish performance values until the scripts have been executed and the generated outputs inspected. Any analysis involving Age and Sex requires careful fairness, legal and governance review.

## Team responsibilities

| Member | Focus |
|---|---|
| Pranav Kumar | Team lead, coordination, repository review and integration |
| Lav Kumar | Data engineering and EDA |
| Divya | Statistical analysis and feature engineering |
| Nivesh | Machine-learning model development |
| Sirisha | Explainability and documentation |
| Raj | BI and dashboard |

## Responsible-use note

This repository is for educational analysis. It must not be used as the basis for actual credit approval or denial.

## Day 8 update — 23 November 2026

- Lav's cleaning pipeline quality checks are integrated through PR #21.
- Raj's Tableau dashboard and insight summary are integrated through PR #19.
- Sirisha's curated feature dictionary and SHAP methodology documentation are integrated through PR #18; actual SHAP/fairness outputs remain pending.
- Nivesh's executed hold-out and stratified 5-fold model results, supporting CSVs and generated report are integrated through PR #22.
- See [Day 8 Project Lead Tracker](reports/day8_project_lead_tracker.md) and [Nivesh's executed ML results](reports/nivesh/day5_ml_execution_results.md).

## Day 9 update — 24 November 2026

- Fast-forwarded the team-lead branch to the current main baseline before preparing Day 9 documentation.
- Lav's data-quality validation report is integrated through PR #25.
- Divya's updated WoE/IV and important-feature notebooks and processed tables are integrated through PR #26.
- The feature summary notebook reports a 0.774 ROC-AUC for its repeated stratified 5-fold feature analysis; this is separate from the Logistic Regression/Random Forest benchmark outputs and should be treated as exploratory pending leakage review.
- Actual SHAP plots/fairness analysis, final Day 9 model-validation sign-off and dashboard review remain open pending evidence.
- See [Day 9 Project Lead Tracker](reports/day9_project_lead_tracker.md).


## Day 10–11 update — 25–26 November 2026

- Lav's Day 10 feature-engineering/data-output validation report is integrated through PR #29. It verifies row counts, target consistency and WoE output completeness, while explicitly noting that model metrics and all WoE/IV calculations were not independently recomputed.
- The reported 0.774 ROC-AUC from the feature-analysis notebook remains preliminary because feature transformations and selection were performed before cross-validation; fold-isolated evaluation is still required.
- Sirisha's PR #28 contains SHAP and Age/Sex subgroup outputs but remains open for revision. Its fairness metrics are computed on the full 1,000-row dataset and are descriptive, and the scripts depend on a Random Forest model artifact not present in main. The PR also includes a duplicate raw dataset and replaces this canonical README, so it is not merged wholesale.
- Final model-validation/leakage sign-off, reproducible SHAP/fairness evidence and dashboard consistency review remain pending. The project is not marked technically complete until those items are verified.
- See [Day 10–11 Final Integration Tracker](reports/day10_day11_final_integration_tracker.md).
