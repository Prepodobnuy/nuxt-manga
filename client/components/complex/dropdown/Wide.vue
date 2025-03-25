<script setup>
import { UiDefaultButton } from '#components';

const props = defineProps({
  inputPlaceholder: { type: String, default: '' },
  emptyPlaceholder: { type: String, default: '' },
  empty: { type: Boolean, default: false },
  rows: {type: Array, default: null }, // [ value: any ]
});

const emit = defineEmits(['select'])

const viewMenu = ref(false)

const model = defineModel();

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
    <UiDefaultButton 
      :caption="rows[model]"
      @mousedown="viewMenu=!viewMenu"
      ref="inputRef"  
    />
    <Transition name="fromtop">
      <menu class="filled" v-if="viewMenu">
        <div class="rows" v-if="!empty">
          <div 
            v-for="(row, index) in rows"
            class="entry" 
            @mousedown="emit('select', index); model=index; viewMenu=false"
          >
            {{ row }}
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

  width: max-content;
  height: max-content;

  menu.filled {
    position: absolute;
    display: flex;

    left: 0;
    top: calc(100% + var(--row-gap-2));

    flex-direction: column;
    align-items: center;
    justify-content: start;

    height: max-content;
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

      .entry {
        cursor: pointer;
        user-select: none;

        display: flex;

        flex-direction: row;
        flex-wrap: nowrap;
        flex-shrink: 0;
        justify-content: start;
        align-items: center;

        height: var(--input-height);
        padding: var(--input-padding);
        border-radius: var(--input-borrad);

        font-size: 90%;

        transition: transform 0.12s, background-color 0.18s;
        
        &:hover {
          background-color: var(--color-primary-background-8);
        }

        &:active {
          transform: translateY(4px);
        }
      }
    }

    .empty {
      display: flex;

      justify-content: center;
      align-items: center;
    }
  }
}

</style>