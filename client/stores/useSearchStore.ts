interface Entity {
  label: string;
  leading: string;
}

const entities = [
  { label: "Тайтл", leading: "heroicons:book-open-16-solid" },
  { label: "Пользователя", leading: "heroicons:user-16-solid" },
  { label: "Персону", leading: "heroicons:face-smile-solid" },
  { label: "Переводчика", leading: "heroicons:language-16-solid" },
];

export const useSearchStore = defineStore("searchStore", () => {
  const selecting = ref(false);
  const selected = ref(0);
  const label = computed<string>(() => {
    if (selecting.value) {
      return "Искать";
    }
    return `Искать ${entities[selected.value].label.toLowerCase()}`;
  });

  const toggleSelecting = () => (selecting.value = !selecting.value);
  const select = (index: number) => (selected.value = index);
  const getEntities = (): Entity[] => entities;

  return {
    selecting,
    selected,
    label,
    toggleSelecting,
    select,
    getEntities,
  };
});
