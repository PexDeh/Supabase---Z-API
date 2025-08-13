import os
import httpx

class ZAPIClient:
    def __init__(self):
        self.base_url = os.getenv("ZAPI_BASE_URL")
        self.instance_id = os.getenv("ZAPI_INSTANCE_ID")
        self.token = os.getenv("ZAPI_TOKEN")
        self.dry_run = os.getenv("DRY_RUN", "true").lower() == "true"
        self.client = httpx.Client(base_url=self.base_url)

    def send_message(self, phone: str, message: str) -> bool:
        if self.dry_run:
            print(f"[DRY RUN] Enviando para {phone}: {message}")
            return True

        url = f"/instances/{self.instance_id}/token/{self.token}/send-message"
        payload = {
            "phone": phone,
            "message": message
        }

        try:
            response = self.client.post(url, json=payload)
            response.raise_for_status()
            data = response.json()
            success = data.get("success", False)
            if success:
                print(f"Mensagem enviada para {phone}")
            else:
                print(f"Falha ao enviar mensagem para {phone}: {data}")
            return success
        except Exception as e:
            print(f"Erro ao enviar mensagem para {phone}: {e}")
            return False
