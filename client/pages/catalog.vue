<script lang="ts" setup>
import { UiResponsiveGrid } from "#components";

const { mobile } = useViewportLE();
const { filters, form } = useCatalogStore();
const { toggleCatalogMenu } = useViewStore();
const cols = ref(4);
const { breakpoint, isLessThan } = useViewport();

watch(breakpoint, () => {
  cols.value = isLessThan("mobile")
    ? 1
    : isLessThan("tabletxs")
      ? 2
      : isLessThan("tablet")
        ? 3
        : 4;
});
</script>

<template>
  <LayoutPseudoHeader>
    <template #header>
      <h4>Каталог</h4>
    </template>

    <div class="content">
      <main>
        <div class="search">
          <UiInput class="fw" variant="outline" placeholder="поиск" />
          <UiDropdown align="right">
            <template #head>
              <UiButton
                class="noshrink"
                variant="outline"
                leading="heroicons:funnel-solid"
                icon
                :fw="false"
              />
            </template>
            <UiButton
              v-for="(f, i) in filters"
              class="noshrink"
              variant="ghost"
              roundness="none"
              start
              :leading="f.leading"
              :label="f.label"
              :toggle="i == form.filter"
              @click="form.filter = i"
            />

            <div style="height: 4px" />

            <UiButton
              :toggle="form.increasing"
              class="noshrink"
              variant="ghost"
              leading="heroicons:bars-arrow-up-16-solid"
              label="По возрастанию"
              roundness="none"
              start
              @click="form.increasing = true"
            />
            <UiButton
              :toggle="!form.increasing"
              class="noshrink"
              variant="ghost"
              leading="heroicons:bars-arrow-down-16-solid"
              label="По убыванию"
              roundness="none"
              start
              @click="form.increasing = false"
            />
          </UiDropdown>
          <UiButton
            v-if="mobile"
            class="noshrink"
            variant="outline"
            leading="heroicons:tag-16-solid"
            icon
            :fw="false"
            @click="toggleCatalogMenu()"
          />
        </div>

        <UiResponsiveGrid :cols="cols" :gap="6">
          <EntityTitleCard :title="{ title_ru: 'asfdas', title_en: 'asfas' }" />
          <EntityTitleCard :title="{}" />
          <EntityTitleCard :title="{}" />
          <EntityTitleCard :title="{}" />
          <EntityTitleCard :title="{}" />
          <EntityTitleCard :title="{}" />
          <EntityTitleCard :title="{}" />
          <EntityTitleCard :title="{}" />
          <EntityTitleCard :title="{}" />
          <EntityTitleCard :title="{}" />
          <EntityTitleCard :title="{}" />
          <EntityTitleCard :title="{}" />
          <EntityTitleCard :title="{}" />
          <EntityTitleCard :title="{}" />
          <EntityTitleCard :title="{}" />
        </UiResponsiveGrid>
      </main>

      <aside>
        <PageCatalogParamsAside v-if="!mobile" />
      </aside>
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
  gap: calc(var(--gap) * 2);
  flex-direction: row;
  overflow-y: visible;

  main {
    position: relative;
    display: flex;
    flex-direction: column;
    gap: var(--gap);

    width: 100%;
    flex-shrink: 1;

    .search {
      width: 100%;
      gap: var(--gap);
      display: inline-flex;

      .fw {
        flex-shrink: 1;
        width: 100%;
      }

      .noshrink {
        flex-shrink: 0;
      }
    }
  }

  aside {
    position: sticky;
    top: 20px;
  }
}
</style>
