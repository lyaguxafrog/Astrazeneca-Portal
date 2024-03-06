<template>
  <div class="app">
    <RouterView />

    <v-snackbar
      v-model="shoveNote"
      multi-line
      :color="activeNote?.type === 'error' ? 'error' : undefined"
    >
      <template v-if="activeNote">
        {{ activeNote.text }}
      </template>

      <template v-slot:actions>
        <v-btn color="white" variant="text" @click="shoveNote = false">
          <v-icon icon="mdi-close" />
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script lang="ts" setup>
import { watch, ref } from 'vue';
import { RouterView } from 'vue-router';
import { usePracticumStore } from '@/store/practicum';
import { useSpecialitiesStore } from '@/store/specialities';
import { useNotificationStore, Notification } from '@/store/notification';

const { getSpecialities } = useSpecialitiesStore();
const { getPracticums, init } = usePracticumStore();
const { notifications } = useNotificationStore();

const shoveNote = ref(false);
const activeNote = ref<Notification>();

watch(
  notifications,
  () => {
    if (notifications.value.length) {
      activeNote.value = notifications.value.at(-1);
      shoveNote.value = true;
    }
  },
  {
    deep: true
  }
);

getSpecialities();
</script>

<style scoped lang="scss"></style>
