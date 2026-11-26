#!/usr/bin/env python3
"""Reproducible Logistic Regression / Random Forest evaluation.

Run from the project root:
  python src/run_final_evaluation.py --data german_credit_data.csv

Protocol:
- 80/20 stratified hold-out split (test set untouched during model/threshold selection)
- Stratified 5-fold CV on the 80% development partition
- Out-of-fold development probabilities for threshold selection
- Final refit on the complete development partition; one final hold-out evaluation
- All imputing, scaling and encoding live inside sklearn Pipelines, so each fold fits
  preprocessing only on its own training partition.

Positive class: Risk == 'bad' (1). Scores are historical-label classification metrics.
"""
from __future__ import annotations
import argparse, json, warnings
from pathlib import Path
import joblib
import matplotlib
matplotlib.use('Agg')
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
    confusion_matrix, f1_score, precision_score, recall_score,
    roc_auc_score, RocCurveDisplay, PrecisionRecallDisplay
)
from sklearn.model_selection import StratifiedKFold, cross_val_predict, cross_validate, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

ROOT = Path(__file__).resolve().parents[1]
RANDOM_STATE = 42
THRESHOLDS = np.round(np.arange(0.10, 0.901, 0.05), 2).tolist()
TARGET = 'Risk'


def load_data(path: Path):
    if not path.exists():
        raise FileNotFoundError(f'Dataset not found: {path}. Place german_credit_data.csv in the repository root.')
    df = pd.read_csv(path)
    df.columns = [str(c).strip() for c in df.columns]
    dropped = [c for c in df.columns if c.lower().startswith('unnamed:') or c.lower() in {'index', 'row_id'}]
    if dropped:
        df = df.drop(columns=dropped)
    if TARGET not in df.columns:
        raise ValueError(f"Expected target column '{TARGET}'. Found: {df.columns.tolist()}")
    df = df.dropna(subset=[TARGET]).copy()
    labels = df[TARGET].astype(str).str.strip().str.lower()
    unexpected = sorted(set(labels) - {'good', 'bad'})
    if unexpected:
        raise ValueError(f'Unexpected target values {unexpected}; expected good/bad.')
    y = labels.map({'good': 0, 'bad': 1}).astype(int)
    X = df.drop(columns=[TARGET]).copy()
    if X.empty or y.nunique() != 2 or y.value_counts().min() < 5:
        raise ValueError('Need predictors and both classes with at least five records per class.')
    return df, X, y, dropped


def build_pipeline(X, estimator):
    numeric = X.select_dtypes(include=['number']).columns.tolist()
    categorical = [c for c in X.columns if c not in numeric]
    transformers = []
    if numeric:
        num_pipe = Pipeline([('imputer', SimpleImputer(strategy='median')),
                             ('scaler', StandardScaler())])
        transformers.append(('numeric', num_pipe, numeric))
    if categorical:
        cat_pipe = Pipeline([('imputer', SimpleImputer(strategy='constant', fill_value='Unknown')),
                             ('onehot', OneHotEncoder(handle_unknown='ignore'))])
        transformers.append(('categorical', cat_pipe, categorical))
    prep = ColumnTransformer(transformers, remainder='drop')
    return Pipeline([('preprocess', prep), ('model', estimator)])


def metrics_at_threshold(y, p, threshold):
    pred = (np.asarray(p) >= threshold).astype(int)
    cm = confusion_matrix(y, pred, labels=[0, 1])
    return {
        'threshold': float(threshold),
        'accuracy': float(accuracy_score(y, pred)),
        'balanced_accuracy': float(balanced_accuracy_score(y, pred)),
        'bad_precision': float(precision_score(y, pred, zero_division=0)),
        'bad_recall': float(recall_score(y, pred, zero_division=0)),
        'bad_f1': float(f1_score(y, pred, zero_division=0)),
        'tn': int(cm[0, 0]), 'fp': int(cm[0, 1]),
        'fn': int(cm[1, 0]), 'tp': int(cm[1, 1]),
        'predicted_bad': int(pred.sum())
    }


