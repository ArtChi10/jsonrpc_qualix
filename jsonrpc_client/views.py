from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from .rpc_client import JsonRpcClient
from django.conf import settings
import json
import logging

logger = logging.getLogger(__name__)

class JsonRpcView(View):
    def get(self, request):
        return render(request, "jsonrpc_client/index.html")

    def post(self, request):
        method = request.POST.get("method", "").strip()
        params = request.POST.get("params", "{}").strip()

        logger.info(f"Получен JSON-RPC запрос: метод={method}, параметры={params}")

        try:
            params = json.loads(params)  # Проверяем, что JSON корректный
        except json.JSONDecodeError:
            logger.warning("Ошибка: передан некорректный JSON")
            return JsonResponse({"error": "Invalid JSON format in parameters"}, status=400)

        client = JsonRpcClient(settings.JSONRPC_ENDPOINT)
        response = client.call(method, params)

        logger.info(f"Ответ JSON-RPC: {response}")
        return JsonResponse(response)
