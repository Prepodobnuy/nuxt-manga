<template>
  <div class="placeholder">
    <div class="row">
      <p>Автор</p>
      <div class="info">ПИДОР</div>
    </div>
    <div class="row">
      <p>Художник</p>
      <div class="info">ПИДОР</div>
    </div>
    <div class="row">
      <p>Мангака</p>
      <div class="info">ПИДОР</div>
    </div>
    <div class="row">
      <p>Издательство</p>
      <div class="info">ПИДОР</div>
    </div>
    <div class="row">
      <p>Название</p>
      <div class="info">ПИДОР</div>
    </div>
    <div class="row">
      <p>Название на английском</p>
      <div class="info">ПИДОР</div>
    </div>
    <div class="row">
      <p>Название на языке оригинала</p>
      <div class="info">ПИДОР</div>
    </div>
    <div class="row">
      <p>Альтернативные названия</p>
      <div class="info">ПИДОР</div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.placeholder {
  width: 100%;
  background-color: var(--neutral-bg);
  color: var(--neutral-fg);
  border-radius: var(--br);
  padding: var(--pd);
  font-size: var(--fs);
  display: flex;
  flex-direction: column;
  gap: var(--gap);

  .row {
    display: flex;
    flex-direction: column;
    p {
      font-size: 0.95em;
    }
    .info {
      font-size: 1em;
    }
  }
}
</style>
