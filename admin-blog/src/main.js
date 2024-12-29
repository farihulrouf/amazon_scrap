import { createApp } from 'vue';
import './style.css';
import './assets/index.css';
import App from './App.vue';
import router from './router'; // Mengimpor router yang sudah Anda buat

// Buat aplikasi Vue dan gunakan router
const app = createApp(App);

app.use(router); // Tambahkan router ke aplikasi
app.mount('#app'); // Pasang aplikasi ke elemen #app
