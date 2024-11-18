from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db.models.contacts import insert_data

router = APIRouter()

class Contact(BaseModel):
    name: str
    number: str

@router.post('/createcontact')
async def create_contact(contact: Contact):
    try:
        insert_data(name=contact.name, number=contact.number)
        return {"message": "Contato criado com sucesso", "contact": contact.name}
        
    except Exception as e:
        print(f"Exception occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
