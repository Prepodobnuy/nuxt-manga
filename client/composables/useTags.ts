import type { Tag } from "~/types/tag";

export const useTags = () => {
  const config = useRuntimeConfig();

  const {
    data: tags,
    pending: tpending,
    error: terror,
  } = useAsyncData<Tag[]>("tags", async () => {
    return await $fetch("/api/tags", { baseURL: config.public.apiBase });
  });

  const {
    data: genres,
    pending: gpending,
    error: gerror,
  } = useAsyncData<Tag[]>("genres", async () => {
    return await $fetch("/api/genres", { baseURL: config.public.apiBase });
  });

  return {
    tags: tags.value || [],
    genres: genres.value || [],
    tagsRef: tags,
    genresRef: genres,
    loading: tpending.value || gpending.value,
    error: terror.value || gerror.value,
  };
};
