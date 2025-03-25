<script setup>

const model = defineModel();

</script>

<template>
  <div class="block" :class="{ attention : model === true }" @mousedown="model = false">
    <slot></slot>
  </div>
</template>

<style lang="scss" scoped>
.block {
  display: flex;
  flex-direction: column;
  gap: var(--row-gap-2);
  width: 100%;

  transition: box-shadow 200ms, background-color 200ms, border-radius 200ms, padding 200ms;

  &.attention {
    box-shadow: 0 0 0 2px var(--color-semantic-n-0);
    background-color: var(--color-semantic-n-background-4);
    border-radius: var(--input-borrad);
    padding: var(--input-padding);
  }
}
</style>