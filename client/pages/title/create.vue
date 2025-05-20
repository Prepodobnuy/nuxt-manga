<script lang="ts" setup>
import { EntityPersonEntry, UiInput } from "#components";
import type { PersonFull } from "~/types/person";

const { form, valid, clear, post } = useTitleForm();
const { tags, genres } = useTags();

const tagEntries = computed(() => {
  return tags
    .filter((t) => !form.tags.includes(t.id))
    .map((t) => ({
      display: t.ru,
      select: t.id,
    }));
});

const genreEntries = computed(() => {
  return genres
    .filter((g) => !form.genres.includes(g.id))
    .map((g) => ({
      display: g.ru,
      select: g.id,
    }));
});

const selectTag = (id: number) => {
  form.tags.push(id);
};

const selectGenre = (id: number) => {
  form.genres.push(id);
};

const handlePost = async () => {
  await post();
};

const fetchPerson = async (prompt: string): Promise<PersonFull[]> => {
  const config = useRuntimeConfig();
  const { data } = await useFetch<PersonFull[]>(
    `/api/person/search/${prompt}`,
    {
      baseURL: config.public.apiBase,
    },
  );

  console.clear();
  console.log(data.value);
  return data.value || [];
};

const authorPrompt = ref("");
const artistPrompt = ref("");
const publisherPrompt = ref("");

const authorTimeout = ref(null);
const artistTimeout = ref(null);
const publisherTimeout = ref(null);

const authors = ref<PersonFull[]>([]);
const artists = ref<PersonFull[]>([]);
const publishers = ref<PersonFull[]>([]);

const authorEntries = computed(() => {
  return authors.value
    .filter((v) => v.id !== form.authorId)
    .map((v) => ({
      display: v.meta.name_ru,
      select: v.id,
    }));
});
const artistEntries = computed(() => {
  return artists.value
    .filter((v) => v.id !== form.artistId)
    .map((v) => ({
      display: v.meta.name_ru,
      select: v.id,
    }));
});
const publisherEntries = computed(() => {
  return publishers.value
    .filter((v) => v.id !== form.publisherId)
    .map((v) => ({
      display: v.meta.name_ru,
      select: v.id,
    }));
});

watch(authorPrompt, () => {
  if (authorTimeout.value) {
    clearTimeout(authorTimeout.value);
  }
  if (authorPrompt.value.length > 2) {
    authorTimeout.value = setTimeout(async () => {
      const authorsData = await fetchPerson(authorPrompt.value);
      authors.value = authorsData;
    }, 600);
    return;
  }
});
watch(artistPrompt, () => {
  if (artistTimeout.value) {
    clearTimeout(artistTimeout.value);
  }
  if (artistPrompt.value.length > 2) {
    artistTimeout.value = setTimeout(async () => {
      const artistsData = await fetchPerson(artistPrompt.value);
      artists.value = artistsData;
    }, 600);
    return;
  }
});
watch(publisherPrompt, () => {
  if (publisherTimeout.value) {
    clearTimeout(publisherTimeout.value);
  }
  if (publisherPrompt.value.length > 2) {
    publisherTimeout.value = setTimeout(async () => {
      const publishersData = await fetchPerson(publisherPrompt.value);
      publishers.value = publishersData;
    }, 600);
    return;
  }
});

const author = computed((): PersonFull | null => {
  if (form.authorId === undefined) return null;
  const val = authors.value.filter((v) => v.id === form.authorId);
  if (val.length === 0) return null;
  return val[0];
});
const artist = computed(() => {
  if (form.artistId === undefined) return null;
  const val = artists.value.filter((v) => v.id === form.artistId);
  if (val.length === 0) return null;
  return val[0];
});
const publisher = computed(() => {
  if (form.publisherId === undefined) return null;
  const val = publishers.value.filter((v) => v.id === form.publisherId);
  if (val.length === 0) return null;
  return val[0];
});

const selectAuthor = (id: number) => {
  form.authorId = id;
};
const selectArtist = (id: number) => {
  form.artistId = id;
};
const selectPublisher = (id: number) => {
  form.publisherId = id;
};

const unselectAuthor = (id: number) => {
  form.authorId = undefined;
};
const unselectArtist = (id: number) => {
  form.artistId = undefined;
};
const unselectPublisher = (id: number) => {
  form.publisherId = undefined;
};
</script>

