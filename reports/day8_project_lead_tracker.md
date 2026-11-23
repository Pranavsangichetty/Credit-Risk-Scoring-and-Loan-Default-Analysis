# Day 8 — Project Integration and Validation Tracker

**Project:** Credit Risk Scoring and Loan Default Analysis  
**Team lead:** Pranav Kumar  
**Date:** 23 November 2026  
**Schedule note:** Day 7 was observed as a holiday; work resumes on Day 8.

## Day 8 objective

Complete the team-lead review, bring the personal team-lead branch in sync with the shared project, integrate verified ML execution evidence selectively, and record the remaining validation and explainability work.

## Live repository baseline

- Shared branch: `main`
- Main commit at the start of Day 8 review: `3338c33973bf207cdc8d8e19f9ee35cb5afa5e45`
- Team-lead branch: `Pranavsangichetty`
- The team-lead branch was 21 commits behind `main` with no unique commits ahead. It has now been fast-forwarded to the current main baseline before Day 8 updates.
- Keep `main` as the curated shared project. Integrate selected reviewed files through a focused PR, not by merging entire contributor branches.

## Team status and Day 8 review

| Member | Repository evidence reviewed | Day 8 status |
|---|---|---|
| **Pranav Kumar** | Team-lead branch synchronized with main; latest PRs and repository tree reviewed; Day 8 tracker and integration documentation updated. | Team-lead review and documentation prepared on `Pranavsangichetty`; submit through this focused PR. |
| **Lav Kumar** | PR [#21](https://github.com/Pranavsangichetty/Credit-Risk-Scoring-and-Loan-Default-Analysis/pull/21) merged. Cleaning pipeline quality checks are in main alongside `src/clean_data.py`, the cleaned dataset and data-quality handoff. | Day 8 data-engineering handoff integrated. Any future binning remains subject to validation. |
| **Divya** | PR [#16](https://github.com/Pranavsangichetty/Credit-Risk-Scoring-and-Loan-Default-Analysis/pull/16) merged with the Day 6 WoE/IV findings summary; earlier analysis notebooks and summaries are also in main. | Deliverables are integrated. Final feature-level calculation and interpretation review should be recorded before calling all findings fully validated. |
| **Nivesh** | PR [#20](https://github.com/Pranavsangichetty/Credit-Risk-Scoring-and-Loan-Default-Analysis/pull/20) remains open and is not mergeable as submitted. GitHub Actions run [#45045131089](https://github.com/Pranavsangichetty/Credit-Risk-Scoring-and-Loan-Default-Analysis/actions/runs/45045131089) completed successfully. The generated hold-out and 5-fold outputs were inspected on `Nivesh243`. | Model execution and result generation are complete on the contributor branch. Selected outputs and the report builder are being integrated through this curated team-lead change. The wholesale PR is not being merged because it replaces the canonical README and includes redundant material. |
| **Sirisha** | Curated documentation merged through PR [#18](https://github.com/Pranavsangichetty/Credit-Risk-Scoring-and-Loan-Default-Analysis/pull/18): feature dictionary/fairness notes and SHAP methodology. | Documentation is integrated. Actual SHAP values/plots, model-specific feature interpretations and completed fairness analysis remain pending. |
| **Raj / Rishuraj** | PR [#19](https://github.com/Pranavsangichetty/Credit-Risk-Scoring-and-Loan-Default-Analysis/pull/19) merged with `dashboard/credit_risk_dashboard.twbx` and `reports/raj_bi_dashboard_insights.md`. | Tableau dashboard and insight handoff integrated. |

## Nivesh — executed model results reviewed

The successful workflow executed the existing hold-out training script, stratified 5-fold validation script and report builder against the repository's 1,000-row German Credit dataset. The generated files distinguish the 80:20 hold-out evaluation from pooled 5-fold out-of-fold validation.

### Stratified 5-fold out-of-fold results

Positive class: `bad = 1`. Values below are taken from `outputs/cross_validation_metrics.json` and `outputs/model_comparison.csv`.

| Model | ROC-AUC | PR-AUC (average precision) | Bad precision | Bad recall | Bad F1 | Balanced accuracy |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 0.7410 | 0.5462 | 0.4842 | 0.7133 | 0.5768 | 0.6938 |
| Random Forest | 0.7607 | 0.5975 | 0.5116 | 0.6633 | 0.5776 | 0.6960 |

These are exploratory results for the supplied historical `good` / `bad` label. The 80:20 hold-out results are separately preserved in `outputs/metrics.json`; they must not be mixed with the 5-fold figures.

### Selected threshold and subgroup evidence

- Threshold comparisons are available in `outputs/threshold_analysis.csv`.
- Sex and age-band descriptive metrics are available in `outputs/subgroup_metrics.csv`.
- These subgroup results are diagnostics only; they do not establish fairness or legal suitability.
- The generated narrative report is `reports/nivesh/day5_ml_execution_results.md`.

## Day 8 integration decisions

1. Keep the canonical project README from main; do not accept the README replacement in PR #20.
2. Integrate the generated hold-out and 5-fold metric files, model comparison/threshold/subgroup CSVs, executed results report and report-generation script.
3. Add the report builder's `tabulate` dependency to the existing requirements file without removing existing dependencies.
4. Keep Nivesh's contributor-specific GitHub Actions workflow and duplicate validation script on the contributor branch unless a shared automation requirement is agreed.
5. Keep Sirisha's actual SHAP/fairness outputs pending until model-specific evidence is submitted and reviewed.
6. Do not describe this dataset target as a verified future loan-default outcome with a defined observation horizon.

## Day 8 completion checklist

- [x] Audit current main and contributor branch state.
- [x] Fast-forward `Pranavsangichetty` to the current main baseline.
- [x] Verify Lav's PR #21 and Raj's PR #19 are merged.
- [x] Verify Sirisha's curated PR #18 is merged and record remaining analysis.
- [x] Verify Nivesh's successful workflow and inspect actual generated outputs.
- [ ] Merge this curated Day 8 team-lead PR into main after review.
- [ ] Complete Divya's final calculation/interpretation validation.
- [ ] Obtain Sirisha's actual SHAP and fairness outputs.
- [ ] Re-run final repository checks after all accepted contributions are integrated.

## Responsible-use and evaluation guardrails

- The target is a historical `good` / `bad` risk category, not a directly observed future-default event with a defined horizon.
- Report bad-class precision, recall and F1 alongside ROC-AUC, PR-AUC and balanced accuracy; do not rely on accuracy alone.
- Keep preprocessing within the training folds to reduce leakage.
- Treat Age/Sex subgroup comparisons as descriptive diagnostics, not proof of fairness.
- This educational project is not a validated production lending system and must not be used for real credit approval or denial.

---
**Team lead note:** The repository status above reflects the GitHub files, pull requests and workflow run inspected for Day 8. Pending work is explicitly left open rather than being marked complete without evidence.
