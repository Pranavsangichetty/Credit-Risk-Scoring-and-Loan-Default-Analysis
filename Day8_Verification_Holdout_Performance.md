# Day8 Verification Holdout Performance

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

# Day 8 — Verify cross-validation and hold-out performance

## Objective
Verify the two models' stratified cross-validation results and evaluate final fitted pipelines on an untouched hold-out set.

## Verification steps
1. Confirm both models have five fold-level metric records.
2. Confirm the hold-out set was created with stratification and was not used during model fitting or threshold selection.
3. Fit each complete pipeline on the development partition.
4. Evaluate hold-out probabilities at the default 0.50 threshold and the development-selected threshold.
5. Review confusion matrices, ROC-AUC, PR-AUC, precision, recall, F1 and balanced accuracy.

## Evidence files
- `outputs/final_evaluation_metrics.json`
- `outputs/final_model_comparison.csv`
- `outputs/holdout_predictions.csv`
- `reports/Nivesh_Days6-11_Final_Model_Evaluation.md`

## Result entry
Hold-out values must be populated from the generated report after the real-data run.
