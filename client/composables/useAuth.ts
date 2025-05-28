import type { User } from "~/types/user";

export const useAuth = () => {
  const { timeOutMessage } = usePopupStore();
  const config = useRuntimeConfig();
  const user = useState<User | null>("user", () => null);
  const isFetching = ref(false);

  const token = useCookie<string | null>("token", {
    default: () => null,
    maxAge: 60 * 60 * 24 * 7,
    watch: true,
    sameSite: "strict",
  });

  const login = async (credentials: { username: string; password: string }) => {
    try {
      const formData = new URLSearchParams();
      formData.append("username", credentials.username);
      formData.append("password", credentials.password);

      const { access_token } = await $fetch<{ access_token: string }>(
        "/api/auth/login",
        {
          baseURL: config.public.apiBase,
          method: "POST",
          body: formData,
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
        },
      );

      token.value = access_token;
      await fetchUser();
      return navigateTo("/");
    } catch (err) {
      timeOutMessage("Ошибка при входе", 1000);
      throw err;
    }
  };

  const signup = async (credentials: {
    username: string;
    email: string;
    password: string;
  }) => {
    try {
      await $fetch("/api/auth/signup", {
        baseURL: config.public.apiBase,
        method: "POST",
        body: credentials,
        headers: {
          "Content-Type": "application/json",
        },
      });

      return await login({
        username: credentials.username,
        password: credentials.password,
      });
    } catch (err) {
      timeOutMessage("Ошибка при создании аккаунта", 1000);
      console.error("Signup error:", err);
      throw err;
    }
  };

  const fetchUser = async () => {
    if (!token.value) return;
    if (isFetching.value) return;

    isFetching.value = true;
    try {
      user.value = await $fetch<User>("/api/user/self", {
        baseURL: config.public.apiBase,
        headers: {
          Authorization: `Bearer ${token.value}`,
        },
      });
    } catch (err) {
      console.error("Failed to fetch user:", err);
      token.value = null;
      user.value = null;
      timeOutMessage("Сессия истекла", 1000);
      navigateTo("/auth/login");
    } finally {
      isFetching.value = false;
    }
  };

  const logout = () => {
    token.value = null;
    user.value = null;
    navigateTo("/auth/login");
  };

  const logged = computed(() => !!token.value && !!user.value);

  onMounted(async () => {
    if (process.client && token.value && !user.value) {
      await fetchUser();
    }
  });

  watch(token, async (newToken) => {
    if (newToken && !user.value) {
      await fetchUser();
    }
  });

  return {
    user: readonly(user),
    token: readonly(token),
    login,
    signup,
    logout,
    fetchUser,
    logged,
  };
};
