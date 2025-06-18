<script setup lang="ts">
import {
  EntityTitleCard,
  UiButton,
  UiDropdown,
  UiImageCarousel,
} from "#components";
import { Transition } from "vue";
import { useTitleStore } from "~/stores/useTitleStore";
import type { Tag } from "~/types/tag";

const { user, logged } = useAuth();
const selected_section = ref(0);
const { tagsRef, genresRef } = useTags();
const { mobile } = useViewportLE();
const route = useRoute();
const router = useRouter();
const id = Number(route.params.id);
const store = useTitleStore(id);
const { total_rates, rate_percent, average_rating, sorted_pages } = storeToRefs(
  useTitleStore(id),
);
const tabs = [{ label: "О тайтле" }, { label: "Главы" }];
const config = useRuntimeConfig();
const images = () =>
  store.form.cover_ids.map((v) => {
    return `${config.public.apiBase}/api/asset/title/${id}/cover/${v}`;
  });
const cover = `${config.public.apiBase}/api/asset/title/${id}/cover`;

const getTag = (id: number): Tag | null => {
  if (!tagsRef.value) return null;
  const tag = tagsRef.value.filter((v) => {
    return v.id === id;
  });
  if (tag.length > 0) return tag[0];
  return null;
};

const getGenre = (id: number): Tag | null => {
  if (!genresRef.value) return null;
  const tag = genresRef.value.filter((v) => {
    return v.id === id;
  });
  if (tag.length > 0) return tag[0];
  return null;
};

const read = () => {
  navigateTo(`/title/${id}/read`);
};

const read_from = (i: number) => {
  const volume = sorted_pages.value[i].volume;
  const chapter = sorted_pages.value[i].chapter;
  const order = sorted_pages.value[i].order;
  navigateTo(
    `/title/${id}/read?volume=${volume}&chapter=${chapter}&order=${order}`,
  );
};

const rate = async (rate: number) => {
  await store.postRate(rate);
};

onMounted(() => {
  const section = parseInt(route.query.selected_section as string, 10) || 0;
  selected_section.value = Math.max(0, section);
});

watch(selected_section, (newValue) => {
  router.replace({
    query: {
      ...route.query,
      selected_section: newValue > 0 ? newValue.toString() : undefined,
    },
  });
});
</script>

