<script setup>
const props = defineProps({
  icon: String,
  caption: String,
});
</script>

<template>
  <button class="active-translate-y">
    <Icon :name="icon" size="16px" v-if="icon" />
    <span>{{ caption }}</span>
  </button>
</template>

<style lang="scss" scoped>

button {
  border: unset;
  outline: unset;

  cursor: pointer;

  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;

  justify-content: start;
  align-items: center;
  gap: var(--row-gap-0);

  color: var(--color-text);

  padding: var(--input-padding);
  height: var(--input-height);
  border-radius: var(--input-borrad);
  background-color: transparent;
  font-size: var(--input-fs);

  transition: background-color 0.2s, transform 0.12s;

  &:hover {
    background-color: var(--color-primary-background-0);
  }
}

</style>