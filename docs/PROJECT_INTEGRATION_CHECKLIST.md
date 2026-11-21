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
