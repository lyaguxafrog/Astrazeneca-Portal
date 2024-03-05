<template>
  <v-container class="ma-0 pt-3 pb-3">
    <v-btn class="bg-blue mb-5" to="/practicum/0"> Создать практикум </v-btn>

    <SlickList axis="y" v-model:list="practicumList" useDragHandle>
      <SlickItem v-for="(practicum, index) in practicumList" :key="practicum.id" :index="index">
        <div class="pt-2 pb-2">
          <v-card>
            <template v-slot:title>
              <div class="d-flex">
                {{ practicum.title }}
                <v-spacer />
                <DragHandle class="cursor-grab">
                  <v-icon icon="mdi-menu" />
                </DragHandle>
              </div>
            </template>
            <div class="d-flex justify-lg-space-between pa-4 pt-0 pb-2">
              <div class="mr-4 text-body-2 text-grey-darken-1">
                <b>23.06.2020</b>
                <p>Дата редактирования</p>
              </div>
              <div class="d-flex">
                <v-btn
                  icon="mdi-invoice-edit-outline"
                  class="mr-2"
                  :to="`/practicum/${practicum.id}`"
                />
                <v-btn icon="mdi-delete-empty" class="bg-red" />
              </div>
            </div>
          </v-card>
        </div>
      </SlickItem>
    </SlickList>
  </v-container>
</template>

<script setup lang="ts">
import { SlickList, SlickItem, DragHandle } from 'vue-slicksort';

const practicumList = [
  {
    id: 1,
    title: 'Название практикума'
  },
  {
    id: 2,
    title: 'Название практикума2'
  }
];
</script>

<style scoped lang="scss"></style>
