import sys
import sys
sys.path.append('/home/marco/Estudo/chat-bot-alb/backend')
import json
from fastapi import FastAPI, Request, HTTPException
from app.core.conv_database import store_conversation, location_contacts
from websocket_manager import WebSocketManager  # Certifique-se de que o caminho está correto

app = FastAPI()
websocket_manager = WebSocketManager()

@app.post("/webhook")
async def receive_whatsapp_message(request: Request):
    try:
        payload = await request.json()

        remote_jid = payload.get('data', {}).get('key', {}).get('remoteJid')
        conversation = payload.get('data', {}).get('message', {}).get('conversation')

        number = remote_jid[0:13]
        contact_ids = location_contacts(int(number))
        if not contact_ids:
            raise HTTPException(status_code=404, detail="Contact not found.")

        contact_id = contact_ids[0][0] 
        store_conversation(contact_id, conversation, 'received')

        if number and conversation:
            print(f"Número (remoteJid): {number}")
            print(f"Mensagem (conversation): {conversation}")

            # Enviar a mensagem para todos os clientes conectados via WebSocket
            await websocket_manager.broadcast(f"Mensagem recebida: {conversation}")

        else:
            print("Não foi possível extrair o número ou a mensagem.")

        return {"status": "success", "message": "Dados recebidos com sucesso", "remoteJid": remote_jid, "conversation": conversation}
    except Exception as e:
        return {"status": "error", "message": str(e)}