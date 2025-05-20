<script lang="ts" setup>
const {
  label,
  size = "md",
  color = "primary",
} = defineProps<{
  label?: string;
  size?: "xs" | "sm" | "md" | "lg" | "xl";
  color?: "primary" | "success" | "error" | "warning";
}>();

const getSelectors = () => {
  return [`size-${size}`, `color-${color}`];
};
</script>

<template>
  <a class="link" :class="getSelectors()">
    <slot>{{ label }}</slot>
  </a>
</template>

<style lang="scss" scoped>
@use "@/assets/mixins";
@use "@/assets/variables";
@use "@/assets/functions";

.link {
  @include mixins.generate-sizes(variables.$sizes);
  cursor: pointer;
  user-select: none;

  font-size: calc(var(--fs) * var(--scale));
  font-weight: 700;

  &.color-primary {
    color: var(--primary-bg) !important;
  }
  &.color-warning {
    color: var(--warnin-bg) !important;
  }
  &.color-error {
    color: var(--error-bg) !important;
  }
  &.color-success {
    color: var(--success-bg) !important;
  }
}
</style>
