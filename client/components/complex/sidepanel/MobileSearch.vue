<script setup>
const store = useSearchStore();

const searchEntities = [
  'Тайтл',
  'Персону',
  'Пользователя',
]

const viewParams = ref(false);

const getCaption = () => {
  return viewParams.value ? 'Искать' : 'Искать ' +  searchEntities[store.searchIndex]
};
</script>

<template>
  <ComplexSideMenu>
    <UiWideInput
      placeholder="Поиск"
      v-model="store.prompt"
    />
    <UiWideButton 
      :caption="getCaption()"
      :checked="viewParams"
      icon="heroicons:funnel-solid"
      @mouseup="viewParams = !viewParams"
      :reverse="true"
      :space-between="true"
    />
    <UiWideButton 
      v-if="viewParams"
      v-for="(value, index) in searchEntities"
      :caption="value"
      :checked="index == store.searchIndex"
      @mouseup="store.searchIndex = index"
    />
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
  </ComplexSideMenu>
</template>

<style lang="scss" scoped>

</style>