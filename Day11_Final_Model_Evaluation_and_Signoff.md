# Day11 Final Model Evaluation and Signoff

**Project:** Credit Risk Scoring and Loan Default Analysis  
**Assigned owner:** Nivesh — ML / Model Development  
**Dataset:** `german_credit_data.csv`  
**Models:** Logistic Regression and Random Forest  
**Target:** `Risk` (`bad` = positive class 1; `good` = class 0)

> **Results integrity:** This is a day-specific submission record and execution specification. Do not fill in guessed scores. Actual metrics must be copied from the generated output files after running the workflow against the repository's original dataset.

## Reproduce
From the repository root, install dependencies and run:

```bash
python -m pip install -r requirements.txt
python src/run_final_evaluation.py --data german_credit_data.csv
```

The script writes the numerical evidence under `outputs/` and the consolidated report under `reports/`.

# Day 11 — Final model evaluation and submission sign-off

## Objective
Consolidate all cross-validation and hold-out metrics, finalize the threshold recommendation and submit a reproducible model-evaluation package.

## Final checklist
- [ ] Logistic Regression and Random Forest both execute successfully.
- [ ] Stratified five-fold metrics are present for both models (five folds each).
- [ ] Mean and standard deviation are reported for the cross-validation metrics.
- [ ] Hold-out metrics are reported separately from cross-validation metrics.
- [ ] Threshold recommendation is based only on development out-of-fold predictions.
- [ ] Hold-out performance is reported at 0.50 and the selected threshold.
- [ ] Confusion matrices and ROC/precision-recall curves are reviewed.
- [ ] Preprocessing leakage checks are documented.
- [ ] Dataset version, random seed and dependency versions are recorded.
- [ ] Final report and generated evidence are committed to the assigned GitHub branch.

## Required final comparison
Compare ROC-AUC, PR-AUC, bad-class precision, bad-class recall, bad-class F1, balanced accuracy and threshold behaviour. Explain the operational trade-off between missed bad-risk cases and false alarms.

## Evidence files
- `outputs/final_model_comparison.csv`
- `outputs/final_evaluation_metrics.json`
- `outputs/development_oof_threshold_analysis.csv`
- `outputs/holdout_predictions.csv`
- `reports/Nivesh_Days6-11_Final_Model_Evaluation.md`

## Final status
The submission package is prepared. Mark this task complete only after the actual dataset run succeeds, all evidence files are checked and the results are committed to GitHub.
