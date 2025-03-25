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
    <div class="pfp" :style="getStyle()"></div>
    <div class="column">
      <div class="row">
        <h4>{{ name }}</h4>
        <p>Пользователь</p>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@use '~/assets/components/uiwide.scss';

.entry {
  cursor: pointer;
  &:active {background-color: var(--bg-active);}
  .pfp {
    position: absolute;
    width: calc(var(--entry-height) * 1.4);
    height: calc(var(--entry-height) * 1.4);
    right: 0;
    top: 0;
    background-image: var(--url);
    background-repeat: no-repeat;
    background-position: 50%;
    opacity: 0.9;
    background-size: cover;
  }
}
</style>