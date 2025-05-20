import type { TitlePost } from "~/types/title";

export const useTitleForm = defineStore("titleForm", () => {
  const config = useRuntimeConfig();

  const loading = ref(false);

  const form = reactive<{
    titleRu?: string;
    titleEn?: string;
    titleJp?: string;
    titleAn?: string;
    description?: string;
    releaseYear?: string;
    authorId?: number;
    artistId?: number;
    publisherId?: number;
    tags: number[];
    genres: number[];
    covers: File[];
  }>({
    titleRu: undefined,
    titleEn: undefined,
    titleJp: undefined,
    titleAn: undefined,
    description: undefined,
    authorId: undefined,
    artistId: undefined,
    publisherId: undefined,
    tags: [],
    genres: [],
    covers: [],
  });

  const valid = ref({
    titleRu: true,
    titleEn: true,
    titleJp: true,
    releaseYear: true,
    authorId: true,
    artistId: true,
    publisherId: true,
    covers: true,
  });

  const clear = () => {
    form.titleRu = undefined;
    form.titleEn = undefined;
    form.titleJp = undefined;
    form.titleAn = undefined;
    form.description = undefined;
    form.releaseYear = undefined;
    form.authorId = undefined;
    form.artistId = undefined;
    form.publisherId = undefined;
    form.tags = [];
    form.genres = [];
    form.covers = [];

    valid.value = {
      titleRu: true,
      titleEn: true,
      titleJp: true,
      releaseYear: true,
      authorId: true,
      artistId: true,
      publisherId: true,
      covers: true,
    };
  };

  const releaseYearValid = (): boolean => {
    const val = Number(form.releaseYear);
    if (isNaN(val)) {
      return false;
    }

    return val > 1900 && val < 2027;
  };

  const validate = () => {
    valid.value.titleRu =
      typeof form.titleRu !== "undefined" &&
      form.titleRu.length > 1 &&
      form.titleRu.length < 100;
    valid.value.titleEn =
      typeof form.titleEn !== "undefined" &&
      form.titleEn.length > 1 &&
      form.titleEn.length < 100;
    valid.value.titleJp =
      typeof form.titleJp !== "undefined" &&
      form.titleJp.length > 1 &&
      form.titleJp.length < 100;
    valid.value.authorId = typeof form.authorId !== "undefined";
    valid.value.artistId = typeof form.artistId !== "undefined";
    valid.value.publisherId = typeof form.publisherId !== "undefined";
    valid.value.releaseYear = releaseYearValid();
    valid.value.covers = form.covers.length > 0 && form.covers.length <= 10;
  };

  const post = async () => {
    const { token, logged } = useAuth();

    if (!logged) return;

    validate();
    if (
      form.titleRu === undefined ||
      form.titleEn === undefined ||
      form.titleJp === undefined ||
      form.releaseYear === undefined ||
      form.authorId === undefined ||
      form.artistId === undefined ||
      form.publisherId === undefined
    )
      return;

    loading.value = true;
    try {
      const formData = new FormData();

      const data: TitlePost = {
        title_ru: form.titleRu,
        title_en: form.titleEn,
        title_jp: form.titleJp,
        title_an: form.titleAn || null,
        release_year: form.releaseYear,
        description: form.description || null,
        author_id: form.authorId,
        artist_id: form.artistId,
        publisher_id: form.publisherId,
        tags: form.tags,
        genres: form.genres,
      };

      form.covers.forEach((c, i) => {
        formData.append(`file_${i}`, c);
      });
      formData.append("scheme", JSON.stringify(data));

      const response = await fetch(`${config.public.apiBase}/api/title`, {
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
