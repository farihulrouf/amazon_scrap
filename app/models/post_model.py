from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class PostCreateRequest(BaseModel):
    title: str
    category: str
    content: str
    image_urls: List[str]  # List of image URLs
    video_url: Optional[str] = None  # Optional video URL

class PostResponse(BaseModel):
    id: str
    title: str
    category: str
    content: str
    image_urls: List[str]
    video_url: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    comments: Optional[List[dict]] = []

    class Config:
        orm_mode = True
