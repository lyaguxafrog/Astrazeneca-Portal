<template>
  <v-container class="ma-0 pt-3 pb-3">
    <div class="v-col-5">
      <Title> Создание экрана №1 </Title>
      <v-form v-model="isValid" validate-on="input" @submit.prevent="onValidate">
        <TextEditor
          v-model="screen.literature"
          title="Список литературы*"
          :validated="isDirty"
          :rules="[required(screen.literature)]"
        />
        <TextEditor
          v-model="screen.literatureDescription"
          title="Расшифровка для списка литературы"
          :validated="isDirty"
          :rules="[required(screen.literatureDescription)]"
        />
        <TextEditor
          v-model="screen.description"
          title="Расшифровка для страницы"
          :validated="isDirty"
          :rules="[required(screen.description)]"
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
              <v-btn v-bind="props" icon="mdi-plus" density="comfortable" :disabled="!screen.id" />
            </template>

            <v-card title="Добавить блок слева">
              <div class="d-flex ga-2 pa-3 pb-4">
                <ButtonBlock />
                <TextBlock />
                <ImageBlock />
                <DropdownBlock />
              </div>
            </v-card>
          </v-bottom-sheet>
        </div>

        <v-card
          v-for="element in screen.leftElements"
          :key="element.id"
          class="mb-3 pb-2"
          prepend-icon="mdi-invoice-list-outline"
          elevation="6"
        >
          <template v-slot:title> {{ element.type }} </template>

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
              <v-btn v-bind="props" icon="mdi-plus" density="comfortable" :disabled="!screen.id" />
            </template>

            <v-card title="Добавить блок справа">
              <div class="d-flex ga-2 pa-3 pb-4">
                <ButtonBlock />
                <TextBlock />
                <ImageBlock />
                <DropdownBlock />
              </div>
            </v-card>
          </v-bottom-sheet>
        </div>

        <v-card
          v-for="element in screen.rightElements"
          :key="element.id"
          class="mb-3 pb-2"
          prepend-icon="mdi-invoice-list-outline"
          elevation="6"
        >
          <template v-slot:title> {{ element.type }} </template>

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
import { ScreenInfo } from '@/types/practicum';
import TextEditor from '@/components/ui/text-editor.vue';
import Title from '@/components/helpers/title.vue';
import ButtonBlock from '@/components/practicum/button-block.vue';
import TextBlock from '@/components/practicum/text-block.vue';
import ImageBlock from '@/components/practicum/image-block.vue';
import DropdownBlock from '@/components/practicum/dropdown-block.vue';

const screen = ref<ScreenInfo>({
  id: 0,
  literature: '',
  literatureDescription: '',
  description: '',
  leftElements: [],
  rightElements: []
});

const { editablePracticum: practicum, saveScreen } = usePracticumStore();

const isDirty = ref(false);
const isValid = ref(false);
const onValidate = () => {
  isDirty.value = true;

  setTimeout(() => {
    if (!isValid.value) {
      return;
    }

    saveScreen(screen.value);
  });
};
</script>

<style scoped lang="scss"></style>
