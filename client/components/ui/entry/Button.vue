<script setup lang="ts">
const {
  toggle = false,
  label,
  leading,
  trailing,
  roundness = "standart",
  color = "primary",
} = defineProps<{
  toggle?: boolean;
  label?: string;
  leading?: string;
  trailing?: string;
  roundness?: "standart" | "pill" | "none";
  color?: "neutral" | "primary" | "success" | "warning" | "error";
}>();

const model = defineModel();

const variant = "solid";

const getSelectors = () => {
  return [
    `color-${color}`,
    `variant-solid`,
    `roundness-${roundness}`,
    toggle ? "active" : "",
  ];
};
</script>

<template>
  <div class="entry" :class="getSelectors()">
    <Icon class="iicon" v-if="leading" size="1.3em" :name="leading" />
    <slot>{{ label }}</slot>
    <Icon class="iicon" v-if="trailing" size="1.3em" :name="trailing" />
  </div>
</template>

<style lang="scss" scoped>
@use "@/assets/mixins";
@use "@/assets/variables";
@use "@/assets/functions";

.entry {
  @include mixins.flex-start;
  @include mixins.button-reset;
  @include mixins.generate-roundness(variables.$roundness);
  @include mixins.generate-colors(variables.$colors);

  width: 100%;
  --height: calc(var(--hg) * var(--xxxl));
  height: var(--height);
  font-size: calc(var(--fs) * var(--lg));
  padding: 0 0.5em;
  gap: 0.4em;
  user-select: none;
  transition:
    background-color 200ms,
    color 200ms;

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
</style>
