#!/usr/bin/env python3
"""Leakage-aware final evaluation for the German Credit historical Risk label.

Run from repository root:
    python src/run_final_evaluation.py --data german_credit_data.csv

The untouched 20% holdout is used only for final reporting. Model selection and
threshold selection use development-set stratified CV / out-of-fold predictions.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import warnings
from pathlib import Path

import joblib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, average_precision_score, balanced_accuracy_score,
    confusion_matrix, f1_score, precision_score, recall_score, roc_auc_score,
    RocCurveDisplay, PrecisionRecallDisplay,
)
from sklearn.model_selection import (
    StratifiedKFold, cross_val_predict, cross_validate, train_test_split,
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

ROOT = Path(__file__).resolve().parents[1]
SEED = 42
TARGET = "Risk"
THRESHOLDS = np.round(np.arange(0.10, 0.901, 0.05), 2)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_dataset(path: Path):
    if not path.is_file():
        raise FileNotFoundError(f"Dataset not found: {path}")
    frame = pd.read_csv(path)
    frame.columns = [str(column).strip() for column in frame.columns]
    index_columns = [
        column for column in frame.columns
        if column.lower().startswith("unnamed:") or column.lower() in {"index", "row_id"}
    ]
    if index_columns:
        frame = frame.drop(columns=index_columns)
    if TARGET not in frame.columns:
        raise ValueError(f"Expected target '{TARGET}'. Found: {frame.columns.tolist()}")
    frame = frame.dropna(subset=[TARGET]).copy()
    labels = frame[TARGET].astype(str).str.strip().str.lower()
    unexpected = sorted(set(labels) - {"good", "bad"})
    if unexpected:
        raise ValueError(f"Unexpected target labels: {unexpected}")
    target = labels.map({"good": 0, "bad": 1}).astype(int)
    features = frame.drop(columns=[TARGET]).copy()
    if features.empty or target.nunique() != 2:
        raise ValueError("Both target classes and at least one predictor are required.")
    return frame, features, target, index_columns


def make_pipeline(features: pd.DataFrame, estimator):
    numeric = features.select_dtypes(include=["number"]).columns.tolist()
    categorical = [column for column in features.columns if column not in numeric]
    transformers = []
    if numeric:
        transformers.append((
            "numeric",
            Pipeline([
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler()),
            ]),
            numeric,
        ))
    if categorical:
        transformers.append((
            "categorical",
            Pipeline([
                ("imputer", SimpleImputer(strategy="constant", fill_value="Unknown")),
                ("onehot", OneHotEncoder(handle_unknown="ignore")),
            ]),
            categorical,
        ))
    return Pipeline([
        ("preprocess", ColumnTransformer(transformers, remainder="drop")),
        ("model", estimator),
    ])


def threshold_metrics(actual, probabilities, threshold):
    predicted = (np.asarray(probabilities) >= float(threshold)).astype(int)
    matrix = confusion_matrix(actual, predicted, labels=[0, 1])
    return {
        "threshold": float(threshold),
        "accuracy": float(accuracy_score(actual, predicted)),
        "balanced_accuracy": float(balanced_accuracy_score(actual, predicted)),
        "bad_precision": float(precision_score(actual, predicted, zero_division=0)),
        "bad_recall": float(recall_score(actual, predicted, zero_division=0)),
        "bad_f1": float(f1_score(actual, predicted, zero_division=0)),
        "tn": int(matrix[0, 0]), "fp": int(matrix[0, 1]),
        "fn": int(matrix[1, 0]), "tp": int(matrix[1, 1]),
        "predicted_bad": int(predicted.sum()),
    }


def subgroup_results(holdout_frame, actual, probabilities, threshold, model_name):
    predicted = (np.asarray(probabilities) >= threshold).astype(int)
    groups = {}
    if "Sex" in holdout_frame:
        groups["Sex"] = holdout_frame["Sex"].fillna("Unknown").astype(str)
    if "Age" in holdout_frame:
        age = pd.to_numeric(holdout_frame["Age"], errors="coerce")
        groups["Age band"] = pd.cut(
            age, [0, 25, 35, 50, np.inf],
            labels=["18-25", "26-35", "36-50", "51+"], include_lowest=True,
        ).astype("object").fillna("Unknown")
    rows = []
    for attribute, values in groups.items():
        subset = pd.DataFrame({
            "group": values.to_numpy(), "actual": np.asarray(actual), "predicted": predicted,
        })
        for group, part in subset.groupby("group", dropna=False):
            rows.append({
                "model": model_name, "attribute": attribute, "group": str(group),
                "n": int(len(part)), "actual_bad": int(part["actual"].sum()),
                "predicted_bad": int(part["predicted"].sum()),
                "bad_precision": float(precision_score(part.actual, part.predicted, zero_division=0)),
                "bad_recall": float(recall_score(part.actual, part.predicted, zero_division=0)),
                "bad_f1": float(f1_score(part.actual, part.predicted, zero_division=0)),
                "note": "Small holdout subgroup (n<10); interpret cautiously." if len(part) < 10 else "",
            })
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", default="german_credit_data.csv")
    parser.add_argument("--output", default="outputs")
    parser.add_argument("--reports", default="reports/nivesh")
    args = parser.parse_args()

    data_path = Path(args.data)
    if not data_path.is_absolute():
        data_path = ROOT / data_path
    output_dir = Path(args.output)
    if not output_dir.is_absolute():
        output_dir = ROOT / output_dir
    report_dir = Path(args.reports)
    if not report_dir.is_absolute():
        report_dir = ROOT / report_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    report_dir.mkdir(parents=True, exist_ok=True)

    frame, X, y, dropped_index_columns = load_dataset(data_path)
    if int(y.value_counts().min()) < 10:
        raise ValueError("At least 10 examples per class are required for the 80/20 + 5-fold protocol.")

    X_dev, X_holdout, y_dev, y_holdout = train_test_split(
        X, y, test_size=0.20, random_state=SEED, stratify=y,
    )
    dev_class_counts = y_dev.value_counts().to_dict()
    if min(dev_class_counts.values()) < 5:
        raise ValueError("Development partition has fewer than five records in a class.")

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
    estimators = {
        "Logistic Regression": LogisticRegression(
            max_iter=3000, class_weight="balanced", random_state=SEED,
        ),
        "Random Forest": RandomForestClassifier(
            n_estimators=500, min_samples_leaf=3, class_weight="balanced",
            random_state=SEED, n_jobs=-1,
        ),
    }
    metrics = {
        "project": "Credit Risk Scoring and Loan Default Analysis",
        "target_definition": "Historical Risk label: good=0, bad=1; bad is positive class.",
        "dataset": {
            "file": data_path.name, "sha256": sha256_file(data_path),
            "rows_after_target_validation": int(len(frame)),
            "feature_count": int(X.shape[1]), "features": X.columns.tolist(),
            "index_columns_removed": dropped_index_columns,
            "class_counts": {"good_0": int((y == 0).sum()), "bad_1": int((y == 1).sum())},
        },
        "environment": {
            "python": platform.python_version(), "platform": platform.platform(),
            "pandas": pd.__version__, "numpy": np.__version__,
            "scikit_learn": sklearn.__version__, "joblib": joblib.__version__,
        },
        "protocol": {
            "holdout": "Stratified 80/20 split; held out until final evaluation.",
            "development_cv": "Stratified 5-fold CV on development partition only.",
            "threshold_selection": "Maximum bad-class F1 on development out-of-fold probabilities; ties prefer recall then higher threshold.",
            "model_selection": "Highest mean development-fold PR-AUC; holdout metrics are reported but never used to choose the model.",
            "random_state": SEED, "positive_class": "bad (1)",
        },
        "split": {
            "development_rows": int(len(X_dev)), "holdout_rows": int(len(X_holdout)),
            "development_class_counts": {
                "good_0": int((y_dev == 0).sum()), "bad_1": int((y_dev == 1).sum()),
            },
            "holdout_class_counts": {
                "good_0": int((y_holdout == 0).sum()), "bad_1": int((y_holdout == 1).sum()),
            },
        },
        "leakage_checks": {
            "target_excluded_from_predictors": TARGET not in X.columns,
            "imputation_scaling_encoding_inside_pipeline": True,
            "preprocessing_refit_inside_each_cv_fold": True,
            "threshold_selected_without_holdout": True,
            "model_selection_based_on_development_cv_only": True,
            "semantic_post_outcome_feature_review": "Still requires domain review of source feature definitions; pipeline isolation cannot detect semantic leakage.",
        },
        "models": {},
    }

    fold_rows, threshold_rows, holdout_rows, subgroup_rows, comparison_rows = [], [], [], [], []
    roc_fig, roc_ax = plt.subplots(figsize=(7, 6))
    pr_fig, pr_ax = plt.subplots(figsize=(7, 6))

    for name, estimator in estimators.items():
        pipeline = make_pipeline(X_dev, estimator)
        fold_scores = cross_validate(
            pipeline, X_dev, y_dev, cv=cv,
            scoring={
                "roc_auc": "roc_auc", "pr_auc": "average_precision",
                "balanced_accuracy": "balanced_accuracy", "bad_f1": "f1",
            },
            return_train_score=False, error_score="raise",
        )
        oof = cross_val_predict(pipeline, X_dev, y_dev, cv=cv, method="predict_proba")[:, 1]
        threshold_table = [
            {"model": name, **threshold_metrics(y_dev, oof, threshold)}
            for threshold in THRESHOLDS
        ]
        threshold_rows.extend(threshold_table)
        selected = sorted(
            threshold_table,
            key=lambda row: (row["bad_f1"], row["bad_recall"], row["threshold"]),
            reverse=True,
        )[0]
        selected_threshold = float(selected["threshold"])

        fold_summary = {}
        for metric in ("roc_auc", "pr_auc", "balanced_accuracy", "bad_f1"):
            values = fold_scores[f"test_{metric}"]
            fold_summary[metric] = {
                "mean": float(np.mean(values)),
                "std": float(np.std(values, ddof=1)),
            }
            for fold_number, value in enumerate(values, start=1):
                fold_rows.append({
                    "model": name, "fold": fold_number,
                    "metric": metric, "score": float(value),
                })

        fitted = make_pipeline(X_dev, estimator)
        fitted.fit(X_dev, y_dev)
        probabilities = fitted.predict_proba(X_holdout)[:, 1]
        holdout_at_default = threshold_metrics(y_holdout, probabilities, 0.50)
        holdout_at_selected = threshold_metrics(y_holdout, probabilities, selected_threshold)
        holdout_roc = float(roc_auc_score(y_holdout, probabilities))
        holdout_pr = float(average_precision_score(y_holdout, probabilities))
        groups = subgroup_results(
            frame.loc[X_holdout.index], y_holdout, probabilities, selected_threshold, name,
        )
        subgroup_rows.extend(groups)

        metrics["models"][name] = {
            "development_cv": fold_summary,
            "development_oof": {
                "roc_auc": float(roc_auc_score(y_dev, oof)),
                "pr_auc_average_precision": float(average_precision_score(y_dev, oof)),
            },
            "threshold_selection": {
                "selected_threshold": selected_threshold,
                "development_oof_metrics": selected,
            },
            "holdout": {
                "roc_auc": holdout_roc, "pr_auc_average_precision": holdout_pr,
                "metrics_at_0_50": holdout_at_default,
                "metrics_at_development_selected_threshold": holdout_at_selected,
            },
        }
        comparison_rows.append({
            "model": name,
            "development_cv_roc_auc_mean": fold_summary["roc_auc"]["mean"],
            "development_cv_roc_auc_std": fold_summary["roc_auc"]["std"],
            "development_cv_pr_auc_mean": fold_summary["pr_auc"]["mean"],
            "development_cv_pr_auc_std": fold_summary["pr_auc"]["std"],
            "development_cv_balanced_accuracy_mean": fold_summary["balanced_accuracy"]["mean"],
            "development_cv_bad_f1_mean": fold_summary["bad_f1"]["mean"],
            "selected_threshold_from_development_oof": selected_threshold,
            "holdout_roc_auc": holdout_roc,
            "holdout_pr_auc": holdout_pr,
            "holdout_bad_precision_at_0_50": holdout_at_default["bad_precision"],
            "holdout_bad_recall_at_0_50": holdout_at_default["bad_recall"],
            "holdout_bad_f1_at_0_50": holdout_at_default["bad_f1"],
            "holdout_bad_precision_at_selected_threshold": holdout_at_selected["bad_precision"],
            "holdout_bad_recall_at_selected_threshold": holdout_at_selected["bad_recall"],
            "holdout_bad_f1_at_selected_threshold": holdout_at_selected["bad_f1"],
        })
        for row_index, actual, probability in zip(X_holdout.index, y_holdout, probabilities):
            holdout_rows.append({
                "row_index": int(row_index), "model": name, "actual_bad_1": int(actual),
                "probability_bad": float(probability),
                "predicted_bad_at_0_50": int(probability >= 0.50),
                "predicted_bad_at_selected_threshold": int(probability >= selected_threshold),
            })
        joblib.dump(fitted, output_dir / (name.lower().replace(" ", "_") + ".joblib"))
        RocCurveDisplay.from_predictions(y_holdout, probabilities, name=name, ax=roc_ax)
        PrecisionRecallDisplay.from_predictions(y_holdout, probabilities, name=name, ax=pr_ax)

    comparison = pd.DataFrame(comparison_rows).sort_values(
        "development_cv_pr_auc_mean", ascending=False,
    )
    metrics["selected_model_by_development_cv_pr_auc"] = str(comparison.iloc[0]["model"])
    metrics["model_selection_note"] = (
        "The selected model is determined only from development-fold mean PR-AUC. "
        "Holdout metrics are reported as final estimates and are not used to select a model."
    )

    comparison.to_csv(output_dir / "final_model_comparison.csv", index=False)
    pd.DataFrame(fold_rows).to_csv(output_dir / "stratified_5fold_metrics_by_fold.csv", index=False)
    pd.DataFrame(threshold_rows).to_csv(output_dir / "development_oof_threshold_analysis.csv", index=False)
    pd.DataFrame(holdout_rows).to_csv(output_dir / "holdout_predictions.csv", index=False)
    pd.DataFrame(subgroup_rows).to_csv(output_dir / "holdout_subgroup_metrics.csv", index=False)
    (output_dir / "final_evaluation_metrics.json").write_text(
        json.dumps(metrics, indent=2), encoding="utf-8",
    )

    roc_ax.plot([0, 1], [0, 1], "--", linewidth=1)
    roc_ax.set_title("Final holdout ROC curves")
    roc_fig.tight_layout()
    roc_fig.savefig(output_dir / "holdout_roc_curves.png", dpi=160)
    plt.close(roc_fig)
    pr_ax.set_title("Final holdout precision-recall curves")
    pr_fig.tight_layout()
    pr_fig.savefig(output_dir / "holdout_precision_recall_curves.png", dpi=160)
    plt.close(pr_fig)

    report = [
        "# Nivesh — Days 6–11 Final ML Evaluation", "",
        f"- Dataset: `{data_path.name}`",
        f"- SHA-256: `{metrics['dataset']['sha256']}`",
        f"- Rows: {len(frame)} | Features: {X.shape[1]} | Good: {(y == 0).sum()} | Bad: {(y == 1).sum()}",
        f"- Development rows: {len(X_dev)} | Holdout rows: {len(X_holdout)}",
        f"- Python: {platform.python_version()} | pandas: {pd.__version__} | NumPy: {np.__version__} | scikit-learn: {sklearn.__version__}",
        "- Positive class: `Risk = bad` (1)",
        "- Thresholds are selected using development out-of-fold predictions only.",
        f"- Model selection by development CV PR-AUC: **{metrics['selected_model_by_development_cv_pr_auc']}**",
        "", "## Development 5-fold metrics", "",
        pd.DataFrame(fold_rows).groupby(["model", "metric"])["score"].agg(["mean", "std"]).reset_index().to_markdown(index=False, floatfmt=".4f"),
        "", "## Final holdout comparison", "",
        comparison.to_markdown(index=False, floatfmt=".4f"),
        "", "## Threshold analysis", "",
        pd.DataFrame(threshold_rows).to_markdown(index=False, floatfmt=".4f"),
        "", "## Holdout subgroup diagnostics", "",
        (pd.DataFrame(subgroup_rows).to_markdown(index=False, floatfmt=".4f") if subgroup_rows else "No supported subgroup columns were available."),
        "", "Subgroup figures are descriptive diagnostics only; they do not establish fairness or legal suitability. Small groups may be unstable.",
        "", "## Leakage and reproducibility notes", "",
        "- Imputation, scaling and one-hot encoding are inside each scikit-learn pipeline and refitted within each training fold.",
        "- The holdout set is excluded from threshold selection and model selection.",
        "- Dataset SHA-256, Python/package versions, seed and split/class counts are recorded in the JSON output.",
        "- Manual domain review is still required to rule out semantic/post-outcome leakage in source features.",
        "", "## Limitations", "",
        "The target is the dataset's historical good/bad Risk label. It is not established here as a directly observed future-default event with a defined horizon. This is an educational classification exercise, not a validated production lending model.",
        "", "## Generated evidence", "",
        "- `outputs/final_evaluation_metrics.json`",
        "- `outputs/final_model_comparison.csv`",
        "- `outputs/stratified_5fold_metrics_by_fold.csv`",
        "- `outputs/development_oof_threshold_analysis.csv`",
        "- `outputs/final_holdout_predictions.csv`",
        "- `outputs/holdout_subgroup_metrics.csv`",
        "- Holdout ROC/PR plots and fitted model artifacts in `outputs/`",
    ]
    report_path = report_dir / "Nivesh_Days6-11_Final_Model_Evaluation.md"
    report_path.write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"Evaluation completed. Report: {report_path}")
    print(comparison.to_string(index=False))


if __name__ == "__main__":
    warnings.filterwarnings("ignore", category=FutureWarning)
    main()
