<script setup lang="ts">
const {
  images = [],
  width = "100",
  height = "100",
  autoscrollInterval = 4000,
} = defineProps<{
  images?: string[];
  width?: string;
  height?: string;
  autoscrollInterval?: number;
}>();

const current = ref(0);
const container = ref<HTMLElement>();
const autoScrollTimer = ref<NodeJS.Timeout>();
const isHovered = ref(false);
const { x: scrollX } = useScroll(container);
const { width: containerWidth } = useElementSize(container);

const getSnapIndex = (scrollPosition: number) => {
  return Math.round(scrollPosition / Number(width));
};

const handleScroll = useThrottleFn(() => {
  current.value = getSnapIndex(scrollX.value);
  resetAutoScroll();
}, 200);

const scrollToIndex = (index: number) => {
  const target = index * Number(width);
  container.value?.scrollTo({
    left: target,
    behavior: "smooth",
  });
  resetAutoScroll();
};

const startAutoScroll = () => {
  if (images.length <= 1 || autoscrollInterval <= 0) return;

  autoScrollTimer.value = setInterval(() => {
    const nextIndex = (current.value + 1) % images.length;
    scrollToIndex(nextIndex);
  }, autoscrollInterval);
};

const resetAutoScroll = () => {
  clearInterval(autoScrollTimer.value);
  startAutoScroll();
};

const selectImage = (index: number) => {
  if (index === current.value) return;
  scrollToIndex(index);
};

watch([containerWidth, autoscrollInterval], () => {
  if (containerWidth.value > 0) {
    scrollToIndex(current.value);
    resetAutoScroll();
  }
});

onMounted(() => {
  startAutoScroll();
  container.value?.addEventListener(
    "mouseenter",
    () => (isHovered.value = true),
  );
  container.value?.addEventListener(
    "mouseleave",
    () => (isHovered.value = false),
  );
});

onBeforeUnmount(() => {
  clearInterval(autoScrollTimer.value);
  container.value?.removeEventListener(
    "mouseenter",
    () => (isHovered.value = true),
  );
  container.value?.removeEventListener(
    "mouseleave",
    () => (isHovered.value = false),
  );
});

const sliderStyle = computed(() => ({
  width: `${width}px`,
  height: `${height}px`,
  "--item-width": `${width}px`,
  "--item-height": `${height}px`,
}));

watch(isHovered, (hovered) => {
  if (hovered) {
    clearInterval(autoScrollTimer.value);
  } else {
    startAutoScroll();
  }
});
</script>

<template>
  <div class="carousel" :style="sliderStyle">
    <div
      ref="container"
      class="carousel-container"
      @scroll.passive="handleScroll"
    >
      <div v-for="(url, index) in images" :key="url" class="carousel-item">
        <NuxtImg
          class="carousel-image"
          :src="url"
          :width="width"
          :height="height"
          fit="cover"
          format="webp"
          loading="lazy"
        />
      </div>
    </div>

    <div class="carousel-controls">
      <button
        v-for="(_, index) in images"
        :key="`indicator-${index}`"
        class="carousel-indicator"
        :class="{ active: current === index }"
        @click="selectImage(index)"
      />
    </div>
  </div>
</template>

<style lang="scss" scoped>
.carousel {
  position: relative;
  overflow: hidden;
  user-select: none;

  &-container {
    display: flex;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    -webkit-overflow-scrolling: touch;
    width: 100%;
    height: 100%;

    &::-webkit-scrollbar {
      display: none;
    }
  }

  &-item {
    flex: 0 0 var(--item-width);
    height: var(--item-height);
    scroll-snap-align: start;
  }

  &-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }

  &-controls {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    display: flex;
    justify-content: center;
    gap: 0.5rem;
    height: var(--hg);
    display: flex;
    align-items: center;
    justify-content: center;
  }

  &-indicator {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: color-mix(in srgb, transparent 100%, var(--reverse-color) 100%);
    border: none;
    cursor: pointer;
    transition: background 0.3s ease;
    box-shadow: 0 0 1px 1px
      color-mix(in srgb, transparent 100%, var(--neutral-bg) 100%);

    &.active {
      background: var(--reverse-color);
    }
  }
}
</style>
