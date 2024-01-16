<template>
  <div class="app">
    <IEZaglushka />
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { useScreen } from '~/utils/composables/useScreen';
import { useSpecialityStore } from '~/utils/composables/store/speciality';
import { useAuth } from '~/utils/composables/useAuth';
import { useFavourites } from '~/utils/composables/useFavourites';
import IEZaglushka from '~/components/IEZaglushka.vue';

const { initBreakpoints } = useScreen();
const { getSpecialities, init: initSpecialityStore } = useSpecialityStore();
const { checkAccessToken, init: initAuth } = useAuth();
const { getFavourites } = useFavourites();

initBreakpoints();
await initAuth();

await getSpecialities();
await initSpecialityStore();
await checkAccessToken();

await getFavourites();

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
