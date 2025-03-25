<script setup>
const store = useSearchStore();

const searchEntities = [
  'Тайтла',
  'Персоны',
  'Пользователя',
]
const emit = defineEmits(['exit']);

const viewParams = ref(false);

const getPlaceholder = () => {
  return 'Поиск ' +  searchEntities[store.searchIndex]
};
</script>

<template>
  <div class="searchmenu-place">
    <article>
      
      <div class="row">
        <UiWideInput :placeholder="getPlaceholder()" v-model="store.prompt"/>
        <UiWideButton class="aspect" icon="heroicons:funnel-solid" :checked="viewParams" @click="viewParams=!viewParams" />
        <UiWideButton class="aspect" icon="heroicons:x-mark-16-solid" @click="emit('exit')" />
      </div>
  
      <div class="row" v-if="viewParams">
        <UiWideButton :checked="store.searchIndex==0" @click="store.searchIndex=0" :thin="true" caption="Тайтл" />
        <UiWideButton :checked="store.searchIndex==1" @click="store.searchIndex=1" :thin="true" caption="Персона" />
        <UiWideButton :checked="store.searchIndex==2" @click="store.searchIndex=2" :thin="true" caption="Пользователь" />
      </div>

      <div class="results">
        <ComplexUiWideTitle 
          bg-url="https://upload.wikimedia.org/wikipedia/ru/f/f1/Makima_cover.jpeg"
          title="Человек Бензопила"
          author="Тацуки Фуджимото"
          type="Манга"
        />
        <ComplexUiWideTitle 
          bg-url="https://m.media-amazon.com/images/I/917IJDfk36L.jpg"
          title="Спокойной ночи, Пунпун"
          author="Инио Асано"
          type="Манга"
        />
        <ComplexUiWideTitle 
          bg-url="https://m.media-amazon.com/images/I/915iJ+j4NzL._AC_UF1000,1000_QL80_.jpg"
          title="Я теперь Мари"
          author="OSHIMI Shuzo"
          type="Манга"
        />
        <ComplexUiWideTitle 
          bg-url="https://m.media-amazon.com/images/I/81VkApOiIdL.jpg"
          title="Гомункул"
          author="Hideo Yamamoto"
          type="Манга"
        />
        <ComplexUiWideTitle 
          bg-url="https://m.media-amazon.com/images/I/81NTOyDG5RL._AC_UF1000,1000_QL80_.jpg"
          title="Адский рай"
          author="Yuuji Kaku"
          type="Манга"
        />
        <ComplexUiWideTitle 
          bg-url="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1489770887i/34614205.jpg"
          title="Одзанари Кун"
          author="Inio Asano"
          type="Манга"
        />
        <ComplexUiWideTitle 
          bg-url="https://shikimori.one/uploads/poster/mangas/463/main_2x-10b6a51f03bedcbbc0aad6ac90002611.webp"
          title="Добро пожаловать в NHK"
          author="TAKIMOTO Tatsuhiko"
          type="Манга"
        />
      </div>

    </article>
  </div>
</template>

<style lang="scss" scoped>
.searchmenu-place {
  --margin: calc( (var(--header-height) - var(--entry-height)) / 2 );
  
  position: fixed;
  display: flex;
  justify-content: center;
  pointer-events: none;
  z-index: 2000;
  width: 100vw;
  height: calc(100vh - var(--margin) - var(--margin));
  overflow: hidden;
  left: 0;
  top: var(--margin);
}

article {
  width: var(--tiny-content-width);
  display: flex;
  flex-direction: column;
  gap: var(--row-gap-2);
  pointer-events: all;
  padding: 0 20px;

  .row {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    gap: var(--row-gap-2);
    * {
      justify-content: center;
    }
  }

  .results {
    display: flex;
    flex-direction: column;
    gap: var(--row-gap-2);
    overflow-y: auto;
    height: 100%;

    * {
      flex-shrink: 0;
    }
  }
}

.aspect {
  aspect-ratio: 1/1;
  width: unset;
  padding: unset;
  flex-shrink: 0;
}
</style>