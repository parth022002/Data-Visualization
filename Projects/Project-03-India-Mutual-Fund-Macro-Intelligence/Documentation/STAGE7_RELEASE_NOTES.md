# Stage 7 — HARDENED_V3_FINAL

## Scope
Question-first analytical implementation for Q1–Q10, downstream of the validated Stage 5 publication layer and Stage 6 feature layer.

## Final analytical contracts
1. Q1 uses observed AMC AAUM as the industry AUM proxy when scheme-level historical AUM is not available, plus T30/B30 distribution and retail proxy evidence. No population-penetration claim.
2. Q2 reports AMC AAUM concentration (HHI, CR3, CR5) and structural product mix by scheme count; product mix is not represented as AUM-weighted without a supporting source.
3. Q3 reports active/passive outcome comparisons, observed classification mix over time, formal non-parametric/parametric comparison tests, and separate source-level TER evidence. Fund-level TER comparison is not claimed without a validated identifier join.
4. Q4 restricts benchmark-relative consistency to eligible active large/mid/small-cap categories and explicit full 36-month matched TRI windows. The result is excess return, not Jensen/CAPM alpha.
5. Q5 compares risk-adjusted outcomes across bull, bear, high-volatility and normal market regimes.
6. Q6 treats debt-fund returns across rising/falling/flat RBI repo-rate regimes as the primary analysis. Duration/YTM remain explicit supplemental disclosures only.
7. Q7 reports Large Cap, Large & Mid Cap, Mid Cap and Small Cap flow momentum plus market-regime context.
8. Q8 separates debt from equity/hybrid flows and reports lagged Pearson/Spearman associations plus HAC regressions against domestic rate, inflation and FX drivers.
9. Q9 evaluates FPI, large-cap fund returns and NIFTY 50 against transformed global shock variables with lags, multiple-testing adjustment and HAC regressions. This remains association analysis, not causal identification.
10. Q10 reports SIP contribution, contribution persistence/stickiness proxy, stress-vs-normal context and gross-redemption/AUM proxy. Redemption is not investor churn.

## Common time policy
- Historical analytical cutoff: 2026-09
- 2026-10 is current/partial and excluded from historical statistics by default.

## Release gates
- Stage 5 release gate = PASS
- Stage 6 runtime validation = PASS
- Stage 6 input hashes must still match the current Stage 5 marts
- Stage 7 technical validation = PASS
- Q1–Q10 technical status = READY
- Evidence coverage is reported separately and is never fabricated.
