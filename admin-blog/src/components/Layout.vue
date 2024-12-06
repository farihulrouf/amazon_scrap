<template>
    <div class="flex h-screen bg-gray-100">
      <!-- Sidebar -->
      <Sidebar />
  
      <!-- Main Content -->
      <div class="flex flex-col flex-1">
        <!-- Navbar -->
        <Navbar />
  
        <!-- Main Content -->
        <main class="flex-1 p-6 bg-gray-100">
          <!-- Menampilkan komponen MainContent -->
          <MainContent />
        </main>
      </div>
    </div>
  </template>
  
  <script>
  import Sidebar from "./Sidebar.vue";
  import Navbar from "./Navbar.vue";
  import MainContent from "./MainContent.vue"; // Impor MainContent.vue
  
  export default {
    name: "Layout",
    components: {
      Sidebar,
      Navbar,
      MainContent, // Daftarkan MainContent sebagai komponen
    },
  };
  </script>
  
  <style scoped>
  /* Tambahkan gaya global atau khusus untuk layout jika perlu */
  </style>
  