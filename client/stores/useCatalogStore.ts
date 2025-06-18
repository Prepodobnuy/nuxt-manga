import type { SearchPost, SearchResponse } from "~/types/search";
import type { Tag } from "~/types/tag";
import type { Title } from "~/types/title";

export const useCatalogStore = defineStore("catalog", () => {
  const config = useRuntimeConfig();
  const filters = [
    {
      leading: "heroicons:calendar-date-range-16-solid",
      label: "По дате релиза",
    },
    { leading: "heroicons:star-16-solid", label: "По рейтингу" },
  ];

  const debouce = ref<ReturnType<typeof setTimeout> | null>(null);
  const loading = ref(false);
  const end = ref(false);
  const index = ref(0);
  const titles = ref<Title[]>([]);
  const form = reactive<{
    selected_filter_index: number;
    descending: boolean;
    prompt: string;
    tags: { value: Tag; state: number }[];
    genres: { value: Tag; state: number }[];
    release_year_min: number | undefined;
    release_year_max: number | undefined;
    rate_min: number | undefined;
    rate_max: number | undefined;
  }>({
    selected_filter_index: 1,
    descending: true,
    prompt: "",
    tags: markRaw([]) as { value: Tag; state: number }[],
    genres: markRaw([]) as { value: Tag; state: number }[],
    release_year_min: undefined,
    release_year_max: undefined,
    rate_min: undefined,
    rate_max: undefined,
  });

  const search = (timeout: number = 200, reset: boolean = false) => {
    if (loading.value) return;
    if (debouce.value) clearTimeout(debouce.value);

    if (reset) {
      end.value = false;
      index.value = 0;
      titles.value = [];
    }

    if (end.value && !reset) return;

    setTimeout(async () => {
      loading.value = true;
      try {
        const include_tags = includeTags().map((v) => v.value.id);
        const include_genres = includeGenres().map((v) => v.value.id);
        const exclude_tags = excludeTags().map((v) => v.value.id);
        const exclude_genres = excludeGenres().map((v) => v.value.id);
        const release_year_min: number | null = form.release_year_min || null;
        const release_year_max: number | null = form.release_year_max || null;
        const rate_min: number | null = form.rate_min || null;
        const rate_max: number | null = form.rate_max || null;

        const scheme: SearchPost = {
          prompt: form.prompt,
          include_tags: include_tags,
          exclude_tags: exclude_tags,
          include_genres: include_genres,
          exclude_genres: exclude_genres,
          release_year_min: release_year_min,
          release_year_max: release_year_max,
          rate_min: rate_min,
          rate_max: rate_max,
          descending_order: form.descending,
          sort_by_views: false,
          sort_by_rating: form.selected_filter_index === 1,
          index: index.value,
        };

        const { data, error } = await useFetch<SearchResponse>(
          "/api/search/title",
          {
            method: "POST",
            body: scheme,
            baseURL: config.public.apiBase,
          },
        );

        if (error.value) return;
        if (data.value) {
          end.value = data.value.end;

          titles.value =
            index.value === 0
              ? data.value.titles
              : [...titles.value, ...data.value.titles];

          index.value += 1;
        }
      } finally {
        loading.value = false;
      }
    }, timeout);
  };

  const resetSearch = () => {
    search(200, true);
  };

  watch(
    () => [
      form.selected_filter_index,
      form.descending,
      form.prompt,
      form.tags,
      form.genres,
      form.release_year_min,
      form.release_year_max,
      form.rate_min,
      form.rate_max,
    ],
    () => {
      resetSearch();
    },
    { deep: true },
  );

  const clear = () => {
    form.selected_filter_index = 0;
    form.descending = true;
    form.prompt = "";
    form.tags = markRaw([]) as { value: Tag; state: number }[];
    form.genres = markRaw([]) as { value: Tag; state: number }[];
    form.release_year_min = undefined;
    form.release_year_max = undefined;
    form.rate_min = undefined;
    form.rate_max = undefined;
    updateTags();
    updateGenres();
  };

  const { tagsRef, genresRef } = useTags();

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
    updateTags();
    updateGenres();
    search(0, true);
    await nextTick();
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
    titles,
    includeTags,
    excludeTags,
    includeGenres,
    excludeGenres,
    clear,
  };
});
