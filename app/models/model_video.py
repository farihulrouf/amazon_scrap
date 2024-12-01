from pydantic import BaseModel
from typing import List

class VideoRequest(BaseModel):
    query: str

class VideoResponse(BaseModel):
    title: str
    url: str
