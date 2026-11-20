"""Run leakage-safe 5-fold out-of-fold validation for baseline classifiers.

Run from repository root:
    python src/validate_baseline.py --data german_credit_data.csv

Outputs are exploratory and classify the supplied historical good/bad label.
They are not validated predictions of future loan default.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    average_precision_score,
    balanced_accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import StratifiedKFold, cross_val_predict

from train_baseline import RANDOM_STATE, build_pipeline, load_dataset


def binary_metrics(y_true: pd.Series, probabilities: np.ndarray, threshold: float) -> dict:
    predicted = (probabilities >= threshold).astype(int)
    return {
        "threshold": float(threshold),
        "precision_bad": float(precision_score(y_true, predicted, zero_division=0)),
        "recall_bad": float(recall_score(y_true, predicted, zero_division=0)),
        "f1_bad": float(f1_score(y_true, predicted, zero_division=0)),
        "balanced_accuracy": float(balanced_accuracy_score(y_true, predicted)),
    }


def subgroup_report(X: pd.DataFrame, y: pd.Series, probabilities: np.ndarray) -> list[dict]:
    rows: list[dict] = []
    groups = {}
    if "Sex" in X.columns:
        groups["sex"] = X["Sex"].astype("string").fillna("Unknown")
    if "Age" in X.columns:
        groups["age_band"] = pd.cut(
            pd.to_numeric(X["Age"], errors="coerce"),
            bins=[0, 25, 35, 50, 120],
            labels=["18-25", "26-35", "36-50", "51+"],
            include_lowest=True,
        ).astype("string").fillna("Unknown")

    predicted = (probabilities >= 0.5).astype(int)
    for dimension, labels in groups.items():
        for group in sorted(labels.unique()):
            mask = labels.to_numpy() == group
            count = int(mask.sum())
            if count == 0:
                continue
            rows.append({
                "dimension": dimension,
                "group": str(group),
                "n": count,
                "bad_label_count": int(y.to_numpy()[mask].sum()),
                "bad_precision": float(precision_score(y.to_numpy()[mask], predicted[mask], zero_division=0)),
                "bad_recall": float(recall_score(y.to_numpy()[mask], predicted[mask], zero_division=0)),
                "note": "Interpret cautiously; small subgroup counts are unstable.",
            })
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--data",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "german_credit_data.csv",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "outputs",
    )
    args = parser.parse_args()

    X, y = load_dataset(args.data)
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
    models = {
        "logistic_regression": LogisticRegression(
            max_iter=2000, class_weight="balanced", random_state=RANDOM_STATE
        ),
        "random_forest": RandomForestClassifier(
            n_estimators=400,
            min_samples_leaf=3,
            class_weight="balanced",
            random_state=RANDOM_STATE,
            n_jobs=-1,
        ),
    }

    args.output.mkdir(parents=True, exist_ok=True)
    report = {
        "validation": "5-fold stratified out-of-fold predictions",
        "random_state": RANDOM_STATE,
        "rows": int(len(X)),
        "target_mapping": {"good": 0, "bad": 1},
        "models": {},
        "interpretation": (
            "Exploratory cross-validation for the supplied historical good/bad risk label; "
            "not validated future-default prediction. Thresholds are diagnostic and must "
            "not be treated as lending policy."
        ),
    }

    for name, estimator in models.items():
        pipeline = build_pipeline(X, estimator)
        probabilities = cross_val_predict(
            pipeline, X, y, cv=cv, method="predict_proba", n_jobs=-1
        )[:, 1]
        report["models"][name] = {
            "roc_auc": float(roc_auc_score(y, probabilities)),
            "pr_auc_average_precision": float(average_precision_score(y, probabilities)),
            "default_threshold_metrics": binary_metrics(y, probabilities, 0.5),
            "threshold_analysis": [
                binary_metrics(y, probabilities, threshold)
                for threshold in (0.25, 0.35, 0.45, 0.50, 0.60, 0.70)
            ],
            "subgroup_metrics_at_0_5": subgroup_report(X, y, probabilities),
        }

    output_file = args.output / "cross_validation_metrics.json"
    with output_file.open("w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2)

    print(json.dumps({
        name: {
            "roc_auc": values["roc_auc"],
            "pr_auc_average_precision": values["pr_auc_average_precision"],
            **values["default_threshold_metrics"],
        }
        for name, values in report["models"].items()
    }, indent=2))
    print(f"Saved validation report to {output_file}")


if __name__ == "__main__":
    main()
