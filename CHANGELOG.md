# Changelog

All notable changes to the **Enterprise Power BI Analytics Portfolio** project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-10-21

### Added
- **Public Release Resource Packs:** Automated release packaging script (`scripts/package_release.py`) generating 5 standalone, integrity-verified ZIP archives with SHA-256 checksum manifest (`releases/v1.0.0/checksums-sha256.txt`):
  - `enterprise-powerbi-datasets-v1.0.0.zip` (Package A: 5 CSVs, data dictionary, relationships, validation report)
  - `enterprise-powerbi-dashboard-designs-v1.0.0.zip` (Package B: 9 PNG/WebP designs, style guide, page specifications)
  - `enterprise-powerbi-svg-icons-v1.0.0.zip` (Package C: 85 SVGs across 12 categories, branding, catalog)
  - `enterprise-powerbi-dax-handbook-v1.0.0.zip` (Package D: 11-sheet Excel handbook, 66 DAX measures, date table, KPI definitions)
  - `enterprise-powerbi-complete-resources-v1.0.0.zip` (Package E: Complete unified portfolio pack)
- **Recruiter Presentation & 5-Minute Review Roadmap:** Added dedicated sections in `README.md` summarizing business and technical BI skills demonstrated, along with a guided 5-step evaluation roadmap for hiring managers and recruiters.
- **DAX Technical Validation Matrix (`docs/dax-validation-matrix.md`):** Complete audit matrix evaluating all 66 DAX measures across syntax, schema references, filter context, safe division (`DIVIDE`), and date relationships.
- **Markdown Link Validation Engine (`scripts/validate_links.py`):** Automated test script verifying internal documentation links, heading anchors, and asset cross-references (391 links verified with zero broken paths).
- **Curated Vector Icon Suite Expansion:** Verified and cataloged 85 SVG icons across 12 business categories with standardized `0 0 24 24` viewboxes, transparent backgrounds, and direct Power BI compatibility.
- **CI Artifact Upload:** Configured GitHub Actions workflow to upload live CI-generated validation reports as workflow artifacts.

### Fixed
- **Statistical Forecast Terminology Alignment (Issue 02):** Replaced statistically unsupported "95% Confidence Interval" labels with accurate business terminology: **Illustrative Baseline Forecast**, **Illustrative Conservative Scenario Bound (-12%)**, and **Illustrative Optimistic Scenario Bound (+12%)**. Documented the exact calculation methodology (`Baseline * 0.88` and `Baseline * 1.12`) across all documentation and DAX comments while preserving CSV schema stability.
- **LinkedIn Author Profile Link (Issue 03):** Removed generic homepage link and established a documented configuration item for the repository owner to insert their verified personal LinkedIn profile handle.
- **Dataset Record Count Consistency (Issue 06):** Reconciled all documentation, badges, and guides to the audited total of **231,130 records** across orders (178,200), customers (46,798), products (320), returns (5,800), and forecast (12), eliminating outdated references.
- **Historical Comparison Metric Classification (Issue 04):** Formally categorized comparative analytics into 4 tiers (Tier 1 Intra-2023 Actuals, Tier 2 Actual vs Forecast, Tier 3 Scenario Bounds, Tier 4 Prior-Year YoY). Documented that YoY growth metrics evaluate to `BLANK()` without 2022 historical actuals and provided implementation guidance for future historical ingestion.
- **Financial Metric Semantics (Issue 07):** Reconciled financial benchmarks to exact source CSV values: Gross Revenue `$12,840,570.00`, Direct Merchandise Cost / COGS `$10,529,660.00`, Gross Operating Profit `$2,310,910.00` ($0.00 variance), Profit Margin `17.997%` (~18.0%), AOV `$72.06`, Return Rate `3.255%`, and Refund Liability `$213,726.90`. Clarified that cost reflects direct procurement and profit represents merchandise gross margin before corporate SG&A overhead.

### Improved
- **Power BI Report Authenticity & Disclosures (Issue 05):** Adopted preferred portfolio title (*Enterprise Power BI Analytics Portfolio — Nine Dashboard Design References with Reproducible Data, DAX, and Implementation Resources*) and added explicit authenticity disclaimers distinguishing visual design references from active compiled `.pbix` reports.
- **README Visual Hierarchy & Navigation (Issue 10):** Streamlined headings, added executive branding emblems, improved mobile responsiveness, verified relative links, and enhanced download options with direct repository fallbacks.
- **GitHub Actions Workflow Hardening (Issue 09):** Implemented least-privilege security permissions (`contents: read`), added automated link validation and release archive verification steps, and configured dynamic validation report artifact uploading.
- **Documentation Quality & Consistency (Issue 13):** Synchronized terminology, table references, and mathematical formulas across all 20+ markdown documentation files.
