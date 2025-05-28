<script setup lang="ts">
import { UiButton, UiNumberInput } from "#components";
import { useTitleStore } from "~/stores/useTitleStore";

const config = useRuntimeConfig();
const { user } = useAuth();
const { tagsRef, genresRef } = useTags();
const { mobile } = useViewportLE();

const route = useRoute();
const id = Number(route.params.id);
const store = useTitleStore(id);

const { total_rates, rate_percent, average_rating } = storeToRefs(
  useTitleStore(id),
);
const { sorted_pages } = storeToRefs(useTitleStore(id));

const images = () =>
  store.form.cover_ids.map((v) => {
    return `${config.public.apiBase}/api/asset/title/${id}/cover/${v}`;
  });
const cover = `${config.public.apiBase}/api/asset/title/${id}/cover`;

const volume = ref(0);
const chapter = ref(0);
const order = ref(0);

const addPage = async () => {
  const last_page = sorted_pages.value[sorted_pages.value.length - 1];
  const has_last = typeof last_page !== "undefined";
  const v = has_last ? last_page.volume : 1;
  const c = has_last ? last_page.chapter : 1;
  const o = has_last ? last_page.order : 0;
  const volume_val = await store.postPage({
    volume: v,
    chapter: c,
    order: o + 1,
  });
};
</script>

<template>
  <div class="pages-wrapper">
    <div class="content">
      <EditPage
        v-for="p in sorted_pages"
        :key="p.id"
        :title_id="id"
        :page="p"
      />
      <div class="page-post">
        <div class="w100" style="width: 100%; flex-shrink: 1" />
        <UiButton
          leading="heroicons:document-plus-solid"
          color="success"
          icon
          @click="addPage()"
        />
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.pages-wrapper {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;

  .content {
    padding: 20px;
    width: 100%;
    max-width: 1100px;
    display: flex;
    flex-direction: column;
    gap: var(--gap);
  }
}

.page-post {
  width: 100%;
  display: inline-flex;
  gap: var(--gap);

  * {
    flex-shrink: 0;
  }
}
</style>
