<template>
  <v-container class="ma-0 pt-3 pb-3">
    <div class="v-col-5">
      <Title>Создание практикума</Title>
      <v-form v-model="isValid" validate-on="input" @submit.prevent="onValidate">
        <v-text-field
          v-model="practicum.title"
          label="Название практикума*"
          class="mb-2"
          :rules="[required(practicum.title)]"
        />
        <v-file-input
          v-model="practicum.image"
          label="Изображение*"
          class="mb-2"
          :rules="[required(practicum.image)]"
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
          :rules="[required(practicum.speciality)]"
          multiple
        />

        <v-btn type="submit" class="mt-2"> Сохранить </v-btn>
      </v-form>

      <Title class="mt-5">Экраны</Title>

      <v-btn
        type="submit"
        class="bg-blue"
        :disabled="practicum.id === 0"
        :to="`/practicum/${practicum.id}/screen/0`"
      >
        Добавить экран
      </v-btn>
    </div>

    <v-card
      v-for="(screen, index) in practicum.screens"
      :key="screen.id"
      class="mb-3 pb-2"
      prepend-icon="mdi-invoice-list-outline"
      elevation="6"
    >
      <template v-slot:title> Экран №{{ index + 1 }} </template>
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
  </v-container>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { required } from '@/utils/validation';
import { usePracticumStore } from '@/store/practicum';
import TextEditor from '@/components/ui/text-editor.vue';
import Title from '@/components/helpers/title.vue';

const $router = useRouter();

const { editablePracticum: practicum, savePracticum } = usePracticumStore();

const isDirty = ref(false);
const isValid = ref(false);
const onValidate = () => {
  isDirty.value = true;

  if (!isValid.value) {
    return;
  }

  savePracticum();

  $router.replace({ params: { id: practicum.value.id } });
};
</script>

<style scoped lang="scss"></style>
