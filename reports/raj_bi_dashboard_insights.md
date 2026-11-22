# BI Dashboard — Insight Summary

**Owner:** Rishuraj (Raj) — Business Intelligence & Dashboard Lead
**Project:** Credit Risk Scoring and Loan Default Analysis
**Date:** 22 November 2026
**Branch:** `Rishuraj`
**Dashboard source:** `dashboard/credit_risk_dashboard.twbx` (Tableau packaged workbook; opened, edited and saved in Tableau Desktop 2026.3)

## What was delivered

| File | Purpose |
|---|---|
| `dashboard/credit_risk_dashboard.twbx` | Tableau workbook: 3 dashboards, 17 worksheets and 7 click-to-filter actions; the data is packaged inside |
| `dashboard/data/*.csv` | The three data extracts the workbook reads |
| `dashboard/build_dashboard_data.py` | Rebuilds the extracts from the team's own model pipeline |
| `dashboard/build_twb.py` | Generates the starting workbook layout from the extracts (before hand edits in Tableau) |
| `dashboard/README.md` | How to open, use and refresh the dashboard |

Every number on the dashboard comes from code that was actually run on 22 November 2026. Nothing is estimated or typed in by hand.

### Workbook structure

| Dashboard | Charts on it |
|---|---|
| **1. Portfolio Risk Overview** | 4 KPI cards (Applications, Bad-Risk Rate, Avg Credit Amount, Avg Duration); bad-risk rate by purpose, duration band, amount band, checking account and saving accounts; amount vs duration scatter coloured by risk |
| **2. Model Comparison** | Logistic Regression vs Random Forest on 6 metrics (5-fold CV and 20% hold-out), threshold trade-off chart, metrics table |
| **3. Customer Risk** | Customers and actual bad-risk rate by model risk band; customer list sorted by Random Forest risk score |

- After the 3 dashboard tabs, each chart and table also has its own tab, so it can be opened full-screen. The amount vs duration scatter is shown only on dashboard 1; its own tab is hidden.
- **Interactions:** on dashboard 1, clicking a bar filters the other charts (5 actions). On dashboard 3, clicking a risk band filters the customer list (2 actions). Click the same mark again to clear the filter.
- **Calculated fields:** Bad-Risk Rate = `AVG([Bad Flag])`, Applications = `COUNT([Customer ID])`, Avg Credit Amount = `AVG([Credit amount])` and Avg Duration = `AVG([Duration])`.
- **Scatter:** plots `SUM(Duration)` against `SUM(Credit amount)` with `Customer ID` on Detail, so each of the 1,000 dots is one customer's actual values. Its Purpose filter keeps all 8 purposes, so it hides no data.

## 1. Portfolio risk (dashboard 1)

1,000 loans; **30.0% are labelled bad**. The average loan is 3,271 DM, and the average duration is 20.9 months.

| Driver | Lowest-risk group | Highest-risk group |
|---|---|---|
| Loan duration | ≤12 months: 21.2% bad (n=359) | **>36 months: 51.7% bad** (n=87) |
| Credit amount | 2k–5k DM: 26.6% (n=380) | **>10k DM: 60.0%** (n=40) |
| Checking account | not recorded: 11.7% (n=394) | **little: 49.3%** (n=274) |
| Saving accounts | rich: 12.5% (n=48) | little: 36.0% (n=603) |
| Housing | own: 26.1% (n=713) | free: 40.7% (n=108) |
| Purpose | radio/TV: 22.1% (n=280) | education: 39.0% (n=59) |
| Age band | 61+: 22.2% (n=45) | 19–25: 42.1% (n=190) |

- **Duration and amount are the clearest risk gradients.** Bad rate rises steadily with loan length: 21% → 30% → 40% → 52%.
- **Checking-account status is the strongest single split.** A "not recorded" checking account is the *lowest*-risk group (11.7%), so these blanks are informative and should not be imputed as if they were random. The team pipeline already keeps them as an explicit "Missing"/"Unknown" category.
- The purpose groups vacation/others (41.7%) and domestic appliances (33.3%) each have only 12 loans, so their rates are unstable.
- `Sex` is deliberately not charted as a risk driver because it is a protected attribute. Subgroup checks belong in the fairness review.

## 2. Model comparison (dashboard 2)

These are the results of the team's own scripts (`src/validate_baseline.py` and `src/train_baseline.py`, seed 42). Until now, Nivesh's Day 5 table on `main` showed them as "pending execution".

