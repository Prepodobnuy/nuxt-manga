<script setup>
const emit = defineEmits(['showSearch', 'showMainMenu']);
</script>

<template>
<header>
  <UiDefaultMobileHeaderEntry 
    icon="heroicons:magnifying-glass-16-solid" 
    caption="Поиск"
    @mouseup="emit('showSearch')"
  />
  <UiDefaultMobileHeaderEntry 
    icon="heroicons:squares-2x2-16-solid" 
    caption="Каталог"
  />
  <UiDefaultMobileHeaderEntry 
    icon="heroicons:home-solid" 
    caption="Главная"
  />
  <UiDefaultMobileHeaderEntry 
    icon="heroicons:user-16-solid" 
    caption="Профиль"
  />
  <UiDefaultMobileHeaderEntry 
    icon="heroicons:cog-6-tooth-solid" 
    caption="Меню"
    @mouseup="emit('showMainMenu')"
  />
</header>
</template>

<style lang="scss" scoped>
header {
  position: fixed;
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  
  justify-content: start;
  align-items: center;
  gap: 0;

  width: 100%;
  height: var(--header-height);
  bottom: 0;
  left: 0;
  z-index: 1000;

  background-color: var(--color-background-8);
}
</style>