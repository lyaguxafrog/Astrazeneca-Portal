<template>
  <v-dialog v-model="isOpened" max-width="800">
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn v-bind="activatorProps"> Изображение </v-btn>
    </template>

    <v-card title="Блок с изображением">
      <v-card-text>
        <v-form validate-on="input" @submit.prevent="save">
          <v-file-input
            v-model="image"
            label="Изображение*"
            class="mb-2"
            :rules="[required(image)]"
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

const isOpened = ref(false);

const image = ref();

const save = () => {
  isOpened.value = true;
};
</script>

<style scoped lang="scss"></style>
