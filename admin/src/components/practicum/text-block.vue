<template>
  <v-dialog v-model="isOpened" max-width="800">
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn v-bind="activatorProps"> Текст </v-btn>
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
import { PracticumScreenElement, TextBlock } from '@/types/practicum';

const props = defineProps<{
  side: 'right' | 'left';
  screenId?: number;
}>();

const { saveScreenBlock } = usePracticumStore();

const textBlock = ref<TextBlock>({
  id: 0,
  type: PracticumScreenElement.Text,
  text: '',
  screenId: props.screenId
});

const isDirty = ref(false);

const isOpened = ref(false);
const isLoading = ref(false);
const isValid = ref(false);

const save = () => {
  isDirty.value = true;

  setTimeout(async () => {
    console.log(isValid.value);
    console.log(props.side);

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
