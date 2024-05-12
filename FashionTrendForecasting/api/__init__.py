from fastapi import FastAPI
from .routers import items, trends

app = FastAPI()

#API routers
app.include_router(items.router)
app.include_router(trends.router)

