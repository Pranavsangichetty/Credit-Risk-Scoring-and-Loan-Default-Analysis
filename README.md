# Credit Risk Scoring and Loan Default Analysis

An exploratory machine-learning project using the German Credit dataset to study the supplied historical credit-risk label (`good` / `bad`).

> **Important:** The dataset target is a historical risk category, not a directly observed future default event with a defined prediction horizon. This project should not be described as a validated future-default prediction system or used to make real lending decisions.

## Project structure

The `main` branch is the single consolidated project workspace. It contains reviewed, reusable deliverables organized by project purpose rather than by individual contributor.

- Root-level numbered notebooks: statistical analysis, feature relationships and feature engineering.
- `src/`: reusable preprocessing, training and validation code.
- `reports/`: project reports, validation plans, team-lead trackers and supporting evidence.
- `german_credit_data.csv`: source dataset.
- `requirements.txt`: Python dependencies.

Do not create member-specific copies of the same notebooks or reports (for example, `reports/<member>/`). Keep one canonical copy in the appropriate project location.

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
| Pranav Kumar | Team lead, coordination, quality review and integration |
| Lav Kumar | Data engineering and EDA |
| Divya | Statistical analysis and feature engineering |
| Nivesh | ML and model development |
| Sirisha | Explainability and documentation |
| Raj | BI and dashboard |

## GitHub workflow

- `main` is the canonical, consolidated branch used for the shared project and daily progress.
- Contributors may use their assigned branches while developing or testing work.
- Only reviewed, non-duplicate and project-ready deliverables should be integrated into `main`.
- Prefer a small pull request containing the final deliverable(s), rather than copying every intermediate file or maintaining member-wise folders.
- Keep the contributor branches as working/history branches; they do not need to be merged wholesale or deleted after each update.
- Do not push unreviewed or untested changes directly to `main`.
- After integration, update the relevant report/tracker and this README when the project structure or workflow changes.

## Project progress

- [Day 1–Day 4 Project Lead Tracker](reports/day1-day4_project_lead_tracker.md)
- [Day 5 Project Lead Tracker](reports/day5_project_lead_tracker.md)
- [Day 6 Project Lead Tracker](reports/day6_project_lead_tracker.md)

The shared `main` branch contains the currently integrated analysis notebooks, baseline training and validation scripts, and project documentation. Check the Day 6 tracker for the latest contributor review and outstanding deliverables.

## Model implementation

The baseline model implementation is in `src/train_baseline.py`. The 5-fold validation workflow is in `src/validate_baseline.py`. Run instructions and methodology are documented in `reports/day4_baseline_model.md` and `reports/day5_validation_plan.md`.

## Evaluation principles

Report the bad-risk class precision, recall and F1, ROC-AUC, PR-AUC and balanced accuracy. Use stratified train/test splitting and keep imputation/encoding inside the model pipeline to avoid leakage. Treat all results as exploratory because the dataset is small. Do not publish scores until generated outputs have been verified.

## Responsible-use note

The source includes Age and Sex. Any analysis involving these attributes requires careful fairness, legal and governance review. Do not use this educational project for real credit approval or denial.
