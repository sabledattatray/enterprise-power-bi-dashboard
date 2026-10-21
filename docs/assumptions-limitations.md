# Project Assumptions, Authenticity Disclosures & Limitations

This document provides transparent documentation regarding dataset scope, modeling assumptions, and known limitations within the **Enterprise Power BI Analytics Portfolio**.

---

## 1. Synthetic Data Notice & Provenance

- **Non-Commercial Demonstration:** All transactions, customer profiles, product names, return reasons, and delivery logs in this repository are **100% synthetically generated** for educational demonstration.
- **No Real PII:** Customer names follow formatted synthetic patterns (`Customer 000001` through `Customer 046798`). No actual personal identifiable information (PII) is included or exposed.
- **Reconciliation Baseline:** The synthetic data has been mathematically calibrated so that internal columns reconcile perfectly:
  - `Sales_Amount_USD - Cost_Amount_USD = Profit_Amount_USD` ($0.00 variance)
  - `Delivered + Returned + Shipped + Processing = 178,200 orders`

---

## 2. Dashboard Mockups vs. Analytical Reality

- **Design References:** The dashboard images located in `assets/dashboards/` are **high-fidelity UI mockups and design references**.
- **Visual Discrepancies:** While the mockups illustrate realistic corporate dashboards, certain annotations or chart slices depicted in the design mockups may vary slightly from the underlying synthetic dataset. The dataset and DAX library serve as the authoritative single source of truth.
- **No Pre-Bundled PBIX:** In accordance with PRD guidelines, no proprietary or pre-compiled `.pbix` binary is bundled in v1.0.0. Complete instructions are provided to construct the report in Power BI Desktop.

---

## 3. Analytical & Longitudinal Limitations

- **Single-Year Transaction History (2023):** Transactional records span from `2023-01-01` to `2023-12-31`. Because full-year 2022 transaction data is not included, prior-year comparisons (`Sales PY`, `Sales YoY %`) return `BLANK()` unless historical data is injected.
- **Order-Level Granularity:** Each order row represents a single product line item. Complex multi-line shopping baskets are not modeled in the current schema.
- **Macro-Level Forecast:** The 2024 forecast is aggregated at the company-wide monthly level. It does not provide SKU-level or state-level predictive models.
- **Return Financials:** Return cases represent separate post-purchase operational events. Refund amounts (`$213,726.90`) are recorded separately in `fact_returns_2023` and are not retroactively deducted from gross order sales.
