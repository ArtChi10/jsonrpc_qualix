import json
import ssl
import urllib.request
import tempfile
import os
import logging
from django.conf import settings

logger = logging.getLogger(__name__)

class JsonRpcClient:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)

        self.cert_file = tempfile.NamedTemporaryFile(delete=False)
        self.cert_file.write(settings.CLIENT_CERT.encode())
        self.cert_file.close()

        self.key_file = tempfile.NamedTemporaryFile(delete=False)
        self.key_file.write(settings.CLIENT_KEY.encode())
        self.key_file.close()

        try:
            self.context.load_cert_chain(certfile=self.cert_file.name, keyfile=self.key_file.name)
            logger.info("Сертификат и ключ загружены успешно")
        except ssl.SSLError as e:
            logger.error(f"Ошибка загрузки сертификатов: {e}")
            raise RuntimeError(f"Ошибка загрузки сертификатов: {e}")

        self.context.check_hostname = False
        self.context.verify_mode = ssl.CERT_NONE

    def call(self, method, params=None):
        request_data = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params or {},
            "id": 1,
        }
        data = json.dumps(request_data).encode("utf-8")

        logger.info(f"Отправка JSON-RPC запроса: {request_data}")

        req = urllib.request.Request(
            self.endpoint, data=data, headers={"Content-Type": "application/json"}
        )

        try:
            with urllib.request.urlopen(req, context=self.context) as response:
                response_data = json.loads(response.read().decode("utf-8"))
                logger.info(f"Ответ от сервера: {response_data}")
                return response_data
        except urllib.error.HTTPError as e:
            logger.error(f"HTTP Error {e.code}: {e.reason}")
            return {"error": f"HTTP Error: {e.code} {e.reason}"}
        except urllib.error.URLError as e:
            logger.error(f"URL Error: {e.reason}")
            return {"error": f"URL Error: {e.reason}"}
        except Exception as e:
            logger.exception(f"Неизвестная ошибка: {e}")
            return {"error": str(e)}
        finally:
            self.cleanup()

    def cleanup(self):
        os.remove(self.cert_file.name)
        os.remove(self.key_file.name)
        logger.info("Временные файлы удалены")
