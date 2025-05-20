<template>
  <div class="placeholder"><slot /></div>
</template>

<style lang="scss" scoped>
.placeholder {
  display: inline-flex;
  align-items: center;
  justify-content: space-between;
  flex-shrink: 0;

  --height: calc(var(--hg) * var(--xxxl));
  height: var(--height);
  width: 100vw;

  padding: 0 calc((var(--height) - var(--hg)) / 2);
  background-color: var(--window-bg);
  box-shadow: var(--header-shadow);
  z-index: 1000;
}
</style>
