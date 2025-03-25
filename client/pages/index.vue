<script setup>
const a = ref('');
const b = ref(0);
const c = ref(false);
</script>

<template>
  <BodyDefaultLayout>
    <template v-slot:header>
      <HeaderPseudoHeader>
        <h1>Главная</h1>
      </HeaderPseudoHeader>
    </template>

    <h1>Title entry</h1>
    <ComplexUiWideTitle 
      bg-url="https://upload.wikimedia.org/wikipedia/ru/f/f1/Makima_cover.jpeg"
      title="Человек Бензопила"
      author="Тацуки Фуджимото"
      type="Манга"
    />
    <ComplexUiWideTitle 
      bg-url="https://i.pinimg.com/550x/84/af/25/84af25ce4b44a43fe6f84a4e39c890c3.jpg"
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

    <h1>Person entry</h1>
    <ComplexUiWidePerson 
      bg-url="https://hibari.rgub.ru/wp-content/uploads/2015/11/08_Inio.jpg"
      name="Инио Асано"
    />

    <h1>User entry</h1>
    <ComplexUiWideUser 
      bg-url="https://pikuco.ru/upload/test_stable/6a6/6a6adefb9ee790654ce7cef945ea0f1e.webp"
      name="Лох 2007"
    />

    <h1>Header Entry</h1>
    <UiWideHeader 
      caption="Заголовок"
    />
    <UiWideHeader 
      caption="Заголовок c иконкой"
      icon="heroicons:academic-cap-solid"
    />

    <h1>Input Entry</h1>
    <UiWideInput 
      placeholder="Текст"
    />
    <UiWideInput 
      placeholder="Пароль"
      type="password"
    />
    <UiWideInput 
      placeholder="Реактивный текст"
      v-model="a"
    />
    <p>{{ a }}</p>

    <h1>Button Entry</h1>
    <UiWideButton 
      :caption="'НАЖАЛ ' + b + ' РАЗ'"
      @click="b += 1"
    />
    <UiWideButton 
      caption="Кнопка с иконкой :>"
      icon="heroicons:at-symbol-16-solid"
    />
    <UiWideButton 
      caption="Переключаемая кнопка"
      :checked="c"
      @click="c=!c"
    />

    <h1>Tooltips</h1>

    <UiThinTooltip
      caption="Anchor left"
      anchor="left"
      position="bottom"
    > <p>1</p> </UiThinTooltip>

    <UiThinTooltip
      caption="Anchor center"
      anchor="center"
      position="bottom"
    > <p>2</p> </UiThinTooltip>

    <UiThinTooltip
      caption="Anchor right"
      anchor="right"
      position="bottom"
    > <p>3</p> </UiThinTooltip>

    <UiThinTooltip
      caption="Anchor left"
      anchor="left"
    > <p>4</p> </UiThinTooltip>

    <UiThinTooltip
      caption="Anchor center"
      anchor="center"
    > <p>5</p> </UiThinTooltip>

    <UiThinTooltip
      caption="Anchor right"
      anchor="right"
    > <p>6</p> </UiThinTooltip>

  </BodyDefaultLayout>
</template>