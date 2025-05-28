import type { TranslateTeamScheme as TranslateTeam } from "~/types/translate";

export const useModPanelStore = defineStore("modpanel", () => {
  const config = useRuntimeConfig();
  const { token, logged } = useAuth();
  const state = reactive({ loading: false });
  const { data: pending_translate, refresh: pending_refresh } = useFetch<
    TranslateTeam[]
  >("/api/translate/pending", {
    method: "GET",
    baseURL: config.public.apiBase,
    headers: {
      Authorization: `Bearer ${token.value}`,
    },
  });

  const approve = async (id: number) => {
    if (state.loading) return;

    state.loading = true;
    try {
      const response = await fetch(
        `${config.public.apiBase}/api/translate/${id}/approve`,
        {
          method: "POST",
          headers: {
            Authorization: `Bearer ${token.value}`,
          },
        },
      );
      if (response.ok) {
        await pending_refresh();
      }
    } finally {
      state.loading = false;
    }
  };

  const decline = async (id: number) => {
    if (state.loading) return;

    state.loading = true;
    try {
      const response = await fetch(
        `${config.public.apiBase}/api/translate/${id}/disapprove`,
        {
          method: "DELETE",
          headers: {
            Authorization: `Bearer ${token.value}`,
          },
        },
      );
      if (response.ok) {
        await pending_refresh();
      }
    } finally {
      state.loading = false;
    }
  };

  return {
    state,
    pending_translate,
    pending_refresh,
    approve,
    decline,
  };
});
