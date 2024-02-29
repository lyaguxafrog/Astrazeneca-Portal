<template>
  <v-container class="ma-0 pt-3 pb-3">
    <div class="v-col-5">
      <h3 class="mb-4">Создание практикума</h3>
      <v-text-field label="Название практикума*" variant="solo-filled"></v-text-field>
      <v-file-input label="Изображение*" variant="solo-filled"></v-file-input>

      <TextEditor />
    </div>
  </v-container>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import TextEditor from '@/components/TextEditor.vue';

const value = ref('');
</script>

<style scoped lang="scss"></style>
