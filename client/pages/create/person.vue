<script setup>
import { BodyFormLayout } from '#components';

const store = useCreatePersonStore();
</script>

<template>
<BodyFormLayout>
  <template v-slot:header>
    <HeaderPseudoHeader>
      <h1>Добавить Персону</h1>
      <div class="row">
        <UiDefaultButton 
          caption="Отправить"
          semantic="y"
          @mousedown="store.postForm()"
        />
      </div>
    </HeaderPseudoHeader>
  </template>

  <ComplexFormBlock v-model="store.attention.image">
    <h4>Фото</h4>
    <UiDefaultImageInput 
      :aspect-ratio="5/7"
      :width="200"
      v-model="store.state.image"
    />
  </ComplexFormBlock>


  <ComplexFormBlock v-model="store.attention.ruName">
    <h4>Имя на русском</h4>
    <UiDefaultInput v-model="store.state.ruName"/>
  </ComplexFormBlock>
  
  <ComplexFormBlock v-model="store.attention.enName">
    <h4>Имя на английском</h4>
    <UiDefaultInput v-model="store.state.enName"/>
  </ComplexFormBlock>

  <ComplexFormBlock v-model="store.attention.orName">
    <h4>Имя на языке оригинала</h4>
    <UiDefaultInput v-model="store.state.orName"/>
  </ComplexFormBlock>

  <ComplexFormBlock v-model="store.attention.type">
    <h4>Тип</h4>
    <UiDefaultInput 
      v-model="store.state.type" 
      placeholder="мангака / художник / издательство / персонаж"
    />
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
</style>