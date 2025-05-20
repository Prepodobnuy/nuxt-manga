<script setup lang="ts">
interface Tab {
  leading?: string;
  trailing?: string;
  label?: string;
  icon?: boolean;
}

const {
  justify = "start",
  fullWidth = false,
  tabs,
  size = "md",
  roundness = "standart",
  color = "neutral",
  variant = "solid",
  vertical = false,
} = defineProps<{
  justify?: "start" | "center" | "end" | "space-between" | "space-evenly";
  fullWidth?: boolean;
  tabs: Tab[];
  size?: "xs" | "sm" | "md" | "lg" | "xl";
  roundness?: "standart" | "pill" | "none";
  color?: "neutral" | "primary" | "success" | "warning" | "error";
  variant?: "solid" | "outline" | "soft" | "softborder" | "ghost" | "link";
  vertical?: boolean;
}>();

const model = defineModel({ default: 0 });

const getSelectors = (): string[] => {
  return [
    `jusctify-${justify}`,
    fullWidth ? "full-width" : "",
    `size-${size}`,
    vertical ? "vertical" : "",
  ];
};

const getButtonSelector = (index: number): string => {
  if (index === 0) {
    return "first";
  }
  if (index === tabs.length - 1) {
    return "last";
  }
  return "central";
};

const setModelValue = (value: number) => {
  model.value = value;
};
</script>

<template>
  <div class="placeholder" :class="getSelectors()">
    <UiButton
      class="button"
      v-for="(tab, index) in tabs"
      roundness="none"
      :class="getButtonSelector(index)"
      :key="JSON.stringify(tab)"
      :size="size"
      :color="color"
      :variant="variant"
      :leading="tab.leading"
      :trailing="tab.trailing"
      :label="tab.label"
      :icon="tab.icon"
      :toggle="index === model"
      :fw="fullWidth"
      @click="setModelValue(index)"
    />
  </div>
</template>

<style lang="scss" scoped>
@use "@/assets/mixins";
@use "@/assets/variables";
@use "@/assets/functions";

.placeholder {
  display: inline-flex;
  flex-direction: row;
  @include mixins.generate-sizes(variables.$sizes);

  height: calc(var(--hg) * var(--scale));
  width: 100%;

  &.jusctify-start {
    justify-content: start;
  }
  &.jusctify-center {
    justify-content: center;
  }
  &.jusctify-end {
    justify-content: end;
  }
  &.jusctify-space-between {
    justify-content: space-between;
  }
  &.jusctify-space-evenly {
    justify-content: space-evenly;
  }

  * {
    width: max-content;
  }
  --borrad: calc(var(--br) * var(--scale));
  border-radius: var(--borrad);

  &.full-width {
    * {
      width: 100%;
    }
  }
}
</style>
