<script setup lang="ts">
const viewStore = useViewStore();

const emit = defineEmits(["close", "login", "sign"]);

const viewProfileMenu = ref(false);
const viewAuthMenu = ref(false);
const viewColorMenu = ref(false);

const toggleProfileMenu = () => {
  viewProfileMenu.value = !viewProfileMenu.value;
};
const toggleAuthMenu = () => {
  viewAuthMenu.value = !viewAuthMenu.value;
};
const toggleColorMenu = () => {
  viewColorMenu.value = !viewColorMenu.value;
};
</script>

<template>
  <SidemenuDefault
    v-if="viewStore.viewUtilMenu && viewStore.mobile"
    @close="viewStore.toggleViewUtilMenu()"
    :reverse="true"
    close-left
  >
    <UiEntryButton label="Главная" leading="heroicons:home-16-solid" />

    <UiEntryButton label="Каталог" leading="heroicons:bars-3-16-solid" />

    <UiEntryButton
      label="Профиль"
      leading="heroicons:user-solid"
      :toggle="viewProfileMenu"
      @click="toggleProfileMenu"
    />
    <div v-if="viewProfileMenu">
      <UiEntryButton
        label="Главная"
        leading="heroicons:building-storefront-solid"
      />
      <UiEntryButton label="Списки" leading="heroicons:bookmark-solid" />
      <UiEntryButton label="Настройки" leading="heroicons:cog-8-tooth-solid" />
      <UiEntryButton
        color="error"
        label="Выход"
        leading="heroicons:power-16-solid"
      />
    </div>

    <UiEntryButton
      label="Аунтефикация"
      leading="heroicons:user-solid"
      :toggle="viewAuthMenu"
      @click="toggleAuthMenu"
    />
    <div v-if="viewAuthMenu">
      <UiEntryButton label="Регистрация" @click="navigateTo('/auth/signup')" />
      <UiEntryButton label="Вход" @click="navigateTo('/auth/login')" />
    </div>

    <UiEntryButton
      label="Цвета"
      leading="heroicons:paint-brush-16-solid"
      :toggle="viewColorMenu"
      @click="toggleColorMenu"
    />
    <div v-if="viewColorMenu">
      <ColorModeEntry />
      <HueSliderEntry />
    </div>
  </SidemenuDefault>
</template>
