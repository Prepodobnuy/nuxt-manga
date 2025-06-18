<script setup lang="ts">
const viewStore = useViewStore();

const emit = defineEmits(["close", "login", "sign"]);
const { user, logged } = useAuth();

const viewProfileMenu = ref(false);
const viewAuthMenu = ref(false);
const viewColorMenu = ref(false);
const viewAddMenu = ref(false);

const toggleProfileMenu = () => {
  viewProfileMenu.value = !viewProfileMenu.value;
};
const toggleAuthMenu = () => {
  viewAuthMenu.value = !viewAuthMenu.value;
};
const toggleColorMenu = () => {
  viewColorMenu.value = !viewColorMenu.value;
};

const toggleAddMenu = () => {
  viewAddMenu.value = !viewAddMenu.value;
};

const logout = () => {
  const { logout: l } = useAuth();
  l();
};
</script>

<template>
  <SidemenuDefault
    v-if="viewStore.viewUtilMenu && viewStore.mobile"
    @close="viewStore.toggleViewUtilMenu()"
    :reverse="true"
    close-left
  >
    <UiEntryButton
      label="Каталог"
      leading="heroicons:bars-3-16-solid"
      @click="navigateTo('/')"
    />

    <UiEntryButton
      label="Профиль"
      leading="heroicons:user-solid"
      :toggle="viewProfileMenu"
      @click="toggleProfileMenu"
    />
    <div v-if="viewProfileMenu">
      <UiEntryButton
        v-if="logged && user"
        label="Главная"
        leading="heroicons:building-storefront-solid"
        @click="navigateTo(`/user/${user.uuid}`)"
      />
      <UiEntryButton
        v-if="logged && user"
        label="Настройки"
        leading="heroicons:cog-8-tooth-solid"
        @click="navigateTo(`/user/${user.uuid}/options`)"
      />
      <UiEntryButton
        v-if="logged && user"
        color="error"
        label="Выход"
        leading="heroicons:power-16-solid"
        @click="logout()"
      />
      <UiEntryButton
        v-if="!logged"
        label="Регистрация"
        @click="navigateTo('/auth/signup')"
      />
      <UiEntryButton
        v-if="!logged"
        label="Вход"
        @click="navigateTo('/auth/login')"
      />
    </div>

    <UiEntryButton
      v-if="logged"
      color="primary"
      :toggle="viewAddMenu"
      leading="heroicons:pencil-square-16-solid"
      variant="ghost"
      label="Добавить"
      @click="toggleAddMenu"
    />

    <div v-if="viewAddMenu && logged">
      <UiEntryButton
        label="Добавить Тайтл"
        variant="ghost"
        roundness="none"
        leading="heroicons:book-open-16-solid"
        start
        @click="navigateTo('/title/create')"
      />
      <UiEntryButton
        label="Добавить Персону"
        variant="ghost"
        roundness="none"
        leading="heroicons:user-solid"
        start
        @click="navigateTo('/person/create')"
      />
      <UiEntryButton
        v-if="!user?.translator"
        label="Создать Команду"
        variant="ghost"
        roundness="none"
        leading="heroicons:language-16-solid"
        start
        @click="navigateTo('/translate/create')"
      />
      <UiEntryButton
        v-if="user?.moder || user?.admin"
        label="Панель модерации"
        variant="ghost"
        roundness="none"
        start
        @click="navigateTo('/panel/moderator')"
      />
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
