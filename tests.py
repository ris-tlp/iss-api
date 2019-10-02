import unittest
from iss.index import app


class RouteTests(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_404_status_code(self):
        result = self.app.get('/random')
        self.assertEqual(result.status_code, 404)

if __name__ == "__main__":
    unittest.main()
