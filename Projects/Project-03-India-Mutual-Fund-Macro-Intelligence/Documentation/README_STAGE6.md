# STAGE 6 — FEATURE ENGINEERING (HARDENED V3)

## Purpose

This package completes the project's `06_FEATURE_ENGINEERING` workstream for the Tableau-first India Mutual Fund & Macro-Financial Intelligence project.

Inputs are read from:

`05_MASTER_DATA/tableau/`

Outputs are written additively to:

`06_FEATURE_ENGINEERING/03_FEATURE_OUTPUT/`

Stage 4 source marts are never modified.

## V3 root-cause fix

The failed V2 runtime gate showed:

`no_infinite_feature_values = FAIL` on `monthly_return`.

V3 explicitly handles this class of bad source observation:

- `+inf` / `-inf` / non-numeric monthly returns are treated as invalid observations.
- Invalid returns are converted to NULL before feature calculations.
- `monthly_return_invalid_flag = 1` records the row-level issue.
- Values below -100% are invalid and become NULL.
- Exactly -100% is accepted as a valid monthly return.
- No numeric output may contain `+inf` or `-inf`.

The validator reports the number of non-finite source observations that were sanitized.

## Hardened analytical behavior

- Rolling 3/6/12/24/36M features require consecutive calendar months.
- Missing observations never become zero.
- Missing/invalid return observations break the drawdown wealth path.
- MoM/YoY changes use explicit calendar-aligned prior periods.
- FPI, market and SIP rolling features also respect calendar continuity.
- Multiple market securities are never arbitrarily collapsed into a month-only context.
- Macro month-over-month changes use calendar-aligned prior months.
- Exactly 82 project months (2020-01 through 2026-10) are checked for the fund backbone and monthly context.
- Feature contracts are checked against the feature dictionary.
- Output finite-value checks run on every generated feature mart.
- Feature profile, validation report and SHA-256 manifest are generated.
- No forward-looking targets, leads or future-outcome labels are generated.
- Benchmark excess-return features remain NULL unless explicit benchmark total-return fields exist; no price-index substitution is permitted.

## Feature groups

### Fund

3/6/12/24/36M compounded return, annualised volatility, downside volatility proxy, current drawdown, maximum drawdown to date, 12M hit rate, positive/negative month counts, best/worst month, momentum, return change, history coverage, valid-return coverage, approximate Sharpe/Sortino, explicit benchmark excess-return slots, invalid-return audit flag.

### India macro

Policy-repo change, G-sec 10Y change, USD/INR MoM change, FX stress label, high-inflation label, rate-hike label.

### Global macro

US 10Y change, DXY MoM change, S&P 500 MoM change, high-VIX label.

### Market

3M/12M market return and monthly stress label at the source security grain.

### FPI

MoM/YoY flow changes, 3M rolling net investment and positive-flow label.

### SIP

3M/12M contribution averages and current contribution relative to the 12M average, when explicit contribution data exists.

### Optional preserved marts

Flows, global transmission and debt characteristics are retained when their Stage 4 source marts exist, with finite-value hygiene and source-grain preservation.

## Required outputs

- `03_FEATURE_OUTPUT/feature_fund_monthly.csv`
- `03_FEATURE_OUTPUT/feature_india_macro_monthly.csv`
- `03_FEATURE_OUTPUT/feature_global_macro_monthly.csv`
- `03_FEATURE_OUTPUT/feature_market_monthly.csv`
- `03_FEATURE_OUTPUT/feature_fpi_monthly.csv`
- `03_FEATURE_OUTPUT/feature_monthly_context.csv`

Optional when source marts exist:

- `feature_sip_monthly.csv`
- `feature_flows_monthly.csv`
- `feature_global_transmission_monthly.csv`
- `feature_debt_characteristics_monthly.csv`

## Reports

- `04_FEATURE_VALIDATION/stage6_feature_validation_report.json`
- `04_FEATURE_VALIDATION/stage6_runtime_validation.json`
- `05_FEATURE_REPORT/stage6_plan.json`
- `05_FEATURE_REPORT/stage6_feature_profile.csv`
- `05_FEATURE_REPORT/stage6_manifest.json`

## Run sequence

```powershell
cd C:\Users\parth\OneDrive\Desktop\Datasets\06_FEATURE_ENGINEERING
python -m pip install -r requirements.txt
python .\02_FEATURE_PIPELINE\run_stage6.py --mode plan
python .\02_FEATURE_PIPELINE\run_stage6.py --mode full
python -m pytest -q .\tests
```

## Final PASS gate

The Stage 6 runtime gate is:

`04_FEATURE_VALIDATION\stage6_runtime_validation.json`

It must contain:

```json
"summary": {
  "fail_count": 0,
  "warn_count": 0,
  "status": "PASS"
}
```

The test suite must also report:

`12 passed`

## Readiness for Stage 7

Only after the real-data Stage 6 runtime gate is PASS should the project proceed to:

`07_ANALYSIS`

Stage 6 is a feature layer; it is not the optional ML layer. `09_OPTIONAL_ML` remains outside the mandatory Tableau-first path.
