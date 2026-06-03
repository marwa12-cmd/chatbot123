import unittest
from unittest.mock import patch
import service as service_module


class ServiceTests(unittest.TestCase):
    def test_get_products_xmlrpc(self):
        def fake_ServerProxy(endpoint):
            class Common:
                def authenticate(self, db, username, password, d):
                    return 42

            class Models:
                def execute_kw(self, db, uid, password, model, method, args, kwargs=None):
                    return [{'website_url': '/p1', 'categ_id': 'Men / jeans / jean'}]

            if endpoint.endswith('/common'):
                return Common()
            return Models()

        with patch('service.xmlrpc.client.ServerProxy', side_effect=fake_ServerProxy):
            with service_module.app.test_request_context('/api/products', method='POST', json={'category_pattern': 'Men / jeans / jean'}):
                resp = service_module.get_products()
                data = resp.get_json()
                self.assertIsInstance(data, list)
                self.assertGreaterEqual(len(data), 1)
                self.assertIn('website_url', data[0])


if __name__ == '__main__':
    unittest.main()
