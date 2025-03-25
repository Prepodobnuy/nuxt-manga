<template>
<BodyAsideLayout :reverse="true" aside-width="260px" :transparent-aside="true">
  <template v-slot:header>
    <HeaderPseudoHeader>
      <h1>Спокойной ночи, Пунпун</h1>
      <UiDefaultButton icon="heroicons:star-solid" caption="Оценить" />
    </HeaderPseudoHeader>
  </template>

  <template v-slot:main>
  
    <UiDefaultHiddenText 
      title="Раскрыть описание"
      hidden-title="Скрыть"
      caption="Пунпун — обыкновенный 11-летний школьник из Японии. Честный идеалист и неисправимый романтик, главный герой наблюдает, как быстро меняется его жизнь, когда в его класс приходит новая девочка Айко Танака. Мальчик узнает, насколько хрупкими могут быть отношения и как трудно бывает отказаться от иллюзий наивного детства. Когда однажды Пунпун становится свидетелем того, как его отец обижает мать, он выносит для себя новый урок: те, кого он когда-то считал для себя примером, оказались вовсе не такими, как он думал. Это глубокая история мангаки Инио Асано о взрослении и адаптации, полная противоречивых эмоций и трудноразрешимых проблем."
    />
    <div>
      
    </div>
  
  </template>
  
  <template v-slot:aside>
    <div class="cover">
      <NuxtImg src="https://m.media-amazon.com/images/I/917IJDfk36L.jpg" />
      <div class="actions">
        <UiThinTooltip anchor="center" caption="Изменить данные">
          <UiDefaultIconButton icon="heroicons:pencil-square-20-solid" />
        </UiThinTooltip>
        <UiThinTooltip anchor="center" caption="Добавить главы">
          <UiDefaultIconButton icon="heroicons:plus-circle-20-solid" />
        </UiThinTooltip>
        <UiThinTooltip anchor="center" caption="Сообщение модератору" >
          <UiDefaultIconButton icon="heroicons:exclamation-triangle-20-solid" />
        </UiThinTooltip>
      </div>
    </div>

    <ComplexUiWideReadButton 
      iconWidth="16px" 
      icon="heroicons:book-open-solid" 
      :current-chapter="12"
      :chapters="55"
      :thin="true" 
    />
    <!--
      <ComplexUiWideRateButton 
        iconWidth="16px" 
        icon="heroicons:star-solid" 
        :rate="10"
        :thin="true" 
      />
    -->
    <ComplexUiWideListButton 
      iconWidth="16px"
      icon="heroicons:document-plus-20-solid" 
      list="Прочитано"
      :thin="true" 
    />

    <div class="meta">
      <div class="block">
        <p class="head">Тип</p>
        <p>Манга</p>
      </div>
      <div class="block">
        <p class="head">Возрастной рейтинг</p>
        <p>18+</p>
      </div>
      <div class="block">
        <p class="head">Автор</p>
        <p>Инио Асано</p>
      </div>
      <div class="block">
        <p class="head">Издатель</p>
        <p>Shogakukan</p>
      </div>
      <div class="block">
        <p class="head">Название на английском</p>
        <p>Goodnight, Punpun</p>
      </div>
      <div class="block">
        <p class="head">Название на языке оригинала</p>
        <p>Oyasumi Punpun</p>
      </div>
      <div class="block">
        <p class="head">Альтернативные названия</p>
        <p>чин чан чон</p>
        <p>пока бунбун</p>
        <p>усни bonbon</p>
      </div>
    </div>
  </template>

</BodyAsideLayout>
</template>

<style lang="scss" scoped>


.cover {
  position: relative;
  border-radius: var(--input-borrad);
  user-select: none;

  img {
    width: 100%;
    border-radius: var(--input-borrad);
  }

  div.actions {
    position: absolute;
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    align-items: center;
    justify-content: space-evenly;

    background-color: var(--color-background-8);
    height: var(--thin-entry-height);
    width: 100%;
    border-radius: 0 0 var(--input-borrad) var(--input-borrad);

    bottom: 0;
    left: 0;
  }
}

div.meta {
  display: flex;
  flex-direction: column;

  background-color: var(--color-background-8);
  padding: 5px;
  border-radius: var(--input-borrad);
  gap: var(--row-gap-3);

  div.block {
    display: flex;
    flex-direction: column;
    gap: var(--row-gap-1);
    padding: 5px;

    p {
      opacity: 1;
      line-height: 1;
      font-size: 85%;

      &.head {
        opacity: 0.7;
      }
    }
  }

}

</style>