# Data Dictionary — Regional Retail Performance

## Dataset 1: `clean_sales_region.csv`
| Column Name | Type | Description | Sample Values |
| :--- | :--- | :--- | :--- |
| `Region` | String | Macro sales zone | `North`, `South`, `East`, `West` |
| `Month` | String | Calendar month abbreviation | `Jan`, `Feb`, `Mar`, `Oct` |
| `Product` | String | Product category name | `Laptop`, `Mobile`, `Tablet` |
| `Sales` | Decimal | Gross sales revenue in INR | `16119.0`, `13200.0`, `17982.0` |
| `Profit` | Decimal | Operating net profit in INR | `2003.96`, `2161.31`, `2280.23` |
| `Month_No` | Integer | Chronological month index (1-12) | `1`, `2`, `10`, `12` |

## Dataset 2: `clean_retail_transactions.csv`
| Column Name | Type | Description | Sample Values |
| :--- | :--- | :--- | :--- |
| `Transaction_ID` | Integer | Unique POS transaction code | `1001`, `1002`, `1003` |
| `Date` | Date | POS transaction date | `2024-06-16`, `2024-07-19` |
| `Region` | String | Geographic market | `North`, `West`, `East`, `South` |
| `Product_Category`| String | Assortment classification | `Electronics`, `Groceries`, `Home Décor` |
| `Sales` | Decimal | Transaction gross total (INR) | `1755.0`, `1106.0`, `1709.0` |
| `Quantity` | Integer | Units purchased per basket | `4`, `6`, `2` |
| `Profit` | Decimal | Transaction net profit margin (INR) | `301.38`, `42.43`, `193.81` |
