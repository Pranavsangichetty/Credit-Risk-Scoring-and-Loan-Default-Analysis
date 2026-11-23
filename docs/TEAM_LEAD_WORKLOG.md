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
- Added selected ML execution outputs, the generated results report and its report-generation script to the team-lead branch for a focused PR.
- Kept all performance claims tied to generated result files and preserved the historical good/bad target limitation.

## Day 8 integration rule

The team-lead branch is updated first. The shared `main` branch receives only the reviewed Day 8 tracker, coordination documentation and selected reproducible ML outputs through the focused pull request. Actual SHAP/fairness work and final WoE/IV verification remain open until evidence is submitted.


### Day 8 integration completion

- Opened and merged focused PR [#22](https://github.com/Pranavsangichetty/Credit-Risk-Scoring-and-Loan-Default-Analysis/pull/22) into `main` (merge commit `28019a126004bb8becbc253d403d167caf4f0e13`).
- Integrated the Day 8 tracker, updated README/worklog/checklist, Nivesh's generated hold-out and 5-fold metrics, threshold/subgroup CSVs, executed results report and report builder.
- Closed Nivesh's original PR #20 without merging; PR #22 is the curated replacement and preserves the canonical README.
- Re-synchronized `Pranavsangichetty` with the merged main baseline before recording this completion update.
