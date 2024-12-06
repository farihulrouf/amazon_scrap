from pydantic import BaseModel
from typing import List, Optional

class CommentRequest(BaseModel):
    content: str

class CommentResponse(BaseModel):
    comment_id: str
    user_id: str
    content: str

class Blog(BaseModel):
    title: str
    content: str
    user_id: str
    category: str
    picture_urls: Optional[List[str]] = []
    video_urls: Optional[List[str]] = []
    comments: List[CommentResponse] = []

class BlogResponse(BaseModel):
    id: str
    title: str
    content: str
    user_id: str
    category: str
    picture_urls: Optional[List[str]] = []
    video_urls: Optional[List[str]] = []
    comments: List[CommentResponse] = []

class CreateBlogRequest(BaseModel):
    title: str
    content: str
    user_id: str
    category: str
    picture_urls: Optional[List[str]] = []
    video_urls: Optional[List[str]] = []
