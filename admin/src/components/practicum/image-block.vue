<template>
  <v-dialog v-model="isOpened" max-width="800" @update:modelValue="onOpenDialog">
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn v-if="!block" v-bind="activatorProps"> Изображение </v-btn>
      <v-btn v-else icon="mdi-invoice-edit-outline" v-bind="activatorProps" />
    </template>

    <v-card title="Блок с изображением">
      <v-card-text>
        <v-form v-model="isValid" validate-on="input" @submit.prevent>
          <v-file-input
            v-model="imageBlock.image"
            label="Изображение*"
            :rules="[required(imageBlock.image)]"
          />
          <div v-if="imageBlock.savedImage" class="text-medium-emphasis mb-2 text-body-2">
            Загруженное
            <a target="_blank" :href="`${baseUrl}${imageBlock.savedImage}`">изображение</a>
          </div>

          <v-btn
            text="Сохранить"
            class="mt-4"
            type="submit"
            :loading="isLoading"
            @click="save"
            color="blue"
          />
        </v-form>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { defineProps, ref } from 'vue';
import { required } from '@/utils/validation';
import { usePracticumStore } from '@/store/practicum';
import { ButtonBlock, ImageBlock, PracticumScreenElement } from '@/types/practicum';
import { baseUrl } from '@/utils/consts';
import { cloneFnJSON } from '@vueuse/core';

const props = defineProps<{
  side: 'right' | 'left';
  screenId: number;
  block?: ImageBlock;
}>();

const { saveScreenBlock } = usePracticumStore();

const isOpened = ref(false);
const isValid = ref(false);
const isLoading = ref(false);

const defaultValue: ImageBlock = {
  id: 0,
  type: PracticumScreenElement.Image,
  image: undefined,
  screenId: props.screenId,
  side: props.side,
  order: 0
};

const imageBlock = ref<ImageBlock>(cloneFnJSON(defaultValue));

const onOpenDialog = (value: boolean) => {
  if (!value) {
    return;
  }

  if (!props.block) {
    imageBlock.value = cloneFnJSON(defaultValue);
  } else {
    imageBlock.value = props.block;
  }
};
const save = async () => {
  if (!isValid.value) {
    return;
  }

  isLoading.value = true;

  await saveScreenBlock(imageBlock.value, props.side);

  isLoading.value = false;
  isOpened.value = false;
};
</script>

<style scoped lang="scss"></style>
