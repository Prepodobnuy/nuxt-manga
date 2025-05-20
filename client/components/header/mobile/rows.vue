<script lang="ts" setup>
const viewStore = useViewStore();
const { logged, user } = useAuth();

const handleProfileClick = () => {
  if (logged) {
    navigateTo(`/user/${user.value?.uuid}`);
    return;
  }
  navigateTo("/auth/signup");
};
</script>

<template>
  <UiButton
    color="primary"
    leading="heroicons:magnifying-glass-16-solid"
    variant="ghost"
    roundness="none"
    column
    label="Поиск"
    @click="viewStore.toggleViewSearch()"
  />
  <UiButton
    color="primary"
    leading="heroicons:bars-3-16-solid"
    variant="ghost"
    roundness="none"
    column
    label="Каталог"
    @click="navigateTo('/catalog')"
  />
  <UiButton
    color="primary"
    leading="heroicons:home-16-solid"
    variant="ghost"
    roundness="none"
    column
    label="Главная"
    @click="navigateTo('/')"
  />
  <UiButton
    color="primary"
    leading="heroicons:user-16-solid"
    variant="ghost"
    roundness="none"
    column
    label="Профиль"
    @click="handleProfileClick()"
  />
  <UiButton
    color="primary"
    leading="heroicons:arrow-left-start-on-rectangle-16-solid"
    variant="ghost"
    roundness="none"
    column
    label="Меню"
    @click="viewStore.toggleViewUtilMenu()"
  />
</template>
