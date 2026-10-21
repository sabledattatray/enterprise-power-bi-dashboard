#!/usr/bin/env python3
"""
Enterprise Power BI Analytics Portfolio — Automated Data Validation Engine
Validates CSV files, schemas, primary keys, referential integrity, and financial reconciliations.
"""

import os
import sys
import pandas as pd
import numpy as np

def run_data_validation():
    # Resolve repo root relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(script_dir, '..'))
    data_dir = os.path.join(repo_root, 'data', 'raw')

    print("================================================================================")
    print("ENTERPRISE POWER BI ANALYTICS PORTFOLIO — DATA VALIDATION")
    print(f"Data Directory: {data_dir}")
    print("================================================================================")

    failures = []
    
    # 1. File existence checks
    required_files = {
        'fact_orders_2023.csv': 178200,
        'dim_customers.csv': 46798,
        'dim_products.csv': 320,
        'fact_returns_2023.csv': 5800,
        'fact_forecast_2024.csv': 12
    }

    dfs = {}
    for filename, expected_rows in required_files.items():
        filepath = os.path.join(data_dir, filename)
        if not os.path.exists(filepath):
            failures.append(f"Missing required data file: {filename}")
            print(f"[FAIL] Missing {filename}")
            continue
        try:
            df = pd.read_csv(filepath)
            dfs[filename] = df
            actual_rows = len(df)
            if actual_rows == expected_rows:
                print(f"[PASS] {filename}: {actual_rows:,} rows (matches expected)")
            else:
                failures.append(f"{filename} row count mismatch: expected {expected_rows}, got {actual_rows}")
                print(f"[FAIL] {filename}: {actual_rows:,} rows (expected {expected_rows})")
        except Exception as e:
            failures.append(f"Error reading {filename}: {str(e)}")
            print(f"[FAIL] Error reading {filename}: {e}")

    if len(dfs) < len(required_files):
        print(f"\nFATAL: Aborting further checks due to missing files.")
        return 1

    orders = dfs['fact_orders_2023.csv']
    customers = dfs['dim_customers.csv']
    products = dfs['dim_products.csv']
    returns = dfs['fact_returns_2023.csv']
    forecast = dfs['fact_forecast_2024.csv']

    print("\n--------------------------------------------------------------------------------")
    print("PRIMARY KEY UNIQUENESS CHECKS")
    print("--------------------------------------------------------------------------------")

    pk_checks = [
        ('fact_orders_2023.csv', orders, 'Order_ID', 178200),
        ('dim_customers.csv', customers, 'Customer_ID', 46798),
        ('dim_products.csv', products, 'Product_ID', 320),
        ('fact_returns_2023.csv', returns, 'Return_ID', 5800),
        ('fact_returns_2023.csv', returns, 'Order_ID', 5800)
    ]

    for tname, df, col, exp_unique in pk_checks:
        n_unique = df[col].nunique()
        if n_unique == exp_unique:
            print(f"[PASS] {tname}[{col}]: {n_unique:,} distinct values (100% unique)")
        else:
            failures.append(f"{tname}[{col}] uniqueness failure: expected {exp_unique}, got {n_unique}")
            print(f"[FAIL] {tname}[{col}]: {n_unique:,} distinct values (expected {exp_unique})")

    print("\n--------------------------------------------------------------------------------")
    print("REFERENTIAL INTEGRITY CHECKS")
    print("--------------------------------------------------------------------------------")

    # Customers FK in orders
    orphan_cust = set(orders['Customer_ID']) - set(customers['Customer_ID'])
    if len(orphan_cust) == 0:
        print(f"[PASS] orders[Customer_ID] -> customers[Customer_ID]: 0 orphan keys")
    else:
        failures.append(f"Found {len(orphan_cust)} orphan Customer_IDs in orders")
        print(f"[FAIL] orders[Customer_ID] -> customers[Customer_ID]: {len(orphan_cust)} orphan keys")

    # Products FK in orders
    orphan_prod = set(orders['Product_ID']) - set(products['Product_ID'])
    if len(orphan_prod) == 0:
        print(f"[PASS] orders[Product_ID] -> products[Product_ID]: 0 orphan keys")
    else:
        failures.append(f"Found {len(orphan_prod)} orphan Product_IDs in orders")
        print(f"[FAIL] orders[Product_ID] -> products[Product_ID]: {len(orphan_prod)} orphan keys")

    # Orders FK in returns
    orphan_ret = set(returns['Order_ID']) - set(orders['Order_ID'])
    if len(orphan_ret) == 0:
        print(f"[PASS] returns[Order_ID] -> orders[Order_ID]: 0 orphan keys")
    else:
        failures.append(f"Found {len(orphan_ret)} orphan Order_IDs in returns")
        print(f"[FAIL] returns[Order_ID] -> orders[Order_ID]: {len(orphan_ret)} orphan keys")

    print("\n--------------------------------------------------------------------------------")
    print("FINANCIAL RECONCILIATION CHECKS")
    print("--------------------------------------------------------------------------------")

    total_sales = float(orders['Sales_Amount_USD'].sum())
    total_cost = float(orders['Cost_Amount_USD'].sum())
    total_profit = float(orders['Profit_Amount_USD'].sum())
    calc_profit = round(total_sales - total_cost, 2)
    profit_diff = abs(total_profit - calc_profit)
    margin_pct = (total_profit / total_sales) * 100
    aov = total_sales / len(orders)
    return_rate_pct = (len(returns) / len(orders)) * 100

    print(f"Total Sales Revenue:  ${total_sales:,.2f} (Target: $12,840,570.00)")
    print(f"Total Merchandise Cost: ${total_cost:,.2f} (Target: $10,529,660.00)")
    print(f"Total Operating Profit: ${total_profit:,.2f} (Target: $2,310,910.00)")
    print(f"Profit Math (Sales-Cost): ${calc_profit:,.2f} (Diff: ${profit_diff:.2f})")
    print(f"Profit Margin:        {margin_pct:.4f}% (Target: ~18.0%)")
    print(f"Average Order Value:  ${aov:.2f} (Target: $72.06)")
    print(f"Return Rate:          {return_rate_pct:.4f}% (Target: ~3.25%)")

    if abs(total_sales - 12840570.0) < 0.01:
        print("[PASS] Total Sales matches $12,840,570.00")
    else:
        failures.append(f"Total Sales mismatch: {total_sales} != 12840570.0")

    if abs(total_profit - 2310910.0) < 0.01:
        print("[PASS] Total Profit matches $2,310,910.00")
    else:
        failures.append(f"Total Profit mismatch: {total_profit} != 2310910.0")

    if profit_diff < 0.01:
        print("[PASS] Sales - Cost = Profit internal reconciliation exact")
    else:
        failures.append(f"Sales - Cost != Profit difference: {profit_diff}")

    if abs(margin_pct - 17.9969) < 0.01:
        print("[PASS] Profit Margin reconciles to 18.0% (~17.997%)")
    else:
        failures.append(f"Profit Margin discrepancy: {margin_pct}")

    if abs(aov - 72.06) < 0.01:
        print("[PASS] Average Order Value reconciles to $72.06")
    else:
        failures.append(f"AOV discrepancy: {aov}")

    print("\n--------------------------------------------------------------------------------")
    print("ORDER STATUS & LOGISTICS AUDIT")
    print("--------------------------------------------------------------------------------")

    status_counts = orders['Order_Status'].value_counts().to_dict()
    print("Order Status Counts:", status_counts)
    returned_orders_count = status_counts.get('Returned', 0)
    if returned_orders_count == 5800:
        print(f"[PASS] 'Returned' order status count ({returned_orders_count:,}) exactly matches fact_returns_2023 rows")
    else:
        failures.append(f"Returned orders status mismatch: {returned_orders_count} != 5800")

    total_refund = float(returns['Refund_Amount_USD'].sum())
    print(f"Total Refund Liability: ${total_refund:,.2f} (Target: $213,726.90)")
    if abs(total_refund - 213726.90) < 0.01:
        print("[PASS] Refund amount matches $213,726.90")
    else:
        failures.append(f"Refund amount mismatch: {total_refund} != 213726.90")

    print("\n================================================================================")
    if not failures:
        print("ALL DATA VALIDATION CHECKS PASSED (100% RECONCILED)")
        print("================================================================================")
        return 0
    else:
        print(f"FAILED CHECKS COUNT: {len(failures)}")
        for f in failures:
            print(f"  - {f}")
        print("================================================================================")
        return 1

if __name__ == '__main__':
    sys.exit(run_data_validation())
