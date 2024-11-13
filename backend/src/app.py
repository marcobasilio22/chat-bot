from fastapi import FastAPI, WebSocket
from typing import List
from src.controllers.show_message import router as message_router
from src.controllers import login_auth as login_auth_router
from src.controllers.create_contact import router as contact_router
from src.controllers.message_chat import router as chat_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import asyncio

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Mensagem do cliente: {data}")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        manager.disconnect(websocket)

def create_app(): 
    app = FastAPI()

    app.add_middleware(CORSMiddleware,
                       allow_origins=["*"],
                       allow_credentials=True,
                       allow_methods=["*"],
                       allow_headers=["*"],)

    app.include_router(login_auth_router, prefix="/auth", tags=["auth"])
    app.include_router(message_router, prefix="/api", tags=["message"])
    app.include_router(chat_router, prefix="/api", tags=["chat"])
    app.include_router(contact_router, prefix="/api", tags=["createcontact"])

    return app

if __name__ == "__main__":
    host = "localhost"
    port = 3000

    uvicorn.run("main:app", host=host, port=port, reload=True)
