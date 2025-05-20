<script setup lang="ts">
const {
  min,
  max,
  size = "md",
  roundness = "standart",
  color = "neutral",
  variant = "solid",
} = defineProps<{
  min?: number;
  max?: number;
  size?: "xs" | "sm" | "md" | "lg" | "xl";
  roundness?: "standart" | "pill" | "none";
  color?: "neutral" | "primary" | "success" | "warning" | "error";
  variant?: "solid" | "outline" | "soft" | "softborder" | "ghost" | "link";
}>();

const model = defineModel<number | null>({ default: null });
const emit = defineEmits(["change"]);

const handleInput = (value: string) => {
  const numericValue = Number(value);

  if (isNaN(numericValue)) {
    model.value = null;
    return;
  }

  model.value = numericValue;
};

watch(model, (newValue) => {
  if (newValue === null) return;

  let correctedValue = newValue;

  if (typeof min === "number") {
    correctedValue = Math.max(min, correctedValue);
  }

  if (typeof max === "number") {
    correctedValue = Math.min(max, correctedValue);
  }

  if (correctedValue !== newValue) {
    model.value = correctedValue;
  }

  emit("change");
});

const decrement = () => {
  if (model.value === null) {
    model.value = min ?? 0;
    return;
  }

  model.value = Math.max(min ?? -Infinity, model.value - 1);
};

const increment = () => {
  if (model.value === null) {
    model.value = min ?? 0;
    return;
  }

  model.value = Math.min(max ?? Infinity, model.value + 1);
};

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
  <div class="wrapper" :class="getSelectors()">
    <UiButton
      class="button"
      icon
      leading="heroicons:minus-16-solid"
      :size="size"
      :color="color"
      :variant="variant"
      roundness="none"
      @click="decrement"
    />
    <UiInput
      v-model="model"
      @input="checkModel"
      class="input"
      :size="size"
      :color="color"
      :variant="variant"
      roundness="none"
    />
    <UiButton
      class="button"
      icon
      leading="heroicons:plus-16-solid"
      :size="size"
      :color="color"
      :variant="variant"
      roundness="none"
      @click="increment"
    />
  </div>
</template>

<style lang="scss" scoped>
@use "@/assets/mixins";
@use "@/assets/variables";
@use "@/assets/functions";

.wrapper {
  @include mixins.generate-sizes(variables.$sizes);
  @include mixins.generate-roundness(variables.$roundness);

  height: calc(var(--hg) * var(--scale));
  display: inline-flex;
  overflow: hidden;

  .button {
    flex-shrink: 0;
  }
  .input {
    max-width: 70px;
    flex-shrink: 1;
  }
}
</style>
