<script setup lang="ts">
import { EntityPersonEntry, EntityTitleEntry, UiButton } from "#components";

const viewStore = useViewStore();
const store = useSearchStore();
const selected = store.getEntities()[store.selected];
const { titles, users, persons } = storeToRefs(useSearchStore());
</script>

<template>
  <Transition name="fade">
    <div
      v-if="!viewStore.mobile && viewStore.viewSearch"
      class="search-wrapper"
    >
      <div class="blank" @click.self="viewStore.toggleViewSearch()" />
      <div class="body" @click.self="viewStore.toggleViewSearch()">
        <div class="inputs">
          <div class="row">
            <UiInput
              v-model="store.prompt"
              style="width: 100%; flex-shrink: 1"
              variant="solid"
              placeholder="Поиск"
              size="lg"
            />
            <UiButton
              style="flex-shrink: 0"
              size="lg"
              :toggle="store.selecting"
              :label="store.label"
              :leading="
                store.selecting
                  ? ''
                  : store.getEntities()[store.selected].leading
              "
              :fw="false"
              @click="store.selecting = !store.selecting"
            />
            <UiButton
              style="flex-shrink: 0"
              size="lg"
              leading="heroicons:x-mark-16-solid"
              icon
              @click="viewStore.toggleViewSearch()"
            />
          </div>
          <div v-if="store.selecting" class="row">
            <UiButton
              v-for="(en, index) in store.getEntities()"
              :toggle="index === store.selected"
              :key="en.label"
              :label="en.label"
              :leading="en.leading"
              @click="store.select(index)"
            />
          </div>
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
      </div>
    </div>
  </Transition>
</template>

<style lang="scss" scoped>
.search-wrapper {
  position: fixed;
  width: 100vw;
  height: 100vh;
  z-index: 3000;

  display: flex;
  flex-direction: column;
  gap: var(--gap);
  align-items: center;

  .body {
    z-index: 100;
    padding: calc(var(--pd) * var(--xl));
    width: 100%;
    max-width: 1100px;
    height: 100%;
    display: flex;
    flex-direction: column;
    gap: var(--gap);

    .inputs {
      display: flex;
      flex-direction: column;
      gap: var(--gap);

      .row {
        width: 100%;
        display: inline-flex;
        gap: var(--gap);
      }
    }

    .entries {
      width: 100%;
      height: max-content;
      max-height: 100%;
      border-radius: var(--br);
      display: flex;
      flex-direction: column;
      overflow-y: auto;
      background-color: var(--window-bg);

      & > * {
        flex-shrink: 0;
      }
    }
  }
}

.blank {
  z-index: 99;
  position: absolute;
  width: 100vw;
  height: 100vh;
  background-color: #000000bb;
}

.fade-enter-from,
.fade.leave-to {
  opacity: 0;
}

.fade-enter-to,
.fade.leave-from {
  transition: opacity 320ms;
}
</style>
