# Contributing to Enterprise Power BI Analytics Portfolio

Thank you for your interest in contributing to this open-source analytics resource! Whether you are fixing typos in documentation, suggesting DAX optimizations, adding unit tests, or sharing custom report templates, your contributions are welcome.

---

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please treat all contributors with respect and professionalism.

---

## How Can You Contribute?

1. **Reporting Issues:**
   - Use the [Bug Report template](.github/ISSUE_TEMPLATE/bug_report.md) to report calculation anomalies, data inconsistencies, or broken links.
   - Use the [Feature Request template](.github/ISSUE_TEMPLATE/feature_request.md) to suggest additional DAX measures, new visualization layouts, or Fabric pipelines.

2. **Improving Documentation:**
   - Clarify Power Query M-code steps or DAX filter context explanations.
   - Improve formatting, diagrams, or visual implementation tips.

3. **Enhancing DAX Measures:**
   - Propose performance-optimized alternatives for calculation patterns.
   - Submit additional advanced time-intelligence patterns.

4. **Extending Test Coverage:**
   - Add new Python validation tests under `tests/` to verify edge cases.

---

## Pull Request Guidelines

1. **Fork the Repository:** Create your own fork and branch from `main`.
2. **Branch Naming:** Use clear branch names such as `fix/dax-time-intelligence` or `docs/power-query-updates`.
3. **Run Validation:** Ensure all Python validation tests pass before submitting:
   ```bash
   python scripts/validate_data.py
   python scripts/validate_assets.py
   python -m unittest discover tests
   ```
4. **Keep Commits Clean:** Write concise, descriptive commit messages.
5. **No Synthetic Data Invalidation:** Never alter source data values to force test matches; if discrepancies exist, document them.

---

## Questions & Contact

For questions regarding this portfolio project:
- Website: [dattasable.com](https://dattasable.com)
- Email: [info@dattasable.com](mailto:info@dattasable.com)
