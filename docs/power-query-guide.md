# Power Query ETL & Data Preparation Guide

This guide details the Power Query M transformations required to clean, normalize, and load the raw CSV files into the Power BI tabular engine.

---

## 15 Standard Transformation Principles

1. **Import Source CSVs:** Use `Csv.Document(File.Contents(...))` with UTF-8 encoding.
2. **Promote Headers:** Use `Table.PromoteHeaders` on initial load.
3. **Explicit Type Casting:** Apply explicit data types to avoid regional culture mismatches.
4. **Whitespace Trimming:** Strip leading and trailing whitespace from string dimensions.
5. **Key Preservation:** Keep `Order_ID`, `Customer_ID`, `Product_ID`, and `Return_ID` as `type text`.
6. **Currency Standardization:** Assign `Currency.Type` to ensure VertiPaq 4-decimal integer storage.
7. **Date Normalization:** Cast date fields as `type date` formatted ISO 8601 (`YYYY-MM-DD`).
8. **Null Value Audit:** Verify that critical transaction keys contain zero null values.
9. **Duplicate Detection:** Confirm primary key uniqueness across fact and dimension tables.
10. **Case Consistency:** Capitalize or title-case text attributes (`Sales_Channel`, `Shipping_Method`).
11. **Boolean Conversion:** Standardize `On_Time_Delivery` as `Yes`/`No` text or logical boolean.
12. **Dimension Independence:** Ensure conformed dimensions contain distinct records only.
13. **Reference Queries:** Avoid duplicate disk reads by referencing base staging queries if necessary.
14. **Row Count Validation:** Confirm row counts post-transformation match expectations.
15. **Query Folding / Dependency Management:** Disable report refresh on static lookup tables.

---

## Reproducible M-Code Snippets

### 1. `fact_orders_2023`
```powerquery
let
    Source = Csv.Document(File.Contents("data/raw/fact_orders_2023.csv"), [Delimiter=",", Columns=19, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Trimmed Text" = Table.TransformColumns(#"Promoted Headers", {
        {"Order_ID", Text.Trim, type text},
        {"Customer_ID", Text.Trim, type text},
        {"Product_ID", Text.Trim, type text},
        {"Country", Text.Trim, type text},
        {"State_Province", Text.Trim, type text},
        {"Region", Text.Trim, type text},
        {"Sales_Channel", Text.Trim, type text},
        {"Shipping_Method", Text.Trim, type text},
        {"Order_Status", Text.Trim, type text},
        {"On_Time_Delivery", Text.Trim, type text}
    }),
    #"Changed Types" = Table.TransformColumnTypes(#"Trimmed Text", {
        {"Order_ID", type text},
        {"Order_Date", type date},
        {"Customer_ID", type text},
        {"Product_ID", type text},
        {"Country", type text},
        {"State_Province", type text},
        {"Region", type text},
        {"Sales_Channel", type text},
        {"Shipping_Method", type text},
        {"Order_Status", type text},
        {"Quantity", Int64.Type},
        {"Sales_Amount_USD", Currency.Type},
        {"Cost_Amount_USD", Currency.Type},
        {"Profit_Amount_USD", Currency.Type},
        {"Profit_Margin_Pct", type number},
        {"Unit_Price_USD", Currency.Type},
        {"Delivery_Days", Int64.Type},
        {"On_Time_Delivery", type text},
        {"Delivery_Date", type date}
    })
in
    #"Changed Types"
```

### 2. `dim_customers`
```powerquery
let
    Source = Csv.Document(File.Contents("data/raw/dim_customers.csv"), [Delimiter=",", Columns=6, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Trimmed Text" = Table.TransformColumns(#"Promoted Headers", {
        {"Customer_ID", Text.Trim, type text},
        {"Customer_Name", Text.Trim, type text},
        {"Customer_Segment", Text.Trim, type text},
        {"Age_Group", Text.Trim, type text},
        {"Acquisition_Channel", Text.Trim, type text},
        {"Customer_Type", Text.Trim, type text}
    }),
    #"Changed Types" = Table.TransformColumnTypes(#"Trimmed Text", {
        {"Customer_ID", type text},
        {"Customer_Name", type text},
        {"Customer_Segment", type text},
        {"Age_Group", type text},
        {"Acquisition_Channel", type text},
        {"Customer_Type", type text}
    })
in
    #"Changed Types"
```

### 3. `dim_products`
```powerquery
let
    Source = Csv.Document(File.Contents("data/raw/dim_products.csv"), [Delimiter=",", Columns=6, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Trimmed Text" = Table.TransformColumns(#"Promoted Headers", {
        {"Product_ID", Text.Trim, type text},
        {"Product_Name", Text.Trim, type text},
        {"Product_Category", Text.Trim, type text},
        {"Product_Subcategory", Text.Trim, type text},
        {"Brand", Text.Trim, type text}
    }),
    #"Changed Types" = Table.TransformColumnTypes(#"Trimmed Text", {
        {"Product_ID", type text},
        {"Product_Name", type text},
        {"Product_Category", type text},
        {"Product_Subcategory", type text},
        {"Brand", type text},
        {"List_Price_USD", Currency.Type}
    })
in
    #"Changed Types"
```

### 4. `fact_returns_2023`
```powerquery
let
    Source = Csv.Document(File.Contents("data/raw/fact_returns_2023.csv"), [Delimiter=",", Columns=7, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Trimmed Text" = Table.TransformColumns(#"Promoted Headers", {
        {"Return_ID", Text.Trim, type text},
        {"Order_ID", Text.Trim, type text},
        {"Return_Reason", Text.Trim, type text},
        {"Resolution", Text.Trim, type text}
    }),
    #"Changed Types" = Table.TransformColumnTypes(#"Trimmed Text", {
        {"Return_ID", type text},
        {"Order_ID", type text},
        {"Return_Date", type date},
        {"Return_Reason", type text},
        {"Resolution", type text},
        {"Refund_Amount_USD", Currency.Type},
        {"Return_Value_USD", Currency.Type}
    })
in
    #"Changed Types"
```

### 5. `fact_forecast_2024`
```powerquery
let
    Source = Csv.Document(File.Contents("data/raw/fact_forecast_2024.csv"), [Delimiter=",", Columns=11, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Changed Types" = Table.TransformColumnTypes(#"Promoted Headers", {
        {"Forecast_Month", type date},
        {"Forecast_Sales_USD", Currency.Type},
        {"Sales_Lower_95_USD", Currency.Type},
        {"Sales_Upper_95_USD", Currency.Type},
        {"Forecast_Orders", Int64.Type},
        {"Orders_Lower_95", Int64.Type},
        {"Orders_Upper_95", Int64.Type},
        {"Forecast_Profit_USD", Currency.Type},
        {"Forecast_Profit_Margin_Pct", type number},
        {"Forecast_Return_Rate_Pct", type number},
        {"Scenario", type text}
    })
in
    #"Changed Types"
```
