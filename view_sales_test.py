import unittest
from store_management_testing import view_sales_history

class TestSalesManagement(unittest.TestCase):

    def test_view_sales_history(self):
        sales_history = [
            {"store_id": 1, "product_name": "Product 105", "quantity": 507},
            {"store_id": 2, "product_name": "Product 102", "quantity": 398}
        ]

        expected_output = [
            "Store 1 - Product 1 (Quantity: 507)",
            "Store 2 - Product 2 (Quantity: 398)"
        ]

        output = view_sales_history(sales_history)

        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
