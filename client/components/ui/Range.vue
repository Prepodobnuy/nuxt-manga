<script setup lang="ts">
import { UiNumberInput } from "#components";

const {
  min,
  max,
  fw = false,
  size = "md",
  roundness = "standart",
  color = "neutral",
  variant = "solid",
} = defineProps<{
  min?: number;
  max?: number;
  fw?: boolean;
  size?: "xs" | "sm" | "md" | "lg" | "xl";
  roundness?: "standart" | "pill" | "none";
  color?: "neutral" | "primary" | "success" | "warning" | "error";
  variant?: "solid" | "outline" | "soft" | "softborder" | "ghost" | "link";
}>();

const minm = defineModel<number | undefined>("minm");
const maxm = defineModel<number | undefined>("maxm");

const minChange = () => {
  if (typeof maxm.value === "undefined") return;
  if (typeof maxm.value === "string") return;
  if (typeof minm.value === "undefined") return;
  if (typeof minm.value === "string") return;
  if (minm.value > maxm.value) {
    maxm.value = minm.value;
  }
};
const maxChange = () => {
  if (typeof maxm.value === "undefined") return;
  if (typeof maxm.value === "string") return;
  if (typeof minm.value === "undefined") return;
  if (typeof minm.value === "string") return;
  if (maxm.value < minm.value) {
    minm.value = maxm.value;
  }
};
</script>

<template>
  <div class="outer-wrapper">
    <UiNumberInput
      v-model="minm"
      @change="minChange"
      :min="min"
      :max="max"
      :size="size"
      :roundness="roundness"
      :color="color"
      :variant="variant"
    />
    <Icon name="heroicons:minus" />
    <UiNumberInput
      v-model="maxm"
      @change="maxChange"
      :min="min"
      :max="max"
      :size="size"
      :roundness="roundness"
      :color="color"
      :variant="variant"
    />
  </div>
</template>

<style lang="scss" scoped>
.outer-wrapper {
  display: inline-flex;
  justify-content: space-between;
  align-items: center;
  gap: var(--gap);
  width: 100%;
}
</style>
