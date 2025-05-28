import type { TranslateTeamPostScheme } from "~/types/translate";

export const useTranslateTeamForm = defineStore("translateForm", () => {
  const config = useRuntimeConfig();
  const { token, logged } = useAuth();

  const form = reactive<{
    title?: string;
    description?: string;
    cover?: File;
  }>({
    title: undefined,
    description: undefined,
    cover: undefined,
  });

  const valid = ref({
    title: true,
    description: true,
    cover: true,
  });

  const clear = () => {
    form.title = undefined;
    form.description = undefined;
    form.cover = undefined;

    valid.value = {
      title: true,
      description: true,
      cover: true,
    };
  };

  const loading = ref(false);

  const validate = () => {
    valid.value.title =
      typeof form.title !== "undefined" &&
      form.title.length > 1 &&
      form.title.length < 100;
    valid.value.cover = typeof form.cover !== "undefined";
  };

  const post = async () => {
    console.log(2);
    if (!logged.value) return;
    if (loading.value) return;

    validate();
    if (typeof form.title === "undefined" || typeof form.cover === "undefined")
      return;

    loading.value = true;
    try {
      const formData = new FormData();

      const data: TranslateTeamPostScheme = {
        title: form.title,
        description: form.description || null,
      };

      formData.append("file", form.cover);
      formData.append("scheme", JSON.stringify(data));

      const response = await fetch(`${config.public.apiBase}/api/translate`, {
        method: "POST",
        body: formData,
        headers: {
          Authorization: `Bearer ${token.value}`,
        },
      });
      if (!response.ok) {
        throw new Error(await response.text());
      }
      clear();
    } catch (err) {
    } finally {
      loading.value = false;
    }
  };

  return {
    form,
    valid,
    clear,
    post,
  };
});
