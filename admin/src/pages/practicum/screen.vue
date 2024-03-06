<template>
  <v-container class="ma-0 pt-3 pb-3 pa-0 pa-xl-3">
    <v-breadcrumbs
      class="pa-0 pl-2 text-caption"
      :items="[
        {
          title: 'Список практикумов',
          disabled: false,
          to: '/practicum'
        },
        {
          title: 'Редактирование практикума',
          disabled: false,
          to: `/practicum/${practicum.id}`
        },
        {
          title: 'Редактирование экрана',
          disabled: true
        }
      ]"
    >
    </v-breadcrumbs>

    <div class="v-col-12 v-col-xl-5">
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
        <v-btn type="submit" :loading="isLoading"> Сохранить </v-btn>
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
                <ButtonBlock side="left" :screenId="screen.id" />
                <TextBlock side="left" :screenId="screen.id" />
                <ImageBlock side="left" :screenId="screen.id" />
                <DropdownBlock side="left" :screenId="screen.id" />
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
          <template v-slot:title>
            {{
              element.type === PracticumScreenElement.Button
                ? 'Кнопка'
                : element.type === PracticumScreenElement.Image
                ? 'Изображение'
                : 'Выпадающий список'
            }}
          </template>

          <div class="d-flex justify-lg-space-between pa-4 pt-0 pb-2">
            <div></div>
            <!--            <div class="mr-4 text-body-2 text-grey-darken-1">
              <b>DD.MM.YYYY</b>
              <p>Дата редактирования</p>
            </div>-->
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
                <ButtonBlock side="right" :screenId="screen.id" />
                <TextBlock side="right" :screenId="screen.id" />
                <ImageBlock side="right" :screenId="screen.id" />
                <DropdownBlock side="right" :screenId="screen.id" />
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
            <div></div>
            <!--            <div class="mr-4 text-body-2 text-grey-darken-1">
              <b>DD.MM.YYYY</b>
              <p>Дата редактирования</p>
            </div>-->
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
import { onMounted, ref, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { required } from '@/utils/validation';
import { usePracticumStore } from '@/store/practicum';
import { PracticumScreenElement, ScreenInfo } from '@/types/practicum';
import TextEditor from '@/components/ui/text-editor.vue';
import Title from '@/components/helpers/title.vue';
import ButtonBlock from '@/components/practicum/button-block.vue';
import TextBlock from '@/components/practicum/text-block.vue';
import ImageBlock from '@/components/practicum/image-block.vue';
import DropdownBlock from '@/components/practicum/dropdown-block.vue';

const $router = useRouter();
const $route = useRoute();

const screen = ref<ScreenInfo>({
  id: 0,
  literature: '',
  literatureDescription: '',
  description: '',
  leftElements: [],
  rightElements: []
});

const { editablePracticum: practicum, saveScreen, init, isLoaded } = usePracticumStore();

watch(
  isLoaded,
  () => {
    const id = +$route.params.screenId;

    if (!id) {
      return;
    }

    const existScreen = practicum.value.screens.find((s) => s.id === id);
    if (existScreen) {
      screen.value = existScreen;
    }
  },
  {
    immediate: true
  }
);

const isDirty = ref(false);
const isValid = ref(false);
const isLoading = ref(false);
const onValidate = () => {
  isDirty.value = true;

  setTimeout(async () => {
    if (!isValid.value) {
      return;
    }
    isLoading.value = true;

    const res = await saveScreen(screen.value);

    if (res) {
      const lastScreen = res.screens.at(-1);

      if (lastScreen) {
        screen.value.id = lastScreen.id;
        $router.replace({ params: { screenId: screen.value.id } });
      }
    }

    isLoading.value = false;
  });
};

onMounted(() => {
  init();
});
</script>

<style scoped lang="scss"></style>
