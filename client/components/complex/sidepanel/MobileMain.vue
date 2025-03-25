<script setup>
const viewAuth = ref(false);
const viewAdd = ref(false);
</script>

<template>
  <ComplexSideMenu :reversed="true">
    <SharedEntryHeader 
      caption="Меню"
    />

    <UiWideButton 
      caption="Главная"
      icon="heroicons:home-solid"
      :reverse="true"
      :space-between="true"
    />

    <UiWideButton 
      caption="О сайте"
      icon="heroicons:information-circle-16-solid"
      :reverse="true"
      :space-between="true"
    />

    <UiWideButton 
      caption="Каталог"
      icon="heroicons:squares-2x2-16-solid"
      :reverse="true"
      :space-between="true"
    />

    <UiWideButton 
      caption="Уведомления"
      icon="heroicons:bell-solid"
      :reverse="true"
      :space-between="true"
    />

    <UiWideButton 
      caption="Профиль"
      icon="heroicons:user-16-solid"
      :reverse="true"
      :space-between="true"
      :checked="viewAuth"
      @mouseup="viewAuth=!viewAuth"
    />

    <UiWideButton 
      v-if="viewAuth"
      caption="Регистрация"
      icon="heroicons:user-plus-16-solid"
      :reverse="true"
      :space-between="true"
    />

    <UiWideButton 
      v-if="viewAuth"
      caption="Вход"
      icon="heroicons:arrow-left-end-on-rectangle-16-solid"
      :reverse="true"
      :space-between="true"
    />

    <UiWideButton 
      caption="Добавить"
      icon="heroicons:pencil-square-solid"
      :reverse="true"
      :space-between="true"
      :checked="viewAdd"
      @mouseup="viewAdd=!viewAdd"
    />

    <UiWideButton
      caption="Тайтл"
      icon="heroicons:document-solid"
      :reverse="true"
      :space-between="true"
      v-if="viewAdd"
    />

    <UiWideButton
      caption="Персону"
      icon="heroicons:user-group-16-solid"
      :reverse="true"
      :space-between="true"
      v-if="viewAdd"
    />

    <UiWideButton
      caption="Панель модерации"
      icon="heroicons:presentation-chart-line-solid"
      :reverse="true"
      :space-between="true"
      v-if="viewAdd"
    />

    <UiWideButton 
      caption="Сменить тему"
      :icon="$colorMode.preference === 'light' ? 'heroicons:sun-16-solid' : 'heroicons:moon-16-solid'" 
      @mouseup="$colorMode.preference = $colorMode.value === 'dark' ? 'light' : 'dark'" 
      :reverse="true"
      :space-between="true"
    />

    <UiWideButton 
      caption="Выход"
      icon="heroicons:arrow-left-start-on-rectangle-16-solid"
      semantic="n"
      :reverse="true"
      :space-between="true"
    />
        
  </ComplexSideMenu>
</template>

<style lang="scss" scoped>

</style>