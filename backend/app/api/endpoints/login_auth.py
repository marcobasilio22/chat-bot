# backend/app/api/endpoints/login_auth.py

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.core.database import connection

router = APIRouter()

@router.get("/login")
def login(email: str, password: str):
    try:
        query = connection()
        if query:
            for user in query:
                if user[1] == email and user[2] == password:
                    return JSONResponse(content={"message": "Login successful"}, status_code=200)
        raise HTTPException(status_code=401, detail="Invalid credentials")
    except Exception as e:
        print(f"Exception occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
