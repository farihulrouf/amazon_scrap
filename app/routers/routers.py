from fastapi import APIRouter
from app.controllers.scraper_controller import get_amazon_products

scraper_router = APIRouter()

@scraper_router.get("/scrape")
async def scrape():
    try:
        amazon_url = 'https://www.amazon.com/s?k=laptop'  # Ganti dengan URL yang diinginkan
        data = get_amazon_products(amazon_url)
        return {"success": True, "data": data}
    except Exception as e:
        return {"success": False, "error": str(e)}
