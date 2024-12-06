<template>
    <aside class="w-64 bg-cyan-500 text-white flex flex-col">
      <div class="p-4 text-2xl font-bold">My Dashboard</div>
      <nav class="flex-1 p-4 space-y-4">
        <a href="#" class="block px-4 py-2 rounded hover:bg-cyan-600">Dashboard</a>
        <a href="#" class="block px-4 py-2 rounded hover:bg-cyan-600">Profile</a>
        <a href="#" class="block px-4 py-2 rounded hover:bg-cyan-600">Settings</a>
        <a href="#" class="block px-4 py-2 rounded hover:bg-cyan-600">Help</a>
      </nav>
      <div class="p-4">
        <button class="w-full bg-white text-cyan-500 font-bold py-2 px-4 rounded hover:bg-gray-200">Logout</button>
      </div>
    </aside>
  </template>
  
  <script>
  export default {
    name: "Sidebar",
  };
  </script>
  