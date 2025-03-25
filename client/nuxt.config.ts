// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: {
    enabled: true,

    timeline: {
      enabled: true,
    },
  },

  runtimeConfig: {
    public: {
      apiBaseUrl: process.env.API_BASE_URL || 'http://localhost:8000',
    },
  },
  routeRules: {
    '/create/person': {ssr: false},
    '/create/title': {ssr: false},
  },
  app: {
    pageTransition: {
      name: 'coolfade',
      mode: 'out-in',
      appear: true,
    },
  },
  css: [
    '~/assets/normalize.css',
    '~/assets/base.scss',
    '~/assets/theme.scss',
    '~/assets/skeleton.scss',
  ],
  modules: [
    '@nuxt/eslint',
    '@nuxt/fonts',
    '@nuxt/icon',
    '@nuxt/image',
    '@nuxt/scripts',
    '@nuxt/test-utils',
    '@nuxt/ui',
    '@nuxt/content',
    '@nuxtjs/color-mode',
    '@pinia/nuxt',
  ],
  colorMode: {
    preference: 'system',
    fallback: 'light',
    classSuffix: '',
    storageKey: 'nuxt-color-mode',
  }
})
