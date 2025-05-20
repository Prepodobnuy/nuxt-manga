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

const emit = defineEmits(["include", "exclude", "clear"]);
const model = defineModel({ default: 0 });

const roll = () => {
  if (model.value == 2) {
    model.value = 0;
    return;
  } else {
    model.value += 1;
  }
  switch (model.value) {
    case 0:
      emit("clear");
      break;
    case 1:
      emit("include");
      break;
    case 2:
      emit("exclude");
      break;
  }
};

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
  <button :class="getSelectors()" @click="roll()">
    <div
      class="box"
      :class="model === 1 ? 'include' : model === 2 ? 'exclude' : ''"
    >
      <Icon v-if="model === 1" class="icon" name="heroicons:check-16-solid" />
      <Icon v-if="model === 2" class="icon" name="heroicons:x-mark-16-solid" />
    </div>
    <slot>{{ label }}</slot>
  </button>
</template>

<style lang="scss" scoped>
@use "@/assets/mixins";
@use "@/assets/variables";
@use "@/assets/functions";

.box {
  height: calc(var(--hg) * var(--scale) - calc(var(--pd) * 2 * var(--scale)));
  width: calc(var(--hg) * var(--scale) - calc(var(--pd) * 2 * var(--scale)));
  border-radius: calc(var(--br) * var(--scale));

  box-shadow: inset 0 0 0 1px var(--neutral-bg);
  background-color: color-mix(in srgb, transparent 100%, var(--neutral-bg) 25%);

  display: flex;
  flex-direction: column;

  align-items: center;
  justify-content: center;

  transition:
    background-color 220ms ease,
    box-shadow 220ms ease;

  color: var(--error-fg);

  &.include {
    background-color: var(--success-bg);
    box-shadow: none;
  }
  &.exclude {
    background-color: var(--error-bg);
    box-shadow: none;
  }

  .icon {
    width: 100%;
    height: 100%;
  }
}

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
      "hover": color-mix(in srgb, transparent 60%, var(--bg-active) 100%),
      "active": color-mix(in srgb, transparent 20%, var(--bg-active) 100%),
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

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 220ms ease;
}
</style>
