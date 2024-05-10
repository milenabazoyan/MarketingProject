from fastapi import APIRouter, HTTPException
from FashionTrendForecasting.api.routers.constants.season import Season
from FashionTrendForecasting.data_processing.sql_interactions import Interactions
from fastapi.responses import JSONResponse
import json
from FashionTrendForecasting.api.utilities.logger import logger
from FashionTrendForecasting.api.utilities.dao import interactions


router = APIRouter()

@router.get('/trends/seasons/{season}')
def get_trends_by_season(season: str):
	try:
		season = Season(season)
	except ValueError:
		raise HTTPException(status_code=400, detail="Invalid season")
	logger.info(f"Finding Most Trending Item of Season = {season}")
	items_entity = interactions.get_top_n_items_with_highest_sales(season.value, 1)
	items_json = items_entity.to_json(orient='records')
	items_dto = json.loads(items_json)
	if items_dto:  
		return JSONResponse(content=items_dto[0])
	else:
		return JSONResponse(content={})  
