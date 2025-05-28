import type { User } from "~/types/user";

export const useUserStore = (uuid: string) => {
  const config = useRuntimeConfig();

  const store = defineStore(`user_${uuid}`, () => {
    const { data, refresh } = useAsyncData<User>(`user_${uuid}`, async () => {
      return await $fetch<User>(`/api/user/${uuid}`, {
        baseURL: config.public.apiBase,
      });
    });

    return {
      data: data,
      refresh: refresh,
    };
  });

  return store();
};

// uuid: string;
// username: string;
// email: string;
// nickname: string | null;
// status?: string;
// about?: string;
// muted: boolean;
// moder: boolean;
// admin: boolean;
// translator: boolean;
// owns_translate_team: boolean;
// created_at: string;
