# Project Overview — India Mutual Fund Financialization

## Institutional Context
The Indian mutual fund sector has undergone a historic expansion, transitioning from a niche institutional investment vehicle into the primary savings conduit for over 40 million retail households. Understanding the structural determinants of this growth requires evaluating monetary policy, AMC competition, and investor behavioral patterns.

## Architecture & Governance
- **Data Hardening Protocol:** Built under strict semantic accounting contracts (`05_MASTER_DATA_CONTROL_CENTER.md`).
- **Feature Engineering Pipeline:** Explicit handling of non-finite observations, rolling return calendars, and drawdowns (`06_FEATURE_ENGINEERING/README_STAGE6.md`).
- **Tableau Engine:** High-performance dashboarding with dual-axis rate comparisons, parameterized horizon filters, and interactive cross-filtering.
