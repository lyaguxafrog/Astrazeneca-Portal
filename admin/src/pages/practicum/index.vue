<template>
  <v-container class="ma-0 pt-3 pb-3">
    <v-btn class="bg-blue mb-5" to="/practicum/0"> Создать практикум </v-btn>

    <div
      v-for="practicum in practicums"
      :key="practicum.id"
      class="pt-2 pb-2 wrapper"
      :class="{ loading: isLoading }"
    >
      <v-card>
        <template v-slot:title>
          <div class="d-flex">
            {{ practicum.title }}
          </div>
        </template>
        <div class="d-flex justify-lg-space-between pa-4 pt-0 pb-2">
          <div></div>
          <!--              <div class="mr-4 text-body-2 text-grey-darken-1">
            <b>DD.MM.YYYY</b>
            <p>Дата редактирования</p>
          </div>-->
          <div class="d-flex">
            <OrderPicker
              :value="practicum.priority"
              @update="(order) => updateOrder(practicum.id, order)"
            />
            <v-btn
              icon="mdi-invoice-edit-outline"
              class="mr-2"
              :to="`/practicum/${practicum.id}`"
            />
            <v-btn
              icon="mdi-delete-empty"
              class="bg-red"
              :loading="practicum.id === deletingPracticumId"
              @click="remove(practicum.id)"
            />
          </div>
        </div>
      </v-card>
    </div>
  </v-container>
</template>

<script setup lang="ts">
import { usePracticumStore } from '@/store/practicum';
import { onMounted, ref } from 'vue';
import OrderPicker from '@/components/ui/order-picker.vue';

const { practicums, deletePracticum, getPracticums, savePracticumRequest } = usePracticumStore();

const deletingPracticumId = ref();
const remove = async (id: number) => {
  deletingPracticumId.value = id;
  await deletePracticum(id);
  deletingPracticumId.value = undefined;
};

onMounted(() => {
  getPracticums();
});

const isLoading = ref(false);

const updateOrder = async (id: number, order: number) => {
  const practicum = practicums.value.find((p) => p.id === id);

  if (practicum) {
    isLoading.value = true;
    practicum.priority = order;

    await savePracticumRequest(practicum);
    await getPracticums();
    isLoading.value = false;
  }
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
</style>
