// src/api/api.js
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL; // Mengambil URL API dari .env

// API untuk login
export const login = async (email, password) => {
  console.log("email and password", email, password)
  console.log(API_URL)
  try {
    const response = await axios.post(`${API_URL}/login`, {
      email,
      password,
    });
    return response.data.token; // Kembalikan token JWT
  } catch (error) {
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
