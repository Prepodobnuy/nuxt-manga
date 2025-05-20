<script setup lang="ts">
import { UiFallbackImg } from "#components";
import type { Title } from "~/types/title";

const { title } = defineProps<{
  title?: Title;
}>();

const config = useRuntimeConfig();
const cover = `${config.public.apiBase}/api/asset/title/${title?.title_id}/cover/0`;
</script>

<template>
  <UiEntryRaw v-if="title" class="entry-wrapper" clickable>
    <UiFallbackImg class="bg" :src="cover" />
    <div class="content">
      <UiFallbackImg class="pfp" :src="cover" />
      <div class="titles">
        <h6>{{ title.title_ru }}</h6>
        <h6>{{ title.title_en }}</h6>
      </div>
    </div>
  </UiEntryRaw>
</template>

<style lang="scss" scoped>
.entry-wrapper {
  position: relative;
  overflow: hidden;

  .bg {
    z-index: 99;
    position: absolute;
    width: 100%;
    height: 100%;
    filter: blur(10px) opacity(0.25);
  }
}

.content {
  z-index: 100;
  height: 100%;
  gap: var(--gap);
  display: inline-flex;
  padding: var(--pd);
  align-items: center;

  .pfp {
    height: 100%;
    aspect-ratio: 1080/1527;
    border-radius: var(--br);
  }

  .titles {
    display: flex;
    flex-direction: column;
    white-space: nowrap;
  }
}
</style>
