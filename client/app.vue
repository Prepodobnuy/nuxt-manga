<template>
  <UiApp>
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </UiApp>
</template>

<style>
html {
  background: #f2f2f2;
}

*,
*::before,
*::after {
  -webkit-tap-highlight-color: transparent;
  box-sizing: border-box;
  margin: 0;
  font-weight: normal;
}

.page-enter-active,
.page-leave-active {
  transition: all 0.25s;
}
.page-enter-from,
.page-leave-to {
  opacity: 0;
  filter: blur(1rem);
}
</style>
