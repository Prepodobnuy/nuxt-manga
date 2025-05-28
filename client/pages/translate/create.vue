<script setup lang="ts">
import { useTranslateTeamForm } from "~/forms/useTranslateTeamForm";

const { form, valid, clear, post } = useTranslateTeamForm();

const handlePost = async () => {
  console.clear();
  console.log(1);
  await post();
};
</script>

<template>
  <LayoutPseudoHeader>
    <template #header>
      <h4>Создание команды переводчиков</h4>
    </template>

    <div class="content">
      <UiFormBlock>
        <h6>Аватарка</h6>
        <UiImageInput
          v-model="form.cover"
          :width="180"
          :aspect="1 / 1"
          variant="outline"
        />
      </UiFormBlock>

      <UiFormBlock label="Заполните поле" :active="!valid.title">
        <h6>Название</h6>
        <UiInput v-model="form.title" variant="outline" placeholder="" />
      </UiFormBlock>

      <UiFormBlock label="Заполните поле" :active="!valid.title">
        <h6>Описание</h6>
        <UiTextarea
          v-model="form.description"
          variant="outline"
          placeholder=""
        />
      </UiFormBlock>

      <div class="row">
        <div style="width: 200%" />
        <UiButton label="Очистить" variant="outline" @click="clear()" />
        <UiButton label="Отправить" color="success" @click="handlePost()" />
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
}

.tags-row {
  display: flex;
  gap: var(--gap);
  flex-wrap: wrap;
}
</style>
