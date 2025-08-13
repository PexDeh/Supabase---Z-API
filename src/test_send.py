import os
import httpx
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("ZAPI_TOKEN")
INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
BASE_URL = f"https://api.z-api.io/instances/{INSTANCE_ID}"

def send_message(phone, message):
    url = f"{BASE_URL}/send-text"
    headers = {
        "Content-Type": "application/json",
        "Client-Token": TOKEN
    }
    payload = {
        "phone": phone,
        "message": message
    }
    with httpx.Client() as client:
        response = client.post(url, json=payload, headers=headers)
        print("Status:", response.status_code)
        print("Response:", response.text)

if __name__ == "__main__":
    send_message("5511945077750", "Olá, isso é um teste.")
