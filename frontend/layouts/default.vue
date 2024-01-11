<template>
  <div class="default-layout">
    <ClientOnly>
      <NuxtLoadingIndicator color="#00D1FF" :throttle="0" />

      <DefaultGuard />

      <DefaultHeader v-if="!$screen.mdAndDown" />

      <slot />

      <DefaultFooter v-if="!meta.hideFooter" class="default-layout__footer" />
      <DefaultMenu v-if="!meta.hideFooter && specialityId" class="for-mobile-or-tablet" />
    </ClientOnly>
  </div>
</template>

<script lang="ts" setup>
import { toRef } from 'vue';
import { useRouter } from '#app';
import { useScreen } from '~/utils/composables/useScreen';
import { useSpecialityStore } from '~/utils/composables/store/speciality';
import DefaultHeader from '~/components/layout/DefaultHeader.vue';
import DefaultFooter from '~/components/layout/DefaultFooter.vue';
import DefaultGuard from '~/components/layout/DefaultGuard.vue';
import DefaultMenu from '~/components/layout/DefaultMenu.vue';

const $router = useRouter();
const { specialityId } = useSpecialityStore();

const meta = toRef(() => $router.currentRoute.value.meta);

const { $screen } = useScreen();
</script>

<style lang="scss" scoped>
.default-layout {
  display: flex;
  flex-direction: column;

  width: 100vw;
  min-height: 100vh;
  overflow: hidden;

  &__footer {
    margin-top: auto;
  }
}
</style>
