<template>
    <div class="max-w-screen-xl mx-auto p-4">
      <!-- Title input field -->
      <input
        v-model="title"
        type="text"
        class="border border-gray-300 p-2 mb-4 w-full"
        placeholder="Enter post title"
      />
      
      <!-- Category input field -->
      <input
        v-model="category"
        type="text"
        class="border border-gray-300 p-2 mb-4 w-full"
        placeholder="Enter post category"
      />
      
      <!-- Image URLs input field -->
      <input
        v-model="imageUrls"
        type="text"
        class="border border-gray-300 p-2 mb-4 w-full"
        placeholder="Enter image URLs (comma-separated)"
      />
      
      <!-- Quill Editor -->
      <div ref="editor" class="quill-editor"></div>
      
      <!-- Submit Button -->
      <button @click="submitPost" class="mt-4 p-2 bg-blue-500 text-white rounded">
        Submit Post
      </button>
    </div>
  </template>
  
  <script>
  import { ref, onMounted, onBeforeUnmount } from 'vue';
  import Quill from 'quill';
  import axios from 'axios';
  import 'quill/dist/quill.snow.css'; // Import Quill's default theme CSS
  
  export default {
    name: 'QuillEditor',
    setup() {
      const editor = ref(null);
      const title = ref('');
      const category = ref('');
      const imageUrls = ref('');
      let quillInstance = null;
  
      // Inisialisasi editor Quill pada mounted
      onMounted(() => {
        quillInstance = new Quill(editor.value, {
          theme: 'snow', // Gunakan tema 'snow' untuk editor
          modules: {
            toolbar: [
              [{ 'header': '1' }, { 'header': '2' }, { 'font': [] }],
              [{ 'list': 'ordered' }, { 'list': 'bullet' }],
              ['bold', 'italic', 'underline', 'strike'],
              ['blockquote', 'code-block'],
              [{ 'align': [] }],
              ['link'],
              ['image'],
              [{ 'color': [] }, { 'background': [] }],
              [{ 'script': 'sub' }, { 'script': 'super' }],
              [{ 'indent': '-1' }, { 'indent': '+1' }],
              [{ 'direction': 'rtl' }],
              ['clean']
            ]
          }
        });
      });
  
      // Bersihkan instance Quill saat komponen di-unmount
      onBeforeUnmount(() => {
        if (quillInstance) {
          quillInstance = null;
        }
      });
  
      // Fungsi untuk submit post ke API
      const submitPost = async () => {
        const content = quillInstance.root.innerHTML; // Ambil konten HTML dari editor
        const images = imageUrls.value.split(',').map(url => url.trim()); // Convert comma-separated URLs to array
  
        try {
          // Kirim data ke API menggunakan POST request
          const response = await axios.post(
            'https://bf38-103-242-105-145.ngrok-free.app/api/posts',
            {
              title: title.value,
              category: category.value,
              content: content,
              image_urls: images, // Send image URLs as an array
            },
            {
              headers: {
                'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmYXJpaGxyb3VmIiwicm9sZSI6ImFkbWluIn0.dZy4xN_tnKfaOBYQgwjNy_e7vXbYz3nPcrzXgUGAPbA'
              }
            }
          );
          console.log('Post submitted:', response.data);
        } catch (error) {
          console.error('Error submitting post:', error);
        }
      };
  
      return { editor, submitPost, title, category, imageUrls };
    }
  };
  </script>
  
  <style scoped>
  .quill-editor {
    height: 500px;
    border: 1px solid #ccc;
  }
  </style>
  