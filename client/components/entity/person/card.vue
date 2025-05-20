<script setup lang="ts">
import { UiButton } from "#components";
import { usePersonStore } from "#imports";
import type { Person } from "~/types/person";

const {
  person,
  mod = false,
  width = 170,
} = defineProps<{
  person: Person;
  mod?: boolean;
  width?: number;
}>();

const { fetchPersonCover, approveMeta, deleteMeta } = usePersonStore();

const url = ref("@/public/pfp.png");
const active = ref(false);

const toggleActive = () => {
  active.value = !active.value;
};

const handleDelete = () => {};
const handleApprove = () => {};
const handleMore = () => {};

onMounted(async () => {
  const new_url = await fetchPersonCover(person.id);
  if (new_url) {
    url.value = new_url;
  }
  console.clear();
  console.log(url.value);
});
</script>

<template>
  <div
    class="person-card-wrapper"
    :style="`--width: ${width}px`"
    @click="toggleActive()"
  >
    <img :src="url" />

    <Transition name="fade" mode="out-in" appear>
      <div v-if="active" class="scroll">
        <div class="caption">
          <span>
            {{ person.name_ru }}
          </span>
          <span>
            {{ person.name_en }}
          </span>
          <span>
            {{ person.name_jp }}
          </span>
          <span>
            {{ person.description }}
          </span>
        </div>
        <div class="actions" v-if="mod">
          <UiButton label="Подробнее" @click.stop="handleMore()" />
          <UiButton label="Одобрить" @click.stop="handleApprove()" />
          <UiButton
            color="error"
            label="Удалить"
            @click.stop="handleDelete()"
          />
        </div>
      </div>
    </Transition>
  </div>
</template>

<style lang="scss" scoped>
.person-card-wrapper {
  position: relative;

  background-color: var(--layer);
  border-radius: var(--br);
  width: var(--width);
  aspect-ratio: 1080 / 1527;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: space-between;

  img {
    z-index: 9;
    position: absolute;
    left: 0;
    top: 0;
    right: 0;
    bottom: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
  }

  .scroll {
    background-color: color-mix(
      in srgb,
      var(--neutral-bg) 100%,
      transparent 25%
    );
    padding: var(--pd);
    z-index: 11;
    width: 100%;
    height: 100%;
    overflow-y: auto;
    gap: calc(var(--gap));
    user-select: none;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  .caption {
    z-index: 11;
    font-size: 0.8em;
    display: flex;
    flex-direction: column;
    gap: calc(var(--gap) / 2);
  }

  .actions {
    z-index: 11;
    display: flex;
    flex-direction: column;
    gap: calc(var(--gap) / 2);
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.22s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
