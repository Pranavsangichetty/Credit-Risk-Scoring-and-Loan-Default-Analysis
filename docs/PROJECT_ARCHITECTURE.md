# Project Architecture and Workflow

## Project purpose

Analyze the German Credit dataset to understand the supplied historical good/bad credit-risk labels, prepare relevant customer attributes, develop baseline classification models, and communicate model behaviour responsibly.

> The target is a historical credit-risk category. It is not a directly observed future default event with a defined horizon.

## End-to-end workflow

```text
German Credit dataset
        |
        v
Data understanding and quality checks
        |
        v
Cleaning and preprocessing
        |
        +----------------------------+
        |                            |
        v                            v
Exploratory / statistical analysis  Feature engineering
        |                            |
        +-------------+--------------+
                      |
                      v
             Model-ready dataset
                      |
                      v
        Logistic Regression / Random Forest
                      |
                      v
         Stratified validation and comparison
                      |
                      v
        Explainability and fairness diagnostics
                      |
                      v
          Dashboard, report and conclusions
```

## Canonical project areas

| Area | Intended contents |
|---|---|
| Dataset | Supplied dataset and documented data dictionary |
| Notebooks | Exploratory analysis, statistical analysis and feature engineering |
| `src/` | Reusable preprocessing, training and validation scripts |
| `reports/` | Model reports, daily project-lead trackers and verified findings |
| `docs/` | Architecture, integration rules and execution guidance |
| Dashboard | Approved BI deliverable and its source mapping |

Existing files may remain in their current paths until a deliberate move is reviewed. Do not create duplicate copies simply to match this suggested layout.

## Integration contracts

1. Use one documented source dataset and preserve the target definition.
2. Keep the exported row index out of predictive features.
3. Fit imputation and encoding within training folds to prevent leakage.
4. Use stratified splitting and stratified cross-validation for the current classification task.
5. Keep model outputs and metrics traceable to the code, dataset version and run configuration.
6. Treat Age and Sex analyses as fairness diagnostics requiring careful interpretation.
7. Do not present this educational model as a production lending decision system.

## Status

This document describes the intended workflow and repository organization. It does not claim that every module has been completed or independently rerun.
