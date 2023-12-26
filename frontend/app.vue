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
import IEZaglushka from '~/components/IEZaglushka.vue';

const { checkUrlToken } = useAuth();
const { initBreakpoints } = useScreen();
const { getSpecialities } = useSpecialityStore();

const nuxtApp = useNuxtApp();

checkUrlToken();

await getSpecialities();

initBreakpoints();

nuxtApp.hook('page:finish', () => {
  window.scrollTo(0, 0);
});
</script>

<style lang="scss" scoped>
.app {
  overflow-x: hidden;
}
</style>
