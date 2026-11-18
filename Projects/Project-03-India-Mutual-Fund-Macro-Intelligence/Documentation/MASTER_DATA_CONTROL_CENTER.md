# Stage 5 — Master Data Control Center — HARDENED_FINAL

Stage 5 is the publication boundary between Stage 4 enrichment/gap closure and Stage 6 features.

## Upstream contract
`05_MASTER_DATA/gap_closure/final_run_state.json` must report `release_gate = PASS` and `semantic_validation = PASS`.

## Downstream contract
`06_FEATURE_ENGINEERING` must consume the Stage 5 published marts only after this release gate is PASS.

## Mandatory semantic checks
- Flow accounting identity: `funds_mobilized_inr_cr - redemption_inr_cr = net_flow_inr_cr` within documented tolerance.
- Large Cap, Large & Mid Cap, Mid Cap and Small Cap flow coverage is at least 48 complete months.
- Debt observations cannot have future dates or duplicate scheme-month keys.
- Historical alpha values are non-null only for full 36-month windows.
- Quarterly AAUM is kept quarterly and is never interpolated to monthly frequency.
- 2026-09 is the historical complete cutoff; 2026-10 is current/partial.

## Important publication rule
A failed semantic check blocks release. Stage 5 never “repairs” economically inconsistent values by overwriting them with zeros, shifted columns, or inferred values.

## Commands
`python .\02_MASTER_DATA_PIPELINE\run_stage5.py --mode plan`
`python .\02_MASTER_DATA_PIPELINE\run_stage5.py --mode test`
`python .\02_MASTER_DATA_PIPELINE\run_stage5.py --mode full`
`python .\02_MASTER_DATA_PIPELINE\run_stage5.py --mode status`
