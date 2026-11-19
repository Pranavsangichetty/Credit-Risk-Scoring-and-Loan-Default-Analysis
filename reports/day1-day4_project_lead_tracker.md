# Project Lead Tracker — Day 1 to Day 4

**Project:** Credit Risk Scoring and Loan Default Analysis  
**Project lead:** Pranav Kumar  
**Reporting period:** 16–19 November 2026  
**Dataset:** `german_credit_data.csv` (1,000 rows; 10 data columns plus exported index)

## Purpose and working agreements

This tracker consolidates the four-day work plan, ownership, integration checks and decisions. It is a coordination record, not a claim that every teammate deliverable has already been merged. Branch history at the time this file was added contained the dataset only; each contributor should link their actual notebook, analysis or dashboard when available.

## Day-by-day plan and status

| Day | Date | Focus | Ownership / expected output | Lead review |
|---|---|---|---|---|
| Day 1 | 16 Nov 2026 | Repository setup and dataset understanding | Pranav: repository and task coordination. Lav: inspect dataset/schema. Divya: identify analysis questions. Nivesh: define target and baseline ML plan. Sirisha: documentation outline. Raj: dashboard scope. | Confirm common dataset version, target definition and task ownership. |
| Day 2 | 17 Nov 2026 | Data quality, cleaning and EDA | Lav: missing-value and duplicate checks, cleaned-data proposal. Divya: descriptive statistics and risk-group comparisons. Nivesh: preprocessing plan. Sirisha: record assumptions and caveats. Raj: EDA dashboard layout. | Ensure missing categories are not silently treated as numeric zero; record reproducible cleaning decisions. |
| Day 3 | 18 Nov 2026 | Feature engineering and preparation | Divya: feature engineering and WoE/IV exploration. Nivesh: encoding and model-ready preprocessing. Lav: finalize data-quality notes. Sirisha: feature definitions and explainability notes. Raj: feature-level dashboard insights. | Review leakage risk, target encoding and feature definitions before model fitting. |
| Day 4 | 19 Nov 2026 | Baseline modelling and integration readiness | Nivesh: reproducible baseline pipeline and validation metrics. Pranav: review branch contents, naming, reproducibility and hand-off. Sirisha: document interpretation limits. Raj: align dashboard labels with agreed target. | Baseline implementation added on Nivesh243 branch. No model metrics are asserted in this tracker; run the script to generate them. |

## Team ownership

| Contributor | Responsibility | Expected evidence |
|---|---|---|
| Pranav Kumar | Team lead, coordination, GitHub branch review and integration | This tracker, decisions, review checklist |
| Lav Kumar (`lav-kumar`) | Data engineering and EDA | Cleaning notebook/script, data-quality report |
| Divya (`Divya-Akbari`) | Statistical analysis and feature engineering | EDA/statistics, WoE and IV analysis with binning notes |
| Nivesh (`Nivesh243`) | ML and model development | Preprocessing pipeline, baseline model, evaluation outputs |
| Sirisha (`Sirisha`) | Explainability and documentation | Feature descriptions, limitations and interpretation notes |
| Raj (`Rishu`) | BI and dashboard | Dashboard source/export and metric definitions |

## Dataset facts verified from the committed CSV

- 1,000 observations and 10 analytical columns: Age, Sex, Job, Housing, Saving accounts, Checking account, Credit amount, Duration, Purpose and Risk.
- Target counts: 700 `good` and 300 `bad` (70% / 30%).
- Missing-value marker `NA`: 183 in Saving accounts and 394 in Checking account.
- The first CSV column is an exported row index and should be dropped from model features.
- Target convention for modelling: `good = 0`, `bad = 1`.

## Project decisions and quality gates

1. **Target wording:** The supplied label is historical `good` / `bad` credit risk. Describe the task as classifying the dataset's risk label. Do not claim that the model directly predicts a future loan default unless a verified default outcome and prediction horizon are supplied.
2. **Missing data:** Preserve the distinction between unknown/missing and a genuine low savings/checking category. Impute categorical missing values as an explicit `Unknown` category in the baseline pipeline; document alternatives if later tested.
3. **Validation:** Use stratified splitting and report bad-class precision, recall and F1 alongside ROC-AUC, PR-AUC and balanced accuracy. Accuracy alone is insufficient.
4. **Leakage:** Fit all imputers, encoders and scalers inside a training pipeline. Never fit preprocessing on the full dataset before the split.
5. **Reproducibility:** Record random seeds, package versions, data source and exact run command. Keep generated metrics separate from hand-written narrative.
6. **Fairness:** Age and Sex are present in the source data. Discuss potential fairness and legal considerations before any real lending use. This academic baseline is not suitable for automated credit decisions.
7. **Small sample:** With only 1,000 rows, treat results as exploratory. Use stratified cross-validation for model selection and avoid overstating generalisation.

## Day 4 integration checklist

- [x] Confirm repository access and identify default branch.
- [x] Confirm both contributor branches exist.
- [x] Inspect current branch trees and verify the source CSV.
- [x] Record dataset schema, target distribution and missing-value counts.
- [x] Add the Day 1–Day 4 coordination tracker to this branch.
- [ ] Collect and review Lav's cleaning/EDA deliverables.
- [ ] Collect and review Divya's WoE/IV and feature-engineering outputs.
- [ ] Review Nivesh's generated model metrics after the script is run.
- [ ] Collect Sirisha's explainability notes and Raj's dashboard artifact.
- [ ] Resolve review comments and open a pull request to main only after team approval.

## Suggested Day 5 priorities

1. Merge or link each contributor's verified deliverable into the shared project structure.
2. Compare logistic regression and tree-based baselines using the same stratified split and metrics.
3. Review threshold choice against the cost of missing a bad-risk case.
4. Add a model interpretation and fairness discussion.
5. Prepare a concise results summary with actual, reproducible outputs.

---
**Integrity note:** This file records the agreed workstream and checks completed during repository review. It does not represent unverified teammate work as finished.
