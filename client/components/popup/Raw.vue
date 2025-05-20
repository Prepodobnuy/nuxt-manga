<script setup lang="ts">
const emit = defineEmits(["exit"]);
</script>

<template>
  <div class="blank" @click.self="emit('exit')">
    <Transition name="fade" appear>
      <div class="popup">
        <slot name="header" />
        <slot name="main" />
      </div>
    </Transition>
  </div>
</template>

<style lang="scss" scoped>
.blank {
  position: fixed;
  z-index: 3000;
  width: 100vw;
  height: 100vh;
  background-color: #0000006f;
}
.popup {
  position: fixed;
  z-index: 3000;
  display: flex;
  flex-direction: column;
  background-color: var(--window-bg);

  padding: calc(var(--pd) * var(--xxxl));
  gap: calc(var(--gap) * var(--xxxl));
  border-radius: calc(var(--br) * var(--xl));

  left: 50%;
  top: 50%;
  transform: translateX(-50%) translateY(-50%);

  width: 540px;
}

@media (max-width: 540px) {
  .popup {
    width: calc(100vw - var(--gap) - var(--gap));
    margin: var(--gap);
    left: 0;
    transform: translateY(-50%);
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 300ms;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.fade-enter-to,
.fade-leave-from {
  opacity: 1;
}
</style>
