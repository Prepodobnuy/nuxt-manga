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
  <div class="main-placeholder">
    <div class="titles">
      <h3>Название</h3>
      <h6>Второе Название</h6>
    </div>
    <PageTitleViewTabsViewer />
  </div>
</template>

<style lang="scss" scoped>
.main-placeholder {
  width: 100%;
  max-width: 2000px;
  height: auto;
  position: relative;
  overflow: hidden;

  display: flex;
  flex-direction: column;
  gap: var(--gap);

  .titles {
    display: flex;
    flex-direction: column;
  }

  .image {
    width: 100%;
    aspect-ratio: 2000/800;
    object-fit: cover;
    border-radius: var(--br);
    opacity: 0.5;
  }
}
</style>
