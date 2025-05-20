<script setup lang="ts">
const { user, logged, fetchUser } = useAuth();
console.clear();
console.log(user);
</script>

<template>
  <div>
    <UiDropdown
      v-if="user?.moder || user?.admin || user?.translator"
      align="right"
    >
      <template #head>
        <UiButton
          color="primary"
          leading="heroicons:squares-2x2-16-solid"
          variant="ghost"
          icon
        />
      </template>
      <UiButton
        v-if="user.moder || user.admin"
        label="Панель модерации"
        variant="ghost"
        roundness="none"
        start
        @click="navigateTo('/panel/moderator')"
      />
      <UiButton
        v-if="user.admin"
        label="Панель администрации"
        variant="ghost"
        roundness="none"
        start
        @click="navigateTo('/panel/admin')"
      />
      <UiButton
        v-if="user.translator || user.admin"
        label="Панель переводчика"
        variant="ghost"
        roundness="none"
        start
        @click="navigateTo('/panel/translator')"
      />
    </UiDropdown>

    <UiDropdown align="right" v-if="logged && !user?.muted">
      <template #head>
        <UiButton
          color="primary"
          leading="heroicons:pencil-square-16-solid"
          variant="ghost"
          icon
        />
      </template>
      <UiButton
        label="Добавить Тайтл"
        variant="ghost"
        roundness="none"
        leading="heroicons:book-open-16-solid"
        start
        @click="navigateTo('/title/create')"
      />
      <UiButton
        label="Добавить Персону"
        variant="ghost"
        roundness="none"
        leading="heroicons:user-solid"
        start
        @click="navigateTo('/person/create')"
      />
      <UiButton
        v-if="!user?.translator"
        label="Создать Команду"
        variant="ghost"
        roundness="none"
        leading="heroicons:language-16-solid"
        start
        @click="navigateTo('/translate/create')"
      />
    </UiDropdown>

    <UiButton
      v-if="logged && user"
      color="primary"
      leading="heroicons:user-16-solid"
      variant="ghost"
      icon
      @click="navigateTo(`/user/${user.uuid}`)"
    />

    <UiDropdown align="right" v-if="!logged">
      <template #head>
        <UiButton
          color="primary"
          leading="heroicons:user-16-solid"
          variant="ghost"
          icon
        />
      </template>
      <UiButton
        label="Регистрация"
        variant="ghost"
        roundness="none"
        start
        @click="navigateTo('/auth/signup')"
      />
      <UiButton
        label="Вход"
        variant="ghost"
        roundness="none"
        start
        @click="navigateTo('/auth/login')"
      />
    </UiDropdown>

    <UiDropdown align="right">
      <template #head>
        <ColorModeThemeIconButton />
      </template>
      <ColorModeThemeSwitchButton />
      <HueSliderDropdown />
    </UiDropdown>
  </div>
</template>
