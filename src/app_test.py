import os
import unittest
from src.app import app, init_db


class TestApp(unittest.TestCase):
    def setUp(self):
        self.db_path = "test_items.db"
        os.environ["DB_PATH"] = self.db_path
        init_db()
        self.client = app.test_client()
        self.client.testing = True
        

    def tearDown(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)


    def test_get_items(self):
        response = self.client.get("/items")
        self.assertEqual(response.status_code, 200)


    def test_add_item(self):
        response = self.client.post("/items", 
                                    json={"id": 1, "name": "Test Item"})
        self.assertEqual(response.status_code, 201)


    def test_delete_item(self):
        self.client.post("/items", json={"id": 2, "name": "Another Item"})
        response = self.client.delete("/items/2")
        self.assertEqual(response.status_code, 200)



if __name__ == "__main__":
    unittest.main()
