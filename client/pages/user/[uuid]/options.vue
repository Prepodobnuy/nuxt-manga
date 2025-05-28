<script setup lang="ts">
import { useUserEditForm } from "~/forms/useUserEditForm";

const { user: userval, logged, token } = useAuth();
const { form, update } = useUserEditForm();
const config = useRuntimeConfig();
const route = useRoute();
const uuid = route.params.uuid as string;
const { data: user, refresh } = useUserStore(uuid);

const pfp = `${config.public.apiBase}/api/asset/user/${user?.uuid}/pfp`;
const back = `${config.public.apiBase}/api/asset/user/${user?.uuid}/back`;

const tabs = [{ label: "Описание" }];

const calert = () => {
  console.clear();
  console.log(user);
};

const uupdate = async () => {
  await update();
  await refresh();
};

const set_back = async (file: File) => {
  const formdata = new FormData();
  formdata.append("file", file);
  const result = await $fetch(`/api/user/back`, {
    method: "POST",
    body: formdata,
    baseURL: config.public.apiBase,
    headers: {
      Authorization: `Bearer ${token.value}`,
    },
  });
};

const set_pfp = async (file: File) => {
  const formdata = new FormData();
  formdata.append("file", file);
  const result = await $fetch(`/api/user/pfp`, {
    method: "POST",
    body: formdata,
    baseURL: config.public.apiBase,
    headers: {
      Authorization: `Bearer ${token.value}`,
    },
  });
};
</script>

<template>
  <LayoutPseudoHeader>
    <template #header>
      <h4 v-show="user !== null">{{ user?.nickname }}</h4>
    </template>

    <div class="content">
      <h5>Задник</h5>
      <UiImageInput
        :aspect="2000 / 600"
        :width="700"
        variant="outline"
        :preview="back"
        @select="set_back"
      />
      <h5>Аватарка</h5>
      <UiImageInput
        :aspect="1 / 1"
        :width="200"
        variant="outline"
        :preview="pfp"
        @select="set_pfp"
      />
      <UiInput
        v-model="form.nickname"
        variant="outline"
        placeholder="Никнейм"
      />
      <UiInput v-model="form.status" variant="outline" placeholder="Статус" />
      <UiTextarea
        v-model="form.about"
        variant="outline"
        placeholder="Обо мне"
      />
      <div class="row">
        <UiButton
          color="success"
          label="Отправить"
          :fw="false"
          @click="uupdate()"
        />
      </div>
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

  flex-direction: row-reverse;
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
  }

  .header__content {
    background-color: var(--neutral-bg);
    display: inline-flex;
    flex-direction: column;
    justify-content: start;
    align-items: center;
    display: inline-flex;
    border-radius: 0 0 var(--brr) var(--brr);

    .description {
      width: 100%;
      padding: 0 var(--pd) var(--pd) var(--pd);
    }

    .row {
      width: 100%;
      position: relative;
      display: inline-flex;
      justify-content: start;
      align-items: center;
      height: calc(calc(var(--hg) * var(--xl)) * 2);
    }

    .settings {
      position: absolute;
      bottom: var(--pd);
      right: var(--pd);
    }

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
