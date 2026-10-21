# Slicers, Interactions & Drill-Through Configuration

This document specifies the slicer configurations, page-level synchronization, and visual interaction matrix for the 9 dashboard pages.

---

## Global Slicers & Synchronization Matrix

| Slicer Name | Bound Field | Slicer Style | Synced Pages | Interaction Behavior |
|---|---|---|---|---|
| **Date Range** | `DimDate[Date]` | Between Slider / Dropdown | Pages 01–08 | Synchronized across all 2023 historical pages. |
| **Region** | `fact_orders_2023[Region]` | Multi-Select Dropdown | Pages 01, 02, 05, 07 | Filters geographic visual elements dynamically. |
| **Product Category** | `dim_products[Product_Category]` | Tile / Buttons | Pages 01, 02, 03, 07 | Filters category-level revenue and profit. |
| **Customer Segment** | `dim_customers[Customer_Segment]` | Dropdown | Pages 01, 04, 06 | Segments consumer, corporate, and small business. |
| **Sales Channel** | `fact_orders_2023[Sales_Channel]` | Horizontal Badges | Pages 02, 06 | Filters Online Store, Retail, Marketplace, Direct. |
| **Forecast Scenario** | `fact_forecast_2024[Scenario]` | Radio / Single-Select | Page 09 only | Toggles baseline vs upper/lower confidence bands. |

---

## Cross-Filtering vs. Cross-Highlighting Rules

In Power BI Desktop (**Format > Edit Interactions**), configure the following visual interactions:

1. **Category Bar Charts -> Monthly Trends:**
   - Set to **Filter** rather than Highlight. Selecting "Electronics" filters the trend line to show Electronics revenue over time, preventing visual clutter from low-opacity background bars.

2. **Geographic Maps -> Regional Matrix:**
   - Set to **Filter**. Clicking a continent or country focuses the detail tables and KPI cards on that specific market.

3. **Return Reason Donut -> Order Details Table:**
   - Set to **Filter**. Selecting "Defective Item" instantly filters the table to show the specific order IDs and refund amounts associated with defective goods.

---

## Drill-Through Tooltips

- **Product Detail Tooltip:** Hovering over any product ranking bar displays a dedicated 320x240 tooltip page displaying:
  - Product Name & SKU
  - Unit Price & Cost
  - Return Rate %
  - 12-Month Sparkline Trend
- **Customer Profile Tooltip:** Hovering over high-value customers reveals their acquisition channel, total orders, and average delivery time.
