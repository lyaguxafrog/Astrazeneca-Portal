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
        <v-file-input
          v-model="practicum.image"
          label="Изображение*"
          class="mb-2"
          variant="solo-filled"
        />

        <TextEditor
          v-model="practicum.description"
          :validated="isDirty"
          :rules="[required(practicum.description)]"
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

    <v-card class="mb-3 pb-2" prepend-icon="mdi-invoice-list-outline" elevation="6">
      <template v-slot:title> Экран №1 </template>
      <div class="d-flex justify-lg-space-between pa-4 pt-0 pb-2">
        <div class="mr-4 text-body-2 text-grey-darken-1">
          <b>23.06.2020</b>
          <p>Дата редактирования</p>
        </div>
        <div class="d-flex">
          <v-btn icon="mdi-invoice-edit-outline" class="mr-2" :to="`/practicum/0/screen/0`" />
          <v-btn icon="mdi-delete-empty" class="bg-red" />
        </div>
      </div>
    </v-card>
    <v-card class="mb-3" prepend-icon="mdi-invoice-list-outline" elevation="6">
      <template v-slot:title> Экран №1 </template>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { required } from '@/utils/validation';
import { usePracticumStore } from '@/store/practicum';
import TextEditor from '@/components/ui/text-editor.vue';
import Title from '@/components/helpers/title.vue';

const { editablePracticum: practicum } = usePracticumStore();

const isDirty = ref(false);
const onValidate = () => {
  isDirty.value = true;
};
</script>

<style scoped lang="scss"></style>
