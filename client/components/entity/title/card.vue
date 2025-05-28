<script setup lang="ts">
import { UiFallbackImg } from "#components";
import type { Title } from "~/types/title";

const { title } = defineProps<{
  title?: Title;
}>();

const config = useRuntimeConfig();
const cover = `${config.public.apiBase}/api/asset/title/${title?.title_id}/cover`;
</script>

<template>
  <div v-if="title" class="card-wrapper">
    <UiFallbackImg class="bg" :src="cover" />
    <div class="top-line"></div>
    <div class="content">
      <UiFallbackImg class="pfp" :src="cover" />
      <div class="titles">
        <h6>{{ title.title_ru }}</h6>
        <h6 class="another-title">{{ title.title_en }}</h6>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.card-wrapper {
  cursor: pointer;
  display: flex;
  flex-direction: column;
  position: relative;
  overflow: hidden;
  border-radius: var(--br);
  transition: transform 220ms;

  .bg {
    z-index: 99;
    position: absolute;
    width: 100%;
    height: 100%;
    filter: blur(10px) opacity(0.25);
  }

  &:active {
    transform: translateY(3px);
  }
}

.top-line {
  z-index: 101;
  position: absolute;
  top: calc(var(--pd) - 2px);
  left: calc(var(--pd) - 2px);
}

.another-title {
  font-size: 0.9em;
}

.rating {
  display: inline-flex;
  align-items: center;
  gap: var(--gap);
  font-size: 0.95em;
  background-color: var(--primary-bg);
  color: var(--parimary-fg);
  padding: var(--pd);
  border-radius: var(--br);
}

.content {
  z-index: 100;
  width: 100%;
  display: flex;
  flex-direction: column;
  padding: var(--pd);
  align-items: start;

  .pfp {
    width: 100%;
    aspect-ratio: 1080/1527;
    border-radius: var(--br);
  }

  .titles {
    display: flex;
    flex-direction: column;
    white-space: nowrap;
    overflow: hidden;
    width: 100%;
    font-size: 0.95em;
  }
}
</style>
