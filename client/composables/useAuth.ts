import type { User } from "~/types/user";

export const useAuth = () => {
  const { timeOutMessage } = usePopupStore();
  const config = useRuntimeConfig();
  const user = useState<User | null>("user", () => null);

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

      const { data, error } = await useFetch<{
        access_token: string;
        token_type: string;
      }>("/api/auth/login", {
        baseURL: config.public.apiBase,
        method: "POST",
        body: formData,
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      });

      if (error.value) throw error.value;

      if (data.value) {
        token.value = data.value.access_token;
      }
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
      const { error } = await useFetch("/api/auth/signup", {
        baseURL: config.public.apiBase,
        method: "POST",
        body: credentials,
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (error.value) throw error.value;

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

    try {
      const { data } = await useFetch<User>("/api/user/self", {
        baseURL: config.public.apiBase,
        headers: {
          Authorization: `Bearer ${token.value}`,
        },
      });

      user.value = data.value;
    } catch (err) {
      timeOutMessage("Ошибка при получении информации о пользователе", 1000);
      logout();
    }
  };

  const logout = () => {
    token.value = null;
    user.value = null;
    return navigateTo("/auth/login");
  };

  const logged = computed(() => token.value !== null);

  if (process.client && token.value && !user.value) {
    fetchUser().catch(console.error); // или useAsyncData
  }

  return {
    user,
    token,
    login,
    signup,
    logout,
    fetchUser,
    logged,
  };
};
