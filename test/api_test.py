from fastapi.testclient import TestClient

from test.helpers import CryptofiTestCase
from src.api import app


class TestHelloWorldRoute(CryptofiTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = TestClient(app)
        cls.url = "/"

    def test_hello_world_route(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"hello": "world"})
