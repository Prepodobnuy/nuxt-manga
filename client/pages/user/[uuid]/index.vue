<script setup lang="ts">
import { UiFallbackImg, UiTabs } from "#components";
import { useUserStore } from "~/stores/useUserStore";

const config = useRuntimeConfig();
const route = useRoute();
const userStore = useUserStore();
const uuid = route.params.uuid as string;

await userStore.fetchUser(uuid);
const user = computed(() => userStore.state.users[uuid]);

const pfp = `${config.public.apiBase}/api/asset/user/${user.value.uuid}/pfp`;
const back = `${config.public.apiBase}/api/asset/user/${user.value.uuid}/back`;

const tabs = [
  { label: "Описание" },
  { label: "Списки" },
  { label: "Оценки" },
  { label: "Комментарии" },
];
</script>

<template>
  <LayoutPseudoHeader>
    <template #header>
      <h4 v-show="user !== null">{{ user?.nickname }}</h4>
    </template>

    <div class="content">
      <header>
        <UiFallbackImg class="back" :src="back" />

        <div class="header__content">
          <UiFallbackImg class="pfp" :src="pfp" />

          <div class="inner">
            <div class="col">
              <div class="username">
                <p>{{ user?.nickname }}</p>
                <p v-if="user.username !== user.nickname" class="user">
                  {{ user?.username }}
                </p>
              </div>
              <div class="status">
                {{ user.status }}
              </div>
            </div>
          </div>
        </div>

        <UiTabs class="tabs" :tabs="tabs" full-width />
      </header>
      <div><UiTextarea /></div>
      <div><UiTextarea /></div>
      <div><UiTextarea /></div>
      <div><UiTextarea /></div>
      <div><UiTextarea /></div>
      <div><UiTextarea /></div>
      <div><UiTextarea /></div>
      <div><UiTextarea /></div>
      <div><UiTextarea /></div>
      <div><UiTextarea /></div>
      <div><UiTextarea /></div>
      <div><UiTextarea /></div>
      <div><UiTextarea /></div>
      <div><UiTextarea /></div>
      <div><UiTextarea /></div>
      <div><UiTextarea /></div>
    </div>
  </LayoutPseudoHeader>
</template>

<style lang="scss" scoped>
@use "@/assets/mixins";
@use "@/assets/variables";
@use "@/assets/functions";

.content {
  @include mixins.page-content;
  padding: 20px;
  gap: var(--gap);
}

.row {
  display: inline-flex;
  gap: var(--gap);
  margin-top: 1em;
}

.tags-row {
  display: flex;
  gap: var(--gap);
  flex-wrap: wrap;
}

header {
  --brr: calc(var(--br) * var(--xxl));
  display: flex;
  flex-direction: column;

  .back {
    width: 100%;
    aspect-ratio: 2000/300;
    flex-shrink: 0;
    border-radius: var(--brr) var(--brr) 0 0;
  }

  .tabs {
    overflow: hidden;
    border-radius: 0 0 var(--brr) var(--brr);
  }

  .header__content {
    background-color: var(--neutral-bg);
    position: relative;
    display: inline-flex;
    justify-content: start;
    align-items: center;
    display: inline-flex;
    height: calc(calc(var(--hg) * var(--xl)) * 2);

    .pfp {
      position: absolute;
      width: clamp(90px, 14vw, 140px);
      aspect-ratio: 1/1;
      flex-shrink: 0;
      bottom: var(--pd);
      left: var(--pd);
      border-radius: var(--br);
      box-shadow: 0 0 4px 0 var(--neutral-bg);
      z-index: 150;
    }

    .inner {
      padding: var(--pd);
      margin-left: clamp(calc(90px + var(--pd)), 16vw, calc(140px + var(--pd)));
      width: 100%;
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: start;
      align-items: start;
    }
  }

  .col {
    display: flex;
    flex-direction: column;
    gap: var(--gap);

    .username {
      display: inline-flex;
      gap: var(--gap);
      align-items: end;
      .user {
        opacity: 0.75;
        font-size: 0.9em;
      }
    }
  }
}
</style>
