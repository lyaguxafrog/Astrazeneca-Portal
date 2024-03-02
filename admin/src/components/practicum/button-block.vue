<template>
  <v-dialog v-model="isOpened" max-width="800">
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn v-bind="activatorProps"> Кнопка </v-btn>
    </template>

    <v-card title="Кнопка">
      <v-card-text>
        <v-form validate-on="input" @submit.prevent>
          <v-text-field
            label="Текст кнопки*"
            class="mb-2"
            variant="solo-filled"
            density="comfortable"
            :rules="[required()]"
          />

          <v-select
            v-model="btnType"
            label="Тип кнопки"
            :items="['Переход на экран', 'Ссылка на страницу', 'PDF-файл']"
          />

          <v-card-actions>
            <v-btn text="Сохранить" type="submit" @click="save" color="blue"></v-btn>
          </v-card-actions>
        </v-form>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { required } from '@/utils/validation';

const btnType = ref('');

const isOpened = ref(false);

const save = () => {
  isOpened.value = false;
};
</script>

<style scoped lang="scss"></style>
