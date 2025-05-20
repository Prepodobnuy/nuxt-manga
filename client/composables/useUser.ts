import type { User } from "~/types/user";

const { timeOutMessage } = usePopupStore();

export const useUser = (uuid: string) => {
  const config = useRuntimeConfig();
  const user = useState<User | null>(`user-${uuid}`, () => null);
  const loading = ref(false);
  const error = ref<Error | null>(null);

  const fetchUser = async () => {
    if (loading.value) return;

    loading.value = true;
    error.value = null;

    try {
      const { data, error: fetchError } = await useFetch<User>(
        `/user/${uuid}`,
        {
          baseURL: config.public.apiBase,
          key: `user-${uuid}`,
        },
      );

      if (fetchError.value) {
        throw fetchError.value;
      }

      user.value = data.value;
    } catch (err) {
      error.value = err as Error;
      console.error("Ошибка при получении пользователя:", err);
    } finally {
      loading.value = false;
    }
  };

  return {
    user: readonly(user),
    loading: readonly(loading),
    error: readonly(error),
    fetchUser,
  };
};
