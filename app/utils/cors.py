# app/utils.py

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

def add_cors_middleware(app: FastAPI, origins: list):
    """
    Fungsi untuk menambahkan CORS middleware ke aplikasi FastAPI.
    :param app: Instance aplikasi FastAPI
    :param origins: Daftar origins yang diizinkan
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,  # Mengizinkan origin yang telah disebutkan
        allow_credentials=True,
        allow_methods=["*"],  # Mengizinkan semua HTTP methods (GET, POST, dll.)
        allow_headers=["*"],  # Mengizinkan semua headers
    )
