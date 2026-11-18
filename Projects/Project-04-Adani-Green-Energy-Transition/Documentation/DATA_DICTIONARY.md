# Data Dictionary — Adani Green Energy (AGEL) Transition

## Dataset: `clean_agel_master_timeseries.csv`
Derived from `AGEL_Master_OneSheet.xlsx`.

| Column Name | Data Type | Null Count | Description | Example Values |
| :--- | :--- | :--- | :--- | :--- |
| `Year` | Integer | 0 | Observation year (2016 to 2030) | `2016`, `2024`, `2030` |
| `State` | String | 0 | Indian state or geographic region | `Rajasthan`, `Gujarat`, `Tamil Nadu` |
| `State Installed Capacity (MW)` | Decimal | 0 | Operational MW deployed in the specific state | `135.0`, `112.0`, `2500.0` |
| `Total Operational Capacity (MW)` | Decimal | 0 | Consolidated national operational capacity | `369.0`, `8310.0`, `45000.0` |
| `Total Potential Capacity (MW)` | Decimal | 0 | Estimated theoretical clean potential in MW | `142000.0`, `248000.0` |
| `Renewable Potential (MW)` | Decimal | 0 | Estimated state renewable potential | `6155.0`, `5197.0` |
| `NonRenewable Potential (MW)` | Decimal | 0 | State non-renewable fossil reserve benchmark | `450.0`, `320.0` |
| `Capacity Gap (MW)` | Decimal | 0 | Untapped potential (`Total Potential - Installed`) | `5800.0`, `4200.0` |
| `Generation_MU` | Decimal | 0 | Electricity output in Million Units (kWh * 10^6) | `640.0`, `14800.0`, `85000.0` |
| `Solar Capacity (MW)` | Decimal | 0 | Operating solar PV capacity | `250.0`, `5200.0` |
| `Wind Capacity (MW)` | Decimal | 0 | Operating wind turbine capacity | `119.0`, `1400.0` |
| `Hybrid Capacity (MW)` | Decimal | 0 | Combined wind-solar hybrid capacity | `0.0`, `2140.0` |
| `Revenue (Cr)` | Decimal | 0 | Power supply revenue in INR Crores | `520.0`, `7735.0`, `24500.0` |
| `CO2 Avoided (MT)` | Decimal | 0 | Avoided carbon emissions in Million Tonnes | `0.85`, `14.20`, `75.00` |
| `Is_Historical` | Integer (0/1) | 0 | Historical flag (1 = 2016-2024, 0 = Forecast) | `1`, `0` |
| `Is_Forecast` | Integer (0/1) | 0 | Future forecast flag (1 = 2025-2030, 0 = Historical) | `0`, `1` |
