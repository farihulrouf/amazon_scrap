<template>
  <div class="p-6 bg-gray-100 min-h-screen flex justify-center items-center">
    <div class="bg-white p-6 shadow-lg rounded-md w-full max-w-2xl">
      <h2 class="text-2xl font-semibold mb-4">Create Post</h2>
      <form @submit.prevent="handleSubmit">
        <!-- Title -->
        <div class="mb-4">
          <label for="title" class="block text-gray-700 font-medium mb-2">Title</label>
          <input
            type="text"
            id="title"
            v-model="title"
            class="w-full p-2 border rounded-md focus:outline-none focus:ring focus:ring-indigo-200"
            required
          />
        </div>

        <!-- Content -->
        <div class="mb-4">
          <label for="content" class="block text-gray-700 font-medium mb-2">Content</label>
          <editor-content
            :editor="editor"
            class="border rounded-md p-2 bg-gray-50"
          />
        </div>

        <!-- Category -->
        <div class="mb-4">
          <label for="category" class="block text-gray-700 font-medium mb-2">Category</label>
          <input
            type="text"
            id="category"
            v-model="category"
            class="w-full p-2 border rounded-md focus:outline-none focus:ring focus:ring-indigo-200"
            required
          />
        </div>

        <!-- Picture URLs -->
        <div class="mb-4">
          <label for="pictureUrls" class="block text-gray-700 font-medium mb-2">Picture URLs (comma-separated)</label>
          <input
            type="text"
            id="pictureUrls"
            v-model="pictureUrls"
            class="w-full p-2 border rounded-md focus:outline-none focus:ring focus:ring-indigo-200"
          />
        </div>

        <!-- Video URLs -->
        <div class="mb-4">
          <label for="videoUrls" class="block text-gray-700 font-medium mb-2">Video URLs (comma-separated)</label>
          <input
            type="text"
            id="videoUrls"
            v-model="videoUrls"
            class="w-full p-2 border rounded-md focus:outline-none focus:ring focus:ring-indigo-200"
          />
        </div>

        <!-- Submit Button -->
        <div class="mt-6">
          <button
            type="submit"
            class="w-full bg-indigo-500 text-white py-2 px-4 rounded-md hover:bg-indigo-600 transition"
          >
            Create Post
          </button>
        </div>
      </form>
      
      <!-- Error Message -->
      <p v-if="error" class="text-red-500 mt-4">{{ error }}</p>
    </div>
  </div>
</template>

<script>
import { Editor, EditorContent } from '@tiptap/vue-3';
import StarterKit from '@tiptap/starter-kit';
import axios from 'axios';

export default {
  name: 'CreatePost',
  components: {
    EditorContent,
  },
  data() {
    return {
      title: '',
      category: '',
      pictureUrls: '',
      videoUrls: '',
      error: '',
      editor: null, // TipTap editor instance
    };
  },
  created() {
    // Initialize the editor
    this.editor = new Editor({
      extensions: [StarterKit],
      content: '', // Initial content
    });

    // Check authentication
    const token = localStorage.getItem('token');
    if (!token) {
      this.$router.push('/login'); // Redirect to login if not authenticated
    }
  },
  beforeUnmount() {
    // Destroy the editor to free resources
    if (this.editor) {
      this.editor.destroy();
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
        const contentHTML = this.editor.getHTML(); // Get WYSIWYG content as HTML
        const response = await axios.post(
          `${process.env.VUE_APP_API_URL}/write-blog`,
          {
            title: this.title,
            content: contentHTML, // Save the WYSIWYG content
            user_id: 'sabilah', // Replace with the appropriate user_id
            category: this.category,
            picture_urls: this.pictureUrls.split(','),
            video_urls: this.videoUrls.split(','),
          },
          {
            headers: {
              Authorization: `Bearer ${token}`, // Include the token in the header
            },
          }
        );
        this.$router.push('/posts'); // Redirect to posts page on success
      } catch (err) {
        this.error = 'Failed to create the post. Please try again.';
      }
    },
  },
};
</script>

<style scoped>
/* Add any custom styles if needed */
</style>
