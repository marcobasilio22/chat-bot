from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from src.controllers.send_message import ApiRequest
from src.db.models.conversations import store_conversation
from src.db.models.contacts import location_contacts

router = APIRouter()

class TextMessage(BaseModel):
    text: str

class MessageRequest(BaseModel):
    number: str
    textMessage: TextMessage

@router.post("/chat")
async def message(request: MessageRequest):
    try:
        api_request = ApiRequest()
        response_data = api_request.send_messages(request.number, request.textMessage.text)
        
        contact_ids = location_contacts(int(request.number))
        if not contact_ids:
            raise HTTPException(status_code=404, detail="Contact not found.")
        
        contact_id = contact_ids[0][0] 
        
        store_conversation(contact_id, request.textMessage.text, "send")
        return JSONResponse(content={"message": "Message sent successfully!", "response": response_data}, status_code=200)

    except HTTPException as e:
        print(f"HTTPException: {e}")
        raise e
    except Exception as e:
        print(f"Exception: {e}")
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")