// src/api/api.js
import axios from 'axios';

const API_URL = "http://localhost:8000/api"// Mengambil URL API dari .env
//console.log("check",process.env); // Memeriksa semua variabel lingkungan
//console.log("API URL:", process.env.VUE_APP_API_URL);

// API untuk login
export const login = async (username, password) => {
  console.log("API URL:", API_URL); // Cek apakah URL API sudah benar
  try {
    const response = await axios.post(`${API_URL}/login`, {
      username,
      password,
    });
    return response.data.token; // Kembalikan token JWT
  } catch (error) {
    console.error(error); // Tambahkan error handling yang lebih lengkap
    throw new Error('Login failed. Please check your credentials.');
  }
};

// API untuk membuat blog post
export const createBlogPost = async (title, content, userId, category, pictureUrls, videoUrls, token) => {
  try {
    const response = await axios.post(
      `${API_URL}/write-blog`,
      {
        title,
        content,
        user_id: userId,
        category,
        picture_urls: pictureUrls.split(','),
        video_urls: videoUrls.split(','),
      },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    return response.data; // Kembalikan data respons blog post
  } catch (error) {
    throw new Error('Failed to create blog post. Please try again.');
  }
};
