<script lang="ts" setup>
const {
  toggle = false,
  label,
  leading,
  trailing,
  size = "md",
  roundness = "standart",
  color = "neutral",
  variant = "solid",
  icon = false,
  column = false,
  start = false,
  end = false,
  fw = true,
} = defineProps<{
  toggle?: boolean;
  label?: string;
  leading?: string;
  trailing?: string;
  size?: "xs" | "sm" | "md" | "lg" | "xl";
  roundness?: "standart" | "pill" | "none";
  color?: "neutral" | "primary" | "success" | "warning" | "error";
  variant?: "solid" | "outline" | "soft" | "softborder" | "ghost" | "link";
  icon?: boolean;
  column?: boolean;
  start?: boolean;
  end?: boolean;
  fw?: boolean;
}>();

const getSelectors = () => {
  return [
    `size-${size}`,
    `color-${color}`,
    `variant-${variant}`,
    `roundness-${roundness}`,
    icon ? "icon" : "",
    column ? "column" : "",
    toggle ? "active" : "",
    start ? "start" : "",
    end ? "end" : "",
    fw ? "fw" : "",
  ];
};
</script>

<template>
  <button :class="getSelectors()">
    <Icon class="iicon" v-if="leading" size="1.3em" :name="leading" />
    <slot>{{ label }}</slot>
    <Icon class="iicon" v-if="trailing" size="1.3em" :name="trailing" />
  </button>
</template>

<style lang="scss" scoped>
@use "@/assets/mixins";
@use "@/assets/variables";
@use "@/assets/functions";

button {
  @include mixins.button-reset;
  @include mixins.flex-center;
  &.start {
    @include mixins.flex-start;
  }
  &.end {
    @include mixins.flex-end;
  }
  @include mixins.generate-sizes(variables.$sizes);
  @include mixins.generate-roundness(variables.$roundness);
  @include mixins.generate-colors(variables.$colors);
  height: calc(var(--hg) * var(--scale));
  padding: 0 calc(var(--pd) * var(--scale));
  gap: calc(var(--gap) * var(--scale));
  font-size: calc(var(--fs) * var(--scale));
  * {
    font-size: calc(var(--fs) * var(--scale));
  }
  transition:
    filter 0.2s,
    background 0.2s,
    color 0.1s;

  &.fw {
    width: 100%;
  }

  &.icon {
    padding: 0;
    height: calc(var(--hg) * var(--scale));
    width: calc(var(--hg) * var(--scale));
  }
  &.column {
    display: flex;
    flex-direction: column;
    --fs: 11px;
    --gap: 1px;

    .iicon {
      font-size: var(--fs);
      height: calc(var(--fs) * 2);
    }
  }
}

button {
  @include mixins.generate-variant(
    "solid",
    (
      "bg": var(--bg),
      "color": var(--fg),
      "hover": color-mix(in srgb, transparent 20%, var(--bg-active) 100%),
      "active": color-mix(in srgb, transparent 0%, var(--bg-active) 100%),
    )
  );
  @include mixins.generate-variant(
    "outline",
    (
      "bg": functions.transparent-mix(var(--bg), 60%, 30%),
      "color": var(--neutral-fg),
      "hover": color-mix(in srgb, transparent 0%, var(--bg-active) 100%),
      "active": color-mix(in srgb, transparent 40%, var(--bg-active) 100%),
      "border": var(--bg),
    )
  );
  @include mixins.generate-variant(
    "soft",
    (
      "bg": functions.transparent-mix(var(--bg), 10%, 75%),
      "color": var(--fg),
      "hover": functions.transparent-mix(var(--bg-active), 100%, 30%),
      "active": functions.transparent-mix(var(--bg-active), 100%, 60%),
    )
  );
  @include mixins.generate-variant(
    "softborder",
    (
      "bg": functions.transparent-mix(var(--bg), 10%, 75%),
      "color": var(--fg),
      "border": var(--bg),
      "hover": functions.transparent-mix(var(--bg-active), 100%, 5%),
      "active": functions.transparent-mix(var(--bg-active), 100%, 30%),
    )
  );
  @include mixins.generate-variant(
    "ghost",
    (
      "bg": transparent,
      "color": var(--neutral-fg),
      "hover": color-mix(in srgb, transparent 100%, var(--bg-active) 50%),
      "active": color-mix(in srgb, transparent 100%, var(--bg-active) 100%),
    )
  );
  @include mixins.generate-variant(
    "link",
    (
      "bg": transparent,
      "color": var(--neutral-fg),
      "active": functions.transparent-mix(var(--bg-active), 100%, 60%),
    )
  );
}

.dark-mode button {
  @include mixins.generate-variant(
    "solid",
    (
      "bg": var(--bg),
      "color": var(--fg),
      "hover": color-mix(
          in srgb,
          var(--bg-active) 100%,
          var(--reverse-color) 0%
        ),
      "active": color-mix(
          in srgb,
          var(--bg-active) 100%,
          var(--reverse-color) 10%
        ),
    )
  );
  @include mixins.generate-variant(
    "outline",
    (
      "bg": functions.transparent-mix(var(--bg), 60%, 30%),
      "color": var(--neutral-fg),
      "hover": functions.transparent-mix(var(--bg-active), 100%, 30%),
      "active": functions.transparent-mix(var(--bg-active), 100%, 60%),
      "border": var(--bg),
    )
  );
  @include mixins.generate-variant(
    "soft",
    (
      "bg": functions.transparent-mix(var(--bg), 10%, 65%),
      "color": var(--fg),
      "hover": functions.transparent-mix(var(--bg-active), 100%, 30%),
      "active": functions.transparent-mix(var(--bg-active), 100%, 60%),
    )
  );
  @include mixins.generate-variant(
    "softborder",
    (
      "bg": functions.transparent-mix(var(--bg), 10%, 65%),
      "color": var(--fg),
      "border": var(--bg),
      "hover": functions.transparent-mix(var(--bg-active), 100%, 5%),
      "active": functions.transparent-mix(var(--bg-active), 100%, 30%),
    )
  );
  @include mixins.generate-variant(
    "ghost",
    (
      "bg": transparent,
      "color": var(--neutral-fg),
      "hover": color-mix(in srgb, transparent 100%, var(--bg-active) 30%),
      "active": color-mix(in srgb, transparent 100%, var(--bg-active) 50%),
    )
  );
  @include mixins.generate-variant(
    "link",
    (
      "bg": transparent,
      "color": var(--neutral-fg),
      "active": functions.transparent-mix(var(--bg-active), 100%, 60%),
    )
  );
}
</style>
