<script setup>
const emit = defineEmits(['showSearch']);
</script>
<template>

  <header>
    <div class="contaiment">
      <div class="row">
        <NuxtLink to="/">
          <UiDefaultNavButton caption="Главная" icon="heroicons:home-solid" />
        </NuxtLink>
      </div>
      
      <nav>
        <NuxtLink to="/catalog">
          <UiDefaultNavButton caption="Каталог" icon="heroicons:squares-2x2-16-solid" />
        </NuxtLink>
        <UiDefaultNavButton caption="Поиск" icon="heroicons:magnifying-glass-16-solid" @click="emit('showSearch')" />
      </nav>
      
      <div class="row">
        <ComplexDropdownBody
          anchor="right"
          position="bottom"
        >
          <template v-slot:head>
            <UiDefaultIconButton icon="heroicons:pencil-square-solid" /> <!--Add menu-->
          </template>
          
          <NuxtLink to="/create/title"><ComplexDropdownEntry>Добавить Тайтл</ComplexDropdownEntry></NuxtLink>
          <NuxtLink to="/create/person"><ComplexDropdownEntry>Добавить Персону</ComplexDropdownEntry></NuxtLink>
          <NuxtLink to=""><ComplexDropdownEntry>Панель Модерации</ComplexDropdownEntry></NuxtLink>
        </ComplexDropdownBody>

        <UiDefaultIconButton icon="heroicons:bell-solid" /> <!--Notifications-->

        <ComplexDropdownBody
          anchor="right"
          position="bottom"
        > 
          <template v-slot:head>
            <UiDefaultIconButton icon="heroicons:user-16-solid" /> <!--Profile-->
          </template>
          <NuxtLink to="/auth/register"><ComplexDropdownEntry>Регистрация</ComplexDropdownEntry></NuxtLink>
          <NuxtLink to="/auth/login"><ComplexDropdownEntry>Вход</ComplexDropdownEntry></NuxtLink>
        </ComplexDropdownBody>

        <UiDefaultIconButton 
          :icon="$colorMode.preference === 'light' ? 'heroicons:sun-16-solid' : 'heroicons:moon-16-solid'" 
          @click="$colorMode.preference = $colorMode.value === 'dark' ? 'light' : 'dark'"
        /> <!--Theme-->
        <UiDefaultIconButton icon="heroicons:cog-6-tooth-solid" /> <!--Menu-->
      </div>
    </div>
  </header>

</template>

<style lang="scss" scoped>
@use 'sass:color';

header {
  position: fixed;
  display: flex;

  justify-content: center;

  left: 0;
  top: 0;
  width: 100%;
  height: var(--header-height);
  z-index: 1000;
  background-color: var(--color-background-8);
}

.contaiment {
  position: relative;
  display: flex;
  padding: 0 var(--row-gap-1);
  flex-direction: row;
  justify-content: space-between;

  max-width: var(--header-content-width);
  width: 100%;
  height: var(--header-height);

  .row, nav {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    align-items: center;
    gap: var(--row-gap-1);
    height: 100%;
  }

  .row {
  }

  nav {
    position: absolute;

    top: 0;
    left: 50%;
    transform: translateX(-50%);
    height: var(--header-height);
  }
}



</style>