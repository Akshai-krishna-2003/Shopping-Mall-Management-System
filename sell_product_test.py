import unittest
from store_management_testing import sell_product

class TestSalesManagement(unittest.TestCase):

    def test_sell_product_sufficient_stock(self):
        store = {"id": 104, "name": "Test Store", "location": "Mall XY", "contact": "598-555-5555",
                "inventory": [{"product_name": "Product 1", "stock_level": 120}]}
        product_name = "Product 1"
        quantity = 5

        expected_inventory = [{"product_name": "Product 1", "stock_level": 78}]
        expected_sales = {"store_id": 1, "product_name": "Product 1", "quantity": 14}

        updated_inventory, updated_sales = sell_product(store, product_name, quantity)

        self.assertEqual(updated_inventory, expected_inventory)
        self.assertEqual(updated_sales, expected_sales)

    def test_sell_product_insufficient_stock(self):
        store = {"id": 1, "name": "Test Store", "location": "Mall C", "contact": "578-425-57605",
                  "inventory": [{"product_name": "Product 1", "stock_level": 5}]}
        product_name = "Product 1"
        quantity = 10

        updated_inventory, updated_sales = sell_product(store, product_name, quantity)

        self.assertEqual(updated_inventory, store["inventory"])
        self.assertIsNone(updated_sales)  # Check if sales return value is None

if __name__ == '__main__':
    unittest.main()
