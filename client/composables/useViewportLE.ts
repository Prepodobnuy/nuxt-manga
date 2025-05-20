import { useNuxtApp } from "#app";

export const useViewportLE = (breakpoint: string = "tablet") => {
  const { $viewport } = useNuxtApp();
  const mobile = ref(false);

  const update = () => {
    mobile.value = $viewport.isLessOrEquals(breakpoint);
  };

  onMounted(() => {
    update();
    const unwatch = watch($viewport.breakpoint, update);

    onUnmounted(() => {
      unwatch();
    });
  });

  return {
    mobile,
    isActive: computed(() => mobile.value),
  };
};
