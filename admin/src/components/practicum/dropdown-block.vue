<template>
  <v-dialog
    v-model="isOpened"
    class="dropdown-container"
    max-width="800"
    @update:modelValue="onOpenDialog"
  >
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn v-if="!block" v-bind="activatorProps"> Выбпадающий список </v-btn>
      <v-btn v-else icon="mdi-invoice-edit-outline" v-bind="activatorProps" />
    </template>

    <v-card title="Блок с выпадающим списком">
      <v-card-text>
        <v-form
          v-model="isValid"
          validate-on="input"
          @submit.prevent
          class="wrapper"
          :class="{ loading: isLoading }"
        >
          <SlickList
            axis="y"
            v-model:list="dropdown.items"
            appendTo=".dropdown-container"
            useDragHandle
            class="list"
            @update:list="onSort"
          >
            <SlickItem v-for="(item, index) in dropdown.items" :key="item.id" :index="index">
              <v-card class="mb-2">
                <DragHandle>
                  <v-icon icon="mdi-menu" density="compact" class="cursor-grab ml-1 mt-1" />
                </DragHandle>
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

                  <div class="d-flex">
                    <v-spacer />
                    <v-btn
                      icon="mdi-delete-empty"
                      class="bg-red"
                      density="compact"
                      :loading="deletingItemId === item.id"
                      @click="deleteItem(item)"
                    />
                  </div>
                </v-card-text>
              </v-card>
            </SlickItem>
          </SlickList>

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
import { DropdownBlock, DropdownItem, PracticumScreenElement } from '@/types/practicum';
import { SlickList, SlickItem, DragHandle } from 'vue-slicksort';
import TextEditor from '@/components/ui/text-editor.vue';
import { usePracticumStore } from '@/store/practicum';
import { useRequest } from '@/utils/composables/request';
import { cloneFnJSON } from '@vueuse/core';

const { saveScreenBlock, editablePracticum, getPracticum } = usePracticumStore();
const { del } = useRequest();

const props = defineProps<{
  side: 'right' | 'left';
  screenId?: number;
  block?: DropdownBlock;
}>();

const defaultItem = (order = 0) => ({
  id: 0,
  title: '',
  text: '',
  order
});

const defaultValue: DropdownBlock = {
  id: 0,
  order: 0,
  type: PracticumScreenElement.Dropdown,
  screenId: props.screenId,
  side: props.side,
  items: [defaultItem()]
};

const dropdown = ref<DropdownBlock>(cloneFnJSON(defaultValue));

const deletingItemId = ref();
const deleteItem = async (item: DropdownItem) => {
  if (!props.block) {
    return;
  }

  deletingItemId.value = item.id;

  await del(
    `/practicum/${editablePracticum.value.id}/screen/${props.screenId}/popupblock/${props.block.id}/point/${item.id}/`
  );
  await getPracticum(editablePracticum.value.id);

  dropdown.value.items = dropdown.value.items.filter((i) => i.id !== item.id);

  deletingItemId.value = undefined;
};

const onOpenDialog = (value: boolean) => {
  if (!value) {
    return;
  }

  if (!props.block) {
    dropdown.value = cloneFnJSON(defaultValue);
  } else {
    dropdown.value = props.block;
  }
};
const addItem = () => {
  dropdown.value.items.push(defaultItem(dropdown.value.items.length + 1));
};

const isOpened = ref(false);
const isDirty = ref(false);
const isValid = ref(false);
const isLoading = ref(false);
const save = async (close = true) => {
  isDirty.value = true;

  setTimeout(async () => {
    if (!isValid.value) {
      return;
    }

    isLoading.value = true;

    await saveScreenBlock(dropdown.value, props.side);

    isLoading.value = false;
    if (close) {
      isOpened.value = false;
    }
  });
};

const onSort = () => {
  dropdown.value.items = dropdown.value.items.map((i, index) => ({
    ...i,
    order: index + 1
  }));
};
</script>

<style scoped lang="scss">
.wrapper {
  transition: opacity 0.2s;

  &.loading {
    opacity: 0.5;

    pointer-events: none;
  }
}

.list {
  padding: 2px;
  max-height: 70vh;
  overflow: auto;
}
</style>
