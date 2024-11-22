from fastapi import FastAPI, WebSocket, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel
import uvicorn
import json

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        print(f"Cliente conectado: {websocket.client}")

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        print(f"Cliente desconectado: {websocket.client}")

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()
app = FastAPI()


class Message(BaseModel):
    message: str

class Contact(BaseModel):
    name: str
    phone: str

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Mensagem recebida do cliente: {data}")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        manager.disconnect(websocket)

@app.post("/send-webhook-message")
async def send_webhook_message_to_frontend(message: Message):
    await manager.broadcast(f"{message.message}")

@app.post("/new_contact")
async def new_contact(contact: Contact):
    
    message = {
        "type": "new_contact",
        "contact": {
            "name": contact.name,
            "phone": contact.phone
        }
    }

    await manager.broadcast(json.dumps(message))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
