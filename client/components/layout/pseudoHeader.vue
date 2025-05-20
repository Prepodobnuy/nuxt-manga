<script lang="ts" setup>
const { mobile } = useViewportLE("tablet");
</script>

<template>
  <div class="layout" :class="{ mobile: mobile }">
    <HeaderPseudo v-if="mobile">
      <slot name="header" />
    </HeaderPseudo>
    <div class="content">
      <slot />
    </div>
  </div>
</template>

<style lang="scss" scoped>
.layout {
  height: 100%;
  display: flex;
  flex-direction: column;

  .content {
    display: flex;
    flex-direction: column;
    max-height: 100%;
  }
}
</style>
