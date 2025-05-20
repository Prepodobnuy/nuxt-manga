<script setup lang="ts">
interface Row {
  mark: string;
  total: string;
  percent: number;
  color: string;
}
const {
  row,
  marklead,
  marktrail,
  markwidth = 40,
  totalwidth = 40,
  percentwidth = 40,
} = defineProps<{
  row: Row;
  marklead?: string;
  marktrail?: string;
  markwidth?: number;
  totalwidth?: number;
  percentwidth?: number;
}>();

const getStyle = (): string => {
  return [
    `gridTemplateColumns: ${markwidth}px 1fr ${totalwidth}px ${percentwidth}px`,
    `--row-color: ${row.color}`,
    `--row-width: ${row.percent}%`,
  ];
};
</script>

<template>
  <div class="row" :style="getStyle()">
    <div class="row-mark">
      <Icon v-if="marklead" :name="marklead" />
      {{ row.mark }}
      <Icon v-if="marktrail" :name="marktrail" />
    </div>

    <div class="row-wrapper"><div class="row-body" /></div>

    <div class="row-total">{{ row.total }}</div>

    <div class="row-percent">{{ row.percent }}%</div>
  </div>
</template>

<style lang="scss" scoped>
.row {
  display: grid;
  width: 100%;
  color: inherit;

  &-total,
  &-percent,
  &-mark {
    display: inline-flex;
    align-items: center;
    justify-content: start;
    font-size: var(--fs);
    gap: calc(var(--gap) * var(--xs));

    * {
      font-size: var(--fs);
    }
  }
  &-total {
    display: inline-flex;
    justify-content: end;
    font-size: calc(var(--fs) * var(--sm));
  }
  &-percent {
    display: inline-flex;
    justify-content: end;
    font-size: calc(var(--fs) * var(--sm));
  }

  &-wrapper {
    display: inline-flex;
    width: 100%;
    background-color: var(--layer);
    overflow: hidden;
    border-radius: var(--br);
    .row-body {
      width: var(--row-width);
      background-color: color-mix(
        in srgb,
        var(--layer) 100%,
        var(--row-color) 100%
      );
    }
  }
}
</style>
