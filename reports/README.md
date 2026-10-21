# Power BI Reports & Template Status

## Current Status: Design Reference & Implementation Phase (v1.0.0)

> [!IMPORTANT]
> **Authenticity Disclosure:** As specified in the Project Requirements Document (PRD), no pre-compiled binary `.pbix` file is bundled in this initial `v1.0.0` release. 
> 
> The nine dashboard views showcased in this repository represent **high-fidelity visual design mockups and reference architectures**. All underlying synthetic data, schema relationships, DAX formulas, visual build matrices, and validation tests are fully provided so any developer can reproduce the reports from scratch in Power BI Desktop.

---

## How to Build the Power BI Report (Reproducibility Guide)

You can build the interactive multi-page Power BI report in 10-15 minutes using the assets in this repository:

1. **Launch Power BI Desktop** (latest release recommended).
2. **Import CSV Data:**
   - Select **Get Data > Text/CSV**.
   - Navigate to `data/raw/` and load:
     - `fact_orders_2023.csv`
     - `dim_customers.csv`
     - `dim_products.csv`
     - `fact_returns_2023.csv`
     - `fact_forecast_2024.csv`
3. **Configure Power Query Transformations:**
   - Follow [`docs/power-query-guide.md`](../docs/power-query-guide.md) to set data types (keep IDs as Text; currencies as Fixed Decimal; dates as Date).
4. **Create the Date Dimension:**
   - Go to **Modeling > New Table** and paste [`dax/date-table.dax`](../dax/date-table.dax).
   - Mark as Date Table.
5. **Establish Relationships:**
   - Configure star-schema relationships as detailed in [`docs/relationships.md`](../docs/relationships.md).
6. **Add DAX Measures:**
   - Create a `_Measures` table.
   - Copy DAX measures from [`dax/measures/`](../dax/measures/) or `excel/powerbi-implementation-handbook.xlsx`.
7. **Build Visual Pages:**
   - Refer to the 9 visual-by-visual guides in [`docs/dashboard-pages/`](../docs/dashboard-pages/) to place cards, charts, and slicers.
8. **Validate Metrics:**
   - Ensure the Executive Overview cards match: Sales `$12.84M`, Profit `$2.31M`, Margin `18.0%`, Orders `178,200`, Customers `46,798`.

---

## Release Roadmap for Compiled Reports

| Milestone | Target Version | Deliverable | Description |
|---|---|---|---|
| **v1.0.0** | Current | Architecture & Data Pack | Design mockups, full relational CSVs, DAX library, Excel handbook, automated test suite |
| **v1.1.0** | Next | Standalone `.pbix` File | Compiled interactive desktop report with bookmarks, tooltips, and theme JSON |
| **v1.2.0** | Future | Power BI Project (`.pbip`) | Git-tracked developer format with TMDL semantic models and report JSON |
| **v1.3.0** | Future | Microsoft Fabric Lakehouse | Fabric lakehouse ingestion pipelines, Direct Lake model, and notebook orchestration |
| **v2.0.0** | Future | Live Web Embed | Public interactive Power BI service embed on [dattasable.com](https://dattasable.com) |
