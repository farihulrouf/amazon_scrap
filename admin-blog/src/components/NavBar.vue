<template>
  <div class="w-full bg-teal-800 text-white shadow">
    <div class="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between">
      <div class="text-lg font-bold">Navbar Title</div>
      <nav>
        <ul class="flex space-x-4">
          <li v-for="(link, index) in navLinks" :key="index">
            <a href="#" class="hover:underline">{{ link }}</a>
          </li>
        </ul>
      </nav>
      <div>
        <button class="px-4 py-2 bg-blue-600 hover:bg-blue-700 rounded">Sign In</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Navbar",
  data() {
    return {
      navLinks: ["Home", "About", "Contact"],
    };
  },
};
</script>
