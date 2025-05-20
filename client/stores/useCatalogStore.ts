import type { Tag } from "~/types/tag";

export const useCatalogStore = defineStore("catalog", () => {
  const filters = [
    { leading: "heroicons:trophy-16-solid", label: "По популярности" },
    { leading: "heroicons:star-16-solid", label: "По рейтингу" },
    { leading: "heroicons:eye-16-solid", label: "По просмотрам" },
    {
      leading: "heroicons:calendar-date-range-16-solid",
      label: "По дате добавления",
    },
  ];
  const { tagsRef, genresRef } = useTags();

  const form = reactive<{
    filter: number;
    increasing: boolean;
    prompt: string;
    tags: { value: Tag; state: number }[];
    genres: { value: Tag; state: number }[];
    releaseYearFrom: number | undefined;
    releaseYearTo: number | undefined;
    minRate: number | undefined;
    maxRate: number | undefined;
  }>({
    filter: 0,
    increasing: true,
    prompt: "",
    tags: [],
    genres: [],
    releaseYearFrom: undefined,
    releaseYearTo: undefined,
    minRate: undefined,
    maxRate: undefined,
  });

  const includeTags = () => form.tags.filter((v) => v.state === 1);
  const excludeTags = () => form.tags.filter((v) => v.state === 2);
  const includeGenres = () => form.genres.filter((v) => v.state === 1);
  const excludeGenres = () => form.genres.filter((v) => v.state === 2);

  const updateTags = () => {
    if (!tagsRef.value?.length) return;
    form.tags = [...tagsRef.value.map((v) => ({ state: 0, value: v }))];
  };

  const updateGenres = () => {
    if (!genresRef.value?.length) return;
    form.genres = genresRef.value.map((v) => ({ state: 0, value: v }));
  };

  onMounted(async () => {
    await nextTick();
    updateTags();
    updateGenres();
  });

  watch(
    [tagsRef, genresRef],
    () => {
      updateTags();
      updateGenres();
    },
    { deep: true },
  );

  return {
    filters,
    form,
    includeTags,
    excludeTags,
    includeGenres,
    excludeGenres,
  };
});
