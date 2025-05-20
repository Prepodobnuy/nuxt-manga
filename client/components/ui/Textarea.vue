<script lang="ts" setup>
const {
  placeholder,
  type = "text",
  size = "md",
  roundness = "standart",
  color = "neutral",
  variant = "solid",
} = defineProps<{
  placeholder?: string;
  type?: "text" | "password";
  size?: "xs" | "sm" | "md" | "lg" | "xl";
  roundness?: "standart" | "pill" | "none";
  color?: "neutral" | "primary" | "success" | "warning" | "error";
  variant?: "solid" | "outline" | "soft" | "softborder" | "ghost" | "link";
}>();

const model = defineModel<string | undefined>({ default: undefined });

const getSelectors = () => {
  return [
    `size-${size}`,
    `color-${color}`,
    `variant-${variant}`,
    `roundness-${roundness}`,
  ];
};
</script>

<template>
  <textarea v-model="model" class="text-area" :class="getSelectors()" />
</template>

<style lang="scss" scoped>
@use "@/assets/mixins";
@use "@/assets/variables";
@use "@/assets/functions";

.text-area {
  @include mixins.textarea-reset;
  @include mixins.flex-center;
  @include mixins.generate-sizes(variables.$sizes);
  @include mixins.generate-roundness(variables.$roundness);
  @include mixins.generate-colors(variables.$colors);

  height: calc(calc(var(--hg) * var(--scale)) * 2.4);
  padding: calc(var(--pd) * var(--scale));
  gap: calc(var(--gap) * var(--scale));
  font-size: calc(var(--fs) * var(--scale));
  flex-shrink: 0;
  transition:
    filter 0.2s,
    background 0.2s,
    color 0.1s;

  @include mixins.generate-variant(
    "solid",
    (
      "bg": var(--bg),
      "color": var(--fg),
    ),
    true
  );
  @include mixins.generate-variant(
    "outline",
    (
      "bg": functions.transparent-mix(var(--bg), 60%, 30%),
      "color": var(--neutral-fg),
      "hover": functions.transparent-mix(var(--bg-active), 100%, 50%),
      "active": functions.transparent-mix(var(--bg-active), 100%, 60%),
      "focus": functions.transparent-mix(var(--bg-active), 100%, 60%),
      "border": var(--bg),
    ),
    true
  );
  @include mixins.generate-variant(
    "soft",
    (
      "bg": functions.transparent-mix(var(--bg), 10%, 75%),
      "color": var(--fg),
      "hover": functions.transparent-mix(var(--bg), 30%, 75%),
      "active": functions.transparent-mix(var(--bg), 10%, 75%),
    ),
    true
  );
  @include mixins.generate-variant(
    "softborder",
    (
      "bg": functions.transparent-mix(var(--bg), 10%, 75%),
      "color": var(--fg),
      "border": var(--bg),
      "hover": functions.transparent-mix(var(--bg), 30%, 75%),
      "active": functions.transparent-mix(var(--bg), 10%, 75%),
    ),
    true
  );
  @include mixins.generate-variant(
    "ghost",
    (
      "bg": transparent,
      "color": var(--neutral-fg),
      "hover": functions.transparent-mix(var(--bg), 90%, 15%),
      "active": functions.transparent-mix(var(--bg), 80%, 35%),
    ),
    true
  );
  @include mixins.generate-variant(
    "link",
    (
      "bg": transparent,
      "color": var(--neutral-fg),
      "active": functions.transparent-mix(var(--bg), 90%, 15%),
    ),
    true
  );

  color: inherit;
}
</style>
