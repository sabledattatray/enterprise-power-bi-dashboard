# Business KPI Definitions & Calculation Logic

This document specifies the business definitions, mathematical formulas, DAX implementations, and reconciled benchmarks for all Key Performance Indicators (KPIs) in the portfolio.

---

## Core Financial & Operational KPIs

### 1. Total Sales Revenue
- **Business Definition:** Gross dollar value generated from all completed retail orders in 2023 before deductions.
- **DAX Formula:** `SUM(fact_orders_2023[Sales_Amount_USD])`
- **Reconciled Value:** **$12,840,570.00**
- **Format:** Currency (`$#,##0.00`)

### 2. Total Cost of Goods Sold (COGS)
- **Business Definition:** Direct merchandise cost associated with the items fulfilled in orders.
- **DAX Formula:** `SUM(fact_orders_2023[Cost_Amount_USD])`
- **Reconciled Value:** **$10,529,660.00**
- **Format:** Currency (`$#,##0.00`)

### 3. Total Operating Profit
- **Business Definition:** Operating profit remaining after deducting direct merchandise costs from gross sales.
- **DAX Formula:** `SUM(fact_orders_2023[Profit_Amount_USD])`
- **Reconciled Value:** **$2,310,910.00**
- **Reconciliation Check:** `$12,840,570.00 - $10,529,660.00 = $2,310,910.00` (Exact match)
- **Format:** Currency (`$#,##0.00`)

### 4. Profit Margin %
- **Business Definition:** Proportion of sales revenue converted into operating profit.
- **DAX Formula:** `DIVIDE([Total Profit], [Total Sales], 0)`
- **Reconciled Value:** **17.997%** (~18.0%)
- **Format:** Percentage (`0.0%`)

### 5. Total Orders
- **Business Definition:** Count of unique commercial transactions fulfilled or placed in 2023.
- **DAX Formula:** `DISTINCTCOUNT(fact_orders_2023[Order_ID])`
- **Reconciled Value:** **178,200 orders**
- **Format:** Whole Number (`#,##0`)

### 6. Unique Customers
- **Business Definition:** Count of distinct customer accounts that placed at least one order in 2023.
- **DAX Formula:** `DISTINCTCOUNT(fact_orders_2023[Customer_ID])`
- **Reconciled Value:** **46,798 customers**
- **Format:** Whole Number (`#,##0`)

### 7. Average Order Value (AOV)
- **Business Definition:** Average revenue generated per placed order.
- **DAX Formula:** `DIVIDE([Total Sales], [Total Orders], 0)`
- **Reconciled Value:** **$72.06** (`$12,840,570.00 / 178,200`)
- **Format:** Currency (`$#,##0.00`)

### 8. Total Returns
- **Business Definition:** Total count of orders resulting in a formal customer return event.
- **DAX Formula:** `DISTINCTCOUNT(fact_returns_2023[Order_ID])`
- **Reconciled Value:** **5,800 returns**
- **Format:** Whole Number (`#,##0`)

### 9. Return Rate %
- **Business Definition:** Percentage of orders that resulted in a product return.
- **DAX Formula:** `DIVIDE([Total Returns], [Total Orders], 0)`
- **Reconciled Value:** **3.255%** (`5,800 / 178,200`)
- **Format:** Percentage (`0.0%`)

### 10. Total Refund Amount
- **Business Definition:** Total monetary refunds issued to customers for approved return cases.
- **DAX Formula:** `SUM(fact_returns_2023[Refund_Amount_USD])`
- **Reconciled Value:** **$213,726.90**
- **Format:** Currency (`$#,##0.00`)

### 11. Average Delivery Duration
- **Business Definition:** Mean elapsed time in calendar days between order placement and customer delivery.
- **DAX Formula:** `AVERAGE(fact_orders_2023[Delivery_Days])`
- **Reconciled Value:** **2.95 days**
- **Format:** Decimal (`0.0 days`)

### 12. On-Time Delivery %
- **Business Definition:** Percentage of delivered orders fulfilled within the promised delivery window.
- **DAX Formula:** `DIVIDE(CALCULATE(COUNTROWS(fact_orders_2023), fact_orders_2023[On_Time_Delivery] = "Yes"), [Total Orders], 0)`
- **Reconciled Value:** **84.9%** (151,292 on-time orders)
- **Format:** Percentage (`0.0%`)
