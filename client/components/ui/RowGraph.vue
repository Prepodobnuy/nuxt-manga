<script setup lang="ts">
interface Row {
  mark: string;
  total: string;
  percent: number;
  color: string;
}
const {
  rows,
  marklead,
  marktrail,
  markwidth = 40,
  totalwidth = 40,
  percentwidth = 40,
} = defineProps<{
  rows: Row[];
  marklead?: string;
  marktrail?: string;
  markwidth?: number;
  totalwidth?: number;
  percentwidth?: number;
}>();
</script>

<template>
  <div class="graph-placeholder">
    <slot />
    <main>
      <UiGraphRow
        v-for="row in rows"
        :key="row"
        :row="row"
        :marklead="marklead"
        :marktrail="marktrail"
        :markwidth="markwidth"
        :totalwidth="totalwidth"
        :percentwidth="percentwidth"
      />
    </main>
  </div>
</template>

<style lang="scss" scoped>
.graph-placeholder {
  background-color: var(--layer);
  display: flex;
  flex-direction: column;
  width: 100%;
  border-radius: var(--br);
  padding: var(--pd);
  gap: calc(var(--gap) * 2);

  main {
    display: flex;
    flex-direction: column;
    font-size: 0.95em;
    gap: var(--gap);
  }
}
</style>
