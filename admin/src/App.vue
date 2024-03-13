<template>
  <div class="app" :class="{ loading: isSaving }">
    <RouterView />

    <v-snackbar
      v-model="showNote"
      multi-line
      :close-on-back="false"
      :color="activeNote?.type === 'error' ? 'error' : undefined"
    >
      <template v-if="activeNote">
        {{ activeNote.text }}
      </template>

      <template v-slot:actions>
        <v-btn color="white" variant="text" @click="showNote = false">
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
const { getPracticums, init, isSaving } = usePracticumStore();
const { notifications } = useNotificationStore();

const showNote = ref(false);
const activeNote = ref<Notification>();

watch(
  notifications,
  () => {
    if (notifications.value.length) {
      activeNote.value = notifications.value.at(-1);
      showNote.value = true;
    }
  },
  {
    deep: true
  }
);

getSpecialities();
</script>

<style scoped lang="scss">
.app {
  transition: opacity 0.2s;

  &.loading {
    opacity: 0.5;

    pointer-events: none;
  }
}
</style>
