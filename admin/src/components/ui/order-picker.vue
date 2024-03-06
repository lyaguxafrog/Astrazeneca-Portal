<template>
  <div class="d-flex align-center ml-2 mr-2">
    <v-btn icon="mdi-menu-up" density="compact" :disabled="inputValue === 1" @click="decrease" />
    <v-text-field
      v-model="inputValue"
      class="ml-1 mr-1 input"
      density="compact"
      hide-details="auto"
      variant="outlined"
      type="number"
      @blur="update"
    />
    <v-btn icon="mdi-menu-down" density="compact" @click="increase" />
  </div>
</template>

<script setup lang="ts">
import { defineProps, defineEmits, ref } from 'vue';

const props = defineProps<{
  value: number;
}>();

const emit = defineEmits<{
  (event: 'update', value: number): void;
}>();

const inputValue = ref(props.value);

const update = () => {
  emit('update', inputValue.value);
};

const increase = () => {
  inputValue.value += 1;
  update();
};
const decrease = () => {
  inputValue.value -= 1;
  update();
};
</script>

<style scoped lang="scss">
.input {
  width: 70px;
}
</style>
