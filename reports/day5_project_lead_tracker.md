# Day 5 — Validation, Explainability and Integration

**Project lead:** Pranav Kumar  
**Date:** 20 November 2026  
**Project:** Credit Risk Scoring and Loan Default Analysis

## Day 5 objective

Move from baseline implementation to evidence-based review. Generate reproducible validation results, explain the model behaviour and prepare the project for integration. Do not report metrics until the scripts have actually been executed and checked.

## Team task allocation

| Member | Day 5 responsibility | Expected deliverable |
|---|---|---|
| Pranav Kumar | Coordinate the team, review both branches, check that outputs are reproducible and prepare the integration checklist. | Updated project tracker, reviewed branch links and integration notes. |
| Lav Kumar | Finalize the cleaning workflow, verify missing-value treatment, duplicates and data types, and document any changes to the source data. | Reproducible cleaning script/notebook and data-quality report. |
| Divya | Complete WoE/IV analysis, explain binning choices and compare statistical findings with the baseline model. Keep feature selection inside training folds if used for modelling. | WoE/IV table and feature-engineering findings. |
| Nivesh | Run the baseline script, execute 5-fold stratified validation, compare Logistic Regression and Random Forest, and review threshold and subgroup metrics. | Actual metrics, validation output and updated ML report. |
| Sirisha | Explain the model results and limitations, document important features using verified evidence, and discuss fairness concerns around Age and Sex. | Explainability and responsible-use report. |
| Raj | Update the dashboard with verified model comparison metrics, risk-label distribution and key feature insights. Clearly label results as exploratory. | Updated dashboard and screenshots/export. |

## Project review checklist

- [ ] Run `python src/train_baseline.py --data german_credit_data.csv` on the `Nivesh243` branch.
- [ ] Run `python src/validate_baseline.py --data german_credit_data.csv` and inspect the generated cross-validation metrics.
- [ ] Compare models using bad-class precision, recall and F1, ROC-AUC, PR-AUC and balanced accuracy.
- [ ] Discuss threshold trade-offs; do not choose a threshold solely to maximise a metric without explaining error costs.
- [ ] Review subgroup results carefully and flag small sample sizes.
- [ ] Verify Lav's cleaning decisions and Divya's WoE/IV calculations.
- [ ] Check Sirisha's interpretation and Raj's dashboard against actual generated results.
- [ ] Link or merge reviewed work only after checking each contributor's branch and obtaining team approval.

## Important modelling guardrails

- The target is the dataset's historical `good` / `bad` risk label, not a directly observed future default outcome with a defined prediction horizon.
- Keep imputation and encoding inside the model pipeline to avoid leakage.
- The dataset has only 1,000 rows; treat validation as exploratory and report uncertainty.
- Do not use this educational project for real lending decisions. Age and Sex require careful fairness, legal and governance review.

## Day 5 status

The `Nivesh243` branch contains the Day 4 baseline training script and its run instructions. The Day 5 validation script is added separately; generated validation metrics remain pending until it is run against the repository dataset. No model performance values are asserted here.

---
**Team lead note:** Keep commits on the assigned branches. Do not push unreviewed work directly to `main`.
