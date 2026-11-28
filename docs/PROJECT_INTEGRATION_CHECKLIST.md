# Project Integration Checklist

**Project:** Credit Risk Scoring and Loan Default Analysis  
**Team lead:** Pranav Kumar  
**Shared baseline:** `main`

## Integration policy

The `main` branch is the consolidated, reviewable project workspace. It should contain only canonical project deliverables that are relevant, non-duplicative and sufficiently reviewed for shared use.

Do not merge every file from every member branch by default. A branch may contain drafts, temporary experiments, duplicate reports, personal worklogs or unverified outputs. Keep those in the contributor branch unless they are needed in the shared project.

## Review before integration

- [ ] Confirm the branch is the member's assigned branch and is current with `main`.
- [ ] Inspect the complete file diff, not just the commit message.
- [ ] Check whether the same file or analysis already exists in `main`.
- [ ] Confirm filenames, paths, dependencies and dataset assumptions.
- [ ] Check that code is relevant to the agreed project scope.
- [ ] Verify notebook outputs or script execution where practical.
- [ ] Confirm metrics are actual generated results, not estimates or placeholders.
- [ ] Check that no credentials, private information, unnecessary raw data or large temporary files are included.
- [ ] Open a focused pull request containing only the approved deliverables.
- [ ] Review and merge only after resolving conflicts and recording limitations.

## What belongs in main

| Contribution | Shared integration rule |
|---|---|
| Data cleaning | Integrate the canonical reproducible cleaning workflow and data-quality evidence. Avoid multiple competing cleaned datasets. |
| EDA and statistics | Integrate the final useful notebooks/reports; omit duplicate drafts and temporary exports. |
| Feature engineering | Integrate the selected feature pipeline and its explanation after reviewing calculations. |
| Model development | Integrate reusable training/validation code, dependencies and concise run instructions. |
| Model results | Integrate only verified metrics and outputs with run details. |
| Explainability/fairness | Integrate evidence-based interpretation and limitations. |
| Dashboard | Integrate the agreed final dashboard artifact and documented data source. |
| Daily personal notes | Keep team-lead worklogs in the team-lead branch or the designated tracker; do not copy every personal note into main. |

## Branch responsibilities

- `main`: stable, consolidated project deliverables.
- `Pranavsangichetty`: team-lead coordination, daily worklogs, integration decisions and documentation changes proposed through PRs.
- `lav-kumar`, `Divya-Akbari`, `Nivesh243`, `Sirisha`, and Raj's confirmed branch: member development and evidence before review.

Contributor branches remain useful for attribution and development history. They are not required to be deleted after their accepted files are integrated.

## Current release checks

