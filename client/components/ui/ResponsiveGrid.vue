<script setup lang="ts">
const { cols = 4, gap = 5 } = defineProps<{
  cols?: number;
  gap?: number;
}>();

const grid = ref<HTMLElement | null>(null);
const gridWidth = ref(0);
const observer = ref<ResizeObserver | null>(null);
const width = ref(0);
const emit = defineEmits(["change"]);

watch(
  gridWidth,
  (v) => {
    const withoutGap = v - gap * (cols - 1);
    width.value = withoutGap / cols;
    emit("change");
  },
  { deep: true },
);

onMounted(() => {
  observer.value = new ResizeObserver((entries) => {
    gridWidth.value = entries[0].contentRect.width;
  });
  if (grid.value) observer.value.observe(grid.value);
});

onBeforeUnmount(() => {
  if (!observer.value) return;
  if (grid.value) observer.value.unobserve(grid.value);
  observer.value.disconnect();
});
</script>

<template>
  <div
    ref="grid"
    class="grid"
    :style="[`--width: ${width}px`, `--gap: ${gap}px`]"
  >
    <slot />
  </div>
</template>

<style lang="scss" scoped>
.grid {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  width: 100%;
  gap: var(--gap);

  & > *:not(slot) {
    margin: 0;
    width: var(--width);
  }
}
</style>
