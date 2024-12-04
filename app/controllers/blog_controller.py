from app.utils.db import blogs_collection

async def create_blog(title: str, content: str):
    blog = {"title": title, "content": content}
    await blogs_collection.insert_one(blog)
    return {"message": "Blog created successfully"}
