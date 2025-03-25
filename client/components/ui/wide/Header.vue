<script setup>
const props = defineProps({
  caption: String,
  icon: String,
  iconWidth: {type: String, default: "22px"},
  checked: {type: Boolean, default: false},
  thin: {type: Boolean, default: false},
  reverse: {type: Boolean, default: false},
  spaceBetween: {type: Boolean, default: false},
  semantic: {type: String, default: ''},
});

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
    <Icon size="22px" :name="icon" v-if="icon" />
    <h1>{{ caption }}</h1>
  </div>
</template>

<style lang="scss" scoped>
@use '~/assets/components/uiwide.scss';
</style>