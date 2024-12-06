import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router';  // Mengimpor router yang sudah Anda buat
createApp(App).mount('#app')


createApp(App).use(router).mount('#app');