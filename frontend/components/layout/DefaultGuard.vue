<template>
  <div v-if="isShowGuard" ref="scrollEl" class="default-guard">
    <div class="default-guard__content">
      <div class="default-guard__title"><span>PRO</span>Рак Легкого</div>
      <div class="default-guard__subtitle">
        инновационный<br />
        портал для специалистов здравоохранения
      </div>
      <AppButton primary class="default-guard__button" @click="toLogin"> Войти </AppButton>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRoute } from '#app';
import { isClient } from '@vueuse/core';
import { useScreen } from '~/utils/composables/useScreen';
import { disableScroll, enableScroll } from '~/utils/functions/scroll-lock';
import { useAuth } from '~/utils/composables/useAuth';

const { $screen } = useScreen();
const $route = useRoute();

const { toLogin, isAuth } = useAuth();

//const isShowGuard = ref(!isAuth && !$route.query.access_token);
const isShowGuard = ref(false);
const scrollEl = ref();

watch(
  isShowGuard,
  (newValue) => {
    if (newValue) {
      disableScroll(scrollEl.value, $screen.value.mdAndDown);
    } else {
      enableScroll(scrollEl.value, $screen.value.mdAndDown);
    }
  },
  {
    immediate: isClient,
  }
);
</script>

<style scoped lang="scss">
.default-guard {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  @include z-index(7);

  width: 100vw;
  height: 100vh;

  background: rgba(19, 37, 72, 0.7);

  backdrop-filter: blur(32px);

  &__content {
    display: flex;
    flex-direction: column;
    align-items: center;

    max-width: 597px;
    margin: 23vh auto 0;
  }

  &__title {
    font-family: $text-font-family;
    font-size: 102px;
    line-height: 90px;
    font-weight: 500;
    color: $primary-color;
    text-transform: uppercase;
    letter-spacing: 1.02px;

    span {
      color: $accent-color;
    }
  }

  &__subtitle {
    margin-top: 47px;

    font-family: $secondary-font-family;
    font-size: 35px;
    line-height: 37px;
    text-transform: uppercase;
    letter-spacing: -0.35px;
  }

  &__button {
    width: 280px;
    margin-top: 73px;
  }

  @include md-and-down {
    &__content {
      margin: 9.8vh auto 0;
      padding: 0 44px;
    }

    &__title {
      font-size: 51px;
      line-height: 46px;
      letter-spacing: 0.51px;
    }

    &__subtitle {
      margin-top: 35px;

      font-size: 19px;
      line-height: 24px;
    }

    &__button {
      width: auto;
      margin-top: 6.6vh;
    }
  }
}
</style>
