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

- [ ] Lav: reproducible cleaning script, cleaned-data description and data-quality report.
- [ ] Divya: verify statistical analysis and WoE/IV calculations; retain only canonical analysis deliverables.
- [ ] Nivesh: execute training and validation, inspect outputs and publish actual metrics.
- [ ] Sirisha: explainability, feature interpretation and fairness report.
- [ ] Raj: confirm branch name and submit the agreed dashboard deliverable.
- [ ] Pranav: review diffs, coordinate interfaces, maintain README/worklog and manage PR integration.

## Model-quality guardrails

The dataset contains 1,000 records and a historical `good` / `bad` label. Report bad-class precision, recall and F1, ROC-AUC, PR-AUC and balanced accuracy; do not rely on accuracy alone. Do not describe the target as a future default outcome with a defined horizon. Do not use this educational project for actual lending decisions.

## Daily review record

| Date | Branch / PR | Files accepted | Files left out and reason | Decision |
|---|---|---|---|---|
| 2026-11-21 | PR #9 and PR #10 | Divya's analysis notebooks/PDF summaries; Nivesh's ML scripts and supporting documentation | Keep future drafts, duplicate copies and unverified metrics out | Merged; continue validation |


## Day 8 review — 23 November 2026

| Member / area | Latest evidence | Current integration status |
|---|---|---|
| Lav — data engineering | PR #21 merged; cleaning pipeline quality checks, cleaned dataset and handoff are in main. | Integrated; retain binning recommendations as proposals until validated. |
| Divya — WoE/IV | PR #16 merged with the Day 6 findings summary and earlier analysis notebooks. | Integrated; final feature-level calculation/interpretation review should be recorded. |
| Nivesh — ML | Successful Actions run #45045131089; actual hold-out and stratified 5-fold outputs generated on Nivesh243. | Curated results are proposed for main; do not merge PR #20 wholesale because its README replacement is not suitable for the shared branch. |
| Sirisha — explainability | PR #18 merged with feature dictionary/fairness notes and SHAP methodology. | Documentation integrated; actual SHAP plots/values and completed fairness analysis remain pending. |
| Raj — dashboard | PR #19 merged with Tableau dashboard and insight summary. | Integrated. |
| Pranav — project integration | Day 8 audit and tracker prepared on the synchronized team-lead branch. | Submit focused PR; verify main after merge. |

### Day 8 selective integration record

- Accept only the executed metrics, hold-out predictions, threshold/subgroup summaries, generated ML results report and the report-generation script from Nivesh's branch.
- Preserve main's canonical README; exclude the contributor README replacement.
- Keep the contributor-specific Actions workflow and redundant validation script on Nivesh's branch.
- Add `tabulate` to the existing requirements rather than replacing existing dependencies.
- Do not mark SHAP/fairness or final WoE/IV review complete without evidence.
