<script setup>
const props = defineProps({
  loaded: { type: Boolean, default: true },
  reverse: { type: Boolean, default: false },
  asideWidth: { type: String, default: '300px' },
  transparentAside: { type: Boolean, default: false },
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

    <div class="split__" :class="{ reverse : reverse }">
      
      <div class="content__" :class="getClass()">
  
        <div class="header__slot" :class="getHeaderClass()">
          <slot name="header"></slot>
        </div>
  
        <div class="main__slot" :class="getContentClass()">
          <slot name="main"></slot>
        </div>
        
      </div>
  
      <div class="aside__slot" :class="{ transparent : transparentAside }" :style="{width:asideWidth}">
        <slot name="aside"></slot>
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

  .split__ {
    display: flex;
    flex-direction: row;

    &.reverse {
      flex-direction: row-reverse;
    }

    flex-wrap: nowrap;
    max-width: var(--content-width);
    width: 100%;
    padding: 20px;

    align-items: start;

    gap: 20px;

    .content__ {
      position: relative;
      display: flex;
    
      flex-direction: column;
      align-items: center;

      max-width: var(--content-width);
      width: 100%;
      height: max-content;
      flex-shrink: 1;
    }
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
  gap: var(--row-gap-2);
}

.aside__slot {
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
  background-color: var(--color-background-5);
  border-radius: var(--content-borrad);
  padding: 5px;
  gap: var(--row-gap-2);

  &.transparent {
    padding: 0;
    border-radius: unset;
    background-color: transparent;
    gap: 10px;
  }
}

@media (max-width: calc(#{breakpoints.$mobile-break-point} - 1px)) {
  .wrapper__ {
    .split__ {
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

  .aside__slot {
    display: none;
  }
}
</style>