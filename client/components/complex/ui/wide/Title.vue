<script setup>
const props = defineProps({
  bgUrl: String,
  title: String,
  author: String,
  type: String,
});

const getStyle = () => {
  return {
    '--url': `url(${props.bgUrl})`
  }
}
</script>

<template>
  <div class="entry complex">
    <div class="bg" :style="getStyle()"></div>
    <div class="column">
      <div class="row">
        <h4>{{ title }}</h4>
        <p>{{ type }}</p>
      </div>
      <p>{{ author }}</p>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@use '~/assets/components/uiwide.scss';

.entry {
  cursor: pointer;
  &:active {background-color: var(--bg-active);}
}
</style>