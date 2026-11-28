# Day 11 — Final Model Evaluation and Sign-off

**Owner:** Nivesh — ML / Model Development  
**Execution source:** `src/run_final_evaluation.py`

## Final evaluation design

1. Evaluate Logistic Regression and Random Forest.
2. Select the model using mean development-fold PR-AUC only.
3. Select each model's classification threshold using development out-of-fold probabilities only.
4. Refit on the complete development partition.
5. Evaluate the untouched stratified holdout once and report ROC-AUC, PR-AUC, bad-class precision, recall, F1 and balanced accuracy.
6. Keep holdout results separate from development cross-validation results.
7. Provide holdout subgroup diagnostics with group counts and limitations.

## Required evidence

- `outputs/final_evaluation_metrics.json`
- `outputs/final_model_comparison.csv`
- `outputs/holdout_predictions.csv`
- `outputs/holdout_subgroup_metrics.csv`
- `reports/nivesh/Nivesh_Days6-11_Final_Model_Evaluation.md`
- Successful GitHub Actions run and its uploaded artifact.

## Sign-off rule

This document is not marked complete until the workflow passes and all generated files are reviewed. Semantic/post-outcome feature review remains a manual requirement. Subgroup results are descriptive diagnostics, not proof of fairness. The dataset's Risk field is a historical good/bad label, not a verified future-default event. This educational project is not a production lending decision system.
