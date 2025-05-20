<script lang="ts" setup>
const viewStore = useViewStore();

const startX = ref();
const startY = ref();
const startStamp = ref();

const endX = ref();
const endY = ref();
const endStamp = ref();

const touchStart = (event: { touches: any[]; timeStamp: any }) => {
  const touch = event.touches[0];
  startX.value = touch.clientX;
  startY.value = touch.clientY;
  startStamp.value = event.timeStamp;
};

const touchEnd = (event: { changedTouches: any[]; timeStamp: any }) => {
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
      length: 140,
    },
  );

  if (!viewStore.viewSearch && left) {
    viewStore.toggleViewSearch();
  }
  if (!viewStore.viewUtilMenu && right) {
    viewStore.toggleViewUtilMenu();
  }
};
</script>

<template>
  <SidemenuSearch :view="viewStore.viewSearch && viewStore.mobile" />
  <SidemenuUtilMenu :view="viewStore.viewUtilMenu && viewStore.mobile" />
  <SidemenuCatalogMenu />

  <PopupLogin v-if="viewStore.viewLogin" />
  <PopupSignUp v-if="viewStore.viewSign" />

  <div class="wrapper">
    <div
      class="layout"
      :class="{ mobile: viewStore.mobile }"
      @touchstart="touchStart"
      @touchend="touchEnd"
    >
      <HeaderDefault style="flex-shrink: 0" />

      <div class="outer-content">
        <slot />
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.wrapper {
  height: 100vh;
  width: 100vw;
  overflow: hidden;
}
.layout {
  width: 100%;
  height: 100%;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;

  &.mobile {
    flex-direction: column-reverse;
  }

  .outer-content {
    height: 100%;
    overflow-y: auto;
  }
}
</style>
