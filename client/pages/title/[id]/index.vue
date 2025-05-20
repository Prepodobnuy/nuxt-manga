<script setup lang="ts">
const titleRu = ref("Спокойной ночи, ПунПун");
</script>

<template>
  <LayoutPseudoHeader>
    <template #header>
      <div class="title-header">
        <UiButton
          variant="ghost"
          leading="heroicons:arrow-left-16-solid"
          icon
        />
        <h4>{{ titleRu }}</h4>
      </div>
    </template>

    <div class="content">
      <PageTitleViewDesktopContent />
    </div>
  </LayoutPseudoHeader>
</template>

<style lang="scss" scoped>
@use "@/assets/mixins";
@use "@/assets/variables";
@use "@/assets/functions";

.content {
  @include mixins.page-content;
  padding: calc(var(--gap) * var(--xxl));
}

.title-header {
  display: inline-flex;
  align-items: center;
  gap: var(--gap);
}
</style>
