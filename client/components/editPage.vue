<script setup lang="ts">
import { UiImageInput } from "#components";
import type { Page } from "~/types/page";

const { title_id, page } = defineProps<{
  title_id: number;
  page: Page;
}>();

const store = useTitleStore(title_id);
const pageRef = ref(page);
const viewAsset = ref(false);
const config = useRuntimeConfig();
const preview = `${config.public.apiBase}/api/asset/page/${page.id}`;

const setPageAsset = async (image: File) => {
  await store.putPageAsset(pageRef.value.id, image);
};

const deletePage = async () => {
  await store.deletePage(pageRef.value.id);
};

watch(
  pageRef,
  async () => {
    console.clear();
    console.log("watch");
    await store.putPage(pageRef.value.id, {
      volume: pageRef.value.volume,
      chapter: pageRef.value.chapter,
      order: pageRef.value.order,
    });
  },
  { deep: true },
);
</script>

<template>
  <div class="page-edit-wrapper">
    <div class="page-edit">
      <div class="info">
        <UiNumberInput v-model="pageRef.volume" />
        <UiNumberInput v-model="pageRef.chapter" />
        <UiNumberInput v-model="pageRef.order" />
      </div>
      <div class="actions">
        <UiButton
          leading="heroicons:pencil-16-solid"
          :toggle="viewAsset"
          icon
          @click="viewAsset = !viewAsset"
        />
        <UiButton
          leading="heroicons:trash-16-solid"
          color="error"
          icon
          @click="deletePage()"
        />
      </div>
    </div>

    <div v-if="viewAsset" class="asset">
      <UiImageInput
        :aspect="null"
        :preview="preview"
        @select="
          (image) => {
            setPageAsset(image);
          }
        "
      />
    </div>
  </div>
</template>

<style lang="scss" scoped>
.page-edit-wrapper {
  background-color: var(--layer);
  padding: var(--pd);
  border-radius: var(--br);
  display: flex;
  flex-direction: column;
  gap: var(--gap);
}

.page-edit {
  width: 100%;
  display: inline-flex;
  gap: var(--gap);
  justify-content: space-between;

  .actions,
  .info {
    display: inline-flex;
    gap: var(--gap);
  }
}
</style>
