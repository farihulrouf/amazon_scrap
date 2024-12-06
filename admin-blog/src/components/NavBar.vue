<template>
    <header class="bg-white shadow p-4 flex justify-between items-center">
      <h1 class="text-xl font-semibold">Welcome, User</h1>
      <div class="flex items-center space-x-4">
        <input
          type="text"
          placeholder="Search..."
          class="border border-gray-300 rounded px-4 py-2 focus:outline-none focus:ring-2 focus:ring-cyan-500"
        />
        <button class="bg-cyan-500 text-white px-4 py-2 rounded hover:bg-cyan-600">Notifications</button>
      </div>
    </header>
  </template>
  
  <script>
  export default {
    name: "Navbar",
  };
  </script>
  