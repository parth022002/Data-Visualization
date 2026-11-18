# Data Dictionary — India Mutual Fund & Macro Intelligence

## Data Marts Overview

### Mart 1: AMC AAUM & Industry Concentration (`clean_amc_average_aum.csv`)
| Field Name | Type | Description | Sample Values |
| :--- | :--- | :--- | :--- |
| `Period` | String / Date | Financial quarter or month | `2023-Q4`, `2024-Q1` |
| `AMC_Name` | String | Asset Management Company legal entity | `HDFC Asset Management Company`, `SBI Funds Management` |
| `Average_AUM_INR_Cr` | Decimal | Average Assets Under Management (Crores) | `452310.50`, `684200.12` |
| `Market_Share_Pct` | Decimal | Percentage share of total industry AAUM | `12.45`, `8.90` |
| `Quartile_Rank` | Integer | Industry ranking based on AUM | `1`, `2`, `5`, `10` |

### Mart 2: Macroeconomic & Debt Indicators (`DS04_DEBT_RATES` / `DS05_FLOWS_MACRO`)
| Field Name | Type | Description | Sample Values |
| :--- | :--- | :--- | :--- |
| `Month_Date` | Date | Month timestamp (`YYYY-MM-01`) | `2022-01-01`, `2023-06-01` |
| `RBI_Repo_Rate` | Decimal | Central bank benchmark policy rate (%) | `4.00`, `4.90`, `6.50` |
| `GSec_10Y_Yield` | Decimal | 10-Year Indian Government Sovereign Bond yield (%) | `6.85`, `7.20`, `7.45` |
| `TBill_91D_Yield` | Decimal | 91-Day Treasury Bill yield (%) | `3.75`, `6.80` |
| `Mutual_Fund_Net_Flow_Cr` | Decimal | Total net capital inflows into mutual funds (INR Cr) | `15420.00`, `-2340.50` |
| `FPI_Net_Investment_Cr` | Decimal | Net Foreign Portfolio Investor equity investment (INR Cr) | `-12300.00`, `24500.00` |
| `SIP_Inflow_INR_Cr` | Decimal | Total retail monthly SIP contribution volume | `8532.00`, `14276.00`, `21500.00` |
