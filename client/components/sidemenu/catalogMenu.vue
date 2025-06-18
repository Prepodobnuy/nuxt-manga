<script setup lang="ts">
import { UiEntryButton, UiNumberInput } from "#components";

const viewStore = useViewStore();
const { form, includeTags, excludeTags, includeGenres, excludeGenres, clear } =
  useCatalogStore();

const tagPrompt = ref("");
const genrePrompt = ref("");
const filteredTags = () =>
  form.tags.filter((v) =>
    v.value.ru.toLowerCase().includes(tagPrompt.value.toLowerCase()),
  );
const filteredGenres = () =>
  form.genres.filter((v) =>
    v.value.ru.toLowerCase().includes(genrePrompt.value.toLowerCase()),
  );

const activeSection = ref(0);
</script>

<template>
  <SidemenuDefault
    v-if="viewStore.viewCatalogMenu && viewStore.mobile"
    @close="viewStore.toggleCatalogMenu()"
    :reverse="true"
    close-left
  >
    <section v-if="activeSection === 0">
      <UiEntryButton @click="activeSection = 1">
        Тэги
        <div style="width: 100%" />
        <p style="flex-shrink: 0; font-size: 0.95em">
          {{ includeTags().length + excludeTags().length }} /
          {{ form.tags.length }}
        </p>
      </UiEntryButton>
      <UiEntryButton @click="activeSection = 2">
        Жанры
        <div style="width: 100%" />
        <p style="flex-shrink: 0; font-size: 0.95em">
          {{ includeGenres().length + excludeGenres().length }} /
          {{ form.genres.length }}
        </p>
      </UiEntryButton>

      <p style="margin: var(--gap); font-size: 1.1em">Год Релиза</p>
      <p style="margin: var(--gap); font-size: 0.95em">От</p>
      <UiNumberInput class="o" v-model="form.release_year_min" fw />
      <p style="margin: var(--gap); font-size: 0.95em">До</p>
      <UiNumberInput class="o" v-model="form.release_year_max" fw />

      <p style="margin: var(--gap); font-size: 1.1em">Оценка</p>
      <p style="margin: var(--gap); font-size: 0.95em">От</p>
      <UiNumberInput class="o" v-model="form.rate_min" fw />
      <p style="margin: var(--gap); font-size: 0.95em">До</p>
      <UiNumberInput class="o" v-model="form.rate_max" fw />

      <UiEntryButton label="Сбросить" @click="clear()" />
    </section>

    <secion v-if="activeSection === 1">
      <UiEntryButton
        label="Назад"
        variant="ghost"
        start
        leading="heroicons:arrow-long-left-16-solid"
        roundness="none"
        size="xl"
        @click="activeSection = 0"
      />
      <UiEntryInput
        v-model="tagPrompt"
        placeholder="фильтр по тегам"
        variant="ghost"
        style="width: 100%"
        roundness="none"
        size="xl"
      />
      <UiTrident
        v-for="t in filteredTags()"
        v-model="t.state"
        :key="t.value.id"
        :label="t.value.ru"
        start
        variant="ghost"
        size="lg"
        roundness="none"
      />
    </secion>

    <secion v-if="activeSection === 2">
      <UiEntryButton
        label="Назад"
        variant="ghost"
        start
        leading="heroicons:arrow-long-left-16-solid"
        roundness="none"
        size="xl"
        @click="activeSection = 0"
      />
      <UiEntryInput
        v-model="genrePrompt"
        placeholder="фильтр по жанрам"
        variant="ghost"
        style="width: 100%"
        roundness="none"
        size="xl"
      />

      <UiTrident
        v-for="g in filteredGenres()"
        v-model="g.state"
        :key="g.value.id"
        :label="g.value.ru"
        start
        variant="ghost"
        size="lg"
        roundness="none"
      />
    </secion>
  </SidemenuDefault>
</template>

<style lang="scss" scoped>
.o {
  margin: 0 var(--pd);
  max-width: calc(100% - var(--pd) - var(--pd));
}
</style>
