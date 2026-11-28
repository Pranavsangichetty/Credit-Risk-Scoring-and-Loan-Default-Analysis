# Day 10 — Reproducibility and Repeat Validation

**Owner:** Nivesh — ML / Model Development  
**Execution source:** `src/run_final_evaluation.py`  
**Dataset:** canonical root `german_credit_data.csv`

## Reproducibility protocol

- Dataset SHA-256 is recorded in `outputs/final_evaluation_metrics.json`.
- Python, pandas, NumPy, scikit-learn and joblib versions are recorded.
- Random seed is fixed at 42.
- A stratified 80/20 split is made before development validation.
- Stratified 5-fold cross-validation and out-of-fold threshold selection run only on the 80% development partition.
- Imputation, scaling and one-hot encoding are fitted inside each pipeline and refitted in each training fold.
- The untouched 20% holdout is used only for final reporting.
- The workflow checks generated evidence and uploads the full run artifacts.

## Evidence

- `outputs/final_evaluation_metrics.json`
- `outputs/stratified_5fold_metrics_by_fold.csv`
- `outputs/development_oof_threshold_analysis.csv`
- `outputs/final_model_comparison.csv`

The workflow run and its artifact provide the execution evidence. Do not claim repeat-run equivalence unless two independent executions have been compared.