- [x] Lav: cleaning workflow, cleaned-data checks and Day 8 data-quality validation report (PR #25); obtain separate Day 9 sign-off if further model-input audit was performed.
- [x] Divya: updated WoE/IV tables and feature-importance notebook integrated (PR #26); independently review fold isolation and feature-selection timing.
- [x] Nivesh: leakage-aware Days 6–11 final evaluation, development-only model/threshold selection and generated holdout evidence integrated through curated PR #37. [ ] Manual semantic/post-outcome feature review remains pending.
- [x] Sirisha: global SHAP plots/feature-importance outputs and full-dataset Age/Sex subgroup diagnostics plus documentation integrated through curated PR #28. [ ] Reproducible SHAP pipeline and independent-holdout fairness assessment still pending.
- [ ] Raj: Day 9 dashboard consistency review against current model outputs and updated evidence if changes are required.
- [x] Pranav: audit main and team-lead branch, fast-forward personal branch and prepare Day 9 tracker/documentation PR.

## Model-quality guardrails

The dataset contains 1,000 records and a historical `good` / `bad` label. Report bad-class precision, recall and F1, ROC-AUC, PR-AUC and balanced accuracy; do not rely on accuracy alone. Do not describe the target as a future default outcome with a defined horizon. Do not use this educational project for actual lending decisions.

## Daily review record

| Date | Branch / PR | Files accepted | Files left out and reason | Decision |
|---|---|---|---|---|
| 2026-11-21 | PR #9 and PR #10 | Divya's analysis notebooks/PDF summaries; Nivesh's ML scripts and supporting documentation | Keep future drafts, duplicate copies and unverified metrics out | Merged; continue validation |
| 2026-11-23 | PR #22 | Day 8 tracker, team-lead documentation, selected executed ML outputs/report builder | Excluded Nivesh's README replacement, contributor-only Actions workflow and duplicate validation script | Merged |
| 2026-11-24 | PR #25 | Lav's Day 8 data-quality validation report | No additional Day 9 sign-off evidenced in reviewed PR list | Merged |
| 2026-11-24 | PR #26 | Updated WoE/IV and feature-importance notebooks; engineered and WoE datasets; IV tables | No SHAP plots/fairness report or Day 9 model-validation rerun in this PR | Merged |
| 2026-11-24 | Team-lead Day 9 PR (to be opened) | Day 9 tracker, README progress link and coordination checklist/worklog updates | Keep personal worklog on team-lead branch; no unverified analysis artifacts | Prepared for review |


## Day 10–11 final review — 26 November 2026

- [x] Lav: Day 10 data/feature-output validation report merged through PR #29; report's stated scope and limitations recorded.
- [ ] Divya: review additional branch notebooks and complete fold-isolated WoE/IV and feature-selection validation.
- [x] Nivesh: corrected final evaluation script, 5-fold development metrics, OOF threshold analysis, separate holdout results and run metadata integrated through PR #37. [ ] Manual semantic feature review remains pending.
- [x] Sirisha: curated SHAP outputs, feature documentation and full-dataset subgroup diagnostics merged through PR #28. [ ] Reproducible SHAP generation and independent-holdout Age/Sex fairness assessment remain pending.
- [ ] Raj: provide final dashboard consistency review against the canonical model outputs.
- [x] Pranav: audit live branches/PRs, fast-forward team-lead branch, prepare Day 10–11 tracker and update README/worklog/checklist.

### Day 10–11 integration record

| Date | Branch / PR | Files accepted | Files left out and reason | Decision |
|---|---|---|---|---|
| 2026-11-26 | PR #29 | Lav's Day 10 feature-engineering/data-output validation report | Report does not independently recompute all WoE/IV values or model metrics | Merged; use within its stated scope |
| 2026-11-26 | PR #28 | Explainability documentation, Day 1/2 feature docs, SHAP plots/CSV, Age/Sex descriptive subgroup CSVs and Day 4 report; README conflict resolved using canonical main content | Excluded duplicate raw dataset, scripts requiring absent `outputs/random_forest.joblib`, and duplicate Day 3 feature summary | Merged after curation; fairness figures remain full-dataset descriptive diagnostics |
| 2026-11-26 | Team-lead Day 10–11 review | Final integration tracker, README progress update, worklog and checklist review | No unverified model metrics or incomplete contributor artifacts added | Prepared for focused PR |

**Release gate:** Do not describe the project as technically complete until the outstanding model validation, explainability/fairness and dashboard checks are supported by reproducible evidence.


## Day 12–13 review — 27–28 November 2026

- [x] Pranav: verify `Pranavsangichetty` and `main` are synchronized before starting this review; prepare Day 12–13 tracker and coordination record.
- [ ] Lav: submit fresh Day 12–13 data/feature handoff verification; prior Day 10 report remains within its stated scope.
- [ ] Divya: provide fold-isolated WoE/IV and feature-selection validation.
- [ ] Nivesh: correct and execute the final-evaluation workflow, then submit reproducible CV and separate holdout evidence. PR #32 remains under review; do not treat its existing metrics as a new Day 10/11 run.
- [ ] Sirisha: provide reproducible SHAP generation and independent-holdout fairness assessment.
- [ ] Raj: provide final dashboard consistency sign-off against approved canonical outputs.

### Day 12–13 PR review record

| Date | Branch / PR | Review finding | Decision |
|---|---|---|---|
| 2026-11-28 | PR #32 / PR #37 — Nivesh243 | Original branch was substantially diverged; accepted final script, dependencies, Day 10/11 docs, generated metrics and holdout diagnostics were curated onto a clean main-based branch. Canonical README and original baseline holdout predictions preserved. | PR #37 merged; original PR #32 closed as superseded |

**Release gate:** Nivesh's leakage-aware final evaluation pipeline and generated holdout evidence are integrated. Semantic feature review, reproducible SHAP, comprehensive independent fairness review and dashboard consistency sign-off remain outstanding.
