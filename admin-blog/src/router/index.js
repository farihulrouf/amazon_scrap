import { createRouter, createWebHistory } from 'vue-router';
import Login from '../components/Login.vue';
import CreatePost from '../components/CreatePost.vue';

const routes = [
  {
    path: '/',
    redirect: '/login',  // Rute default yang mengarah ke /login
  },
  {
    path: '/login',
    component: Login,
  },
  {
    path: '/create-post',
    component: CreatePost,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
