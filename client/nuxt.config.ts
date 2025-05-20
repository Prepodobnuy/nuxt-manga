// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2024-11-01",
  devtools: { enabled: true },
  css: ["@/assets/base.scss"],

  modules: [
    "@nuxt/eslint",
    "@nuxt/fonts",
    "@nuxt/icon",
    "@nuxt/image",
    "@nuxt/scripts",
    "@nuxt/test-utils",
    "@nuxtjs/color-mode",
    "nuxt-viewport",
    "@vueuse/nuxt",
    "@pinia/nuxt",
  ],

  nitro: {
    prerender: {
      routes: ["/api/tags", "/api/genres"],
    },
  },

  runtimeConfig: {
    public: {
      apiBase: "http://127.0.0.1:8000",
    },
  },

  viewport: {
    breakpoints: {
      desktop: 1024,
      desktopMedium: 1280,
      desktopWide: 1600,

      mobile: 320,
      mobileMedium: 375,
      mobileWide: 425,

      tabletxs: 568,
      tablet: 768,
    },
  },

  colorMode: {
    preference: "system",
    fallback: "light",
  },

  pinia: {
    storesDirs: ["./stores/**", "./forms/**"],
  },
});
