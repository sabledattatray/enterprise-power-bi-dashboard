# Changelog

All notable changes to the **Enterprise Power BI Analytics Portfolio** project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2024-10-21

### Added
- **Dashboard Design References:** 9 high-resolution dashboard mockups covering Executive Overview, Sales Performance, Product Analysis, Customer Insights, Region Analysis, Order Details, Profitability Analysis, Return Analysis, and Forecast Analysis.
- **Relational Synthetic Dataset:** Complete 5-table relational retail business dataset totaling 231,130 records across:
  - `fact_orders_2023.csv` (178,200 rows)
  - `dim_customers.csv` (46,798 rows)
  - `dim_products.csv` (320 rows)
  - `fact_returns_2023.csv` (5,800 rows)
  - `fact_forecast_2024.csv` (12 rows)
- **Data Samples:** Lightweight 100-row CSV samples in `data/samples/` for fast previewing without loading large data files.
- **DAX Measure Library:** 66 verified DAX measures categorized into Core KPIs, Time Intelligence, Mix & Ratios, Customer Analytics, Order Analytics, Return Analytics, and Forecast Analytics.
- **Calculated Objects & Date Table:** DAX calendar dimension script and order dimension calculated columns.
- **Excel Implementation Handbook:** Preserved master Excel handbook `excel/powerbi-implementation-handbook.xlsx` containing 11 structured worksheets covering data dictionary, model relationships, visual build matrix, slicer configurations, and build roadmaps.
- **SVG Icon Library:** 62 vector icons categorized across Navigation, KPIs, Charts, Commerce, Customers, and UI/Brand.
- **Technical Documentation:**
  - `data-dictionary.md`: Full specifications for 49 table columns.
  - `architecture.md`: Architectural overview and Microsoft Fabric compatibility.
  - `data-model.md`: Star schema documentation with Mermaid ERD.
  - `relationships.md`: Cardinality and filter propagation guidelines.
  - `kpi-definitions.md`: Formulaic logic and business rationales.
  - `power-query-guide.md`: End-to-end Power Query ETL transformations.
  - `dax-guide.md`: DAX patterns, filter context, and best practices.
  - `slicers-interactions.md`: Visual cross-filtering matrix.
  - `visual-style-guide.md`: Typography, color palette tokens, card layout specifications.
  - `forecasting-methodology.md`: Baseline scenario projections and confidence bands.
  - `assumptions-limitations.md`: Transparent documentation of dataset scope.
- **Detailed Dashboard Page Guides:** 9 comprehensive Markdown build guides for every dashboard view.
- **Automated Validation Engine:** Python scripts (`scripts/validate_data.py`, `scripts/validate_assets.py`, `scripts/generate_validation_report.py`) and automated test suite (`tests/`).
- **CI Automation:** GitHub Actions workflow `.github/workflows/validate.yml` executing data integrity, financial reconciliation, and asset checks.
- **Downloadable Resource Packaging:** Packaging script for versioned release bundles.

### Fixed
- Reconciled initial financial benchmark discrepancies to validated dataset source figures ($12,840,570.00 sales, $2,310,910.00 profit, 17.997% profit margin).
- Enforced strict 1-to-1 order line item verification (178,200 rows = 178,200 distinct order IDs).
- Verified zero orphan foreign keys across customer, product, and return relationships.
