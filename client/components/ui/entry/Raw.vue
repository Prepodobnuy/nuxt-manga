<script setup lang="ts">
const {
  roundness = "standart",
  color = "primary",
  clickable = false,
} = defineProps<{
  roundness?: "standart" | "pill" | "none";
  color?: "neutral" | "primary" | "success" | "warning" | "error";
  clickable?: boolean;
}>();

const getSelectors = () => {
  return [
    `color-${color}`,
    `variant-solid`,
    `roundness-${roundness}`,
    clickable ? "clickable" : "",
  ];
};
</script>

<template>
  <div class="entry" :class="getSelectors()">
    <slot />
  </div>
</template>

<style lang="scss" scoped>
@use "@/assets/mixins";
@use "@/assets/variables";
@use "@/assets/functions";

.entry {
  @include mixins.flex-start;
  @include mixins.generate-roundness(variables.$roundness);
  @include mixins.generate-colors(variables.$colors);

  width: 100%;
  --height: calc(var(--hg) * var(--xxxl));
  height: var(--height);
  font-size: calc(var(--fs) * var(--lg));
  user-select: none;
  gap: 0.4em;
  transition:
    background-color 200ms,
    color 200ms;

  @include mixins.generate-variant(
    "solid",
    (
      "bg": color-mix(in srgb, transparent 100%, var(--bg) 0%),
      "hover": color-mix(in srgb, transparent 100%, var(--bg) 0%),
      "active": color-mix(in srgb, transparent 100%, var(--bg) 0%),
      "color": var(--reverse-color),
    )
  );

  &.clickable {
    cursor: pointer;
    @include mixins.generate-variant(
      "solid",
      (
        "bg": color-mix(in srgb, transparent 100%, var(--bg) 0%),
        "hover": color-mix(in srgb, transparent 100%, var(--bg) 33%),
        "active": color-mix(in srgb, transparent 100%, var(--bg) 77%),
        "color": var(--reverse-color),
      )
    );
  }
}
</style>