| Metric (bad = positive class) | Logistic Regression, 5-fold CV | Random Forest, 5-fold CV | Logistic Regression, 20% hold-out | Random Forest, 20% hold-out |
|---|---:|---:|---:|---:|
| ROC-AUC | 0.741 | **0.761** | 0.761 | **0.786** |
| PR-AUC | 0.546 | **0.597** | 0.613 | **0.652** |
| Bad precision @0.5 | 0.484 | **0.512** | **0.517** | 0.500 |
| Bad recall @0.5 | **0.713** | 0.663 | **0.750** | 0.683 |
| Bad F1 @0.5 | 0.577 | 0.578 | **0.612** | 0.577 |
| Balanced accuracy @0.5 | 0.694 | 0.696 | **0.725** | 0.695 |

- **Random Forest ranks risk better.** It has the higher ROC-AUC and PR-AUC in both the 5-fold evaluation and the hold-out.
- **Logistic Regression catches more bad loans at the default 0.5 threshold** (recall 71% vs 66% in CV).
- The 5-fold CV figures cover all 1,000 rows, so they are the more reliable comparison. The hold-out has only 200 rows.
- **The threshold sets the trade-off.** For Random Forest, a 0.35 threshold catches 84.7% of bad loans at 42.6% precision. A 0.70 threshold catches only 30.0% of bad loans, at 72.0% precision. The right threshold depends on the relative cost of a missed bad loan versus a wrongly declined good customer, so it is a team and business decision. The threshold chart on the dashboard is diagnostic, not a lending policy.

## 3. Customer risk (dashboard 3)

Each customer has an **out-of-fold Random Forest probability** of being labelled bad, meaning each one was scored by a model that never saw that customer in training.

| Model risk band | Customers | Actually bad | Avg amount | Avg duration |
|---|---:|---:|---:|---:|
| Low (< 0.30) | 339 | 11.5% | 2,486 DM | 17.2 months |
| Medium (0.30–0.50) | 272 | 22.8% | 3,174 DM | 18.1 months |
| High (≥ 0.50) | 389 | **51.2%** | 4,023 DM | 26.2 months |

- The bands separate risk well. A "High" customer is **4.5 times** as likely to be bad as a "Low" one.
- Among the 100 highest-scored customers, 73% are bad. Among the 100 lowest-scored, 11% are.
- The High band contains 199 of the 300 bad loans (66%).
- 94% of High-band customers hold a "little" or "moderate" checking account. Car, furniture/equipment and radio/TV are the most common purposes, largely because those purposes have the most loans overall.
- The dashboard's customer list is sorted from highest score down. Clicking a risk band filters it, so an analyst can review the riskiest applications first.

## Recommendations for the business

1. **Review long and large loans more closely.** Applications over 36 months, or over 10k DM, are labelled bad about half the time or more.
2. **Treat checking-account status as a key screening field.** A "little" balance is the single strongest warning sign in this data.
3. **Use Random Forest risk scores to prioritise manual review, not to automatically decline applicants.** Set the threshold together with the team once the costs of a missed bad loan and a wrongly declined good customer are agreed.
4. **Before any real use, complete the fairness review on age and sex subgroups.** Nivesh's script already outputs the subgroup metrics, and Sirisha's SHAP and fairness work is still pending.

## Limitations

- `Risk` is a historical good/bad label, not an observed future default with a defined time window. The results are exploratory classification, not validated default prediction.
- The dataset has 1,000 rows from the 1990s, with amounts in Deutsche Mark. It has no income or debt-to-income fields.
- The risk-band cut-offs (0.30 and 0.50) were chosen for presentation. They are not calibrated policy thresholds.
- The hold-out metrics come from a single 200-row split and are noisier than the 5-fold CV results.
- The workbook was opened, edited and saved in Tableau Desktop 2026.3. It has not been published to Tableau Server or Tableau Public, so viewers need Tableau Desktop or the free Tableau Public app.

## Reproduce

```bash
pip install -r requirements.txt
python src/train_baseline.py --data german_credit_data.csv
python src/validate_baseline.py --data german_credit_data.csv
python dashboard/build_dashboard_data.py . dashboard/data outputs
```

The commands above rebuild the three data extracts. The committed `credit_risk_dashboard.twbx` is the final dashboard source, because it includes edits made by hand in Tableau Desktop. To refresh it after the extracts change, open the workbook in Tableau. For each data source, use **Data → [data source] → Edit Connection** to point it at the new CSV in `dashboard/data/`, then save again as a packaged workbook (`.twbx`). `dashboard/build_twb.py` regenerates only the original starting layout, not these hand edits.
