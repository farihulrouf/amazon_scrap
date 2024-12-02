from fastapi import APIRouter
from app.controllers.scraper_controller import get_amazon_products
from app.controllers.video_controller import fetch_videos
from app.models.model_video import VideoRequest, VideoResponse
from typing import List
scraper_router = APIRouter()




@scraper_router.post("/api/getvideos", response_model=List[VideoResponse])
async def get_videos(request: VideoRequest):
    # Call the controller function to fetch videos
    return fetch_videos(request.query)

@scraper_router.get("/api/scrape")
async def scrape():
    try:
        amazon_url = 'https://www.amazon.com/s?k=best+2024+laptop+deals&crid=1MYRVA5H2VXLY&sprefix=best+2024+laptop+%2Caps%2C465&ref=nb_sb_ss_ts-doa-p_1_17'  # Ganti dengan URL yang diinginkan
        data = get_amazon_products(amazon_url)
        return {"success": True, "data": data}
    except Exception as e:
        return {"success": False, "error": str(e)}
