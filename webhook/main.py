import sys
sys.path.append('/home/marco/Estudo/chat-bot-alb/backend')
from app.core.conv_database import store_conversation, location_contacts
from fastapi import FastAPI, Request, HTTPException


app = FastAPI()



@app.post("/webhook")
async def receive_whatsapp_message(request: Request):
    try:
        payload = await request.json()
        
        # print("Payload recebido:", json.dumps(payload, indent=4))
        
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
        else:
            print("Não foi possível extrair o número ou a mensagem.")

        return {"status": "success", "message": "Dados recebidos com sucesso", "remoteJid": remote_jid, "conversation": conversation}
    except Exception as e:
        return {"status": "error", "message": str(e)}

