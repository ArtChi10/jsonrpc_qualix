from django.test import TestCase
from jsonrpc_client.rpc_client import JsonRpcClient
from django.conf import settings
import json

class JsonRpcClientTests(TestCase):
    def setUp(self):
        self.client = JsonRpcClient(settings.JSONRPC_ENDPOINT)

    def test_auth_check(self):
        response = self.client.call("auth.check")
        self.assertIn("result", response, "Ответ должен содержать ключ 'result'")
        self.assertNotIn("error", response, "Ответ не должен содержать ключ 'error'")

    def test_invalid_method(self):
        response = self.client.call("invalid.method")
        self.assertIn("error", response, "Ответ должен содержать ключ 'error'")

    def test_invalid_json_params(self):
        response = self.client.call("auth.check", params="invalid_json")
        self.assertIn("error", response, "Ответ должен содержать ключ 'error'")

class JsonRpcViewTests(TestCase):
    def test_get_request_renders_form(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<form")

    def test_post_request_valid_method(self):
        response = self.client.post("/", {"method": "auth.check", "params": "{}"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("jsonrpc", response.json(), "Ответ должен содержать jsonrpc")

    def test_post_request_invalid_json(self):
        response = self.client.post("/", {"method": "auth.check", "params": "{invalid"})
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json(), "Должно быть сообщение об ошибке")
