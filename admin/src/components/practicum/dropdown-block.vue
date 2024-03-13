<template>
  <v-dialog v-model="isOpened" max-width="800">
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn v-bind="activatorProps"> Выбпадающий список </v-btn>
    </template>

    <v-card title="Блок с выпадающим списком">
      <v-card-text>
        <v-form v-model="isValid" validate-on="input" @submit.prevent>
          <v-card v-for="item in dropdown.items" :key="item.id" class="mb-2">
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
import { DropdownBlock, PracticumScreenElement } from '@/types/practicum';
import TextEditor from '@/components/ui/text-editor.vue';
import { usePracticumStore } from '@/store/practicum';

const { saveScreenBlock } = usePracticumStore();

const props = defineProps<{
  side: 'right' | 'left';
  screenId?: number;
}>();

const defaultItem = () => ({
  id: 0,
  title: '',
  text: ''
});

const dropdown = ref<DropdownBlock>({
  id: 0,
  order: 50,
  type: PracticumScreenElement.Dropdown,
  screenId: props.screenId,
  side: props.side,
  items: [defaultItem()]
});

const addItem = () => {
  dropdown.value.items.push(defaultItem());
};

const isOpened = ref(false);
const isDirty = ref(false);
const isValid = ref(false);
const isLoading = ref(false);
const save = async () => {
  isDirty.value = true;

  setTimeout(async () => {
    if (!isValid.value) {
      return;
    }

    isLoading.value = true;

    await saveScreenBlock(dropdown.value, props.side);

    isLoading.value = false;
    isOpened.value = false;
  });
};
</script>

<style scoped lang="scss"></style>
