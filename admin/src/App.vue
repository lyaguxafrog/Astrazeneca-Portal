<template>
  <div class="app">
    <RouterView></RouterView>
  </div>
</template>

<script lang="ts" setup>
import { RouterView } from 'vue-router';
import { useSpecialitiesStore } from '@/store/specialities';

const { getSpecialities } = useSpecialitiesStore();

getSpecialities();
</script>

<style scoped lang="scss"></style>
