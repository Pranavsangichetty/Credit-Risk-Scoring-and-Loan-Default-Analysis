from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd
import shap


ROOT = Path(__file__).resolve().parents[1]

DATA_PATH = ROOT / "german_credit_data.csv"
MODEL_PATH = ROOT / "outputs" / "random_forest.joblib"
OUTPUT_DIR = ROOT / "outputs" / "shap"


# Load dataset
data = pd.read_csv(DATA_PATH)

# Remove exported index column
data = data.loc[:, ~data.columns.astype(str).str.match(r"^Unnamed:")]

# Separate target
X = data.drop(columns=["Risk"])

# Load trained pipeline
model = joblib.load(MODEL_PATH)

# Get preprocessing and Random Forest model
preprocessor = model.named_steps["preprocess"]
classifier = model.named_steps["model"]

# Transform original data into numeric features
X_transformed = preprocessor.transform(X)

# Get feature names after preprocessing
feature_names = preprocessor.get_feature_names_out()

# Convert transformed data to DataFrame
X_transformed = pd.DataFrame(
    X_transformed,
    columns=feature_names,
    index=X.index
)

# Create SHAP Tree Explainer for Random Forest
explainer = shap.TreeExplainer(classifier)

# Calculate SHAP values
shap_values = explainer.shap_values(X_transformed)

# Select class 1 = bad risk
if isinstance(shap_values, list):
    values = shap_values[1]
else:
    values = shap_values[:, :, 1]

# Create output directory
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# SHAP summary plot
plt.figure()
shap.summary_plot(
    values,
    X_transformed,
    max_display=15,
    show=False
)
plt.title("SHAP Summary Plot - Random Forest")
plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "shap_summary.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# Mean absolute SHAP importance
importance = pd.DataFrame({
    "feature": feature_names,
    "mean_abs_shap": abs(values).mean(axis=0)
}).sort_values(
    "mean_abs_shap",
    ascending=False
)

# Save feature importance
importance.to_csv(
    OUTPUT_DIR / "shap_feature_importance.csv",
    index=False
)

# SHAP bar plot
plt.figure()
shap.summary_plot(
    values,
    X_transformed,
    plot_type="bar",
    max_display=15,
    show=False
)
plt.title("SHAP Feature Importance - Random Forest")
plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "shap_feature_importance.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

print("\nSHAP analysis completed successfully.")

print("\nTop 10 SHAP features:")
print(
    importance.head(10).to_string(index=False)
)

print(
    f"\nResults saved to: {OUTPUT_DIR}"
)