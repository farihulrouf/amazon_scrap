from app.models.blog_model import CreateBlogRequest, CommentRequest
from app.utils.db import blogs_collection, comments_collection
from app.models.blog_model import BlogResponse
from typing import Optional, List

async def create_blog(blog_data: CreateBlogRequest):
    blog = {
        "title": blog_data.title,
        "content": blog_data.content,
        "user_id": blog_data.user_id,
        "category": blog_data.category,
        "picture_urls": blog_data.picture_urls or [],
        "video_urls": blog_data.video_urls or [],
        "comments": []  # Daftar komentar kosong saat blog dibuat
    }
    result = await blogs_collection.insert_one(blog)
    blog_id = str(result.inserted_id)
    return BlogResponse(id=blog_id, **blog)

async def add_comment_to_blog(blog_id: str, user_id: str, comment_data: CommentRequest):
    # Memasukkan komentar ke dalam koleksi comments dan menambahkannya ke blog
    comment = {
        "blog_id": blog_id,
        "user_id": user_id,
        "content": comment_data.content
    }
    # Menyimpan komentar di koleksi komentar
    result = await comments_collection.insert_one(comment)
    comment_id = str(result.inserted_id)
    
    # Menambahkan komentar ke dalam blog yang bersangkutan
    await blogs_collection.update_one(
        {"_id": blog_id},
        {"$push": {"comments": {"comment_id": comment_id, "content": comment_data.content, "user_id": user_id}}}
    )
    return {"message": "Comment added successfully", "comment_id": comment_id}
