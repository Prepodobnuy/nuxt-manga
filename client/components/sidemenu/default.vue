<script setup lang="ts">
const {
  reverse = false,
  closeRight = false,
  closeLeft = false,
} = defineProps<{
  reverse?: boolean;
  closeRight?: boolean;
  closeLeft?: boolean;
}>();

const emit = defineEmits(["close"]);
const isVisible = ref(true);
const slideDuration = 210;
const opacityDuration = 200;

const computedFrom = computed(() => (reverse ? "100%" : "-100%"));
const slideStyle = `${slideDuration}ms`;
const opacityStyle = `${opacityDuration}ms`;

function closeMenu() {
  isVisible.value = false;
  setTimeout(
    () => {
      emit("close");
    },
    Math.max(slideDuration, opacityDuration),
  );
}

const startX = ref();
const startY = ref();
const startStamp = ref();

const endX = ref();
const endY = ref();
const endStamp = ref();

const touchStart = (event) => {
  const touch = event.touches[0];
  startX.value = touch.clientX;
  startY.value = touch.clientY;
  startStamp.value = event.timeStamp;
};

const touchEnd = (event) => {
  const touch = event.changedTouches[0];
  endX.value = touch.clientX;
  endY.value = touch.clientY;
  endStamp.value = event.timeStamp;

  handleSwipe();
};

const handleSwipe = () => {
  const { handleSwipe } = useSwipe();

  const { left, right } = handleSwipe(
    {
      x: startX.value,
      y: startY.value,
      stamp: startStamp.value,
    },
    {
      x: endX.value,
      y: endY.value,
      stamp: endStamp.value,
    },
    {
      length: 100,
    },
  );

  if (left && closeLeft) {
    closeMenu();
  }
  if (right && closeRight) {
    closeMenu();
  }
};
</script>

<template>
  <div
    class="placeholder"
    :class="{ reverse, inactive: !isVisible }"
    @click.self="closeMenu"
  >
    <Transition name="slide" appear>
      <div
        v-if="isVisible"
        class="sidemenu"
        :style="{ '--from': computedFrom, '--duration': slideStyle }"
        @touchstart="touchStart"
        @touchend="touchEnd"
      >
        <slot />
      </div>
    </Transition>
  </div>

  <Transition name="opacity" appear>
    <div
      v-if="isVisible"
      class="darkness"
      :class="{ inactive: !isVisible }"
      :style="{ '--duration': opacityStyle }"
    />
  </Transition>
</template>

<style lang="scss" scoped>
.placeholder,
.darkness {
  position: fixed;
  left: 0;
  top: 0;
  width: 100vw;
  height: 100vh;
  z-index: 2000;
}

.placeholder {
  display: inline-flex;
  flex-direction: row;
  &.reverse {
    flex-direction: row-reverse;
  }
  z-index: 2001;

  .sidemenu {
    width: calc(100% - 50px);
    max-width: 600px;
    height: 100%;

    display: flex;
    flex-direction: column;
    flex-shrink: 0;

    box-shadow: var(--header-shadow);
    background-color: var(--sidebar-bg);
    overflow-y: auto;
    overflow-x: hidden;
  }
  .blank {
    width: 100%;
  }
}

.inactive {
  pointer-events: none;
}
.darkness {
  background-color: var(--shadow-color);
}

.slide-enter-active,
.slide-leave-active {
  transition: transform var(--duration) ease-in-out;
}
.slide-enter-from,
.slide-leave-to {
  transform: translateX(var(--from));
}

.opacity-enter-active,
.opacity-leave-active {
  transition: opacity var(--duration) ease-in-out;
}
.opacity-enter-from,
.opacity-leave-to {
  opacity: 0;
}
</style>
