import os
import unittest
import pandas as pd

class TestRelationships(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        test_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(test_dir, '..', 'data', 'raw')
        cls.orders = pd.read_csv(os.path.join(data_dir, 'fact_orders_2023.csv'))
        cls.customers = pd.read_csv(os.path.join(data_dir, 'dim_customers.csv'))
        cls.products = pd.read_csv(os.path.join(data_dir, 'dim_products.csv'))
        cls.returns = pd.read_csv(os.path.join(data_dir, 'fact_returns_2023.csv'))

    def test_customer_foreign_key_integrity(self):
        """All Customer_IDs in fact_orders_2023 must exist in dim_customers."""
        order_customers = set(self.orders['Customer_ID'])
        master_customers = set(self.customers['Customer_ID'])
        orphans = order_customers - master_customers
        self.assertEqual(len(orphans), 0, f"Found {len(orphans)} orphan Customer_IDs in orders")

    def test_product_foreign_key_integrity(self):
        """All Product_IDs in fact_orders_2023 must exist in dim_products."""
        order_products = set(self.orders['Product_ID'])
        master_products = set(self.products['Product_ID'])
        orphans = order_products - master_products
        self.assertEqual(len(orphans), 0, f"Found {len(orphans)} orphan Product_IDs in orders")

    def test_return_foreign_key_integrity(self):
        """All Order_IDs in fact_returns_2023 must exist in fact_orders_2023."""
        return_orders = set(self.returns['Order_ID'])
        valid_orders = set(self.orders['Order_ID'])
        orphans = return_orders - valid_orders
        self.assertEqual(len(orphans), 0, f"Found {len(orphans)} orphan Order_IDs in returns")

    def test_customer_primary_key_uniqueness(self):
        """Customer_ID in dim_customers must be 100% unique."""
        self.assertEqual(len(self.customers), self.customers['Customer_ID'].nunique())

    def test_product_primary_key_uniqueness(self):
        """Product_ID in dim_products must be 100% unique."""
        self.assertEqual(len(self.products), self.products['Product_ID'].nunique())

    def test_order_primary_key_uniqueness(self):
        """Order_ID in fact_orders_2023 must be 100% unique."""
        self.assertEqual(len(self.orders), self.orders['Order_ID'].nunique())

if __name__ == '__main__':
    unittest.main()
