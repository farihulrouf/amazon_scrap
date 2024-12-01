# YouTube Video Fetcher & Scrapre amazon

This project allows you to fetch and display YouTube videos based on a search query. It utilizes the YouTube Data API, FastAPI for the backend, and provides a RESTful endpoint to search for videos related to any query.

## Features

- **Fetch YouTube videos**: The API connects to the YouTube Data API to retrieve video results based on the query provided.
- **FastAPI Backend**: The backend is built using FastAPI, providing a fast and scalable framework for handling requests.
- **Error Handling**: If no videos are found for the given query, the API will respond with a 404 error.

## Requirements

Before running the project, you need to install the required dependencies.

### Steps to Run the Project

1. **Clone the repository**:
    ```bash
    git clone https://github.com/farihulrouf/amazon_scrap
    ```

2. **Navigate into the project directory**:
    ```bash
    cd <project-name>
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    uvicorn app.main:app --reload
    ```

### Project Structure

The project is organized into the following main components:

- **`app/`**: Contains the main application code.
  - **`controllers/`**: Handles the business logic for fetching videos and any other operations.
  - **`models/`**: Defines the Pydantic models used for request and response validation.
  - **`routers/`**: Defines the FastAPI routes and endpoints.
  - **`main.py`**: The entry point of the FastAPI application.

## API Endpoints

### `POST /api/getvideos`
- **Description**: Fetches a list of YouTube videos based on the search query.
- **Request Body**:
    ```json
    {
        "query": "your search query"
    }
    ```
- **Response**:
    ```json
    [
        {
            "title": "Video Title",
            "url": "https://www.youtube.com/watch?v=video_id"
        },
        ...
    ]
    ```
- **Error Response**:
    - If no videos are found for the query:
      ```json
      {
          "detail": "No videos found for the given query."
      }
      ```

## Environment Variables

The project requires the following environment variables to function properly:

- **`YOUTUBE_API_KEY`**: Your YouTube Data API v3 key.

You can store these in a `.env` file in the project root.

## Example `.env` File

```env
YOUTUBE_API_KEY=your_youtube_api_key
