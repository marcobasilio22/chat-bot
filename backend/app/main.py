from fastapi import FastAPI
from app.api.endpoints.show_message import router as message_router
from app.api.endpoints import login_auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login_auth.router, prefix="/auth", tags=["auth"])
app.include_router(message_router, prefix="/api", tags=["messages"])
