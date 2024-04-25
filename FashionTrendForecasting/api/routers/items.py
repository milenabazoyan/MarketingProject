from fastapi import APIRouter
from pydantic import BaseModel
from FashionTrendForecasting.data_processing.sql_interactions import Interactions
import pandas as pd
from fastapi.responses import JSONResponse
import json


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

@router.get('/items/seasons/{season}')
def get_items_by_season(season: str):
    items_entity = Interactions.get_seasonal_trend_items('Spring')
    items_json = items_entity.to_json(orient='records')
    print(items_json)
    items_dto = json.loads(items_json)
    return JSONResponse(content=items_dto)
