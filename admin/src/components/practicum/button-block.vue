<template>
  <v-dialog v-model="isOpened" max-width="800">
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn v-bind="activatorProps"> Кнопка </v-btn>
    </template>

    <v-card title="Кнопка">
      <v-card-text>
        <v-form validate-on="input" @submit.prevent>
          <v-text-field
            v-model="buttonInfo.title"
            label="Текст кнопки*"
            class="mb-2"
            :rules="[required(buttonInfo.title)]"
          />

          <v-select
            v-model="buttonInfo.btnType"
            label="Тип кнопки"
            :items="['Переход на экран', 'Ссылка на страницу', 'PDF-файл']"
            @update="onBtnTypeUpdate"
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
            :rules="[required(buttonInfo.link)]"
          />

          <v-file-input
            v-if="buttonInfo.btnType === 'PDF-файл'"
            v-model="buttonInfo.file"
            label="pdf-файл*"
            class="mb-2"
          />

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

          <v-btn text="Сохранить" class="mt-4" type="submit" @click="save" color="blue"></v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { required } from '@/utils/validation';

const buttonInfo = ref({
  title: '',
  btnType: null,
  screenNumber: '',
  link: '',
  file: null,
  withBg: true,
  confirmation: false
});

const onBtnTypeUpdate = () => {
  buttonInfo.value.screenNumber = '';
  buttonInfo.value.link = '';
  buttonInfo.value.file = null;
};

const isOpened = ref(false);

const save = () => {
  isOpened.value = false;
};
</script>

<style scoped lang="scss"></style>
