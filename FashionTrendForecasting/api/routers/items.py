from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
from pydantic import BaseModel
from FashionTrendForecasting.api.routers.constants.season import Season
from fastapi.responses import JSONResponse
from FashionTrendForecasting.api.utilities.logger import logger
from FashionTrendForecasting.api.utilities.dao import crud_obj, interactions

class ItemDTO(BaseModel):
    name: str
    category: str
    material: str
    style: str
    color: str
    picture_id: int

class ItemUpdateDTO(BaseModel):
    name: str | None = None
    category: str | None = None
    material: str | None = None
    style: str | None = None
    color: str | None = None
    picture_id: int | None = None


router = APIRouter()

@router.post('/items/')
def create_item(request_body: dict):
    try:
        item_dto = ItemDTO(**request_body)
        item_dict = item_dto.dict()
        logger.info(f"Insertin New Item = {item_dict}")
        item = crud_obj.add_item_with_details(item_dict)
        return item
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete('/items/{id}')
def delete_by_id(id:int):
    logger.info(f"Deleting Item With ID = {id}")
    is_deleted=crud_obj.delete_item(id)
    if is_deleted is False:
        raise HTTPException(status_code=404, detail=f"Item with ID={id} not found")


@router.put('/items/{id}')
def update_item(id: int, request_body: dict):
    item_dto = ItemUpdateDTO(**request_body)
    item_dict = item_dto.dict(exclude_unset=True)
    logger.info(f"Updating Item With ID = {id} to have {item_dict}")
    is_updated=crud_obj.update_item(id, item_dict)
    if is_updated is False:
        raise HTTPException(status_code=404, detail=f"Item with ID={id} not found")


@router.get('/items/{id}')
def get_item_by_id(id: int):
    logger.info(f"Finding Item With ID = {id}")
    item = crud_obj.get_item_by_id(id)
    if item is None:
       raise HTTPException(status_code=404, detail=f"Item with ID={id} not found")
    return item


@router.get('/items/seasons/{season}')
def get_items_by_season(season: str, limit: int = 0, offset: int = 0):
    try:
        season = Season(season)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid season")
    logger.info(f"Finding Items for Season={season}, limit={limit}, offset={offset}")
    items = interactions.get_seasonal_trend_items_top_n_offset_k(season.value, limit+1, offset)
    if len(items)>limit:
        next_page=f'http://127.0.0.1:8000/items/seasons/{season.value}?limit={limit}&offset={offset + limit}'
        items=items[:limit]
    else:
        next_page=None
    response={ 
        "items": items,
        "next_page": next_page
    }
    return JSONResponse(content=response)

