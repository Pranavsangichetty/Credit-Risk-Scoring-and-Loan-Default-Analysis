# Day 4 — Baseline Machine-Learning Models and Evaluation

**Owner:** Nivesh — ML and Model Development  
**Project:** Credit Risk Scoring and Loan Default Analysis  
**Date:** 19 November 2026  
**Branch:** `Nivesh243`

## Assigned task
Build baseline machine-learning models and evaluate their performance.

## Models
1. Logistic Regression
2. Random Forest Classifier

Both models use the preprocessing pipeline documented in Day 2 and Day 3. Class weighting is enabled to account for the reported 70:30 good/bad target distribution.

## Experimental design
- Stratified 80:20 train/test split.
- Random seed: 42.
- Preprocessing fitted on training data only.
- Probability threshold: 0.50 for the baseline class predictions.

## Evaluation metrics
The baseline script calculates:
- Accuracy
- Balanced accuracy
- Precision for the bad-risk class
- Recall for the bad-risk class
- F1-score for the bad-risk class
- ROC-AUC
- Average precision (PR-AUC)
- Confusion matrix
- Classification report

The bad-risk class is the positive class (`1`). Recall for this class is important because a false negative means a record labelled bad is predicted as good by the classifier.

## Implementation
Run from the repository root:

```bash
python -m pip install -r requirements.txt
python src/train_baseline.py --data german_credit_data.csv
```

Expected generated files:
- `outputs/metrics.json`
- `outputs/holdout_predictions.csv`
- `outputs/logistic_regression.joblib`
- `outputs/random_forest.joblib`

## Results reporting
Metrics must be copied from the generated `outputs/metrics.json` after the script has been executed. No performance values are hard-coded in this document.

**Execution status:** The repository contains the baseline implementation. The results should be marked complete only after running the script in the project environment and checking the generated output files.

## Interpretation and limitation
The source target is a historical `good`/`bad` risk label. It must not be described as a verified future loan-default event. These models are exploratory educational baselines and are not a production lending decision system.
