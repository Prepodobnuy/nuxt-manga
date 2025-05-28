<script setup lang="ts">
const { form, includeTags, excludeTags, includeGenres, excludeGenres, clear } =
  useCatalogStore();

const tagPrompt = ref("");
const genrePrompt = ref("");
const filteredTags = () => form.tags.filter((v) => v);
const filteredGenres = () => form.genres.filter((v) => v);

const activeSection = ref(0);
</script>

<template>
  <aside>
    <section v-if="activeSection === 0">
      <UiButton
        variant="ghost"
        start
        roundness="none"
        @click="activeSection = 1"
      >
        Тэги
        <div style="width: 100%" />
        <p style="flex-shrink: 0; font-size: 0.95em">
          {{ includeTags().length + excludeTags().length }} /
          {{ form.tags.length }}
        </p>
      </UiButton>
      <UiButton
        variant="ghost"
        start
        roundness="none"
        @click="activeSection = 2"
      >
        Жанры
        <div style="width: 100%" />
        <p style="flex-shrink: 0; font-size: 0.95em">
          {{ includeGenres().length + excludeGenres().length }} /
          {{ form.genres.length }}
        </p>
      </UiButton>

      <div style="height: 16px" />

      <p style="margin: var(--gap); font-size: 0.95em">Год Релиза</p>
      <UiRange
        style="margin: 0 var(--gap)"
        v-model:minm="form.release_year_min"
        v-model:maxm="form.release_year_max"
        :min="1900"
        :max="2025"
        size="sm"
      />

      <p style="margin: var(--gap); font-size: 0.95em">Оценка</p>
      <p>
        <UiRange
          style="margin: 0 var(--gap)"
          v-model:minm="form.rate_min"
          v-model:maxm="form.rate_max"
          :min="1"
          :max="5"
          size="sm"
        />
      </p>

      <UiButton
        label="Очистить"
        variant="ghost"
        roundness="none"
        start
        @click="clear()"
      />
    </section>

    <section v-if="activeSection === 1">
      <div style="display: inline-flex; width: 100%">
        <UiButton
          label="Назад"
          variant="ghost"
          start
          leading="heroicons:arrow-long-left-16-solid"
          roundness="none"
          @click="activeSection = 0"
        />
        <UiButton
          style="flex-shrink: 0"
          leading="heroicons:arrow-path-16-solid"
          icon
          variant="ghost"
          roundness="none"
        />
      </div>
      <UiInput
        v-model="tagPrompt"
        placeholder="фильтр"
        variant="ghost"
        style="width: 100%"
        roundness="none"
      />
      <UiTrident
        v-for="t in filteredTags()"
        v-model="t.state"
        :key="t.value.id"
        :label="t.value.ru"
        start
        variant="ghost"
        roundness="none"
      />
    </section>

    <section v-if="activeSection === 2">
      <div style="display: inline-flex; width: 100%">
        <UiButton
          label="Назад"
          variant="ghost"
          start
          leading="heroicons:arrow-long-left-16-solid"
          roundness="none"
          @click="activeSection = 0"
        />
        <UiButton
          style="flex-shrink: 0"
          leading="heroicons:arrow-path-16-solid"
          icon
          variant="ghost"
          roundness="none"
        />
      </div>
      <UiInput
        v-model="genrePrompt"
        placeholder="фильтр"
        variant="ghost"
        style="width: 100%"
        roundness="none"
      />
      <UiTrident
        v-for="g in filteredGenres()"
        v-model="g.state"
        :key="g.value.id"
        :label="g.value.ru"
        start
        variant="ghost"
        roundness="none"
      />
    </section>
  </aside>
</template>

<style lang="scss" scoped>
aside {
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  width: 300px;
  overflow-y: auto;

  max-height: calc(100vh - 40px - 58px);

  background-color: color-mix(in srgb, transparent 60%, var(--neutral-bg) 30%);
  box-shadow: inset 0 0 0 1px var(--neutral-bg);
  border-radius: var(--br);
}
</style>
