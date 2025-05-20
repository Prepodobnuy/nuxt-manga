import type { PersonPost } from "~/types/person";

export const usePersonForm = defineStore("personForm", () => {
  const config = useRuntimeConfig();

  const loading = ref(false);

  const form = reactive<{
    nameRu?: string;
    nameEn?: string;
    nameJp?: string;
    nameAn?: string;
    description?: string;
    cover?: File;
  }>({
    nameRu: undefined,
    nameEn: undefined,
    nameJp: undefined,
    nameAn: undefined,
    description: undefined,
    cover: undefined,
  });

  const valid = ref({
    nameRu: true,
    nameEn: true,
    nameJp: true,
    nameAn: true,
    description: true,
    cover: true,
  });

  const clear = () => {
    form.nameRu = undefined;
    form.nameEn = undefined;
    form.nameJp = undefined;
    form.nameAn = undefined;
    form.description = undefined;
    form.cover = undefined;

    valid.value = {
      nameRu: true,
      nameEn: true,
      nameJp: true,
      nameAn: true,
      description: true,
      cover: true,
    };
  };

  const validate = () => {
    valid.value.nameRu =
      typeof form.nameRu !== "undefined" &&
      form.nameRu.length > 1 &&
      form.nameRu.length < 100;
    valid.value.nameEn =
      typeof form.nameEn !== "undefined" &&
      form.nameEn.length > 1 &&
      form.nameEn.length < 100;
    valid.value.nameJp =
      typeof form.nameJp !== "undefined" &&
      form.nameJp.length > 1 &&
      form.nameJp.length < 100;
    valid.value.cover = typeof form.cover !== "undefined";
  };

  const post = async () => {
    const { token, logged } = useAuth();

    if (!logged) return;

    validate();
    if (
      form.nameRu === undefined ||
      form.nameEn === undefined ||
      form.nameJp === undefined ||
      form.cover === undefined
    )
      return;

    loading.value = true;
    try {
      const formData = new FormData();

      const data: PersonPost = {
        name_ru: form.nameRu,
        name_en: form.nameEn,
        name_jp: form.nameJp,
        name_an: form.nameAn || null,
        description: form.description || null,
      };

      formData.append("file", form.cover);
      formData.append("scheme", JSON.stringify(data));

      const response = await fetch(`${config.public.apiBase}/api/person`, {
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
    loading,
  };
});
