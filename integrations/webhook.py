import sys
import requests
sys.path.append('/home/marco/Estudo/chat-bot-alb/backend')

from fastapi import FastAPI, Request, HTTPException
from app.core.conv_database import store_conversation, location_contacts
from app.core.register_contact import insert_data


app = FastAPI()

@app.post("/webhook")
async def receive_whatsapp_message(request: Request):
    try:
        payload = await request.json()

        remote_jid = payload.get('data', {}).get('key', {}).get('remoteJid')
        conversation = payload.get('data', {}).get('message', {}).get('conversation')

        number = remote_jid[0:13]
        contact_ids = location_contacts(int(number))
        if not contact_ids:
            print(f"Número (remoteJid): {number}")
            print(f"Mensagem (conversation): {conversation}")
            insert_data(number, number, False)
            
            request.post('http://localhost:8765/show-contact', number, number)

        contact_id = contact_ids[0][0]
        store_conversation(contact_id, conversation, 'received')

        if number and conversation:
            print(f"Número (remoteJid): {number}")
            print(f"Mensagem (conversation): {conversation}")

            requests.post('http://localhost:8765/send-webhook-message', json={"message": conversation})

        else:
            print("Não foi possível extrair o número ou a mensagem.")

        return {"status": "success", "message": "Dados recebidos com sucesso", "remoteJid": remote_jid, "conversation": conversation}
    except Exception as e:
        return {"status": "error", "message": str(e)}
