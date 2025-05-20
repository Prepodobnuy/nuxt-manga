<script setup lang="ts">
interface Entry {
  display: string;
  select: number;
}

const model = defineModel<string>();
const input = ref<HTMLInputElement>();
const wrapper = ref<HTMLInputElement>();
const active = ref(false);

const { entries } = defineProps<{
  entries?: Entry[];
}>();

const emit = defineEmits<{
  select: [id: number];
}>();

const select = (entry: Entry) => {
  emit("select", entry.select);
};

const filtered = computed<Entry[] | undefined>(() => {
  if (!model.value) return entries;
  return entries.filter((item) =>
    item.display.toLowerCase().includes(model.value.toLowerCase()),
  );
});

onClickOutside(wrapper, () => {
  active.value = false;
});

const toggleActive = () => {
  active.value = !active.value;
};
</script>

<template>
  <div ref="wrapper" class="wrapper">
    <UiInput
      ref="input"
      v-model="model"
      variant="outline"
      @click="toggleActive()"
    />
    <menu v-if="active">
      <UiButton
        v-for="(entry, index) in filtered"
        variant="ghost"
        :label="entry.display"
        start
        @click.stop="select(entry)"
      />
    </menu>
  </div>
</template>

<style lang="scss" scoped>
menu {
  display: flex;
  flex-direction: column;
  max-height: 300px;
  overflow: auto;

  * {
    flex-shrink: 0;
  }
}
.wrapper {
  display: flex;
  flex-direction: column;
}
</style>
