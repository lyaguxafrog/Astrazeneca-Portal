<template>
  <v-container v-if="isLoaded" class="ma-0 pt-3 pb-3 pa-0 pa-xl-3">
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
      <ScreenBlocks
        :elements="screen.leftElements"
        :side="'left'"
        :screenId="screen.id"
        @updateOrder="updateOrder"
      />

      <ScreenBlocks
        :elements="screen.rightElements"
        :side="'right'"
        :screenId="screen.id"
        @updateOrder="updateOrder"
      />
    </div>
  </v-container>
</template>

<script setup lang="ts">
import { onMounted, ref, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { required } from '@/utils/validation';
import { usePracticumStore } from '@/store/practicum';
import { ScreenInfo, Side } from '@/types/practicum';
import TextEditor from '@/components/ui/text-editor.vue';
import Title from '@/components/helpers/title.vue';
import ScreenBlocks from '@/components/practicum/screen-blocks.vue';

const $router = useRouter();
const $route = useRoute();

const {
  editablePracticum: practicum,
  saveScreen,
  init,
  isLoaded,
  getPracticum
} = usePracticumStore();

const screen = ref<ScreenInfo>({
  id: 0,
  literature: '',
  literatureDescription: '',
  description: '',
  order: practicum.value.screens.length + 1,
  leftElements: [],
  rightElements: []
});

watch(
  [isLoaded, practicum],
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
    immediate: true,
    deep: true
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
        await $router.replace({ params: { screenId: screen.value.id } });
      }
    }

    isLoading.value = false;
  });
};

const updateOrder = async (id: number, order: number, side: Side) => {
  const collection = side === 'left' ? screen.value.leftElements : screen.value.rightElements;

  const el = collection.find((e) => e.id === id);

  if (el) {
    el.order = order;
  }

  await saveScreen(screen.value);
  await getPracticum(practicum.value.id);
};

onMounted(() => {
  init();
});
</script>

<style scoped lang="scss"></style>
