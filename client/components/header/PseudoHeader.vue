<template>
  <header>
    <slot></slot>
  </header>
</template>

<style lang="scss" scoped>
@use '../../assets/variables/breakpoints.scss';

header {
  position: relative;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  padding: var(--input-padding);
  justify-content: space-between;
  align-items: start;
}

@media (max-width: calc(#{breakpoints.$mobile-break-point} - 1px)) {
  header {
    box-shadow: unset;
    align-items: center;
  }
}
</style>