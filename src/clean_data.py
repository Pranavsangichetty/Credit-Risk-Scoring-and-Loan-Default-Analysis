from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "german_credit_data.csv"
OUT_PATH = ROOT / "data" / "interim" / "german_credit_cleaned.csv"
LOG_PATH = ROOT / "reports" / "day3_transformation_log.md"

df = pd.read_csv(RAW_PATH)
raw_shape = df.shape
raw_missing = df.isna().sum()

# Remove only from the working copy: audit found this is a sequential index.
working = df.drop(columns=["Unnamed: 0"], errors="ignore").copy()

# Keep missing categorical values explicit for EDA; do not infer a category.
categorical_cols = working.select_dtypes(include=["object", "category"]).columns
for col in categorical_cols:
    working[col] = working[col].fillna("Missing")

OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
working.to_csv(OUT_PATH, index=False)

with LOG_PATH.open("w") as f:
    f.write("# Day 3 — Cleaning and Preprocessing Log\n\n")
    f.write("## Input and output\n")
    f.write(f"- Input: `{RAW_PATH.name}` (raw file left unchanged)\n")
    f.write(f"- Raw shape: {raw_shape[0]} rows × {raw_shape[1]} columns\n")
    f.write(f"- Output: `{OUT_PATH.relative_to(ROOT)}`\n")
    f.write(f"- Output shape: {working.shape[0]} rows × {working.shape[1]} columns\n\n")
    f.write("## Transformations\n")
    f.write("- Removed `Unnamed: 0` from the working copy only; audit identified it as a sequential index.\n")
    f.write("- Replaced missing values in categorical columns with the explicit label `Missing` for EDA.\n")
    f.write("- No rows were dropped; no numeric values were imputed or changed.\n")
    f.write("- No model imputer or encoder was fitted. Those must be fitted on training data only in the model pipeline.\n\n")
    f.write("## Before/after missingness\n")
    f.write("| Column | Raw missing | Working-copy missing |\n|---|---:|---:|\n")
    for col in df.columns:
        after = working[col].isna().sum() if col in working.columns else "— (column removed)"
        f.write(f"| {col} | {int(raw_missing[col])} | {after} |\n")

print("Raw shape:", raw_shape)
print("Working shape:", working.shape)
print("Remaining missing values:", int(working.isna().sum().sum()))
print("Saved:", OUT_PATH)
print("Saved:", LOG_PATH)
