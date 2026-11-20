# Day 5 — Model Validation and Review

**Owner:** Nivesh (ML and model development)  
**Date:** 20 November 2026  
**Branch:** `Nivesh243`

## Objective

Validate the Day 4 Logistic Regression and Random Forest baselines with out-of-fold predictions, inspect threshold trade-offs and produce exploratory subgroup metrics. This report describes the validation procedure; it does not claim results before the code is run.

## Run commands

From the repository root:

```bash
python -m pip install -r requirements.txt
python src/train_baseline.py --data german_credit_data.csv
python src/validate_baseline.py --data german_credit_data.csv
```

The validation script writes:

- `outputs/cross_validation_metrics.json` — 5-fold out-of-fold metrics, threshold analysis and subgroup metrics at the default 0.50 threshold.

## Validation design

- Use 5-fold stratified cross-validation with shuffle enabled and random seed 42.
- Generate out-of-fold predicted probabilities so each row is evaluated by a model that did not train on that row.
- Compare Logistic Regression and Random Forest using ROC-AUC and average precision (PR-AUC).
- At threshold 0.50, report bad-risk precision, recall, F1 and balanced accuracy.
- Review thresholds 0.25, 0.35, 0.45, 0.50, 0.60 and 0.70 to understand the precision/recall trade-off.
- Review metrics by Sex and age bands as a diagnostic only. Small subgroup counts make estimates unstable.

## Review requirements

1. Execute both the Day 4 training script and this validation script in the project environment.
2. Confirm that the generated JSON files are present and inspect them before sharing any metric.
3. Compare cross-validation results with the Day 4 single hold-out results; explain differences rather than selecting the best-looking score.
4. Do not treat a threshold as a lending policy. Any threshold decision needs an explicit discussion of false-negative and false-positive costs.
5. Record package versions, command, random seed and dataset version with the final results.

## Limitations

- The supplied target is a historical `good` / `bad` risk label, not a directly observed future default event with a documented prediction horizon.
- The dataset contains 1,000 rows, so results are exploratory and may vary across splits.
- Subgroup metrics are not proof of fairness or legal compliance.
- Age and Sex require careful fairness, legal and governance review.
- This project is educational and is not suitable for real credit approval or denial.

## Day 5 completion checklist

- [ ] Run the Day 4 baseline training script.
- [ ] Run the 5-fold validation script.
- [ ] Review and share actual metrics.
- [ ] Explain threshold trade-offs.
- [ ] Review subgroup metrics and sample counts.
- [ ] Update this report with verified findings only.
