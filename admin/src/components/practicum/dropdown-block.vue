<template>
  <v-dialog v-model="isOpened" max-width="800">
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn v-bind="activatorProps"> Выбпадающий список </v-btn>
    </template>

    <v-card title="Блок с выпадающим списком">
      <v-card-text>
        <v-form validate-on="input" @submit.prevent="save">
          <v-card v-for="item in dropdown" :key="item.id" class="mb-2">
            <v-card-text>
              <v-text-field
                v-model="item.title"
                label="Заголовок пункта*"
                class="mb-2"
                :rules="[required(item.title)]"
              />
              <TextEditor
                v-model="item.text"
                title="Описание*"
                :validated="isDirty"
                :rules="[required(item.text)]"
              />
            </v-card-text>
          </v-card>

          <v-btn icon="mdi-plus" density="comfortable" class="d-block mt-2" @click="addItem" />

          <v-btn text="Сохранить" class="mt-4" type="submit" @click="save" color="blue"></v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { required } from '@/utils/validation';
import { DropdownBlock, PracticumScreenElement } from '@/types/practicum';
import TextEditor from '@/components/ui/text-editor.vue';
import { getUiId } from '@/utils/functions';

const defaultItem = () =>
  ({
    id: getUiId(),
    type: PracticumScreenElement.Dropdown,
    title: '',
    text: ''
  } as DropdownBlock);

const dropdown = ref<DropdownBlock[]>([defaultItem()]);

const addItem = () => {
  dropdown.value.push(defaultItem());
};

const isOpened = ref(false);
const isDirty = ref(false);

const save = () => {
  isDirty.value = true;
  isOpened.value = true;
};
</script>

<style scoped lang="scss"></style>
