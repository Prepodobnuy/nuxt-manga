<script setup lang="ts"></script>

<template>
  <LayoutPseudoHeader>
    <template #header>
      <h4>Главная</h4>
      <UiButton label="тык" variant="outline" />
    </template>

    <div class="content">
      <UiTextarea variant="outline" />
      <UiRange></UiRange>

      <EntityUserEntry />
    </div>
  </LayoutPseudoHeader>
</template>

<style lang="scss" scoped>
@use "@/assets/mixins";
@use "@/assets/variables";
@use "@/assets/functions";

.content {
  @include mixins.page-content;
  padding: 20px;
  gap: 20px;
}
</style>
