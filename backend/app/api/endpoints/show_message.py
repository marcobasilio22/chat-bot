from fastapi import APIRouter, HTTPException
from app.core.database import get_connection
from app.core.conv_database import location_contacts
from app.core.contacts import show_contacts, last_message


router = APIRouter()

def get_messages_from_db(number: str):
    connection = get_connection()
    if not connection:
        return []

    contact_ids = location_contacts(int(number))
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