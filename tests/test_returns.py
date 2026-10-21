import os
import unittest
import pandas as pd

class TestReturns(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        test_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(test_dir, '..', 'data', 'raw')
        cls.orders = pd.read_csv(os.path.join(data_dir, 'fact_orders_2023.csv'))
        cls.returns = pd.read_csv(os.path.join(data_dir, 'fact_returns_2023.csv'))

    def test_total_returns_count(self):
        """Total return records must equal 5,800."""
        self.assertEqual(len(self.returns), 5800)

    def test_order_status_returned_match(self):
        """Orders with Order_Status == 'Returned' must equal 5,800."""
        returned_orders = (self.orders['Order_Status'] == 'Returned').sum()
        self.assertEqual(returned_orders, 5800)

    def test_return_rate_calculation(self):
        """Return rate must equal 3.255% (5,800 / 178,200)."""
        rate = (len(self.returns) / len(self.orders)) * 100
        self.assertAlmostEqual(rate, 3.2548, places=3)

    def test_total_refund_amount(self):
        """Total refund amount must reconcile to $213,726.90."""
        refund_sum = float(self.returns['Refund_Amount_USD'].sum())
        self.assertAlmostEqual(refund_sum, 213726.90, places=2)

    def test_return_reasons_present(self):
        """Standard return reason codes must be populated with no nulls."""
        self.assertEqual(self.returns['Return_Reason'].isna().sum(), 0)
        reasons = self.returns['Return_Reason'].unique()
        self.assertIn('Defective Product', reasons)
        self.assertIn('Wrong Item', reasons)

    def test_resolution_codes_present(self):
        """Standard resolutions (Refund, Exchange, Replacement) must be present."""
        self.assertEqual(self.returns['Resolution'].isna().sum(), 0)
        resolutions = self.returns['Resolution'].unique()
        self.assertTrue(len(resolutions) >= 3)

if __name__ == '__main__':
    unittest.main()
