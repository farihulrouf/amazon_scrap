import { createRouter, createWebHistory } from 'vue-router';
import BlogEditor from '../components/BlogEditor.vue';

const routes = [
  {
    path: '/blog-editor',
    name: 'BlogEditor',
    component: BlogEditor,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
