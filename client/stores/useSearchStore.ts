import { useQuickSearch } from "#imports";
import type { Person, PersonFull } from "~/types/person";
import type { Title } from "~/types/title";
import type { User } from "~/types/user";

interface Entity {
  label: string;
  leading: string;
}

const entities = [
  { label: "Тайтл", leading: "heroicons:book-open-16-solid" },
  { label: "Пользователя", leading: "heroicons:user-16-solid" },
  { label: "Персону", leading: "heroicons:face-smile-solid" },
  // { label: "Переводчика", leading: "heroicons:language-16-solid" },
];

export const useSearchStore = defineStore("searchStore", () => {
  const config = useRuntimeConfig();
  const selecting = ref(false);
  const selected = ref(0);
  const label = computed<string>(() => {
    if (selecting.value) {
      return "Искать";
    }
    return `Искать ${entities[selected.value].label.toLowerCase()}`;
  });

  const debouce = ref<ReturnType<typeof setTimeout> | null>(null);
  const prompt = ref("");

  const titles = ref<Title[]>([]);
  const persons = ref<PersonFull[]>([]);
  const users = ref<User[]>([]);

  const { fetchTitles, fetchUsers, fetchPersons } = useQuickSearch();

  watch(prompt, () => {
    if (debouce.value) clearTimeout(debouce.value);
    debouce.value = setTimeout(async () => {
      switch (selected.value) {
        case 0:
          titles.value = (await fetchTitles(prompt.value)) || [];
          break;
        case 1:
          users.value = (await fetchUsers(prompt.value)) || [];
          break;
        case 2:
          persons.value = (await fetchPersons(prompt.value)) || [];
          break;
      }
    }, 400);
  });

  const toggleSelecting = () => (selecting.value = !selecting.value);
  const select = (index: number) => (selected.value = index);
  const getEntities = (): Entity[] => entities;

  return {
    prompt,
    titles,
    persons,
    users,
    selecting,
    selected,
    label,
    toggleSelecting,
    select,
    getEntities,
  };
});
