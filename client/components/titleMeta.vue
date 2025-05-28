<script setup lang="ts">
import { useTitleStore } from "#imports";

const { id } = defineProps<{
  id: number;
}>();

const store = useTitleStore(id);
</script>

<template>
  <div class="meta">
    <div v-if="store.form.release_year" class="row">
      <div class="header">Год релиза</div>
      <div class="body">{{ store.form.release_year }}</div>
    </div>

    <div v-if="store.form.author" class="row">
      <div class="header">Автор</div>
      <div
        class="url body"
        @click="navigateTo(`/person/${store.form.author.id}`)"
      >
        {{ store.form.author.name_ru }}
      </div>
    </div>

    <div v-if="store.form.artist" class="row">
      <div class="header">Художник</div>
      <div
        class="url body"
        @click="navigateTo(`/person/${store.form.artist.id}`)"
      >
        {{ store.form.artist.name_ru }}
      </div>
    </div>

    <div v-if="store.form.publisher" class="row">
      <div class="header">Издатель</div>
      <div
        class="url body"
        @click="navigateTo(`/person/${store.form.publisher.id}`)"
      >
        {{ store.form.publisher.name_ru }}
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
aside .meta {
  display: flex;
  flex-direction: column;
  background-color: var(--neutral-bg);
  gap: calc(var(--gap) * var(--sm));
  border-radius: var(--br);
  padding: var(--pd);

  .row {
    display: flex;
    flex-direction: column;
    gap: 2px;
    .header {
      font-size: 0.95em;
      opacity: 0.7;
    }
    .url {
      cursor: pointer;
      color: color-mix(in srgb, var(--primary-bg) 100%, currentColor 100%);
    }
  }
}

main .meta {
  display: inline-flex;
  flex-direction: row;
  border-radius: var(--br);
  z-index: 100;
  width: 100%;
  gap: 5px;

  .row {
    z-index: 100;
    padding: 2px;
    width: 100%;
    flex-shrink: 1;
    align-items: center;
    display: flex;
    flex-direction: column;
    gap: 5px;
    .header {
      text-align: center;
      font-size: 0.9em;
      font-weight: 900;
    }
    .body {
      width: 100%;
      font-size: 0.9em;
      text-align: center;
      word-break: break-word;
      hyphens: auto;
    }
    .url {
      cursor: pointer;
      color: color-mix(in srgb, var(--primary-bg) 25%, currentColor 100%);
    }
  }
}
</style>
