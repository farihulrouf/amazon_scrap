from fastapi import APIRouter, Depends
from app.controllers.scraper_controller import get_amazon_products
from app.controllers.video_controller import fetch_videos
from app.models.model_video import VideoRequest, VideoResponse
from app.controllers.auth_controller import authenticate_user, require_admin, register_user, RegisterRequest
from app.controllers.blog_controller import create_blog, add_comment_to_blog
from app.models.user_model import LoginRequest, Token, UserResponse
from app.models.blog_model import BlogResponse, CommentRequest, CreateBlogRequest

from typing import List

# Buat router
scraper_router = APIRouter()

# Endpoint login
@scraper_router.post("/api/login", response_model=Token)
async def login(data: LoginRequest):
    return await authenticate_user(data)


@scraper_router.post("/api/register", response_model=UserResponse)
async def register(data: RegisterRequest):
    # Panggil controller untuk registrasi
    return await register_user(data)


@scraper_router.post("/api/write-blog", dependencies=[Depends(require_admin)], response_model=BlogResponse)
async def write_blog(blog_data: CreateBlogRequest):
    return await create_blog(blog_data)

# Endpoint untuk membuat komentar pada blog
@scraper_router.post("/api/blogs/{blog_id}/comments", response_model=dict)
async def add_comment(blog_id: str, comment: CommentRequest, token: Token = Depends(authenticate_user)):
    # Menambahkan komentar ke blog
    return await add_comment_to_blog(blog_id, token.sub, comment.content)

# Endpoint untuk mendapatkan video
@scraper_router.post("/api/getvideos", response_model=List[VideoResponse])
async def get_videos(request: VideoRequest):
    return fetch_videos(request.query)

# Endpoint untuk scraping data Amazon
@scraper_router.get("/api/scrape")
async def scrape():
    try:
        amazon_url = 'https://www.amazon.com/s?k=best+2024+laptop+deals&crid=1MYRVA5H2VXLY&sprefix=best+2024+laptop+%2Caps%2C465&ref=nb_sb_ss_ts-doa-p_1_17'
        data = get_amazon_products(amazon_url)
        return {"success": True, "data": data}
    except Exception as e:
        return {"success": False, "error": str(e)}
