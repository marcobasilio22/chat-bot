import subprocess
import time
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from controllers.show_message import router as message_router
from controllers.login_auth import router as login_auth_router
from controllers.create_contact import router as contact_router
from controllers.message_chat import router as chat_router
from controllers.sidebar import router as sidebar_router

app = FastAPI()

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
    app.include_router(sidebar_router, prefix="/api", tags=["sidebar_router"])

    return app

app = create_app()

def run_uvicorn_app():
    subprocess.Popen(["uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "8000"])

def run_webhook():
    subprocess.Popen(["uvicorn", "connectors.webhook:app", "--reload", "--host", "0.0.0.0", "--port", "8001"])

def run_websocket():
    subprocess.Popen(["python3", "connectors/websocket_server.py"])

if __name__ == "__main__":
    print("Iniciando os serviços...")

    run_uvicorn_app()
    time.sleep(2) 

    run_webhook()
    time.sleep(2)

    run_websocket()

    print("Todos os serviços estão rodando.")
