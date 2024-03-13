<template>
  <div class="v-col-6 pt-0">
    <div class="d-flex align-center mb-3">
      <h4 class="mr-3">{{ side === 'left' ? 'Слева' : 'Справа' }}</h4>
      <v-bottom-sheet>
        <template v-slot:activator="{ props }">
          <v-btn v-bind="props" icon="mdi-plus" density="comfortable" :disabled="!screenId" />
        </template>

        <v-card title="Добавить блок слева">
          <div class="d-flex ga-2 pa-3 pb-4">
            <ButtonBlock :side="side" :screenId="screenId" />
            <TextBlock :side="side" :screenId="screenId" />
            <ImageBlock :side="side" :screenId="screenId" />
            <DropdownBlock :side="side" :screenId="screenId" />
          </div>
        </v-card>
      </v-bottom-sheet>
    </div>

    <v-card
      v-for="element in elements"
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
            : element.type === PracticumScreenElement.Text
            ? 'Текстовый блок'
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
          <OrderPicker
            :value="element.order"
            @update="(order) => updateOrder(element.id, order, side)"
          />
          <v-btn icon="mdi-invoice-edit-outline" class="mr-2" :to="`/practicum/0/screen/0`" />
          <v-btn icon="mdi-delete-empty" class="bg-red" />
        </div>
      </div>
    </v-card>
  </div>
</template>

<script setup lang="ts">
import { PracticumScreenElement, ScreenBlock, Side } from '@/types/practicum';
import OrderPicker from '@/components/ui/order-picker.vue';
import TextBlock from '@/components/practicum/text-block.vue';
import ButtonBlock from '@/components/practicum/button-block.vue';
import ImageBlock from '@/components/practicum/image-block.vue';
import DropdownBlock from '@/components/practicum/dropdown-block.vue';

const props = defineProps<{
  elements: ScreenBlock[];
  side: Side;
  screenId: number;
}>();

const emit = defineEmits<{
  (event: 'updateOrder', id: number, order: number, side: Side): void;
}>();

const updateOrder = (id: number, order: number, side: Side) => {
  emit('updateOrder', id, order, side);
};
</script>

<style scoped lang="scss"></style>
