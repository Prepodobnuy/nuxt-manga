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
</script>

<template>
  <UiButton :leading="icon" variant="ghost" color="primary" icon />
</template>
