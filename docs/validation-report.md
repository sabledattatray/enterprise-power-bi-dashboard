# Automated Data & Asset Validation Report

**Generated On:** 2026-10-21 14:58:40  
**Execution Engine:** Python 3.14.4 / Automated CI Pipeline  
**Overall Status:** **ALL CHECKS PASSED (100% RECONCILED)**

---

## 1. Table Record Counts & Primary Key Integrity

| Table Name | File Name | Expected Rows | Actual Rows | Primary Key | Distinct PKs | Uniqueness | Status |
|---|---|---:|---:|---|---:|:---:|:---:|
| Orders | `fact_orders_2023.csv` | 178,200 | 178,200 | `Order_ID` | 178,200 | 100.0% | **PASS** |
| Customers | `dim_customers.csv` | 46,798 | 46,798 | `Customer_ID` | 46,798 | 100.0% | **PASS** |
| Products | `dim_products.csv` | 320 | 320 | `Product_ID` | 320 | 100.0% | **PASS** |
| Returns | `fact_returns_2023.csv` | 5,800 | 5,800 | `Return_ID` | 5,800 | 100.0% | **PASS** |
| Forecast | `fact_forecast_2024.csv` | 12 | 12 | `Forecast_Month` | 12 | 100.0% | **PASS** |
| **Total** | | **231,130** | **231,130** | | | | **PASS** |

---

## 2. Referential Integrity & Foreign Key Audit

| Foreign Key Relationship | Parent Table | Child Table | Expected Orphans | Actual Orphans | Status |
|---|---|---|:---:|:---:|:---:|
| `Customer_ID` | `dim_customers` | `fact_orders_2023` | 0 | 0 | **PASS** |
| `Product_ID` | `dim_products` | `fact_orders_2023` | 0 | 0 | **PASS** |
| `Order_ID` | `fact_orders_2023` | `fact_returns_2023` | 0 | 0 | **PASS** |

---

## 3. Financial Metric Reconciliation

| Metric Name | Benchmark Target | Actual Calculated Value | Reconciled Formula | Variance | Status |
|---|---:|---:|---|:---:|:---:|
| **Total Sales Revenue** | $12.84M | **$12,840,570.00** | `SUM(Sales_Amount_USD)` | $0.00 | **PASS** |
| **Total Product Cost** | $10.53M | **$10,529,660.00** | `SUM(Cost_Amount_USD)` | $0.00 | **PASS** |
| **Total Operating Profit** | $2.31M | **$2,310,910.00** | `SUM(Profit_Amount_USD)` | $0.00 | **PASS** |
| **Profit Math Check** | $2,310,910.00 | **$2,310,910.00** | `Total Sales - Total Cost` | $0.00 | **PASS** |
| **Profit Margin %** | ~18.0% | **17.9969%** | `Total Profit / Total Sales` | 0.003% | **PASS** |
| **Average Order Value (AOV)** | $72.06 | **$72.06** | `Total Sales / Total Orders` | $0.00 | **PASS** |
| **Return Rate %** | ~3.25% | **3.2548%** | `Total Returns / Total Orders` | 0.005% | **PASS** |
| **Total Refund Liability** | $213,726.90 | **$213,726.90** | `SUM(Refund_Amount_USD)` | $0.00 | **PASS** |

---

## 4. Order Status Breakdown

| Order Status | Count | Percentage | Notes |
|---|---:|---:|---|
| `Delivered` | 162,400 | 91.13% | Fulfilled successfully |
| `Returned` | 5,800 | 3.25% | Exactly matches 5,800 records in `fact_returns_2023` |
| `Shipped` | 5,800 | 3.25% | In transit |
| `Processing` | 4,200 | 2.36% | Warehouse processing |
| **Total** | **178,200** | **100.00%** | |

---

## 5. Visual Asset Verification

- **Dashboard Images:** All 9 dashboard views verified in both `.png` (high-fidelity lossless) and `.webp` formats (18 files total).
- **SVG Icon Library:** 62 vector SVG icons verified for well-formed XML syntax and 100% absence of embedded scripts or external network dependencies.
- **Implementation Handbook:** `excel/powerbi-implementation-handbook.xlsx` verified with 11 operational worksheets intact.
