# Getting Started & Reproducible Build Guide

Welcome to the **Enterprise Power BI Analytics Portfolio** build guide. This document provides an end-to-end walkthrough for data analysts, BI developers, and engineers seeking to reproduce the multi-page analytics report using the provided datasets, DAX measures, and design specifications.

---

## Prerequisites & Environment

| Component | Minimum Requirement | Recommended | Purpose |
|---|---|---|---|
| **Power BI Desktop** | 2.120+ (2023 or newer) | Latest Release (64-bit) | Report modeling & visual layout |
| **Operating System** | Windows 10 / 11 | Windows 11 (64-bit) | Power BI Desktop execution |
| **Python** | 3.10+ | 3.11 / 3.12 / 3.14 | Automated validation & test execution |
| **Git** | 2.30+ | Latest | Version control & repository cloning |
| **RAM** | 8 GB | 16 GB+ | VertiPaq tabular memory buffer |

---

## Step-by-Step Implementation Roadmap (Steps 1 to 24)

### Step 1: Install Power BI Desktop
Download and install the official Microsoft Power BI Desktop application from the Microsoft Store or [Microsoft Power BI Download Portal](https://powerbi.microsoft.com/desktop/).

### Step 2: Clone or Download the Repository
```bash
git clone https://github.com/sabledattatray/enterprise-power-bi-dashboard.git
cd enterprise-power-bi-dashboard
```

### Step 3: Inspect Data Assets
Review `data/raw/` containing the five relational CSV files:
- `fact_orders_2023.csv` (178,200 rows)
- `dim_customers.csv` (46,798 rows)
- `dim_products.csv` (320 rows)
- `fact_returns_2023.csv` (5,800 rows)
- `fact_forecast_2024.csv` (12 rows)

### Step 4: Import CSV Files into Power BI Desktop
1. Open Power BI Desktop.
2. Click **Get Data > Text/CSV**.
3. Select each CSV from `data/raw/` and click **Transform Data** to open the Power Query Editor.

### Step 5: Power Query Transformations & Type Casting
Follow [`docs/power-query-guide.md`](power-query-guide.md) to set standard data types:
- Set `Order_ID`, `Customer_ID`, `Product_ID`, and `Return_ID` to **Text**.
- Set currency columns (`Sales_Amount_USD`, `Cost_Amount_USD`, `Profit_Amount_USD`, etc.) to **Fixed Decimal Number**.
- Set date columns (`Order_Date`, `Delivery_Date`, `Return_Date`, `Forecast_Month`) to **Date**.
- Click **Close & Apply**.

### Step 6: Validate Imported Row Counts
Confirm the table record counts in the Data View:
- `fact_orders_2023`: 178,200 rows
- `dim_customers`: 46,798 rows
- `dim_products`: 320 rows
- `fact_returns_2023`: 5,800 rows
- `fact_forecast_2024`: 12 rows

### Step 7: Create the Date Dimension
1. Go to **Modeling > New Table**.
2. Paste the DAX expression from [`dax/date-table.dax`](../dax/date-table.dax).
3. Right-click `DimDate` > **Mark as date table**, choosing `DimDate[Date]`.
4. Sort `Month` by `Month No` and `Year Month` by `Year Month Sort`.

### Step 8: Configure Star Schema Relationships
In the Model View, create single-direction 1-to-many (`1:*`) relationships:
- `dim_customers[Customer_ID]` (1) -> `fact_orders_2023[Customer_ID]` (*)
- `dim_products[Product_ID]` (1) -> `fact_orders_2023[Product_ID]` (*)
- `fact_orders_2023[Order_ID]` (1) -> `fact_returns_2023[Order_ID]` (0..1)
- `DimDate[Date]` (1) -> `fact_orders_2023[Order_Date]` (*) [Active]
- `DimDate[Date]` (1) -> `fact_orders_2023[Delivery_Date]` (*) [Inactive]
- `DimDate[Date]` (1) -> `fact_forecast_2024[Forecast_Month]` (*) [Active]

### Step 9: Create Dedicated Measure Storage
1. On the **Home** tab, click **Enter Data**.
2. Name the table `_Measures` and load.

### Step 10: Import DAX Measures
Open [`dax/measures/`](../dax/measures/) and copy the DAX measures into the `_Measures` table:
- Core KPIs: `Total Sales`, `Total Cost`, `Total Profit`, `Profit Margin`, `Total Orders`, `Total Customers`, `Average Order Value`.
- Sales, Products, Customers, Regions, Orders, Profitability, Returns, Forecast.

### Steps 11–19: Build the 9 Dashboard Pages
Follow the visual-by-visual documentation in [`docs/dashboard-pages/`](dashboard-pages/):
- **Page 1:** [Executive Overview](dashboard-pages/01-executive-overview.md)
- **Page 2:** [Sales Performance](dashboard-pages/02-sales-performance.md)
- **Page 3:** [Product Analysis](dashboard-pages/03-product-analysis.md)
- **Page 4:** [Customer Insights](dashboard-pages/04-customer-insights.md)
- **Page 5:** [Region Analysis](dashboard-pages/05-region-analysis.md)
- **Page 6:** [Order Details](dashboard-pages/06-order-details.md)
- **Page 7:** [Profitability Analysis](dashboard-pages/07-profitability-analysis.md)
- **Page 8:** [Return Analysis](dashboard-pages/08-return-analysis.md)
- **Page 9:** [Forecast Analysis](dashboard-pages/09-forecast-analysis.md)

### Step 20: Configure Slicers & Interactions
Refer to [`docs/slicers-interactions.md`](slicers-interactions.md) to set up synchronized date filters across historical pages and configure drill-through tooltips.

### Step 21: Validate Report Figures
Check that card visuals on Executive Overview display:
- **Total Revenue:** `$12.84M` (`$12,840,570.00`)
- **Total Profit:** `$2.31M` (`$2,310,910.00`)
- **Profit Margin:** `18.0%` (`17.997%`)
- **Total Orders:** `178,200`
- **Total Customers:** `46,798`

### Step 22: Apply Visual Styling & Branding
Incorporate color tokens and icons from [`docs/visual-style-guide.md`](visual-style-guide.md) and [`assets/icons/`](../assets/icons/).

### Step 23: Save Power BI File
Save your completed report as `Enterprise_Sales_Analytics.pbix`.

### Step 24: Publish & Share
Publish to the Power BI Service or Microsoft Fabric workspace as authorized.
