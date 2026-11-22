# Nivesh — Final ML Results Report

**Status: Pending execution against the actual project dataset.**

Run the command below to generate this report with actual values:

```bash
python -m pip install -r requirements.txt
python src/nivesh_ml_validation.py --data german_credit_data.csv
```

The script writes the executed report to this path, including:
- Logistic Regression and Random Forest 5-fold out-of-fold metrics
- ROC-AUC and PR-AUC
- Bad-class precision, recall and F1
- Threshold comparison
- Sex and age-band subgroup results
- Limitations and interpretation

No numerical model scores are supplied here because the original `german_credit_data.csv` was not provided in this conversation. Do not submit placeholder values as measured results.
