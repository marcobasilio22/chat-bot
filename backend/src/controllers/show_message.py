from fastapi import APIRouter, HTTPException
from db.configs.connection import get_connection
from db.models.conversations import last_message
from db.models.contacts import (
    location_contacts,
    show_contacts,
    rename_contact_to_number, 
    delete_messages_by_number, 
    delete_contact_and_messages)

from pydantic import BaseModel

router = APIRouter()

class RenameContact(BaseModel):
    number: str
    new_name: str
    
def get_messages_from_db(number: str):
    connection = get_connection()
    if not connection:
        return []

    contact_ids = location_contacts(str(number))
    if not contact_ids:
        raise HTTPException(status_code=404, detail="Contact not found.")
    
    contact_id = contact_ids[0][0] 
    
    cursor = connection.cursor()

    query = """
    SELECT message, type_message, TO_CHAR(date_message, 'HH24:MI') as time
    FROM conversations
    WHERE customer_id = %s
    """
    
    try:
        cursor.execute(query, (contact_id,))
        
        messages = []
        for message, type_message, time in cursor.fetchall():
            messages.append({
                "id": len(messages) + 1,
                "text": message,
                "time": time,
                "sent": type_message == 'send'
            })
    
    except Exception as e:
        print(f"Erro ao executar consulta: {e}")
        return []
    
    cursor.close()
    connection.close()
    
    return messages

@router.get("/messages/{number}")
async def get_messages(number: str):
    messages = get_messages_from_db(number)
    return {"messages": messages}

@router.get("/listcontact")
async def list_contacts():
    contacts = show_contacts()
    return {"data": contacts}

@router.get("/lastmessage")
async def get_last_messages():
    messages = last_message()
    return {"data": messages}

@router.post("/renamecontact")
async def post_rename_contact_to_number(contact: RenameContact):
    messages = rename_contact_to_number(contact.number, contact.new_name)
    
    if 'error' in messages:
        raise HTTPException(status_code=400, detail=messages['error'])
    
    return {"data": messages}

@router.delete("/delete_messages/{number}")
async def delete_messages_endpoint(number: str):
    response = delete_messages_by_number(number)
    if "error" in response:
        raise HTTPException(status_code=500, detail=response["error"])
    return response

@router.delete("/delete_contact/{number}")
async def delete_contact_endpoint(number: str):
    response = delete_contact_and_messages(number)
    if "error" in response:
        raise HTTPException(status_code=500, detail=response["error"])
    return response
