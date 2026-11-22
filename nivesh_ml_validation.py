#!/usr/bin/env python3
"""Execute Logistic Regression and Random Forest with stratified 5-fold CV.

Run from the repository root:
    python src/nivesh_ml_validation.py --data german_credit_data.csv

The script creates actual metrics only after it reads and processes the supplied CSV.
Positive class: Risk == "bad" (encoded as 1).
"""
from __future__ import annotations

import argparse
import json
import warnings
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, average_precision_score, balanced_accuracy_score,
    classification_report, confusion_matrix, f1_score, precision_score,
    recall_score, roc_auc_score, RocCurveDisplay, PrecisionRecallDisplay
)
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
REPORT = ROOT / "reports" / "Nivesh_Day4_Day6_ML_Results.md"
RANDOM_STATE = 42
THRESHOLDS = [0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80]

def load_data(path: Path):
    df = pd.read_csv(path)
    df.columns = [str(c).strip() for c in df.columns]
    df = df.loc[:, ~pd.Index(df.columns).str.match(r"^Unnamed")]
    if "Risk" not in df.columns:
        raise ValueError("Expected target column 'Risk' was not found.")
    df = df.dropna(subset=["Risk"]).copy()
    labels = df["Risk"].astype(str).str.strip().str.lower()
    unexpected = sorted(set(labels) - {"good", "bad"})
    if unexpected:
        raise ValueError(f"Unexpected Risk labels: {unexpected}; expected good/bad.")
    y = labels.map({"good": 0, "bad": 1}).astype(int)
    X = df.drop(columns=["Risk"]).copy()
    if X.empty:
        raise ValueError("No predictor columns remain after removing target/index.")
    return df, X, y

def make_pipeline(X, estimator):
    numeric = X.select_dtypes(include=["number"]).columns.tolist()
    categorical = [c for c in X.columns if c not in numeric]
    transformers = []
    if numeric:
        numeric_pipe = Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ])
        transformers.append(("numeric", numeric_pipe, numeric))
    if categorical:
        categorical_pipe = Pipeline([
            ("imputer", SimpleImputer(strategy="constant", fill_value="Unknown")),
            ("onehot", OneHotEncoder(handle_unknown="ignore"))
        ])
        transformers.append(("categorical", categorical_pipe, categorical))
    prep = ColumnTransformer(transformers=transformers, remainder="drop")
    return Pipeline([("preprocess", prep), ("model", estimator)])

def safe_auc(y, p):
    return float(roc_auc_score(y, p)) if len(np.unique(y)) == 2 else None

