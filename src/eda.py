from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "interim" / "german_credit_cleaned.csv"
FIG_DIR = ROOT / "reports" / "figures"
REPORT_PATH = ROOT / "reports" / "day4_eda_summary.md"

FIG_DIR.mkdir(parents=True, exist_ok=True)
df = pd.read_csv(DATA_PATH)

# Use the verified target labels; bad = high-risk class for descriptive rates.
df["high_risk"] = (df["Risk"] == "bad").astype(int)

def save_bar(series, title, filename, xlabel="", ylabel="Count", rotate=0):
    ax = series.plot(kind="bar", figsize=(9, 5))
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.tick_params(axis="x", labelrotation=rotate)
    plt.tight_layout()
    plt.savefig(FIG_DIR / filename, dpi=150)
    plt.close()

def save_risk_rate(group_col, title, filename, rotate=0):
    summary = df.groupby(group_col, dropna=False)["high_risk"].agg(["mean", "count"])
    summary["risk_percent"] = summary["mean"] * 100
    ax = summary["risk_percent"].plot(kind="bar", figsize=(9, 5))
    ax.set_title(title)
    ax.set_xlabel(group_col)
    ax.set_ylabel("High-risk (`bad`) cases (%)")
    ax.tick_params(axis="x", labelrotation=rotate)
    plt.tight_layout()
    plt.savefig(FIG_DIR / filename, dpi=150)
    plt.close()
    return summary[["count", "risk_percent"]].round(2)

# Target and categorical distributions
save_bar(df["Risk"].value_counts(), "Risk class distribution", "risk_distribution.png")
for col in ["Purpose", "Housing", "Job", "Sex"]:
    save_bar(
        df[col].value_counts().sort_index(),
        f"{col} distribution",
        f"{col.lower().replace(' ', '_')}_distribution.png",
        xlabel=col,
        rotate=30,
    )

# Numeric distributions and skewness
numeric_cols = ["Age", "Credit amount", "Duration"]
for col in numeric_cols:
    ax = df[col].plot(kind="hist", bins=25, figsize=(8, 5), edgecolor="black")
    ax.set_title(f"{col} distribution")
    ax.set_xlabel(col)
    ax.set_ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(FIG_DIR / f"{col.lower().replace(' ', '_')}_histogram.png", dpi=150)
    plt.close()

# Use descriptive bands for readable risk-rate charts.
df["Age band"] = pd.cut(
    df["Age"], bins=[18, 25, 35, 45, 55, 65, 100],
    labels=["19–25", "26–35", "36–45", "46–55", "56–65", "66+"],
)
df["Duration band"] = pd.cut(
    df["Duration"], bins=[0, 12, 24, 36, 48, 60, 100],
    labels=["1–12", "13–24", "25–36", "37–48", "49–60", "61+"],
)
df["Credit amount band"] = pd.qcut(
    df["Credit amount"], q=4, duplicates="drop"
).astype(str)

risk_tables = {}
for col in ["Purpose", "Housing", "Job", "Age band", "Duration band", "Credit amount band"]:
    table = save_risk_rate(
        col,
        f"High-risk rate by {col}",
        f"risk_by_{col.lower().replace(' ', '_')}.png",
        rotate=30,
    )
    risk_tables[col] = table

# Numeric summary, skewness and IQR-based potential outlier counts.
numeric_summary = df[numeric_cols].describe().T
numeric_summary["skewness"] = df[numeric_cols].skew()
outlier_counts = {}
for col in numeric_cols:
    q1, q3 = df[col].quantile([0.25, 0.75])
    iqr = q3 - q1
    outlier_counts[col] = int(((df[col] < q1 - 1.5 * iqr) |
                               (df[col] > q3 + 1.5 * iqr)).sum())

with REPORT_PATH.open("w") as f:
    f.write("# Day 4 — EDA Summary\n\n")
    f.write("Descriptive analysis only. Risk-rate differences are associations, not causal effects.\n\n")
    f.write("## Numeric distributions\n\n")
    f.write(numeric_summary.round(2).to_markdown())
    f.write("\n\n## Potential IQR outlier counts\n\n")
    for col, count in outlier_counts.items():
        f.write(f"- {col}: {count}\n")
    f.write("\n## High-risk rates by feature\n\n")
    for col, table in risk_tables.items():
        f.write(f"### {col}\n\n")
        f.write(table.to_markdown())
        f.write("\n\n")

print("Saved EDA figures to:", FIG_DIR)
print("Saved EDA summary to:", REPORT_PATH)
print("\nNumeric summary:")
print(numeric_summary.round(2).to_string())
print("\nPotential IQR outlier counts:", outlier_counts)
