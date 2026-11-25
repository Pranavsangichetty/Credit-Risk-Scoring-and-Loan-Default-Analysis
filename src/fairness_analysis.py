from pathlib import Path

import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


ROOT = Path(__file__).resolve().parents[1]

DATA_PATH = ROOT / "german_credit_data.csv"
MODEL_PATH = ROOT / "outputs" / "random_forest.joblib"
OUTPUT_DIR = ROOT / "outputs" / "fairness"


# Load dataset
data = pd.read_csv(DATA_PATH)

# Remove exported index column
data = data.loc[:, ~data.columns.astype(str).str.match(r"^Unnamed:")]

# Target
y = data["Risk"].map({"good": 0, "bad": 1})

# Features
X = data.drop(columns=["Risk"])

# Load trained Random Forest pipeline
model = joblib.load(MODEL_PATH)

# Predicted probability and class
probability = model.predict_proba(X)[:, 1]
prediction = model.predict(X)

# Add predictions to analysis dataset
analysis = data.copy()
analysis["actual_bad"] = y
analysis["predicted_bad"] = prediction
analysis["bad_probability"] = probability

# Create age groups
analysis["Age_group"] = pd.cut(
    analysis["Age"],
    bins=[0, 29, 44, float("inf")],
    labels=["Young (<30)", "Middle (30-44)", "Older (45+)"]
)


def calculate_metrics(group):
    return pd.Series({
        "samples": len(group),
        "bad_rate_actual": group["actual_bad"].mean(),
        "bad_rate_predicted": group["predicted_bad"].mean(),
        "mean_bad_probability": group["bad_probability"].mean(),
        "accuracy": accuracy_score(
            group["actual_bad"],
            group["predicted_bad"]
        ),
        "precision": precision_score(
            group["actual_bad"],
            group["predicted_bad"],
            zero_division=0
        ),
        "recall": recall_score(
            group["actual_bad"],
            group["predicted_bad"],
            zero_division=0
        ),
        "f1": f1_score(
            group["actual_bad"],
            group["predicted_bad"],
            zero_division=0
        ),
    })


# Sex subgroup analysis
sex_results = (
    analysis
    .groupby("Sex", observed=True)
    .apply(calculate_metrics, include_groups=False)
    .reset_index()
)

# Age subgroup analysis
age_results = (
    analysis
    .groupby("Age_group", observed=True)
    .apply(calculate_metrics, include_groups=False)
    .reset_index()
)

# Create output directory
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Save results
sex_results.to_csv(
    OUTPUT_DIR / "sex_fairness_results.csv",
    index=False
)

age_results.to_csv(
    OUTPUT_DIR / "age_fairness_results.csv",
    index=False
)

# Print results
print("\n===== SEX FAIRNESS ANALYSIS =====")
print(sex_results.to_string(index=False))

print("\n===== AGE FAIRNESS ANALYSIS =====")
print(age_results.to_string(index=False))

print(f"\nResults saved to: {OUTPUT_DIR}")