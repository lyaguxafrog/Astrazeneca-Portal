import HomePage from '@/pages/index.vue';
import PracticumPage from '@/pages/practicum/index.vue';
import PracticumEditorPage from '@/pages/practicum/_id.vue';
import PracticumScreenPage from '@/pages/practicum/screen.vue';

export const routes = [
  { path: '/', component: HomePage },
  { path: '/practicum', component: PracticumPage },
  { path: '/practicum/:id', component: PracticumEditorPage },
  { path: '/practicum/:id/screen/:screenId', component: PracticumScreenPage }
];
