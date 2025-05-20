<script setup lang="ts">
const viewStore = useViewStore();
</script>

<template>
  <PopupRaw @exit="viewStore.toggleViewLogin()">
    <template #header>
      <header>
        <h4>Вход</h4>
        <UiButton label="Войти" color="success" :fw="false" />
      </header>
    </template>
    <template #main>
      <UiInput placeholder="Имя пользователя / почта" variant="outline" />
      <UiInput placeholder="Пароль" type="password" variant="outline" />
      <span>
        нету аккаунта?
        <UiLink
          label="создать"
          size="md"
          color="success"
          @click="viewStore.loginReverse()"
        />
      </span>
    </template>
  </PopupRaw>
</template>

<style lang="scss" scoped>
header {
  display: inline-flex;
  align-items: center;
  justify-content: space-between;
}

span {
  margin-left: 8px;
  font-size: var(--fs);
  display: inline-flex;
  gap: var(--gap);
}
</style>
