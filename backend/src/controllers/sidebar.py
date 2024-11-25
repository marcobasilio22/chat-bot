from fastapi import APIRouter, HTTPException
from db.configs.connection import get_connection
from db.models.contacts import (
    order_contacts,
    search_contacts
                                )

from pydantic import BaseModel

router = APIRouter()


@router.get("/contact/order")
async def get_messages():
    order = order_contacts()
    return {"order": order}

@router.get("/contact/search")
async def get_search(name: str):
    search = search_contacts(name=name)
    return {"result": search}