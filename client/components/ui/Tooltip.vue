<script setup lang="ts">
const {
  label = "",
  horizontal = "center",
  vertical = "bottom",
  timeout = 300,
} = defineProps<{
  label?: string;
  horizontal?: "left" | "center" | "right";
  vertical?: "bottom" | "top";
  timeout?: number;
}>();

const isVisible = ref(false);
let showTimeout: NodeJS.Timeout | null = null;
let hideTimeout: NodeJS.Timeout | null = null;

const handleMouseEnter = () => {
  if (hideTimeout) {
    clearTimeout(hideTimeout);
    hideTimeout = null;
  }
  showTimeout = setTimeout(() => {
    isVisible.value = true;
  }, timeout);
};

const handleMouseLeave = () => {
  if (showTimeout) {
    clearTimeout(showTimeout);
    showTimeout = null;
  }
  hideTimeout = setTimeout(() => {
    isVisible.value = false;
  }, 100);
};

const tooltipPosition = computed(() => {
  const verticalStyles = {
    bottom: "top: calc(100% + 8px);",
    top: "bottom: calc(100% + 8px);",
  }[vertical];

  const horizontalStyles = {
    left: "left: 0;",
    center: "left: 50%; transform: translateX(-50%);",
    right: "right: 0;",
  }[horizontal];

  return verticalStyles + horizontalStyles;
});
</script>

<template>
  <div
    class="tooltip-container"
    @mouseenter="handleMouseEnter"
    @mouseleave="handleMouseLeave"
  >
    <slot />
    <transition name="fade">
      <div v-if="isVisible && label" class="tooltip" :style="tooltipPosition">
        {{ label }}
      </div>
    </transition>
  </div>
</template>

<style lang="scss" scoped>
.tooltip-container {
  position: relative;
  display: inline-block;
}

.tooltip {
  position: absolute;
  background: var(--window-bg);
  color: inherit;
  padding: var(--pd);
  border-radius: 4px;
  font-size: 14px;
  white-space: nowrap;
  pointer-events: none;
  box-shadow: var(--header-shadow);
  font-size: calc(var(--fs) * var(--sm));
  z-index: 100;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 200ms ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
