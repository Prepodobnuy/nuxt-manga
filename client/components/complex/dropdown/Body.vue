<script setup>
const props = defineProps({
  anchor: {type: String, default: 'left'}, // left center right
  position: {type: String, default: 'top'}, // top bottom
});

const getClass = () => {
  return [
    `anchor-${props.anchor}`,
    `position-${props.position}`,
  ]
}

const viewDropDown = ref(false);
const dropdownRef = ref(null);
const buttonRef = ref(null);

const handleClickOutside = (event) => {
  if (
    dropdownRef.value && !dropdownRef.value.contains(event.target)
    &&
    buttonRef.value && !buttonRef.value.contains(event.target)
  ) {
    viewDropDown.value = false;
  }
};

onMounted(() => {
  document.addEventListener('click', handleClickOutside);
});

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside);
});
</script>

<template>
  <div class="dropdown">
    <div ref="buttonRef" @click="viewDropDown=!viewDropDown">
      <slot name="head"></slot>
    </div>

    <Transition name="fademoveup">
      <menu ref="dropdownRef" v-if="viewDropDown" :class="getClass()">
        <slot></slot>
      </menu>
    </Transition>
  </div>
</template>

<style lang="scss">
.dropdown {
  position: relative;
}

menu {
  position: absolute;
  
  display: flex;
  flex-direction: column;

  z-index: 200;

  overflow: hidden;

  width: max-content;

  padding-left: 0;
  margin-left: 0;

  &.anchor-left {
    left: 0;
  }
  &.anchor-center {
    left: 50%;
    transform: translateX(-50%);
  }
  &.anchor-right {
    left: unset;
    right: 0;
  }
  &.position-bottom {
    top: calc(100% + var(--row-gap-2));
  }
  &.position-top {
    bottom: calc(100% + var(--row-gap-2));
  }

  background-color: var(--color-background-8);
  border-radius: var(--input-borrad);
  box-shadow: 0 0 5px 1px var(--color-shadow-0);
}
</style>
