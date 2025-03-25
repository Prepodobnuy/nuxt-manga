<script setup>
const props = defineProps({
  inputPlaceholder: { type: String, default: '' },
  emptyPlaceholder: { type: String, default: '' },
  empty: { type: Boolean, default: false },
  rows: {type: Array, default: null }, // [ {value: any, display: any} ]
});

const emit = defineEmits(['select'])

const prompt = ref('');

const viewMenu = ref(false)

const filter = () => {
  if (!props.rows) return [];

  return props.rows.filter((row) =>
    row.display.toLowerCase().includes(prompt.value.toLowerCase())
  );
};

const inputRef = ref(null);
const menuRef = ref(null);

const handleClickOutside = (event) => {
  if (
    menuRef.value && !menuRef.value.contains(event.target)
  ) {
    viewMenu.value = false;
  }
};

onMounted(() => {
  document.addEventListener('mousedown', handleClickOutside);
});

onUnmounted(() => {
  document.removeEventListener('mousedown', handleClickOutside);
});
</script>

<template>
  <article class="row-menu" ref="menuRef">
    <UiDefaultInput 
      :placeholder="inputPlaceholder" 
      v-model="prompt"
      @mousedown="viewMenu=!viewMenu"
      ref="inputRef"/>
    <Transition name="fromtop">
      <menu class="filled" v-if="viewMenu">
        <div class="rows" v-if="!empty">
          <div 
            v-for="row in filter()"
            class="entry" 
            @mousedown="emit('select', row.value)"
          >
            {{ row.display }}
          </div>
        </div>
        <div class="empty" v-else>{{ emptyPlaceholder }}</div>
      </menu>
    </Transition>
  </article>
</template>

<style lang="scss" scoped>

article.row-menu {
  position: relative;
  display: flex;
  
  flex-direction: column;
  gap: var(--row-gap-2);

  width: 100%;

  menu.filled {
    position: absolute;
    display: flex;

    left: 0;
    top: calc(100% + var(--row-gap-2));

    flex-direction: column;
    align-items: center;
    justify-content: start;

    height: 300px;
    width: 100%;
    background-color: var(--color-background-8);
    box-shadow: inset 0 0 0 1px var(--color-text-0);

    .rows {
      display: flex;

      padding: 1px;
      flex-direction: column;
      max-height: 100%;
      height: max-content;
      width: 100%;
      overflow-y: auto;

      .entry {
        cursor: pointer;

        display: flex;
        flex-direction: row;
        flex-wrap: nowrap;
        flex-shrink: 0;
        justify-content: start;
        align-items: center;

        user-select: none;

        height: var(--input-height);
        padding: var(--input-padding);
        border-radius: var(--input-borrad);
        transition: transform 0.12s, background-color 0.18s;
        font-size: 90%;
        
        &:hover {
          background-color: var(--color-primary-background-8);
        }

        &:active {
          transform: translateY(4px);
        }
      }
    }

    .empty {
      width: 100%;
      height: 100%;
      display: flex;
      opacity: 0.7;

      justify-content: center;
      align-items: center;
    }
  }
}

</style>