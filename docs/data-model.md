# Data Model & Star Schema Specification

This document details the analytical data model for the **Enterprise Power BI Analytics Portfolio**.

---

## Entity-Relationship Diagram (Mermaid ERD)

```mermaid
erDiagram
    dim_customers ||--o{ fact_orders_2023 : "places (1:N)"
    dim_products ||--o{ fact_orders_2023 : "ordered in (1:N)"
    fact_orders_2023 ||--o| fact_returns_2023 : "returned as (1:0..1)"
    DimDate ||--o{ fact_orders_2023 : "ordered on (1:N active)"
    DimDate ||--o{ fact_orders_2023 : "delivered on (1:N inactive)"
    DimDate ||--o{ fact_forecast_2024 : "forecast period (1:N active)"

    dim_customers {
        string Customer_ID PK
        string Customer_Name
        string Customer_Segment
        string Age_Group
        string Acquisition_Channel
        string Customer_Type
    }

    dim_products {
        string Product_ID PK
        string Product_Name
        string Product_Category
        string Product_Subcategory
        string Brand
        decimal List_Price_USD
    }

    fact_orders_2023 {
        string Order_ID PK
        date Order_Date FK
        string Customer_ID FK
        string Product_ID FK
        string Country
        string State_Province
        string Region
        string Sales_Channel
        string Shipping_Method
        string Order_Status
        int Quantity
        decimal Sales_Amount_USD
        decimal Cost_Amount_USD
        decimal Profit_Amount_USD
        decimal Profit_Margin_Pct
        decimal Unit_Price_USD
        int Delivery_Days
        string On_Time_Delivery
        date Delivery_Date
    }

    fact_returns_2023 {
        string Return_ID PK
        string Order_ID FK
        date Return_Date
        string Return_Reason
        string Resolution
        decimal Refund_Amount_USD
        decimal Return_Value_USD
    }

    fact_forecast_2024 {
        date Forecast_Month PK_FK
        decimal Forecast_Sales_USD
        decimal Sales_Lower_95_USD
        decimal Sales_Upper_95_USD
        int Forecast_Orders
        decimal Forecast_Profit_USD
        decimal Forecast_Profit_Margin_Pct
        decimal Forecast_Return_Rate_Pct
        string Scenario
    }

    DimDate {
        date Date PK
        int Year
        int Month_No
        string Month
        string Year_Month
        string Quarter
        int Year_Month_Sort
    }
```

---

## Grain & Cardinality Analysis

### Transactional Grain: One Row per Order
In `fact_orders_2023.csv`, every record represents an individual sales order containing a single product SKU line:
- **Total records:** `178,200`
- **Distinct Order_IDs:** `178,200`
- **Significance:** `COUNTROWS(fact_orders_2023)` is identical to `DISTINCTCOUNT(fact_orders_2023[Order_ID])`. This simplifies order-level aggregations and guarantees zero line-item duplication.

### Dimension Cardinality
- `dim_customers`: 46,798 unique customer accounts. Customer order frequency ranges from 1 to multiple repeat orders.
- `dim_products`: 320 unique products spanning 4 primary categories (`Electronics`, `Apparel`, `Home & Garden`, `Sports`).
- `fact_returns_2023`: 5,800 return records (exactly matching the 5,800 orders with `Order_Status == 'Returned'`).
- `fact_forecast_2024`: 12 monthly summary records for calendar year 2024.
