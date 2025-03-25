<script setup>
const props = defineProps({
  loaded: { type: Boolean, default: true },
});

const getClass = () => {
  return {
    skeleton : !props.loaded
  }
}
const getHeaderClass = () => {
  return {
    skeletonHeader : !props.loaded
  }
}
const getContentClass = () => {
  return {
    skeletonContent : !props.loaded
  }
}
</script>

<template>
  <div class="wrapper__">
    <div class="content__" :class="getClass()">
      <div class="header__slot" :class="getHeaderClass()">
        <slot name="header"></slot>
      </div>
      <div class="main__slot" :class="getContentClass()">
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@use '../../assets/variables/breakpoints.scss';

.wrapper__ {
  width: 100vw;
  display: flex;
  flex-direction: column;
  align-items: center;

  .content__ {
    position: relative;
    display: flex;
    padding: 20px;
  
    flex-direction: column;
    align-items: center;
  
    max-width: var(--tiny-content-width);
    width: 100%;
    height: max-content;
  }
}


.header__slot {
  height: var(--pseudo-header-height);
  max-height: var(--pseudo-header-height);
  background-color: var(--color-background-5);
  width: 100%;
  border-radius: var(--content-borrad) var(--content-borrad) 0 0;
}

.main__slot {
  display: flex;
  flex-direction: column;
  background-color: var(--color-background-5);
  width: 100%;
  border-radius: 0 0 var(--content-borrad) var(--content-borrad);
  padding: 5px;
  gap: var(--row-gap-6);
}

@media (max-width: calc(#{breakpoints.$mobile-break-point} - 1px)) {
  .wrapper__ {
    .content__ {
      padding: 0;
    }
  }

  .header__slot {
    height: var(--header-height);
    max-height: var(--header-height);
    position: fixed;
    z-index: 1000;
    left: 0;
    top: 0;
    background-color: var(--color-background-8);
    border-radius: unset;
  }

  .main__slot {
    margin-top: var(--header-height);
    background-color: var(--color-background-6);
    max-width: var(--mobile-content-width);
    width: 100%;
    padding: 20px 10px;
    border-radius: unset;
  }
}
</style>