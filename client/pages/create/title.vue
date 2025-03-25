<script setup>
const store = useCreateTitleStore();

const config = useRuntimeConfig();
const baseUrl = config.public.apiBaseUrl;

const { data: tagsData } = useFetch('/tags', {
  baseURL: config.public.apiBaseUrl,
  cache: 'force-cache',
});
const { data: genresData } = useFetch('/genres', {
  baseURL: config.public.apiBaseUrl,
  cache: 'force-cache',
});


const getTagRows = () => {
  let rows = []
  
  if (tagsData.value) {
    tagsData.value.forEach(element => {
      if (!store.state.tags.includes(element.id)) {
        rows.push({value: element.id, display: element.ru})
      }
    });
  }

  return rows.toSorted()
}

const getGenreRows = () => {
  let rows = []
  
  if (genresData.value) {
    genresData.value.forEach(element => {
      if (!store.state.genres.includes(element.id)) {
        rows.push({value: element.id, display: element.ru})
      }
    });
  }

  return rows.toSorted()
}

onMounted(() => {
  console.log(tagsData, genresData)
})
</script>

<template>
<BodyFormLayout>
  <template v-slot:header>
    <HeaderPseudoHeader>
      <h1>Добавить Тайтл</h1>
      <div class="row">
        <UiDefaultButton 
          caption="Отправить"
          semantic="y"
          @mouseup="store.postForm()"
        />
      </div>
    </HeaderPseudoHeader>
  </template>

  <ComplexFormBlock v-model="store.attention.image">
    <h4>Обложка</h4>
    <UiDefaultImageInput 
      :aspect-ratio="5/7"
      :width="200"
      v-model="store.state.image"
    />
  </ComplexFormBlock>

  <ComplexFormBlock v-model="store.attention.tags">
    <h4>Тэги</h4>
    <div class="buttons-row" v-if="store.state.tags.length > 0">
      <UiDefaultButton 
        icon="heroicons:tag-20-solid"
        v-for="tag in tagsData.filter((v) => store.state.tags.includes(v.id))"
        :caption="tag.ru"
        @mouseup="() => {
          const index = store.state.tags.indexOf(tag.id);
          if (index > -1) {
            store.state.tags.splice(index, 1)
          }
        }"
      />
    </div>
    <ComplexRowMenu
      input-placeholder="поиск по тэгам"
      :empty="!tagsData"
      :rows="getTagRows()"
      empty-placeholder="тут пусто..."
      @select="(id) => {store.state.tags.push(id)}"
    />
  </ComplexFormBlock>

  <ComplexFormBlock v-model="store.attention.genres">
    <h4>Жанры</h4>
    <div class="buttons-row" v-if="store.state.genres.length > 0">
      <UiDefaultButton 
        v-for="genre in genresData.filter((v) => store.state.genres.includes(v.id))"
        :caption="genre.ru"
        @mouseup="() => {
          const index = store.state.genres.indexOf(genre.id);
          if (index > -1) {
            store.state.genres.splice(index, 1)
          }
        }"
      />
    </div>
    <ComplexRowMenu
      input-placeholder="поиск по жанрам"
      :empty="!genresData"
      :rows="getGenreRows()"
      empty-placeholder="тут пусто..."
      @select="(id) => {store.state.genres.push(id)}"
    />
  </ComplexFormBlock>

  <div class="row-50">
    <ComplexFormBlock v-model="store.attention.trStatus">
      <h4>Статус перевода</h4>
      <ComplexDropdownWide 
        :style="{width:'100%'}" 
        :rows="['Закончен', 'Приостановлен', 'Продолжается', 'Заброшен']"
        v-model="store.state.trStatus"
      />
    </ComplexFormBlock>

    <ComplexFormBlock v-model="store.attention.rlStatus">
      <h4>Статус выхода глав</h4>
      <ComplexDropdownWide 
        :style="{width:'100%'}" 
        :rows="['Закончен', 'Приостановлен', 'Продолжается', 'Заброшен']"
        v-model="store.state.rlStatus"
      />
    </ComplexFormBlock>
  </div>

  <div class="row-50">
    <ComplexFormBlock v-model="store.attention.ageRating">
      <h4>Возрастной рейтинг</h4>
      <ComplexDropdownWide 
        :style="{width:'100%'}" 
        :rows="['0+', '12+', '16+', '18+']"
        v-model="store.state.ageRating"
      />
    </ComplexFormBlock>

    <ComplexFormBlock v-model="store.attention.type">
      <h4>Тип тайтла</h4>
      <ComplexDropdownWide 
        :style="{width:'100%'}" 
        :rows="['Манга', 'Манхва', 'Маньхуа']"
        v-model="store.state.type"
      />
    </ComplexFormBlock>
  </div>

  <ComplexFormBlock v-model="store.attention.releaseYear">
    <h4>Год релиза</h4>
    <UiDefaultInput v-model="store.state.releaseYear"/>
  </ComplexFormBlock>

  <ComplexFormBlock v-model="store.attention.ruName">
    <h4>Название на русском</h4>
    <UiDefaultInput v-model="store.state.ruName"/>
  </ComplexFormBlock>
  
  <ComplexFormBlock v-model="store.attention.enName">
    <h4>Название на английском</h4>
    <UiDefaultInput v-model="store.state.enName"/>
  </ComplexFormBlock>

  <ComplexFormBlock v-model="store.attention.orName">
    <h4>Название на языке оригинала</h4>
    <UiDefaultInput v-model="store.state.orName"/>
  </ComplexFormBlock>

  <ComplexFormBlock v-model="store.attention.anName">
    <h4>Другие названия</h4>
    <UiDefaultInput 
      placeholder="разделяйте названия символом ' / '"
      v-model="store.state.anName"
    />
  </ComplexFormBlock>

  <ComplexFormBlock v-model="store.attention.description">
    <h4>Описание</h4>
    <UiDefaultTextArea v-model="store.state.description"/>
  </ComplexFormBlock>

</BodyFormLayout>
</template>

<style lang="scss" scoped>
.row {
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  gap: var(--row-gap-0);
}

.buttons-row {
  display: flex;
  flex-wrap: wrap;
  gap: var(--row-gap-2);
}

.row-50 {
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  gap: var(--row-gap-2);
}
</style>