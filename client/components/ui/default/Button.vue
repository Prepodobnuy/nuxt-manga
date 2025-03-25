<script setup>
const props = defineProps({
  icon: String,
  caption: String,
  semantic: {type: String, default: ''},
});

const getClass = () => {
  return [
    `semantic-${props.semantic}`
  ]
}
</script>

<template>
  <button class="active-translate-y" :class="getClass()">
    <Icon :name="icon" size="14px" v-if="icon" />
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
  background-color: var(--color-background-8);
  box-shadow: inset 0 0 0 1px var(--color-text-0);
  font-size: var(--input-fs);

  transition: color 0.2s, box-shadow 0.2s, transform 0.2s;

  &:hover {
    color: var(--color-primary-text-0);
    box-shadow: inset 0 0 0 1px var(--color-primary-text-0);
  }
}

</style>