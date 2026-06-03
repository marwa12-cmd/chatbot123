import unittest
import json

import app as app_module


class AppTests(unittest.TestCase):
    def setUp(self):
        # Ensure a known language state
        app_module.lan = "français"

    def test_greeting_response(self):
        with app_module.app.test_request_context('/', method='POST', data={'user_input': 'Hello'}):
            resp = app_module.send_message()
            data = json.loads(resp.get_data(as_text=True))
            self.assertIn('bot_response', data)
            self.assertEqual(data['product_mentioned'], "No product")
            self.assertIn('Hi', data['bot_response'])

    def test_product_detection_french(self):
        app_module.lan = "français"
        with app_module.app.test_request_context('/', method='POST', data={'user_input': 'Je cherche des jeans'}):
            resp = app_module.send_message()
            data = json.loads(resp.get_data(as_text=True))
            self.assertEqual(data['product_mentioned'], 'jeans')
            self.assertIn('Pour mieux vous aider', data['bot_response'])

    def test_prompts_messages(self):
        app_module.lan = "anglais"
        resp = app_module.get_gender_prompt()
        data = resp.get_json()
        self.assertIn('Which category', data['message'])
        resp = app_module.get_price_prompt()
        data = resp.get_json()
        self.assertIn('Do you want to set a price', data['message'])


if __name__ == '__main__':
    unittest.main()
