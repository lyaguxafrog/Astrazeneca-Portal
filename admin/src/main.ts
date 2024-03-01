import { createApp } from 'vue';
import { createVuetify } from 'vuetify';
import { createRouter, createWebHistory } from 'vue-router';
import { routes } from '@/routes';
// Vuetify
// eslint-disable-next-line import/extensions
import 'vuetify/styles';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';
import '@mdi/font/css/materialdesignicons.css';
import '@/assets/scss/main.scss';

import App from './App.vue';

const app = createApp(App);

const router = createRouter({
  history: createWebHistory(),
  routes
});
app.use(router);

const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: 'mdi'
  },
  theme: {
    themes: {
      light: {
        dark: false,
        colors: {
          error: '#B71C1C'
        }
      }
    }
  }
});
app.use(vuetify);

app.mount('#app');
