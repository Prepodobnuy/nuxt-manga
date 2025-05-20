<script lang="ts" setup>
const {
  placeholder,
  leading,
  trailing,
  type = "text",
  size = "md",
  roundness = "standart",
  color = "neutral",
  variant = "solid",
} = defineProps<{
  placeholder?: string;
  leading?: string;
  trailing?: string;
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
  <div class="placeholder" :class="getSelectors()">
    <slot />
  </div>
</template>

<style lang="scss" scoped>
@use "@/assets/mixins";
@use "@/assets/variables";
@use "@/assets/functions";

.placeholder {
  @include mixins.flex-center;
  @include mixins.generate-sizes(variables.$sizes);
  @include mixins.generate-roundness(variables.$roundness);
  @include mixins.generate-colors(variables.$colors);
  width: 100%;
  height: calc(var(--hg) * var(--scale));
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
      "hover": color-mix(in srgb, transparent 0%, var(--bg-active) 100%),
      "active": color-mix(in srgb, transparent 40%, var(--bg-active) 100%),
      "focus": color-mix(in srgb, transparent 40%, var(--bg-active) 100%),
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
  * {
    font-size: calc(var(--fs) * var(--scale));
  }
}
input {
  @include mixins.input-reset;
  width: 100%;
  height: 100%;
  color: inherit;
  background: unset;
}
.icon {
  display: inline-flex;
  width: 1em;
  height: 1em;
}

.dark-mode .input-placeholder {
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
      "focus": color-mix(
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
      "focus": functions.transparent-mix(var(--bg-active), 100%, 60%),
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
      "hover": color-mix(in srgb, transparent 100%, currentColor 4%),
      "active": color-mix(in srgb, transparent 100%, currentColor 8%),
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
