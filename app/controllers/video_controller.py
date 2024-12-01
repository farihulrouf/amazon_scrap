from typing import List
import requests
from app.models.model_video import VideoRequest, VideoResponse
from fastapi import HTTPException
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variables
API_KEY = os.getenv('API_YOUTUBE_KEY')
YOUTUBE_API_URL = os.getenv('YOUTUBE_API_URL')

def fetch_videos(query: str) -> List[VideoResponse]:
    params = {
        'part': 'snippet',
        'q': query,
        'key': API_KEY,
        'maxResults': 5  # Set the number of results to fetch
    }

    # Request data from YouTube API
    response = requests.get(YOUTUBE_API_URL, params=params)
    data = response.json()

    # Handle case when no items are found
    if 'items' not in data or len(data['items']) == 0:
        raise HTTPException(status_code=404, detail="No videos found for the given query.")

    # Construct the video response
    videos = [
        VideoResponse(title=item['snippet']['title'], url=f"https://www.youtube.com/watch?v={item['id']['videoId']}")
        for item in data['items'] if 'videoId' in item['id']
    ]

    return videos
