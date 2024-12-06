<!-- src/components/CreatePost.vue -->
<template>
    <div>
      <h2>Create Post</h2>
      <form @submit.prevent="handleSubmit">
        <div>
          <label for="title">Title</label>
          <input type="text" id="title" v-model="title" required />
        </div>
        <div>
          <label for="content">Content</label>
          <textarea id="content" v-model="content" required></textarea>
        </div>
        <div>
          <label for="category">Category</label>
          <input type="text" id="category" v-model="category" required />
        </div>
        <div>
          <label for="pictureUrls">Picture URLs</label>
          <input type="text" id="pictureUrls" v-model="pictureUrls" />
        </div>
        <div>
          <label for="videoUrls">Video URLs</label>
          <input type="text" id="videoUrls" v-model="videoUrls" />
        </div>
        <button type="submit">Create Post</button>
      </form>
      <p v-if="error">{{ error }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        title: '',
        content: '',
        category: '',
        pictureUrls: '',
        videoUrls: '',
        error: '',
      };
    },
    created() {
      const token = localStorage.getItem('token');
      if (!token) {
        this.$router.push('/login'); // Jika tidak ada token, redirect ke login
      }
    },
    methods: {
      async handleSubmit() {
        const token = localStorage.getItem('token');
        if (!token) {
          this.error = 'You must be logged in to create a post.';
          return;
        }
  
        try {
          const response = await axios.post(
            `${process.env.VUE_APP_API_URL}/write-blog`,
            {
              title: this.title,
              content: this.content,
              user_id: 'sabilah', // Ganti sesuai dengan user_id yang sesuai
              category: this.category,
              picture_urls: this.pictureUrls.split(','),
              video_urls: this.videoUrls.split(','),
            },
            {
              headers: {
                Authorization: `Bearer ${token}`, // Sertakan token di header
              },
            }
          );
          this.$router.push('/posts'); // Redirect setelah berhasil membuat post
        } catch (err) {
          this.error = 'Failed to create the post. Please try again.';
        }
      },
    },
  };
  </script>
  