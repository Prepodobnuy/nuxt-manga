<script setup>
const props = defineProps({
  icon: String,
  iconWidth: {type: String, default: "22px"},
  checked: {type: Boolean, default: false},
  thin: {type: Boolean, default: false},
  reverse: {type: Boolean, default: false},
  spaceBetween: {type: Boolean, default: false},
  semantic: {type: String, default: ''},
  currentChapter: {type: Number, default: 0},
  chapters: {type: Number, default: 0},
});

const getClass = () => {
  return [
    { checked : props.checked },
    { thin : props.thin },
    { reverse : props.reverse },
    { spaceBetween : props.spaceBetween },
    `semantic-${props.semantic}`,
  ]
}

const getCaption = () => {
  if (props.currentChapter === undefined || props.chapters === undefined) {
    return 'Загрузка...';
  }
  return props.currentChapter === 0 ? 'Начать читать' : 'Продолжить'
}
</script>

<template>
  <div class="entry" :class="getClass()">
    <div class="row">
      <Icon :size="iconWidth" :name="icon" v-if="icon" />
      <p>{{ getCaption() }}</p>
    </div>
    <div class="read">
      <p>{{ currentChapter }} / {{ chapters }}</p>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@use '~/assets/components/uiwide.scss';

.entry {
  cursor: pointer;
  &:active {background-color: var(--bg-active);}

  justify-content: space-between;

  .row {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    gap: var(--row-gap-2);
    align-items: center;
  }

  .read {
    font-size: 80%;
  }
}
</style>