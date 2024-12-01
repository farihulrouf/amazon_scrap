from fastapi import APIRouter
from app.controllers.scraper_controller import get_amazon_products

scraper_router = APIRouter()

@scraper_router.get("/scrape")
async def scrape():
    try:
        amazon_url = 'https://www.amazon.com/s?k=best+2024+laptop+deals&crid=CG1KHU2C4WB2&sprefix=best+2024+laptop%2Caps%2C945&ref=nb_sb_ss_ts-doa-p_1_16'  # Ganti dengan URL yang diinginkan
        data = get_amazon_products(amazon_url)
        return {"success": True, "data": data}
    except Exception as e:
        return {"success": False, "error": str(e)}
