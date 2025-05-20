<script lang="ts" setup></script>
<template>
  <div class="split">
    <PageTitleViewAside />
    <PageTitleViewMain />
  </div>
</template>

<style lang="scss" scoped>
.split {
  position: relative;
  display: inline-flex;
  gap: calc(var(--gap) * var(--xxl));
}
</style>
