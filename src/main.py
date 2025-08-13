from services.zapi_client import ZAPIClient


import os
from dotenv import load_dotenv
from supabase import create_client
from services.zapi_client import ZAPIClient

def main():
    load_dotenv()
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_ANON_KEY")
    max_messages = int(os.getenv("MAX_MESSAGES", "3"))

    supabase = create_client(supabase_url, supabase_key)
    zapi = ZAPIClient()

    response = supabase.table("contacts").select("*").limit(max_messages).execute()
    contacts = response.data if hasattr(response, 'data') else response

    if not contacts:
        print("Nenhum contato para enviar mensagem.")
        return

    for contact in contacts:
        name = contact.get("name")
        phone = ''.join(filter(str.isdigit, contact.get("phone", "")))

        message = f"Olá {name}, tudo bem com você?"
        zapi.send_message(phone, message)

if __name__ == "__main__":
    main()
