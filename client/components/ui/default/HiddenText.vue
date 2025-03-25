<script setup>
const props = defineProps({
  caption: { type: String, default: null },
  title: { type: String, default: null },
  hiddenTitle: { type: String, default: null },
});

const shown = ref(false);
</script>

<template>
  <div class="column">
    <article class="multiline-truncate" :class="{ shown : shown }">
      {{ caption }}
    </article>
    <a @mouseup="shown=!shown">{{ shown ? hiddenTitle : title }}</a>
  </div>
</template>

<style lang="scss" scoped>

div.column {
  display: flex;
  flex-direction: column;
  gap: var(--row-gap-0);

  .multiline-truncate {
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 4;
    overflow: hidden;
    text-overflow: ellipsis;
    font-size: 90%;

    &.shown {
      -webkit-line-clamp: unset;
    }
  }

  a {
    cursor: pointer;
    color: var(--color-primary-text-0);
    font-size: 90%;
    user-select: none;

    transition: color 0.1s;

    &:active {
      color: var(--color-primary-text-4);
    }
  }
}


</style>