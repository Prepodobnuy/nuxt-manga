<script setup>
const props = defineProps({
  icon: String,
  caption: String,
});
</script>

<template>
  <button class="entry">
    <Icon :name="icon" />
    <span class="caption">{{ caption }}</span>
  </button>
</template>

<style lang="scss" scoped>
button.entry {
  cursor: pointer;

  border: unset;
  outline: unset;

  display: flex;
  flex-direction: column;
  
  justify-content: center;
  align-items: center;
  gap: var(--row-gap-0);

  background-color: transparent;
  color: var(--color-text-0);
  height: 100%;
  width: 100%;

  transition: background-color 0.12s ease;

  &:active {
    background-color: var(--color-primary-background-8);
  }

  .caption {
    font-size: 80%;
  }
}
</style>