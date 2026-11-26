# Nivesh — Days 6 to 11 (separate submission files)

This package contains an individual Markdown submission record for each assigned day, plus one shared evaluation script and dependency file.

## Day-wise documents
- `reports/Day6_5Fold_Model_Execution.md`
- `reports/Day7_Stratified_CV_Comparison_Threshold_Analysis.md`
- `reports/Day8_Verification_Holdout_Performance.md`
- `reports/Day9_Rerun_Validation_Leakage_Check.md`
- `reports/Day10_Reproducibility_Repeat_Validation.md`
- `reports/Day11_Final_Model_Evaluation_and_Signoff.md`

## Shared execution files
- `src/run_final_evaluation.py`
- `requirements.txt`

## Run from repository root
```bash
python -m pip install -r requirements.txt
python src/run_final_evaluation.py --data german_credit_data.csv
```

**Important:** The day-wise documents describe the assigned work and the evidence required. Actual numerical metrics are not fabricated; generate them by running the script on the project's real `german_credit_data.csv`, then add the generated `outputs/` and final report.
