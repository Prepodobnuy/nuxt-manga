<script lang="ts" setup>
const viewStore = useViewStore();
const { user, logged, fetchUser } = useAuth();
</script>

<template>
  <div class="placeholder" :class="{ mobile: viewStore.mobile }">
    <header class="desktop">
      <div>
        <UiButton
          color="primary"
          leading="heroicons:bars-3-16-solid"
          variant="ghost"
          label="Каталог"
          @click="navigateTo('/')"
        />
        <UiButton
          color="primary"
          leading="heroicons:magnifying-glass-16-solid"
          variant="ghost"
          label="Поиск"
          @click="viewStore.toggleViewSearch()"
        />
      </div>
      <HeaderDesktopRight />
    </header>

    <header class="mobile">
      <HeaderMobileRows />
    </header>
  </div>
</template>

<style lang="scss" scoped>
header {
  flex-shrink: 0;
}

header.desktop {
  position: relative;
  width: 100%;
  max-width: var(--header-content-width);
  justify-content: space-between;
  padding: 0 calc((var(--height) - var(--hg)) / 2);

  nav {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    top: 0;
    height: 100%;
  }

  nav,
  div {
    height: 100%;
    display: inline-flex;
    flex-direction: row;
    gap: var(--gap);
    align-items: center;
  }
}

header.mobile {
  position: relative;
  width: 100%;
  align-items: center;

  * {
    width: 100%;
    height: 100%;
  }
}

.placeholder {
  position: relative;
  display: inline-flex;
  justify-content: center;
  width: 100vw;
  --height: calc(var(--hg) * var(--xxxl));
  height: var(--height);
  background-color: var(--window-bg);
  box-shadow: var(--header-shadow);
  z-index: 1000;

  header.desktop {
    display: inline-flex;
  }
  header.mobile {
    display: none;
  }

  &.mobile {
    header.desktop {
      display: none;
    }
    header.mobile {
      display: inline-flex;
    }
  }
}
</style>
