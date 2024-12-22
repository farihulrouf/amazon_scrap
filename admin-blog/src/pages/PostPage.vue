<template>
    <div class="bg-gray-100 p-6">
      <div class="flex justify-center items-center">
        <div class="bg-white shadow-md rounded-lg p-8 w-full max-w-2xl">
          <create-post />
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import CreatePost from "../components/CreatePost.vue";
  
  export default {
    name: "PostPage",
    components: {
      CreatePost,
    },
  };
  </script>
  
  <style scoped>
  /* Tambahkan styling tambahan di sini jika diperlukan */
  </style>
  