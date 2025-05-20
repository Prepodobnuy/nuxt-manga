import type { User } from "~/types/user";

export const useUserStore = defineStore("user", () => {
  const config = useRuntimeConfig();

  const state = reactive({
    users: {} as Record<string, User>,
    loading: false,
  });

  const fetchUser = async (uuid: string) => {
    state.loading = true;
    try {
      const responce = await $fetch<User>(`/api/user/${uuid}`, {
        baseURL: config.public.apiBase,
      });
      state.users[uuid] = responce;
    } catch (err) {
    } finally {
      state.loading = false;
    }
  };

  return {
    state,
    fetchUser,
  };
});
