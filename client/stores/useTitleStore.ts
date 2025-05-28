import type { Page, PagePost } from "~/types/page";
import type { Person } from "~/types/person";
import type { Title } from "~/types/title";

export const useTitleStore = (id: number) => {
  const store = defineStore(`title_${id}_store`, () => {
    const config = useRuntimeConfig();
    const { token, logged } = useAuth();

    const form = reactive<{
      id: number | null;
      title_id: number;
      title_ru: string | null;
      title_en: string | null;
      title_jp: string | null;
      title_an: string | null;
      release_year: string | null;
      description: string | null;
      author_id: number | null;
      artist_id: number | null;
      publisher_id: number | null;
      tags: number[];
      genres: number[];
      approved: boolean | null;
      approved_at: string | null;
      approved_user_uuid: string | null;
      created_user_uuid: string | null;
      created_at: string | null;
      rates_1: number | null;
      rates_2: number | null;
      rates_3: number | null;
      rates_4: number | null;
      rates_5: number | null;
      user_rate: number | null;
      cover_ids: number[];
      author: Person | null;
      artist: Person | null;
      publisher: Person | null;
      pages: Page[];
    }>({
      id: null,
      title_id: id,
      title_ru: null,
      title_en: null,
      title_jp: null,
      title_an: null,
      release_year: null,
      description: null,
      author_id: null,
      artist_id: null,
      publisher_id: null,
      tags: [],
      genres: [],
      approved: null,
      approved_at: null,
      approved_user_uuid: null,
      created_user_uuid: null,
      created_at: null,
      rates_1: null,
      rates_2: null,
      rates_3: null,
      rates_4: null,
      rates_5: null,
      user_rate: null,
      cover_ids: [],
      author: null,
      artist: null,
      publisher: null,
      pages: [],
    });

    const total_rates = computed((): number => {
      return (
        (form.rates_1 ?? 0) +
        (form.rates_2 ?? 0) +
        (form.rates_3 ?? 0) +
        (form.rates_4 ?? 0) +
        (form.rates_5 ?? 0)
      );
    });

    const rate_percent = computed(() => {
      return {
        rate1: total_rates.value
          ? Math.round(((form.rates_1 ?? 0) / total_rates.value) * 100)
          : 0,
        rate2: total_rates.value
          ? Math.round(((form.rates_2 ?? 0) / total_rates.value) * 100)
          : 0,
        rate3: total_rates.value
          ? Math.round(((form.rates_3 ?? 0) / total_rates.value) * 100)
          : 0,
        rate4: total_rates.value
          ? Math.round(((form.rates_4 ?? 0) / total_rates.value) * 100)
          : 0,
        rate5: total_rates.value
          ? Math.round(((form.rates_5 ?? 0) / total_rates.value) * 100)
          : 0,
      };
    });

    const average_rating = computed(() => {
      if (total_rates.value === 0) return 0;

      const weightedSum =
        (form.rates_5 ?? 0) * 5 +
        (form.rates_4 ?? 0) * 4 +
        (form.rates_3 ?? 0) * 3 +
        (form.rates_2 ?? 0) * 2 +
        (form.rates_1 ?? 0) * 1;

      return parseFloat((weightedSum / total_rates.value).toFixed(2));
    });

    const sorted_pages = computed(() => {
      return [...form.pages].sort((a, b) => {
        if (a.volume !== b.volume) return a.volume - b.volume;
        if (a.chapter !== b.chapter) return a.chapter - b.chapter;
        return a.order - b.order;
      });
    });

    const postRate = async (rate: number) => {
      const { error } = await useFetch(`/api/title/${id}/rate`, {
        method: "POST",
        body: { rate: rate },
        baseURL: config.public.apiBase,
        headers: {
          Authorization: `Bearer ${token.value}`,
        },
      });

      if (!error.value) {
        await fetchRates();
      }
    };

    const fetchMeta = async () => {
      try {
        const data = await $fetch<Title>(`/api/title/${id}/meta`, {
          method: "GET",
          baseURL: config.public.apiBase,
        });

        if (data) {
          const value = data;
          form.id = value.id;
          form.title_id = value.title_id;
          form.title_ru = value.title_ru;
          form.title_en = value.title_en;
          form.title_jp = value.title_jp;
          form.title_an = value.title_an;
          form.release_year = value.release_year;
          form.description = value.description;
          form.author_id = value.author_id;
          form.artist_id = value.artist_id;
          form.publisher_id = value.publisher_id;
          form.tags = value.tags;
          form.genres = value.genres;
          form.approved = value.approved;
          form.approved_at = value.approved_at;
          form.approved_user_uuid = value.approved_user_uuid;
          form.created_user_uuid = value.created_user_uuid;
          form.created_at = value.created_at;
        }
      } catch (err) {}
    };

    const fetchRates = async () => {
      const { data } = await useFetch<{
        rates_5: number;
        rates_4: number;
        rates_3: number;
        rates_2: number;
        rates_1: number;
      }>(`/api/title/${id}/rates`, {
        method: "GET",
        baseURL: config.public.apiBase,
      });

      if (data.value) {
        const value = data.value;
        form.rates_5 = value.rates_5;
        form.rates_4 = value.rates_4;
        form.rates_3 = value.rates_3;
        form.rates_2 = value.rates_2;
        form.rates_1 = value.rates_1;
      }

      if (!logged) return;

      const { data: myRateData } = await useFetch<{ rate: number | null }>(
        `/api/title/${id}/rate`,
        {
          method: "GET",
          baseURL: config.public.apiBase,
          headers: {
            Authorization: `Bearer ${token.value}`,
          },
        },
      );

      if (myRateData.value) {
        form.user_rate = myRateData.value.rate;
      }
    };

    const fetchCovers = async () => {
      const { data } = await useFetch<
        {
          id: number;
          title_id: number;
          order: number;
        }[]
      >(`/api/asset/title/${id}/covers`, {
        method: "GET",
        baseURL: config.public.apiBase,
      });

      if (data.value) {
        form.cover_ids = data.value.map((v) => v.order);
      }
    };

    const putPageAsset = async (i: number, file: File) => {
      const formData = new FormData();
      formData.append("file", file);

      const response = await fetch(
        `${config.public.apiBase}/api/page/${i}/asset`,
        {
          method: "POST",
          body: formData,
          headers: {
            Authorization: `Bearer ${token.value}`,
          },
        },
      );
    };

    const fetchPages = async () => {
      const { data } = await useFetch<Page[]>(`/api/page/title/${id}/pages`, {
        method: "GET",
        baseURL: config.public.apiBase,
      });

      if (data.value) {
        form.pages = data.value;
      }
    };

    const postPage = async (page: PagePost) => {
      const { error } = await useFetch(`/api/page/title/${id}`, {
        method: "POST",
        baseURL: config.public.apiBase,
        body: page,
        headers: {
          Authorization: `Bearer ${token.value}`,
        },
      });

      if (!error.value) {
        await fetchPages();
      }
    };

    const putPage = async (i: number, page: PagePost) => {
      const { error } = await useFetch(`/api/page/${i}`, {
        method: "PUT",
        baseURL: config.public.apiBase,
        body: page,
        headers: {
          Authorization: `Bearer ${token.value}`,
        },
      });

      if (!error.value) {
        await fetchPages();
      }
    };

    const deletePage = async (i: number) => {
      const { error } = await useFetch(`/api/page/${i}`, {
        method: "DELETE",
        baseURL: config.public.apiBase,
        headers: {
          Authorization: `Bearer ${token.value}`,
        },
      });

      if (!error.value) {
        await fetchPages();
      }
    };

    const fetchPersons = async () => {
      async function fetch(id: number): Promise<Person | null> {
        const { data } = await useFetch<Person>(`/api/person/meta/${id}`, {
          method: "GET",
          baseURL: config.public.apiBase,
        });

        return data.value;
      }
      const author = form.author_id ? await fetch(form.author_id) : null;
      const artist = form.artist_id ? await fetch(form.artist_id) : null;
      const publisher = form.publisher_id
        ? await fetch(form.publisher_id)
        : null;

      form.author = author;
      form.artist = artist;
      form.publisher = publisher;
    };

    onMounted(async () => {
      await fetchMeta();
      await fetchPersons();
      await fetchRates();
      await fetchCovers();
      await fetchPages();
    });

    const view = async () => {
      await useFetch(`/api/title/${id}/view`, {
        method: "POST",
        baseURL: config.public.apiBase,
        headers: {
          Authorization: `Bearer ${token.value}`,
        },
      });
    };

    return {
      form,
      total_rates,
      rate_percent,
      average_rating,
      postPage,
      putPage,
      putPageAsset,
      deletePage,
      sorted_pages,
      postRate,
      fetchPages,
      view,
    };
  });

  return store();
};
