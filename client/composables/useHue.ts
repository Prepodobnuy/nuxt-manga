import { useCookie } from "#app";
import type { CookieRef } from "#app";
import { onMounted } from "vue";

export function useSetHue(value: number) {
  if (typeof document === "undefined") {
    return;
  }
  const hue = useCookie<number>("hue", {
    maxAge: 3600 * 24 * 10,
    default: () => 213,
    watch: true,
  });
  hue.value = value;
  document.documentElement.style.setProperty("--hue", `${hue.value}deg`);
}

export function useGetHue(): CookieRef<number> | undefined {
  if (typeof document === "undefined") {
    return;
  }
  const hue = useCookie<number>("hue", {
    maxAge: 3600 * 24 * 10,
    default: () => 213,
    watch: false,
  });
  return hue;
}

export function useGetHueValue(): number | undefined {
  return useGetHue()?.value;
}

export function useInitHue() {
  const hue = useGetHue();
  if (typeof hue !== "undefined") {
    useSetHue(hue.value);

    onMounted(() => {
      useSetHue(hue.value);
    });
  }
}