<template>
  <LayoutPseudoHeader>
    <template #header>
      <div class="title-header">
        <UiButton
          variant="ghost"
          leading="heroicons:arrow-left-16-solid"
          icon
        />
        <h4>{{ store.form.title_ru }}</h4>
      </div>
    </template>

    <div class="content">
      <aside v-if="!mobile">
        <div class="image-wrapper">
          <UiImageCarousel
            width="300"
            height="424"
            class="image"
            :images="images()"
          />
          <div
            v-if="user?.moder || user?.admin || user?.translator"
            class="low-tab"
          >
            <UiButton
              v-if="user?.moder || user?.admin"
              icon
              leading="heroicons:pencil-solid"
              size="sm"
              @click="navigateTo(`/title/${id}/edit`)"
            />
            <UiButton
              v-if="user?.translator"
              icon
              leading="heroicons:language-16-solid"
              size="sm"
              @click="navigateTo(`/title/${id}/pages`)"
            />
          </div>
        </div>

        <UiButton
          label="Читать"
          leading="heroicons:book-open-16-solid"
          start
          @click="read()"
        />

        <TitleMeta :id="id" v-if="!mobile" />
      </aside>

      <main>
        <div v-if="mobile" class="mobile-entry-wrapper">
          <UiFallbackImg class="bg" :src="cover" />
          <UiFallbackImg class="image" :src="cover" />

          <div class="titles">
            <h3>{{ store.form.title_ru }}</h3>
            <h5>{{ store.form.title_en }}</h5>
          </div>

          <div class="actions">
            <div class="primary">
              <UiButton
                label="Читать"
                size="xl"
                variant="soft"
                leading="heroicons:book-open-16-solid"
                @click="read()"
              />
            </div>

            <div class="minor">
              <UiButton
                v-if="user?.moder || user?.admin"
                leading="heroicons:pencil-solid"
                size="xl"
                variant="soft"
                @click="navigateTo(`/title/${id}/edit`)"
              />
              <UiButton
                v-if="user?.translator"
                leading="heroicons:language-16-solid"
                size="xl"
                variant="soft"
                @click="navigateTo(`/title/${id}/pages`)"
              />
            </div>
          </div>

          <div />
          <div />
          <div />
          <div />

          <TitleMeta :id="id" v-if="mobile" />
        </div>
        <div v-if="!mobile" class="titles">
          <h3>{{ store.form.title_ru }}</h3>
          <h5>{{ store.form.title_en }}</h5>
        </div>

        <UiTabs
          style="overflow: hidden; border-radius: var(--br)"
          v-model="selected_section"
          :tabs="tabs"
          full-width
          variant="solid"
        />

        <Transition name="page">
          <section v-if="selected_section === 0">
            <div v-if="store.form.tags || store.form.genres" class="tags">
              <UiButton
                v-if="store.form.tags"
                v-for="t in store.form.tags"
                leading="heroicons:tag-16-solid"
                :label="getTag(t)?.ru"
                :fw="false"
              />
              <UiButton
                v-if="store.form.genres"
                v-for="t in store.form.genres"
                :label="getGenre(t)?.ru"
                :fw="false"
              />
            </div>

            <div v-if="store.form.description" class="description">
              <h5>Описание</h5>
              <p>{{ store.form.description }}</p>
            </div>

            <div class="rates-body">
              <div class="header">
                <h5>Средняя оценка: {{ average_rating }}</h5>
                <UiDropdown v-if="logged" align="right">
                  <template #head>
                    <UiButton
                      leading="heroicons:star-16-solid"
                      label="Оценить"
                      color="primary"
                      variant="ghost"
                      :fw="false"
                    />
                  </template>
                  <UiButton
                    v-for="i in [5, 4, 3, 2, 1]"
                    :key="i"
                    :toggle="store.form.user_rate === i"
                    :label="`${i}`"
                    leading="heroicons:star-16-solid"
                    color="primary"
                    variant="ghost"
                    start
                    roundness="none"
                    @click="rate(i)"
                  />
                </UiDropdown>
              </div>

              <div class="rows">
                <Transition name="ratechange" mode="out-in">
                  <div class="row rate-5">
                    <div class="mark">
                      <Icon name="heroicons:star-16-solid" /> 5
                    </div>
                    <div class="line-wrapper">
                      <div
                        class="line"
                        :style="`width: ${rate_percent.rate5}%`"
                      />
                    </div>
                    <div class="percent">{{ rate_percent.rate5 }}%</div>
                    <div class="rates">{{ store.form.rates_5 ?? 0 }}</div>
                  </div>
                </Transition>

                <Transition name="ratechange" mode="out-in">
                  <div class="row rate-4">
                    <div class="mark">
                      <Icon name="heroicons:star-16-solid" /> 4
                    </div>
                    <div class="line-wrapper">
                      <div
                        class="line"
                        :style="`width: ${rate_percent.rate4}%`"
                      />
                    </div>
                    <div class="percent">{{ rate_percent.rate4 }}%</div>
                    <div class="rates">{{ store.form.rates_4 ?? 0 }}</div>
                  </div>
                </Transition>

                <Transition name="ratechange" mode="out-in">
                  <div class="row rate-3">
                    <div class="mark">
                      <Icon name="heroicons:star-16-solid" /> 3
                    </div>
                    <div class="line-wrapper">
                      <div
                        class="line"
                        :style="`width: ${rate_percent.rate3}%`"
                      />
                    </div>
                    <div class="percent">{{ rate_percent.rate3 }}%</div>
                    <div class="rates">{{ store.form.rates_3 ?? 0 }}</div>
                  </div>
                </Transition>

                <Transition name="ratechange" mode="out-in">
                  <div class="row rate-2">
                    <div class="mark">
                      <Icon name="heroicons:star-16-solid" /> 2
                    </div>
                    <div class="line-wrapper">
                      <div
                        class="line"
                        :style="`width: ${rate_percent.rate2}%`"
                      />
                    </div>
                    <div class="percent">{{ rate_percent.rate2 }}%</div>
                    <div class="rates">{{ store.form.rates_2 ?? 0 }}</div>
                  </div>
                </Transition>

                <Transition name="ratechange" mode="out-in">
                  <div class="row rate-1">
                    <div class="mark">
                      <Icon name="heroicons:star-16-solid" /> 1
                    </div>
                    <div class="line-wrapper">
                      <div
                        class="line"
                        :style="`width: ${rate_percent.rate1}%`"
                      />
                    </div>
                    <div class="percent">{{ rate_percent.rate1 }}%</div>
                    <div class="rates">{{ store.form.rates_1 ?? 0 }}</div>
                  </div>
                </Transition>
              </div>
            </div>
          </section>
        </Transition>

        <Transition name="page">
          <section v-if="selected_section === 1" class="pages">
            <div
              class="page"
              v-for="(page, index) in sorted_pages"
              :key="page.id"
              @click="read_from(index)"
            >
              <div class="meta">
                <div class="volume">Том {{ page.volume }}</div>
                <div class="chapter">Глава {{ page.chapter }}</div>
                <div class="order">Страница {{ page.order }}</div>
              </div>
              <UiButton label="читать" :fw="false" variant="outline" />
            </div>
          </section>
        </Transition>

        <section v-if="selected_section === 2">2</section>
      </main>
    </div>
  </LayoutPseudoHeader>
