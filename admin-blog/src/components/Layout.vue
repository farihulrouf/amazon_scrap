<template>
  <div v-if="isLoggedIn" class="flex h-screen bg-gray-100">
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

  <!-- If not logged in, redirect to login page -->
  <div v-else>
    <Login />
  </div>
</template>

<script>
import Sidebar from "./SideBar.vue"
import Navbar from  "./NavBar.vue"
import MainContent from "./MainContent.vue"; // Import MainContent.vue
import Login from "./Login.vue"; // Import the Login component

export default {
  name: "Layout",
  components: {
    Sidebar,
    Navbar,
    MainContent, // Register MainContent as a component
    Login, // Register Login as a component
  },
  data() {
    return {
      isLoggedIn: false, // Initially set to false, update based on login status
    };
  },
  created() {
    this.checkLoginStatus();
  },
  methods: {
    checkLoginStatus() {
      // Example: Check if user data is in localStorage or sessionStorage
      const user = localStorage.getItem("token"); // or use a Vuex store for state management
      this.isLoggedIn = user !== null; // If user exists, they are logged in
    },
  },
};
</script>

<style scoped>
/* Add global or specific styles for the layout */
</style>
