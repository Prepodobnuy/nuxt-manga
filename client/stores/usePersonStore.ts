import type { Person, PersonMeta, PersonPost } from "~/types/person";

export const usePersonStore = defineStore("person", () => {
  const config = useRuntimeConfig();
  const { token } = useAuth();

  const state = reactive({
    loading: false,
    persons: {} as Record<number, Person>,
    metas: {} as Record<number, PersonMeta>,
    pendingMetas: {} as Record<number, PersonMeta>,
  });

  const fetch = async (id: number): Promise<Person | null> => {
    state.loading = true;
    try {
      const { data } = await useFetch<Person>(`/api/person/${id}`, {
        baseURL: config.public.apiBase,
        headers: {
          Authorization: `Bearer ${token.value}`,
        },
      });

      if (data.value) {
        state.persons[id] = data.value;
        if (data.value.meta) {
          state.metas[id] = data.value.meta;
        }
        if (data.value.unapproved_metas?.length) {
          state.pendingMetas[id] = data.value.unapproved_metas[0];
        }
      }
      return data.value;
    } finally {
      state.loading = false;
    }
  };

  const fetchMeta = async (id: number) => {
    state.loading = true;
    try {
      const { data } = await useFetch<PersonMeta>(`/api/person/meta/${id}`, {
        baseURL: config.public.apiBase,
        headers: {
          Authorization: `Bearer ${token.value}`,
        },
      });

      if (data.value) {
        state.metas[id] = data.value;
      }
      return data.value;
    } finally {
      state.loading = false;
    }
  };

  const quickSearch = async (prompt: string) => {
    state.loading = true;
    try {
      const { data } = await useFetch<Person[]>(
        `/api/person/search/${prompt}`,
        {
          baseURL: config.public.apiBase,
          headers: {
            Authorization: `Bearer ${token.value}`,
          },
        },
      );

      if (data.value) {
        data.value.forEach((person) => {
          state.persons[person.id] = person;
          if (person.meta) {
            state.metas[person.id] = person.meta;
          }
        });
      }
      return data.value || [];
    } finally {
      state.loading = false;
    }
  };

  const approveMeta = async (id: number) => {
    state.loading = true;
    try {
      await useFetch(`/api/person/meta/${id}/approve`, {
        baseURL: config.public.apiBase,
        method: "POST",
        headers: {
          Authorization: `Bearer ${token.value}`,
        },
      });

      await fetch(id);
    } finally {
      state.loading = false;
    }
  };

  const deletePerson = async (id: number) => {
    state.loading = true;
    try {
      await useFetch(`/api/person/${id}`, {
        baseURL: config.public.apiBase,
        method: "DELETE",
        headers: {
          Authorization: `Bearer ${token.value}`,
        },
      });

      delete state.persons[id];
      delete state.metas[id];
      delete state.pendingMetas[id];
    } finally {
      state.loading = false;
    }
  };

  const deleteMeta = async (id: number) => {
    state.loading = true;
    try {
      await useFetch(`/api/person/meta/${id}`, {
        baseURL: config.public.apiBase,
        method: "DELETE",
        headers: {
          Authorization: `Bearer ${token.value}`,
        },
      });

      await fetch(id);
    } finally {
      state.loading = false;
    }
  };

  const getPersonCoverUrl = (id: number) => {
    return `${config.public.apiBase}/api/person/asset/${id}/cover`;
  };

  return {
    state,
    fetch,
    fetchMeta,
    quickSearch,
    approveMeta,
    deletePerson,
    deleteMeta,
    getPersonCoverUrl,
  };
});
