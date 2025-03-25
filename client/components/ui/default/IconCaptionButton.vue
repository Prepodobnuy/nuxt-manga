<script setup>
const props = defineProps({
  icon: String,
  caption: String,
});
</script>

<template>
  <button class="active-translate-y">
    <Icon :name="icon" size="16px" />
    <span class="caption">{{ caption }}</span>
  </button>
</template>

<style lang="scss" scoped>
button {
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
  height: var(--input-height);
  width: max-content;
  padding: var(--input-padding);
  border-radius: var(--input-borrad);

  transition: background-color 0.2s, transform 0.12s;

  &:active {
    background-color: var(--color-primary-background-0);
  }

  .caption {
    font-size: 50%;
  }
}
</style>