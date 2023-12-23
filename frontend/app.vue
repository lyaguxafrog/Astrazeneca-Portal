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
import IEZaglushka from '~/components/IEZaglushka.vue';

const { initBreakpoints } = useScreen();

const nuxtApp = useNuxtApp();

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
