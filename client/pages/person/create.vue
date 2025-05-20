<script setup lang="ts">
import { UiImageInput, UiTextarea } from "#components";

const { loading, form, valid, clear, post } = usePersonForm();

const handlePost = async () => {
  if (loading) return;

  await post();
};
</script>

<template>
  <LayoutPseudoHeader>
    <template #header>
      <h4>Добавление Персоны</h4>
    </template>

    <div class="content">
      <UiFormBlock>
        <h6>Изображение</h6>
        <UiImageInput
          v-model="form.cover"
          :width="180"
          :aspect="1080 / 1527"
          variant="outline"
        />
      </UiFormBlock>

      <UiFormBlock label="Заполните поле" :active="!valid.nameRu">
        <h6>Имя / название на русском</h6>
        <UiInput v-model="form.nameRu" variant="outline" placeholder="" />
      </UiFormBlock>

      <UiFormBlock label="Заполните поле" :active="!valid.nameEn">
        <h6>Имя / название на английском</h6>
        <UiInput v-model="form.nameEn" variant="outline" placeholder="" />
      </UiFormBlock>

      <UiFormBlock>
        <h6>Имя / название на языке оригинала</h6>
        <UiInput v-model="form.nameJp" variant="outline" placeholder="" />
      </UiFormBlock>

      <UiFormBlock>
        <h6>Альтернативные имена / названия</h6>
        <UiInput
          v-model="form.nameAn"
          variant="outline"
          placeholder="вводите названия разделяя их символом ' / '"
        />
      </UiFormBlock>

      <UiFormBlock>
        <h6>Описание</h6>
        <UiTextarea v-model="form.description" variant="outline" />
      </UiFormBlock>

      <div class="row">
        <div style="width: 200%" />
        <UiButton label="Очистить" variant="outline" @click="clear()" />
        <UiButton
          label="Отправить"
          color="success"
          :variant="loading ? 'ghost' : 'solid'"
          @click="handlePost()"
        />
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
