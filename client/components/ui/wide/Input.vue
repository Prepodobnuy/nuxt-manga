<script setup>
const props = defineProps({
  placeholder: String,
  type: {type: String, default: 'text'},
  iconWidth: {type: String, default: "22px"},
  checked: {type: Boolean, default: false},
  thin: {type: Boolean, default: false},
  reverse: {type: Boolean, default: false},
  spaceBetween: {type: Boolean, default: false},
  semantic: {type: String, default: ''},
});

const model = defineModel();

const getClass = () => {
  return [
    { checked : props.checked },
    { thin : props.thin },
    { reverse : props.reverse },
    { spaceBetween : props.spaceBetween },
    `semantic-${props.semantic}`,
    'entry'
  ]
}
</script>

<template>
  <div :class="getClass()">
    <input :type="type" :placeholder="placeholder" v-model="model">
  </div>
</template>

<style lang="scss" scoped>
@use '~/assets/components/uiwide.scss';

.entry {
  padding: 0;
  input {
    transition: background-color 0.22s;
    background-color: var(--bg);
    color: var(--color-text-0);
    border: unset;
    outline: unset;

    width: 100%;
    height: 100%;
    padding: var(--input-padding);
    border-radius: var(--entry-borrad);
    &:focus {background-color: var(--bg-active);}
  }
}

</style>