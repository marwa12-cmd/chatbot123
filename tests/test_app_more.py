import unittest
from unittest.mock import patch
import app as app_module


class AppMoreTests(unittest.TestCase):
    def test_extract_text_from_pdf_directory(self):
        with patch('app.os.listdir', return_value=['a.pdf', 'b.pdf', 'c.txt']):
            def fake_extract(path):
                return f'CONTENT:{path}'

            with patch('app.extract_single_pdf_text', side_effect=fake_extract):
                combined = app_module.extract_text_from_pdf_directory('some_dir')
                self.assertIn('CONTENT:', combined)
                self.assertIn('a.pdf', combined)
                self.assertIn('b.pdf', combined)

    def test_get_products_xmlrpc_app(self):
        def fake_ServerProxy(endpoint):
            class Common:
                def authenticate(self, db, username, password, d):
                    return 1

            class Models:
                def execute_kw(self, db, uid, password, model, method, args, kwargs=None):
                    return [{'id': 1, 'barcode': '123', 'name': 'Product 1', 'website_url': '/p1'}]

            if endpoint.endswith('/common'):
                return Common()
            return Models()

        with patch('app.xmlrpc.client.ServerProxy', side_effect=fake_ServerProxy):
            with app_module.app.test_request_context('/api/products', method='POST', json={'productType': 'jeans', 'gender': 'Men', 'product': 'jean'}):
                resp = app_module.get_products()
                data = resp.get_json()
                self.assertIsInstance(data, list)
                self.assertEqual(data[0]['name'], 'Product 1')


if __name__ == '__main__':
    unittest.main()
