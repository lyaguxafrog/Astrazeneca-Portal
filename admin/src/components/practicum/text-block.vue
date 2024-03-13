<template>
  <v-dialog v-model="isOpened" max-width="800" @update:modelValue="onOpenDialog">
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn v-if="!block" v-bind="activatorProps"> Текст </v-btn>
      <v-btn v-else icon="mdi-invoice-edit-outline" v-bind="activatorProps" />
    </template>

    <v-card title="Текстовый блок">
      <v-card-text>
        <v-form v-model="isValid" validate-on="input" @submit.prevent="save">
          <TextEditor
            v-model="textBlock.text"
            :validated="isDirty"
            :rules="[required(textBlock.text)]"
            title="Текст*"
          />

          <v-btn text="Сохранить" class="mt-4" type="submit" :loading="isLoading" color="blue" />
        </v-form>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref, defineProps } from 'vue';
import TextEditor from '@/components/ui/text-editor.vue';
import { usePracticumStore } from '@/store/practicum';
import { required } from '@/utils/validation';
import { ButtonBlock, PracticumScreenElement, TextBlock } from '@/types/practicum';
import { cloneFnJSON } from '@vueuse/core/index';

const props = defineProps<{
  side: 'right' | 'left';
  screenId?: number;
  block?: TextBlock;
}>();

const { saveScreenBlock } = usePracticumStore();

const defaultValue: TextBlock = {
  id: 0,
  order: 0,
  side: props.side,
  type: PracticumScreenElement.Text,
  text: '',
  screenId: props.screenId
};

const textBlock = ref<TextBlock>(cloneFnJSON(defaultValue));

const onOpenDialog = (value: boolean) => {
  if (!value) {
    return;
  }

  if (!props.block) {
    textBlock.value = cloneFnJSON(defaultValue);
  } else {
    textBlock.value = props.block;
  }
};

const isDirty = ref(false);

const isOpened = ref(false);
const isLoading = ref(false);
const isValid = ref(false);

const save = () => {
  isDirty.value = true;

  setTimeout(async () => {
    if (!isValid.value) {
      return;
    }

    isLoading.value = true;

    await saveScreenBlock(textBlock.value, props.side);

    isLoading.value = false;
    isOpened.value = false;
  });
};
</script>

<style scoped lang="scss"></style>
