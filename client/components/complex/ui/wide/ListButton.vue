<script setup>
const props = defineProps({
  icon: String,
  iconWidth: {type: String, default: "22px"},
  checked: {type: Boolean, default: false},
  thin: {type: Boolean, default: false},
  reverse: {type: Boolean, default: false},
  spaceBetween: {type: Boolean, default: false},
  semantic: {type: String, default: ''},
  list: {type: String, default: null }
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
</script>

<template>
  <div class="entry" :class="getClass()">
    <div class="row">
      <Icon :size="iconWidth" :name="icon" v-if="icon" />
      <p>{{ rate === null ? 'Добавить в список' : 'В списке' }}</p>
    </div>
    <div class="list" v-if="list !== null">
      <p>{{ list }}</p>
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

  .list {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;

    gap: var(--row-gap-0);
    align-items: center;
    
    font-size: 80%;
  }
}
</style>