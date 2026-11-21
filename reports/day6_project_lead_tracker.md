# Day 6 — Project Review, Branch Integration and Quality Check

**Project lead:** Pranav Kumar  
**Date:** 21 November 2026  
**Project:** Credit Risk Scoring and Loan Default Analysis

## Day 6 objective

Review contributor branches, document project status, integrate verified work through pull requests and keep `main` as the shared stable branch.

## Project lead work completed

- Audited the repository branches and compared contributor branches with `main`.
- Consolidated Nivesh's two extra patch branches into the canonical `Nivesh243` branch.
- Reviewed Divya's latest statistical-analysis and feature-engineering notebooks.
- Reviewed Nivesh's baseline training and 5-fold validation scripts, requirements and ML documentation.
- Prepared the Day 6 tracker and updated the project README.
- Created and merged pull requests for the project-lead update and the verified Divya and Nivesh branch contributions.
- Verified the final `main` tree contains the Day 6 tracker, Divya's six notebooks, her two PDF summaries, and Nivesh's training and validation scripts and reports.

## Team progress and integration status

| Member | Latest repository evidence | Status |
|---|---|---|
| Pranav Kumar | Day 6 tracker and README update merged through PR #8. | Day 6 coordination, branch audit and integration completed. |
| Lav Kumar | `lav-kumar` has no commits ahead of `main`; only the shared dataset is visible. | Cleaning script, cleaned dataset and data-quality report remain pending. |
| Divya | Six notebooks and two PDF summaries merged through PR #9. The WoE/IV notebook has 18 executed code cells; the important-features notebook has 12 executed code cells. | Uploaded analysis integrated. Review calculations and interpretations before treating findings as final. |
| Nivesh | ML documentation and current branch updates merged through PR #10. Training and 5-fold validation scripts are present in `main`. | Code and documentation integrated. Actual numerical evaluation results remain pending; no generated metrics were verified in the branch. |
| Sirisha | `Sirisha` has no commits ahead of `main`; no distinct explainability/fairness deliverable is visible. | Explainability, feature interpretation and fairness report remain pending. |
| Raj | No `Rishu` branch is present in the current branch list. | Confirm the correct branch name and share dashboard work or its repository link. |

## Pull requests merged on Day 6

| PR | Description | Result |
|---|---|---|
| [#8](https://github.com/Pranavsangichetty/Credit-Risk-Scoring-and-Loan-Default-Analysis/pull/8) | Day 6 project lead tracker and README update | Merged |
| [#10](https://github.com/Pranavsangichetty/Credit-Risk-Scoring-and-Loan-Default-Analysis/pull/10) | Nivesh's ML documentation and validation updates | Merged |
| [#9](https://github.com/Pranavsangichetty/Credit-Risk-Scoring-and-Loan-Default-Analysis/pull/9) | Divya's statistical analysis and feature engineering notebooks | Merged |

## Remaining integration checklist

- [ ] Lav: push the cleaning script, cleaned dataset and data-quality report.
- [ ] Nivesh: run the training and validation scripts, inspect generated outputs and commit actual metrics.
- [ ] Sirisha: push the explainability, feature-interpretation and fairness report.
- [ ] Raj: confirm branch name and push the dashboard deliverable.
- [ ] Review all remaining contributions before merging them into `main`.

## ML validation guardrails

- The supplied `Risk` target is a historical good/bad credit-risk label, not a directly observed future default outcome with a defined prediction horizon.
- Do not publish model metrics until the training and validation scripts have actually been run and the generated output files have been inspected.
- Compare bad-class precision, recall and F1, ROC-AUC, PR-AUC and balanced accuracy; do not rely on accuracy alone.
- Keep imputation and encoding inside the cross-validation pipeline to avoid leakage.
- Treat subgroup analysis by Age and Sex as a cautious diagnostic, not proof of fairness.
- This educational project must not be used to make real lending decisions.

## Day 6 outcome

The Day 6 project-lead update, Divya's uploaded statistical-analysis and feature-engineering deliverables, and Nivesh's current ML code and documentation are integrated into `main`. Lav's cleaning deliverables, Sirisha's explainability/fairness report and Raj's dashboard contribution still require updates. Nivesh's actual model metrics also remain pending execution and verification.

---
**Team lead note:** Keep contributor work on assigned branches and integrate through pull requests. Do not overwrite `main` directly or report unverified model results.


## Repository structure decision — Day 6

After comparing the current repository with the team's previous Axlero Group 3 repository, the project will use a consolidated, deliverable-first structure:

- `main` is the canonical shared project branch and should contain the reviewed project deliverables.
- Organize notebooks, scripts and reports by their purpose, not by contributor name.
- Contributor branches remain useful as temporary work/review branches, but they do not need to be merged wholesale.
- Integrate only final, reviewed and non-duplicate deliverables through pull requests.
- Keep one canonical copy of each report or notebook. The duplicate copies under `reports/nivesh/` were removed because the same five reports already exist at the project root.
- Continue daily updates in the project tracker and keep the README aligned with the actual repository structure.

This keeps `main` clean and usable as the complete project workspace without losing the individual branch history.
