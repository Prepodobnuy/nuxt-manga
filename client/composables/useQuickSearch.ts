import type { Person, PersonFull } from "~/types/person";
import type { Title } from "~/types/title";
import type { User } from "~/types/user";

export const useQuickSearch = () => {
  const config = useRuntimeConfig();

  const fetchTitles = async (prompt: string): Promise<Title[] | null> => {
    const { data } = await useFetch<Title[]>(`/api/title/search/${prompt}`, {
      baseURL: config.public.apiBase,
    });
    return data.value;
  };

  const fetchUsers = async (prompt: string): Promise<User[] | null> => {
    const { data } = await useFetch<User[]>(`/api/user/search/${prompt}`, {
      baseURL: config.public.apiBase,
    });
    return data.value;
  };

  const fetchPersons = async (prompt: string): Promise<PersonFull[] | null> => {
    const { data } = await useFetch<PersonFull[]>(
      `/api/person/search/${prompt}`,
      {
        baseURL: config.public.apiBase,
      },
    );
    return data.value;
  };

  return {
    fetchTitles,
    fetchPersons,
    fetchUsers,
  };
};
