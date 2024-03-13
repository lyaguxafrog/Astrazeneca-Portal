<template>
  <v-dialog v-model="isOpened" max-width="800">
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn v-bind="activatorProps"> Изображение </v-btn>
    </template>

    <v-card title="Блок с изображением">
      <v-card-text>
        <v-form v-model="isValid" validate-on="input" @submit.prevent>
          <v-file-input
            v-model="block.image"
            label="Изображение*"
            class="mb-2"
            :rules="[required(block.image)]"
          />

          <v-btn
            text="Сохранить"
            class="mt-4"
            type="submit"
            :loading="isLoading"
            @click="save"
            color="blue"
          ></v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { defineProps, ref } from 'vue';
import { required } from '@/utils/validation';
import { usePracticumStore } from '@/store/practicum';
import { ImageBlock, PracticumScreenElement } from '@/types/practicum';

const props = defineProps<{
  side: 'right' | 'left';
  screenId: number;
}>();

const { saveScreenBlock } = usePracticumStore();

const isOpened = ref(false);
const isValid = ref(false);
const isLoading = ref(false);

const block = ref<ImageBlock>({
  id: 0,
  type: PracticumScreenElement.Image,
  image: undefined,
  screenId: props.screenId,
  side: props.side,
  order: 0
});

const save = async () => {
  if (!isValid) {
    return;
  }

  isLoading.value = true;

  await saveScreenBlock(block.value, props.side);

  isLoading.value = false;
  isOpened.value = false;
};
</script>

<style scoped lang="scss"></style>
