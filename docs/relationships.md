# Model Relationships & Filter Propagation

This document defines the relationships established within the Power BI semantic model, their cardinalities, cross-filter behaviors, and filter propagation paths.

---

## Relationship Specification Matrix

| From (Dimension / Parent) | To (Fact / Child) | Cardinality | Filter Direction | State | Business Rationale & DAX Interaction |
|---|---|:---:|:---:|:---:|---|
| `dim_customers[Customer_ID]` | `fact_orders_2023[Customer_ID]` | `1:*` | Single | **Active** | Filters sales orders by customer demographics, segment, and acquisition channel. |
| `dim_products[Product_ID]` | `fact_orders_2023[Product_ID]` | `1:*` | Single | **Active** | Filters sales orders by category, subcategory, brand, and list price. |
| `fact_orders_2023[Order_ID]` | `fact_returns_2023[Order_ID]` | `1:0..1` | Single | **Active** | Links returns to original sales transactions. Enables return rate calculation against total orders. |
| `DimDate[Date]` | `fact_orders_2023[Order_Date]` | `1:*` | Single | **Active** | Primary date filter driving all sales, profit, and order time intelligence. |
| `DimDate[Date]` | `fact_orders_2023[Delivery_Date]` | `1:*` | Single | *Inactive* | Secondary fulfillment date relationship; invoked via `USERELATIONSHIP(DimDate[Date], fact_orders_2023[Delivery_Date])`. |
| `DimDate[Date]` | `fact_forecast_2024[Forecast_Month]` | `1:*` | Single | **Active** | Enables unified date filtering between historical 2023 data and 2024 projections. |

---

## Filter Direction Best Practices

1. **Strictly Single-Direction Filtering:**
   All relationships use **Single** cross-filtering direction from dimension to fact. Bi-directional filtering is explicitly disabled to avoid:
   - Ambiguous filter paths
   - Unintended circular filter dependencies
   - Significant performance degradation on high-cardinality tables (178,200 rows)

2. **Role-Playing Date Dimension:**
   `fact_orders_2023` contains two date fields: `Order_Date` and `Delivery_Date`.
   - The primary active relationship connects `DimDate[Date]` to `Order_Date`.
   - To analyze logistics delivery efficiency by delivery month, use explicit DAX:
     ```dax
     Delivered Orders by Delivery Date = 
     CALCULATE (
         [Delivered Orders],
         USERELATIONSHIP ( DimDate[Date], fact_orders_2023[Delivery_Date] )
     )
     ```

3. **Forecast Fact Isolation:**
   `fact_forecast_2024` contains company-level monthly aggregates. It is deliberately connected **only** to `DimDate`. It does not connect directly to `dim_products` or `dim_customers` because product or customer keys do not exist in the macro forecast dataset.
