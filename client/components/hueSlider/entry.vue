<script setup lang="ts">
const hueValue = defineModel({ default: useGetHueValue() });

const updateHue = () => {
  const hue = useGetHue();
  useSetHue(hueValue.value);
};
</script>

<template>
  <UiEntryRaw>
    <input
      v-model="hueValue"
      type="range"
      min="0"
      max="360"
      step="1"
      @input="updateHue"
    />
  </UiEntryRaw>
</template>

<style lang="scss" scoped>
.light-mode input {
  --opacity: 50%;
  --thumb-color: var(--primary-200);
}
.dark-mode input {
  --opacity: 20%;
  --thumb-color: var(--primary-400);
}
input {
  width: 100%;
  height: 100%;
  background: transparent;
  -webkit-appearance: none;
  appearance: none;
  margin: 0;

  &:focus {
    outline: none;
  }

  /* Track */
  &::-webkit-slider-runnable-track {
    margin: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(
      to right,
      color-mix(
        in srgb,
        hsl(0, 80%, 50%) var(--opacity),
        var(--sidebar-bg) 100%
      ),
      color-mix(
        in srgb,
        hsl(60, 80%, 50%) var(--opacity),
        var(--sidebar-bg) 100%
      ),
      color-mix(
        in srgb,
        hsl(120, 80%, 50%) var(--opacity),
        var(--sidebar-bg) 100%
      ),
      color-mix(
        in srgb,
        hsl(180, 80%, 50%) var(--opacity),
        var(--sidebar-bg) 100%
      ),
      color-mix(
        in srgb,
        hsl(240, 80%, 50%) var(--opacity),
        var(--sidebar-bg) 100%
      ),
      color-mix(
        in srgb,
        hsl(300, 80%, 50%) var(--opacity),
        var(--sidebar-bg) 100%
      ),
      color-mix(
        in srgb,
        hsl(360, 80%, 50%) var(--opacity),
        var(--sidebar-bg) 100%
      )
    );
    border: unset;
  }

  &::-moz-range-track {
    @extend ::-webkit-slider-runnable-track;
  }

  /* Thumb */
  &::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    margin: 0;
    width: 10px;
    height: 100%;
    background: color-mix(
      in srgb,
      var(--reverse-color) 10%,
      var(--thumb-color) 100%
    );
    border-radius: 2px;
    border: unset;
    box-shadow: var(--shadow-color);
    transition: transform 0.1s ease;

    &:hover {
      transform: scale(1.1);
    }
  }

  &::-moz-range-thumb {
    @extend ::-webkit-slider-thumb;
  }

  /* Firefox focus ring */
  &::-moz-focus-outer {
    border: 0;
  }
}
</style>
