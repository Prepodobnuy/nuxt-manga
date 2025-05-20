<script setup lang="ts">
const { label } = defineProps<{
  label?: string;
}>();
</script>

<template>
  <div class="wrapper">
    <header>
      <h6 v-if="label">{{ label }}</h6>
    </header>
    <div class="placeholder">
      <slot />
    </div>
    <footer />
  </div>
</template>

<style lang="scss" scoped>
.wrapper {
  width: 100%;
  display: flex;
  flex-direction: column;
  border-radius: var(--br);
  background-color: var(--neutral-bg);

  header {
    background-color: var(--neutral-bg);
    padding: var(--pd);
    border-radius: var(--br) var(--br) 0 0;
  }

  footer {
    background-color: var(--neutral-bg);
    padding: var(--pd);
    padding-bottom: calc(var(--pd) * 2);
    border-radius: 0 0 var(--br) var(--br);
  }

  .placeholder {
    display: inline-flex;
    gap: var(--gap);
    padding: var(--pd);
  }
}
</style>
