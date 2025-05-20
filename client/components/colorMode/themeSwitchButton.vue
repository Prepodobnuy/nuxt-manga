<script setup lang="ts">
const colorMode = useColorMode();

const isDark = computed({
  get() {
    return colorMode.value === "dark";
  },
  set(_isDark) {
    colorMode.preference = _isDark ? "dark" : "light";
  },
});

const icon = computed(() =>
  isDark.value ? "heroicons:moon-16-solid" : "heroicons:sun-16-solid",
);
const label = computed(() => (isDark.value ? "Тёмная тема" : "Светлая тема"));

const cycle = () => {
  isDark.value = !isDark.value;
};
</script>

<template>
  <UiButton
    :label="label"
    :leading="icon"
    @click="cycle"
    start
    variant="ghost"
    roundness="none"
  />
</template>
