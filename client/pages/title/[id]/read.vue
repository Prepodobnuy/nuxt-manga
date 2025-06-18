<script setup lang="ts">
const config = useRuntimeConfig();
const route = useRoute();
const router = useRouter();
const id = Number(route.params.id);
const { mobile } = useViewportLE();
const store = useTitleStore(id);
const { sorted_pages } = storeToRefs(useTitleStore(id));

const index = ref(0);
const isLoaded = ref(false);

onMounted(async () => {
  await store.fetchPages();
  await waitForData();
  isLoaded.value = true;
  syncIndexFromQuery();
  await store.view();
});

const waitForData = async () => {
  let i = 0;
  while (!sorted_pages.value?.length) {
    await new Promise((resolve) => setTimeout(resolve, 100));
    i += 1;
    if (i === 20) {
      navigateTo(`/title/${id}`);
    }
  }
};

const syncIndexFromQuery = () => {
  const { volume, chapter, order } = route.query;
  const targetIndex = sorted_pages.value.findIndex((v) => {
    return (
      v.volume === Number(volume) &&
      v.chapter === Number(chapter) &&
      v.order === Number(order)
    );
  });

  if (targetIndex > -1) {
    index.value = targetIndex;
  } else {
    router.replace({
      query: {
        volume: sorted_pages.value[0].volume,
        chapter: sorted_pages.value[0].chapter,
        order: sorted_pages.value[0].order,
      },
    });
  }
};

watch(index, (newIndex) => {
  const page = sorted_pages.value[newIndex];
  router.replace({
    query: {
      volume: page.volume,
      chapter: page.chapter,
      order: page.order,
    },
  });
});

watch(
  () => route.query,
  () => {
    if (isLoaded.value) syncIndexFromQuery();
  },
);

const prev = () => {
  if (index.value > 0) {
    index.value -= 1;
  }
};

const next = () => {
  if (index.value < sorted_pages.value.length - 1) {
    index.value += 1;
    return;
  }
  navigateTo(`/title/${id}`);
};

const asset = computed(() => {
  return `${config.public.apiBase}/api/asset/page/${sorted_pages.value[index.value]?.id}`;
});
</script>
<template>
  <div class="page-wrapper">
    <div class="content">
      <div class="reader">
        <div class="image">
          <img :src="asset" />
          <div class="left" @click="prev" />
          <div class="right" @click="next" />
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.page-wrapper {
  display: flex;
  flex-direction: column;
  gap: var(--gap);
  min-height: 90vh;
  align-items: center;
  justify-content: start;

  .content {
    max-width: 800px;
    width: 100%;
  }
}

.reader {
  position: relative;
  max-width: 1100px;
  min-height: 100vh;
  display: flex;
  align-items: center;
  user-select: none;

  .image {
    position: relative;
    width: 100%;

    img {
      width: 100%;
    }

    .left,
    .right {
      position: absolute;
      top: 0;
      bottom: 0;
    }

    .left {
      left: 0;
      width: 45%;
    }

    .right {
      right: 0;
      width: 45%;
    }
  }
}
</style>
