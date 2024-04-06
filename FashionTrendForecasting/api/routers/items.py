from fastapi import APIRouter
from pydantic import BaseModel


class ItemDTO(BaseModel):
    name: str
    category: str
    material: str
    style: str
    color: str

class ItemUpdateDTO(BaseModel):
    name: str | None = None
    category: str | None = None
    material: str | None = None
    style: str | None = None
    color: str | None = None


router = APIRouter()

@router.post('/items/')   
def create_item(item: ItemDTO):
    '''
    Calling DB Developer to insert an item
    '''
    return item


@router.put('/items/{item_id}')
def update_item(item_id: int, request:ItemUpdateDTO):
    '''
    calling DB Developer to update item by ID with given request
    '''

