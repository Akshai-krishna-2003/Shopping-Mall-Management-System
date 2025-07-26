# test_store_management.py

import unittest
from store_management_testing import add_store

class TestStoreManagement(unittest.TestCase):

    def test_add_store(self):
        stores = []
        next_store_id = 1

        new_name = "Test Store A"
        new_location = "Mall C"
        new_contact = "875-8888-4444"

        expected_store = {"id": next_store_id, "name": new_name, "location": new_location, "contact": new_contact, "inventory": []}

        updated_stores, updated_next_store_id = add_store(stores, next_store_id, new_name, new_location, new_contact)

        self.assertEqual(updated_stores, [expected_store])
        self.assertEqual(updated_next_store_id, next_store_id + 1)

if __name__ == '__main__':
    unittest.main()
