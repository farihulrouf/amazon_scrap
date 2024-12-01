from fastapi import FastAPI
from app.routers.routers import scraper_router

app = FastAPI()

# Menambahkan route dari scraper_router
app.include_router(scraper_router)
