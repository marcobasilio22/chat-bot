from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from app.codes.send_message import ApiRequest
from app.core.conv_database import store_conversation, location_contacts
from app.core.contact_database import resgister_contact


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
        
        resgister_contact('paulo', request.number)
        
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