<script setup>
const props = defineProps({
  type: {type: String, default: 'text'},
  placeholder: {type: String, default: ''},
  semantic: {type: String, default: ''},
});

const model = defineModel();

const getClass = () => {
  return [
    `semantic-${props.semantic}`
  ]
}
</script>

<template>
  <textarea
    :type="type" 
    :placeholder="placeholder" 
    v-model="model"
  >  
  </textarea>
</template>

<style lang="scss" scoped>

textarea {
  border: unset;
  outline: unset;

  resize: none;

  cursor: pointer;

  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;

  justify-content: start;
  align-items: center;
  gap: var(--row-gap-0);

  color: var(--color-text);

  padding: var(--input-padding);
  height: calc(var(--input-height) * 3);
  border-radius: var(--input-borrad);
  background-color: var(--color-background-8);
  box-shadow: inset 0 0 0 1px var(--color-text-0);
  font-size: var(--input-fs);

  transition: color 0.2s, box-shadow 0.2s, transform 0.2s;

  &:focus {
    color: var(--color-primary-text-0);
    box-shadow: inset 0 0 0 1px var(--color-primary-text-0);
  }
}

</style>