import os
import unittest
import pandas as pd

class TestDataQuality(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        test_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(test_dir, '..', 'data', 'raw')
        cls.orders = pd.read_csv(os.path.join(data_dir, 'fact_orders_2023.csv'))
        cls.customers = pd.read_csv(os.path.join(data_dir, 'dim_customers.csv'))
        cls.products = pd.read_csv(os.path.join(data_dir, 'dim_products.csv'))
        cls.returns = pd.read_csv(os.path.join(data_dir, 'fact_returns_2023.csv'))
        cls.forecast = pd.read_csv(os.path.join(data_dir, 'fact_forecast_2024.csv'))

    def test_null_values_in_keys(self):
        """Primary and foreign key columns must contain zero null values."""
        self.assertEqual(self.orders['Order_ID'].isna().sum(), 0)
        self.assertEqual(self.orders['Customer_ID'].isna().sum(), 0)
        self.assertEqual(self.orders['Product_ID'].isna().sum(), 0)
        self.assertEqual(self.customers['Customer_ID'].isna().sum(), 0)
        self.assertEqual(self.products['Product_ID'].isna().sum(), 0)
        self.assertEqual(self.returns['Return_ID'].isna().sum(), 0)
        self.assertEqual(self.returns['Order_ID'].isna().sum(), 0)

    def test_date_ranges(self):
        """Order dates must fall strictly within 2023 calendar year."""
        min_date = self.orders['Order_Date'].min()
        max_date = self.orders['Order_Date'].max()
        self.assertTrue(min_date.startswith('2023-01'))
        self.assertTrue(max_date.startswith('2023-12'))

    def test_forecast_period_coverage(self):
        """Forecast table must cover exactly 12 months in 2024."""
        self.assertEqual(len(self.forecast), 12)
        months = self.forecast['Forecast_Month'].tolist()
        self.assertEqual(months[0], '2024-01-01')
        self.assertEqual(months[-1], '2024-12-01')

    def test_forecast_scenario_bounds(self):
        """Forecast scenario bounds must equal exactly Baseline * 0.88 and Baseline * 1.12."""
        for _, row in self.forecast.iterrows():
            baseline = row['Forecast_Sales_USD']
            lower = row['Sales_Lower_95_USD']
            upper = row['Sales_Upper_95_USD']
            self.assertAlmostEqual(lower, baseline * 0.88, places=2)
            self.assertAlmostEqual(upper, baseline * 1.12, places=2)

    def test_record_counts_consistency(self):
        """Total records across all 5 tables must equal exactly 231,130."""
        total_rows = (
            len(self.orders) +
            len(self.customers) +
            len(self.products) +
            len(self.returns) +
            len(self.forecast)
        )
        self.assertEqual(len(self.orders), 178200)
        self.assertEqual(len(self.customers), 46798)
        self.assertEqual(len(self.products), 320)
        self.assertEqual(len(self.returns), 5800)
        self.assertEqual(len(self.forecast), 12)
        self.assertEqual(total_rows, 231130)

    def test_positive_pricing_and_quantities(self):
        """Orders must have positive quantities and selling prices."""
        self.assertTrue((self.orders['Quantity'] > 0).all())
        self.assertTrue((self.orders['Sales_Amount_USD'] > 0).all())
        self.assertTrue((self.orders['Cost_Amount_USD'] > 0).all())

    def test_delivery_days_positive(self):
        """Delivered orders must have non-negative delivery days; in-flight orders are null."""
        delivered_days = self.orders['Delivery_Days'].dropna()
        self.assertTrue((delivered_days >= 0).all())
        # Exactly 10,000 in-flight orders (Shipped 5,800 + Processing 4,200) have no delivery date
        self.assertEqual(self.orders['Delivery_Days'].isna().sum(), 10000)

if __name__ == '__main__':
    unittest.main()
