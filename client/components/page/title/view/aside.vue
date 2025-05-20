<script lang="ts" setup>
const covers = [
  "https://m.media-amazon.com/images/I/917IJDfk36L.jpg",
  "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1474824314i/29499014.jpg",
  "https://images.booksense.com/images/229/586/9781421586229.jpg",
];

const rateHandle = () => {};
const metaChangeHandle = () => {};
const volumeChangeHandle = () => {};
const reportHandle = () => {};

const actions = [
  {
    label: "Оценить",
    leading: "heroicons:star-16-solid",
    handle: () => rateHandle(),
  },
  {
    label: "Изменить данные",
    leading: "heroicons:pencil-solid",
    handle: () => metaChangeHandle(),
  },
  {
    label: "Добавить главы",
    leading: "heroicons:paint-brush-20-solid",
    handle: () => volumeChangeHandle(),
  },
  {
    label: "Пожаловаться",
    leading: "heroicons:exclamation-triangle-16-solid",
    handle: () => reportHandle(),
  },
];
</script>
<template>
  <aside>
    <div class="image">
      <UiImageCarousel class="img" width="257" height="364" :images="covers" />
      <div class="actions">
        <UiTooltip
          v-for="(action, index) in actions"
          :key="`${action}${index}`"
          :label="action.label"
          vertical="top"
          horizontal="center"
        >
          <UiButton
            icon
            variant="ghost"
            :leading="action.leading"
            @click="action.handle"
          />
        </UiTooltip>
      </div>
    </div>
    <PageTitleViewReadButton />
    <PageTitleViewListButton />
    <PageTitleViewMeta />
  </aside>
</template>

<style lang="scss" scoped>
aside {
  position: relative;
  width: 257px;
  display: flex;
  flex-direction: column;
  gap: calc(var(--gap) * var(--xxl));

  .image {
    display: flex;
    flex-direction: column;

    .img {
      border-radius: var(--br) var(--br) 0 0;
    }
    .actions {
      border-radius: 0 0 var(--br) var(--br);
      background-color: var(--neutral-bg);
      height: calc(var(--hg) * var(--xl));
      padding: calc(calc(calc(var(--hg) * var(--xl)) - var(--hg)) / 2);
      width: 100%;

      align-items: center;
      display: inline-flex;
      justify-content: space-between;
    }
  }
}
</style>
