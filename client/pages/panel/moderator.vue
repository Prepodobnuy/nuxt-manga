<script setup lang="ts">
import { useModPanelStore } from "~/stores/useModPanelStore";

const { approve, decline } = useModPanelStore();
const { pending_translate } = storeToRefs(useModPanelStore());
</script>

<template>
  <LayoutPseudoHeader>
    <template #header>
      <h4>Панель модерации</h4>
    </template>

    <div class="content">
      <h5>Новые команды переводчиков</h5>
      <div class="mod-row" v-for="t in pending_translate" :key="t.id">
        <EntityTranslatorEntry :translate="t" />
        <UiButton
          leading="heroicons:trash-16-solid"
          :fw="false"
          label="Удалить"
          variant="outline"
          color="error"
          @click="decline(t.id)"
        />
        <UiButton
          label="Утвердить"
          variant="outline"
          :fw="false"
          color="success"
          @click="approve(t.id)"
        />
      </div>
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

.mod-row {
  display: inline-flex;
  gap: var(--gap);
  align-items: center;
}
</style>
