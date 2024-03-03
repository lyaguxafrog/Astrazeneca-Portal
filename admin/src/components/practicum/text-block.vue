<template>
  <v-dialog v-model="isOpened" max-width="800">
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn v-bind="activatorProps"> Текст </v-btn>
    </template>

    <v-card title="Текстовый блок">
      <v-card-text>
        <v-form validate-on="input" @submit.prevent="save">
          <TextEditor
            v-model="text"
            :validated="isDirty"
            :rules="[required(text)]"
            title="Текст*"
          />

          <v-btn text="Сохранить" class="mt-4" type="submit" @click="save" color="blue"></v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import TextEditor from '@/components/ui/text-editor.vue';
import { required } from '@/utils/validation';

const text = ref('');

const isDirty = ref(false);

const isOpened = ref(false);

const save = () => {
  isDirty.value = true;
  isOpened.value = true;
};
</script>

<style scoped lang="scss"></style>
