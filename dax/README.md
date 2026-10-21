# DAX Measure Library & Analytical Architecture

Welcome to the **DAX Measure Library** for the Enterprise Power BI Analytics Portfolio. This folder contains all DAX calculation logic, organized by subject domain, extracted from `excel/powerbi-implementation-handbook.xlsx` and calibrated against the 231,130-row relational retail dataset.

---

## Directory Organization

| File | Domain | Measure Count | Key Measures |
|---|---|---|---|
| [`01-core-kpis.dax`](measures/01-core-kpis.dax) | Core Business KPIs | 9 | `[Total Sales]`, `[Total Profit]`, `[Profit Margin]`, `[Total Orders]`, `[Total Customers]`, `[Average Order Value]` |
| [`02-sales.dax`](measures/02-sales.dax) | Sales & Time Intelligence | 10 | `[Sales YTD]`, `[Sales MoM %]`, `[Sales YoY %]`, `[Rolling 3M Sales]`, `[Sales Share %]` |
| [`03-products.dax`](measures/03-products.dax) | Product & Category Performance | 7 | `[Total Products]`, `[Units Sold]`, `[Average Unit Selling Price]`, `[Product Sales Rank]` |
| [`04-customers.dax`](measures/04-customers.dax) | Customer Segmentation & Behavior | 9 | `[Repeat Customer Rate]`, `[Revenue per Customer]`, `[Customer Share %]`, `[Orders per Customer]` |
| [`05-regions.dax`](measures/05-regions.dax) | Geographic & Regional Analytics | 5 | `[Region Sales Share %]`, `[Regional Revenue]`, `[Regional Profit]`, `[Regional Margin %]` |
| [`06-orders.dax`](measures/06-orders.dax) | Logistics & Fulfillment | 9 | `[Delivery Fulfillment %]`, `[Average Delivery Days]`, `[On-Time Delivery %]`, `[Delivered Orders]` |
| [`07-profitability.dax`](measures/07-profitability.dax) | Profit Drivers & Margin Variance | 5 | `[Total Profit]`, `[Profit Margin]`, `[Category Profit Share %]`, `[Profit PY]`, `[Profit YoY %]` |
| [`08-returns.dax`](measures/08-returns.dax) | Return Exposure & Quality Assurance | 10 | `[Return Rate]`, `[Return Value]`, `[Refund Amount]`, `[Average Refund]`, `[Refunded Cases]` |
| [`09-forecast.dax`](measures/09-forecast.dax) | 2024 Planning & Projections | 8 | `[Forecast Sales]`, `[Forecast Orders]`, `[Forecast Profit]`, `[Forecast Margin]`, `[Forecast Return Rate]` |
| [`date-table.dax`](date-table.dax) | Calendar Dimension | Table | 24-month calendar spanning 2023-01-01 to 2024-12-31 with sorting keys |
| [`calculated-columns.dax`](calculated-columns.dax) | Dimension Groupings | Columns | `Order Size Band`, `Price Band`, `Delivery Status`, `Order Month` |

---

## DAX Best Practices Applied

1. **Measures Over Calculated Columns:** All financial metrics and aggregations are evaluated dynamically via explicit measures, allowing VertiPaq memory compression to remain optimal.
2. **Safe Division (`DIVIDE`):** All percentages, margins, and rates use `DIVIDE(Numerator, Denominator, 0)` or `DIVIDE(Numerator, Denominator, BLANK())` to eliminate divide-by-zero errors.
3. **Dedicated Date Dimension:** All time intelligence (`DATEADD`, `DATESYTD`, `DATESINPERIOD`) relies exclusively on the contiguous calendar table `DimDate[Date]`.
4. **Distinct Identifiers:** `DISTINCTCOUNT` is strictly applied across `Order_ID`, `Customer_ID`, and `Product_ID` to preserve integrity and avoid accidental double counting.
5. **Clear Filter Context:** `CALCULATE` is used purposefully with explicit filter arguments (`REMOVEFILTERS`, `ALLSELECTED`, `USERELATIONSHIP`).
6. **Blanks Handling:** Calculations explicitly document conditions where prior-year data is not available in single-year baselines, preventing misleading outputs.

---

## How to Import DAX Measures into Power BI

1. Open **Power BI Desktop**.
2. Create a dedicated measure storage table:
   - On the **Home** tab, click **Enter Data**.
   - Name the table `_Measures` and click **Load**.
3. Open any `.dax` file from this directory.
4. On the **Modeling** tab, click **New Measure**.
5. Paste the measure definition and press **Enter**.
6. Set the data format string as specified in the measure header (e.g., Currency `$#,##0.00`, Percentage `0.0%`).
7. Hide the default blank column `Column1` in `_Measures` to turn the table into a floating measure container with a calculator icon.
