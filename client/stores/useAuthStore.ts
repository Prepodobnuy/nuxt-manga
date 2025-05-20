import { useRoutes, useAuth } from "~/composables/useApi";

interface Validation {
  valid: boolean;
  message?: string;
}

const isPasswordValid = (val: string | undefined): Validation => {
  if (typeof val === "undefined") {
    return { valid: false, message: "Поле пустое" };
  }
  const len = val.length;
  if (len > 30) {
    return { valid: false, message: "Пароль слишком длинный" };
  }
  if (len < 9) {
    return { valid: false, message: "Пароль слишком короткий" };
  }

  return { valid: true };
};

const isUsernameValid = (val: string | undefined): Validation => {
  if (typeof val === "undefined") {
    return { valid: false, message: "Поле пустое" };
  }
  const len = val.length;
  if (len > 21) {
    return { valid: false, message: "Юзернейм слишком длинный" };
  }
  if (len < 5) {
    return { valid: false, message: "Юзернейм слишком короткий" };
  }

  return { valid: true };
};

const isEmailValid = (val: string | undefined): Validation => {
  if (typeof val === "undefined") {
    return { valid: false, message: "Поле пустое" };
  }
  const emailRegex =
    /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;
  const valid = emailRegex.test(val);
  return { valid: valid, message: valid ? undefined : "Неверная почта" };
};

const routes = useRoutes();
const { token, isAuthenticated, setToken } = useAuth();
const router = useRouter();

export const useAuthStore = defineStore("auth", () => {
  const state = ref<{
    password?: string;
    username?: string;
    email?: string;
  }>({
    password: undefined,
    username: undefined,
    email: undefined,
  });

  const valid = {
    password: () => isPasswordValid(state.value.password),
    username: () => isUsernameValid(state.value.username),
    email: () => isEmailValid(state.value.email),
  };

  const isFormValid = computed(() => {
    return Object.values(valid).every((validator) => validator());
  });

  const logIn = async () => {
    const { data, status, error } = await useFetch(
      `${routes.base}/${routes.login}`,
      {
        method: "POST",
        body: {
          username: state.value.username,
          email: state.value.email,
        },
      },
    );
    if (error.value) {
      throw error;
    }
    if (data.value?.access_token) {
      setToken(data.value.access_token);
      await navigateTo("/", { replace: true, redirectCode: 301 });
      window.location.reload();
    }
  };

  const logOut = async () => {
    const { clearToken } = useAuth();
    clearToken();
    await navigateTo("/", { replace: true, redirectCode: 301 });
    window.location.reload();
  };

  const signUp = async () => {
    const { data, status, error } = await useFetch(
      `${routes.base}/${routes.login}`,
      {
        method: "POST",
        body: {
          password: state.value.password,
          username: state.value.username,
          email: state.value.email,
        },
      },
    );
  };
  return {
    state,
    valid,
    logIn,
    logOut,
    signUp,
  };
});