def subgroup_rows(df, y, pred, group_col, model_name):
    if group_col not in df.columns:
        return []
    rows = []
    tmp = pd.DataFrame({
        "group": df[group_col].fillna("Unknown").astype(str),
        "actual": np.asarray(y),
        "predicted": np.asarray(pred)
    })
    for group, part in tmp.groupby("group", dropna=False):
        if len(part) < 5:
            note = "Small subgroup (n<5); metrics are highly unstable."
        else:
            note = ""
        rows.append({
            "model": model_name, "attribute": group_col, "group": str(group),
            "n": int(len(part)), "actual_bad": int(part["actual"].sum()),
            "predicted_bad": int(part["predicted"].sum()),
            "bad_precision": float(precision_score(part.actual, part.predicted, zero_division=0)),
            "bad_recall": float(recall_score(part.actual, part.predicted, zero_division=0)),
            "bad_f1": float(f1_score(part.actual, part.predicted, zero_division=0)),
            "note": note
        })
    return rows

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="german_credit_data.csv")
    args = parser.parse_args()
    data_path = Path(args.data)
    if not data_path.is_absolute():
        data_path = ROOT / data_path
    if not data_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {data_path}\n"
            "Place german_credit_data.csv in the repository root or pass --data /path/to/file.csv."
        )

    df, X, y = load_data(data_path)
    if y.nunique() != 2 or y.value_counts().min() < 5:
        raise ValueError("Need both Risk classes and at least five records in each class for 5-fold CV.")

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
    models = {
        "Logistic Regression": LogisticRegression(
            max_iter=3000, class_weight="balanced", random_state=RANDOM_STATE
        ),
        "Random Forest": RandomForestClassifier(
            n_estimators=500, min_samples_leaf=3, class_weight="balanced",
            random_state=RANDOM_STATE, n_jobs=-1
        )
    }

    OUT.mkdir(parents=True, exist_ok=True)
    result = {
        "project": "Credit Risk Scoring and Loan Default Analysis",
        "owner": "Nivesh — ML / Model Development",
        "dataset": data_path.name,
        "rows": int(len(df)),
        "features": list(X.columns),
        "class_counts": {"good_0": int((y == 0).sum()), "bad_1": int((y == 1).sum())},
        "validation": "Stratified 5-fold cross-validation; pooled out-of-fold probabilities",
        "random_state": RANDOM_STATE,
        "positive_class": "bad (1)",
        "models": {},
        "limitations": (
            "Risk is the supplied historical good/bad label. It is not established by this dataset "
            "alone as a directly observed future loan-default outcome with a defined observation horizon. "
            "Results are educational historical-label classification, not a production lending model."
        )
    }
    comparison, thresholds, subgroup, predictions = [], [], [], []
    fig_roc, ax_roc = plt.subplots()
    fig_pr, ax_pr = plt.subplots()

    for name, estimator in models.items():
        pipe = make_pipeline(X, estimator)
        # Out-of-fold probabilities: every row is predicted by a model that did not train on it.
        prob = cross_val_predict(pipe, X, y, cv=cv, method="predict_proba", n_jobs=None)[:, 1]
        fold_auc, fold_ap = [], []
        for train_idx, valid_idx in cv.split(X, y):
            fold_pipe = make_pipeline(X, estimator)
            fold_pipe.fit(X.iloc[train_idx], y.iloc[train_idx])
            fold_prob = fold_pipe.predict_proba(X.iloc[valid_idx])[:, 1]
            fold_auc.append(safe_auc(y.iloc[valid_idx], fold_prob))
            fold_ap.append(float(average_precision_score(y.iloc[valid_idx], fold_prob)))

        pred50 = (prob >= 0.50).astype(int)
        cm = confusion_matrix(y, pred50, labels=[0, 1])
        model_result = {
            "roc_auc": safe_auc(y, prob),
            "pr_auc_average_precision": float(average_precision_score(y, prob)),
            "fold_roc_auc_mean": float(np.mean(fold_auc)),
            "fold_roc_auc_std": float(np.std(fold_auc, ddof=1)),
            "fold_pr_auc_mean": float(np.mean(fold_ap)),
            "fold_pr_auc_std": float(np.std(fold_ap, ddof=1)),
            "default_threshold_metrics": {
                "threshold": 0.50,
                "accuracy": float(accuracy_score(y, pred50)),
                "balanced_accuracy": float(balanced_accuracy_score(y, pred50)),
                "precision_bad": float(precision_score(y, pred50, zero_division=0)),
                "recall_bad": float(recall_score(y, pred50, zero_division=0)),
                "f1_bad": float(f1_score(y, pred50, zero_division=0)),
                "confusion_matrix_labels_0_good_1_bad": cm.tolist()
            },
            "threshold_analysis": [],
            "subgroup_metrics_at_0_5": []
        }
        for threshold in THRESHOLDS:
            pred = (prob >= threshold).astype(int)
            row = {
                "threshold": threshold,
                "predicted_bad": int(pred.sum()),
                "bad_precision": float(precision_score(y, pred, zero_division=0)),
                "bad_recall": float(recall_score(y, pred, zero_division=0)),
                "bad_f1": float(f1_score(y, pred, zero_division=0)),
                "balanced_accuracy": float(balanced_accuracy_score(y, pred))
            }
            model_result["threshold_analysis"].append(row)
            thresholds.append({"model": name, **row})

        groups = subgroup_rows(df, y, pred50, "Sex", name)
        # Age bands are descriptive; use only if Age is present and numeric.
        if "Age" in df.columns:
            age = pd.to_numeric(df["Age"], errors="coerce")
            age_band = pd.cut(age, bins=[0, 25, 35, 50, np.inf],
                              labels=["18-25", "26-35", "36-50", "51+"], include_lowest=True)
            age_df = df.copy()
            age_df["Age band"] = age_band.astype("object").fillna("Unknown")
            groups += subgroup_rows(age_df, y, pred50, "Age band", name)
        model_result["subgroup_metrics_at_0_5"] = groups
        subgroup.extend(groups)
        result["models"][name] = model_result
        comparison.append({
            "model": name, "roc_auc_oof": model_result["roc_auc"],
            "pr_auc_average_precision_oof": model_result["pr_auc_average_precision"],
            "fold_roc_auc_mean": model_result["fold_roc_auc_mean"],
            "fold_roc_auc_std": model_result["fold_roc_auc_std"],
            "bad_precision_at_0_50": model_result["default_threshold_metrics"]["precision_bad"],
            "bad_recall_at_0_50": model_result["default_threshold_metrics"]["recall_bad"],
            "bad_f1_at_0_50": model_result["default_threshold_metrics"]["f1_bad"],
            "balanced_accuracy_at_0_50": model_result["default_threshold_metrics"]["balanced_accuracy"]
        })
        for i, (actual, probability, predicted) in enumerate(zip(y, prob, pred50)):
            predictions.append({
                "row_index": int(i), "model": name, "actual_risk_bad_1": int(actual),
                "oof_probability_bad": float(probability), "predicted_bad_at_0_50": int(predicted)
            })
        RocCurveDisplay.from_predictions(y, prob, name=name, ax=ax_roc)
        PrecisionRecallDisplay.from_predictions(y, prob, name=name, ax=ax_pr)

    comparison_df = pd.DataFrame(comparison)
    comparison_df.to_csv(OUT / "model_comparison.csv", index=False)
    pd.DataFrame(thresholds).to_csv(OUT / "threshold_analysis.csv", index=False)
    pd.DataFrame(subgroup).to_csv(OUT / "subgroup_metrics.csv", index=False)
    pd.DataFrame(predictions).to_csv(OUT / "oof_predictions.csv", index=False)
    with open(OUT / "cross_validation_metrics.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    ax_roc.plot([0, 1], [0, 1], linestyle="--", linewidth=1)
    ax_roc.set_title("5-fold out-of-fold ROC curves")
    fig_roc.tight_layout()
    fig_roc.savefig(OUT / "roc_curve_5fold.png", dpi=160)
    ax_pr.set_title("5-fold out-of-fold Precision–Recall curves")
    fig_pr.tight_layout()
    fig_pr.savefig(OUT / "precision_recall_curve_5fold.png", dpi=160)
    plt.close(fig_roc); plt.close(fig_pr)

    lines = [
        "# Nivesh — Day 4 to Day 6 ML Execution Results", "",
        f"- Dataset: `{data_path.name}`",
        f"- Rows evaluated: {len(df)}",
        f"- Class counts: good={int((y==0).sum())}, bad={int((y==1).sum())}",
        "- Validation: Stratified 5-fold cross-validation with out-of-fold probabilities",
        "- Positive class: `bad = 1`",
        "- Random state: 42", "",
        "## Model comparison", "",
        comparison_df.to_markdown(index=False, floatfmt=".4f"), "",
        "## Threshold analysis", "",
        pd.DataFrame(thresholds).to_markdown(index=False, floatfmt=".4f"), "",
        "## Subgroup analysis at threshold 0.50", "",
        (pd.DataFrame(subgroup).to_markdown(index=False, floatfmt=".4f")
         if subgroup else "No supported subgroup columns were available."), "",
        "Subgroup metrics are descriptive, not proof of fairness. Review subgroup sizes and class counts; "
        "small groups can produce unstable estimates. Sex-based analysis requires appropriate governance "
        "and should not be used as an unreviewed lending decision rule.", "",
        "## Generated artifacts", "",
        "- `outputs/cross_validation_metrics.json`",
        "- `outputs/model_comparison.csv`",
        "- `outputs/threshold_analysis.csv`",
        "- `outputs/subgroup_metrics.csv`",
        "- `outputs/oof_predictions.csv`",
        "- `outputs/roc_curve_5fold.png`",
        "- `outputs/precision_recall_curve_5fold.png`", "",
        "## Interpretation and limitations", "",
        result["limitations"], "",
        "ROC-AUC and average precision assess ranking quality across thresholds. Precision, recall and F1 "
        "at 0.50 describe the bad-risk class at one threshold. Lower thresholds generally flag more records "
        "as bad and can trade precision for recall. The threshold should be selected only with stakeholder "
        "costs, calibration, policy and legal review; this analysis does not prescribe a lending cutoff.", ""
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print("Completed. Actual results saved under outputs/ and report written to", REPORT)
    print(comparison_df.to_string(index=False))

if __name__ == "__main__":
    warnings.filterwarnings("ignore", category=FutureWarning)
    main()
