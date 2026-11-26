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
- [ ] Nivesh: final Day 9 reproducibility, threshold recommendation, preprocessing-leakage review and model-validation sign-off.
- [ ] Sirisha: actual model-specific SHAP outputs, plots, feature interpretations and completed fairness report.
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
- [ ] Nivesh: provide final reproducible LR/RF validation, threshold recommendation and preprocessing-leakage review.
- [ ] Sirisha: revise PR #28 to make SHAP reproducible from the canonical training pipeline and rerun Age/Sex diagnostics on an independent holdout; current full-dataset subgroup results are descriptive only.
- [ ] Raj: provide final dashboard consistency review against the canonical model outputs.
- [x] Pranav: audit live branches/PRs, fast-forward team-lead branch, prepare Day 10–11 tracker and update README/worklog/checklist.

### Day 10–11 integration record

| Date | Branch / PR | Files accepted | Files left out and reason | Decision |
|---|---|---|---|---|
| 2026-11-26 | PR #29 | Lav's Day 10 feature-engineering/data-output validation report | Report does not independently recompute all WoE/IV values or model metrics | Merged; use within its stated scope |
| 2026-11-26 | PR #28 | None yet | Open PR replaces canonical README, adds duplicate raw data, scripts depend on absent model artifact, and fairness results use full-data predictions | Request focused revision; do not merge wholesale |
| 2026-11-26 | Team-lead Day 10–11 review | Final integration tracker, README progress update, worklog and checklist review | No unverified model metrics or incomplete contributor artifacts added | Prepared for focused PR |

**Release gate:** Do not describe the project as technically complete until the outstanding model validation, explainability/fairness and dashboard checks are supported by reproducible evidence.
