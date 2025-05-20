<script setup lang="ts">
const viewStore = useViewStore();
const store = useSearchStore();
</script>

<template>
  <SidemenuDefault
    v-if="viewStore.viewSearch && viewStore.mobile"
    @close="viewStore.toggleViewSearch()"
    close-right
  >
    <UiEntryInput
      placeholder="Поиск"
      leading="heroicons:magnifying-glass-16-solid"
    />
    <UiEntryButton
      :toggle="store.selecting"
      :label="store.label"
      :leading="
        store.selecting ? '' : store.getEntities()[store.selected].leading
      "
      @click="store.toggleSelecting()"
    />
    <div v-if="store.selecting">
      <UiEntryButton
        v-for="(entity, index) in store.getEntities()"
        :key="`entity.label${index}`"
        :label="entity.label"
        :leading="entity.leading"
        :toggle="index === store.selected"
        @click="store.select(index)"
      />
    </div>
  </SidemenuDefault>
</template>
