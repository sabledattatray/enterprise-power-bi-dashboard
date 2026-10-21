# Synthetic Retail Analytics Dataset

This directory contains the synthetic relational business dataset used throughout the **Enterprise Power BI Analytics Portfolio**.

---

## Directory Contents

- [`raw/`](raw/): Complete production-scale source CSV files totaling **231,130 rows** across 5 relational tables.
- [`samples/`](samples/): 100-row preview samples of each table for quick inspection, testing, and rapid development without downloading full data tables.
- [`data-dictionary.md`](data-dictionary.md): Comprehensive 49-column data dictionary detailing types, cardinalities, null handling, and sample values.

---

## Table Inventory & File Sizes

| Table | File Name | Size (Uncompressed) | Total Rows | Columns | Purpose |
|---|---|---:|---:|---:|---|
| Orders | [`raw/fact_orders_2023.csv`](raw/fact_orders_2023.csv) | 29.7 MB | 178,200 | 19 | Transactional sales, logistics, revenue, cost, profit |
| Customers | [`raw/dim_customers.csv`](raw/dim_customers.csv) | 2.7 MB | 46,798 | 6 | Customer master, demographics, segments, acquisition channel |
| Products | [`raw/dim_products.csv`](raw/dim_products.csv) | 19.6 KB | 320 | 6 | Product catalog, hierarchy, categories, brands, list price |
| Returns | [`raw/fact_returns_2023.csv`](raw/fact_returns_2023.csv) | 394 KB | 5,800 | 7 | Return records, reasons, resolutions, refund amounts |
| Forecast | [`raw/fact_forecast_2024.csv`](raw/fact_forecast_2024.csv) | 1.5 KB | 12 | 11 | 2024 monthly scenario projections & illustrative ±12% planning bounds |
| **Total** | | **~32.8 MB** | **231,130** | **49** | |

---

## Validated Core Financial Totals

All records in this dataset reconcile mathematically to the penny:
- **Total Sales Revenue:** `$12,840,570.00`
- **Total Cost:** `$10,529,660.00`
- **Total Operating Profit:** `$2,310,910.00` (`$12,840,570.00 - $10,529,660.00 = $2,310,910.00`)
- **Portfolio Profit Margin:** `17.997%` (~18.00%)
- **Average Order Value (AOV):** `$72.06` (`$12,840,570.00 / 178,200 orders`)
- **Return Rate:** `3.255%` (`5,800 returned orders / 178,200 orders`)
- **Referential Integrity:** 100% match (0 orphan customers, 0 orphan products, 0 orphan returns)

---

## Data Provenance & Synthetic Disclaimer

> [!NOTE]
> All records in this dataset are synthetically generated for educational demonstration and portfolio modeling. Any resemblance to actual companies, proprietary financial records, or real persons is purely coincidental.
