<script setup lang="ts">
const rates = [
  { mark: "1", total: "10", percent: 25, color: "#63ff47" },
  { mark: "2", total: "10", percent: 25, color: "#c5ff47" },
  { mark: "3", total: "10", percent: 25, color: "#ffce47" },
  { mark: "4", total: "10", percent: 25, color: "#ff7b47" },
  { mark: "5", total: "10", percent: 25, color: "#ff4747" },
];
</script>

<template>
  <div>
    <div class="graps-row">
      <UiRowGraph
        class="graph"
        :rows="rates"
        marklead="heroicons:star-16-solid"
        :markwidth="40"
        :totalwidth="25"
        :percentwidth="35"
      >
        <header class="row">
          <h5>Рейтинг</h5>
          <div class="row">
            <UiButton
              size="sm"
              label="в среднем: 4.5"
              variant="ghost"
              leading="heroicons:star-16-solid"
            />
          </div>
        </header>
      </UiRowGraph>
      <UiRowGraph class="graph" :rows="rates" />
    </div>
  </div>
</template>

<style lang="scss" scoped>
.graps-row {
  padding: var(--pd);
  display: inline-flex;
  gap: var(--gap);
  width: 100%;

  header {
    display: inline-flex;
    justify-content: space-between;
    align-items: center;

    .row {
      display: inline-flex;
      align-items: center;
      gap: var(--gap);

      p {
        opacity: 0.9;
        font-size: calc(var(--fs) * var(--sm));
      }
    }
  }
}
</style>
