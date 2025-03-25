<script setup>
import Cropper from 'cropperjs';
import 'cropperjs/dist/cropper.css';

const props = defineProps({
  width: Number,
  aspectRatio: Number,
});

const model = defineModel();

const emit = defineEmits(['update']);

const imageSrc = ref(null);
const editImage = ref(false);
const editedImageSrc = ref(null);
const cropper = ref(null);
const fileInput = ref(null);
const image = ref(null);

const getStyle = () => {
  return { maxWidth: props.width + 'px', width: '100%', aspectRatio: props.aspectRatio }
}

watch(
  () => model.value,
  (newImage) => {
    if (newImage) {
      try {
        editedImageSrc.value = URL.createObjectURL(model.value);
      } catch (err) {
        editedImageSrc.value = null;
      }
    } else {
      editedImageSrc.value = null;
    }
  },
  { immediate: true }
);

const imageChange = (event) => {
  const file = event.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = (e) => {
      imageSrc.value = e.target.result;
      editImage.value = true;
      initCropper();
    };
    reader.readAsDataURL(file);
  }
};

const triggerImageChange = () => {
  fileInput.value.click();
};

const initCropper = () => {
  nextTick(() => {
    cropper.value = new Cropper(image.value, {
      aspectRatio: props.aspectRatio,
      viewMode: 1,
      autoCropArea: 0,
    });
  });
};

const getCroppedImage = () => {
  if (cropper.value) {
    const canvas = cropper.value.getCroppedCanvas();
    canvas.toBlob((blob) => {
      editedImageSrc.value = URL.createObjectURL(blob);
      model.value = blob
    }, 'image/png');
  }
  stopCropping()
};

const stopCropping = () => {
  editImage.value = false;
};
</script>

<template>
  <div 
    v-if="!editImage" 
    class="input-wrapper" 
    :style="getStyle()"
  >
    <div class="hover" @mousedown="triggerImageChange"></div>
    <input 
      type="file" 
      ref="fileInput" 
      accept="image/*" 
      @change="imageChange" 
    />
    <NuxtImg 
      :style="getStyle()"
      :src="editedImageSrc" 
      alt=""
    />
  </div>
  <div v-if="editImage" class="cropper-container">
    <img 
      ref="image" 
      :src="imageSrc" 
    />
  </div>
  <div v-if="editImage" class="button-row hide-on-mobile">
    <div class="w100"></div>
    <UiDefaultButton @mousedown="stopCropping" caption="Отмена"/>
    <UiDefaultButton @mousedown="getCroppedImage" caption="Продолжить"/>
  </div>
</template>

<style lang="scss" scoped>
* {
  user-select: none;
}
.input-wrapper {
  background-color: var(--color-background-8);
  position: relative;
  border-radius: var(--input-borrad);
  overflow: hidden;

  input {
    display: none;  
  }

  .hover {
    width: 100%;
    height: 100%;
    cursor: pointer;
    position: absolute;
    top: 0;
    left: 0;
    background: rgba(0, 0, 0, 0);
    box-shadow: inset 0 0 0 1px var(--color-text-0);
    border-radius: var(--input-borrad);
    
    transition: 
      opacity 0.2s, 
      background 0.2s, 
      box-shadow 0.2s;

    &:hover, &:active {
      box-shadow: inset 0 0 0 1px var(--color-primary-text-0);
    }
  }
}

img {
  border: unset;
  outline: unset;

  background: url();
  border-radius: var(--input-borrad);
}

.cropper-container {
  width: 100%;
  height: 350px;
  border-radius: var(--input-borrad);
}

.button-row {
  margin-top: 5px;
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  gap: var(--row-gap-2);
  .w100 {
    width: 100%;
  }
  .button {
    flex-shrink: 0;
    width: 180px;
  }
  &.hide-on-desktop {
    .button {
      flex-shrink: 1;
      width: 100%;
    }
  }
}
</style>
