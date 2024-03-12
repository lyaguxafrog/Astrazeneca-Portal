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
          disabled: true
        }
      ]"
    />

    <div class="v-col-12 v-col-xl-5">
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
          :class="{ 'mb-2': !practicum.loadedImage }"
          :rules="[required(practicum.image || practicum.loadedImage)]"
        />
        <div v-if="practicum.loadedImage" class="text-medium-emphasis mb-2 text-body-2">
          Загруженное
          <a target="_blank" :href="`${baseUrl}${practicum.loadedImage}`">изображение</a>
        </div>

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
          item-title="name"
          item-value="id"
          :items="specialities"
          :rules="[required(practicum.speciality)]"
          multiple
        />

        <v-btn type="submit" class="mt-2" :loading="isLoading"> Сохранить </v-btn>
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

    <SlickList axis="y" v-model:list="practicum.screens" useDragHandle>
      <SlickItem v-for="(screen, index) in practicum.screens" :key="screen.id" :index="index">
        <div class="pt-2 pb-2">
          <v-card class="pb-2" prepend-icon="mdi-invoice-list-outline" elevation="6">
            <template v-slot:title>
              <div class="d-flex">
                Экран №{{ index + 1 }}
                <v-spacer />
                <DragHandle class="cursor-grab">
                  <v-icon icon="mdi-menu" />
                </DragHandle>
              </div>
            </template>
            <div class="d-flex justify-lg-space-between pa-4 pt-0 pb-2">
              <div></div>
              <!--              <div class="mr-4 text-body-2 text-grey-darken-1">
                <b>DD.MM.YYYY</b>
                <p>Дата редактирования</p>
              </div>-->
              <div class="d-flex">
                <v-btn
                  icon="mdi-invoice-edit-outline"
                  class="mr-2"
                  :to="`/practicum/${practicum.id}/screen/${screen.id}`"
                />
                <v-btn
                  icon="mdi-delete-empty"
                  class="bg-red"
                  :loading="!!screen.removing"
                  @click="removeScreen(screen.id)"
                />
              </div>
            </div>
          </v-card>
        </div>
      </SlickItem>
    </SlickList>
  </v-container>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import { SlickList, SlickItem, DragHandle } from 'vue-slicksort';
import { required } from '@/utils/validation';
import { usePracticumStore } from '@/store/practicum';
import { useSpecialitiesStore } from '@/store/specialities';
import TextEditor from '@/components/ui/text-editor.vue';
import Title from '@/components/helpers/title.vue';
import { baseUrl } from '@/utils/consts';

const $router = useRouter();

const {
  editablePracticum: practicum,
  savePracticum,
  removeScreen: remove,
  init,
  isLoaded
} = usePracticumStore();
const { specialities } = useSpecialitiesStore();

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

    try {
      const res = await savePracticum();

      if (res && res.id) {
        await $router.replace({ params: { id: res.id } });
      }
    } finally {
      isLoading.value = false;
    }
  });
};

const removeScreen = async (id: number) => {
  await remove(id);
};

onMounted(() => {
  init();
});
</script>

<style scoped lang="scss"></style>
