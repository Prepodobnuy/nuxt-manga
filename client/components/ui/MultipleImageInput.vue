<script setup lang="ts">
import Cropper from "cropperjs";
import "cropperjs/dist/cropper.css";

const { mobile } = useViewStore();

const {
  aspect = 16 / 9,
  height = 300,
  color = "neutral",
  variant = "solid",
  limit = 10,
} = defineProps<{
  aspect?: number;
  height?: number;
  color?: "neutral" | "primary" | "success" | "warning" | "error";
  variant?: "solid" | "outline" | "soft" | "softborder" | "ghost" | "link";
  limit?: number;
}>();

const model = defineModel<File[]>({ default: () => [] });

const cropper = ref<Cropper>();
const file = ref<HTMLInputElement>();
const image = ref<HTMLImageElement>();
const edit = ref(false);
const editValue = ref<string>();
const editFile = ref<File | null>(null);
const editIndex = ref<number | null>(null);
const controlsVisibility = ref<boolean[]>([]);

const previewImages = computed<URL[]>(() => {
  if (!process.client || !model.value) return [];
  return model.value.map((file) => URL.createObjectURL(file));
});

watch(
  model,
  (newVal) => {
    controlsVisibility.value = new Array(newVal.length).fill(false);
  },
  { immediate: true },
);

onBeforeUnmount(() => {
  previewImages.value.forEach((url) => URL.revokeObjectURL(url));
});

const imageChange = (event: Event) => {
  const input = event.target as HTMLInputElement;
  const selectedFile = input.files?.[0];

  if (!selectedFile || !selectedFile.type.startsWith("image/")) return;

  editFile.value = selectedFile;
  editValue.value = URL.createObjectURL(selectedFile);
  edit.value = true;
};

const stopEdit = () => {
  edit.value = false;
  cropper.value?.destroy();
  if (editValue.value) URL.revokeObjectURL(editValue.value);
  if (editIndex.value !== null) editIndex.value = null;
  if (editFile.value) editFile.vakue = null;
};
const crop = () => {
  if (!cropper.value) return;

  cropper.value.getCroppedCanvas().toBlob((blob) => {
    if (!blob) return;

    const croppedFile = new File([blob], "image", {
      type: editFile.value.type,
      lastModified: Date.now(),
    });

    let updatedModel = [...model.value];
    if (editIndex.value !== null) {
      updatedModel[editIndex.value] = croppedFile;
    } else {
      updatedModel.push(croppedFile);
    }
    model.value = updatedModel;
    stopEdit();
  }, editFile.value.type);
};

const addImage = () => {
  file.value?.click();
};

const moveLeft = (index: number) => {
  controlsVisibility.value[index] = false;
  if (index <= 0) return;
  const arr = [...model.value];
  [arr[index - 1], arr[index]] = [arr[index], arr[index - 1]];
  model.value = arr;
};

const moveRight = (index: number) => {
  controlsVisibility.value[index] = false;
  if (index >= model.value.length - 1) return;
  const arr = [...model.value];
  [arr[index], arr[index + 1]] = [arr[index + 1], arr[index]];
  model.value = arr;
};

const editImage = (index: number) => {
  const file = model.value[index];
  if (!file) return;

  editIndex.value = index;
  editValue.value = URL.createObjectURL(file);
  edit.value = true;
};

const deleteImage = (index: number) => {
  const arr = [...model.value];
  arr.splice(index, 1);
  model.value = arr;
};

onMounted(() => {
  if (model.value) {
    model.value.forEach((element) => {
      files.value = [...files.value, element];
    });
  }
});

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

const viewOverflow = (index: number) => {
  setTimeout(() => {
    controlsVisibility.value[index] = !controlsVisibility.value[index];
  }, 40);
};

const getSelectors = () => {
  return [`color-${color}`, `variant-${variant}`];
};
</script>

<template>
  <input ref="file" type="file" accept="image/*" hidden @change="imageChange" />
  <div
    v-if="!edit"
    class="wrapper"
    :style="[`--aspect: ${aspect}`, `--height: ${height}px`]"
    @touchstart.stop="touchStart"
    @touchend.stop="touchEnd"
  >
    <div
      class="image-wrapper"
      v-for="(file, index) in previewImages"
      :key="`${file}`"
      @click="viewOverflow(index)"
    >
      <NuxtPicture
        :src="file"
        :aspect="aspect"
        :width="height * aspect"
        :color="color"
        :variant="variant"
      />
      <Transition name="fade" mode="out-in" appear>
        <div v-if="controlsVisibility[index]" class="overflow" :key="`${file}`">
          <UiButton
            class="btn"
            label="Изменить"
            leading="heroicons:wrench-screwdriver-solid"
            start
            @mouseup="editImage(index)"
          />
          <div
            class="row"
            v-if="index !== previewImages.length - 1 || index > 0"
          >
            <UiButton
              v-if="index > 0"
              class="btn"
              leading="heroicons:arrow-small-left-solid"
              @click="moveLeft(index)"
            />
            <UiButton
              v-if="index !== previewImages.length - 1"
              class="btn"
              leading="heroicons:arrow-small-right-solid"
              @click="moveRight(index)"
            />
          </div>
          <UiButton
            class="btn"
            label="Удалить"
            leading="heroicons:trash-16-solid"
            start
            @click="deleteImage(index)"
          />
        </div>
      </Transition>
    </div>
    <div
      v-if="model.length < limit"
      class="empty-card"
      :class="getSelectors()"
      @click="addImage"
    >
      <Icon name="heroicons:plus-solid" />
    </div>
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
</template>

<style lang="scss" scoped>
@use "@/assets/mixins";
@use "@/assets/variables";
@use "@/assets/functions";

.wrapper {
  display: inline-flex;
  justify-content: start;
  gap: var(--gap);
  width: 100%;
  height: var(--height);
  overflow: auto;
  &::-webkit-scrollbar {
    display: none;
  }
  scroll-snap-type: x mandatory;
  -webkit-overflow-scrolling: touch;

  .image-wrapper {
    position: relative;
    cursor: pointer;
    scroll-snap-align: start;
    height: var(--height);
    flex-shrink: 0;
    aspect-ratio: var(--aspect);
    border-radius: var(--br);
    overflow: hidden;

    img {
      width: 100%;
      height: 100%;
    }

    .overflow {
      cursor: default;
      position: absolute;
      display: flex;
      flex-direction: column;
      gap: var(--gap);
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      padding: var(--pd);
      overflow: auto;
      transition:
        opacity 110ms,
        background-color 220ms;
      scroll-snap-type: x mandatory;
      -webkit-overflow-scrolling: touch;
      background-color: #00000064;

      .btn {
        flex-shrink: 0;
        scroll-snap-align: start;
      }

      .row {
        gap: var(--gap);
        display: inline-flex;
        .btn {
          flex-shrink: 1;
        }
      }
    }
  }

  .empty-card {
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5em;
    transition: background-color 220ms;
    border-radius: var(--br);
    height: 100%;
    aspect-ratio: var(--aspect);
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

.empty-card {
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
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.22s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