def threshold_table(y, p, model_name):
    rows = []
    for t in THRESHOLDS:
        rows.append({'model': model_name, **metrics_at_threshold(y, p, t)})
    return rows


def subgroup_metrics(test_df, y, p, threshold, model_name):
    pred = (np.asarray(p) >= threshold).astype(int)
    rows = []
    groups = {}
    if 'Sex' in test_df.columns:
        groups['Sex'] = test_df['Sex'].fillna('Unknown').astype(str)
    if 'Age' in test_df.columns:
        age = pd.to_numeric(test_df['Age'], errors='coerce')
        groups['Age band'] = pd.cut(age, [0, 25, 35, 50, np.inf],
            labels=['18-25', '26-35', '36-50', '51+'], include_lowest=True).astype('object').fillna('Unknown')
    for attr, values in groups.items():
        tmp = pd.DataFrame({'group': values.to_numpy(), 'actual': np.asarray(y), 'pred': pred})
        for group, part in tmp.groupby('group', dropna=False):
            rows.append({
                'model': model_name, 'attribute': attr, 'group': str(group), 'n': int(len(part)),
                'actual_bad': int(part.actual.sum()), 'predicted_bad': int(part.pred.sum()),
                'bad_precision': float(precision_score(part.actual, part.pred, zero_division=0)),
                'bad_recall': float(recall_score(part.actual, part.pred, zero_division=0)),
                'bad_f1': float(f1_score(part.actual, part.pred, zero_division=0)),
                'note': 'Small subgroup (n<10); interpret cautiously.' if len(part) < 10 else ''
            })
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', default='german_credit_data.csv')
    parser.add_argument('--output', default='outputs')
    parser.add_argument('--reports', default='reports')
    args = parser.parse_args()
    data_path = Path(args.data)
    if not data_path.is_absolute(): data_path = ROOT / data_path
    out = Path(args.output); out = out if out.is_absolute() else ROOT / out
    reports = Path(args.reports); reports = reports if reports.is_absolute() else ROOT / reports
    out.mkdir(parents=True, exist_ok=True); reports.mkdir(parents=True, exist_ok=True)

    df, X, y, dropped = load_data(data_path)
    X_dev, X_test, y_dev, y_test = train_test_split(
        X, y, test_size=0.20, random_state=RANDOM_STATE, stratify=y
    )
    dev_df = df.loc[X_dev.index].copy()
    test_df = df.loc[X_test.index].copy()
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
    models = {
        'Logistic Regression': LogisticRegression(max_iter=3000, class_weight='balanced', random_state=RANDOM_STATE),
        'Random Forest': RandomForestClassifier(n_estimators=500, min_samples_leaf=3,
            class_weight='balanced', random_state=RANDOM_STATE, n_jobs=-1)
    }

    result = {
        'project': 'Credit Risk Scoring and Loan Default Analysis',
        'contributor': 'Nivesh — ML / Model Development', 'dataset': data_path.name,
        'dataset_rows': int(len(df)), 'feature_count': int(X.shape[1]), 'features': X.columns.tolist(),
        'class_counts': {'good_0': int((y == 0).sum()), 'bad_1': int((y == 1).sum())},
        'development_rows': int(len(X_dev)), 'holdout_rows': int(len(X_test)),
        'development_class_counts': {'good_0': int((y_dev == 0).sum()), 'bad_1': int((y_dev == 1).sum())},
        'holdout_class_counts': {'good_0': int((y_test == 0).sum()), 'bad_1': int((y_test == 1).sum())},
        'protocol': 'Stratified 80/20 hold-out; stratified 5-fold CV on development data; threshold selected from development OOF only.',
        'positive_class': 'bad (1)', 'random_state': RANDOM_STATE,
        'versions': {'python_note': 'Record Python version in execution log', 'pandas': pd.__version__, 'scikit_learn': sklearn.__version__},
        'leakage_audit': {
            'target_removed_from_predictors': TARGET not in X.columns,
            'index_columns_removed': dropped,
            'preprocessing_inside_pipeline': True,
            'cv_preprocessing_refit_per_fold': True,
            'holdout_used_for_threshold_selection': False,
            'holdout_used_for_model_selection': False,
            'remaining_manual_review': 'Review source provenance and feature definitions for any business-level post-outcome fields; code-level pipeline isolation cannot rule out semantic leakage in raw columns.'
        },
        'models': {}
    }
    comparison, cv_rows, thresholds, subgroup_rows, holdout_rows = [], [], [], [], []
    roc_fig, roc_ax = plt.subplots(figsize=(7, 6)); pr_fig, pr_ax = plt.subplots(figsize=(7, 6))

    for name, estimator in models.items():
        pipe = build_pipeline(X_dev, estimator)
        # CV score arrays are fold-level generalization estimates on development partition.
        cv_scores = cross_validate(pipe, X_dev, y_dev, cv=cv,
            scoring={'roc_auc': 'roc_auc', 'pr_auc': 'average_precision',
                     'balanced_accuracy': 'balanced_accuracy', 'f1_bad': 'f1'},
            return_train_score=False, n_jobs=None)
        # Each development row gets a probability from a model that did not train on it.
        oof_prob = cross_val_predict(pipe, X_dev, y_dev, cv=cv, method='predict_proba')[:, 1]
        oof_auc = float(roc_auc_score(y_dev, oof_prob))
        oof_ap = float(average_precision_score(y_dev, oof_prob))
        t_rows = threshold_table(y_dev, oof_prob, name)
        thresholds.extend(t_rows)
        # Maximise OOF F1; tie-break toward higher recall, then higher threshold.
        best = sorted(t_rows, key=lambda r: (r['bad_f1'], r['bad_recall'], r['threshold']), reverse=True)[0]
        selected_t = float(best['threshold'])

        fitted = build_pipeline(X_dev, estimator)
        fitted.fit(X_dev, y_dev)
        holdout_prob = fitted.predict_proba(X_test)[:, 1]
        holdout_default = metrics_at_threshold(y_test, holdout_prob, 0.50)
        holdout_selected = metrics_at_threshold(y_test, holdout_prob, selected_t)
        holdout_auc = float(roc_auc_score(y_test, holdout_prob))
        holdout_ap = float(average_precision_score(y_test, holdout_prob))

        cv_summary = {}
        for metric in ['test_roc_auc', 'test_pr_auc', 'test_balanced_accuracy', 'test_f1_bad']:
            vals = cv_scores[metric]
            cv_summary[metric.replace('test_', '')] = {'mean': float(np.mean(vals)), 'std': float(np.std(vals, ddof=1))}
            for fold, val in enumerate(vals, 1): cv_rows.append({'model': name, 'fold': fold, 'metric': metric.replace('test_', ''), 'score': float(val)})

        groups = subgroup_metrics(test_df, y_test, holdout_prob, selected_t, name)
        subgroup_rows.extend(groups)
        model_res = {
            'cv_fold_metrics': cv_summary,
            'development_oof': {'roc_auc': oof_auc, 'pr_auc_average_precision': oof_ap,
                                'metrics_at_0_50': metrics_at_threshold(y_dev, oof_prob, 0.50)},
            'threshold_selection': {'method': 'Maximum bad-class F1 on development out-of-fold probabilities; tie-break recall then higher threshold.',
                                    'selected_threshold': selected_t, 'development_oof_metrics_at_selected_threshold': best},
            'holdout': {'roc_auc': holdout_auc, 'pr_auc_average_precision': holdout_ap,
                        'metrics_at_0_50': holdout_default, 'metrics_at_selected_threshold': holdout_selected}
        }
        result['models'][name] = model_res
        comparison.append({
            'model': name, 'cv_roc_auc_mean': cv_summary['roc_auc']['mean'], 'cv_roc_auc_std': cv_summary['roc_auc']['std'],
            'cv_pr_auc_mean': cv_summary['pr_auc']['mean'], 'cv_pr_auc_std': cv_summary['pr_auc']['std'],
            'holdout_roc_auc': holdout_auc, 'holdout_pr_auc': holdout_ap,
            'holdout_bad_precision_at_0_50': holdout_default['bad_precision'],
            'holdout_bad_recall_at_0_50': holdout_default['bad_recall'],
            'holdout_bad_f1_at_0_50': holdout_default['bad_f1'],
            'selected_threshold_from_dev_oof': selected_t,
            'holdout_bad_precision_at_selected_threshold': holdout_selected['bad_precision'],
            'holdout_bad_recall_at_selected_threshold': holdout_selected['bad_recall'],
            'holdout_bad_f1_at_selected_threshold': holdout_selected['bad_f1']
        })
        for idx, (actual, prob) in enumerate(zip(y_test.to_numpy(), holdout_prob)):
            holdout_rows.append({'row_index': int(X_test.index[idx]), 'model': name,
                'actual_bad_1': int(actual), 'probability_bad': float(prob),
                'predicted_bad_at_0_50': int(prob >= 0.50),
                'predicted_bad_at_selected_threshold': int(prob >= selected_t)})
        RocCurveDisplay.from_predictions(y_test, holdout_prob, name=name, ax=roc_ax)
        PrecisionRecallDisplay.from_predictions(y_test, holdout_prob, name=name, ax=pr_ax)
        joblib.dump(fitted, out / (name.lower().replace(' ', '_') + '.joblib'))
        # Save per-model confusion matrices at the selected development threshold.
        cm = confusion_matrix(y_test, (holdout_prob >= selected_t).astype(int), labels=[0, 1])
        fig, ax = plt.subplots(figsize=(5, 4)); im = ax.imshow(cm)
        ax.set(title=f'{name} — Hold-out confusion matrix', xlabel='Predicted class', ylabel='Actual class',
               xticks=[0, 1], yticks=[0, 1]); ax.set_xticklabels(['Good (0)', 'Bad (1)']); ax.set_yticklabels(['Good (0)', 'Bad (1)'])
        for (i, j), value in np.ndenumerate(cm): ax.text(j, i, str(value), ha='center', va='center')
        fig.tight_layout(); fig.savefig(out / (name.lower().replace(' ', '_') + '_holdout_confusion_matrix.png'), dpi=160); plt.close(fig)

    comp = pd.DataFrame(comparison).sort_values('holdout_pr_auc', ascending=False)
    comp.to_csv(out / 'final_model_comparison.csv', index=False)
    pd.DataFrame(cv_rows).to_csv(out / 'stratified_5fold_metrics_by_fold.csv', index=False)
    pd.DataFrame(thresholds).to_csv(out / 'development_oof_threshold_analysis.csv', index=False)
    pd.DataFrame(subgroup_rows).to_csv(out / 'holdout_subgroup_metrics.csv', index=False)
    pd.DataFrame(holdout_rows).to_csv(out / 'holdout_predictions.csv', index=False)
    (out / 'final_evaluation_metrics.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    roc_ax.plot([0, 1], [0, 1], '--', linewidth=1); roc_ax.set_title('Hold-out ROC curves'); roc_fig.tight_layout(); roc_fig.savefig(out / 'holdout_roc_curves.png', dpi=160); plt.close(roc_fig)
    pr_ax.set_title('Hold-out Precision–Recall curves'); pr_fig.tight_layout(); pr_fig.savefig(out / 'holdout_precision_recall_curves.png', dpi=160); plt.close(pr_fig)

    report = [
        '# Nivesh — Days 6–11 Final ML Evaluation Report', '',
        '**Project:** Credit Risk Scoring and Loan Default Analysis  ',
        '**Contributor:** Nivesh — ML / Model Development  ',
        f'**Dataset:** `{data_path.name}`  ',
        f'**Rows:** {len(df)} | **Features:** {X.shape[1]} | **Good:** {(y==0).sum()} | **Bad:** {(y==1).sum()}  ',
        '**Positive class:** `Risk = bad` (1)  ',
        '**Protocol:** Stratified 80/20 hold-out; stratified 5-fold CV on development data; threshold selected using development OOF predictions only.', '',
        '## Final model comparison (hold-out)', '', comp.to_markdown(index=False, floatfmt='.4f'), '',
        '## Stratified 5-fold CV (fold-level metrics)', '',
        pd.DataFrame(cv_rows).groupby(['model','metric'])['score'].agg(['mean','std']).reset_index().to_markdown(index=False, floatfmt='.4f'), '',
        '## Threshold selection', '',
        'The selected threshold maximises bad-class F1 on development-set out-of-fold probabilities. The hold-out set is not used to select the threshold.', '',
        pd.DataFrame([{'model': n, 'selected_threshold': v['threshold_selection']['selected_threshold'],
          'dev_oof_precision': v['threshold_selection']['development_oof_metrics_at_selected_threshold']['bad_precision'],
          'dev_oof_recall': v['threshold_selection']['development_oof_metrics_at_selected_threshold']['bad_recall'],
          'dev_oof_f1': v['threshold_selection']['development_oof_metrics_at_selected_threshold']['bad_f1'],
          'holdout_precision': v['holdout']['metrics_at_selected_threshold']['bad_precision'],
          'holdout_recall': v['holdout']['metrics_at_selected_threshold']['bad_recall'],
          'holdout_f1': v['holdout']['metrics_at_selected_threshold']['bad_f1']}
          for n,v in result['models'].items()]).to_markdown(index=False, floatfmt='.4f'), '',
        '## Leakage and reproducibility audit', '',
        '- Target column is excluded from predictors.',
        '- Index-like export columns are removed before modelling.',
        '- Imputation, scaling and one-hot encoding are inside the model Pipeline.',
        '- Each CV fold refits preprocessing using only its training fold.',
        '- The final hold-out split is stratified and is not used for threshold selection.',
        '- Random state is fixed at 42; fold metrics and predictions are exported.',
        '- Manual source-level review is still required to rule out semantic/post-outcome leakage in raw feature definitions.', '',
        '## Subgroup analysis', '',
        (pd.DataFrame(subgroup_rows).to_markdown(index=False, floatfmt='.4f') if subgroup_rows else 'No supported subgroup columns found.'), '',
        'Subgroup metrics are descriptive and do not establish fairness, legal suitability, or permission to use protected attributes in lending decisions. Small groups are unstable.', '',
        '## Limitations', '',
        'The dataset target is a historical good/bad Risk label. Unless the dataset documentation establishes an observed future-default outcome and a defined observation horizon, interpret this as historical credit-risk classification—not verified future-default prediction. Metrics are educational research results and are not a production lending approval rule. Threshold choice requires business-cost, calibration, policy, fairness and legal review.', '',
        '## Artifacts', '',
        '- `outputs/final_evaluation_metrics.json`', '- `outputs/final_model_comparison.csv`',
        '- `outputs/stratified_5fold_metrics_by_fold.csv`', '- `outputs/development_oof_threshold_analysis.csv`',
        '- `outputs/holdout_predictions.csv`', '- `outputs/holdout_subgroup_metrics.csv`',
        '- `outputs/holdout_roc_curves.png`', '- `outputs/holdout_precision_recall_curves.png`',
        '- Per-model joblib estimators and hold-out confusion matrices.', ''
    ]
    (reports / 'Nivesh_Days6-11_Final_Model_Evaluation.md').write_text('\n'.join(report), encoding='utf-8')
    print('Evaluation completed. Results are in:', out)
    print(comp.to_string(index=False))

if __name__ == '__main__':
    warnings.filterwarnings('ignore', category=FutureWarning)
    main()
