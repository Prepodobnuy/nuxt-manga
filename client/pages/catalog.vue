<template>
  <div>
    <PageLayout>
      <template v-slot:header>
        <SharedUiPseudoHeader>
          <h1>Каталог</h1>
          <div class="box">
            <SharedUiIconButton class="hide-on-m" icon="heroicons:bars-arrow-down-16-solid" />
            <SharedUiIconCaptionButton class="hide-on-d" icon="heroicons:bars-arrow-down-16-solid" caption="Сортировка" />
            <SharedUiIconCaptionButton class="hide-on-d" icon="heroicons:funnel-solid" caption="Фильтр" />
          </div>
        </SharedUiPseudoHeader>
      </template>
      <div>LOL</div>
    </PageLayout>
  </div>
</template>

<style lang="scss" scoped>

header {
  padding: var(--content-padding);
  width: calc(100% - var(--content-padding) * 2);
  height: calc(100% - var(--content-padding) * 2);

  .box {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    gap: var(--row-gap-1);
  }
}

</style>