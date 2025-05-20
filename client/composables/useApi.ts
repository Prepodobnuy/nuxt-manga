interface Route {
  path: string;
  auth?: boolean;
}

const base = "127.0.0.1:8000";

const route = (path: string, auth: boolean): Route => {
  return {
    path: `${base}${path}`,
    auth: auth,
  };
};

interface Tag {
  id: number;
  ru: string;
  en: string;
}

const routes = {
  login: route("/auth/login", false),
  signup: route("/auth/signup", false),
  getTags: async (): Promise<Tag[] | null> => {
    const { data } = await useFetch<Tag[]>(`${base}/tags`);
    return data.value;
  },
  getGenres: async (): Promise<Tag[] | null> => {
    const { data } = await useFetch<Tag[]>(`${base}/genres`);
    return data.value;
  },
};

export const useAuth = () => {
  const token = useCookie("auth_token");

  const isAuthenticated = computed(() => !!token.value);

  const setToken = (newToken: string) => {
    const authToken = useCookie("auth_token", {
      maxAge: 60 * 60 * 24 * 7,
      secure: true,
    });
    authToken.value = newToken;
  };

  const clearToken = () => {
    token.value = null;
  };

  return {
    token,
    isAuthenticated,
    setToken,
    clearToken,
  };
};

export const useRoutes = () => {
  return routes;
};
