<script setup lang="ts">
import { UiFallbackImg } from "#components";

const config = useRuntimeConfig();
const route = useRoute();
const id = Number(route.params.id);
const { mobile } = useViewportLE();
const store = usePersonStore();
const person = await store.fetchMeta(id);
const cover = `${config.public.apiBase}/api/asset/person/${id}/cover`;
</script>

<template>
  <LayoutPseudoHeader>
    <template #header>
      <div class="title-header">
        <UiButton
          variant="ghost"
          leading="heroicons:arrow-left-16-solid"
          icon
        />
        <h4>{{ person.name_ru }}</h4>
      </div>
    </template>
    <div class="content" :class="mobile ? 'mobile' : ''">
      <aside>
        <img class="img" :src="cover" />
      </aside>
      <main>
        <h5>{{ person.name_ru }}</h5>
        <h6>{{ person.name_en }}</h6>
        <p v-if="person.description">{{ person.description }}</p>
      </main>
    </div>
  </LayoutPseudoHeader>
</template>

<style lang="scss" scoped>
@use "@/assets/mixins";
@use "@/assets/variables";
@use "@/assets/functions";

.title-header {
  gap: calc(var(--gap) * var(--xxl));
  align-items: center;
  display: inline-flex;
}

.content {
  @include mixins.page-content;
  padding: calc(var(--gap) * var(--xxl));
  gap: calc(var(--gap) * var(--xxl));
  display: inline-flex;
  flex-direction: row;

  &.mobile {
    flex-direction: column;
    align-items: center;
  }

  aside {
    width: 300px;
    flex-shrink: 0;
    height: max-content;
    display: flex;
    flex-direction: column;
    gap: calc(var(--gap) * var(--xxl));

    .img {
      width: 300px;
      border-radius: var(--br);
    }
  }

  main {
    height: max-content;
    display: flex;
    flex-direction: column;
    width: 100%;
    flex-shrink: 1;
    gap: calc(var(--gap) * var(--xxl));
  }
}
</style>
