<script lang="ts" setup>
import Cropper from "cropperjs";
import "cropperjs/dist/cropper.css";

const {
  aspect = 16 / 9,
  width = 200,
  color = "neutral",
  variant = "solid",
} = defineProps<{
  aspect?: number;
  width?: number;
  color?: "neutral" | "primary" | "success" | "warning" | "error";
  variant?: "solid" | "outline" | "soft" | "softborder" | "ghost" | "link";
}>();

const model = defineModel<File | undefined>();

const file = ref<HTMLInputElement>();
const image = ref<HTMLImageElement>();
const edit = ref(false);
const editValue = ref<string>();
const cropper = ref<Cropper>();
const previewUrl = ref<string>();

const updatePreview = () => {
  if (model.value) {
    previewUrl.value = window.URL.createObjectURL(model.value);
    return;
  }
  previewUrl.value = "";
};

watch(model, updatePreview, { immediate: true });

onMounted(() => {
  if (model.value) {
    editValue.value = URL.createObjectURL(model.value);
    edit.value = true;
  }
});

onBeforeUnmount(() => {
  if (previewUrl.value) {
    window.URL.revokeObjectURL(previewUrl.value);
  }
});

const selectImage = () => {
  file.value?.click();
};

const imageChange = (event: Event) => {
  const input = event.target as HTMLInputElement;
  const selectedFile = input.files?.[0];

  if (!selectedFile || !selectedFile.type.startsWith("image/")) return;

  editValue.value = URL.createObjectURL(selectedFile);
  edit.value = true;
};

const stopEdit = () => {
  edit.value = false;
  cropper.value?.destroy();
  if (editValue.value) URL.revokeObjectURL(editValue.value);
};

const crop = () => {
  if (!cropper.value) return;

  cropper.value.getCroppedCanvas().toBlob((blob) => {
    if (!blob) return;

    const croppedFile = new File([blob], "image.png", {
      type: "image/png",
      lastModified: Date.now(),
    });

    model.value = croppedFile;
    stopEdit();
  }, "image/png");
};

watch([image, edit], ([img, isEdit]) => {
  if (isEdit && img) {
    cropper.value = new Cropper(img, {
      aspectRatio: aspect,
      viewMode: 1,
      autoCropArea: 1,
      responsive: true,
      guides: true,
    });
  }
});

const getSelectors = () => {
  return [`color-${color}`, `variant-${variant}`];
};
</script>

<template>
  <div class="wrapper" :style="[`--aspect: ${aspect}`, `--width: ${width}px`]">
    <div
      v-if="!edit"
      class="wrapper-preview"
      :class="getSelectors()"
      @click="selectImage"
    >
      <div class="overlay">
        <span v-if="!model">Выбрать изображение</span>
        <span v-else />
      </div>
      <input
        ref="file"
        type="file"
        accept="image/*"
        hidden
        @change="imageChange"
      />
      <img class="preview-image" v-if="previewUrl" :src="previewUrl" />
    </div>

    <div v-else class="cropper-container">
      <div class="cropper-container-image">
        <img ref="image" :src="editValue" />
      </div>
      <div class="cropper-container-inputs">
        <div style="width: 200%" />
        <UiButton label="Отмена" @click="stopEdit" variant="outline" />
        <UiButton label="Сохранить" @click="crop" />
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@use "@/assets/mixins";
@use "@/assets/variables";
@use "@/assets/functions";

.wrapper-preview {
  @include mixins.generate-colors(variables.$colors);
  @include mixins.generate-variant(
    "solid",
    (
      "bg": var(--bg),
      "color": var(--fg),
    ),
    true
  );
  @include mixins.generate-variant(
    "outline",
    (
      "bg": functions.transparent-mix(var(--bg), 60%, 30%),
      "color": var(--neutral-fg),
      "hover": functions.transparent-mix(var(--bg-active), 100%, 50%),
      "active": functions.transparent-mix(var(--bg-active), 100%, 60%),
      "focus": functions.transparent-mix(var(--bg-active), 100%, 60%),
      "border": var(--bg),
    ),
    true
  );
  @include mixins.generate-variant(
    "soft",
    (
      "bg": functions.transparent-mix(var(--bg), 10%, 75%),
      "color": var(--fg),
      "hover": functions.transparent-mix(var(--bg), 30%, 75%),
      "active": functions.transparent-mix(var(--bg), 10%, 75%),
    ),
    true
  );
  @include mixins.generate-variant(
    "softborder",
    (
      "bg": functions.transparent-mix(var(--bg), 10%, 75%),
      "color": var(--fg),
      "border": var(--bg),
      "hover": functions.transparent-mix(var(--bg), 30%, 75%),
      "active": functions.transparent-mix(var(--bg), 10%, 75%),
    ),
    true
  );
  @include mixins.generate-variant(
    "ghost",
    (
      "bg": transparent,
      "color": var(--neutral-fg),
      "hover": functions.transparent-mix(var(--bg), 90%, 15%),
      "active": functions.transparent-mix(var(--bg), 80%, 35%),
    ),
    true
  );
  @include mixins.generate-variant(
    "link",
    (
      "bg": transparent,
      "color": var(--neutral-fg),
      "active": functions.transparent-mix(var(--bg), 90%, 15%),
    ),
    true
  );
}

.wrapper {
  &-preview {
    cursor: pointer;
    position: relative;
    max-width: var(--width);
    width: 100%;
    aspect-ratio: var(--aspect);
    border-radius: var(--br);
    transition:
      filter 0.2s,
      background 0.2s,
      color 0.1s;
    overflow: hidden;

    .overlay {
      position: absolute;
      left: 0;
      top: 0;
      bottom: 0;
      right: 0;
      width: 100%;
      height: 100%;
      user-select: none;
      transition: background-color 0.25s;
      * {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        height: 100%;
        pointer-events: none;
        opacity: 0.5;
      }
    }

    .preview-image {
      transition: opacity 0.25s;
      width: 100%;
      height: 100%;
    }

    &:hover {
      .overlay {
        background-color: var(--bg);
      }
      .preview-image {
        opacity: 0.75;
      }
    }
  }

  .cropper-container {
    display: flex;
    flex-direction: column;
    gap: var(--gap);

    &-image {
      height: 400px;
      width: 100%;
      flex-shrink: 1;
    }

    &-inputs {
      display: inline-flex;
      gap: var(--gap);
      flex-shrink: 0;
    }
  }
}
</style>
