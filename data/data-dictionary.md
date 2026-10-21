# Data Dictionary & Schema Specification

This document provides the authoritative column-by-column schema specification for all five tables in the **Enterprise Power BI Analytics Portfolio**. All definitions are verified against `excel/powerbi-implementation-handbook.xlsx` and reconciled against the 231,130 source records in `data/raw/`.

---

## Relational Architecture Summary

| Table Name | Entity Type | Row Count | Primary Key | Foreign Keys | Granularity |
|---|---|---:|---|---|---|
| [`fact_orders_2023`](#1-fact_orders_2023) | Transaction Fact | 178,200 | `Order_ID` | `Customer_ID`, `Product_ID` | One row per sales order |
| [`dim_customers`](#2-dim_customers) | Conformed Dimension | 46,798 | `Customer_ID` | None | One row per customer |
| [`dim_products`](#3-dim_products) | Conformed Dimension | 320 | `Product_ID` | None | One row per product item |
| [`fact_returns_2023`](#4-fact_returns_2023) | Event Fact | 5,800 | `Return_ID` | `Order_ID` | One row per returned order |
| [`fact_forecast_2024`](#5-fact_forecast_2024) | Scenario Fact | 12 | `Forecast_Month` | Connects via `DimDate` | One row per calendar month |
| **Total Records** | | **231,130** | | | |

---

## 1. `fact_orders_2023`

**Description:** Central transactional fact table recording every customer purchase in calendar year 2023. Contains one row per order line item (178,200 orders).  
- **Total Records:** 178,200  
- **Primary Key:** `Order_ID (Primary Key)`  
- **Foreign Keys:** `Customer_ID -> dim_customers[Customer_ID], Product_ID -> dim_products[Product_ID]`  
- **Grain:** One record per completed sales order  

| Column Name | Suggested Type | Handling / Transformation | Sample Values | Nulls | Source |
|---|---|---|---|---|---|
| `Order_ID` | Text | Use Power Query to confirm type; keys remain text | `ORD0000001, ORD0000002, ORD0000003` | None (0%) | Source CSV |
| `Order_Date` | Date | Use Power Query to confirm type; keys remain text | `2023-07-09, 2023-09-19, 2023-09-23` | None (0%) | Source CSV |
| `Customer_ID` | Text | Use Power Query to confirm type; keys remain text | `C023885, C037060, C007841` | None (0%) | Source CSV |
| `Product_ID` | Text | Use Power Query to confirm type; keys remain text | `P0249, P0183, P0315` | None (0%) | Source CSV |
| `Country` | Text | Use Power Query to confirm type; keys remain text | `United Kingdom, United States, S...` | None (0%) | Source CSV |
| `State_Province` | Text | Use Power Query to confirm type; keys remain text | `Manchester, New York, Madrid` | None (0%) | Source CSV |
| `Region` | Text | Use Power Query to confirm type; keys remain text | `Europe, North America, Asia` | None (0%) | Source CSV |
| `Sales_Channel` | Text | Use Power Query to confirm type; keys remain text | `Online Store, Corporate, Retail ...` | None (0%) | Source CSV |
| `Shipping_Method` | Text | Use Power Query to confirm type; keys remain text | `Standard Shipping, Express Shipp...` | None (0%) | Source CSV |
| `Order_Status` | Text | Use Power Query to confirm type; keys remain text | `Delivered, Returned, Shipped` | None (0%) | Source CSV |
| `Quantity` | Whole number | Use Power Query to confirm type; keys remain text | `1, 2, 3` | None (0%) | Source CSV |
| `Sales_Amount_USD` | Decimal number | Use Power Query to confirm type; keys remain text | `92.58, 25.94, 106.54` | None (0%) | Source CSV |
| `Cost_Amount_USD` | Decimal number | Use Power Query to confirm type; keys remain text | `75.16, 21.39, 86.49` | None (0%) | Source CSV |
| `Profit_Amount_USD` | Decimal number | Use Power Query to confirm type; keys remain text | `17.42, 4.55, 20.05` | None (0%) | Source CSV |
| `Profit_Margin_Pct` | Decimal number | Use Power Query to confirm type; keys remain text | `18.816, 17.54, 18.819` | None (0%) | Source CSV |
| `Unit_Price_USD` | Decimal number | Use Power Query to confirm type; keys remain text | `92.58, 25.94, 53.27` | None (0%) | Source CSV |
| `Delivery_Days` | Whole number | Use Power Query to confirm type; keys remain text | `1.0, 3.0, 4.0` | 10,000 (5.6%) | Source CSV |
| `On_Time_Delivery` | Text | Use Power Query to confirm type; keys remain text | `Yes, No, Not Applicable` | None (0%) | Source CSV |
| `Delivery_Date` | Date | Use Power Query to confirm type; keys remain text | `2023-07-10, 2023-09-22, 2023-09-27` | 10,000 (5.6%) | Source CSV |

---

## 2. `dim_customers`

**Description:** Customer demographic and profile dimension containing unique attributes for all purchasing accounts.  
- **Total Records:** 46,798  
- **Primary Key:** `Customer_ID (Primary Key)`  
- **Foreign Keys:** `None (Referenced by fact_orders_2023)`  
- **Grain:** One record per unique registered customer  

| Column Name | Suggested Type | Handling / Transformation | Sample Values | Nulls | Source |
|---|---|---|---|---|---|
| `Customer_ID` | Text | Use Power Query to confirm type; keys remain text | `C000001, C000002, C000003` | None (0%) | Source CSV |
| `Customer_Name` | Text | Use Power Query to confirm type; keys remain text | `Customer 000001, Customer 000002...` | None (0%) | Source CSV |
| `Customer_Segment` | Text | Use Power Query to confirm type; keys remain text | `Corporate, Consumer, Home Office` | None (0%) | Source CSV |
| `Age_Group` | Text | Use Power Query to confirm type; keys remain text | `18-24, 25-34, 65+` | None (0%) | Source CSV |
| `Acquisition_Channel` | Text | Use Power Query to confirm type; keys remain text | `Organic Search, Email, Referral` | None (0%) | Source CSV |
| `Customer_Type` | Text | Use Power Query to confirm type; keys remain text | `New, Existing` | None (0%) | Source CSV |

---

## 3. `dim_products`

**Description:** Product catalog dimension detailing merchandise hierarchy, brand information, and standard list pricing.  
- **Total Records:** 320  
- **Primary Key:** `Product_ID (Primary Key)`  
- **Foreign Keys:** `None (Referenced by fact_orders_2023)`  
- **Grain:** One record per unique SKU / product item  

| Column Name | Suggested Type | Handling / Transformation | Sample Values | Nulls | Source |
|---|---|---|---|---|---|
| `Product_ID` | Text | Use Power Query to confirm type; keys remain text | `P0001, P0002, P0003` | None (0%) | Source CSV |
| `Product_Name` | Text | Use Power Query to confirm type; keys remain text | `Laptop Pro 15", Smartphone X, Of...` | None (0%) | Source CSV |
| `Product_Category` | Text | Use Power Query to confirm type; keys remain text | `Electronics, Furniture, Sports` | None (0%) | Source CSV |
| `Product_Subcategory` | Text | Use Power Query to confirm type; keys remain text | `Laptops, Mobile Phones, Chairs` | None (0%) | Source CSV |
| `Brand` | Text | Use Power Query to confirm type; keys remain text | `Nexora, Aster, PrimeLine` | None (0%) | Source CSV |
| `List_Price_USD` | Decimal number | Use Power Query to confirm type; keys remain text | `116.98, 24.64, 91.57` | None (0%) | Source CSV |

---

## 4. `fact_returns_2023`

**Description:** Return transactions fact table tracking returned orders, reason codes, resolutions, and processed refund amounts.  
- **Total Records:** 5,800  
- **Primary Key:** `Return_ID (Primary Key)`  
- **Foreign Keys:** `Order_ID -> fact_orders_2023[Order_ID]`  
- **Grain:** One record per returned order transaction  

| Column Name | Suggested Type | Handling / Transformation | Sample Values | Nulls | Source |
|---|---|---|---|---|---|
| `Return_ID` | Text | Use Power Query to confirm type; keys remain text | `RET000001, RET000002, RET000003` | None (0%) | Source CSV |
| `Order_ID` | Text | Use Power Query to confirm type; keys remain text | `ORD0000004, ORD0000059, ORD0000061` | None (0%) | Source CSV |
| `Return_Date` | Date | Use Power Query to confirm type; keys remain text | `2023-09-09, 2023-06-16, 2023-07-18` | None (0%) | Source CSV |
| `Return_Reason` | Text | Use Power Query to confirm type; keys remain text | `Defective Product, Changed Mind,...` | None (0%) | Source CSV |
| `Resolution` | Text | Use Power Query to confirm type; keys remain text | `Refunded, Exchanged, Replaced` | None (0%) | Source CSV |
| `Refund_Amount_USD` | Decimal number | Use Power Query to confirm type; keys remain text | `57.37, 62.21, 0.0` | None (0%) | Source CSV |
| `Return_Value_USD` | Decimal number | Use Power Query to confirm type; keys remain text | `61.32, 70.99, 51.2` | None (0%) | Source CSV |

---

## 5. `fact_forecast_2024`

**Description:** Monthly projection scenario table establishing 2024 forecast baselines and illustrative planning scenario bounds (conservative -12% / optimistic +12%). Note that legacy column headers containing '_95' represent deterministic managerial scenario planning bounds rather than Gaussian statistical confidence intervals.  
- **Total Records:** 12  
- **Primary Key:** `Forecast_Month (Composite / Temporal Key)`  
- **Foreign Keys:** `Forecast_Month -> DimDate[Date] (Connected via Calendar dimension)`  
- **Grain:** One record per forecast calendar month in 2024  

| Column Name | Suggested Type | Handling / Transformation | Sample Values | Nulls | Source |
|---|---|---|---|---|---|
| `Forecast_Month` | Date | Use Power Query to confirm type; keys remain text | `2024-01-01, 2024-02-01, 2024-03-01` | None (0%) | Source CSV |
| `Forecast_Sales_USD` | Decimal number | Use Power Query to confirm type; keys remain text | `1048938.46, 1085529.34, 1134317.17` | None (0%) | Source CSV |
| `Sales_Lower_95_USD` | Decimal number | Use Power Query to confirm type; keys remain text | `923065.84, 955265.82, 998199.11` | None (0%) | Source CSV |
| `Sales_Upper_95_USD` | Decimal number | Use Power Query to confirm type; keys remain text | `1174811.08, 1215792.86, 1270435.23` | None (0%) | Source CSV |
| `Forecast_Orders` | Whole number | Use Power Query to confirm type; keys remain text | `14204, 14700, 15361` | None (0%) | Source CSV |
| `Orders_Lower_95` | Whole number | Use Power Query to confirm type; keys remain text | `12499, 12936, 13517` | None (0%) | Source CSV |
| `Orders_Upper_95` | Whole number | Use Power Query to confirm type; keys remain text | `15909, 16464, 17205` | None (0%) | Source CSV |
| `Forecast_Profit_USD` | Decimal number | Use Power Query to confirm type; keys remain text | `189857.86, 197270.29, 206961.32` | None (0%) | Source CSV |
| `Forecast_Profit_Margin_Pct` | Decimal number | Use Power Query to confirm type; keys remain text | `18.1, 18.17, 18.25` | None (0%) | Source CSV |
| `Forecast_Return_Rate_Pct` | Decimal number | Use Power Query to confirm type; keys remain text | `3.1, 3.05, 2.99` | None (0%) | Source CSV |
| `Scenario` | Text | Use Power Query to confirm type; keys remain text | `Illustrative baseline` | None (0%) | Source CSV |

---

## Data Type Standardization Guidelines

When importing these CSV tables into Power BI Desktop via Power Query:
1. **Disable Automatic Type Detection:** Power BI's automatic date/time detection can introduce locale discrepancies. Explicitly declare column data types in the Applied Steps.
2. **Key Columns as Text:** Always maintain `Order_ID`, `Customer_ID`, `Product_ID`, and `Return_ID` as `Text` to avoid unintentional mathematical operations and preserve leading zeros.
3. **Currency Columns:** Set `Sales_Amount_USD`, `Cost_Amount_USD`, `Profit_Amount_USD`, `Unit_Price_USD`, `Refund_Amount_USD`, and `Return_Value_USD` to `Fixed Decimal Number` (`Currency`) for high precision and 4-decimal VertiPaq internal storage.
4. **Dates:** Explicitly set `Order_Date`, `Delivery_Date`, `Return_Date`, and `Forecast_Month` as `Date` (ISO 8601 `YYYY-MM-DD`).
5. **Percentages:** Store `Profit_Margin_Pct` and `Forecast_Profit_Margin_Pct` as `Decimal Number` and format as `0.0%` in the modeling view.
