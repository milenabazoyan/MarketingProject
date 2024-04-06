import uvicorn
import os
from FashionTrendForecasting.api.main import app

if __name__=="__main__":
    uvicorn.run(app)