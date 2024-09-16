from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.core.login_database import fetch_all_conversations

router = APIRouter()

@router.get("/login")
def login(email: str, password: str):
    try:
        user = fetch_all_conversations()
        if user and user[2] == password: 
            return JSONResponse(content={"message": "Login successful"}, status_code=200)
        raise HTTPException(status_code=401, detail="Invalid credentials")
    except Exception as e:
        print(f"Exception occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
