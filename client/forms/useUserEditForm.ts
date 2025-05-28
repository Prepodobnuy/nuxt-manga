export const useUserEditForm = defineStore("edit-user", () => {
  const { user, token } = useAuth();
  const config = useRuntimeConfig();

  const state = reactive({
    loading: false,
  });
  const form = reactive<{
    nickname: string;
    status: string;
    about: string;
  }>({
    nickname: user.value?.nickname || user.value?.username,
    status: user.value?.status || "",
    about: user.value?.about || "",
  });

  const pfp_url = () => `${config.public.apiBase}/api/user/pfp`;
  const back_url = () => `${config.public.apiBase}/api/user/back`;
  const nickname_url = (v: string) =>
    `${config.public.apiBase}/api/user/nickname?nickname=${v}`;
  const status_url = (v: string) =>
    `${config.public.apiBase}/api/user/status?status=${v}`;
  const about_url = (v: string) =>
    `${config.public.apiBase}/api/user/about?about=${v}`;

  const update = async () => {
    if (form.nickname) {
      await $fetch(nickname_url(form.nickname), {
        method: "PUT",
        headers: {
          Authorization: `Bearer ${token.value}`,
        },
      });
    }

    if (form.status) {
      await $fetch(status_url(form.status), {
        method: "PUT",
        headers: {
          Authorization: `Bearer ${token.value}`,
        },
      });
    }

    if (form.about) {
      await $fetch(about_url(form.about), {
        method: "PUT",
        headers: {
          Authorization: `Bearer ${token.value}`,
        },
      });
    }
  };

  return { form, update };
});
