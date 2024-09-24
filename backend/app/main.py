from fastapi import FastAPI, WebSocket
from app.api.endpoints.show_message import router as message_router
from app.api.endpoints import login_auth
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints.message_chat import router as chat_router
from typing import List
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login_auth.router, prefix="/auth", tags=["auth"])
app.include_router(message_router, prefix="/api", tags=["message"])
app.include_router(chat_router, prefix="/api", tags=["chat"])

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

def console_input():
    while True:
        message = input("Digite uma mensagem para enviar ao front: ")
        asyncio.run(manager.broadcast(message))

if __name__ == "__main__":
    threading.Thread(target=console_input).start()
    uvicorn.run(app, host="0.0.0.0", port=8000)
