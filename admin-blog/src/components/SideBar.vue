<template>
  <div class="flex flex-col h-screen w-64 bg-gray-800 text-white">
    <div class="p-4 text-lg font-bold border-b border-gray-700">
      Sidebar Title
    </div>
    <nav class="flex-1 p-4">
      <ul>
        <li v-for="(item, index) in menuItems" :key="index" class="mb-2">
          <a href="#" class="block px-4 py-2 rounded hover:bg-gray-700">
            {{ item }}
          </a>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
export default {
  name: "Sidebar",
  data() {
    return {
      menuItems: ["Dashboard", "Post", "Settings", "Logout"],
    };
  },
};
</script>
