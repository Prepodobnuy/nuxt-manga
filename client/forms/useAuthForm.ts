const { login, signup, fetchUser } = useAuth();

const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const MAX_EMAIL_LENGTH = 100;

const validateEmail = (email: string | undefined): boolean => {
  if (typeof email === "undefined") return false;
  const trimmedEmail = email.trim();
  return (
    trimmedEmail.length <= MAX_EMAIL_LENGTH && EMAIL_REGEX.test(trimmedEmail)
  );
};

export const useAuthForm = defineStore("authForm", () => {
  const form = reactive<{
    username?: string;
    email?: string;
    password?: string;
  }>({
    username: undefined,
    email: undefined,
    password: undefined,
  });

  const valid = ref({
    username: true,
    email: true,
    password: true,
  });

  const clear = () => {
    form.username = undefined;
    form.email = undefined;
    form.password = undefined;

    valid.value = {
      username: true,
      email: true,
      password: true,
    };
  };

  const validate = () => {
    valid.value.username =
      typeof form.username !== "undefined" &&
      form.username.length > 1 &&
      form.username.length < 100;
    valid.value.email = validateEmail(form.email);
    valid.value.password =
      typeof form.password !== "undefined" &&
      form.password.length > 1 &&
      form.password.length < 100;
  };

  const postLogin = async () => {
    validate();
    if (!valid.value.username || !valid.value.password) {
      return;
    }

    if (form.username === undefined) return;
    if (form.password === undefined) return;

    await login({ username: form.username, password: form.password });
  };

  const postSignup = async () => {
    validate();
    if (!valid.value.username || !valid.value.email || !valid.value.password) {
      return;
    }

    if (form.username === undefined) return;
    if (form.password === undefined) return;
    if (form.email === undefined) return;

    await signup({
      username: form.username,
      email: form.email,
      password: form.password,
    });
  };

  return {
    form,
    valid,
    clear,
    postLogin,
    postSignup,
  };
});
