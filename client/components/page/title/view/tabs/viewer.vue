<script setup lang="ts">
const selectedTab = defineModel({ default: 0 });
const tabs = ref([
  {
    label: "О Тайтле",
    icon: false,
  },
  {
    label: "Главы",
    icon: false,
  },
  {
    label: "Комментарии",
    icon: false,
  },
]);
</script>

<template>
  <main>
    <UiTabs v-model="selectedTab" :tabs="tabs" full-width variant="ghost" />
    <PageTitleViewTabsAbout v-if="selectedTab === 0" />
  </main>
</template>

<style lang="scss" scoped>
main {
  overflow: hidden;
  width: 100%;
  background-color: var(--neutral-bg);
  border-radius: var(--br);
}
</style>
