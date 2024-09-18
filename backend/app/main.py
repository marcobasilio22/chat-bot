from fastapi import FastAPI
from app.api.endpoints.show_message import router as message_router
from app.api.endpoints import login_auth
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints.message_chat import router as chat_router

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
