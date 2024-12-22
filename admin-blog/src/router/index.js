import { createRouter, createWebHistory } from 'vue-router';
import BlogDetail from '../components/BlogDetail.vue';

const routes = [
  {
    path: '/blog-detail',
    name: 'BlogDetail',
    component: BlogDetail,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