</template>

<style lang="scss" scoped>
@use "@/assets/mixins";
@use "@/assets/variables";
@use "@/assets/functions";

.content {
  @include mixins.page-content;
  padding: calc(var(--gap) * var(--xxl));
  gap: calc(var(--gap) * var(--xxl));
  display: inline-flex;
  flex-direction: row;

  aside {
    width: 300px;
    flex-shrink: 0;
    height: max-content;
    display: flex;
    flex-direction: column;
    gap: calc(var(--gap) * var(--xxl));

    .image-wrapper {
      background-color: var(--neutral-bg);
      border-radius: var(--br);
      overflow: hidden;
      position: relative;
      display: flex;
      flex-direction: column;

      .low-tab {
        display: inline-flex;
        gap: var(--gap);
        justify-content: space-evenly;
        align-items: center;
        background-color: var(--neutral-bg);
        height: var(--hg);
        width: 100%;
        bottom: 0;
        left: 0;
      }
    }
  }

  main {
    height: max-content;
    display: flex;
    flex-direction: column;
    width: 100%;
    flex-shrink: 1;
    gap: calc(var(--gap) * var(--xxl));

    section {
      display: flex;
      flex-direction: column;
      gap: calc(var(--gap) * var(--xxl));
    }

    .tags {
      display: flex;
      flex-direction: row;
      gap: var(--gap);
      flex-wrap: wrap;
    }

    .description {
      display: flex;
      flex-direction: column;
      gap: var(--gap);
    }

    .rates-body {
      display: flex;
      flex-direction: column;
      gap: var(--gap);
      background-color: var(--neutral-bg);
      padding: var(--pd);
      border-radius: var(--br);

      .header {
        display: inline-flex;
        justify-content: space-between;
        align-items: center;
      }

      .rows {
        display: flex;
        flex-direction: column;
        gap: var(--gap);
        border-radius: var(--br);

        .row {
          position: relative;
          display: inline-flex;
          height: var(--hg);
          width: 100%;
          align-items: center;
          gap: var(--gap);

          &.rate-5 {
            --line-bg: color-mix(in srgb, white 10%, var(--primary-bg) 100%);
          }
          &.rate-4 {
            --line-bg: color-mix(in srgb, white 20%, var(--primary-bg) 100%);
          }
          &.rate-3 {
            --line-bg: color-mix(in srgb, white 40%, var(--primary-bg) 100%);
          }
          &.rate-2 {
            --line-bg: color-mix(in srgb, white 60%, var(--primary-bg) 100%);
          }
          &.rate-1 {
            --line-bg: color-mix(in srgb, white 80%, var(--primary-bg) 100%);
          }

          * {
            flex-shrink: 0;
          }

          .line-wrapper {
            width: 100%;
            height: 100%;
            flex-shrink: 1;
            border-radius: var(--br);
            display: flex;
            align-items: center;
            background-color: var(--layer);

            .line {
              height: 100%;
              opacity: 0.9;
              background-color: var(--line-bg);
              border-radius: var(--br);
              transition: width 0.46s ease;
            }
          }

          .mark {
            display: inline-flex;
            width: max-content;
            gap: 4px;
            justify-content: start;
            align-items: center;
            z-index: 100;

            position: absolute;
            height: 100%;
            top: 0%;
            left: calc(var(--pd) * 2);
          }

          .rates,
          .percent {
            position: absolute;
            height: 100%;
            top: 0%;
            font-size: 0.95em;
            z-index: 100;
          }

          .rates {
            display: inline-flex;
            width: 50px;
            gap: 4px;
            text-align: end;
            flex-shrink: 0;
            text-align: end;
            justify-content: end;
            overflow: hidden;
            align-items: center;
            right: calc(var(--pd) * 2);
          }

          .percent {
            display: inline-flex;
            width: 60px;
            gap: 4px;
            text-align: end;
            justify-content: end;
            flex-shrink: 0;
            align-items: center;
            overflow: hidden;
            right: calc(var(--pd) * 2 + 50px);
          }
        }
      }

      .total-row {
        display: inline-flex;
        align-items: center;
        justify-content: end;
        width: 100%;
        background-color: unset;
        padding: 0 var(--pd);
        font-size: var(--fs);
        .rates {
          gap: 4px;
          text-align: end;
          flex-shrink: 1;
          font-size: 1em;
          opacity: 1;
        }
      }
    }

    .mobile-entry-wrapper {
      position: relative;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 20px;
      overflow: hidden;
      border-radius: var(--br);
      gap: calc(var(--gap));

      .bg {
        position: absolute;
        width: 100%;
        height: 100%;
        filter: blur(25px) opacity(0.5);
      }

      .titles {
        justify-content: center;
        align-items: center;
        text-align: center;
        z-index: 100;
      }

      .image {
        max-width: 320px;
        width: 100%;
        aspect-ratio: 1080/1527;
        border-radius: var(--br);
      }
      .actions {
        display: flex;
        flex-direction: column;
        z-index: 100;
        max-width: 400px;
        width: 100%;
        gap: calc(var(--gap));

        button {
          backdrop-filter: blur(15px);
          font-size: 0.94em;
        }

        .primary {
          gap: calc(var(--gap));
          width: 100%;
          display: inline-flex;
        }

        .minor {
          gap: calc(var(--gap));
          display: inline-flex;
          justify-content: space-evenly;
        }
      }
    }
  }
}

.pages {
  display: flex;
  flex-direction: column;
  gap: 0 !important;

  .page {
    display: inline-flex;
    gap: var(--gap);
    padding: var(--pd);
    background-color: var(--neutral-bg);
    justify-content: space-between;
    align-items: center;

    &:last-child {
      border-radius: 0 0 var(--br) var(--br);
    }
    &:first-child {
      border-radius: var(--br) var(--br) 0 0;
    }

    .meta {
      display: inline-flex;
      gap: var(--gap);
    }
  }
}

.title-header {
  display: inline-flex;
  align-items: center;
  gap: var(--gap);
}

.ratechange-enter-active,
.ratechange-leave-active {
  transition: all 0.25s;
}
.ratechange-enter-from,
.ratechange-leave-to {
  opacity: 0;
  filter: blur(1rem);
}
</style>
