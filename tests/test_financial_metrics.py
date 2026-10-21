import os
import unittest
import pandas as pd

class TestFinancialMetrics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        test_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(test_dir, '..', 'data', 'raw')
        cls.orders = pd.read_csv(os.path.join(data_dir, 'fact_orders_2023.csv'))

    def test_total_sales_revenue(self):
        """Total sales revenue must reconcile exactly to $12,840,570.00."""
        total_sales = float(self.orders['Sales_Amount_USD'].sum())
        self.assertAlmostEqual(total_sales, 12840570.0, places=2)

    def test_total_cost_of_goods(self):
        """Total cost must reconcile exactly to $10,529,660.00."""
        total_cost = float(self.orders['Cost_Amount_USD'].sum())
        self.assertAlmostEqual(total_cost, 10529660.0, places=2)

    def test_total_operating_profit(self):
        """Total profit must reconcile exactly to $2,310,910.00."""
        total_profit = float(self.orders['Profit_Amount_USD'].sum())
        self.assertAlmostEqual(total_profit, 2310910.0, places=2)

    def test_profit_internal_consistency(self):
        """Sales minus Cost must equal Profit exactly across all records."""
        sales = self.orders['Sales_Amount_USD'].sum()
        cost = self.orders['Cost_Amount_USD'].sum()
        profit = self.orders['Profit_Amount_USD'].sum()
        self.assertAlmostEqual(sales - cost, profit, places=2)

    def test_profit_margin_benchmark(self):
        """Profit margin must reconcile to ~18.0% (17.997%)."""
        sales = self.orders['Sales_Amount_USD'].sum()
        profit = self.orders['Profit_Amount_USD'].sum()
        margin_pct = (profit / sales) * 100
        self.assertAlmostEqual(margin_pct, 17.9969, places=3)

    def test_average_order_value(self):
        """Average Order Value (AOV) must reconcile to $72.06."""
        sales = self.orders['Sales_Amount_USD'].sum()
        orders_count = self.orders['Order_ID'].nunique()
        aov = sales / orders_count
        self.assertAlmostEqual(aov, 72.06, places=2)

    def test_zero_negative_margins(self):
        """Ensure no orders have negative profit in 2023 baseline."""
        negative_profit = (self.orders['Profit_Amount_USD'] < 0).sum()
        self.assertEqual(negative_profit, 0)

if __name__ == '__main__':
    unittest.main()
