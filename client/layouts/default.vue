<script setup>
const viewValue = ref(null);
const viewEnum = reactive({
  search: 0,
  mainmenu: 1,
});

watch(viewValue, (newValue) => {
  if (newValue !== null) {
    document.body.classList.add('locked');
  } else {
    document.body.classList.remove('locked');
  }
});
</script>

<template>
  <Transition name="fade">
    <div class="blank" v-if="viewValue!==null" @mousedown="viewValue=null"></div>
  </Transition>
  <Transition name="moveright">
    <ComplexSidepanelMobileSearch v-if="viewValue==viewEnum.search" class="hide-on-d" />
  </Transition>
  <Transition name="moveleft">
    <ComplexSidepanelMobileMain v-if="viewValue==viewEnum.mainmenu" class="hide-on-d" />
  </Transition>
  <Transition name="movedown">
    <ComplexSearchMenu v-if="viewValue==viewEnum.search" class="hide-on-m" @exit="viewValue=null" />
  </Transition>


  <HeaderDesktop class="hide-on-m" 
    @showSearch="viewValue=viewEnum.search"
  />
  <div class="default-layout-placeholder" :class="{ locked : viewValue !== null }">
    <slot>
    </slot>
  </div>
  <HeaderMobile class="hide-on-d" 
    @showSearch="viewValue=viewEnum.search"
    @showMainMenu="viewValue=viewEnum.mainmenu"
  />
</template>

<style lang="scss" scoped>

.blank {
  position: fixed;

  top: 0;
  left: 0;
  z-index: 1999;

  width: 100vw;
  height: 100vh;

  background-color: var(--color-shadow-0);
}

</style>