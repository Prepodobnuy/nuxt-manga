<script setup lang="ts">
const {
  src,
  fallback = "/pfp.png",
  alt = "",
} = defineProps<{
  src: string;
  fallback?: string;
  alt?: string;
}>();

const hasError = ref(false);
const imageRef = ref<HTMLImageElement>();

const onError = () => {
  hasError.value = true;
};

onMounted(() => {
  if (imageRef.value?.complete && imageRef.value.naturalHeight === 0) {
    hasError.value = true;
  }
});
</script>

<template>
  <div class="wrapper">
    <img
      v-if="!hasError"
      ref="imageRef"
      :src="src"
      :alt="alt"
      class="main-image"
      @error="onError"
    />
    <img :src="fallback" :alt="alt" class="fallback-image" />
  </div>
</template>

<style scoped>
.wrapper {
  position: relative;
  overflow: hidden;
}

.main-image,
.fallback-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  position: absolute;
  top: 0;
  left: 0;
}

.fallback-image {
  z-index: 1;
}

.main-image {
  z-index: 2;
}
</style>
