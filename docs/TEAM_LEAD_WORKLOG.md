# Team Lead Worklog — Pranav Kumar

**Repository:** Pranavsangichetty/Credit-Risk-Scoring-and-Loan-Default-Analysis  
**Personal working branch:** `Pranavsangichetty`  
**Shared project branch:** `main`

## Role

Coordinate the project plan, assign and track work, review contributor branches, agree on file handoffs, maintain project documentation, and selectively integrate accepted deliverables into `main`.

## Day 6 — 21 November 2026

- Reviewed the repository structure and current branch state.
- Confirmed `main` is the shared project workspace and `Pranavsangichetty` is the team-lead documentation branch.
- Consolidated Nivesh's two extra patch branches into the canonical `Nivesh243` branch before the Day 6 integration.
- Reviewed the merged Divya statistical-analysis/feature-engineering notebooks and Nivesh training/validation code and documentation.
- Recorded merged PRs #8, #9, #10 and #11 in the Day 6 tracker.
- Documented a selective integration policy based on the workflow used in Axlero-Group3.
- Added architecture and integration guidance so that future contributions are reviewed file by file rather than copied wholesale.

## Daily operating routine

### Start of day
- Confirm today's objective and deliverables.
- Check branch names, current heads and blockers.
- Confirm data schemas and shared file ownership before parallel changes.

### During the day
- Review actual diffs and execution evidence.
- Keep one canonical version of each dataset, script, notebook and report.
- Coordinate changes that affect downstream modules.
- Record unresolved assumptions and dependencies.

### End of day
- Update the daily tracker with completed work and pending items.
- Create a focused PR from the team-lead branch for documentation changes.
- Review member PRs selectively; do not merge a whole branch without inspecting its contents.
- Verify the final `main` tree and record exact PR/commit links.
- Never claim execution, metrics or completion without evidence.

## Integration principle

A contributor branch is a development and attribution space. The shared `main` branch is a curated project deliverable. Only the files needed for the integrated project should be merged. Keep useful but non-final work on its source branch until it is ready.

## Important modelling caveat

The German Credit dataset target is a historical good/bad risk label, not a directly observed future default event with a defined prediction horizon. Model findings are exploratory and must not be used for real lending decisions.

## Day 8 — 23 November 2026

- Treated Day 7 as a holiday and resumed project work on Day 8.
- Audited the live repository branches, pull requests and main tree. The `Pranavsangichetty` branch was 21 commits behind `main` and had no unique commits ahead; fast-forwarded it to the current main baseline before adding Day 8 work.
- Verified Lav's cleaning pipeline quality-check PR #21 and Raj's Tableau dashboard PR #19 are merged.
- Verified Sirisha's curated documentation PR #18 is merged; recorded that actual SHAP outputs and completed fairness analysis are still pending.
- Reviewed Nivesh's PR #20 and successful GitHub Actions run #45045131089. Inspected the generated 80:20 hold-out metrics, stratified 5-fold out-of-fold metrics, threshold analysis, subgroup metrics and generated report.
- Chose a curated integration rather than merging PR #20 wholesale because it replaces the canonical README and includes redundant contributor-specific material.
- Integrated selected ML execution outputs and documentation through PR #22.
- PR #23 recorded Day 8 integration completion; PR #24 corrected the tracker to show that Nivesh's original PR #20 was closed unmerged.

## Day 8 integration rule

The team-lead branch is updated first. The shared `main` branch receives only reviewed trackers, coordination documentation and selected reproducible ML outputs through focused pull requests. Actual SHAP/fairness outputs and final feature-analysis verification remain open until evidence is submitted.

## Day 9 — 24 November 2026

- Audited the live branches, merged PR list and main tree. Main was at `91255f004403e4b6928b024684fd5fe4908c5f4f`; the team-lead branch was at `6359489a5962d918ba659ee57933b784f84ca49c`.
- Compared the branches and confirmed the team-lead branch was four commits behind main with no unique commits ahead. Fast-forwarded `Pranavsangichetty` to main without force.
- Verified PR #25 merged Lav's data-quality validation report.
- Verified PR #26 merged updated WoE/IV and important-feature notebooks plus processed WoE/IV datasets.
- Inspected executed outputs in `06_Important_Features_Summary.ipynb`: the notebook reports 0.774 ROC-AUC for its repeated stratified 5-fold feature analysis, a largest drop-one AUC loss of 0.0603 for checking account status, and nine passing internal validation checks.
- Recorded that the 0.774 feature-analysis result is distinct from the Logistic Regression/Random Forest benchmark outputs. Feature-selection timing and fold isolation require review before treating it as an unbiased generalization estimate.
- Prepared `reports/day9_project_lead_tracker.md` and updated README and integration checklist on the personal branch for a focused PR.
- Left actual SHAP/fairness outputs, new Day 9 model-validation evidence and dashboard review open because no corresponding Day 9 deliverables were found in the merged PR list reviewed.

## Day 9 integration rule

The personal branch contains team-lead coordination and review documentation. Main should receive the Day 9 tracker and the necessary README/checklist coordination updates through a focused PR. Do not claim SHAP, fairness, final model validation or dashboard review complete without actual evidence.
