<script setup>
const store = useAuthFormStore();
</script>

<template>
<BodyFormLayout>
  <template v-slot:header>
    <HeaderPseudoHeader>
      <h1>Регистрация</h1>
      <div class="row">
        <p>Уже есть аккаунт? <NuxtLink class="active-translate-y" to="login">Войти</NuxtLink></p>
        <UiDefaultButton 
          caption="Отправить"
          semantic="y"
          @mouseup="store.postSignup()"
        />
      </div>
    </HeaderPseudoHeader>
  </template>

  <ComplexFormBlock v-model="store.attention.login">
    <h4>Имя пользователя</h4>
    <UiDefaultInput v-model="store.state.login"/>
  </ComplexFormBlock>

  <ComplexFormBlock v-model="store.attention.email">
    <h4>Почта</h4>
    <UiDefaultInput v-model="store.state.email"/>
  </ComplexFormBlock>

  <ComplexFormBlock v-model="store.attention.password">
    <h4>Пароль</h4>
    <UiDefaultInput v-model="store.state.password" type="password"/>
  </ComplexFormBlock>

</BodyFormLayout>
</template>

<style lang="scss" scoped>
.row {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--row-gap-2);
  
  p {
    font-size: 80%;

    a {
      color: var(--color-primary-text-0);
      transition: transform 0.2s;
    }
  }
}
</style>