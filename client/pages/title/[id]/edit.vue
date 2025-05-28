<script setup lang="ts">
import { useTitleStore } from "~/stores/useTitleStore";

const config = useRuntimeConfig();
const { user } = useAuth();
const { tagsRef, genresRef } = useTags();
const { mobile } = useViewportLE();

const route = useRoute();
const id = Number(route.params.id);
const store = useTitleStore(id);

const { total_rates, rate_percent, average_rating } = storeToRefs(
  useTitleStore(id),
);

const images = () =>
  store.form.cover_ids.map((v) => {
    return `${config.public.apiBase}/api/asset/title/${id}/cover/${v}`;
  });
const cover = `${config.public.apiBase}/api/asset/title/${id}/cover`;
</script>
