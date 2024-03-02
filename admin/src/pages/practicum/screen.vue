<template>
  <v-container class="ma-0 pt-3 pb-3">
    <div class="v-col-5">
      <Title> Создание экрана №1 </Title>
      <v-form validate-on="input" @submit.prevent="onValidate">
        <TextEditor
          v-model="practicum.screens[0].literature"
          title="Список литературы*"
          :validated="isDirty"
          :rules="[required(practicum.screens[0].literature)]"
        />
        <TextEditor
          v-model="practicum.screens[0].literatureDescription"
          title="Расшифровка для списка литературы"
          :validated="isDirty"
          :rules="[required(practicum.screens[0].literatureDescription)]"
        />
        <TextEditor
          v-model="practicum.screens[0].description"
          title="Расшифровка для страницы"
          :validated="isDirty"
          :rules="[required(practicum.screens[0].description)]"
        />
        <v-btn type="submit"> Сохранить </v-btn>
      </v-form>

      <Title class="mt-6"> Компоненты </Title>
    </div>
    <div class="d-flex">
      <div class="v-col-6 pt-0">
        <div class="d-flex align-center mb-3">
          <h4 class="mr-3">Слева</h4>
          <v-bottom-sheet>
            <template v-slot:activator="{ props }">
              <v-btn v-bind="props" icon="mdi-plus" density="comfortable"></v-btn>
            </template>

            <v-card title="Добавить блок слева">
              <div class="d-flex ga-2 pa-3">
                <ButtonBlock />
                <v-btn> Текст </v-btn>
                <v-btn> Изображение </v-btn>
                <v-btn> Выпадающий список </v-btn>
              </div>
            </v-card>
          </v-bottom-sheet>
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
      </div>
      <div class="v-col-6 pt-0">
        <div class="d-flex align-center mb-3">
          <h4 class="mr-3">Справа</h4>
          <v-bottom-sheet>
            <template v-slot:activator="{ props }">
              <v-btn v-bind="props" icon="mdi-plus" density="comfortable"></v-btn>
            </template>

            <v-card title="Добавить блок справа">
              <div class="d-flex ga-2 pa-3">
                <v-btn> Кнопка </v-btn>
                <v-btn> Текст </v-btn>
                <v-btn> Изображение </v-btn>
                <v-btn> Выпадающий список </v-btn>
              </div>
            </v-card>
          </v-bottom-sheet>
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
      </div>
    </div>
  </v-container>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { required } from '@/utils/validation';
import { usePracticumStore } from '@/store/practicum';
import TextEditor from '@/components/ui/text-editor.vue';
import Title from '@/components/helpers/title.vue';
import ButtonBlock from '@/components/practicum/button-block.vue';

const { editablePracticum: practicum } = usePracticumStore();

const isDirty = ref(false);
const onValidate = () => {
  isDirty.value = true;
};
</script>

<style scoped lang="scss"></style>
