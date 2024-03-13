<template>
  <v-dialog v-model="isOpened" max-width="800" @update:modelValue="onOpenDialog">
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn v-if="!block" v-bind="activatorProps"> Кнопка </v-btn>
      <v-btn v-else icon="mdi-invoice-edit-outline" v-bind="activatorProps" />
    </template>

    <v-card title="Кнопка">
      <v-card-text>
        <v-form v-model="isValid" validate-on="input" @submit.prevent>
          <v-text-field
            v-model="buttonInfo.title"
            label="Текст кнопки*"
            class="mb-2"
            :rules="[required(buttonInfo.title)]"
          />

          <v-select
            v-model="buttonInfo.btnType"
            label="Тип кнопки"
            :items="btnTypes"
            :rules="[required(buttonInfo.btnType)]"
            @update:modelValue="onBtnTypeUpdate"
          />

          <v-text-field
            v-if="buttonInfo.btnType === 'Переход на экран'"
            v-model="buttonInfo.screenNumber"
            label="Номер экрана*"
            class="mb-2"
            type="number"
            :rules="[required(buttonInfo.screenNumber)]"
          />

          <v-text-field
            v-if="buttonInfo.btnType === 'Ссылка на страницу'"
            v-model="buttonInfo.link"
            label="Ссылка*"
            class="mb-2"
            :rules="[required(buttonInfo.link), isUrl(buttonInfo.link)]"
          />

          <v-file-input
            v-if="buttonInfo.btnType === 'PDF-файл'"
            v-model="buttonInfo.file"
            label="pdf-файл*"
            :rules="[required(buttonInfo.file || buttonInfo.loadedFile)]"
          />
          <div v-if="buttonInfo.loadedFile" class="text-medium-emphasis mb-2 text-body-2">
            Загруженный
            <a target="_blank" :href="`${baseUrl}${buttonInfo.loadedFile}`">файл</a>
          </div>

          <v-checkbox
            v-model="buttonInfo.withBg"
            hide-details
            color="primary"
            label="Кнопка с фоном"
            density="compact"
          />

          <v-checkbox
            v-model="buttonInfo.confirmation"
            hide-details
            label="Требовать подтвержение"
            density="compact"
            color="primary"
          />

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
import { required, isUrl } from '@/utils/validation';
import { BtnType, ButtonBlock, PracticumScreenElement } from '@/types/practicum';
import { usePracticumStore } from '@/store/practicum';
import { cloneFnJSON } from '@vueuse/core';
import { baseUrl } from '@/utils/consts';

const props = defineProps<{
  side: 'right' | 'left';
  screenId: number;
  block?: ButtonBlock;
}>();

const btnTypes = [BtnType.Screen, BtnType.Link, BtnType.File];

const { saveScreenBlock } = usePracticumStore();

const defaultValue: ButtonBlock = {
  id: 0,
  order: 0,
  type: PracticumScreenElement.Button,
  title: '',
  btnType: null,
  screenId: props.screenId,
  screenNumber: undefined,
  link: '',
  file: undefined,
  withBg: true,
  confirmation: false,
  side: props.side
};

const buttonInfo = ref<ButtonBlock>(cloneFnJSON(defaultValue));

const onOpenDialog = (value: boolean) => {
  if (!value) {
    return;
  }

  if (!props.block) {
    buttonInfo.value = cloneFnJSON(defaultValue);
  } else {
    buttonInfo.value = props.block;
  }
};

const onBtnTypeUpdate = () => {
  buttonInfo.value.screenNumber = undefined;
  buttonInfo.value.link = '';
  buttonInfo.value.file = undefined;
};

const isOpened = ref(false);

const isValid = ref(false);
const isLoading = ref(false);

const save = async () => {
  if (!isValid.value) {
    return;
  }

  try {
    isLoading.value = true;

    const res = await saveScreenBlock(buttonInfo.value, props.side);

    isLoading.value = false;
    if (res) {
      isOpened.value = false;
    }
  } finally {
    isLoading.value = false;
  }
};
</script>

<style scoped lang="scss"></style>
