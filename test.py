from main import app
from sanic.testing import SanicTestClient
import unittest

class Test(unittest.TestCase):
    def test_root(self):
        request, response = SanicTestClient(app, port=None).get('/')
        self.assertEqual(response.status, 200)

    def test_get_companies(self):
        request, response = SanicTestClient(app, port=None).get('/CompanyProducts')
        self.assertEqual(response.status, 200)


if __name__ == '__main__':
    unittest.main()