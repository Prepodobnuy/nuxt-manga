<script setup lang="ts">
const { view = false } = defineProps<{
  view?: boolean;
}>();
const isSelecting = ref(false);

const searchEntities = [
  { label: "Тайтл" },
  { label: "Пользователя" },
  { label: "Персону" },
  { label: "Переводчика" },
];
const selectedEntity = ref(0);

const getLabel = (): string => {
  const entry = searchEntities[selectedEntity.value].label;
  if (isSelecting.value) {
    return "Искать";
  }
  return `Искать ${entry.toLowerCase()}`;
};
const selectToggle = () => {
  isSelecting.value = !isSelecting.value;
};
const select = (index: number) => {
  selectedEntity.value = index;
};
const selectClose = () => {
  isSelecting.value = false;
};
</script>

<template>
  <div class="blank">
    <div class="col">
      <div class="row">
        <UiInput />
        <UiButton />
        <UiButton />
      </div>
    </div>
  </div>
</template>
