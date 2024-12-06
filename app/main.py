# app/main.py

from fastapi import FastAPI
from app.routers.routers import scraper_router
from app.utils.cors import add_cors_middleware  # Mengimpor fungsi add_cors_middleware

# Membuat instance aplikasi FastAPI
app = FastAPI()

# Daftar origins yang diizinkan
origins = [
    "http://localhost:5173",  # Ganti dengan origin frontend Anda
    # Anda dapat menambahkan origin lain jika diperlukan
]

# Menambahkan CORS middleware menggunakan fungsi dari utils.py
add_cors_middleware(app, origins)

# Menambahkan route dari scraper_router
app.include_router(scraper_router)
