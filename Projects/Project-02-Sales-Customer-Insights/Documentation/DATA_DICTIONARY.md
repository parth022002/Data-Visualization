# Data Dictionary — Sales & Customer Dashboards

## Primary Mart: `clean_sales_orders_complete.csv`
Consolidated and enriched from `Orders.csv`, `Customers.csv`, `Products.csv`, and `Location.csv`.

| Column Name | Data Type | Null Count | Description | Sample Values |
| :--- | :--- | :--- | :--- | :--- |
| `Row ID` | Integer | 0 | Unique row index | `1`, `2`, `3` |
| `Order ID` | String | 0 | Unique customer order identifier | `CA-2022-152156`, `US-2021-108966` |
| `Order Date` | Date (ISO) | 0 | Placement date of order (`YYYY-MM-DD`) | `2022-11-08`, `2021-10-11` |
| `Ship Date` | Date (ISO) | 0 | Order dispatch date (`YYYY-MM-DD`) | `2022-11-11`, `2021-10-18` |
| `Ship Mode` | String | 0 | Shipping service level | `Standard Class`, `Second Class`, `Same Day` |
| `Customer ID` | String | 0 | Unique customer identifier | `CG-12520`, `DV-13045` |
| `Customer Name` | String | 0 | Full legal name of purchasing client | `Claire Gute`, `Darrin Van Huff` |
| `Segment` | String | 0 | Customer market tier | `Consumer`, `Corporate`, `Home Office` |
| `Product ID` | String | 0 | Unique SKU product code | `FUR-BO-10001798`, `OFF-LA-10000240` |
| `Category` | String | 0 | Top-level product category | `Furniture`, `Office Supplies`, `Technology` |
| `Sub-Category` | String | 0 | Granular product classification | `Bookcases`, `Chairs`, `Phones`, `Storage` |
| `Product Name` | String | 0 | Full SKU descriptive title | `Bush Somerset Collection Bookcase` |
| `Sales` | Decimal | 0 | Net gross revenue in USD | `261.96`, `731.94` |
| `Quantity` | Integer | 0 | Number of units purchased | `2`, `3`, `5` |
| `Discount` | Decimal | 0 | Promotional discount applied (0.00 to 0.80) | `0.00`, `0.20`, `0.70` |
| `Profit` | Decimal | 0 | Operating profit contribution in USD | `41.91`, `219.58`, `-12.50` |
| `Postal Code` | String / Int | 0 | ZIP / Postal code | `42420`, `90036` |
| `City` | String | 0 | Customer delivery city | `Henderson`, `Los Angeles`, `Seattle` |
| `State` | String | 0 | Delivery US State | `Kentucky`, `California`, `Washington` |
| `Region` | String | 0 | US Macro sales territory | `South`, `West`, `Central`, `East` |
