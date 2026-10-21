# Executive Overview Dashboard — Development & Implementation Guide

This document provides the complete technical and visual specification for **Page 01: Executive Overview Dashboard** of the **Enterprise Power BI Analytics Portfolio**.

---

## 1. Business Objective
Provide C-suite executives and senior leadership with a consolidated, top-level pulse on commercial health, profitability, customer acquisition, and fulfillment efficiency.

---

## 2. Executive Questions Answered
- What is our total gross revenue, net operating profit, and profit margin for the year?
- How is revenue and profit trending month-over-month across 2023?
- Which geographic regions and product categories drive the largest revenue share?
- How is our customer base distributed across Corporate, Consumer, and Small Business segments?
- What are our top revenue-generating products?

---

## 3. Dashboard Preview

![Executive Overview Dashboard](../../assets/dashboards/01-executive-overview.png)
*Figure 01: Executive Overview Dashboard design reference mockup (synthetic demonstration data).*

---

## 4. Key Performance Indicator (KPI) Definitions

| KPI Card | Target Value / Reconciled Benchmark | Bound DAX Measure | Business Description |
|---|---|---|---|
| **Total Revenue** | `$12,840,570.00 ($12.84M)` | `[Total Sales]` | Gross dollar volume across all 2023 orders |
| **Total Operating Profit** | `$2,310,910.00 ($2.31M)` | `[Total Profit]` | Gross sales minus direct merchandise cost |
| **Profit Margin %** | `17.997% (~18.0%)` | `[Profit Margin]` | Operating profit divided by gross revenue |
| **Total Orders** | `178,200` | `[Total Orders]` | Distinct count of commercial sales transactions |
| **Unique Customers** | `46,798` | `[Total Customers]` | Distinct count of purchasing customer accounts |
| **Average Order Value** | `$72.06` | `[Average Order Value]` | Total revenue divided by total orders |

---

## 5. Visual Inventory & Build Matrix

The following visual specifications define the exact layout, chart types, data fields, and measure bindings for this report page:

| Visual Title | Power BI Visual Type | Axis / Rows / Legend | Values / Bound Measures | Interactions & Notes |
|---|---|---|---|---|
| **KPI cards** | Cards | `Sales, Profit, Orders, Customers, Margin` | `[Total Sales], [Total Profit], [Total Orders], [Total Customers], [Profit Margin]` | All cards recompute; YOY blank without 2022 |
| **Sales & profit trend** | Line and clustered column | `DimDate[Year Month]` | `[Total Sales] bars; [Total Profit] line` | Sort by Year Month Sort |
| **Regional sales** | Filled map or bar | `fact_orders_2023[Country] / [Region]` | `[Total Sales]` | Set geography data category; bar fallback |
| **Category mix** | Donut | `dim_products[Product_Category]` | `[Total Sales]` | Use [Sales Share %] in tooltip |
| **Top products** | Horizontal bar | `dim_products[Product_Name]` | `[Total Sales]` | Filter rank <=5 |
| **Segment mix** | Donut | `dim_customers[Customer_Segment]` | `[Total Orders]` | Orders, not unique customers |
| **Region matrix** | Matrix | `fact_orders_2023[Region]` | `[Total Sales], [Total Profit], [Total Orders], [Total Customers], [Profit Margin]` | Conditional format growth only if PY exists |

---

## 6. Required Source Tables
- [`fact_orders_2023`](../../data/data-dictionary.md#fact_orders_2023)
- [`dim_customers`](../../data/data-dictionary.md#dim_customers)
- [`dim_products`](../../data/data-dictionary.md#dim_products)
- [`DimDate`](../../data/data-dictionary.md#DimDate)

---

## 7. Field Mappings & Schema Requirements

- **Primary Date Field:** `DimDate[Date]` (or `fact_forecast_2024[Forecast_Month]` for Page 09)
- **Aggregation Dimensions:** Mapped directly from conformed dimensions (`dim_customers`, `dim_products`, `DimDate`).
- **Measures Storage:** All calculations referenced from the dedicated `_Measures` container.

---

## 8. DAX Measures Used on this Page

The following verified DAX measures from [`dax/measures/`](../../dax/measures/) drive this view:
- `[Total Sales]`
- `[Total Profit]`
- `[Profit Margin]`
- `[Total Orders]`
- `[Total Customers]`
- `[Average Order Value]`

---

## 9. Filters & Slicers Configuration

- **Page Slicers:**
  - Date Range (DimDate[Date])
  - Region (fact_orders_2023[Region])
  - Category (dim_products[Product_Category])
  - Customer Segment (dim_customers[Customer_Segment])

---

## 10. Visual Interactions & Cross-Filtering Behavior

- **Edit Interactions:** All visuals set to **Filter** mode when interacting with bar charts and category tiles.
- **Cross-Highlighting:** Disabled on line charts to prevent low-contrast background bars.
- **Synchronized Slicers:** Date range and global regional slicers synchronize with other historical report pages.

---

## 11. Expected Analytical Insights
- North America ($4.85M) and Europe ($3.11M) represent over 61% of total enterprise revenue.
- Electronics is the largest revenue category, while Home & Garden delivers the highest margin stability.
- Sales show steady growth through Q3 with acceleration in Q4, reaching peak volumes in November and December.
- Average Order Value of $72.06 reflects healthy basket size across online store and retail channels.

---

## 12. Validation Requirements

- Verify all card values match the benchmark targets listed in Section 4.
- Sum of category / regional slices must reconcile exactly to the top-level total without duplication.
- Ensure automated test suite (`tests/`) passes before publishing.

---

## 13. Step-by-Step Implementation Instructions

1. **Create Page Canvas:** Add a new page in Power BI Desktop and name it `Executive Overview Dashboard`.
2. **Apply Visual Grid:** Configure a 16:9 canvas with `#F5F8FC` background and 16px page margins.
3. **Add Navigation Header:** Place the Datta Sable monogram logo and top navigation bar.
4. **Insert KPI Cards:** Place the top summary cards using Segoe UI 28pt bold callout values.
5. **Construct Charts:** Follow the Visual Inventory table in Section 5 to create and position each chart.
6. **Configure Interactions:** Select each visual, navigate to **Format > Edit Interactions**, and enforce single-direction filtering.
7. **Test Slicers:** Select various dates and segments to confirm responsive recalculation.

---

## 14. Known Limitations & Authenticity Notes

- Prior-year comparison cards (YoY) evaluate to BLANK() because transaction records are confined to calendar year 2023.
- Visual mockup depicted in Section 3 serves as an illustrative design benchmark; underlying dataset metrics are the authoritative source of truth.