<template>
  <LayoutPseudoHeader>
    <template #header>
      <h4>Добавление Тайтла</h4>
    </template>

    <div class="content">
      <UiFormBlock :active="!valid.covers" @click="valid.covers = true">
        <h6>Обложки</h6>
        <UiMultipleImageInput
          v-model="form.covers"
          :height="254.5"
          :aspect="1080 / 1527"
          variant="outline"
        />
      </UiFormBlock>

      <UiFormBlock
        label="Заполните поле"
        :active="!valid.titleRu"
        @click="valid.titleRu = true"
      >
        <h6>Название на русском</h6>
        <UiInput v-model="form.titleRu" variant="outline" placeholder="" />
      </UiFormBlock>

      <UiFormBlock
        label="Заполните поле"
        :active="!valid.titleEn"
        @click="valid.titleEn = true"
      >
        <h6>Название на английском</h6>
        <UiInput v-model="form.titleEn" variant="outline" placeholder="" />
      </UiFormBlock>

      <UiFormBlock :active="!valid.titleJp" @click="valid.titleJp = true">
        <h6>Название на языке оригинала</h6>
        <UiInput v-model="form.titleJp" variant="outline" placeholder="" />
      </UiFormBlock>

      <UiFormBlock>
        <h6>Альтернативные названия</h6>
        <UiInput
          v-model="form.titleAn"
          variant="outline"
          placeholder="вводите названия разделяя их символом ' / '"
        />
      </UiFormBlock>

      <UiFormBlock>
        <h6>Описание</h6>
        <UiTextarea v-model="form.description" variant="outline" />
      </UiFormBlock>

      <UiFormBlock
        :active="!valid.releaseYear"
        @click="valid.releaseYear = true"
      >
        <h6>Дата выхода</h6>
        <UiInput v-model="form.releaseYear" variant="outline" />
      </UiFormBlock>

      <UiFormBlock>
        <h6>Тэги</h6>
        <div v-if="form.tags.length > 0" class="tags-row">
          <UiButton
            v-for="(id, pos) in form.tags"
            variant="outline"
            :key="id"
            :label="tags[id - 1].ru"
            :fw="false"
            @click="form.tags.splice(pos, 1)"
          />
        </div>
        <UiSelectMenu :entries="tagEntries" @select="selectTag" />
      </UiFormBlock>

      <UiFormBlock>
        <h6>Жанры</h6>
        <div v-if="form.genres.length > 0" class="tags-row">
          <UiButton
            v-for="(id, pos) in form.genres"
            variant="outline"
            :key="id"
            :label="genres[id - 1].ru"
            :fw="false"
            @click="form.genres.splice(pos, 1)"
          />
        </div>
        <UiSelectMenu :entries="genreEntries" @select="selectGenre" />
      </UiFormBlock>

      <UiFormBlock :active="!valid.authorId" @click="valid.authorId = true">
        <h6>Автор</h6>
        <EntityPersonEntry
          v-if="author"
          :person="author"
          @click="unselectAuthor"
        />
        <UiSelectMenu
          v-model="authorPrompt"
          :entries="authorEntries"
          @select="selectAuthor"
        />
      </UiFormBlock>

      <UiFormBlock :active="!valid.artistId" @click="valid.artistId = true">
        <h6>Художник</h6>
        <EntityPersonEntry
          v-if="artist"
          :person="artist"
          @click="unselectArtist"
        />
        <UiSelectMenu
          v-model="artistPrompt"
          :entries="artistEntries"
          @select="selectArtist"
        />
      </UiFormBlock>

      <UiFormBlock
        :active="!valid.publisherId"
        @click="valid.publisherId = true"
      >
        <h6>Издатель</h6>
        <EntityPersonEntry
          v-if="publisher"
          :person="publisher"
          @click="unselectPublisher"
        />
        <UiSelectMenu
          v-model="publisherPrompt"
          :entries="publisherEntries"
          @select="selectPublisher"
        />
      </UiFormBlock>

      <div class="row">
        <div style="width: 200%" />
        <UiButton label="Очистить" variant="outline" @click="clear()" />
        <UiButton label="Отправить" color="success" @click="handlePost()" />
      </div>
    </div>
  </LayoutPseudoHeader>
</template>

<style lang="scss" scoped>
@use "@/assets/mixins";
@use "@/assets/variables";
@use "@/assets/functions";

.content {
  @include mixins.form-content;
  padding: 20px;
  gap: var(--gap);
}

.row {
  display: inline-flex;
  gap: var(--gap);
  margin-top: 1em;
}

.tags-row {
  display: flex;
  gap: var(--gap);
  flex-wrap: wrap;
}
</style>
