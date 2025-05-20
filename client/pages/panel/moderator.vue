<script setup lang="ts">
import {
  LazyPersonCard,
  PersonCard,
  UiButton,
  UiHBox,
  UiLink,
  UiTabs,
} from "#components";
import { usePersonStore } from "#imports";

const route = useRoute();
const router = useRouter();
const personStore = usePersonStore();

interface Tab {
  leading?: string;
  trailing?: string;
  label?: string;
  icon?: boolean;
}

const tabs = [{ label: "Тайтлы" }, { label: "Персоны" }, { label: "Жалобы" }];
const tab = defineModel<number>({ default: 0 });

watch(tab, (newTab) => {
  router.push({
    query: {
      ...route.query,
      tab: newTab,
    },
  });
});

onMounted(async () => {
  if (route.query.tab) {
    tab.value = Number(route.query.tab);
  }
  personStore.fetchPendingPersons();
});
</script>

<template>
  <LayoutPseudoHeader>
    <template #header>
      <h4>Панель модерации</h4>
    </template>

    <div class="content">
      <div style="border-radius: var(--br); overflow: hidden">
        <UiTabs v-model="tab" :tabs="tabs" full-width />
      </div>

      <section v-if="tab === 0" class="section">
        <h4>asdfasd</h4>
      </section>

      <section v-if="tab === 1" class="section">
        <UiHBox label="Обновления метаданных">
          <PersonCard
            :key="person.id"
            :person="person"
            mod
            v-for="person in personStore.state.pendingPersons"
          />
        </UiHBox>
      </section>

      <section v-if="tab === 2" class="section"></section>
    </div>
  </LayoutPseudoHeader>
</template>

<style lang="scss" scoped>
@use "@/assets/mixins";
@use "@/assets/variables";
@use "@/assets/functions";

.content {
  @include mixins.page-content;
  padding: 20px;
  gap: var(--gap);

  .section {
    display: flex;
    flex-direction: column;
    width: 100%;

    gap: var(--gap);
  }
}

.testbox {
  height: 300px;
  width: 200px;
  background-color: red;
}
</style>
