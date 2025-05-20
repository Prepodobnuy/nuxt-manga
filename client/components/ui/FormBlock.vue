<script lang="ts" setup>
const { active = false, label = "" } = defineProps<{
  active?: boolean;
  label?: string;
}>();
</script>

<template>
  <div class="form" :class="{ active: active }">
    <slot />
    <p v-if="active">{{ label }}</p>
  </div>
</template>

<style lang="scss" scoped>
.form {
  display: flex;
  flex-direction: column;
  gap: var(--gap);
  transition: padding 110ms;

  &.active {
    background-color: color-mix(in srgb, var(--error-bg) 50%, transparent 100%);
    box-shadow: 0 0 0 2px var(--error-bg);
    border-radius: var(--br);
    padding: var(--pd);
  }

  p {
    font-size: 0.9em;
  }
}
</style>
