export const useTranslateTeamForm = defineStore("translateForm", () => {
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

  const validate = () => {
    valid.value.title =
      typeof form.title !== "undefined" &&
      form.title.length > 1 &&
      form.title.length < 100;
  };

  const post = () => {};

  return {
    form,
    valid,
    clear,
    post,
  };
});
