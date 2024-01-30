// https://nuxt.com/docs/api/configuration/nuxt-config
import { resolve } from 'path';

const SHARING_TITLE = 'Информационный Портал для специалистов здравоохранения';
const SHARING_DESCRIPTION = 'Description';
const SHARING_IMAGE = '/';

export default defineNuxtConfig({
  ssr: false,
  app: {
    head: {
      title: SHARING_TITLE,
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon/favicon.ico' },
        { rel: 'manifest', type: 'image/png', href: '/favicon/site.webmanifest' }
      ],

      meta: [
        { charset: 'utf-8' },
        {
          name: 'viewport',
          content:
            'width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no, shrink-to-fit=no',
        },

        { hid: 'description', name: 'description', content: SHARING_DESCRIPTION },

        /* { hid: 'google:name', itemprop: 'name', content: SHARING_TITLE },
        { hid: 'google:description', itemprop: 'description', content: SHARING_DESCRIPTION },
        { hid: 'google:image', itemprop: 'image', content: SHARING_IMAGE }, */

        { property: 'og:type', content: 'website' },
        { hid: 'og:title', property: 'og:title', content: SHARING_TITLE },
        { hid: 'og:description', property: 'og:description', content: SHARING_DESCRIPTION },
        { hid: 'og:image', property: 'og:image', content: SHARING_IMAGE },
        { property: 'og:image:width', content: '1024' },
        { property: 'og:image:height', content: '456' },

        { name: 'twitter:cart', content: 'summary_large_image' },
        { hid: 'twitter:title', name: 'twitter:title', content: SHARING_TITLE },
        { hid: 'twitter:description', name: 'twitter:description', content: SHARING_DESCRIPTION },
        { hid: 'twitter:image', name: 'twitter:image', content: SHARING_IMAGE },

        { name: 'format-detection', content: 'telephone=no' },

        {
          name: 'description',
          content: SHARING_DESCRIPTION,
        },
      ],
    },
  },

  components: [
    {
      path: '~/components/app',
      pathPrefix: false,
    },
  ],

  runtimeConfig: {
    public: {
      apiUrl: process.env.API_URL,
      baseUrl: process.env.BASE_URL,
      capchaKey: process.env.CAPCHA_KEY,
    },
  },

  modules: [
    'nuxt-svgo',
    ['@nuxtjs/device'],
    ['@nuxtjs/stylelint-module', { lintOnStart: false }],
    ['@nuxtjs/eslint-module', { lintOnStart: false }],
  ],

  svgo: {
    defaultImport: 'url',
  },

  device: {
    refreshOnResize: true,
  },

  css: ['assets/scss/main.scss'],

  vite: {
    css: {
      preprocessorOptions: {
        scss: {
          additionalData: '@use "@/assets/scss/abstracts/index.scss" as *;',
        },
      },
    },
  },
});
