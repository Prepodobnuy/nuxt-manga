<script setup>
const props = defineProps({
  bgUrl: String,
  name: String,
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
        <h4>{{ name }}</h4>
        <p>Персона</p>
      </div>
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