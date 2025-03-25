<script setup>
const props = defineProps({
  caption: String,
  anchor: {type: String, default: 'left'}, // left center right
  position: {type: String, default: 'top'}, // top bottom
});

const getClass = () => {
  return [
    `anchor-${props.anchor}`,
    `position-${props.position}`,
  ]
}

const time = 200;
const timeOut = ref(null);

const handleMouseEnter = () => {
  timeOut.value = setTimeout(() => {
    viewTooltip.value=true
  }, time)
}
const handleMouseLeave = () => {
  clearTimeout(timeOut.value)
  viewTooltip.value=false
}

const viewTooltip = ref(false);
</script>

<template>
  <div class="tooltip-placeholder">
    <Transition name="fademoveup">
      <div 
        class="tooltip" 
        :class="getClass()"  
        v-if="caption && viewTooltip"
      >
        <p>{{ caption }}</p>
      </div>
    </Transition>
    <div
      @mouseenter="handleMouseEnter()"
      @mouseleave="handleMouseLeave()"
    >
      <slot></slot>
    </div>
  </div>
</template>

<style lang="scss" scoped>

.tooltip-placeholder {
  position: relative;

  height: max-content;
  width: max-content;
  text-wrap: nowrap;

  .tooltip {
    pointer-events: none;
    user-select: none;
    position: absolute;
    
    z-index: 100;

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
    padding: var(--input-padding);
    border-radius: var(--input-borrad);
    box-shadow: 0 0 5px 1px var(--color-shadow-0);
  
    p {
      font-size: 70%;
    }
  }
}

</style>