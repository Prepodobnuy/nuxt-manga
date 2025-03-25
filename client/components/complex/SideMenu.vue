<script setup>
const props = defineProps({
  reversed: {type: Boolean, default: false},
});
</script>

<template>
  <article :class="{ reversed : reversed }">
    <slot></slot>
  </article>
</template>

<style lang="scss" scoped>
article {
  position: fixed;
  display: flex;
  flex-direction: column;
  gap: 0;

  left: 0;
  top: 0;
  z-index: 2000;

  &.reversed {
    left: unset;
    right: 0;
  }

  width: calc(100% - 30px);
  max-width: 500px;
  height: 100vh;

  background-color: var(--color-background-8);

  overflow-x: hidden;
  overflow-y: auto;
  * {
    flex-shrink: 0;
  }
}
</style>