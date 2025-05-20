<script setup lang="ts">
const viewStore = useViewStore();
</script>

<template>
  <PopupRaw @exit="viewStore.toggleViewSign()">
    <template #header>
      <header>
        <h4>Регистрация</h4>
        <UiButton label="Создать аккаунт" color="success" :fw="false" />
      </header>
    </template>
    <template #main>
      <UiInput placeholder="Имя пользователя" variant="outline" />
      <UiInput placeholder="Почта" variant="outline" />
      <UiInput placeholder="Пароль" type="password" variant="outline" />
      <span>
        уже есть аккаунт?
        <UiLink
          label="войти"
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
  font-size: var(--fs);
  display: inline-flex;
  gap: var(--gap);
  margin-left: 8px;
}
</style>
