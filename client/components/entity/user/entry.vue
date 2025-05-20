<script setup lang="ts">
import { UiFallbackImg } from "#components";
import type { User } from "~/types/user";

const { user } = defineProps<{
  user?: User;
}>();

const config = useRuntimeConfig();
const pfp = `${config.public.apiBase}/api/asset/user/${user?.uuid}/pfp`;
</script>

<template>
  <UiEntryRaw v-if="user" class="entry-wrapper" clickable>
    <UiFallbackImg class="pfp" :src="pfp" />
    <div class="names">
      <h6 class="nickname">{{ user.nickname }}</h6>
      <h6 v-if="user.username !== user.nickname" class="username">
        {{ user.username }}
      </h6>
    </div>
  </UiEntryRaw>
</template>

<style lang="scss" scoped>
.entry-wrapper {
  padding: var(--pd);

  .pfp {
    height: 100%;
    aspect-ratio: 1/1;
    border-radius: var(--br);
  }

  .names {
    display: flex;
    flex-direction: column;
    white-space: nowrap;
    .username {
      font-size: 0.9em;
      opacity: 0.9;
    }
  }
}
</style>
