<script lang="ts" setup>
import { useAuthForm } from "~/forms/useAuthForm";

const { form, valid, clear, postLogin } = useAuthForm();
</script>

<template>
  <LayoutPseudoHeader>
    <template #header>
      <h4>Вход</h4>
    </template>
    <div class="content">
      <UiFormBlock label="Заполните поле" :active="!valid.username">
        <h6>Имя пользователя</h6>
        <UiInput v-model="form.username" variant="outline" placeholder="" />
      </UiFormBlock>

      <UiFormBlock label="Заполните поле" :active="!valid.password">
        <h6>Пароль</h6>
        <UiInput
          v-model="form.password"
          type="password"
          variant="outline"
          placeholder=""
        />
      </UiFormBlock>

      <div class="row">
        <div style="width: 200%">
          нету аккаунта?
          <UiLink
            label="создать"
            size="md"
            color="success"
            @click="navigateTo('/auth/signup')"
          />
        </div>
        <UiButton label="Очистить" variant="outline" @click="clear()" />
        <UiButton label="Отправить" color="success" @click="postLogin()" />
      </div>
    </div>
  </LayoutPseudoHeader>
</template>

<style lang="scss" scoped>
@use "@/assets/mixins";
@use "@/assets/variables";
@use "@/assets/functions";

.content {
  @include mixins.form-content;
  padding: 20px;
  gap: var(--gap);
}

.row {
  display: inline-flex;
  gap: var(--gap);
  margin-top: 1em;
  align-items: center;

  div {
    font-size: var(--fs);
    display: inline-flex;
    gap: var(--gap);
  }
}

.tags-row {
  display: flex;
  gap: var(--gap);
  flex-wrap: wrap;
}
</style>
