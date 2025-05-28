<script setup lang="ts">
useInitHue();
</script>

<template>
  <div class="app-wrapper">
    <slot />
  </div>
</template>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Ubuntu:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&display=swap");

.app-wrapper {
  --h: var(--hue, 360deg);
  --primary-100: hsl(var(--h), 37%, 77%);
  --primary-200: hsl(var(--h), 75%, 65%);
  --primary-300: hsl(var(--h), 81%, 56%);
  --primary-400: hsl(var(--h), 77%, 48%);
  --primary-500: hsl(var(--h), 75%, 40%);
  --blue-100: #99c1f1;
  --blue-200: #62a0ea;
  --blue-300: #3584e4;
  --blue-400: #1c71d8;
  --blue-500: #1a5fb4;
  --green-100: #8ff0a4;
  --green-200: #57e389;
  --green-300: #33d17a;
  --green-400: #2ec27e;
  --green-500: #26a269;
  --yellow-100: #f9f06b;
  --yellow-200: #f8e45c;
  --yellow-300: #f6d32d;
  --yellow-400: #f5c211;
  --yellow-500: #e5a50a;
  --orange-100: #ffbe6f;
  --orange-200: #ffa348;
  --orange-300: #ff7800;
  --orange-400: #e66100;
  --orange-500: #c64600;
  --red-100: #f66151;
  --red-200: #ed333b;
  --red-300: #e01b24;
  --red-400: #c01c28;
  --red-500: #a51d2d;
  --purple-100: #dc8add;
  --purple-200: #c061cb;
  --purple-300: #9141ac;
  --purple-400: #813d9c;
  --purple-500: #613583;
  --brown-100: #cdab8f;
  --brown-200: #b5835a;
  --brown-300: #986a44;
  --brown-400: #865e3c;
  --brown-500: #63452c;
  --light-100: #ffffff;
  --light-200: #f7f6f5;
  --light-300: #deddda;
  --light-400: #c0bfbc;
  --light-500: #9a9996;
  --dark-100: #77767b;
  --dark-200: #5e5c64;
  --dark-300: #3d3846;
  --dark-400: #241f31;
  --dark-500: #000000;

  --hg: 34px;
  --br: 5px;
  --pd: 6px;
  --fs: 14px;
  --gap: 8px;

  --xs: 0.7;
  --sm: 0.85;
  --md: 1;
  --lg: 1.15;
  --xl: 1.3;
  --xxl: 1.5;
  --xxxl: 1.7;

  width: 100%;
  height: 100%;
  min-height: 100vh;
  --layer: color-mix(in srgb, transparent 100%, black 8%);

  * {
    font-family: "Ubuntu", sans-serif;
    font-weight: 400;
    font-style: normal;
  }
}

:root {
  --root-fs: var(--fs, 14px);
}

.light-mode .app-wrapper {
  --neutral-bg: var(--light-200);
  --neutral-fg: var(--dark-500);
  --neutral-bg-active: var(--light-100);
  --neutral-fg-active: var(--dark-500);

  --primary-bg: var(--primary-300);
  --primary-fg: var(--light-100);
  --primary-bg-active: var(--primary-400);
  --primary-fg-active: var(--light-200);

  --success-bg: var(--green-300);
  --success-fg: var(--dark-500);
  --success-bg-active: var(--green-400);
  --success-fg-active: var(--dark-500);

  --warning-bg: var(--yellow-300);
  --warning-fg: var(--dark-500);
  --warning-bg-active: var(--yellow-400);
  --warning-fg-active: var(--dark-500);

  --error-bg: var(--red-300);
  --error-fg: var(--light-100);
  --error-bg-active: var(--red-400);
  --error-fg-active: var(--light-100);

  --theme-color: var(--light-100);
  --reverse-color: var(--dark-500);
  --bg-0: var(--light-500);
  --bg-1: var(--light-400);
  --bg-2: var(--light-300);
  --bg-3: var(--light-200);

  --view-bg: #ffffff;
  --window-bg: #e3e3e3;
  --sidebar-bg: #e9e9e9;
  --shadow-color: #00000033;
  --header-shadow: 0 0 4px 1px var(--shadow-color);

  --break-desktop: 1200px;
  --break-mobile: 876px;

  background: var(--window-bg);
  color: var(--dark-500);
}

.dark-mode .app-wrapper {
  --neutral-bg: color-mix(
    in srgb,
    var(--dark-500) 100%,
    var(--reverse-color) 35%
  );
  --neutral-fg: var(--light-100);
  --neutral-bg-active: color-mix(
    in srgb,
    var(--dark-500) 100%,
    var(--reverse-color) 40%
  );
  --neutral-fg-active: var(--light-100);

  --primary-bg: var(--primary-300);
  --primary-fg: var(--light-100);
  --primary-bg-active: var(--primary-400);
  --primary-fg-active: var(--light-200);

  --success-bg: var(--green-400);
  --success-fg: var(--dark-500);
  --success-bg-active: var(--green-500);
  --success-fg-active: var(--dark-500);

  --warning-bg: var(--yellow-400);
  --warning-fg: var(--dark-500);
  --warning-bg-active: var(--yellow-500);
  --warning-fg-active: var(--dark-500);

  --error-bg: var(--red-400);
  --error-fg: var(--light-100);
  --error-bg-active: var(--red-500);
  --error-fg-active: var(--light-100);

  --theme-color: var(--dark-500);
  --reverse-color: var(--light-100);
  --bg-0: var(--dark-500);
  --bg-1: var(--dark-400);
  --bg-2: var(--dark-300);
  --bg-3: var(--dark-200);

  --view-bg: #1e1e1e;
  --window-bg: #242424;
  --sidebar-bg: #303030;
  --shadow-color: #00000033;
  --header-shadow: 0 0 4px 1px var(--shadow-color);

  --break-desktop: 1200px;
  --break-mobile: 876px;

  background: var(--window-bg);
  color: var(--light-100);
  * {
    color: var(--light-100);
  }
}
</style>
