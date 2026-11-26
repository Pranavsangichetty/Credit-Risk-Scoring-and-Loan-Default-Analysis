# Day10 Reproducibility Repeat Validation

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

# Day 10 — Repeat validation and reproducibility review

## Objective
Repeat the complete model evaluation under a fixed protocol and verify that the outputs are reproducible.

## Reproducibility checks
1. Use the same source dataset and record its Git commit or checksum.
2. Use the fixed random seed configured in the evaluation script.
3. Re-run both models and the stratified five-fold validation.
4. Compare fold metrics, hold-out metrics and threshold-analysis outputs with the previous run.
5. Confirm dependencies are recorded in `requirements.txt`.
6. Confirm generated output files are present, readable and tracked in GitHub.

## Evidence files
- `outputs/stratified_5fold_metrics_by_fold.csv`
- `outputs/final_model_comparison.csv`
- `outputs/development_oof_threshold_analysis.csv`
- `outputs/final_evaluation_metrics.json`

## Result entry
Do not claim identical reproducibility until two runs have been compared. Record any differences and their cause.
