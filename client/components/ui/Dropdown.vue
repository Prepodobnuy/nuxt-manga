<script setup lang="ts">
import { ref, watchEffect } from "vue";

const isOpen = ref(false);
const triggerRef = ref<HTMLElement | null>(null);
const menuRef = ref<HTMLElement | null>(null);

const toggleMenu = () => {
  isOpen.value = !isOpen.value;
};

watchEffect((onCleanup) => {
  if (isOpen.value) {
    const handleClickOutside = (event: MouseEvent) => {
      if (
        !menuRef.value?.contains(event.target as Node) &&
        !triggerRef.value?.contains(event.target as Node)
      ) {
        isOpen.value = false;
      }
    };

    document.addEventListener("click", handleClickOutside);
    onCleanup(() => {
      document.removeEventListener("click", handleClickOutside);
    });
  }
});

const { align = "center" } = defineProps<{
  align?: "center" | "left" | "right";
}>();

const getSelector = (): string[] => {
  return [`align-${align}`];
};
</script>

<template>
  <div class="dropdown-container">
    <div
      ref="triggerRef"
      @click.prevent="toggleMenu"
      aria-haspopup="true"
      :aria-expanded="isOpen"
      class="trigger-button"
    >
      <slot name="head"> Toggle Menu </slot>
    </div>

    <transition name="dropdown-transition">
      <div
        v-if="isOpen"
        ref="menuRef"
        class="dropdown-menu"
        :class="getSelector()"
        role="menu"
      >
        <slot />
      </div>
    </transition>
  </div>
</template>

<style lang="scss" scoped>
.dropdown-container {
  position: relative;
  display: inline-block;
  z-index: 200;
}

.dropdown-menu {
  position: absolute;
  top: calc(100% + var(--gap));
  display: flex;
  flex-direction: column;
  align-items: start;
  z-index: 200;
  min-width: max-content;
  overflow: hidden;
  transform-origin: top right;
  background-color: var(--window-bg);
  border-radius: var(--br);
  box-shadow: var(--header-shadow);

  &.align-left {
    left: 0;
  }
  &.align-right {
    right: 0;
  }
  &.align-center {
    left: 50%;
    transform: translateX(-50%);
  }
}

.dropdown-transition-enter-active,
.dropdown-transition-leave-active {
  transition:
    opacity 0.15s ease-out,
    transform 0.15s ease-out;
}

.dropdown-transition-enter-from,
.dropdown-transition-leave-to {
  opacity: 0;
  transform: scale(0.95) translateY(-0.5rem);
}
</style>
