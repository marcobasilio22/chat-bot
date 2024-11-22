import sys
import requests
from fastapi import FastAPI, Request, HTTPException
from db.models.contacts import location_contacts, insert_data
from db.models.conversations import store_conversation

app = FastAPI()

@app.post("/webhook")
async def receive_whatsapp_message(request: Request):
    try:
        payload = await request.json()
        
        remote_jid = payload.get('data', {}).get('key', {}).get('remoteJid')
        conversation = payload.get('data', {}).get('message', {}).get('conversation')

        number = remote_jid[0:13]
        contact_ids = location_contacts(int(number))

        if contact_ids == []: 
            register = insert_data(number, number)
            store_conversation(register, conversation, 'received')

            contact_data = {
                "name": f"{number}",
                "phone": number
            }
            response = requests.post(
                'http://localhost:8002/new_contact', 
                json=contact_data
            )

            if response.status_code == 200:
                print("Contato enviado ao WebSocket com sucesso!")
            else:
                print(f"Erro ao enviar contato ao WebSocket: {response.status_code} - {response.text}")


        contact_id =  [0][0]
        store_conversation(contact_id, conversation, 'received')

        if number and conversation:
            requests.post('http://localhost:8002/send-webhook-message', json={"message": conversation})

        else:
            print("Não foi possível extrair o número ou a mensagem.")

        return {"status": "success", "message": "Dados recebidos com sucesso", "remoteJid": remote_jid, "conversation": conversation}
    except Exception as e:
        return {"status": "error", "message": str(e)}
