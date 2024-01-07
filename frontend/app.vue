<template>
  <div class="app">
    <IEZaglushka />
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>

<script lang="ts" setup>
import { useScreen } from '~/utils/composables/useScreen';
import { useSpecialityStore } from '~/utils/composables/store/speciality';
import { useAuth } from '~/utils/composables/useAuth';
import { useFavourites } from '~/utils/composables/useFavourites';
import IEZaglushka from '~/components/IEZaglushka.vue';
import { useHistoriesStore } from '~/utils/composables/store/histories';

const { initBreakpoints } = useScreen();
const { getSpecialities, init: initSpecialityStore } = useSpecialityStore();
const { checkAccessToken } = useAuth();
const { getFavourites } = useFavourites();
const { getHistories } = useHistoriesStore();

initBreakpoints();

await getSpecialities();
initSpecialityStore();

await checkAccessToken();
await getFavourites();

onMounted(async () => {
  await getHistories();
});

const nuxtApp = useNuxtApp();

nuxtApp.hook('page:finish', () => {
  window.scrollTo(0, 0);
});
</script>

<style lang="scss" scoped>
.app {
  overflow-x: hidden;
}
</style>
