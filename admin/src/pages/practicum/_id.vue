<template>
  <v-container class="ma-0 pt-3 pb-3">
    <div class="v-col-5">
      <Title>Создание практикума</Title>
      <v-form validate-on="input" @submit.prevent="onValidate">
        <v-text-field
          v-model="practicum.title"
          label="Название практикума*"
          variant="solo-filled"
          class="mb-2"
          :rules="[required(practicum.title)]"
        />
        <v-file-input label="Изображение*" class="mb-2" variant="solo-filled" />

        <TextEditor
          v-model="practicum.description"
          :rules="isDirty ? [required(practicum.description)] : []"
          title="Описание*"
        />
        <TextEditor v-model="practicum.patientInfo" title="Краткая информация о пациенте*" />
        <v-select
          v-model="practicum.speciality"
          clearable
          chips
          label="Специальность*"
          :items="['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming']"
          multiple
        />

        <v-btn type="submit"> Сохранить </v-btn>
      </v-form>

      <Title class="mt-5">Экраны</Title>

      <v-btn type="submit" class="bg-blue"> Добавить экран </v-btn>
    </div>
  </v-container>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { required } from '@/utils/validation';
import TextEditor from '@/components/ui/TextEditor.vue';
import Title from '@/components/helpers/title.vue';

const practicum = ref({
  title: '',
  description: '',
  patientInfo:
    '<p><strong style="color: rgb(0, 209, 255);">Имя:</strong></p><p><strong style="color: rgb(0, 209, 255);">Возраст:</strong></p><p><strong style="color: rgb(0, 209, 255);">Образ жизни:</strong></p><p><strong style="color: rgb(0, 209, 255);">Семейный анамнез:</strong></p><p><strong style="color: rgb(0, 209, 255);">Перенесенные заболевания:</strong></p><p><strong style="color: rgb(0, 209, 255);">Оценка состояния:</strong></p><p><strong style="color: rgb(0, 209, 255);">Диагноз:</strong></p>',
  speciality: []
});

const isDirty = ref(false);
const onValidate = () => {
  isDirty.value = true;
};
</script>

<style scoped lang="scss"></style>
