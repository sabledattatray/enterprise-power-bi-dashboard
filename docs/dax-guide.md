# DAX Development & Optimization Guide

This guide covers the DAX design patterns, calculation evaluation contexts, and performance optimizations utilized throughout the **Enterprise Power BI Analytics Portfolio**.

---

## 1. Context Evaluation: Row vs. Filter Context

- **Filter Context:** The ambient set of active filters applied by visual slicing, page filters, and user selections. All aggregations (`SUM`, `DISTINCTCOUNT`, `AVERAGE`) evaluate strictly over the active filter context.
- **Row Context:** The current row cursor present during calculated column evaluation or table iterator functions (`SUMX`, `AVERAGEX`).
- **Context Transition:** When calling `CALCULATE()` within a row context, the current row context is automatically transformed into an equivalent filter context.

---

## 2. Core DAX Calculation Patterns

### Base Metric Pattern
Always define simple explicit base measures rather than dragging raw columns into visuals:
```dax
Total Sales = SUM ( fact_orders_2023[Sales_Amount_USD] )
Total Cost = SUM ( fact_orders_2023[Cost_Amount_USD] )
Total Profit = SUM ( fact_orders_2023[Profit_Amount_USD] )
```

### Ratio & Share Pattern
Always use `DIVIDE` to avoid divide-by-zero errors, and use `ALLSELECTED` or `REMOVEFILTERS` for share calculations:
```dax
Profit Margin = DIVIDE ( [Total Profit], [Total Sales], 0 )

Sales Share % = 
DIVIDE (
    [Total Sales],
    CALCULATE ( [Total Sales], ALLSELECTED () )
)
```

### Time Intelligence Patterns
Time intelligence requires a contiguous date table marked as a Date table:
```dax
// Year-to-Date
Sales YTD = TOTALYTD ( [Total Sales], DimDate[Date] )

// Month-over-Month Growth
Sales Previous Month = CALCULATE ( [Total Sales], DATEADD ( DimDate[Date], -1, MONTH ) )
Sales MoM % = DIVIDE ( [Total Sales] - [Sales Previous Month], [Sales Previous Month] )

// Rolling 3 Months
Rolling 3M Sales = 
CALCULATE (
    [Total Sales],
    DATESINPERIOD ( DimDate[Date], MAX ( DimDate[Date] ), -3, MONTH )
)
```

---

## 3. VertiPaq Performance Optimization Tips

1. **Avoid Calculated Columns for Metrics:** Calculated columns consume RAM in the data model and do not recalculate dynamically based on slicers. Use explicit measures.
2. **Minimize Iterators:** Avoid nesting `SUMX` or `FILTER` when native columnar aggregations (`SUM`, `CALCULATE`) can achieve the same result.
3. **Keep Keys as Text:** VertiPaq compresses high-cardinality alphanumeric keys efficiently when stored as string hash dictionaries.
