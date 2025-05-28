<script setup lang="ts">
const viewStore = useViewStore();
const store = useSearchStore();
const { titles, users, persons } = storeToRefs(useSearchStore());
</script>

<template>
  <SidemenuDefault
    v-if="viewStore.viewSearch && viewStore.mobile"
    @close="viewStore.toggleViewSearch()"
    close-right
  >
    <UiEntryInput
      v-model="store.prompt"
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

    <div class="entries">
      <EntityTitleEntry
        v-if="store.selected === 0"
        v-for="title in titles"
        :title="title"
        @click="navigateTo(`/title/${title.title_id}`)"
      />
      <EntityUserEntry
        v-if="store.selected === 1"
        v-for="user in users"
        :user="user"
        @click="navigateTo(`/user/${user.uuid}`)"
      />
      <EntityPersonEntry
        v-if="store.selected === 2"
        v-for="person in persons"
        :person="person.meta"
        @click="navigateTo(`/peson/${person.id}`)"
      />
    </div>
  </SidemenuDefault>
</template>
