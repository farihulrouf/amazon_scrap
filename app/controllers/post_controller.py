from app.models.post_model import PostCreateRequest, PostResponse
from app.utils.db import database
from bson import ObjectId
from datetime import datetime
from fastapi import HTTPException

# Access the post collection
post_collection = database.get_collection("posts")

async def create_post(post_data: PostCreateRequest) -> PostResponse:
    post = {
        "title": post_data.title,
        "category": post_data.category,
        "content": post_data.content,
        "image_urls": post_data.image_urls,
        "video_url": post_data.video_url,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
        "comments": []  # Start with an empty list of comments
    }
    
    # Insert the post into the MongoDB collection
    result = await post_collection.insert_one(post)
    post_id = result.inserted_id

    # Return a PostResponse object
    return PostResponse(
        id=str(post_id),
        title=post["title"],
        category=post["category"],
        content=post["content"],
        image_urls=post["image_urls"],
        video_url=post.get("video_url"),
        created_at=post["created_at"],
        updated_at=post["updated_at"],
        comments=post["comments"]
    )

async def get_post_by_id(post_id: str) -> PostResponse:
    # Retrieve the post from the MongoDB collection
    post = await post_collection.find_one({"_id": ObjectId(post_id)})
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return PostResponse(
        id=str(post["_id"]),
        title=post["title"],
        category=post["category"],
        content=post["content"],
        image_urls=post["image_urls"],
        video_url=post.get("video_url"),
        created_at=post["created_at"],
        updated_at=post["updated_at"],
        comments=post.get("comments", [])
    )
