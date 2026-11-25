# Day 4 — EDA Summary

Descriptive analysis only. Risk-rate differences are associations, not causal effects.

## Numeric distributions

|               |   count |    mean |     std |   min |    25% |    50% |     75% |   max |   skewness |
|:--------------|--------:|--------:|--------:|------:|-------:|-------:|--------:|------:|-----------:|
| Age           |    1000 |   35.55 |   11.38 |    19 |   27   |   33   |   42    |    75 |       1.02 |
| Credit amount |    1000 | 3271.26 | 2822.74 |   250 | 1365.5 | 2319.5 | 3972.25 | 18424 |       1.95 |
| Duration      |    1000 |   20.9  |   12.06 |     4 |   12   |   18   |   24    |    72 |       1.09 |

## Potential IQR outlier counts

- Age: 23
- Credit amount: 72
- Duration: 70

## High-risk rates by feature

### Purpose

| Purpose             |   count |   risk_percent |
|:--------------------|--------:|---------------:|
| business            |      97 |          35.05 |
| car                 |     337 |          31.45 |
| domestic appliances |      12 |          33.33 |
| education           |      59 |          38.98 |
| furniture/equipment |     181 |          32.04 |
| radio/TV            |     280 |          22.14 |
| repairs             |      22 |          36.36 |
| vacation/others     |      12 |          41.67 |

### Housing

| Housing   |   count |   risk_percent |
|:----------|--------:|---------------:|
| free      |     108 |          40.74 |
| own       |     713 |          26.09 |
| rent      |     179 |          39.11 |

### Job

|   Job |   count |   risk_percent |
|------:|--------:|---------------:|
|     0 |      22 |          31.82 |
|     1 |     200 |          28    |
|     2 |     630 |          29.52 |
|     3 |     148 |          34.46 |

### Age band

| Age band   |   count |   risk_percent |
|:-----------|--------:|---------------:|
| 19–25      |     190 |          42.11 |
| 26–35      |     398 |          29.65 |
| 36–45      |     226 |          24.34 |
| 46–55      |     115 |          24.35 |
| 56–65      |      53 |          26.42 |
| 66+        |      18 |          27.78 |

### Duration band

| Duration band   |   count |   risk_percent |
|:----------------|--------:|---------------:|
| 1–12            |     359 |          21.17 |
| 13–24           |     411 |          29.68 |
| 25–36           |     143 |          39.86 |
| 37–48           |      71 |          52.11 |
| 49–60           |      15 |          46.67 |
| 61+             |       1 |         100    |

### Credit amount band

| Credit amount band   |   count |   risk_percent |
|:---------------------|--------:|---------------:|
| (1365.5, 2319.5]     |     250 |           24.8 |
| (2319.5, 3972.25]    |     250 |           22.4 |
| (249.999, 1365.5]    |     250 |           30.8 |
| (3972.25, 18424.0]   |     250 |           42   |

