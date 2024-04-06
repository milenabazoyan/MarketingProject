from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

@router.get('/trends/seasons/{season}')
def get_trends_by_season(season: str):
    return {
	  "color": "pink",
	  "style": "floral",
	  "material": "lightweight material"
	}

