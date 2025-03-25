<script setup>
</script>

<template>
  <Transition name="loading">
    
  </Transition>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>

<style lang="scss" scoped>
.loading-enter-active {
  transition: 
    opacity 130ms,
}
.loading-leave-active {
  transition: 
    opacity 800ms,
}
.loading-enter-from,
.loading-leave-to {
  opacity: 0;
}
</style>