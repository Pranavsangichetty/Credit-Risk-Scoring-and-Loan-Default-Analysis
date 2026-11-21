"""Train exploratory baseline classifiers for the German Credit risk label.

Run from the repository root:
    python -m pip install -r requirements.txt
    python src/train_baseline.py --data german_credit_data.csv

The target is the supplied historical good/bad label, not a directly observed
future-default outcome. Metrics are written to outputs/ and are not hard-coded.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    average_precision_score,
    balanced_accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


ROOT = Path(__file__).resolve().parents[1]
TARGET = "Risk"
RANDOM_STATE = 42


def load_dataset(path: Path) -> tuple[pd.DataFrame, pd.Series]:
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")
    data = pd.read_csv(path)
    # Drop common exported index columns; they are identifiers, not predictors.
    data = data.loc[:, ~data.columns.astype(str).str.match(r"^Unnamed:")]
    if TARGET not in data.columns:
        raise ValueError(f"Required target column {TARGET!r} is missing.")
    data = data.dropna(subset=[TARGET]).copy()
    target = data.pop(TARGET).astype(str).str.strip().str.lower()
    mapping = {"good": 0, "bad": 1}
    unexpected = sorted(set(target.unique()) - set(mapping))
    if unexpected:
        raise ValueError(f"Unexpected target labels: {unexpected}; expected good/bad.")
    y = target.map(mapping).astype(int)
    if y.nunique() != 2:
        raise ValueError("Both good and bad classes are required for evaluation.")
    return data, y


def build_pipeline(X: pd.DataFrame, estimator) -> Pipeline:
    numeric = X.select_dtypes(include=["number"]).columns.tolist()
    categorical = [c for c in X.columns if c not in numeric]
    transformers = []
    if numeric:
        numeric_pipe = Pipeline(
            steps=[
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler()),
            ]
        )
        transformers.append(("numeric", numeric_pipe, numeric))
    if categorical:
        categorical_pipe = Pipeline(
            steps=[
                # Keep missing category information explicit rather than
                # treating an unknown account balance as a zero balance.
                ("imputer", SimpleImputer(strategy="constant", fill_value="Unknown")),
                ("onehot", OneHotEncoder(handle_unknown="ignore")),
            ]
        )
        transformers.append(("categorical", categorical_pipe, categorical))
    preprocessor = ColumnTransformer(transformers=transformers, remainder="drop")
    return Pipeline(
        steps=[("preprocess", preprocessor), ("model", estimator)]
    )


def evaluate(name: str, model: Pipeline, X_test: pd.DataFrame, y_test: pd.Series) -> dict:
    predicted = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]
    return {
        "model": name,
        "threshold": 0.5,
        "accuracy": float(accuracy_score(y_test, predicted)),
        "balanced_accuracy": float(balanced_accuracy_score(y_test, predicted)),
        "bad_precision": float(precision_score(y_test, predicted, zero_division=0)),
        "bad_recall": float(recall_score(y_test, predicted, zero_division=0)),
        "bad_f1": float(f1_score(y_test, predicted, zero_division=0)),
        "roc_auc": float(roc_auc_score(y_test, probabilities)),
        "pr_auc_average_precision": float(average_precision_score(y_test, probabilities)),
        "confusion_matrix_labels_0_good_1_bad": confusion_matrix(
            y_test, predicted, labels=[0, 1]
        ).tolist(),
        "classification_report": classification_report(
            y_test, predicted, labels=[0, 1],
            target_names=["good", "bad"], output_dict=True, zero_division=0
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=ROOT / "german_credit_data.csv")
    parser.add_argument("--output", type=Path, default=ROOT / "outputs")
    args = parser.parse_args()

    X, y = load_dataset(args.data)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=RANDOM_STATE, stratify=y
    )

    candidates = {
        "logistic_regression": LogisticRegression(
            max_iter=2000, class_weight="balanced", random_state=RANDOM_STATE
        ),
        "random_forest": RandomForestClassifier(
            n_estimators=400, min_samples_leaf=3, class_weight="balanced",
            random_state=RANDOM_STATE, n_jobs=-1
        ),
    }

    args.output.mkdir(parents=True, exist_ok=True)
    summary = {
        "dataset": str(args.data),
        "rows": int(len(X)),
        "features_before_encoding": X.columns.tolist(),
        "target_mapping": {"good": 0, "bad": 1},
        "class_counts": {
            "good_0": int((y == 0).sum()),
            "bad_1": int((y == 1).sum()),
        },
        "split": {
            "test_size": 0.20,
            "random_state": RANDOM_STATE,
            "stratified": True,
            "train_rows": int(len(X_train)),
            "test_rows": int(len(X_test)),
        },
        "models": [],
        "caveat": (
            "Exploratory classification of the supplied historical good/bad risk "
            "label; not validated prediction of future loan default."
        ),
    }

    fitted = {}
    for name, estimator in candidates.items():
        pipeline = build_pipeline(X_train, estimator)
        pipeline.fit(X_train, y_train)
        fitted[name] = pipeline
        summary["models"].append(evaluate(name, pipeline, X_test, y_test))
        joblib.dump(pipeline, args.output / f"{name}.joblib")

    # Save a clearly labelled hold-out prediction file for review.
    best_name = max(summary["models"], key=lambda m: m["pr_auc_average_precision"])["model"]
    best_model = fitted[best_name]
    predictions = pd.DataFrame({
        "row_index": X_test.index,
        "actual_risk_bad_1": y_test.to_numpy(),
        "predicted_risk_bad_1": best_model.predict(X_test),
        "predicted_probability_bad": best_model.predict_proba(X_test)[:, 1],
        "selected_model_by_holdout_pr_auc": best_name,
    }).sort_values("row_index")
    predictions.to_csv(args.output / "holdout_predictions.csv", index=False)

    with (args.output / "metrics.json").open("w", encoding="utf-8") as handle:
        json.dump(summary, handle, indent=2)
    print(json.dumps({
        "rows": summary["rows"],
        "class_counts": summary["class_counts"],
        "models": [
            {k: m[k] for k in (
                "model", "accuracy", "balanced_accuracy", "bad_precision",
                "bad_recall", "bad_f1", "roc_auc", "pr_auc_average_precision"
            )}
            for m in summary["models"]
        ],
        "outputs": str(args.output),
    }, indent=2))


if __name__ == "__main__":
    main()
